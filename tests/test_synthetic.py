"""Pre-field checks: matrix confounding must fail and reagent signal must pass."""
import csv
import tempfile
import unittest
from pathlib import Path

import numpy as np

from src.analysis import GRID, evaluate, evaluate_chlorophyll, load_assays, metrics, ridge_predict


def synthetic(real_signal):
    rows = []
    for lake in range(1, 6):
        for point in range(1, 4):
            pigment = 1.5 + lake * 0.8 + point * 0.13
            baseline = 0.10 + 0.12 * pigment if lake != 5 else 1.2 - 0.12 * pigment
            raw = 0.04 * pigment * np.exp(-((GRID - 665) / 20) ** 2) + 0.015 * pigment * np.exp(-((GRID - 440) / 32) ** 2)
            for level, delta in zip(("0", "2L", "5L", "10L"), (0, 0.1, 0.25, 0.5)):
                coloured = np.array([0.4, 0.6, 0.4]) * (baseline + delta if real_signal else 0.1 * pigment)
                rows.append({"lake_id": f"L{lake:02}", "sample_id": f"L{lake:02}-P{point}", "level_code": level, "actual_delta_mg_l": delta, "reference_value": baseline + delta, "chlorophyll_ug_l": 3 * pigment, "raw": raw.copy(), "coloured": coloured, "sensors": np.array([pigment, 12 + lake])})
    return rows


class SyntheticFalsification(unittest.TestCase):
    def test_matrix_correlation_does_not_survive_spike(self):
        result = evaluate(synthetic(real_signal=False))
        self.assertAlmostEqual(result["all"]["raw_spike_slope"], 0, places=10)
        self.assertAlmostEqual(result["all"]["coloured_spike_slope"], 0, places=10)
        train = [row for row in synthetic(False) if row["lake_id"] != "L05" and row["level_code"] == "0"]
        holdout = [row for row in synthetic(False) if row["lake_id"] == "L05" and row["level_code"] == "0"]
        predicted = ridge_predict([row["raw"] for row in train], [row["reference_value"] for row in train], [row["raw"] for row in holdout])
        baseline = np.repeat(np.median([row["reference_value"] for row in train]), len(holdout))
        self.assertLess(metrics([row["reference_value"] for row in holdout], predicted, baseline)["skill"], 0)

    def test_chlorophyll_is_the_positive_control(self):
        rows = [row for row in synthetic(False) if row["level_code"] == "0"]
        result = evaluate_chlorophyll(rows)
        self.assertGreater(result["all"]["skill"], 0.25)
        self.assertGreaterEqual(sum(value["skill"] > 0 for value in result["by_lake"].values()), 4)

    def test_censored_reference_is_not_imputed(self):
        rows = synthetic(True)
        for row in rows:
            if row["level_code"] == "0" and row["sample_id"].endswith("P1"):
                row["reference_value"] = None
        result = evaluate(rows)
        self.assertEqual(result["all"]["n_censored"], 5)
        self.assertGreater(result["all"]["coloured_spike_slope"], 0.8)

    def test_export_pair_subtracts_reagent_blank(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            raw, blank = np.ones(len(GRID)) * 0.1, np.ones(len(GRID)) * 0.02
            peak = np.exp(-((GRID - 540) / 14) ** 2) * 0.4
            for name, values in [("raw", raw), ("reacted", raw + blank + peak), ("blank0", np.zeros(len(GRID))), ("blank1", blank)]:
                with (root / f"{name}.csv").open("w", newline="") as handle:
                    writer = csv.writer(handle); writer.writerow(["Pixel", "Wavelength_nm", "abs"])
                    writer.writerows((i, wavelength, value) for i, (wavelength, value) in enumerate(zip(GRID, values)))
            columns = ["assay_id", "technical_duplicate", "level_code", "native_spectrum_file", "reacted_spectrum_file", "native_blank_file", "reacted_blank_file", "kit_wavelength_nm", "reference_kit_value", "actual_delta_mg_l", "lake_id", "sample_id", "analyte", "kit_sku", "kit_lot", "reported_species", "reference_kit_unit", "filtered_045_um"]
            with (root / "assays.csv").open("w", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=columns); writer.writeheader()
                writer.writerow({"assay_id":"x", "technical_duplicate":"NO", "level_code":"2L", "native_spectrum_file":"raw.csv", "reacted_spectrum_file":"reacted.csv", "native_blank_file":"blank0.csv", "reacted_blank_file":"blank1.csv", "kit_wavelength_nm":540, "reference_kit_value":0.2, "actual_delta_mg_l":0.1, "lake_id":"L01", "sample_id":"L01-P1", "analyte":"nitrite", "kit_sku":"synthetic", "kit_lot":"lot1", "reported_species":"NO2-N", "reference_kit_unit":"mg/L", "filtered_045_um":"NO"})
            row = load_assays(root / "assays.csv", root)["nitrite"][0]
            np.testing.assert_allclose(row["raw"], raw)
            np.testing.assert_allclose(row["coloured"], peak[[22, 24, 26]])

    def test_reagent_signal_is_recognised_on_unseen_lake(self):
        result = evaluate(synthetic(real_signal=True))
        self.assertAlmostEqual(result["all"]["raw_spike_slope"], 0, places=10)
        self.assertGreater(result["all"]["coloured_all"]["skill"], 0.25)
        self.assertGreater(result["all"]["coloured_spike_slope"], 0.8)
        self.assertLess(result["all"]["coloured_spike_slope"], 1.2)


if __name__ == "__main__":
    unittest.main()
