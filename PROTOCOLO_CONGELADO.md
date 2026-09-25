# Protocolo congelado — campaña de correlación en estanques de Bruselas

**Versión 0.1 · 25 de septiembre de 2026 · prerregistro previo a campo.** Según el estado comunicado por el equipo, aún no hay muestras de esta campaña. Este commit fija el diseño y sus reglas de decisión antes de observarlas. **La congelación geográfica y de los kits no está completa:** todo elemento marcado **POR CONFIRMAR** debe cerrarse mediante un commit fechado antes de la primera muestra del 5 de octubre. Si no se cierra, no se presentará como protocolo totalmente prerregistrado. El piloto del 2 de octubre se identifica como piloto; sus datos no entran en el entrenamiento, la validación ni los resultados de campaña.

Fuente de planificación: `doctorado/Orbital/plan-sep-dic-2026.md` (C1–C4). El manuscrito vive en otro repositorio. Cualquier desviación se añade al registro final con fecha, causa y si ya se habían visto datos reales; no se reescribe la versión anterior.

## 1. Preguntas y resultados posibles

1. **Control positivo:** comprobar si el espectro sin reactivo de MonoSpectro (rango validado 420–780 nm) predice clorofila-a frente a extracción y fluorómetro independientes.
2. **Control de matriz:** evaluar si un modelo de nutrientes basado en espectro sin reactivo solo aprovecha covariación con pigmentos/color/turbidez. Una adición incolora no puede crear una banda visible propia. Una predicción que cambie al enriquecer sin que cambie el espectro exige investigar fuga de etiquetas, contaminación o un artefacto de preparación; no prueba detección del analito.
3. **Señal química:** comprobar si el *cambio espectral causado por el reactivo* responde a cantidades conocidas del nutriente y generaliza a un lago no visto. Se decide por separado para ortofosfato, amonio y nitrito. El kit comercial es la referencia, no el modelo.

No se afirmará detección directa visible de nutrientes sin reactivo. CDOM (A254) requiere un equipo UV independiente: MonoSpectro no mide 254 nm. Si no se dispone de ese equipo, se reportará solo **color visible filtrado a 440 nm**, sin llamarlo A254 ni concentración de CDOM.

## 2. Lagos, puntos y profundidad

Se estudiarán **cinco cuerpos de agua distintos**, un día por lago del **5 al 9 de octubre**, en orden L01–L05 fijado antes de salir. La selección busca contraste previo de calidad y acceso legal; no se sustituirán lagos tras ver resultados. **POR CONFIRMAR:** nombre definitivo, gestor, respuesta escrita sobre toma de agua, mapa y coordenadas WGS84 de los tres puntos de cada lago. La lista de opciones y su estado está en `SITIOS_CANDIDATOS.md`. El acceso público no equivale a permiso de extracción.

En cada lago se fijarán en mapa **tres puntos P1–P3** accesibles desde camino público y separados en lo posible ≥30 m a lo largo de la orilla: P1 en el sector de entrada de agua, P3 en el de salida y P2 a mitad del recorrido accesible. Si la entrada/salida no es identificable, se usa el extremo norte accesible como P1, el extremo sur como P3 y el punto intermedio como P2; se anotará la regla aplicada. Las coordenadas se publican antes del primer muestreo. No se entra en el agua ni se altera la orilla.

Una toma independiente por punto, a **0,30 m bajo superficie** mediante pértiga. Si el agua tiene <0,50 m, se toma a mitad de la columna siempre que queden ≥0,10 m sobre el sedimento; si no, el punto se marca no válido y no se sustituye después de medir. La profundidad real y la profundidad total se registran. Se toma además **un duplicado de campo independiente en P2 de cada lago** para control de variabilidad, sin contarlo como nueva matriz en el entrenamiento. Diseño previsto: 15 matrices primarias + 5 duplicados de campo.

## 3. Registro de cada muestra y reparto

Identificador inmutable `Lxx-Py` o `Lxx-P2-DUP`. En la toma: fecha, hora local con zona (`Europe/Brussels`), WGS84 lat/lon, punto, profundidad de toma y total, temperatura (°C), conductividad (µS/cm), pH, oxígeno disuelto (mg/L y saturación si disponible), turbidez (unidad del equipo), observaciones meteorológicas y operador. Registrar instrumentos/identificadores, calibración y lecturas fuera de rango. Todos los campos obligatorios están en `plantillas/campo.csv` y la hoja PDF.

Repartir inmediatamente con etiquetas y trazabilidad en alícuotas para: (a) clorofila sin filtrar, protegida de luz; (b) nutrientes, filtrados a 0,45 µm; (c) color visible/A254 si hay UV, filtrado a 0,45 µm; (d) PlanktoScope; (e) reserva Cruz. Volúmenes y conservación de cada destino: **POR CONFIRMAR** con los métodos de referencia antes de campo. Nunca filtrar la alícuota de clorofila antes de retener el pigmento. Registrar hora de filtración, temperatura de transporte y destino de cada alícuota.

**Puerta temporal:** las series de nutrientes y su lectura de referencia se completarán dentro del plazo más corto entre el inserto del kit y **48 h desde la toma**; el filtrado se hará en campo o al llegar, objetivo ≤2 h. Si el método elegido exige menos tiempo, manda ese tiempo. Un resultado fuera de plazo se marca inválido y no se usa para sostener capacidad cuantitativa. Esto obliga a adelantar C3.1–C3.5 del plan original, que los sitúa el 14–29 de octubre: ese calendario no es compatible sin una conservación expresamente validada. La nueva agenda se documentará antes del 2 de octubre. La referencia de clorofila sigue el protocolo P1 de Daniela y conserva la misma ID.

## 4. Instrumentación y señales

MonoSpectro: guardar CSV original `Pixel, Wavelength_nm, abs`, configuración de calibración, cubeta, trayectoria óptica, blanco, tiempo de exposición y hora. Usar 420–780 nm calibrados; no extrapolar. Por cada alícuota de nutrientes guardar **dos espectros emparejados**, antes y después de la reacción, con la misma geometría y blanco apropiado; archivo y hora de ambos en `plantillas/ensayos.csv`. Registrar lote/caducidad del kit, concentración y lote del patrón, volúmenes reales, factor de dilución, tiempo y temperatura de reacción, y lectura del fotómetro comercial. Blanco de reactivo, patrón de control y muestra sin reactivo por lote y día. No reutilizar cubeta con residuo de reactivo sin limpieza verificada.

**POR CONFIRMAR:** kit/SKU, intervalo cuantificable `[L,U]` expresado en la misma especie y unidad que el patrón, longitud de onda, cubeta, volumen, tiempo de reacción y plazo de conservación para cada analito. Griess para nitrito, Berthelot para amonio y azul de molibdeno para ortofosfato. Un candidato compatible con el rango visible es Spectroquant 1.14543 para fosfato, cuyo certificado indica 690 nm; su compra, compatibilidad de cubeta y método exacto siguen POR CONFIRMAR. Si la longitud de onda útil o la cubeta del kit no es compatible y el piloto no demuestra una respuesta en 420–780 nm, ese analito se declara no evaluable por MonoSpectro; no se cambia de química tras mirar datos de campaña.

## 5. Adición patrón y réplicas

En cada una de las 15 matrices primarias, preparar **una serie independiente para cada analito**, sin mezclar reactivos de kits. Niveles de incremento final sobre el basal: `0, 2L, 5L, 10L`, donde `L` es el límite inferior cuantificable del kit elegido, en unidades del analito declarado. Esta regla fija los niveles antes de conocer concentraciones naturales y permite expresarlos en números absolutos al cerrar el kit. La concentración final real se calcula con concentración certificada del stock y volúmenes medidos; **no se sustituye por la nominal**.

Prelectura comercial de `C0` solo para aplicar la regla de rango: si `C0 + 10L > U`, diluir **toda** la serie de esa matriz por factores 2, luego 4, con agua de calidad analítica, hasta que quepa. Si ni a 1:4 cabe, esa matriz se marca fuera de rango y se reporta sin optimizar el nivel. Igualar volumen final y fracción de disolvente añadido en los cuatro brazos usando blanco de patrón; el stock debe permitir adición ≤1 % del volumen final o se declara inviable. Registrar volúmenes exactos. Reaccionar los cuatro brazos del mismo lote en orden alternado, sin que la concentración codificada aparezca en el nombre del espectro entregado al análisis hasta cerrar QC.

En P2 de cada lago se preparan además **duplicados técnicos independientes** de los niveles `0` y `10L` para cada analito. Previsión: 15 × 3 × 4 = **180 ensayos**, más 5 × 3 × 2 = **30** duplicados técnicos; 210 ensayos y 420 espectros, más blancos/patrones. Comprar al menos **70 determinaciones por analito más blancos y controles**; disponibilidad POR CONFIRMAR. Los duplicados de campo tienen referencia y espectro nativo propios, pero no toda la serie patrón.

## 6. QC y exclusiones predefinidas

Exclusión de un espectro si falta archivo original, eje de longitud de onda no calibrado, valor no finito, saturación del detector o referencia de blanco inválida; la razón queda en una tabla auditable. Espectros de reacción fuera del tiempo del kit, estándares caducados, volumen desconocido y referencias fuera de `[L,U]` se excluyen del análisis cuantitativo, pero se cuentan. Un blanco de kit ≥L o un control comercial fuera de 80–120 % de su valor certificado invalida el lote analítico y obliga a repetirlo dentro del plazo; de lo contrario queda excluido. Duplicados a `10L` deben diferir ≤20 % respecto a su media; si fallan, se reporta la tasa y se invalida la serie de ese lago/analito hasta repetirla a tiempo. No se eliminan observaciones por valor alto/bajo o por empeorar métricas.

## 7. Particiones, modelos y métricas

La unidad independiente es el **punto de muestreo**, no el espectro ni la alícuota. Validación principal **leave-one-lake-out**: cinco pliegues; en cada uno todas las matrices, duplicados y niveles de un lago quedan fuera de ajuste, calibración estadística, selección de rasgos y normalización. El piloto queda siempre fuera. No se hace partición aleatoria por espectro. Duplicados no aumentan `n` efectivo. Mantener también la evaluación por lago, para que una media agregada no oculte un fallo.

Modelo base fijado: regresión ridge lineal con intercepto, λ=1 sobre rasgos centrados/escalados **solo con entrenamiento**; sin búsqueda de hiperparámetros sobre el lago retenido. Espectro interpolado en rejilla fija de 5 nm, 420–780 nm. Para clorofila y nutrientes nativos, usar espectro sin reactivo; para cada nutriente coloreado, usar diferencia `A_con_reactivo - A_sin_reactivo` en su longitud de onda de kit y dos vecinos ±10 nm si existen, descontando blanco de reactivo. Las comparaciones ablatorias se ejecutan con espectro, sensores, sensores+espectro, y una referencia ingenua (mediana del entrenamiento), sin usar ID de lago, hora, coordenadas ni nivel nominal como predictor. Las concentraciones enriquecidas sí son etiquetas de entrenamiento dentro de los cuatro lagos, pero se prohíbe mezclar niveles del mismo punto entre entrenamiento y prueba.

Métricas principales, calculadas solo en el lago retenido y luego agrupadas: MAE en unidad declarada, sesgo medio, `R²` solo si hay varianza suficiente, y habilidad `S = 1 - MAE_modelo/MAE_mediana`. Para adición patrón: pendiente de respuesta `b = Σ(Δreal·Δpredicha)/Σ(Δreal²)` sobre los tres niveles enriquecidos, con `Δpredicha = predicción_nivel - predicción_0` emparejada en cada matriz; reportar por lago, total y rango de duplicados. `b≈0` en el modelo sin reactivo es la expectativa física, no un éxito del método para nutrientes. Cualquier cambio de aspecto de espectro sin reactivo tras añadir stock se analiza como artefacto y se reporta; la perturbación cromática no puede atribuirse al nutriente sin controles.

## 8. Criterios de fracaso, fijados antes de datos

- **Diseño:** sin cinco lagos con extracción autorizada/aclarada y ≥2 puntos válidos por lago, o con menos de 10 matrices primarias válidas, no se hará afirmación de generalización a un lago nuevo. La falta de cinco lagos se declara incumplimiento del diseño.
- **Tiempo/QC:** si >20 % de las series de un analito son inválidas por plazo, referencia o espectros, ese analito queda **no concluyente**, no se cambia el umbral de exclusión.
- **Control positivo:** si la clorofila nativa no alcanza `S ≥ 0,25` agrupado y `S > 0` en al menos cuatro de cinco lagos, fracasa la premisa de capacidad predictiva del instrumento sobre un analito con señal visible. No se hacen afirmaciones de cuantificación espectral de nutrientes para esos datos.
- **Falsación nativa:** si `|b| > 0,20` para cualquier nutriente sin reactivo, revisar identidad de archivos, preparación, dilución y fuga. Si persiste, la cadena falla el control negativo y toda afirmación para ese nutriente es inválida. Si `|b| ≤ 0,20`, los aparentes aciertos nativos se describen como asociación de matriz, no detección.
- **Señal con reactivo:** un analito solo pasa si `0,80 ≤ b ≤ 1,20` global, `0,70 ≤ b ≤ 1,30` en al menos cuatro lagos y `S ≥ 0,25` agrupado en leave-one-lake-out. Si falla, se declara que MonoSpectro + ese kit **no cuantifica de forma transferible** ese analito en estas matrices. No se cambia a una métrica favorable tras ver datos.
- **Límite de alcance:** aunque pase, no se afirmará sensibilidad por debajo de `2L` ni causalidad sobre nutrientes sin reactivo. Un resultado publicable puede ser el fracaso documentado de la inferencia de matriz.

## 9. Pendientes bloqueantes antes de salir

1. **POR CONFIRMAR, 29/09:** los cinco lagos, gestor, respuesta sobre permiso/exención, 15 coordenadas y fotos de acceso. No se toma agua en un sitio sin aclaración del gestor.
2. **POR CONFIRMAR, 30/09:** tres SKU, rangos L/U, longitudes de onda, cubetas, inserto, existencias, patrones y plazos. Completar tabla de dosis numéricas como anexo fechado, sin cambiar la regla `0,2L,5L,10L`.
3. **POR CONFIRMAR, 01/10:** nueva agenda de lectura dentro de plazo, volumen por muestra para los cuatro destinos, reserva de fluorómetro y método de A254 o renuncia explícita a A254.
4. **02/10:** piloto técnico con muestras etiquetadas PILOTO; probar tiempo, blancos, compatibilidad óptica, volúmenes y trazabilidad.
5. **03/10:** registrar correcciones mecánicas derivadas del piloto y crear commit de versión final antes de campo. Cambios en criterios de éxito por rendimiento del piloto quedan marcados como posteriores a datos piloto.

## 10. Fuentes y registro de cambios

- Plan doctoral local citado arriba; protocolo anterior `series-Sentinel-2/PROTOCOLO_CONGELADO.md` como referencia de prerregistro.
- Bruxelles Environnement, [calidad ecológica de estanques](https://environnement.brussels/citoyen/documentation-et-outils/etat-des-lieux-de-lenvironnement/eaux-de-surface-qualite-biologie-et-emissions-de-polluants) y [gestión de estanques](https://environnement.brussels/pro/reglementation-et-inspection/obligations-et-autorisations/la-gestion-et-la-protection-des-cours-deau-non-navigables-et-des-etangs-bruxellois).
- [Ordenanza de 16/05/2019](https://refli.be/fr/lex/2019012903), [reglas de parques regionales](https://environnement.brussels/citoyen/reglementation-et-inspection/obligations-et-autorisations/que-peut-faire-et-ne-pas-faire-dans-les-parcs-regionaux-bruxellois).
- USGS, [técnica de adición patrón y sus condiciones](https://pubs.usgs.gov/twri/twri5a6/pdf/TWRI_5-A6.pdf); Merck, [certificado 1.14543 a 690 nm](https://www.merckmillipore.com/deepweb/assets/sigmaaldrich/product/documents/374/742/114543dat-mk.pdf).

| Fecha | Cambio | ¿Datos de campaña vistos? |
|---|---|---|
| 2026-09-25 | Versión 0.1: diseño, niveles relativos, validación y fracasos fijados; sitios/kits pendientes declarados | No, según estado comunicado |
