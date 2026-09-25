# Campaña de correlación · estanques de Bruselas

Repositorio de **protocolo, hojas de campo, espectros, referencias, análisis y resultados** de la campaña MonoSpectro del 5–9 de octubre de 2026. El manuscrito se redacta en otro repositorio.

## Estado real · 25/09/2026

- `PROTOCOLO_CONGELADO.md` versión **0.1**, commiteado antes de campo: diseño, réplicas, adiciones, particiones, métricas y criterios de fracaso fijados. **Aún no es congelación completa**: faltan sitios/coordenadas, respuesta del gestor, kits y agenda compatible con conservación de nutrientes. Cerrar todo antes del 5/10 en un nuevo commit fechado.
- `SITIOS_CANDIDATOS.md` propone cinco estanques municipales con acceso público. **No se ha verificado que la extracción de agua esté exenta de permiso** ni que constituyan un gradiente trófico.
- Hojas imprimibles y CSV de campo/laboratorio listas. Los CSV contienen **solo diseño prellenado**, ningún dato medido.
- Cadena de análisis y cinco pruebas sintéticas incluidas. Las pruebas distinguen correlación de matriz de señal creada por reactivo. **No hay muestras ni resultados de campo** en este repositorio, según el estado declarado al iniciar el trabajo.

## Riesgo de calendario que requiere acción

El plan doctoral sitúa las reacciones y lecturas comerciales del 14–29 de octubre, después de la toma del 5–9. El protocolo exige completar la serie dentro del plazo más corto entre el inserto del kit y 48 h; para ello hay que medir durante la semana de campo o validar por escrito una conservación alternativa antes de recoger agua. Si no, los resultados de nutrientes quedan inválidos según el prerregistro.

## Estructura

- `src/analisis.py`: lectura de CSV originales de MonoSpectro, diferencia con blanco, regresión ridge, validación dejando fuera un lago, ablación de sensores y pendientes de adición.
- `tests/test_sintetico.py`: escenarios sin señal propia y con señal coloreada; control positivo de clorofila.
- `datos/crudo/`: exportaciones sin modificar y lecturas instrumentales originales.
- `datos/procesado/`: copias completadas de las tablas enlazadas a crudo, con decisiones de QC documentadas.
- `datos/productos/`: tablas procesadas derivadas; `resultados/`: métricas reales cuando existan.
- `plantillas/`: CSV planificados y PDF para imprimir.

## Uso

1. Leer `PROTOCOLO_CONGELADO.md`, `SITIOS_CANDIDATOS.md` e `INSTALACION.md`.
2. Confirmar gestores, lagos, 15 puntos, kits, volúmenes, conservación y agenda; registrar cada cierre en el protocolo **antes de la primera muestra**.
3. Imprimir `plantillas/hoja_campo.pdf` y `plantillas/hoja_ensayos.pdf`. Copiar CSV a `datos/procesado/` al comenzar a registrar; mantener las plantillas originales sin datos reales.
4. Con el conjunto completo y QC cerrado, ejecutar:

```sh
python3 -m unittest discover -s tests -v
python3 -m src.analisis datos/procesado/ensayos.csv --clorofila datos/procesado/clorofila.csv --campo datos/procesado/campo.csv --root . --salida resultados/validacion.json
```

La segunda orden **debe fallar** si faltan espectros o referencias; no genera resultados a partir de plantillas vacías. `validacion.json` resume métricas y pendientes, no asigna por sí solo un veredicto: compárese con la sección 8 del protocolo y registre exclusiones y QC.
