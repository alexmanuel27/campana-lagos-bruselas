"""Análisis de la campaña, protocolo v2.3 (§5–6 de protocolo/PROTOCOLO_CONGELADO.md).
Escrito ANTES del primer día de campaña: si se cambia algo después de ver datos, se registra en §11 del protocolo.

Uso: python3 -m src.campana <referencias.csv> <lago> <carpeta_salida> [raíz_raw=data/raw]
referencias.csv (plantilla en templates/referencias_campana.csv): una fila por muestra (fecha DD-MM, punto);
celda vacía = no medido, '<x'/'>x' = fuera del rango del método, 'a-b' (JBL) = punto medio. Los crudos se buscan en <raíz_raw>/<fecha>/<lago>/<punto>/."""
import csv, json, re, sys
from pathlib import Path
import numpy as np
from src.analysis import ridge_predict
from src.piloto import GRID, SENTINEL, mono, fluo

GRUPO_A = ("clorofila_ug_l", "color_a440", "atenuacion_particulas_a750")
GRUPO_B = ("nh4_abs", "po4_abs", "conductividad_us_cm", "ph", "od_mg_l", "temperatura_c")
JBL = ("kh_dkh", "gh_dgh", "fe_mg_l", "sio2_mg_l")  # cribado: grupo B exploratorio, nunca referencia
DESCRIPTIVAS = ("nox_abs",)  # §4.3: subconjunto, no entra en criterios
EXCLUIDOS_NM = (410, 435, 485)  # 410/435 saturados por la geometría de 180°, 485 con ceros intermitentes
MODELOS = {"M1": slice(0, 4), "M2": slice(4, 6), "M3": slice(0, 6)}  # columnas: nivel, PC1-3, atenuación, índice 680
S_O1, DS_O2, FRAC_DIAS = 0.25, 0.10, 0.8
MIN_DIAS, MIN_POR_DIA, MIN_TOTAL = 5, 5, 30


def saturadas(meta):
    return sum(map(int, re.findall(r"\d+", meta.get("saturated_columns", "0"))))


def rasgos_muestra(carpeta, log):
    """Media de réplicas válidas → (nivel, espectro sin desplazamiento en GRID, [atenuación, índice 680]) o None."""
    esp, fl = [], []
    for d in sorted(p for p in (carpeta / "monospectro").glob("*") if p.is_dir()):
        f = [p for p in d.glob("*.csv") if not p.name.startswith(("blank", "dark"))]
        if len(f) != 1:
            log.append(f"{d}: archivo de muestra ausente o duplicado"); continue
        wl, a, meta = mono(f[0])
        if saturadas(meta) or not np.all(np.isfinite(a)):
            log.append(f"{f[0]}: columnas saturadas o valores no finitos"); continue
        esp.append(np.interp(GRID, wl, a))
    for d in sorted(p for p in (carpeta / "fluorometer").glob("*") if p.is_dir()):
        try:
            wls, s, w, _ = fluo(d)
        except (IndexError, KeyError, ValueError) as e:
            log.append(f"{d}: no se pudo leer ({e!r})"); continue
        ok = ~np.isin(wls, EXCLUIDOS_NM)
        with np.errstate(divide="ignore", invalid="ignore"):
            R = s / w
        if np.any(s[ok] >= SENTINEL) or np.any(w[ok] >= SENTINEL) or not np.all(np.isfinite(R[ok])):
            log.append(f"{d}: canal válido saturado o no finito"); continue
        c = {int(x): i for i, x in enumerate(wls)}
        fl.append([-np.log10(R[ok].mean()), R[c[680]] / ((R[c[645]] + R[c[705]]) / 2)])
    if not esp or not fl:
        log.append(f"{carpeta}: sin réplicas válidas de MonoSpectro o del fluorómetro; muestra excluida")
        return None
    m = np.mean(esp, 0)
    return m.mean(), m - m[GRID >= 740].mean(), np.mean(fl, 0)


def matriz(nivel, forma, fl, train):
    """PCA de la forma ajustada solo con el entrenamiento (§5)."""
    mu = forma[train].mean(0)
    vt = np.linalg.svd(forma[train] - mu, full_matrices=False)[2]
    return np.column_stack([nivel, (forma - mu) @ vt[:3].T, fl])


def skill(y, p, base):
    b = np.mean(np.abs(y - base))
    return None if b == 0 else float(1 - np.mean(np.abs(y - p)) / b)


def frac_pos(xs):
    return float(np.mean([x is not None and x > 0 for x in xs]))


def valor(v):
    """'' → None; '<x' o '>x' (fuera del rango del método) → nan; 'a-b' (rango de tarjeta JBL) → punto medio; coma decimal admitida."""
    v = v.replace(",", ".").replace(" ", "")
    if not v:
        return None
    if v[0] in "<>":
        return float("nan")
    a = re.fullmatch(r"([\d.]+)-([\d.]+)", v)
    return (float(a[1]) + float(a[2])) / 2 if a else float(v)


def evaluar(nombre, valores, dias, nivel, forma, fl):
    x = np.array([valor(v) for v in valores], dtype=object)
    medido = np.array([v is not None for v in x])
    fuera = np.array([v is not None and np.isnan(v) for v in x])
    res = {"n_medidas": int(medido.sum()), "n_fuera_de_rango": int(fuera.sum())}
    if medido.sum() == 0:
        return res | {"estado": "sin datos"}
    if fuera.sum() > 0.5 * medido.sum():
        return res | {"estado": "no evaluable (>50 % fuera del rango del método)"}
    ok = medido & ~fuera  # decisión pendiente (§6): por ahora los '<'/'>' (≤50 %) se excluyen del modelo y se cuentan arriba
    y, d = np.array(x[ok], dtype=float), dias[ok]
    if nombre in DESCRIPTIVAS:
        return res | {"estado": "descriptiva (no entra en criterios)", "min": float(y.min()), "max": float(y.max()), "mediana": float(np.median(y))}
    por_dia = {k: int((d == k).sum()) for k in np.unique(d)}
    exploratorio = len(por_dia) < MIN_DIAS or min(por_dia.values()) < MIN_POR_DIA or len(y) < MIN_TOTAL
    if len(por_dia) < 2:
        return res | {"estado": "exploratorio: un solo día, no hay validación"}
    pred = {k: np.full(len(y), np.nan) for k in ("M0", *MODELOS)}
    for k in por_dia:
        te, tr = d == k, d != k
        X = matriz(nivel[ok], forma[ok], fl[ok], tr)
        pred["M0"][te] = np.median(y[tr])
        for m, cols in MODELOS.items():
            pred[m][te] = ridge_predict(X[tr, cols], y[tr], X[te, cols])
    S = {m: skill(y, pred[m], pred["M0"]) for m in MODELOS}
    Sd = {m: {k: skill(y[d == k], pred[m][d == k], pred["M0"][d == k]) for k in por_dia} for m in MODELOS}
    res |= {"muestras_por_dia": por_dia, "diseño_mínimo_cumplido": not exploratorio, "S_global": S, "S_por_dia": Sd}
    s1 = S["M1"] is not None and S["M1"] >= S_O1 and frac_pos(Sd["M1"].values()) >= FRAC_DIAS
    if nombre in GRUPO_A:
        dS = None if None in (S["M1"], S["M3"]) else S["M3"] - S["M1"]
        dSd = [None if None in (Sd["M1"][k], Sd["M3"][k]) else Sd["M3"][k] - Sd["M1"][k] for k in por_dia]
        s2 = dS is not None and dS >= DS_O2 and frac_pos(dSd) >= FRAC_DIAS
        res |= {"O1_MonoSpectro_mide": "PASA" if s1 else "NO PASA", "dS_M3_menos_M1": dS,
                "O2_fluorometro_mejora": ("PASA" if s2 else "NO PASA") + ("" if nombre == "clorofila_ug_l" else " (descriptivo)")}
    else:
        res["O1_grupo_B" + ("_JBL_exploratorio" if nombre in JBL else "")] = "asociación con la matriz (no es medida)" if s1 else "sin asociación"
    if exploratorio:
        res["aviso"] = "diseño mínimo no cumplido: resultado exploratorio (§6)"
    res["predicciones"] = {m: p.round(5).tolist() for m, p in pred.items()} | {"y": y.tolist(), "dia": d.tolist()}
    return res


def main(refs, lago, out, raiz="data/raw"):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    filas = list(csv.DictReader(open(refs, encoding="utf-8")))
    log, keep, R = [], [], []
    for f in filas:
        r = rasgos_muestra(Path(raiz) / f["fecha"] / lago / f["punto"], log)
        if r is not None:
            keep.append(f); R.append(r)
    if len(keep) < 3:
        raise SystemExit(f"Solo {len(keep)} muestras válidas: no se puede analizar. Registro: {log}")
    nivel = np.array([r[0] for r in R]); forma = np.array([r[1] for r in R]); fl = np.array([r[2] for r in R])
    dias = np.array([f["fecha"] for f in keep])
    res = {"protocolo": "v2.3", "lago": lago, "n_muestras": len(keep), "exclusiones": log, "variables": {}}
    for v in (*GRUPO_A, *GRUPO_B, *JBL, *DESCRIPTIVAS):
        if v in keep[0]:
            res["variables"][v] = evaluar(v, np.array([f[v].strip() for f in keep], dtype=object), dias, nivel, forma, fl)
    (out / "resultados.json").write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
    return res


if __name__ == "__main__":
    r = main(*sys.argv[1:5])
    for v, x in r["variables"].items():
        print(v, {k: x[k] for k in x if k not in ("predicciones", "S_por_dia")})
    print(f"Exclusiones: {len(r['exclusiones'])} (ver resultados.json)")
