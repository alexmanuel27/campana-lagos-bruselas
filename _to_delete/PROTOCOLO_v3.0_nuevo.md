# Protocolo: v3.0 — escenarios en acuario + prueba en el lago

**05/11/2026 · fijado antes de tomar ninguna muestra.**
Sustituye a la v2.3, que se guarda como `protocolo-v2.3.md`. La v2.3 quedó sin ejecutar: el 04/11 el nivel del lago había bajado y no había acceso.
Cualquier cambio posterior se añade al registro de cambios (§12), indicando si ya se habían visto datos.
Lo no comprobado va marcado **POR CONFIRMAR**.

**Cambios principales respecto a la v2.3:**
- el modelo se entrena en **4 escenarios de 5 L** con agua del lago filtrada, a los que se añaden algas, nutrientes, partículas y color;
- después se prueba **sin reajustar nada** en el lago (Experimento 2);
- la validación sigue dejando un día fuera.

## 1. Objetivos e hipótesis

**O1. ¿Qué puede medir MonoSpectro sin reactivos?**
- **H1a.** Las variables con **señal visible propia** (grupo A) se predicen en días no vistos.
- **H1b.** Las variables **sin señal visible** (grupo B) no se predicen. Si alguna lo hace, se interpreta como asociación con la matriz, no como medida.

**O2. ¿Mejora la lectura al añadir el fluorómetro?**
- **H2.** El modelo combinado predice mejor que el de solo MonoSpectro la clorofila-a.

**Comprobación de especificidad (E4).** En el escenario E4 hay partículas y color pero **no hay algas**. Si el modelo predice clorofila alta en E4, está midiendo atenuación y no clorofila. Se informa siempre (§7).

**Nunca se afirmará** que el espectro sin reactivo mide un nutriente.

## 2. Escenarios

Base común: **agua del lago filtrada** con el sistema de filtración grande del laboratorio. Conserva el color natural, la dureza y la conductividad, sin las algas ni las partículas del lago.

| Escenario | Qué se añade | Para qué |
|---|---|---|
| **E1** | Algas | Clorofila baja o de crecimiento lento |
| **E2** | Algas + nutrientes | Mucha clorofila con agua clara |
| **E3** | Algas + nutrientes + caolín | Clorofila con turbidez |
| **E4** | Caolín + color, **sin algas** | Turbidez y color con clorofila ≈ 0 |

**Algas: mezcla de *Chlorella vulgaris* y *Acutodesmus obliquus***, cultivos del laboratorio.
- **La misma mezcla y la misma proporción** en E1, E2 y E3. No se pone una especie por pecera: si se hiciera, la especie quedaría confundida con el tratamiento.
- Antes de inocular, se mide la clorofila del inóculo y se anota el volumen añadido a cada pecera.
- **Proporción entre especies y volumen de inóculo: POR CONFIRMAR** con Daniela.

**Nutrientes:** solo **nitrógeno y fósforo** de BG-11 al 1 %, preparados con sales sueltas. El BG-11 completo es demasiado caro; los oligoelementos los aporta el agua del lago filtrada.
- **Equivalencia:** BG-11 lleva 1,5 g/L de NaNO₃ y 0,04 g/L de K₂HPO₄. Al 1 % eso es **NO₃⁻ ≈ 11 mg/L** y **PO₄³⁻ ≈ 0,22 mg/L**.
- **Solución madre** (100 ml de agua destilada, en matraz aforado):
  - **0,89 g de KNO₃** (o 0,75 g de NaNO₃);
  - **15,6 mg de KH₂PO₄** (o 20 mg de K₂HPO₄).
- **Dosis:** **10 ml de madre por pecera de 5 L**, en E2 y E3. Total: 20 ml de madre.
- **Si a los ~7 días no hay crecimiento visible** en E2 y E3 (el color no cambia), puede que falten oligoelementos. Se añaden 5 ml de BG-11 a cada una y se anota.
- **Las mismas sales sirven de patrones** para los kits de nitrato y fosfato (ver `reactivos/`).
- **POR CONFIRMAR** que el laboratorio tiene estas sales y una balanza que pese con precisión de 0,1 mg.

**Caolín:** caolín blanco en polvo, **100 % kaolin, sin perfume, aceites ni colorantes**.
- Se prepara una suspensión concentrada en agua destilada y se añade poco a poco.
- Se añade hasta que el agua sin filtrar tenga una **A750 de 0,05–0,1** en el espectrofotómetro comercial. Es unas 3–10 veces la turbidez de P1 en el piloto.
- Se anota la masa añadida.

**Color (solo E4):** extracto húmico o de taninos **sin aditivos**, por ejemplo hojas de catappa o extracto de turba. Si no hay, té negro filtrado a 0,2 µm.
- Se añade hasta **duplicar o triplicar la A440 de la base filtrada**, y se anota la dosis.
- **No se usan:**
  - tintes alimentarios, que tienen bandas estrechas y el azul y el verde caen en la zona de la clorofila;
  - acondicionadores de agua (quelantes, coloides, anticloro);
  - "boosters" de KH (bicarbonato);
  - productos con bacterias.
- **Producto elegido:** hojas de catappa ARKA mySCAPE (solo hojas, sin aditivos).
- **Extracto (se prepara el día 0, no se meten hojas en la pecera):**
  1. Enjuagar 2 hojas con agua destilada y trocearlas.
  2. Ponerlas en un bote de vidrio limpio con **500 ml de agua destilada caliente (~80–90 °C)**.
  3. Tapar y dejar **24 h**: en nevera y a oscuras una vez frío.
  4. Filtrar: primero un filtro de papel o de café, y después el sistema grande a 0,2 µm.
  5. Medir la A440 del extracto en el espectrofotómetro comercial. Si pasa de ~2, diluir una parte con agua destilada y medir esa dilución.
  6. Etiquetar con fecha y guardar en nevera, a oscuras.
- **Dosis para E4:** `volumen de extracto (ml) = 5000 × (A440 objetivo − A440 base) / A440 del extracto`.
  - Añadir la mitad, mezclar, medir la A440 filtrada y completar.
  - Anotar el volumen total añadido y el pH antes y después: los taninos acidifican un poco.

**Recipientes:**
- 4 recipientes iguales y transparentes, de 5 L, **tapados** para que no haya evaporación ni contaminación cruzada.
- Una marca con el nivel inicial.
- Material (pipetas, cubos, varillas) **separado por escenario**. Si no puede ser, se enjuaga con agua destilada entre escenarios y E4 se manipula siempre **el primero**, para que no le lleguen algas.

## 3. Luz y temperatura

| Qué | Condición |
|---|---|
| Lámpara | **LED blanco** (4000–6500 K), la misma para las 4 peceras. Puede ser la lámpara de Daniela con su temporizador |
| Horario | **12 h encendida / 12 h apagada** |
| Intensidad | Moderada. Orientativo: 50–150 µmol/m²/s, unos 4000–10 000 lux con un luxómetro de móvil (no es una medida de PAR). **Valor exacto: POR CONFIRMAR** con Daniela. Se anota el valor medido en cada pecera al montar |
| Colocación | **Misma distancia** de la lámpara a cada pecera. **Rotar las posiciones** cada día de muestreo, siguiendo E1→E2→E3→E4→E1, y anotarlo |
| Evitar | Luz del sol directa, y que la lámpara caliente el agua |
| Temperatura | Se registra en cada muestreo con la sonda. Si alguna pecera se separa más de 2 °C de las demás, se anota |

## 4. Calendario

- **Día 0:** montaje (§5.1).
- **Muestreo cada 2–3 días durante unas 3 semanas**, con **≥ 8 días de muestreo**. Fecha de inicio: **POR CONFIRMAR**.
- **Muestra** = un escenario en un día. **Objetivo: ≥ 32 muestras** (4 × 8).
- **Hora fija:** siempre **3 h después de encenderse la luz**. La fotosíntesis cambia el O₂, el pH y la fluorescencia a lo largo del día.
- **Réplicas:** 3 lecturas por muestra en cada instrumento, promediadas. Las réplicas no cuentan como muestras.

## 5. Procedimiento

### 5.1 Día 0 (montaje)
1. Recoger agua del lago y filtrarla con el sistema grande. Necesitas unos 20 L más reserva.
2. Llenar las 4 peceras con 5 L cada una y marcar el nivel.
3. **Medir la base** en las 4 peceras, antes de añadir nada, con el procedimiento completo de §5.2. Estas medidas son el punto de partida y no entran en el modelo.
4. Añadir, en este orden:
   - caolín a E3 y E4;
   - color a E4;
   - nutrientes a E2 y E3;
   - por último, el inóculo de algas a E1, E2 y E3.

   Anotar cantidades y horas.
5. Encender la luz con el temporizador.

### 5.2 Cada día de muestreo (orden de las peceras: E4, E1, E2, E3)

**En cada pecera:**
1. Hora, temperatura del laboratorio y nivel del agua.
2. Sonda dentro de la pecera; enjuagarla con agua destilada antes y después.
3. **Remover suavemente** y sacar unos **300 ml** a un vaso limpio. Esa es la muestra del día.
4. Del vaso, después de **removerlo antes de cada alícuota**:
   - **Dejar la alícuota 10–15 min a oscuras** (en un cajón o tapada) **antes de medir en el fluorómetro.** Bajo luz, las algas reducen su fluorescencia como protección. Así todas las muestras parten de la misma condición. Para simplificar, MonoSpectro también se mide después de esa espera.
   - MonoSpectro sin filtrar, 3 réplicas.
   - Fluorómetro sin filtrar, 3 réplicas, con un blanco de agua destilada por réplica.
   - Filtro GF/F con volumen conocido (100–250 ml; menos si está muy verde) → aluminio → congelador.
   - Filtrar por 0,2 µm unos 40 ml para los kits y el color.
5. **No rellenar la pecera.** Si alguna vez hiciera falta, anotar volumen y tipo de agua.

**En el laboratorio, el mismo día:**
1. Espectrofotómetro comercial: espectro de la muestra sin filtrar y de la filtrada.
2. MonoSpectro: muestra filtrada.
3. Kits NH₄ y PO₄ sobre la porción filtrada, con 5 blancos de reactivo por kit y día. En E2 y E3 pueden superar el rango del kit: diluir con agua destilada y anotar el factor.
4. NOx (§5.3).
5. Extracción de los GF/F y lectura en el espectrofotómetro comercial (ISO 10260).
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
- Con 8 muestras, el NOx se informa **solo de forma descriptiva**.

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
| **Especificidad (E4)** | Se informa la clorofila predicha en E4 por M1 y M3 frente a la medida. Si la predicha supera de forma sistemática la medida en más que el error medio del modelo, el modelo confunde atenuación con clorofila, y así se dice |
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
  - observaciones (espuma, olor, algas pegadas a las paredes, crecimiento en E4).
- **Archivos originales:** sin editar. Celda vacía = no medido; `<x`/`>x` = fuera de rango.

## 11. Análisis

`src/campana.py` sirve tal cual con el lago = `acuarios` y el punto = `E1`…`E4`:

```
python3 -m src.campana referencias.csv acuarios results/acuarios
```

Antes del primer día de muestreo quedan dos cosas por hacer en el script:
1. la validación secundaria dejando una pecera fuera;
2. el informe de especificidad de E4.

## 12. Registro de cambios

| Fecha | Cambio | ¿Datos vistos? |
|---|---|---|
| … | (versiones anteriores: ver `protocolo-v2.3.md`) | |
| 2026-11-04 | v2.3 rev. 2: JBL solo en 2 puntos | No |
| 2026-11-05 | **v3.0**: la campaña en el lago no es viable por el bajo nivel. Entrenamiento en 4 escenarios de 5 L (agua del lago filtrada + *C. vulgaris* / *A. obliquus*, nutrientes, caolín, color húmico), luz LED 12:12, muestreo a hora fija, 10–15 min de oscuridad antes del fluorómetro, NOx en E1/E2 en días alternos, prueba en el lago con el modelo congelado. Se habían visto solo datos del piloto | No |
