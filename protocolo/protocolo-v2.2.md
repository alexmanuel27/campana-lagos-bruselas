# Protocolo de campaña: v2.2 (archivada el 01/11/2026, sustituida por v2.3)

**30/10/2026 · fijado antes de tomar ninguna muestra de campaña.** El piloto del 28/10 (`data/raw/28-10/`) no cuenta como campaña.
Versiones anteriores: [v2.1](protocolo-v2.1.md) · [v1.0](protocolo-v1.0.md). Versión de campo: [PROTOCOLO_CAMPO.md](PROTOCOLO_CAMPO.md).
Cualquier cambio posterior se añade al registro de cambios (§10), indicando si ya se habían visto datos.

## 1. Objetivos e hipótesis

**O1. ¿Qué puede medir MonoSpectro sin reactivos?**
- **H1a.** Las variables con **señal visible propia** (grupo A) se predicen en un lago no visto.
- **H1b.** Las variables **sin señal visible** (grupo B) no se predicen en un lago no visto. Si alguna lo hace dentro de los lagos medidos, es correlación con la matriz, no medida.

**O2. ¿Mejora la lectura al añadir el fluorómetro a MonoSpectro?**
- **H2.** El modelo combinado predice mejor que el de solo MonoSpectro las variables del grupo A relacionadas con pigmentos, empezando por la clorofila-a.
- **No se espera mejora en el grupo B.** Si aparece, se interpreta como correlación con la matriz.

**Nunca se afirmará** que el espectro sin reactivo mide un nutriente.

## 2. Variables de referencia (lo que se intenta predecir)

| Grupo | Variable | Referencia (independiente de MonoSpectro y del fluorómetro) |
|---|---|---|
| A | Clorofila-a (µg/L de lago) | Filtro GF/F → extracción en etanol → espectrofotómetro comercial (ISO 10260, 665/750 nm) |
| A | Color filtrado | Espectrofotómetro comercial, muestra filtrada a 0,2 µm, absorbancia a 440 nm |
| A | Atenuación por partículas | Espectrofotómetro comercial: sin filtrar − filtrada, a 750 nm |
| B | NH₄, NO₂, PO₄ | Kit (Spectroquant / Roche) leído en el espectrofotómetro comercial: **absorbancia neta** (muestra − blanco de reactivo) a la λ del kit. Sin patrones no hay curva de calibrado: se trabaja en absorbancia, no en mg/L |
| B | Conductividad específica, pH, O₂ disuelto, temperatura | Sonda Aqua TROLL en el lago, a 0,30 m |

- Ninguna referencia se mide con los instrumentos que se evalúan.
- Una variable del grupo B con más del 50 % de las muestras por debajo del blanco + 3 desviaciones estándar se declara **no evaluable**. En el piloto, los nutrientes salieron por debajo del límite del JBL.
- El kit JBL es solo cribado: no es referencia.

## 3. Diseño de muestreo

- **Lagos:** los 5 de [map/sites.md](../map/sites.md), con permiso escrito, un lago por día. Fechas: POR CONFIRMAR.
- **Puntos principales:** 3 por lago (P1 entrada, P2 medio, P3 salida), con el juego completo de medidas. **Son los que entran en el análisis principal (15 muestras).**
- **Puntos extra (opcionales, con el bote):** solo sonda + MonoSpectro + fluorómetro, sin extracción ni kits. Son exploratorios y no entran en los criterios de §6.
- **Réplicas:** 5 lecturas por muestra en cada instrumento. Se promedian antes del análisis y su dispersión se registra como ruido.

## 4. Procedimiento

**En cada punto:**
1. GPS, hora con desfase (`+01:00` desde el 25/10) y foto.
2. Sonda **en el lago** a 0,30 m, 2 min de estabilización.
3. Cubo de plástico sin detergente, enjuagado 3 veces con agua del punto, sin remover el fondo. Anotar la profundidad real.
4. JBL (cribado).
5. MonoSpectro sin filtrar, 5 réplicas.
6. Fluorómetro sin filtrar, con un blanco de agua destilada por réplica, 5 réplicas.
7. Filtro GF/F de un volumen conocido, en aluminio, congelado.
8. **Antes de 15 min:** filtrar por 0,2 µm la porción de nutrientes.
9. Guardar también una porción sin filtrar. Todo a la nevera, a oscuras.

**En el laboratorio (empezar antes de 4 h):**
1. Espectrofotómetro comercial: blanco de agua destilada; muestra sin filtrar y filtrada (440 y 750 nm, espectro completo si es posible).
2. MonoSpectro sin filtrar otra vez (efecto del traslado) y filtrada.
3. Kits sobre la porción filtrada, según el prospecto. Leer en el **espectrofotómetro comercial** (referencia) y en MonoSpectro (exploratorio). Blancos de reactivo: 5 por kit y día.
4. Extracción de los GF/F según el protocolo de Daniela, y lectura en el espectrofotómetro comercial (ISO 10260). El fluorómetro puede leer los extractos, pero su clorofila **no** se usa como referencia hasta corregir su calibración.

**Si llegan los patrones antes de la campaña:** se añade el test de adición patrón de la v2.1 (§6.3–6.5 y criterios de su §10) como módulo adicional, sin cambiar nada de lo anterior.

## 5. Variables del modelo (se fijan ahora)

| Instrumento | Variables | Cómo se calculan |
|---|---|---|
| MonoSpectro (muestra sin filtrar, media de 5 réplicas) | **Nivel:** absorbancia media 420–780 nm. **Forma:** 3 primeras componentes principales (PCA) del espectro sin el desplazamiento | Interpolado a 420–780 nm cada 5 nm; desplazamiento = media de 740–780 nm; PCA ajustada **solo con los datos de entrenamiento** de cada pliegue |
| Fluorómetro (media de 5 réplicas) | **Atenuación:** −log₁₀(media de muestra/blanco en los canales válidos). **Fluorescencia:** índice R680 / media(R645, R705) | Canales válidos: todos menos 410, 435 (saturados por la geometría de 180°) y 485 (ceros intermitentes). Las filas de resumen de los archivos de blanco se ignoran |

**Modelos para cada variable de referencia:**
- M0, mediana de entrenamiento: línea base.
- M1, solo MonoSpectro: 4 variables.
- M2, solo fluorómetro: 2 variables.
- M3, MonoSpectro + fluorómetro: 6 variables.

Todos son ridge lineales con intercepto y α = 1, con escalado ajustado solo con los datos de entrenamiento. El ID del lago, la hora y las coordenadas no son nunca variables del modelo.

## 6. Validación y criterios (fijados antes de ver los datos)

**Validación:** se deja un lago fuera cada vez (5 pliegues). La unidad es el punto de muestreo, nunca la réplica.

**Métrica:** habilidad `S = 1 − MAE_modelo / MAE_mediana`, global y por cada lago dejado fuera.

| Criterio | Pasa si |
|---|---|
| **O1 · "MonoSpectro mide X"** (solo grupo A) | M1 con S ≥ 0,25 global **y** S > 0 en ≥ 4 de los 5 lagos |
| **O1 · grupo B** | Aunque M1 alcance S ≥ 0,25, se informa como **asociación con la matriz**, nunca como medida |
| **O2 · "el fluorómetro mejora la lectura de X"** | M3 − M1: ΔS ≥ 0,10 global **y** ΔS > 0 en ≥ 4 de los 5 lagos. **Variable principal: clorofila-a**; las demás se informan de forma descriptiva |
| **Diseño mínimo** | ≥ 4 lagos con ≥ 2 puntos válidos y ≥ 10 muestras válidas. Si no, los resultados son exploratorios |

Con 15 muestras, ningún resultado se presenta como generalizable fuera de estos estanques. Un fallo documentado también es un resultado válido.

## 7. Control de calidad (aprendido en el piloto)

- **MonoSpectro:**
  - ajustar la exposición hasta que no haya píxeles saturados (cabecera `saturated_columns`) antes del primer punto de cada día;
  - poner el reloj en hora;
  - medir un oscuro (dark) por sesión.
- **Fluorómetro:** un blanco por réplica.
- **Exclusión:** se excluye una réplica si falta el archivo, hay valores no finitos o canales válidos saturados. Nada se excluye por ser alto, bajo o porque empeore una métrica. Toda exclusión se anota con su motivo.

## 8. Datos

- **Carpetas:** `data/raw/DD-MM/<lago>/<punto>/{monospectro,fluorometer}/<réplica>/`, como en el piloto. Hoja `JBL.xlsx` por día.
- **Archivos originales:** sin editar.
- **Celdas:** una celda vacía significa "no medido". Un valor por debajo del límite se escribe `<L`.

## 9. Análisis

- **Piloto:** `src/piloto.py` (control de calidad, una sola muestra).
- **Campaña:** el script se escribe a partir de §5–6 **antes** del primer día de campaña. Si se cambia algo después de ver los datos, se registra en §10.

## 10. Registro de cambios

| Fecha | Cambio | ¿Datos de campaña vistos? |
|---|---|---|
| 2026-09-25 | v1.0 (en inglés) | No |
| 2026-09-27 | Reorganización del repositorio; L02 pasa a Mellaerts | No |
| 2026-09-30 | v2.0: todo el mismo día; kits Spectroquant y Roche; JBL solo como cribado | No |
| 2026-10-20 | Campaña aplazada; registro del desfase horario | No |
| 2026-10-21 | v2.1: piloto sin patrones; sin turbidímetro; clorofila con el fluorómetro propio | No |
| 2026-10-30 | **v2.2**: nuevos objetivos O1 (qué mide MonoSpectro sin reactivos) y O2 (si el fluorómetro mejora la lectura); referencias independientes por grupos A y B; variables y criterios fijados; la adición patrón pasa a módulo opcional; control de calidad del piloto del 28/10 (solo se vieron datos de un punto del piloto, en otro estanque que no es de la campaña) | No |
