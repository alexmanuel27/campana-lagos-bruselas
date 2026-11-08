# Campaña lagos de Bruselas · MonoSpectro

¿Puede un espectrómetro visible de bajo coste distinguir la señal real de un nutriente, creada por el reactivo, de una simple correlación con la matriz del agua? Este repo guarda el protocolo, los datos de campo, los espectros y el análisis. El manuscrito va en otro repo.

**Estado (05/11/2026):** piloto del 28/10 analizado. El lago no es accesible por el bajo nivel: el modelo se entrenará en 4 escenarios de acuario (protocolo v3.0) y se probará después en el lago. Fechas POR CONFIRMAR.

## Dónde está cada cosa

| Carpeta | Qué hay |
|---|---|
| `protocolo/` | `PILOTO.md` (piloto del 28/10) · `PROTOCOLO_CAMPO.md` (versión corta) · `PROTOCOLO_CONGELADO.md` (v3.0 explicada) · `protocolo-v2.3.md`, `protocolo-v2.2.md`, `protocolo-v2.1.md` y `protocolo-v1.0.md` (archivadas) |
| `map/` | Los 5 lagos: coordenadas, contactos, permisos, mapa interactivo y PDF |
| `templates/` | Hojas de campo para imprimir (PDF) y CSV vacíos |
| `data/raw/` | Exportes originales de MonoSpectro, el fluorómetro y la sonda, sin tocar. Una carpeta por día (`AAAA-MM-DD/`) |
| `data/processed/` | CSV completados a partir de las plantillas |
| `src/` · `tests/` | Código de análisis y su test |
| `results/` | Resultados (por ahora solo la simulación) |
| `compras/` | Lista de compra |
| `docs/historial/` | Documentos superados, conservados para trazabilidad |

## Flujo de trabajo

1. **Antes de campo:** comprar (`compras/compras.xlsx`), confirmar los permisos (`map/sites.md`) e imprimir las hojas de `templates/`.
2. **En campo, el mismo día:** tomar la muestra, medir los sensores y, en MonoSpectro, el espectro sin reactivo, la reacción con el kit, el espectro con reactivo y la lectura del kit.
3. **Después:**
   - Copiar los exportes de MonoSpectro, sin modificarlos, a `data/raw/`.
   - Pasar las hojas de papel a copias de los CSV de `templates/` en `data/processed/`, sin cambiar las cabeceras ni los identificadores.
4. **Análisis:**

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v        # comprueba que el código funciona
python3 -m src.analysis data/processed/assays.csv \
  --chlorophyll data/processed/chlorophyll.csv \
  --field-log data/processed/field_log.csv \
  --root . --output results/validation.json
```

## Reglas para rellenar los CSV

- Una celda vacía significa "no medido". Nunca se escribe 0 en lugar de un valor que falta.
- Un valor por debajo del límite del kit se escribe `<L` y no se sustituye por un número.
- `sample_id` y `assay_id` no se cambian nunca.
- `actual_delta_mg_l` se calcula a partir del patrón certificado y de los volúmenes pipeteados.
- La especie química se conserva tal cual: `PO4-P` y `PO4` no son lo mismo. Tampoco lo son `NH4-N` y `NH4`, ni `NO2-N` y `NO2`.
- Los espectros sin reactivo y con reactivo de un mismo ensayo tienen que tener la misma condición de filtrado.
- La hora se anota en hora local (`Europe/Brussels`) y las coordenadas en WGS84 decimal.
- Exporte de MonoSpectro: columnas `Pixel`, `Wavelength_nm` y `abs`, dentro del rango calibrado de 420 a 780 nm.

Para regenerar las plantillas: `python3 templates/build_templates.py` (necesita `reportlab`).
