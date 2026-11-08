"""Datos sintéticos con el formato real de los archivos: el análisis v2.3 debe detectar una señal real,
no inventar una asociación con ruido y declarar no evaluable lo que está bajo el límite."""
import csv, tempfile, unittest
from pathlib import Path
import numpy as np
from src.campana import main

WL = np.linspace(367, 1067, 450)
FL_NM = [410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940]


def escribir(raiz, rng, dia, punto, chl, saturar=False):
    base = raiz / dia / "LX" / punto
    for r in range(1, 4):
        m = base / "monospectro" / str(r); m.mkdir(parents=True)
        a = 0.01 + 0.004 * chl * np.exp(-((WL - 675) / 15) ** 2) + 0.002 * chl * np.exp(-((WL - 440) / 40) ** 2) + rng.normal(0, 0.0004, WL.size)
        sat = "sample 3, blank 0" if (saturar and r == 1) else "sample 0, blank 0"
        with open(m / f"{punto}.{r}.csv", "w") as f:
            f.write(f"# date: 2026-11-{dia[:2]}T10:00:00\n# saturated_columns: {sat}\nPixel,Wavelength_nm,I_sample,I_blank,I_dark,abs,T_percent\n")
            f.writelines(f"{i},{w:.2f},1,1,0,{x:.5f},100\n" for i, (w, x) in enumerate(zip(WL, a)))
        d = base / "fluorometer" / str(r); d.mkdir(parents=True)
        white = np.where(np.isin(FL_NM, [410, 435]), 4294967296.0, 1000.0)
        samp = white * 0.9 * np.where(np.array(FL_NM) == 680, 1 + 0.01 * chl, 1) * (1 + rng.normal(0, 0.003, len(FL_NM)))
        samp[:2] = 4294967296.0
        with open(d / f"{punto}.{r}-spectrum.csv", "w") as f:
            f.write("wavelength_nm,mean_intensity,standard_deviation,n\n")
            f.writelines(f"{w},{s},0,10\n" for w, s in zip(FL_NM, samp))
        with open(d / f"white-reference-2026-11-{dia[:2]}-10-0{r}-00.csv", "w") as f:
            f.write("reading," + ",".join(f"{w}_nm" for w in FL_NM) + "\n")
            f.writelines(f"{k}," + ",".join(map(str, white)) + "\n" for k in range(1, 4))
            f.write("average," + ",".join(map(str, white)) + "\nstandard_deviation," + ",".join("0" for _ in FL_NM) + "\n")


class Campana(unittest.TestCase):
    def test_sintetico(self):
        rng = np.random.default_rng(1)
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); filas = []
            for dia in ("03-11", "06-11", "09-11", "12-11", "15-11"):
                for p in range(1, 8):
                    chl = rng.uniform(5, 60)
                    escribir(t / "raw", rng, dia, f"p{p}", chl, saturar=(dia == "03-11" and p == 1))
                    filas.append({"fecha": dia, "punto": f"p{p}", "clorofila_ug_l": f"{chl:.2f}", "ph": f"{rng.normal(8, 0.2):.2f}",
                                  "nh4_abs": "<0,05" if p <= 5 else "0,01", "sio2_mg_l": ">6" if p <= 4 else "5", "fe_mg_l": "0,2-0,4", "nox_abs": "0.05" if p in (1, 7) else ""})
            with open(t / "refs.csv", "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
            r = main(t / "refs.csv", "LX", t / "out", t / "raw")
        v = r["variables"]
        self.assertEqual(r["n_muestras"], 35)
        self.assertTrue(any("saturadas" in e for e in r["exclusiones"]))
        self.assertTrue(v["clorofila_ug_l"]["diseño_mínimo_cumplido"])
        self.assertEqual(v["clorofila_ug_l"]["O1_MonoSpectro_mide"], "PASA")
        self.assertEqual(v["ph"]["O1_grupo_B"], "sin asociación")
        self.assertTrue(v["nh4_abs"]["estado"].startswith("no evaluable"))
        self.assertTrue(v["sio2_mg_l"]["estado"].startswith("no evaluable"))
        self.assertEqual(v["fe_mg_l"]["n_medidas"], 35)
        self.assertTrue(v["nox_abs"]["estado"].startswith("descriptiva"))


if __name__ == "__main__":
    unittest.main()
