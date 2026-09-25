# Plantillas de campaña

- `campo.csv`: 20 tomas planificadas (15 puntos primarios y un duplicado de campo P2 por lago). Una fila = una botella independiente. Las celdas vacías son **datos aún no obtenidos**.
- `ensayos.csv`: 210 ensayos planificados (60 niveles por analito en las 15 matrices primarias, más 10 duplicados técnicos por analito). Una fila = una alícuota preparada; exige rutas de los dos espectros y lectura del kit.
- `hoja_campo.pdf`: una página A4 horizontal por lago, para imprimir.
- `hoja_ensayos.pdf`: página A4 horizontal reutilizable, con seis filas para la serie P2 con duplicados. Completar la versión CSV al digitalizar.

Los encabezados CSV son el esquema de datos obligatorio. `muestra_id` y `ensayo_id` no se cambian; `nivel_codigo` es solo el diseño (`0`, `2L`, `5L`, `10L`), **no** un resultado. `delta_real_mg_l` se calcula desde concentración certificada y volúmenes reales. Guardar la especie reportada: `PO4-P` y `PO4` no son la misma unidad de masa, como tampoco `NH4-N` y `NH4` ni `NO2-N` y `NO2`. `lat_wgs84` y `lon_wgs84` son grados decimales con signo; `hora_local` se interpreta en `Europe/Brussels` y se registra con fecha. Si un dato falta, dejar la celda vacía y explicar en `incidencias` / `incidencia_qc`. No poner cero para datos ausentes.

Los archivos originales de MonoSpectro se guardan intactos en `datos/crudo/` y sus rutas relativas se escriben en `archivo_espectro_sin` y `archivo_espectro_con`. No se incluyen aquí espectros ni concentraciones ficticias.
