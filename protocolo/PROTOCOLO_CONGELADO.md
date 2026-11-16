# Protocolo: v3.0 — escenarios en acuario + prueba en el lago

**05/11/2026 · fijado antes de tomar ninguna muestra.**
Sustituye a la v2.3, que se guarda como `archivo/protocolo-v2.3.md`. La v2.3 quedó sin ejecutar: el 04/11 el nivel del lago había bajado y no había acceso.
Cualquier cambio posterior se añade al registro de cambios (§12), indicando si ya se habían visto datos.
Lo no comprobado va marcado **POR CONFIRMAR**.

**Cambios principales respecto a la v2.3:**
- el modelo se entrena en **4 escenarios de 4 L** (2 L de agua del lago + 2 L de agua del grifo reposada), a los que se añaden algas, nutrientes, partículas y color;
- después se prueba **sin reajustar nada** en el lago (Experimento 2);
- la validación sigue dejando un día fuera.

## 1. Objetivos e hipótesis

**O1. ¿Qué puede medir MonoSpectro sin reactivos?**
- **H1a.** Las variables con **señal visible propia** (grupo A) se predicen en días no vistos.
- **H1b.** Las variables **sin señal visible** (grupo B) no se predicen. Si alguna lo hace, se interpreta como asociación con la matriz, no como medida.

**O2. ¿Mejora la lectura al añadir el fluorómetro?**
- **H2.** El modelo combinado predice mejor que el de solo MonoSpectro la clorofila-a.

**Comprobación de especificidad (E3).** En el escenario E3 hay partículas y color pero **no hay algas**. Si el modelo predice clorofila alta en E3, está midiendo atenuación y no clorofila. Se informa siempre (§7).

**Nunca se afirmará** que el espectro sin reactivo mide un nutriente.

## 2. Escenarios

Base común (rev. 06/11): **mezcla 1:1 de agua del lago y agua del grifo reposada**, preparada en **una sola tanda** y repartida en las 4 peceras. El filtro del laboratorio es de ósmosis inversa y no sirve: quitaría también el color y las sales del lago.
- **Agua del lago:** pasada por un paño fino o un filtro de café (~20–50 µm). Así se quitan el zooplancton, que se comería las algas, y las partículas grandes. Las algas pequeñas y las bacterias del lago sí pasan.
- **Agua del grifo:** reposada **48 h** en recipientes abiertos, para que se vaya el cloro. El agua de Bruselas lleva solo cloro, sin cloramina (confirmado por Alex, 10/11): basta con el reposo.
- **Proporción 1:1:** confirmada con el tutor (10/11).
- **Consecuencias que se asumen y se miden en el día 0:**
  - E1 lleva algo de nitrato del grifo, así que no es "sin nutrientes": la diferencia con E2, E3 y E4 es la dosis añadida;
  - E3 no lleva algas añadidas pero **sí nutrientes** (11/11): las algas del lago que trae la base pueden crecer. Su clorofila se mide igual y **se sigue su crecimiento como observación de interés**; la comprobación de §7 compara clorofila predicha frente a medida.

| Escenario | Qué se añade | Para qué |
|---|---|---|
| **E1** | Algas | Clorofila baja o de crecimiento lento |
| **E2** | Algas + nutrientes | Mucha clorofila con agua clara |
| **E3** | Caolín + color + nutrientes, **sin algas añadidas** | Turbidez y color; clorofila solo de las algas del lago que crezcan (se sigue) |
| **E4** | Algas + nutrientes + caolín | Clorofila con turbidez |

**Algas: mezcla de *Chlorella vulgaris* y *Acutodesmus obliquus***, cultivos del laboratorio.
- **La misma mezcla y la misma proporción** en E1, E2 y E4. No se pone una especie por pecera: si se hiciera, la especie quedaría confundida con el tratamiento.
- Antes de inocular, se mide la clorofila del inóculo y se anota el volumen añadido a cada pecera.
- **Proporción y volumen (10/11):** las dos especies aportan la misma clorofila. Se lee cada cultivo diluido en el espectrofotómetro comercial, S = (A680 − A750) × dilución; se usa todo el cultivo más flojo y, del más fuerte, el volumen que iguale S × volumen. La mezcla se reparte en tres partes iguales (E1, E2, E4). Lo que sobra del cultivo fuerte queda de reserva. Cálculo en `data/raw/registro_acuarios.xlsx`, hoja Inoculo.
- La lectura S de cada cultivo y de la mezcla sirve de medida de clorofila del inóculo; no se gasta cultivo en GF/F.
- **Lo hecho el 11/11:** no se pudo leer el inóculo (Daniela no permite tomar muestra de los cultivos originales; las lecturas disponibles son de otros cultivos suyos, con dilución desconocida: *Chlorella* A680 0,07 / A750 0,065; *Acutodesmus* A680 0,47 / A750 0,325). Se mezclan **volúmenes iguales** (60 ml + 60 ml) y se reparten 40 ml por pecera (E1, E2, E4). La clorofila del inóculo se registra leyendo la mezcla. Lecturas de los cultivos originales enviadas por Daniela (11/11, 19:34, sin diluir; confirmado por Alex): *C. vulgaris* A680 0,075 / A750 0,039; *A. obliquus* A680 1,35 / A750 0,771. Con volúmenes iguales, *A. obliquus* aporta ~94 % de la señal A680 − A750 del inóculo.

**Nutrientes:** solo **nitrógeno y fósforo** de BG-11 al 1 %, preparados con sales sueltas. El BG-11 completo es demasiado caro; los oligoelementos los aporta el agua del lago filtrada.
- **Equivalencia:** BG-11 lleva 1,5 g/L de NaNO₃ y 0,04 g/L de K₂HPO₄. Al 1 % eso es **NO₃⁻ ≈ 11 mg/L** y **PO₄³⁻ ≈ 0,22 mg/L**.
- **Solución madre** (100 ml de agua destilada, en matraz aforado):
  - **0,89 g de KNO₃** (o 0,75 g de NaNO₃, o **1,04 g de nitrato cálcico tetrahidrato**, Ca(NO₃)₂·4H₂O, CAS 13477-34-4; con un fertilizante: gramos = 12,3 ÷ % de N de la etiqueta);
  - **15,6 mg de KH₂PO₄** (o 20 mg de K₂HPO₄).
- **Dosis:** **8 ml de madre por pecera de 4 L**, en E2, E3 y E4 (misma concentración que 10 ml en 5 L). Total: 24 ml de madre.
- **Si a los ~7 días no hay crecimiento visible** en E2 y E4 (el color no cambia), puede que falten oligoelementos. Se añaden 4 ml de BG-11 a cada una y se anota.
- **El nitrógeno va como nitrato (KNO₃ o NaNO₃), no como amonio.** El sulfato amónico no vale: a pH ~8 parte del amonio pasa a amoníaco, que es tóxico para las algas, y además acidifica. Tampoco coincide con BG-11 ni con el kit de nitrato.
- Las sales pueden ser de grado fertilizante (por ejemplo, fosfato monopotásico MKP). Para usarlas como patrón de los kits, mejor de grado reactivo si el laboratorio las tiene.
- **Las mismas sales sirven de patrones** para los kits de nitrato y fosfato (ver `reactivos/`).
- Sales y balanza de 0,1 mg: confirmadas (10/11).

**Caolín:** caolín blanco en polvo, **100 % kaolin, sin perfume, aceites ni colorantes**.
- Se prepara una suspensión concentrada en agua destilada y se añade poco a poco.
- Se añade hasta que el agua sin filtrar tenga una **A750 de 0,05–0,1** en el espectrofotómetro comercial. Es unas 3–10 veces la turbidez de P1 en el piloto.
- Se anota la masa añadida.

**Color (solo E3):** extracto húmico o de taninos **sin aditivos**, por ejemplo hojas de catappa o extracto de turba. Si no hay, té negro filtrado a 0,2 µm.
- Se añade hasta **duplicar o triplicar la A440 de la base filtrada**, y se anota la dosis.
- **11/11:** la base filtrada de E3 dio A440 = 0,003 (prácticamente sin color), así que duplicarla no tiene sentido. Objetivo absoluto: **A440 filtrada de 0,05–0,1** (propuesta, a confirmar con los datos). El extracto de 2 hojas en 500 ml dio A440 = 0,864. Se añade ese mismo extracto, sin concentrar: para A440 = 0,05 hacen falta **~231 ml** (x = V·(objetivo − base)/(extracto − objetivo), contando la dilución). E3 queda en ~4,23 L y el caolín se diluye ~5 %; se marca el nivel nuevo y se vuelve a leer la A750.
- **No se usan:**
  - tintes alimentarios, que tienen bandas estrechas y el azul y el verde caen en la zona de la clorofila;
  - acondicionadores de agua (quelantes, coloides, anticloro);
  - "boosters" de KH (bicarbonato);
  - productos con bacterias.
- **Producto elegido:** hojas de catappa ARKA mySCAPE (solo hojas, sin aditivos).
- **Extracto (se prepara el día 0 y el color se añade a E3 al día siguiente, porque necesita 24 h; no se meten hojas en la pecera):**
  1. Enjuagar 2 hojas con agua destilada y trocearlas.
  2. Ponerlas en un bote de vidrio limpio con **500 ml de agua destilada caliente (~80–90 °C)**.
  3. Tapar y dejar **24 h**: en nevera y a oscuras una vez frío.
  4. Filtrar: primero un filtro de papel o de café, y después, con filtros de jeringa de 0,2 µm, solo el volumen que se vaya a usar (unos 100–150 ml).
  5. Medir la A440 del extracto en el espectrofotómetro comercial. Si pasa de ~2, diluir una parte con agua destilada y medir esa dilución.
  6. Etiquetar con fecha y guardar en nevera, a oscuras.
- **Dosis para E3:** `volumen de extracto (ml) = 4000 × (A440 objetivo − A440 base) / A440 del extracto`.
  - Añadir la mitad, mezclar, medir la A440 filtrada y completar.
  - Anotar el volumen total añadido y el pH antes y después: los taninos acidifican un poco.

**Recipientes:**
- 4 recipientes iguales y transparentes, con **4 L** de agua cada uno, **tapados** para que no haya evaporación ni contaminación cruzada.
- Una marca con el nivel inicial.
- Material (pipetas, cubos, varillas) **separado por escenario**. Si no puede ser, se enjuaga con agua destilada entre escenarios y E3 se manipula siempre **el primero**, para que no le lleguen algas.

## 3. Luz y temperatura

| Qué | Condición |
|---|---|
| Lámpara | **LED blanco** (4000–6500 K), la misma para las 4 peceras. Puede ser la lámpara de Daniela con su temporizador |
| Horario | **12 h encendida / 12 h apagada**: de **8:00 a 20:00** (muestreo a las 11:00) |
| Intensidad | Moderada. Orientativo: 50–150 µmol/m²/s, unos 4000–10 000 lux con un luxómetro de móvil (no es una medida de PAR). **Valor exacto: POR CONFIRMAR** con Daniela. Se anota el valor medido en cada pecera al montar |
| Colocación | **Misma distancia** de la lámpara a cada pecera. **Rotar las posiciones** cada día de muestreo, siguiendo E1→E2→E3→E4→E1, y anotarlo |
| Evitar | Luz del sol directa, y que la lámpara caliente el agua |
| Aireación | Una bomba de acuario **fuera de la zona de luz**, con distribuidor de 4 salidas y llave en cada una; **24 h encendida**. Tubos de la misma longitud, abiertos en la punta, sin piedra, sujetos con la punta a **3 cm del fondo** en las 4. Bomba al máximo con las 4 llaves abiertas del todo (montaje del 10/11); se comprueba que el nivel baja igual en las 4. Bomba por encima del nivel del agua o con válvula antirretorno. Tapas con un agujero para el tubo y otro de salida de aire. Mantiene en suspensión caolín y algas y aporta CO₂; el O₂ de la sonda quedará cerca de saturación |
| Temperatura | **Ambiente del laboratorio, 20–25 °C**, sin calentador. Si el laboratorio baja de ~18 °C por la noche, un calentador pequeño por pecera, todos iguales. No imitar el lago en noviembre (~11 °C): las algas apenas crecerían. Se registra en cada muestreo con la sonda, más la mínima y la máxima del laboratorio entre muestreos. Si alguna pecera se separa más de 2 °C de las demás, se anota |

## 4. Calendario

- **Día 0:** montaje (§5.1).
- **Muestreo lunes, miércoles y viernes durante unos 24 días, con 10 días de muestreo** (≥ 8 como mínimo): 13, 16, 18, 20, 23, 25, 27 y 30/11, y 2 y 4/12. Día 0: **11/11/2026** (peceras llenas y aireadas desde el 10/11; base, caolín, nutrientes, algas y color el 11/11). Primer muestreo: **13/11/2026**.
- **Muestra** = un escenario en un día. **Objetivo: 40 muestras** (4 × 10; mínimo 32).
- **Hora fija:** siempre **3 h después de encenderse la luz**. La fotosíntesis cambia el O₂, el pH y la fluorescencia a lo largo del día.
- **Réplicas:** 3 lecturas por muestra en cada instrumento, promediadas. Las réplicas no cuentan como muestras.

## 5. Procedimiento

### 5.1 Día 0 (montaje)
1. Dos días antes: llenar recipientes abiertos con agua del grifo (unos 9 L). El día 0: recoger unos 9 L de agua del lago, pasarlos por un paño fino o un filtro de café y mezclar 1:1 con el agua del grifo reposada en un solo recipiente. Guardar 1 L de cada agua por separado para medirla.
2. Llenar las 4 peceras con **4 L** cada una (2 L de lago + 2 L de grifo) y marcar el nivel.
3. **Medir la base** en las 4 peceras, antes de añadir nada, con el procedimiento completo de §5.2. Estas medidas son el punto de partida y no entran en el modelo. Después, cada pecera se rellena hasta la marca de 4 L con la reserva de mezcla 1:1 (misma agua, guardada en nevera), para que las dosis sean exactas.
4. Añadir, en este orden:
   - caolín a E4 y E3;
   - color a E3, cuando el extracto de catappa tenga 24 h (si no las tiene, al día siguiente);
   - nutrientes a E2, E3 y E4;
   - por último, el inóculo de algas a E1, E2 y E4.

   Anotar cantidades y horas en `data/raw/registro_acuarios.xlsx`.
5. Encender la luz con el temporizador. Medir los lux de cada pecera y anotarlos en la hoja Luz_y_posicion.

### 5.2 Cada día de muestreo (orden de las peceras: E3, E1, E2, E4)

**En cada pecera:**
1. Hora, temperatura del laboratorio y nivel del agua.
2. Sonda dentro de la pecera; enjuagarla con agua destilada antes y después.
3. **Remover suavemente** y sacar unos **200 ml** a un vaso limpio (desde el 13/11; con 4 L y 10 muestreos, cada pecera baja a la mitad, ~2 L al final). Esa es la muestra del día.
4. Del vaso, después de **removerlo antes de cada alícuota**:
   - **Dejar la alícuota 10–15 min a oscuras** (en un cajón o tapada) **antes de medir en el fluorómetro.** Bajo luz, las algas reducen su fluorescencia como protección. Así todas las muestras parten de la misma condición. Para simplificar, MonoSpectro también se mide después de esa espera.
   - MonoSpectro sin filtrar, 3 réplicas.
   - Fluorómetro sin filtrar, 3 réplicas, con un blanco de agua destilada por réplica.
   - Filtro GF/F con volumen conocido (**150 ml**; 50–100 ml si está muy verde) → **extracción en etanol el mismo día**, sin congelar (desde el 13/11 no hay sitio en el congelador). Mientras se espera la extracción, el filtro se guarda doblado en aluminio, a oscuras.
   - Filtrar por 0,2 µm unos 40 ml para los kits y el color. **Se miden el mismo día**; no se guarda nada para otro día.
5. **No rellenar la pecera.** Si alguna vez hiciera falta, anotar volumen y tipo de agua.

**En el laboratorio, el mismo día:**
1. Espectrofotómetro comercial: espectro de la muestra sin filtrar y de la filtrada.
2. MonoSpectro: muestra filtrada.
3. Kits NH₄ y PO₄ sobre la porción filtrada, con 5 blancos de reactivo por kit y día. En E2, E3 y E4 pueden superar el rango del kit: diluir con agua destilada y anotar el factor.
4. NOx (§5.3).
5. Extracción de los GF/F y lectura en el espectrofotómetro comercial (ISO 10260), **siempre el mismo día del muestreo**. Método: `protocolo/protocolo_Chl.md` (etanol al 90 % a 75 °C, 5 ml, lectura el mismo día, sin acidificar).
6. Copiar los archivos crudos a `data/raw/DD-MM/acuarios/E1…E4/`.

### 5.3 Nitrito/nitrato (kit Roche, cubetas de 3 ml)

Protocolo de laboratorio: `reactivos/nitrito-nitrato_paso-a-paso.md`.

- Quedan **~21 cubetas**: no da para las 4 peceras todos los días.
- **Se mide NOx** (solo la cubeta con enzima) **en E1 y E2, en días alternos de muestreo** (días 1, 3, 5 y 7). En cada uno: 1 blanco + E1 + E2.
- **Control positivo:**
  - el primer día de NOx;
  - el día que se abra el segundo frasco de enzima. El primero caduca hacia el 13/11, a las 2 semanas de disolverlo; **fecha exacta POR CONFIRMAR**.
- **Comprobación de nitrito**, solo el primer día: 1 blanco sin enzima + E2 sin enzima.
- **Dilución:** E2 empieza con ~11 mg/l de nitrato y el kit llega hasta 5 mg/l. E2 se mide **diluida 1:4** con agua destilada (1 parte de muestra + 3 de agua). Si un día sale por debajo de ~0,5 mg/l equivalentes, porque las algas lo han consumido, los días siguientes se mide sin diluir.
- **Total ≈ 4 × 3 + 2 controles + 2 de nitrito = 16 cubetas.**
- Con 8 muestras de NOx (4 días × E1 y E2), el NOx se informa **solo de forma descriptiva**.

## 6. Variables

### 6.1 Referencias (lo que se intenta predecir)

| Grupo | Variable | Referencia |
|---|---|---|
| A | Clorofila-a (µg/L) | GF/F → etanol → espectrofotómetro comercial (ISO 10260) |
| A | Color filtrado | Espectrofotómetro comercial, filtrada a 0,2 µm, A440 |
| A | Atenuación por partículas | Espectrofotómetro comercial, A750 sin filtrar − filtrada |
| B | NH₄, PO₄ | Kits Spectroquant, absorbancia neta = muestra − blanco de reactivo − filtrada sin reactivo. Si se dispone del medio de cultivo, sirve como control de concentración aproximada |
| B | NOx | Kit Roche, solo en el subconjunto de §5.3, descriptivo |
| B | Conductividad, pH, O₂, temperatura | Sonda |

**El JBL no se usa en los acuarios.**

### 6.2 Variables del modelo (igual que la v2.3)

| Instrumento | Variable | Qué mide |
|---|---|---|
| MonoSpectro | 1. **Nivel**: absorbancia media 420–780 nm | Luz quitada en total |
| MonoSpectro | 2–4. **Forma**: PC1–PC3 del espectro sin desplazamiento, con la PCA ajustada solo con el entrenamiento | Cómo se reparte la absorción por colores |
| Fluorómetro | 5. **Atenuación**: −log₁₀(media muestra/blanco en los canales válidos) | Luz del LED que atraviesa |
| Fluorómetro | 6. **Índice 680**: R680 / media(R645, R705) | Fluorescencia de la clorofila |

- Canales válidos: todos menos 410, 435 y 485.
- **Modelos** (ridge, α = 1, escalado ajustado solo con el entrenamiento):
  - M0, mediana;
  - M1, variables 1–4;
  - M2, variables 5–6;
  - M3, variables 1–6.
- El escenario, el día y la hora no son nunca variables del modelo.

## 7. Validación y criterios (Experimento 1, acuarios)

**Validación principal:** se deja un **día** fuera cada vez; cada día tiene las 4 peceras.
**Validación secundaria (descriptiva):** se deja una **pecera** fuera cada vez.
**Métrica:** `S = 1 − MAE_modelo / MAE_mediana`, global y por día.

| Criterio | Pasa si |
|---|---|
| **O1 · "MonoSpectro mide X"** (grupo A) | M1: S ≥ 0,25 global **y** S > 0 en ≥ 80 % de los días |
| **O1 · grupo B** | Aunque se alcance S ≥ 0,25, es **asociación**, nunca medida. Con nutrientes añadidos, la asociación con la clorofila es esperable |
| **O2 · "el fluorómetro mejora la clorofila"** | M3 − M1: ΔS ≥ 0,10 global **y** ΔS > 0 en ≥ 80 % de los días |
| **Especificidad (E3)** | Se informa la clorofila predicha en E3 por M1 y M3 frente a la medida. Si la predicha supera de forma sistemática la medida en más que el error medio del modelo, el modelo confunde atenuación con clorofila, y así se dice |
| **Diseño mínimo** | ≥ 6 días de muestreo con las 4 peceras válidas (≥ 24 muestras). Si no, el resultado es exploratorio |

**Siguen pendientes, y se decidirán con datos vistos registrándolo en §12:**
1. qué hacer con los valores fuera de rango (≤ 50 %);
2. el techo del criterio de O2 cuando S(M1) se acerca a 1.

## 8. Experimento 2: prueba en el lago con el modelo congelado

1. Al cerrar el Experimento 1, se entrenan M1 y M3 con **todas** las muestras de acuario. Se guardan los coeficientes, el escalado y la PCA en `results/` con fecha, **antes** de ir al lago. Desde ese momento, no se reajusta nada.
2. **Lago:** el mismo de donde salió el agua base.
   - **≥ 2 días, ≥ 12 muestras**, en los puntos accesibles; con pértiga muestreadora si hace falta.
   - Mismo procedimiento que §5.2: oscuridad antes del fluorómetro, 3 réplicas, GF/F, kits y sonda.
   - **Fechas y acceso: POR CONFIRMAR.**
3. **Métrica:**
   - S con la mediana **del propio lago** como línea base;
   - también el error medio en µg/L, porque en noviembre la clorofila del lago puede variar muy poco.
4. **Criterios:**
   - O1 pasa si S ≥ 0,25;
   - O2 pasa si ΔS(M3 − M1) ≥ 0,10, con la clorofila como variable principal.
   - Si fallan, es un resultado: el modelo depende del entorno (especies, matriz). Las algas del cultivo son verdes; si en el lago dominan otros grupos (por ejemplo, cianobacterias o diatomeas), se anota.

## 9. Control de calidad

**MonoSpectro, cada día antes de medir:**
- reloj en hora;
- exposición con **0 columnas saturadas**;
- **oscuro con esa misma exposición** al empezar.

**Fluorómetro:**
- un blanco por réplica;
- **siempre 10–15 min de oscuridad** antes de leer.

**Kits:** 5 blancos de reactivo por kit y día; restar también la muestra filtrada sin reactivo.

**Exclusión:**
- solo por archivo ausente, valores no finitos o saturación;
- nada se excluye por ser alto, bajo o porque empeore una métrica;
- toda exclusión se anota con su motivo.

## 10. Datos

- **Carpetas:** `data/raw/DD-MM/acuarios/E1…E4/{monospectro,fluorometer,sonda}/<réplica>/`. Medidas de laboratorio en `data/raw/DD-MM/reactivos/`.
- **Hoja de montaje (día 0):**
  - volúmenes;
  - inóculo (volumen y clorofila);
  - medio y dilución;
  - caolín (g);
  - color (producto y dosis);
  - luz medida por pecera.
- **Hoja diaria:**
  - hora;
  - posición de cada pecera;
  - nivel del agua;
  - temperatura;
  - observaciones (espuma, olor, algas pegadas a las paredes, crecimiento en E3).
- **Archivos originales:** sin editar. Celda vacía = no medido; `<x`/`>x` = fuera de rango.

## 11. Análisis

`src/campana.py` sirve tal cual con el lago = `acuarios` y el punto = `E1`…`E4`:

```
python3 -m src.campana referencias.csv acuarios results/acuarios
```

Antes del primer día de muestreo quedan dos cosas por hacer en el script:
1. la validación secundaria dejando una pecera fuera;
2. el informe de especificidad de E3.

## 12. Registro de cambios

| Fecha | Cambio | ¿Datos vistos? |
|---|---|---|
| … | (versiones anteriores: ver `archivo/protocolo-v2.3.md`) | |
| 2026-11-04 | v2.3 rev. 2: JBL solo en 2 puntos | No |
| 2026-11-05 | **v3.0**: la campaña en el lago no es viable por el bajo nivel. Entrenamiento en 4 escenarios de 5 L (agua del lago filtrada + *C. vulgaris* / *A. obliquus*, nutrientes, caolín, color húmico), luz LED 12:12, muestreo a hora fija, 10–15 min de oscuridad antes del fluorómetro, NOx en E1/E2 en días alternos, prueba en el lago con el modelo congelado. Se habían visto solo datos del piloto | No |
| 2026-11-06 | v3.0 rev.: base = lago (paño fino) + grifo reposado 1:1, porque el filtro disponible es de ósmosis; nitrato cálcico como alternativa; temperatura 20–25 °C | No |
| 2026-11-10 | v3.0 rev.: confirmados base 1:1, agua de grifo solo con cloro, sales y balanza; regla del inóculo (misma clorofila por especie); color de E4 el día 1 porque el extracto necesita 24 h; día 0 = 10/11, primer muestreo 13/11; registro en `data/raw/registro_acuarios.xlsx` | No |
| 2026-11-10 | v3.0 rev.: aireación suave igual en las 4 peceras (tubo abierto, sin piedra), 24 h | No |
| 2026-11-10 | v3.0 rev.: peceras de 4 L (2 L lago + 2 L grifo); nutrientes 8 ml de madre; fórmula del color con 4000 ml | No |
| 2026-11-10 | v3.0 rev.: se descarta filtrar por GF/F el agua del lago de E4; E4 usa la misma base que E1–E3 y conserva las pocas algas del lago | No |
| 2026-11-10 | v3.0 rev.: día 0 pasa al 11/11; peceras llenas y aireadas el 10/11; extracto de catappa preparado el 10/11 | No |
| 2026-11-11 | v3.0 rev.: luz de 8:00 a 20:00, muestreo a las 11:00; tras medir la base, rellenar a 4 L con la reserva 1:1 | No |
| 2026-11-11 | v3.0 rev.: inóculo a volúmenes iguales (60 + 60 ml, 40 ml por pecera) porque no se pudo leer el cultivo original | No |
| 2026-11-11 | v3.0 rev.: color de E4 con objetivo absoluto A440 0,05–0,1 (la base no tiene color); sin concentrar el extracto (~231 ml en E4) | No |
| 2026-11-11 | **Escenarios E3 y E4 redefinidos** (decisión de Alex): el color se echó en la pecera E3, así que desde el día 0 **E3 = caolín + color, sin algas** y **E4 = algas + nutrientes + caolín**. Cambiado en todo el protocolo; las filas anteriores de este registro usan la numeración antigua | No |
| 2026-11-11 | E3 recibió nutrientes (8 ml de madre) antes de redefinir los escenarios: se incorpora al diseño (E3 = caolín + color + nutrientes, sin algas añadidas) y se sigue el crecimiento de las algas del lago | No |
| 2026-11-13 | Muestra diaria de 300 → 200 ml; GF/F 150 ml (50–100 si está muy verde), por el volumen de 4 L | No |
| 2026-11-13 | 10 días de muestreo (13/11–4/12, lunes-miércoles-viernes), 40 muestras; cada pecera baja a ~2 L; GF/F ≈ 44 | No |
| 2026-11-13 | Nada se congela ni se guarda para otro día: GF/F extraídos y kits medidos el mismo día del muestreo (sin espacio en el congelador). Lo guardado de la base del 11/11 se procesa el 13/11 | No |
| 2026-11-13 | Método de clorofila propio (`protocolo/protocolo_Chl.md`), adaptado de ISO 10260 | No |
