# Nitrito / nitrato — protocolo detallado (Roche 11 746 081 001)

Basado en el manual `11746081001.pdf` (versión 07, nov. 2020) y en la ficha del producto de Sigma-Aldrich.
Lo que viene del manual va sin marca. Lo que es consejo práctico mío va marcado **[práctico]**. Lo que no está verificado va marcado **POR CONFIRMAR**.
Si algo choca con el manual, manda el manual.

---

## 0. Idea del método (leer una vez)

1. **Nitrito** + reactivo de color I (sulfanilamida) + reactivo de color II (NED) → colorante **rosa-violeta**. Se lee a **540 nm**.
2. **El nitrato no da color por sí solo.** La enzima *nitrato reductasa*, con NADPH, lo convierte primero en nitrito. Después se colorea igual.
3. Por eso cada muestra lleva **2 cubetas**:
   - **N** (sin enzima) → mide solo nitrito.
   - **N+N** (con enzima) → mide nitrito + nitrato.
   - **Nitrato = N+N − N.**
4. Cada cubeta se lee **dos veces**, siempre en la misma cubeta:
   - **A1** antes del color: es el "fondo" de la muestra, la cubeta y la turbidez.
   - **A2** después del color.
   - Lo que cuenta es **A2 − A1**.

**Problema típico del método [práctico]:** si la enzima falla, el nitrato sale 0 y parece que "no hay nitrato".
La única forma de distinguir "no hay nitrato" de "la enzima no funcionó" es un **control positivo** (§3).

---

## 1. Material

**Del kit (todo a 2–8 °C)**

| Frasco | Contenido | Uso |
|---|---|---|
| 1 | Tampón fosfato pH 7,5, 22 ml | Disolver la pastilla |
| 2 | 7 pastillas NADPH/FAD | Coenzima |
| 3 | Nitrato reductasa liofilizada, 2 frascos | Enzima |
| 4 | Reactivo de color I (sulfanilamida), 2 × 8 ml | Color |
| 5 | Reactivo de color II (NED), 2 × 8 ml | Color |

**Del laboratorio**

- Espectrofotómetro a **540 nm**; vale el comercial.
- **Cubetas semimicro de 1 cm**, de vidrio o desechables (PS/PMMA valen a 540 nm). Volumen final 1,27 ml: la cubeta debe admitir unos 1,5 ml.
- **Micropipetas calibradas**:
  - P20 para los 20 µl de enzima;
  - P200 o P1000 para 250 µl;
  - P1000 para 270, 500 y 770 µl.
- Puntas nuevas para cada reactivo y cada muestra.
- **Agua bidestilada o ultrapura recién servida.** Es la fuente nº 1 de contaminación.
- Parafilm, gradilla para cubetas, temporizador, caja o cajón oscuro.
- Filtros de jeringa de 0,2 µm (los que hay) y jeringas.
- Guantes, gafas y bata.
  - La ficha del producto indica que es corrosivo, que puede causar daño ocular grave y que puede sensibilizar piel y vías respiratorias. **No inhalar el polvo de la enzima.**

---

## 2. Antes de empezar (30 min antes)

1. **Sacar el kit de la nevera** y dejarlo a temperatura ambiente (**15–25 °C**). Con reactivos fríos la enzima va lenta y el nitrato sale bajo.
2. **Hacer la lista de cubetas** de la sesión (ejemplo en §5) y **numerar las cubetas** en la parte de arriba, no en las caras ópticas.
3. **[práctico]** Marcar en cada cubeta qué cara mira a la luz. **A1 y A2 deben leerse en la misma cubeta y con la misma orientación**: si no, A2 − A1 no corrige nada.
4. **[práctico]** Probar que el espectro lee a 540 nm y hacer el **cero con una cubeta de agua bidestilada**. Ese cero se usa para toda la sesión.

---

## 3. Muestras y controles

### 3.1 Muestras de lago

1. **Filtrar** con filtro de jeringa de 0,2 µm:
   - desechar los **primeros 2 ml**;
   - recoger unos **2 ml** en un tubo limpio.
2. Las muestras deben ser transparentes. Si salen turbias, se pierde A1 y la medida.
3. Medir el **mismo día** del muestreo; si no se puede, guardar a **4 °C** y medir antes de 24 h. **[práctico — POR CONFIRMAR con tu protocolo de campo]**: el nitrito no es estable en el tiempo.
4. No diluir: el kit mide **0,02–5 mg/l**. Solo si una muestra da A2 − A1 > ~1,5, diluir con agua bidestilada y anotar el factor.

### 3.2 Controles (cada sesión)

| Control | Qué es | Para qué |
|---|---|---|
| **Blanco N** | Agua en lugar de muestra, sin enzima | Restar el color de reactivos y agua |
| **Blanco N+N** | Agua en lugar de muestra, con enzima | Ídem, para las cubetas con enzima |
| **Control positivo [práctico]** | Una solución que **seguro** tiene nitrato | Comprobar que la enzima funciona |
| **Blanco de filtro [práctico]** | Agua bidestilada pasada por un filtro nuevo | Comprobar que el filtro no aporta nitrato (una vez por lote de filtros) |

**Control positivo**
- **Lo ideal:** KNO₃ (nitrato potásico) a ~1 mg nitrato/l (preparación en §7). Si hay NaNO₂, un patrón de nitrito a ~1 mg/l sirve de control de la reacción de color.
- **Si no hay sales [práctico]:** agua del grifo diluida 1:5 con agua bidestilada.
  - El agua de red suele llevar nitrato. **POR CONFIRMAR** cuánto tiene la de Bruselas.
  - No da un número, pero tiene que dar **N+N claramente mayor que N**. Si no lo da, la enzima no funciona y los nitratos de esa sesión no valen.

---

## 4. Preparar las soluciones de trabajo (justo antes de pipetear)

| Solución | Cómo | Dura |
|---|---|---|
| **1** | Frasco 1 tal cual, a temperatura ambiente | 1 año a 2–8 °C |
| **2 (mezcla de reacción)** | Con la pinza del kit, **1 pastilla** del frasco 2 en un tubo limpio + **3 ml de Solución 1** | **Solo ese día**: se prepara al momento |
| **3 (enzima)** | **Un** frasco 3 + **0,7 ml** de agua bidestilada | **2 semanas a 2–8 °C** |
| **4 y 5 (color)** | Frascos 4 y 5 tal cual | 3 meses a 2–8 °C una vez abiertos |

### Detalles que suelen fallar [práctico]

**Pastilla (Solución 2)**
- Dejar que se disuelva **del todo**: 5–10 min, agitando suavemente o invirtiendo el tubo.
- **No debe quedar ningún grumo.** Si queda, la cantidad de NADPH por cubeta varía.
- Alcanza para **12 cubetas con enzima**, contando blancos y controles. Si en una sesión hay más de 12 cubetas N+N, hace falta una segunda pastilla.

**Enzima (Solución 3)**
- Añadir el agua, tapar y **girar suavemente**. **No usar vórtex ni agitar fuerte**: la enzima se desnaturaliza. Esperar 10 min.
- **Escribir en el frasco la fecha** de reconstitución. A las 2 semanas no vale.
- No congelar. Guardar a 2–8 °C entre usos.
- Abrir el **segundo frasco solo** cuando caduque o se acabe el primero.

**Pipetear 20 µl de enzima**
- Es el volumen más pequeño y el que más falla.
- Usar una P20 y meter la punta en el líquido ya dentro de la cubeta.
- Enjuagar la punta subiendo y bajando 2–3 veces para que no quede enzima pegada.

---

## 5. Esquema de pipeteo

Volúmenes en **ml**, en el orden de las filas. Todas las cubetas acaban con **1,27 ml**.

| Paso | Añadir | Blanco N | Muestra N | Blanco N+N | Muestra N+N |
|---|---|---|---|---|---|
| a | Muestra (o control) | — | **0,500** | — | **0,500** |
| b | Agua bidestilada | **0,770** | **0,270** | **0,500** | — |
| c | Solución 2 (mezcla de reacción) | — | — | **0,250** | **0,250** |
| d | Solución 3 (enzima) | — | — | **0,020** | **0,020** |
| e | Mezclar · **30 min** a 15–25 °C · **leer A1** | ✓ | ✓ | ✓ | ✓ |
| f | Color I (frasco 4) | **0,250** | **0,250** | **0,250** | **0,250** |
| g | Color II (frasco 5) | **0,250** | **0,250** | **0,250** | **0,250** |
| h | Mezclar · **10–15 min a oscuras** · **leer A2** | ✓ | ✓ | ✓ | ✓ |

Antes de pipetear la muestra, enjuagar la punta una vez con la propia muestra (lo indica el manual).

### Ejemplo de sesión: 3 muestras + control positivo = 10 cubetas

| Cubeta | Contenido |
|---|---|
| 1 | Blanco N |
| 2 | Blanco N+N |
| 3 / 4 | Muestra 1: N / N+N |
| 5 / 6 | Muestra 2: N / N+N |
| 7 / 8 | Muestra 3: N / N+N |
| 9 / 10 | Control positivo: N / N+N |

Lleva 5 cubetas N+N, que caben en 1 pastilla.

---

## 6. Paso a paso con tiempos

| Tiempo | Qué hacer |
|---|---|
| −30 min | Kit fuera de la nevera. Filtrar las muestras. Numerar las cubetas. |
| −10 min | Preparar la Solución 2 (pastilla). Si hace falta, reconstituir la enzima (Solución 3). |
| 0 | Pipetear los pasos **a → d** en todas las cubetas. **La enzima la última**, cubeta por cubeta. |
| 0 | **Mezclar** (cómo, más abajo). Arrancar el temporizador: **30 min**. |
| 30 min | Hacer el **cero con agua**. **Leer A1** de todas las cubetas, en orden y con la orientación marcada. Anotar. |
| 35 min | Añadir **0,250 ml de color I** a todas las cubetas y después **0,250 ml de color II** a todas. |
| 35 min | Mezclar. Guardar **a oscuras**. Temporizador: **10–15 min**. |
| 50 min | **Leer A2** de todas, en el **mismo orden** y con la misma orientación. Anotar. |

**Cómo mezclar [práctico]**
- Tapar la cubeta con un trozo de parafilm, apretar con el dedo e **invertir 5–6 veces suavemente**.
- Golpear con el dedo para que no queden **burbujas** en la cara óptica. Las burbujas son la causa nº 1 de lecturas raras.

**Comprobaciones al leer [práctico]**
- La cara óptica tiene que estar seca y limpia (secar con papel sin pelusa).
- Leer A2 entre los 10 y los 30 min tras el color. No dejar las cubetas horas antes de leer.
- **Leer los blancos primero y después las muestras.**

Si también se lee en **MonoSpectro**, hacerlo justo después del comercial con las mismas cubetas, anotando qué cubeta es cuál.

---

## 7. Patrones (solo si hay las sales)

**Soluciones madre**
- **Nitrito**: **75,0 mg de NaNO₂** en un matraz aforado de 100 ml con agua bidestilada → 500 mg nitrito/l.
- **Nitrato**: **81,5 mg de KNO₃** en 100 ml → 500 mg nitrato/l.

**Diluciones [práctico], dentro del rango 0,05–5 mg/l**
- Primero una intermedia **1:100** (1 ml de madre → 100 ml) = **5 mg/l**.
- A partir de la de 5 mg/l:

| Concentración | ml de la de 5 mg/l | Llevar a |
|---|---|---|
| 2,5 mg/l | 5 | 10 ml |
| 1 mg/l | 2 | 10 ml |
| 0,5 mg/l | 1 | 10 ml |
| 0,1 mg/l | 0,2 | 10 ml |

**Uso**
- Los patrones se tratan **igual que las muestras**:
  - patrones de **nitrito** → solo cubeta N;
  - patrones de **nitrato** → cubeta N+N.
- Según el manual, la curva no hay que hacerla cada vez: basta comprobarla de vez en cuando con un patrón como control.

**Gasto**
- Una curva de 4 puntos de nitrato cuesta 4 cubetas N+N más su blanco.
- Con los reactivos de color para 64 cubetas, una curva por kit es razonable.

---

## 8. Cálculos

**1.** Para cada cubeta: **ΔA = A2 − A1**.

**2.** Restar los blancos:
- **ΔA nitrito** = ΔA(muestra N) − ΔA(blanco N)
- **ΔA nitrito+nitrato** = ΔA(muestra N+N) − ΔA(blanco N+N)
- **ΔA nitrato** = ΔA nitrito+nitrato − ΔA nitrito

**3.** Pasar a concentración:
- **Con curva:** concentración = ΔA / pendiente de la recta, y multiplicada por el factor de dilución si se diluyó.
- **Sin curva:** se informa **ΔA a 540 nm**, como fija el protocolo v2.2 para el grupo B.

**4.** Conversión del manual, si la curva se expresa como sal:
- NaNO₂ → nitrito (NO₂⁻): × **0,667**
- KNO₃ → nitrato (NO₃⁻): × **0,613**

**Orden de magnitud esperado [práctico — estimación mía, no del manual; la curva manda]**
- Con la dilución en cubeta (0,5 → 1,27 ml) y la absortividad típica del colorante de Griess (~4–5 × 10⁴ l mol⁻¹ cm⁻¹):
  - 1 mg/l de nitrito → ΔA ≈ 0,35–0,45;
  - 1 mg/l de nitrato → ΔA ≈ 0,25–0,35.
- En el límite de detección (0,02 mg/l): ΔA ≈ 0,005–0,01. Eso es del orden del ruido del espectro, así que ahí sale "< LD".

---

## 9. Qué hacer si algo sale mal

| Lo que ves | Causa probable | Qué hacer |
|---|---|---|
| **Nada se pone rosa**, ni el control positivo | Reactivos de color fríos, caducados o cambiados de orden; o no hay nitrito/nitrato | Comprobar caducidad y temperatura; repetir con el control positivo |
| **El control positivo da N+N ≈ N** | **La enzima no funciona**: reconstituida hace > 2 semanas, agitada con vórtex, congelada, fría; o la pastilla no estaba disuelta; o la incubación fue < 30 min | Enzima nueva (segundo frasco), pastilla nueva, 30 min completos a temperatura ambiente |
| **Los blancos salen rosas** (ΔA del blanco > ~0,02) [práctico] | Agua o material contaminado con nitrito/nitrato | Agua ultrapura recién servida, puntas nuevas, material enjuagado con agua bidestilada |
| **ΔA de la muestra menor que la del blanco** (negativo) | Blanco contaminado; o A1 y A2 leídos en distinta orientación o cubeta; o burbujas | Revisar orientación y burbujas; repetir el blanco con agua nueva |
| **Lecturas que bailan** al repetir | Burbujas, cara óptica sucia, cubeta mal asentada | Golpear, secar, recolocar y leer de nuevo |
| **Cubeta turbia o con precipitado** [práctico] | Muestra sin filtrar; o el agua muy dura del lago reacciona con el tampón fosfato | Filtrar a 0,2 µm. Si persiste con muestra filtrada, anotarlo: A2 − A1 lo corrige solo en parte |
| **ΔA > ~1,5** | Muestra demasiado concentrada | Diluir con agua bidestilada y repetir |
| **Valores muy pequeños e irregulares** | Estás en el límite de detección (0,02 mg/l), normal en P1 | Informar "< LD", sin forzar un número |
| **Nitrato negativo** (N+N < N) | Ruido en el límite de detección, o la enzima no funciona | Si el control positivo funcionó: nitrato < LD. Si no: sesión no válida para nitrato |

**Interferencias según el manual** (raras en lagos)
- Manganeso > 5 µg por cubeta: retrasa la reacción del nitrato.
- Cianuro > 1,6 µg o sulfuro > 100 µg por cubeta: inactivan la enzima.
- Cloruro: solo molesta por encima de 4,3 mg por cubeta.

---

## 10. Cuánto da el kit

| Componente | Cuánto hay | Gasto por cubeta | Cubetas |
|---|---|---|---|
| Color I y II | 2 × 8 ml cada uno | 0,25 ml | **64 en total** ← el límite |
| Pastillas | 7 | 1 por cada 12 cubetas N+N | 84 N+N |
| Enzima | 2 × 0,7 ml | 0,02 ml | 70 N+N, en dos tandas de 2 semanas |

Cada sesión gasta **2 cubetas de blancos + 2 de control positivo + 2 por muestra**.
Agrupar muestras en pocas sesiones ahorra blancos.

---

## 11. Hoja de registro

Fecha: ______ Operador: ______ Lote del kit: ______

- Enzima reconstituida el: ______
- Pastilla preparada a las: ______
- Temperatura del lab: ______ °C
- Hora de pipeteo: ______ · Hora A1: ______ · Hora A2: ______

| Nº | Cubeta | Muestra | A1 (540) | A2 (540) | ΔA = A2 − A1 | Observaciones (burbujas, turbidez, color) |
|---|---|---|---|---|---|---|
| 1 | Blanco N | — | | | | |
| 2 | Blanco N+N | — | | | | |
| 3 | N | | | | | |
| 4 | N+N | | | | | |
| 5 | N | | | | | |
| 6 | N+N | | | | | |
| 7 | N | | | | | |
| 8 | N+N | | | | | |
| 9 | N | Control + | | | | |
| 10 | N+N | Control + | | | | |
