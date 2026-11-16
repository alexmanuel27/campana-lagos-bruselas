# Piloto del 28/10/2026 (datos crudos, sin tocar)

Piloto: no entra en el análisis de la campaña. Análisis en `results/piloto_28-10/` (código: `src/piloto.py`).

| Ruta | Qué es |
|---|---|
| `lagos/p1/monospectro/1…5/` | 5 réplicas independientes del agua del lago (P1): muestra `p1.N.csv` + `blank_*` (+ `dark_*` solo en la 1) |
| `lagos/p1/fluorometer/1…5/` | Las mismas 5 réplicas con el fluorómetro: `p1.N-spectrum.csv`, `p1.N.xls` y la referencia blanca |
| `lagos/p1/sonda/` | Sonda Aqua TROLL (CSV, log y `NOTAS.md`) |
| `reactivos/comercial/` | Kits comerciales leídos en espectrofotómetro de laboratorio: `amonio/`, `fosfato/`, `lago raw/` |
| `reactivos/mono/` | Mismas reacciones leídas en MonoSpectro: `amonio/`, `fosfato/`, `lago RAW/` (con su `blank_*` y `dark_*`) |
| `JBL.xlsx` | Lecturas del kit JBL |
| `IMG_0781.HEIC`, `lagos/p1/IMG_0794.HEIC` | Fotos (contenido sin identificar: POR CONFIRMAR) |

Avisos:
- Los archivos `blank_*` y `dark_*` de MonoSpectro llevan fecha `20260413` en el nombre. Es probable que sea el reloj del equipo y no la fecha de medida: POR CONFIRMAR.
- `fosfato/fosfoto 3.csv` tiene el nombre mal escrito; se deja así para no tocar los crudos.
- En el fluorómetro, los canales 410 y 435 nm salen saturados y el 485 nm da ceros intermitentes. En MonoSpectro, el máximo de la lámpara (697 nm) está saturado en las 5 réplicas.
