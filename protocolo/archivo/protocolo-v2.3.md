# Protocolo de campaña: v2.3 (archivada el 05/11/2026, sustituida por v3.0)

**01/11/2026 · fijado antes de tomar ninguna muestra de campaña.**
El piloto del 28/10 (`data/raw/28-10/`), con sus medidas de laboratorio del 29–30/10, no cuenta como campaña.
Versiones anteriores: [v2.2](protocolo-v2.2.md) · [v2.1](protocolo-v2.1.md) · [v1.0](protocolo-v1.0.md). Versión de campo: [PROTOCOLO_CAMPO.md](PROTOCOLO_CAMPO.md).
Cualquier cambio posterior se añade al registro de cambios (§11), indicando si ya se habían visto datos.

**Cambios principales respecto a la v2.2:**
- un solo lago, el más eutrófico, en varios días;
- sin barca: solo puntos de orilla;
- validación dejando fuera un **día**, en lugar de un lago;
- 3 réplicas por muestra;
- nitrito/nitrato en un subconjunto de muestras;
- nuevo Experimento 2: el modelo congelado se aplica a un lago no visto.

## 1. Objetivos e hipótesis

**O1. ¿Qué puede medir MonoSpectro sin reactivos?**
- **H1a.** Las variables con **señal visible propia** (grupo A) se predicen en **días no vistos** del lago.
- **H1b.** Las variables **sin señal visible** (grupo B) no se predicen. Si alguna lo hace, se interpreta como correlación con la matriz, no como medida.

**O2. ¿Mejora la lectura al añadir el fluorómetro a MonoSpectro?**
- **H2.** El modelo combinado predice mejor que el de solo MonoSpectro las variables del grupo A relacionadas con pigmentos, empezando por la clorofila-a.

**Alcance:**
- El Experimento 1 (§3–6) solo permite concluir sobre **este lago**.
- La generalización a otro lago se prueba aparte, en el Experimento 2 (§7), con el modelo congelado.
- **Nunca se afirmará** que el espectro sin reactivo mide un nutriente.

## 2. Variables de referencia (lo que se intenta predecir)

| Grupo | Variable | Referencia (independiente de MonoSpectro y del fluorómetro) |
|---|---|---|
| A | Clorofila-a (µg/L de lago) | Filtro GF/F → extracción en etanol → espectrofotómetro comercial (ISO 10260, 665/750 nm) |
| A | Color filtrado | Espectrofotómetro comercial, muestra filtrada a 0,2 µm, absorbancia a 440 nm |
| A | Atenuación por partículas | Espectrofotómetro comercial: sin filtrar − filtrada, a 750 nm |
| B | NH₄, PO₄ | Kit Spectroquant en el espectrofotómetro comercial: absorbancia neta = muestra − blanco de reactivo − muestra filtrada sin reactivo, a la λ del kit. **Todas las muestras** |
| B | NO₂ + NO₃ (NOx) | Kit Roche, solo la cubeta con enzima. Absorbancia neta a 540 nm. **Solo en un subconjunto** (§4.3) |
| B | Conductividad específica, pH, O₂ disuelto, temperatura | Sonda Aqua TROLL en el lago, a 0,30 m |
| B (exploratorio) | KH, GH, Fe, SiO₂ | Kit JBL (cribado). Se analizan igual que el grupo B, pero **solo como exploración**: es una lectura de tarjeta de color o por gotas, no una referencia. Rango de tarjeta `a-b` → punto medio. El O₂ y el pH del JBL no se usan: hay sonda |

- Sin patrones no hay curva de calibrado: los kits se expresan en **absorbancia, no en mg/L**. Si llegan patrones o sales (NH₄Cl, KH₂PO₄, KNO₃), se añade una curva sin cambiar nada más.
- Una variable del grupo B con más del 50 % de las muestras por debajo del blanco + 3 desviaciones estándar se declara **no evaluable**.
- El kit JBL es solo cribado: no es referencia.
- **Relación esperable, no es medida:** en un lago eutrófico, la fotosíntesis hace subir de día el O₂ disuelto y el pH junto con la clorofila. Si MonoSpectro "predice" O₂ o pH, se interpreta como asociación vía clorofila (H1b). Como esa relación depende de la hora, la hora de cada muestra se registra siempre, aunque no es variable del modelo.

## 3. Diseño de muestreo (Experimento 1)

- **Lago:** uno, el más eutrófico de los candidatos.
  - Cuál es: **POR CONFIRMAR**. El criterio usado para elegirlo (visual, JBL, clorofila del fluorómetro…) se anota en `map/sites.md` **antes del primer día**.
  - Hace falta permiso escrito.
- **Puntos:** **6–8 puntos de orilla**, repartidos por el perímetro.
  - Se fijan antes del primer día, con coordenadas y foto, y se numeran P1…P8.
  - **Se usan los mismos puntos todos los días.**
  - Sin barca.
- **Días:** **≥ 5 días de muestreo**, separados al menos 2 días entre sí. Fechas: **POR CONFIRMAR**.
- **Muestra** = un punto en un día. **Objetivo: 30–48 muestras; mínimo 30.**
- **Réplicas:** 3 lecturas por muestra en cada instrumento. Se promedian antes del análisis y su dispersión se registra como ruido. Las réplicas **no** cuentan como muestras.

## 4. Procedimiento

### 4.1 En cada punto
1. GPS, hora con desfase (`+01:00`) y foto.
2. Sonda **en el lago** a 0,30 m, 2 min de estabilización.
3. Cubo de plástico sin detergente, enjuagado 3 veces con agua del punto, sin remover el fondo. Anotar la profundidad real.
4. JBL (cribado): **solo en los 2 puntos fijos de NOx** (P1 y el más alejado de P1).
5. **Remover el cubo antes de cada alícuota.** En el piloto, el ruido entre réplicas venía sobre todo de la muestra.
6. MonoSpectro sin filtrar, 3 réplicas.
7. Fluorómetro sin filtrar, con un blanco de agua destilada por réplica, 3 réplicas.
8. Filtro GF/F de un volumen conocido, en aluminio, congelado. **POR CONFIRMAR** que hay GF/F, portafiltros y bomba.
9. **Antes de 15 min:** filtrar por 0,2 µm la porción de nutrientes.
10. Guardar también una porción sin filtrar. Todo a la nevera, a oscuras.

### 4.2 En el laboratorio (empezar antes de 4 h)
1. Espectrofotómetro comercial: cero con agua destilada; espectro completo de la muestra sin filtrar y de la filtrada.
2. MonoSpectro sin filtrar otra vez (efecto del traslado) y filtrada.
3. Kits NH₄ y PO₄ sobre la porción filtrada, según el prospecto.
   - Leer en el **espectrofotómetro comercial** (referencia) y en MonoSpectro (exploratorio).
   - Blancos de reactivo: 5 por kit y día.
4. NOx en el subconjunto (§4.3).
5. Extracción de los GF/F según el protocolo de Daniela y lectura en el espectrofotómetro comercial (ISO 10260). La clorofila calculada por el fluorómetro **no** se usa como referencia.

### 4.3 Nitrito/nitrato reducido (kit Roche)
Protocolo de laboratorio: [`reactivos/nitrito-nitrato_paso-a-paso.md`](../reactivos/nitrito-nitrato_paso-a-paso.md).

**Medida:** solo la cubeta **con enzima** (NOx = nitrito + nitrato). Se ahorran las cubetas de nitrito solo.

**Comprobación del nitrito, solo el día 1:** 1 blanco sin enzima + 1 muestra sin enzima.
- Si la muestra no supera al blanco en más de **0,01 de absorbancia** (umbral propuesto, ≈ límite de detección), el nitrito se considera despreciable y NOx ≈ nitrato.
- Si lo supera, se informa NOx sin separar.

**Cada día:**
- 1 blanco con enzima;
- 2 puntos fijos, que se eligen antes del día 1 y se anotan en `map/sites.md`: P1 y el punto más alejado de P1 por la orilla.

**Control positivo** (agua de la pila 1:5 o KNO₃): el primer día de cada frasco de enzima y el último día de campaña. Si el control no supera claramente al blanco, los NOx de ese día **no son válidos**.

**Presupuesto:**

| Cubetas | Volumen por cubeta | Cubetas del kit | Uso con 5 días | Uso con 6 días |
|---|---|---|---|---|
| Actuales, 10 mm | 3 ml | ~26 | **20** | **23** |
| Semimicro, si se compran antes del día 1 | 1,27 ml | 64 | Se amplía a **todas** las muestras: ~51 cubetas con 6 días | |

**Uso:** con 10–12 muestras, el NOx se informa **solo de forma descriptiva** (rango, relación con la sonda y con los demás kits). No entra en los criterios de §6.

## 5. Variables del modelo (se fijan ahora)

| Instrumento | Variable | Qué mide | Cómo se calcula |
|---|---|---|---|
| MonoSpectro (sin filtrar, media de 3 réplicas) | **1. Nivel** | Cuánta luz quita el agua en total (partículas + color) | Absorbancia media de 420–780 nm |
| | **2–4. Forma** (PC1, PC2, PC3) | Cómo se reparte la absorción por colores: pendiente hacia el azul, bandas… | Espectro interpolado a 420–780 nm cada 5 nm; se resta el desplazamiento (media de 740–780 nm); PCA ajustada **solo con los días de entrenamiento** |
| Fluorómetro (media de 3 réplicas) | **5. Atenuación** | Cuánta luz del LED de 430 nm llega a través de la muestra | −log₁₀(media de muestra/blanco en los canales válidos) |
| | **6. Índice 680** | Fluorescencia de la clorofila | R680 / media(R645, R705), con R = muestra/blanco |

- Canales válidos del fluorómetro: todos menos 410, 435 (saturados por la geometría de 180°) y 485 (ceros intermitentes). Las filas de resumen (`average`, `standard_deviation`) de los archivos de blanco se ignoran.
- **Modelos:**
  - M0, mediana de entrenamiento: línea base;
  - M1, solo MonoSpectro: variables 1–4;
  - M2, solo fluorómetro: variables 5–6;
  - M3, ambos: variables 1–6.
- Todos son ridge lineales con intercepto y α = 1, con escalado ajustado solo con los días de entrenamiento.
- El día, el punto, la hora y las coordenadas no son nunca variables del modelo.

## 6. Validación y criterios del Experimento 1 (fijados antes de ver los datos)

**Validación:** se deja un **día** fuera cada vez (tantos pliegues como días). La unidad es la muestra (punto-día), nunca la réplica.

**Métrica:** habilidad `S = 1 − MAE_modelo / MAE_mediana`, global y por cada día dejado fuera.

| Criterio | Pasa si |
|---|---|
| **O1 · "MonoSpectro mide X en este lago"** (solo grupo A) | M1 con S ≥ 0,25 global **y** S > 0 en ≥ 80 % de los días (4 de 5, 5 de 6…) |
| **O1 · grupo B** | Aunque M1 alcance S ≥ 0,25, se informa como **asociación con la matriz**, nunca como medida |
| **O2 · "el fluorómetro mejora la lectura de X"** | M3 − M1: ΔS ≥ 0,10 global **y** ΔS > 0 en ≥ 80 % de los días. **Variable principal: clorofila-a**; las demás se informan de forma descriptiva |
| **Diseño mínimo** | ≥ 5 días, ≥ 5 muestras válidas por día y ≥ 30 en total. Si no se cumple, los resultados son exploratorios |

Los umbrales (0,25, 0,10, 80 %) son propuestos, no salen de la literatura. Se fijan aquí para no moverlos después.

**Decisiones pendientes (se tomarán con los datos y se registrarán en §11 como tomadas con datos vistos):**
1. Qué hacer con los valores fuera de rango (`<x`, `>x`) cuando son ≤ 50 %. Por defecto, en el script: se excluyen del modelo y se cuentan.
2. El techo del criterio de O2: si M1 ya tiene S cercano a 1, ΔS ≥ 0,10 es imposible. La alternativa es exigir una reducción relativa del error.

Lo que se decida con datos vistos se informa como tal.
Un fallo documentado también es un resultado válido.

## 7. Experimento 2 (posterior): modelo congelado en un lago no visto

1. Al cerrar el Experimento 1, se entrenan M1 y M3 con **todas** sus muestras.
2. Se guardan los coeficientes, el escalado y la PCA en `results/` con fecha, **antes** de medir el lago nuevo. Desde ese momento, **no se reajusta nada**.
3. Lago nuevo: mismo protocolo (§4), ≥ 2 días, ≥ 12 muestras. Qué lago y qué fechas: **POR CONFIRMAR**.
4. **Métrica:** S con la mediana **del propio lago nuevo** como línea base, que es la opción más exigente.
5. **Criterios:**
   - O1 pasa si S ≥ 0,25;
   - O2 pasa si ΔS(M3 − M1) ≥ 0,10, con la clorofila-a como variable principal.
6. Si hay que cambiar algo de este apartado, se hace antes de medir el lago nuevo y se registra en §11.

## 8. Control de calidad

**MonoSpectro, antes del primer punto de cada día:**
- ajustar la exposición hasta que no haya píxeles saturados (cabecera `saturated_columns`);
- poner el reloj en hora;
- medir el **oscuro al empezar la sesión, con la misma exposición**. En el piloto de laboratorio se tomó después y con otra exposición.

**Fluorómetro:** un blanco por réplica.

**Kits:**
- 5 blancos de reactivo por kit y día. En el piloto, la dosis variaba entre cubetas.
- A la absorbancia del kit se resta también la de la muestra filtrada sin reactivo. En el piloto, el fondo del agua era del mismo orden que la señal.

**Exclusión:**
- Se excluye una réplica si falta el archivo, hay valores no finitos o canales válidos saturados.
- Nada se excluye por ser alto, bajo o porque empeore una métrica.
- Toda exclusión se anota con su motivo.

## 9. Datos

- **Carpetas:** `data/raw/DD-MM/<lago>/<punto>/{monospectro,fluorometer,sonda}/<réplica>/`. Hoja `JBL.xlsx` por día. Medidas de laboratorio en `data/raw/DD-MM/reactivos/`.
- **Archivos originales:** sin editar.
- **Celdas:** una celda vacía significa "no medido". Un valor por debajo del límite se escribe `<L`.

## 10. Análisis

- **Piloto:** `src/piloto.py` (control de calidad, una sola muestra).
- **Campaña:** el script se escribe a partir de §5–6 **antes** del primer día de campaña. Si se cambia algo después de ver los datos, se registra en §11.

## 11. Registro de cambios

| Fecha | Cambio | ¿Datos de campaña vistos? |
|---|---|---|
| 2026-09-25 | v1.0 (en inglés) | No |
| 2026-09-27 | Reorganización del repositorio; L02 pasa a Mellaerts | No |
| 2026-09-30 | v2.0: todo el mismo día; kits Spectroquant y Roche; JBL solo como cribado | No |
| 2026-10-20 | Campaña aplazada; registro del desfase horario | No |
| 2026-10-21 | v2.1: piloto sin patrones; sin turbidímetro; clorofila con el fluorómetro propio | No |
| 2026-10-30 | v2.2: objetivos O1/O2; referencias por grupos A y B; variables y criterios fijados; la adición patrón pasa a módulo opcional; control de calidad del piloto | No |
| 2026-11-01 | **v2.3**: un solo lago (el más eutrófico), sin barca, 6–8 puntos de orilla fijos, ≥ 5 días; validación dejando un día fuera; 3 réplicas; NOx solo con enzima y en un subconjunto; resta de la muestra sin reactivo en los kits; oscuro al inicio; Experimento 2 con el modelo congelado. Motivo: logística. Se habían visto solo datos del piloto (un punto, en otro estanque, más las medidas de laboratorio del 29–30/10) | No |
| 2026-11-01 | v2.3 (rev.): JBL (KH, GH, Fe, SiO₂) como grupo B exploratorio; dos decisiones de análisis quedan pendientes y se tomarán con datos (§6) | No |
| 2026-11-04 | v2.3 (rev. 2): JBL solo en los 2 puntos fijos de NOx, por tiempo en campo. Decidido antes del primer día | No |
