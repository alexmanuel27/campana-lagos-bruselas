# Protocolo de campaña: versión 2.0, explicada

**Versión 2.0 · 30/09/2026 · redactada antes de tomar ninguna muestra de campaña.**

- Sustituye a la v1.0 del 25/09/2026, archivada sin cambios en [docs/protocolo-v1.0.md](docs/protocolo-v1.0.md).
- La versión corta para llevar al campo está en [PROTOCOLO_CAMPO.md](PROTOCOLO_CAMPO.md).
- Todo lo marcado **POR CONFIRMAR** debe cerrarse antes del piloto.
- Cualquier cambio posterior se añade al registro de cambios (§13), indicando si ya se habían visto datos de campaña.

---

## 0. Qué cambia respecto a la v1.0

| Tema | v1.0 | v2.0 | Motivo |
|---|---|---|---|
| Cuándo se mide | Espectros y kits entre 1 y 3 semanas después de la toma | **Todo el mismo día.** En el lago: toma, sensores, filtración y kit visual. En el laboratorio: reacciones y espectros, en menos de 4 h | El nitrito y el ortofosfato solo aguantan 48 h, y la clorofila cambia en horas |
| Referencia de nutrientes | Kit fotométrico aún sin elegir | Merck Spectroquant (fosfato y amonio) y Roche (nitrito/nitrato), leídos en el espectrofotómetro de laboratorio | Kits definidos en la lista de compra |
| Kit visual | No existía | JBL ProAquaTest Lab: solo cribado en campo, **no es referencia** | JBL no publica su química; no se puede defender como referencia en el artículo |
| Patrones | Certificados, comprados | Los prepara Daniela a partir de sales secas | Decisión del equipo |
| Filtración | 0,45 µm | 0,2 µm, acetato de celulosa | Filtros comprados |
| L02 | Estanques de Ixelles | Grand étang Mellaerts | En Ixelles está prohibido pisar la orilla |
| Nitrato | No se medía | Se mide como variable de contexto (kit Roche). **No entra en el test de adición** | El kit Roche mide nitrito y nitrato |

El diseño del test, el modelo, las métricas y los criterios de fallo (§9–§10) **no cambian**.

---

## 1. Qué se quiere demostrar y qué no se puede afirmar

1. **Control positivo (clorofila-a).** La clorofila absorbe en el visible (~665–680 nm). Si el espectro de MonoSpectro sin reactivo no predice la clorofila medida por extracción y fluorómetro en un lago no visto, el instrumento no sirve como sensor visible. En ese caso no se afirma nada sobre nutrientes.
2. **Control de matriz.** El nitrito, el amonio y el ortofosfato **no absorben en el visible**. Un modelo que los "prediga" desde el espectro sin reactivo lee la correlación con pigmentos, color o turbidez.
   - La adición patrón lo delata: se añade analito incoloro, la concentración sube y el espectro sin reactivo no cambia.
   - La pendiente de respuesta del modelo sin reactivo (`b_nativo`) debe salir ≈ 0.
3. **Señal química.** Después de añadir el reactivo aparece color proporcional al analito. Si el modelo sobre el espectro con reactivo responde a la adición con `b ≈ 1` en lagos no vistos, MonoSpectro + kit miden ese analito. Ese es el resultado publicable.

**Nunca se afirmará** que el espectro sin reactivo detecta un nutriente. La absorbancia filtrada a 440 nm se llama "color visible filtrado", no CDOM ni A254.

---

## 2. Lagos, estaciones y profundidad

| ID | Lago | Centro de planificación (WGS84) | Gestor |
|---|---|---|---|
| L01 | Bois de la Cambre | 50.804436, 4.378577 | Ciudad de Bruselas |
| L02 | Grand étang Mellaerts | 50.827675, 4.434544 | Bruxelles Environnement |
| L03 | Parc Léopold | 50.838056, 4.378611 | Ciudad de Bruselas |
| L04 | Square Marie-Louise | 50.846836, 4.379034 | Ciudad de Bruselas |
| L05 | Parc d'Osseghem | 50.895473, 4.346072 | Ciudad de Bruselas |

- **Permiso de toma de agua:** POR CONFIRMAR en los cinco lagos. Sin permiso escrito no se toma agua. Detalle y contactos en [map/sites.md](map/sites.md).
- **Estaciones:** tres por lago.
  - P1, cerca de la entrada de agua.
  - P3, cerca de la salida.
  - P2, entre ambas.
  - Si no se identifican entrada y salida: P1 en el extremo norte accesible, P3 en el sur y P2 en el medio. Se anota la regla usada.
  - Separación ≥ 30 m si la forma del lago lo permite.
- **Profundidad:** 0,30 m bajo la superficie, desde la orilla y sin entrar en el agua.
  - Si la profundidad total es < 0,50 m, se toma a media columna, al menos a 0,10 m del sedimento.
  - Si no es posible, la estación se marca como inválida.
- **Diseño:** 15 muestras primarias (5 × 3) más un duplicado de campo en P2 por lago.
- **No se cambia de lago** una vez vistos datos de campaña.

**Por qué 0,30 m y desde la orilla:** es reproducible entre lagos, no requiere barca y no infringe la prohibición de entrar en el agua de los parques.

---

## 3. Equipos, reactivos y patrones

### 3.1 Equipos disponibles (confirmado por Alex, 30/09)

| Equipo | Uso |
|---|---|
| MonoSpectro (420–780 nm calibrado) | Espectros sin reactivo y con reactivo |
| Sonda multiparámetro | Temperatura, conductividad, pH y O₂ disuelto in situ |
| Turbidímetro | Turbidez de cada muestra |
| Fluorómetro + material de extracción | Referencia de clorofila-a (método de P1, Daniela) |
| Pipetas y material de laboratorio | Micropipetas, puntas, matraces aforados, agua destilada, cubetas de 10 mm, botellas |
| **Espectrofotómetro de laboratorio** (el "comercial" de P1) | **Lectura de referencia de los kits.** **POR CONFIRMAR** que está disponible esa semana y que llega a 540 y 690 nm |

### 3.2 Reactivos (lista de compra)

| Analito | Kit | Química | λ de lectura | Rango del fabricante | Tests |
|---|---|---|---|---|---|
| Ortofosfato | Merck Spectroquant 1.14848 | Azul de fosfomolibdeno (molibdato + ácido ascórbico en medio ácido) | **POR CONFIRMAR** en el prospecto | 0,0025–5,00 mg/L PO₄-P | 220 |
| Amonio | Merck Spectroquant 1.14752 | Azul de indofenol (tipo Berthelot) | 690 nm (Merck) | 0,010–3,00 mg/L NH₄-N | 250 |
| Nitrito (+ nitrato) | Roche 11746081001 | Griess (sulfanilamida + NED); el nitrato se mide tras reducirlo con nitrato reductasa | ~540 nm, **POR CONFIRMAR** | 0,02–5,00 mg/L | **~64 ensayos: NO alcanza** (ver §12) |
| Cribado visual | JBL ProAquaTest Lab | Gotas + comparador; química no publicada | — | Según tarjeta | 1 maletín |

- **Límite de trabajo de cada kit:** la λ de lectura debe estar dentro de 430–770 nm. Si un kit no cumple, ese analito se declara "no evaluable con MonoSpectro".
- **Qué es L:** el límite inferior de cuantificación del kit **para cubeta de 10 mm**, tomado del prospecto. **POR CONFIRMAR** para los tres kits.
- **Filtros:** acetato de celulosa de 0,2 µm (comprados). Se anota en cada ensayo.

### 3.3 Patrones (los prepara Daniela)

- **Sales:** KH₂PO₄ (fosfato), NH₄Cl (amonio) y NaNO₂ (nitrito), de grado analítico, secadas y pesadas.
  - **POR CONFIRMAR:** que el laboratorio tiene las tres sales, con lote y pureza anotados.
- **Madre:** 1000 mg/L, expresada **en la misma forma química que informa el kit**. PO₄-P para el fosfato, NH₄-N para el amonio y la forma que informe el kit Roche para el nitrito (POR CONFIRMAR).
  - Se anotan la masa pesada, el volumen del matraz, la fecha y quién la prepara.
- **Trabajo:** diluciones preparadas **cada día** a partir de la madre, para que el pipeteo de 2L, 5L y 10L sea de volúmenes ≥ 10 µL.
- **Patrón de control independiente:** una segunda pesada, preparada por separado. Sustituye al control certificado de la v1.0.
  - Se lee cada día.
  - Debe recuperar entre el 80 y el 120 %.

**Por qué el control independiente:** los patrones no son certificados. Un error de pesada afectaría por igual a la adición y a la curva de calibrado, y ese error no se vería. La segunda pesada independiente lo detecta.

---

## 4. Organización de la semana

Se muestrea **un lago por día**, del 5 al 9 de octubre. El orden es POR CONFIRMAR, según lleguen los permisos.

| Momento | Dónde | Quién | Qué |
|---|---|---|---|
| Antes de salir | Laboratorio | Ambos | Calibrar la sonda y el turbidímetro. Preparar las diluciones de trabajo. Etiquetar tubos y botellas. Nevera con acumuladores |
| Mañana (~2–3 h) | Lago | Ambos | Estaciones P1–P3, sensores, toma, filtración inmediata, filtros de clorofila y cribado JBL (§5) |
| Traslado | — | — | Nevera a ~4 °C y a oscuras. Se anota la hora |
| Tarde (empezar en < 4 h desde la toma) | Laboratorio | Alex: MonoSpectro · Daniela: reacciones y referencia | Espectros, adiciones, reacciones y lecturas (§6) |
| Final del día | Laboratorio | Ambos | Copiar los archivos crudos a `data/raw/AAAA-MM-DD/`. Revisar que no falta nada |

**Por qué "el mismo día" y no "en la orilla":**

- El kit necesita una lectura de referencia en un espectrofotómetro estable. Las reacciones se hacen sobre la mesa, con tiempos exactos.
- El ortofosfato debe filtrarse al momento, y eso se hace en la orilla (§5.4).
- Con las reacciones empezando en menos de 4 h se queda muy dentro de las 48 h de conservación de la EPA para el nitrito y el ortofosfato.

**Carga diaria:** 3 estaciones × 3 analitos × 4 niveles = 36 reacciones, más 6 duplicados técnicos en P2, más blancos y controles.

---

## 5. En el lago (paso a paso)

1. **Llegada.** Se anotan fecha, hora local, tiempo atmosférico, operador y las coordenadas WGS84 de cada estación. Se fotografía cada punto de toma.
2. **Sensores in situ,** en cada estación y a 0,30 m: temperatura, conductividad, pH y O₂ disuelto. Se anotan el ID de la sonda y la hora de su calibración de esa mañana.
3. **Toma.** La botella se enjuaga 3 veces con agua del lago y se llena a 0,30 m. En P2 se toma además una **segunda botella independiente** como duplicado de campo (`Lxx-P2-DUP`).
4. **Reparto inmediato de cada botella**, siempre con etiqueta `Lxx-Py-<destino>`:

   | Alícuota | Qué se hace | Por qué |
   |---|---|---|
   | A · sin filtrar | A la nevera, a oscuras | Espectro sin reactivo para la clorofila (§6.2) y turbidez |
   | B · clorofila | Filtrar un volumen conocido por GF/F. Doblar el filtro, envolverlo en aluminio y congelarlo | Referencia de clorofila (extracción y fluorómetro de Daniela) |
   | C · nutrientes | **Filtrar por 0,2 µm en la orilla, en menos de 15 min.** A tubos limpios, en frío y a oscuras | Fracción disuelta. La filtración inmediata frena el consumo biológico de nutrientes |
   | D · PlanktoScope | Según el protocolo de P2 | Destino compartido |
   | E · reserva Cruz | Conservación según el plan | Validación del prototipo |

   **Volumen de C:** tiene que cubrir los 4 niveles de los 3 analitos, más los duplicados de P2, los blancos de muestra y un 30 % de reserva. **POR CONFIRMAR** cuando se conozca el volumen de muestra por ensayo de cada prospecto.
5. **Turbidez:** se mide sobre la alícuota A, en el turbidímetro, y se anota la unidad.
6. **Cribado JBL** (NH₄, NO₂, NO₃, PO₄), sobre la alícuota C.
   - Se anota el valor de la tarjeta.
   - **No es referencia.** Solo sirve para saber de antemano si alguna muestra va a salir del rango del kit y habrá que diluirla, y como respaldo si falla la referencia.
   - Los residuos van a la garrafa de residuos, nunca al lago.
7. **Salida.** Se anota la hora de la última toma.

---

## 6. En el laboratorio (el mismo día)

### 6.1 Arranque (cada día)

- **MonoSpectro:** encendido y estabilizado. Se registran la calibración de longitud de onda y el blanco de agua destilada en cubeta de 10 mm.
- **Espectrofotómetro de referencia:** curva de calibrado de cada analito con un blanco y 5 patrones de trabajo, de 0 a ≥ 10L. Se lee además el **control independiente**.
- **Cuándo se invalida el día para un analito:**
  - si el control no recupera entre el 80 y el 120 %;
  - si el blanco de reactivo es ≥ L.
  - En ambos casos se repite el calibrado antes de seguir.

### 6.2 Clorofila: espectro sin reactivo

- La alícuota A se agita suavemente y se lee en MonoSpectro, en cubeta de 10 mm, **sin filtrar**.
- Los filtros GF/F pasan a Daniela para la extracción y el fluorómetro, según el protocolo de P1.
- El valor obtenido va a `chlorophyll.csv` junto a la ruta del espectro.

### 6.3 Series de adición (para cada estación y cada analito)

1. Se preparan 4 tubos con el **mismo volumen de muestra filtrada** (alícuota C).
2. Se añade patrón de trabajo para subir la concentración en **0, 2L, 5L y 10L**.
3. **Se enrasan los 4 tubos al mismo volumen final.** En el tubo 0 se añade agua destilada en lugar de patrón.
   - **Por qué:** si el tubo con más patrón quedara más diluido, su espectro sin reactivo bajaría y el modelo "respondería" por dilución, no por analito.
4. En P2 se preparan además **duplicados técnicos** independientes de 0 y 10L.
5. Se anotan: el lote del patrón, su concentración, cada volumen pipeteado, el volumen final y el incremento calculado (`actual_delta_mg_l`).

### 6.4 Espectro sin reactivo de cada tubo

Cada tubo se lee en MonoSpectro **antes** de añadir el reactivo y se guarda el CSV original. Es el espectro "native" del ensayo.

### 6.5 Reacción, espectro con reactivo y referencia

1. Se añade el reactivo **según el prospecto** del kit: volúmenes, orden y tiempo de reacción exactos. Se anotan la hora de inicio y la temperatura.
2. Cumplido el tiempo de reacción, **la misma cubeta**:
   1. se lee en MonoSpectro (espectro "reacted");
   2. **inmediatamente después**, se lee en el espectrofotómetro de referencia a la λ del kit. Esa lectura, pasada por la curva del día, es `reference_kit_value`.
3. Por cada lote de reactivo y día se hace un **blanco de reactivo** con agua destilada, leído sin reactivo y con reactivo en MonoSpectro.
4. Una cubeta con restos de reactivo no se reutiliza sin haberla lavado.

### 6.6 Nitrato (solo contexto)

Con el kit Roche, sobre la muestra sin enriquecer de cada estación. Se anota como variable de contexto. No entra en el test de adición ni en el análisis preregistrado.

---

## 7. Registro de datos

- **Hojas de campo:** `templates/field_log.pdf` y `templates/assays.pdf`. Se pasan a los CSV de `templates/` y se guardan en `data/processed/`, sin cambiar las cabeceras ni los identificadores.
- **Archivos de MonoSpectro:** en `data/raw/AAAA-MM-DD/`, sin editar. Nombre: `Lxx-Py-<analito>-<nivel>_native.csv` y `..._reacted.csv`; los blancos, `BLK-<analito>-<lote>_native.csv`.
- **Datos que faltan:** una celda vacía significa "no medido". Un valor por debajo del límite del kit se escribe `<L`. Nunca se pone 0 en lugar de un dato que falta.
- **Hora:** hora local de Bruselas.
- **Forma química:** se conserva la que informa el kit (`PO4-P`, `NH4-N`, `NO2-N` / `NO2`).

---

## 8. Control de calidad y exclusiones

**Se excluye un espectro** si:
- falta el archivo original;
- el eje de longitud de onda no está calibrado o no es monótono;
- hay valores no finitos;
- el detector está saturado;
- o su blanco es inválido.

**Se excluye una serie** si:
- el patrón está caducado o mal preparado;
- falta algún volumen;
- la referencia está fuera del rango del kit;
- la reacción se hizo fuera del tiempo del prospecto;
- o la reacción empezó **más de 8 h después de la toma**.

**Se invalida un lote analítico del día** si el blanco de reactivo es ≥ L o si el control independiente queda fuera del 80–120 %.

**Duplicados técnicos (10L):** deben coincidir dentro del ±20 % de su media. Si no coinciden, se invalida esa serie de lago y analito, salvo que pueda repetirse el mismo día.

Nada se excluye por ser alto, bajo o porque empeore una métrica. Todo lo excluido queda registrado con su motivo.

---

## 9. Análisis (sin cambios respecto a la v1.0)

- **Unidad independiente:** la estación. Nunca el espectro ni la alícuota.
- **Validación principal: dejar un lago fuera.** Todo el lago retenido queda fuera del ajuste, del escalado y de la selección.
- **Modelo:** regresión ridge lineal con intercepto, α = 1,0. Escalado solo con los datos de entrenamiento. Espectros interpolados a 420–780 nm cada 5 nm.
- **Qué entra en cada modelo:**
  - Clorofila y nutrientes "sin reactivo": el espectro sin reactivo.
  - Nutrientes "con reactivo": `(con reactivo − sin reactivo) − (blanco con reactivo − blanco sin reactivo)` a la λ del kit ±10 nm.
- **Ablaciones:** espectro, sensores, espectro + sensores y la mediana de entrenamiento como línea base.
- **Nunca son variables del modelo:** el ID del lago, la hora, las coordenadas ni el nivel nominal de adición.
- **Métricas en el lago no visto:** MAE, sesgo, R² y habilidad `S = 1 − MAE_modelo / MAE_mediana`.
- **Pendiente de adición:** `b = Σ(Δreal · Δpredicho) / Σ(Δreal²)`, emparejada al nivel 0 de cada muestra.
- El código está en `src/analysis.py`.

## 10. Criterios de fallo (sin cambios respecto a la v1.0)

- **Diseño:** menos de 5 lagos con permiso y ≥ 2 estaciones válidas, o menos de 10 muestras primarias válidas → falla el diseño de generalización a un lago nuevo.
- **Series inválidas:** más del 20 % de series inválidas en un analito → ese analito es **no concluyente**.
- **Control positivo:** la clorofila sin reactivo no alcanza `S ≥ 0,25` global y `S > 0` en al menos 4 lagos → **falla el control positivo** y no se afirma nada sobre nutrientes.
- **Modelo sin reactivo:** `|b| > 0,20` → se investiga un posible artefacto (identidad de archivos, preparación, dilución, fuga de etiquetas). Si persiste, falla el control negativo. Si `|b| ≤ 0,20`, la precisión aparente se reporta como **asociación con la matriz**, no como detección.
- **Modelo con reactivo:** pasa solo con `0,80 ≤ b ≤ 1,20` global, `0,70 ≤ b ≤ 1,30` en al menos 4 lagos y `S ≥ 0,25` global.
- Pasar el test no demuestra sensibilidad por debajo de 2L. Un fallo documentado también es un resultado válido.

## 11. Seguridad y residuos

- **Protección:** guantes de nitrilo y gafas para todos los reactivos. Los reactivos de fosfato y nitrito son ácidos, y el de amonio contiene compuestos tóxicos: seguir la ficha de seguridad de cada kit.
- **Residuos:** todo va a una garrafa de residuos etiquetada, tanto en el lago como en el laboratorio. **Nada vuelve al lago.**
- **Conservación:** la enzima y los reactivos Roche se guardan a 2–8 °C.

## 12. POR CONFIRMAR antes del piloto (02/10)

1. Permiso escrito de toma de agua en los cinco lagos.
2. Espectrofotómetro de laboratorio disponible del 5 al 9 de octubre, y que cubra 540 y 690 nm.
3. λ de lectura del fosfato 1.14848 y del kit Roche según sus prospectos. Ambas deben estar dentro de 430–770 nm.
4. L de cada kit para cubeta de 10 mm, y forma química (PO₄-P, NH₄-N, NO₂) en la que informa cada uno.
5. **Kit Roche:** con unos 64 ensayos no alcanza para ~70 ensayos de nitrito más los blancos y el nitrato. Opciones: comprar un segundo kit, o cambiar el nitrito a Spectroquant 1.14776 (335 tests).
6. Sales para los patrones (KH₂PO₄, NH₄Cl, NaNO₂) disponibles, con lote y pureza.
7. Volumen de la alícuota C, según los volúmenes de los prospectos.
8. Jeringas para filtrar (unas 100): ya no están en la lista de compra.
9. Orden de los lagos por día.

## 13. Registro de cambios

| Fecha | Cambio | ¿Datos de campaña vistos? |
|---|---|---|
| 2026-09-25 | Versión 1.0 (en inglés) | No |
| 2026-09-27 | Reorganización del repositorio; L02 pasa de los estanques de Ixelles a Mellaerts | No |
| 2026-09-30 | **Versión 2.0**: todo se mide el mismo día; kits Spectroquant y Roche como referencia; JBL solo como cribado; patrones preparados por Daniela; filtros de 0,2 µm; nitrato como variable de contexto. Diseño, análisis y criterios de fallo sin cambios. La v1.0 queda archivada en `docs/protocolo-v1.0.md` | No |
