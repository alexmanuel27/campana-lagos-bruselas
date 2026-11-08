"""Fluorometer geometry is 180 deg (transmission): 410/435 nm saturate by design.
Pilot 28/10/2026, Étang des Pêcheries, P1 only (P2/P3 not sampled).
MonoSpectro: spectral SHAPE across 5 replicates (intensity is uncalibrated, so absolute level is not interpreted).
Fluorometer: sample/white ratio per channel.
Usage: python3 -m src.piloto data/raw/28-10/lagos/p1 results/piloto_28-10"""
import csv, glob, io, json, re, sys
from pathlib import Path
import numpy as np

SENTINEL = 4.29e9  # AS7265X reading of 2^32 = saturated/overflow
GRID = np.arange(420, 781, 5.0)


def mono(path):
    rows = list(csv.DictReader(io.StringIO("".join(l for l in open(path) if not l.startswith("#")))))
    meta = dict(l[2:].strip().split(": ", 1) for l in open(path) if l.startswith("# ") and ": " in l)
    wl = np.array([float(r["Wavelength_nm"]) for r in rows])
    return wl, np.array([float(r["abs"]) for r in rows]), meta


def shape(wl, a):
    """Offset removed (mean 740-780 nm) and scaled to unit L2 norm on 420-780 nm."""
    s = np.interp(GRID, wl, a) - a[(wl >= 740) & (wl <= 780)].mean()
    return s / np.linalg.norm(s)


def line_height_675(s):
    b = lambda c: s[np.abs(GRID - c) <= 5].mean()
    return b(675) - (b(650) + b(710)) / 2


def fluo(folder):
    s = list(csv.DictReader(open(glob.glob(f"{folder}/*-spectrum.csv")[0])))
    wpath = glob.glob(f"{folder}/white-reference-*.csv")[0]
    w = [r for r in csv.DictReader(open(wpath)) if r["reading"].isdigit()]  # file ends with average/standard_deviation rows
    wls = [r["wavelength_nm"] for r in s]
    sample = np.array([float(r["mean_intensity"]) for r in s])
    white = np.array([np.mean([float(r[f"{k}_nm"]) for r in w]) for k in wls])
    t = re.search(r"(\d{4}-\d{2}-\d{2})-(\d{2})-(\d{2})-(\d{2})", wpath).groups()
    return np.array(wls, float), sample, white, f"{t[0]} {t[1]}:{t[2]}:{t[3]}"


def main(src, out):
    src, out = Path(src), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    reps = sorted(p for p in (src / "monospectro").iterdir() if p.is_dir())
    S, raw, metas = [], [], []
    for d in reps:
        wl, a, meta = mono(next(p for p in d.glob("*.csv") if not p.name.startswith(("blank", "dark"))))
        S.append(shape(wl, a)); raw.append(np.interp(GRID, wl, a)); metas.append(meta)
    S, raw = np.array(S), np.array(raw)
    X = raw - raw.mean(0); sv = np.linalg.svd(X, compute_uv=False)
    mono_broadband = raw.mean(1)  # mean absorbance 420-780 nm per replicate
    corr = np.corrcoef(S)
    mean_shape = S.mean(0)
    rel_sd = S.std(0, ddof=1) / np.abs(mean_shape).max()  # per-wavelength SD relative to the shape's peak
    lh = np.array([line_height_675(s) for s in S])

    fl = [fluo(d) for d in sorted(p for p in (src / "fluorometer").iterdir() if p.is_dir())]
    fwl = fl[0][0]
    FS = np.array([f[1] for f in fl]); FW = np.array([f[2] for f in fl])
    valid = (FS.max(0) < SENTINEL) & (FW.max(0) < SENTINEL) & (fwl != 485)  # 485 nm: intermittent zero readings
    R = FS / FW
    c = {int(w): k for k, w in enumerate(fwl)}
    fl_index = R[:, c[680]] / ((R[:, c[645]] + R[:, c[705]]) / 2)  # chlorophyll fluorescence adds to 680 only; attenuation is common to all channels
    fl_broadband = -np.log10(R[:, valid].mean(1))  # pseudo-absorbance, mean over valid channels
    r_cross = float(np.corrcoef(mono_broadband, fl_broadband)[0, 1])

    res = {
        "site": "Étang des Pêcheries, P1 (50.813192, 4.412844; iPhone GPS ±33 m)",
        "replicate_times_local": [f[3] for f in fl],  # fluorometer clock; MonoSpectro replicate i taken at the same time
        "monospectro_clock_wrong": [m.get("date") for m in metas],
        "monospectro_saturated_columns": [m.get("saturated_columns") for m in metas],
        "shape_pairwise_r_min": round(float(corr[np.triu_indices(len(S), 1)].min()), 4),
        "shape_pairwise_r_mean": round(float(corr[np.triu_indices(len(S), 1)].mean()), 4),
        "shape_rel_sd_max": round(float(rel_sd.max()), 3),
        "shape_rel_sd_median": round(float(np.median(rel_sd)), 3),
        "line_height_675_normalised": lh.round(4).tolist(),
        "grid_nm": GRID.astype(int).tolist(),
        "mean_shape": mean_shape.round(4).tolist(),
        "monospectro_pca_variance_explained": (sv**2 / (sv**2).sum()).round(4).tolist(),
        "monospectro_mean_abs_420_780": mono_broadband.round(4).tolist(),
        "fluorometer_pseudo_abs": fl_broadband.round(4).tolist(),
        "r_monospectro_vs_fluorometer_broadband": round(r_cross, 3),
        "fluorescence_index_680": fl_index.round(3).tolist(),
        "fluorometer_valid_nm": fwl[valid].astype(int).tolist(),
        "fluorometer_ratio_mean": R.mean(0)[valid].round(3).tolist(),
        "fluorometer_ratio_sd": R.std(0, ddof=1)[valid].round(3).tolist(),
    }
    (out / "resultados.json").write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    for i, s in enumerate(S, 1):
        ax[0].plot(GRID, s, lw=0.8, alpha=0.7, label=f"réplica {i}")
    ax[0].plot(GRID, mean_shape, "k", lw=1.8, label="media")
    ax[0].axvline(675, ls=":", c="g"); ax[0].set_xlabel("nm"); ax[0].set_ylabel("forma (norma L2 = 1)")
    ax[0].set_title("MonoSpectro, P1 sin filtrar: forma del espectro"); ax[0].legend(fontsize=7)
    ax[1].errorbar(fwl[valid], R.mean(0)[valid], yerr=R.std(0, ddof=1)[valid], fmt="o", capsize=3)
    ax[1].axhline(1, c="k", lw=0.8); ax[1].set_xlabel("nm"); ax[1].set_ylabel("muestra / blanco")
    ax[1].set_title("Fluorómetro, canales válidos (media ± DE, n=5)")
    ax[2].scatter(mono_broadband, fl_broadband)
    for i, (x, y) in enumerate(zip(mono_broadband, fl_broadband), 1):
        ax[2].annotate(str(i), (x, y), textcoords="offset points", xytext=(4, 4))
    ax[2].set_xlabel("MonoSpectro: absorbancia media 420–780 nm"); ax[2].set_ylabel("Fluorómetro: −log10(muestra/blanco)")
    ax[2].set_title(f"Atenuación de banda ancha por réplica (r = {r_cross:.2f}, n = 5)")
    fig.tight_layout(); fig.savefig(out / "figura_piloto_p1.png", dpi=150)
    return res


if __name__ == "__main__":
    r = main(*sys.argv[1:3])
    assert len(r["line_height_675_normalised"]) == 5 and abs(np.linalg.norm(r["mean_shape"]) - 1) < 0.1
    print(json.dumps({k: v for k, v in r.items() if k not in ("grid_nm", "mean_shape")}, indent=1, ensure_ascii=False))
