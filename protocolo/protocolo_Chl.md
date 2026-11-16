# Clorofila-a por extracción en etanol caliente — protocolo para los acuarios (v1.0, 13/11/2026)

Adaptado de ISO 10260:1992 (variante con baño a 75 °C) para este experimento: muestras pequeñas (150 ml), poca clorofila al principio, cubetas de 10 mm y 3 ml, y **lectura el mismo día, sin congelar nada**.
Lo no comprobado va marcado **POR CONFIRMAR**.

## 1. Material

| Qué | Detalle |
|---|---|
| Filtros | GF/F (fibra de vidrio), los mismos de siempre |
| Etanol al 90 % | 93,75 ml de etanol 96 % + 6,25 ml de agua destilada (≈ 100 ml). Se prepara una vez y se guarda cerrado |
| Tubos | Tubos de centrífuga de 15 ml de polipropileno (aguantan etanol), con tapón y graduados. Uno por muestra + uno para el blanco de filtro |
| Baño | Baño de agua a **75 °C** (termostático o un vaso con agua y termómetro sobre una placa). **Sin llama**: el etanol arde |
| Varilla | Varilla de vidrio para romper el filtro |
| Aclarado | Centrífuga (preferible). Si no hay: jeringa + filtro de jeringa compatible con etanol (nylon o PTFE). **POR CONFIRMAR** el material de tus filtros de jeringa: los de acetato de celulosa pueden dañarse con etanol |
| Cubeta | **Vidrio o cuarzo**, 10 mm. Las de plástico (PMMA, poliestireno) pueden estropearse con etanol: **POR CONFIRMAR** qué cubetas tienes |
| Espectrofotómetro | El comercial. Blanco con etanol al 90 % |

## 2. Cuánto etanol y por qué

- Se usan **5 ml** de etanol al 90 %. Es lo mínimo que cubre un GF/F y deja ≥ 3 ml limpios para llenar la cubeta.
- Con poco etanol el extracto queda más concentrado: con 5 ml en lugar de 10, la absorbancia es el doble.
- Con 150 ml filtrados, 5 ml de etanol y cubeta de 10 mm, **1 unidad de absorbancia ≈ 406 µg/L** de clorofila en la pecera. El mínimo fiable (A665 − A750 = 0,01, ISO 10260) equivale a **~4 µg/L**.

## 3. Procedimiento (el mismo día del muestreo)

**Prepara antes:** baño a 75 °C, un tubo con etiqueta por filtro (E3, E1, E2, E4 y "blanco filtro").

1. **Filtrar** 150 ml (medidos con probeta) por GF/F, con vacío suave. Anotar el volumen exacto (Vs).
2. Con pinzas, doblar el filtro **con la cara verde hacia dentro** y meterlo en su tubo. Desde aquí, todo a **oscuras o con poca luz** (aluminio alrededor del tubo).
3. **Blanco de filtro:** un GF/F limpio, mojado con agua destilada, en su tubo. Se trata igual que las muestras (una vez por día).
4. Añadir **5,0 ml** de etanol al 90 % a cada tubo. Romper el filtro con la varilla de vidrio, apretando contra el fondo, ~30 s. Enjuagar la varilla con unas gotas del etanol del mismo tubo.
5. Tapar el tubo **sin apretar** (que pueda salir el vapor) y meterlo en el **baño a 75 °C durante 5 min**.
6. Sacar, cerrar el tapón y dejar **enfriar 15 min a oscuras** (en un cajón o envuelto en aluminio), a temperatura ambiente.
7. **Aclarar el extracto:**
   - **con centrífuga:** 10 min a ~3500 rpm;
   - **sin centrífuga:** pasar el líquido por la jeringa con filtro de nylon o PTFE a un tubo limpio. Si tampoco hay, dejar reposar 10 min y tomar solo el líquido de arriba con pipeta.
8. **Leer el volumen final** del extracto en la escala del tubo (Ve, ml). Con el calor se evapora algo: si no se puede leer, usar 5,0 ml y anotarlo.
9. **Espectrofotómetro:**
   - blanco con **etanol al 90 %** limpio;
   - llenar la cubeta con el extracto y leer **A665 y A750** (si el aparato hace barrido, guardar 400–750 nm);
   - leer también el blanco de filtro.
10. Leer **antes de 2 h** desde el paso 6. No se guarda nada para otro día.

**Comprobaciones al leer:**
- **A750 debe ser < 0,005.** Si es mayor, el extracto está turbio: volver a centrifugar o filtrar y leer de nuevo.
- **A665 del blanco de filtro** debe ser casi 0. Si no, restarla a las muestras y anotarlo.
- Si **A665 − A750 > 0,8**, diluir el extracto con etanol al 90 % (por ejemplo 1 + 1), leer y anotar el factor.

**No se acidifica.** El método ISO añade HCl para separar feopigmentos, pero con tan poca clorofila esa resta mete más ruido que información, y los cultivos son jóvenes y sanos. Se sigue el criterio de la norma danesa M07, que no acidifica.

## 4. Cálculo

```
Chl-a (µg/L) = (A665 − A750) × Ve × 1000 / (82 × l × Vs)
```

- A665 − A750: absorbancias del extracto (menos el blanco de filtro si hace falta), × factor de dilución si se diluyó.
- Ve: volumen del extracto en **ml**.
- Vs: volumen de agua filtrado en **L** (150 ml = 0,150).
- l: paso de la cubeta en **cm** (1).
- 82: coeficiente de absorción de la clorofila-a en etanol al 90 % (L g⁻¹ cm⁻¹, ISO 10260).

Ejemplo (inventado, solo para ver la cuenta): A665 = 0,052, A750 = 0,002, Ve = 4,8 ml, Vs = 0,150 L, l = 1 cm → (0,050 × 4,8 × 1000) / (82 × 1 × 0,150) = **19,5 µg/L**.

**Por debajo del límite:** si A665 − A750 < 0,01, se anota la lectura tal cual y en la columna de clorofila `<4` (o el límite que salga con tu Ve y Vs). **Nunca 0.**

## 5. Qué anotar (en `data/raw/DD-MM/reactivos/comercial/`)

Por cada tubo: pecera, fecha, volumen filtrado (ml), hora de filtrado, hora de extracción (paso 5), hora de lectura, Ve (ml), A665, A750, factor de dilución, paso de cubeta, y si se usó centrífuga o filtro.

## 6. Seguridad

- Etanol: inflamable. Nada de llama ni placa al rojo cerca de los tubos abiertos.
- Tubos flojos en el baño: si se cierran del todo con el calor, el tapón puede saltar.
- Guantes y gafas.

## 7. Filtros de la base del 11/11

Estuvieron congelados. Se extraen el 13/11 con este mismo método y se anota "congelado 2 días". Los filtros congelados pueden dar algo menos de clorofila (Sartory, 1982); queda registrado como desviación.

## Fuentes

- ISO 10260:1992, *Water quality — Spectrometric determination of the chlorophyll-a concentration* (extracto público): https://cdn.standards.iteh.ai/samples/18300/0c526b03acc743f197d849451d9e557a/ISO-10260-1992.pdf
- Aarhus Universitet, TA M07 *Klorofyl a koncentration* (etanol 96 %, sin acidificar): https://pure.au.dk/ws/files/68371319/TA_M07_Klorofyl_a.pdf
- Algal Web, *Photosynthetic pigment determination using ethanol extraction*: https://algalwebofc.github.io/Methods/Chlorophyll-ethanol-extraction.pdf
- Sartory (1982), TR 115, *Spectrophotometric analysis of chlorophyll a in freshwater plankton*: https://www.dws.gov.za/iwqs/reports/tr/TR115_Sartory_Spectrophotometric_analysis_of_chlorophyll_a_in_freshwater_plankton.pdf
