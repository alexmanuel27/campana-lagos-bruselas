"""Leave-one-lake-out validation and standard-addition falsification for MonoSpectro."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

GRID = np.arange(420.0, 781.0, 5.0)
LEVELS = ("0", "2L", "5L", "10L")


def read_spectrum(path: Path) -> np.ndarray:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    try:
        wavelengths = np.array([float(row["Wavelength_nm"]) for row in rows])
        absorbance = np.array([float(row["abs"]) for row in rows])
    except (KeyError, ValueError) as exc:
        raise ValueError(f"Invalid spectrum: {path}") from exc
    if len(wavelengths) < 2 or not np.isfinite(wavelengths).all() or not np.isfinite(absorbance).all():
        raise ValueError(f"Incomplete or non-finite spectrum: {path}")
    if not (np.diff(wavelengths) > 0).all() or wavelengths[0] > GRID[0] or wavelengths[-1] < GRID[-1]:
        raise ValueError(f"Spectrum lacks increasing 420-780 nm coverage: {path}")
    return np.interp(GRID, wavelengths, absorbance)


def ridge_predict(x_train, y_train, x_test, alpha=1.0):
    """Fit and scale on training data only; do not penalise the intercept."""
    x_train, x_test, y_train = map(lambda value: np.asarray(value, dtype=float), (x_train, x_test, y_train))
    if x_train.ndim != 2 or x_test.ndim != 2 or x_train.shape[1] != x_test.shape[1]:
        raise ValueError("Incompatible feature arrays")
    centre, scale = x_train.mean(axis=0), x_train.std(axis=0)
    scale[scale == 0] = 1
    x, z = (x_train - centre) / scale, (x_test - centre) / scale
    mean = y_train.mean()
    coefficients = np.linalg.solve(x.T @ x + alpha * np.eye(x.shape[1]), x.T @ (y_train - mean))
    return mean + z @ coefficients


def metrics(actual, predicted, baseline):
    actual, predicted, baseline = map(lambda value: np.asarray(value, dtype=float), (actual, predicted, baseline))
    mae = float(np.mean(np.abs(actual - predicted)))
    baseline_mae = float(np.mean(np.abs(actual - baseline)))
    total = float(np.sum((actual - actual.mean()) ** 2))
    return {
        "n": len(actual),
        "mae": mae,
        "bias": float(np.mean(predicted - actual)),
        "r2": None if total == 0 else 1 - float(np.sum((actual - predicted) ** 2)) / total,
        "skill": None if baseline_mae == 0 else 1 - mae / baseline_mae,
    }


def spike_slope(rows, prediction_key):
    """Zero-intercept slope of predicted response against the known spike."""
    groups = {}
    for row in rows:
        levels = groups.setdefault(row["sample_id"], {})
        if row["level_code"] in levels:
            raise ValueError(f"Duplicate level: {row['sample_id']}/{row['level_code']}")
        levels[row["level_code"]] = row
    numerator = denominator = 0.0
    for sample_id, levels in groups.items():
        if set(levels) != set(LEVELS):
            raise ValueError(f"Incomplete standard-addition series: {sample_id}")
        zero = levels["0"][prediction_key]
        for level in LEVELS[1:]:
            delta = levels[level]["actual_delta_mg_l"]
            if delta <= 0:
                raise ValueError(f"Non-positive spike: {sample_id}/{level}")
            numerator += delta * (levels[level][prediction_key] - zero)
            denominator += delta * delta
    return numerator / denominator


def evaluate(rows):
    """Predict held lakes; censored references remain un-imputed."""
    rows = [dict(row) for row in rows]
    lakes = sorted({row["lake_id"] for row in rows})
    if len(lakes) != 5:
        raise ValueError("Leave-one-lake-out requires five lakes")
    held = []
    have_sensors = all("sensors" in row for row in rows)
    for lake in lakes:
        train = [row for row in rows if row["lake_id"] != lake]
        test = [row for row in rows if row["lake_id"] == lake]
        native = [row for row in train if row["level_code"] == "0" and row["reference_value"] is not None]
        quantifiable = [row for row in train if row["reference_value"] is not None]
        if len(quantifiable) < 2 or not test:
            raise ValueError(f"No quantifiable reference in fold: {lake}")
        models = [("coloured", "pred_coloured", quantifiable)]
        if len(native) >= 2:
            models.append(("raw", "pred_raw", native))
            if have_sensors:
                models.extend([("sensors", "pred_sensors", native), ("combined", "pred_combined", native)])
        for feature, prediction_key, subset in models:
            def vector(row):
                return np.r_[row["raw"], row["sensors"]] if feature == "combined" else row[feature]
            predicted = ridge_predict([vector(row) for row in subset], [row["reference_value"] for row in subset], [vector(row) for row in test])
            for row, value in zip(test, predicted):
                row[prediction_key] = float(value)
        raw_baseline = float(np.median([row["reference_value"] for row in native])) if native else None
        coloured_baseline = float(np.median([row["reference_value"] for row in quantifiable]))
        for row in test:
            row["baseline_raw"] = raw_baseline
            row["baseline_coloured"] = coloured_baseline
        held.extend(test)

    def score(part, level, prediction, baseline):
        usable = [row for row in part if (level is None or row["level_code"] == level) and row["reference_value"] is not None and prediction in row]
        return metrics([row["reference_value"] for row in usable], [row[prediction] for row in usable], [row[baseline] for row in usable]) if usable else None

    def summary(part):
        outcome = {
            "n_censored": sum(row["reference_value"] is None for row in part),
            "raw_native": score(part, "0", "pred_raw", "baseline_raw"),
            "coloured_all": score(part, None, "pred_coloured", "baseline_coloured"),
            "raw_spike_slope": spike_slope(part, "pred_raw") if all("pred_raw" in row for row in part) else None,
            "coloured_spike_slope": spike_slope(part, "pred_coloured"),
        }
        if have_sensors:
            outcome["sensors_native"] = score(part, "0", "pred_sensors", "baseline_raw")
            outcome["combined_native"] = score(part, "0", "pred_combined", "baseline_raw")
        return outcome

    return {"all": summary(held), "by_lake": {lake: summary([row for row in held if row["lake_id"] == lake]) for lake in lakes}}


def evaluate_chlorophyll(rows):
    rows = list(rows)
    lakes = sorted({row["lake_id"] for row in rows})
    if len(lakes) != 5:
        raise ValueError("Chlorophyll validation requires five lakes")
    held = []
    for lake in lakes:
        train, test = [row for row in rows if row["lake_id"] != lake], [row for row in rows if row["lake_id"] == lake]
        predicted = ridge_predict([row["raw"] for row in train], [row["chlorophyll_ug_l"] for row in train], [row["raw"] for row in test])
        baseline = float(np.median([row["chlorophyll_ug_l"] for row in train]))
        held.extend((lake, row["chlorophyll_ug_l"], float(value), baseline) for row, value in zip(test, predicted))
    summarise = lambda part: metrics([row[1] for row in part], [row[2] for row in part], [row[3] for row in part])
    return {"all": summarise(held), "by_lake": {lake: summarise([row for row in held if row[0] == lake]) for lake in lakes}}


def load_chlorophyll(path: Path, root: Path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if any(not row["chlorophyll_ug_l"] or not row["native_spectrum_file"] for row in rows):
        raise ValueError("Chlorophyll references or spectra are missing")
    return [{"lake_id": row["lake_id"], "chlorophyll_ug_l": float(row["chlorophyll_ug_l"]), "raw": read_spectrum(root / row["native_spectrum_file"])} for row in rows]


def load_assays(path: Path, root: Path, field_log: Path | None = None):
    sensors = {}
    if field_log:
        with field_log.open(newline="", encoding="utf-8-sig") as handle:
            field_rows = [row for row in csv.DictReader(handle) if row["field_duplicate"] == "NO"]
        columns = ("temperature_c", "conductivity_us_cm", "ph", "dissolved_oxygen_mg_l", "turbidity_value")
        if len({row["turbidity_unit"] for row in field_rows}) != 1:
            raise ValueError("Turbidity units differ between samples")
        for row in field_rows:
            if any(not row[column] for column in columns):
                raise ValueError(f"Incomplete sensor record: {row['sample_id']}")
            sensors[row["sample_id"]] = np.array([float(row[column]) for column in columns])

    data, methods = {}, {}
    required = ("native_spectrum_file", "reacted_spectrum_file", "native_blank_file", "reacted_blank_file", "kit_wavelength_nm", "reference_kit_value", "actual_delta_mg_l", "kit_sku", "kit_lot", "reported_species", "reference_kit_unit", "filtered_045_um")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            if row["technical_duplicate"] == "YES":
                continue
            if row["level_code"] not in LEVELS:
                raise ValueError(f"Invalid level: {row['assay_id']}")
            if any(not row[key] for key in required):
                raise ValueError(f"Missing required measurement: {row['assay_id']}")
            if row["level_code"] == "0" and float(row["actual_delta_mg_l"]) != 0:
                raise ValueError(f"Non-zero unspiked control: {row['assay_id']}")
            if row["filtered_045_um"] not in ("YES", "NO"):
                raise ValueError(f"Invalid filtration value: {row['assay_id']}")
            method = (row["kit_sku"], row["reported_species"], row["reference_kit_unit"], float(row["kit_wavelength_nm"]), row["filtered_045_um"])
            if methods.setdefault(row["analyte"], method) != method:
                raise ValueError(f"Method changes within {row['analyte']}")
            wavelength = float(row["kit_wavelength_nm"])
            if not 430 <= wavelength <= 770:
                raise ValueError(f"Kit wavelength outside useful grid: {row['assay_id']}")
            raw = read_spectrum(root / row["native_spectrum_file"])
            reacted = read_spectrum(root / row["reacted_spectrum_file"])
            blank = read_spectrum(root / row["reacted_blank_file"]) - read_spectrum(root / row["native_blank_file"])
            indices = [int(np.argmin(abs(GRID - (wavelength + offset)))) for offset in (-10, 0, 10)]
            text_value = row["reference_kit_value"].strip()
            record = {"lake_id": row["lake_id"], "sample_id": row["sample_id"], "level_code": row["level_code"], "actual_delta_mg_l": float(row["actual_delta_mg_l"]), "reference_value": None if text_value in ("<L", "<LOQ") else float(text_value), "raw": raw, "coloured": (reacted - raw - blank)[indices]}
            if field_log:
                if row["sample_id"] not in sensors:
                    raise ValueError(f"No sensor record: {row['sample_id']}")
                record["sensors"] = sensors[row["sample_id"]]
            data.setdefault(row["analyte"], []).append(record)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assays_csv", type=Path, nargs="?", help="Completed assays.csv")
    parser.add_argument("--chlorophyll", type=Path, help="Completed chlorophyll.csv")
    parser.add_argument("--field-log", type=Path, help="Completed field_log.csv for sensor ablations")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Root for spectrum paths")
    parser.add_argument("--output", type=Path, default=Path("results/validation.json"))
    args = parser.parse_args()
    if not args.assays_csv and not args.chlorophyll:
        parser.error("Provide assays_csv, --chlorophyll, or both")
    result = {}
    if args.chlorophyll:
        result["chlorophyll_a"] = evaluate_chlorophyll(load_chlorophyll(args.chlorophyll, args.root))
    if args.assays_csv:
        result.update({analyte: evaluate(rows) for analyte, rows in load_assays(args.assays_csv, args.root, args.field_log).items()})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
