# Instalación y preparación

## Software

Python 3.10 o superior y NumPy. El análisis no requiere scikit-learn ni servicios externos.

```sh
python3 -m pip install numpy
python3 -m unittest discover -s tests -v
```

Los PDF ya están listos para imprimir y no necesitan generarse en campo. MonoSpectro se instala y calibra según su propio repositorio. Su exportación esperada es CSV con columnas `Pixel`, `Wavelength_nm`, `abs` y cobertura calibrada 420–780 nm. Guardar archivos originales bajo `datos/crudo/` sin editarlos.

## Antes del 2 de octubre

- Confirmar cinco estanques, gestor y condiciones de extracción desde orilla; fijar 15 coordenadas WGS84 y rutas de acceso. La lista de opciones no es autorización.
- Confirmar kits comerciales para ortofosfato, amonio y nitrito: fabricante, SKU, lote, método, especie/unidad reportada, `[L,U]`, longitud de onda, cubeta, tiempo de reacción, plazo de conservación y número de determinaciones. Comprar patrón certificado compatible. Si el kit no da `L`, usar su límite inferior cuantificable declarado, y dejar constancia.
- Confirmar sonda de temperatura, conductividad, pH y oxígeno; turbidímetro; fluorómetro y extracción P1 para clorofila. A254 solo si hay espectrofotómetro UV: MonoSpectro no alcanza 254 nm.
- Preparar cubetas, blancos de reactivo **antes y después** de reaccionar, filtro 0,45 µm, etiquetas, nevera y alícuotas de los cuatro destinos. La longitud de onda útil del kit debe quedar dentro de 430–770 nm para evaluar tres bandas ±10 nm.
- Cambiar la agenda C3 del plan doctoral para respetar el plazo del kit o justificar una conservación validada. Documentar en protocolo y commit.

## Archivos de entrada del análisis

`plantillas/ensayos.csv` tiene 210 filas de diseño. En la copia completada, cada ensayo primario exige `referencia_kit_valor`, `delta_real_mg_l`, `lambda_kit_nm`, `archivo_espectro_sin`, `archivo_espectro_con`, `archivo_blanco_sin` y `archivo_blanco_con`. Las rutas son relativas a `--root`; las dos últimas son los archivos originales del blanco emparejado del mismo lote. El programa resta `(muestra_con - muestra_sin) - (blanco_con - blanco_sin)` y usa la longitud de onda del kit ±10 nm. Los duplicados técnicos quedan para QC y no entran en el ajuste.

El campo `filtrada_045` de ensayos se fija según el kit; medir ambos espectros del par en la misma preparación. El espectro de clorofila usa una alícuota sin filtrar. `plantillas/coanclas.csv` registra color visible filtrado a 440 nm, A254 solo si hay equipo UV, y turbidez de referencia. `plantillas/clorofila.csv` tiene las 15 matrices primarias; la copia completada exige `clorofila_ug_l` y `archivo_espectro_sin`. Si una lectura nativa está bajo `L`, escribir literalmente `<L` en `referencia_kit_valor` (conservar la serie); el análisis la cuenta como censurada sin imputarla. No convertir automáticamente especies químicas (`PO4-P` a `PO4`, etc.); todas las referencias y patrones de cada analito deben usar la misma especie y unidad.

Si se pasa `--campo datos/procesado/campo.csv`, el informe añade modelos de sensores y espectro+sensores sobre muestras nativas, con temperatura, conductividad, pH, oxígeno y turbidez. Antes del análisis cerrar QC según el protocolo. El programa detecta entradas vacías o espectros fuera de rango, pero la revisión del tiempo de conservación, saturación y controles del kit requiere las hojas instrumentales y un registro de exclusiones auditable.
