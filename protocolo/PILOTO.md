# Piloto: viernes 23/10/2026

1 lago (permiso ✔): **Étang des Pêcheries / Terlindenvijver** (Auderghem; punto de referencia 50.812806, 4.412256) · 3 puntos (P1, P2, P3) · datos etiquetados **PILOTO**: no entran en el análisis.
Sin patrones: hoy **no** hay adición patrón. Hora: anotar siempre con su desfase (`+02:00`).

## Llevar
Sonda Aqua TROLL · cubo de plástico limpio (sin detergente) · botellas · jeringas + filtros de 0,2 µm · aluminio · nevera · maletín JBL · MonoSpectro + cubetas + agua destilada · fluorómetro · GPS/móvil · garrafa de residuos · guantes.

## En cada punto
1. GPS + hora + foto.
2. **Sonda en el lago** a 0,30 m, 2 min estable → guardar el registro.
3. Cubo enjuagado 3 veces con agua del punto → llenarlo sin remover el fondo. Anotar la profundidad real.
4. JBL: NH₄, NO₂, NO₃, PO₄ → anotar. Residuos a la garrafa.
5. MonoSpectro **sin filtrar** → guardar el CSV.
6. Fluorómetro con el agua **tal cual** (blanco de agua destilada una vez por sesión) → guardar el CSV de 18 canales.
7. Clorofila: **no hay filtros GF/F**. Llevar 1 L extra sin filtrar, en frío y a oscuras. Si Daniela tiene GF/F en el laboratorio, se filtra allí el mismo día y el filtro se congela; si no, la clorofila de este piloto se queda solo en fluorescencia in vivo + MonoSpectro.
8. **Antes de 15 min:** filtrar por 0,2 µm una porción para nutrientes.
9. Guardar también una porción **sin filtrar**. Todo a la nevera, a oscuras.

Anotar en cada porción el volumen y la hora de toma y de filtrado.

## En el laboratorio (empezar antes de 4 h)
1. Ruido: agua destilada en MonoSpectro, 5 lecturas.
2. MonoSpectro de la porción **sin filtrar** otra vez (sirve para ver cuánto cambia en el traslado).
3. Para cada punto y cada kit, sobre la porción **filtrada**: MonoSpectro → reactivo según el prospecto (tiempo exacto) → MonoSpectro → **espectrofotómetro comercial con la misma cubeta**.
4. Blanco de reactivo (agua destilada + reactivo), 5 veces por kit, leído en los dos equipos.
5. **Dilución en P2** (100 / 50 / 25 % con agua destilada), con los 3 kits.
6. Copiar los archivos crudos, sin tocarlos, a `data/raw/2026-10-23_PILOTO/`.

## Luz verde para la campaña (fijado antes del piloto)
| Prueba | Pasa si |
|---|---|
| Color de cada kit | Señal neta > media del blanco + 3 desviaciones típicas del blanco, en al menos 1 de los 3 puntos |
| Dilución | 50 % → 0,5 ± 0,1 y 25 % → 0,25 ± 0,1 de la señal neta del 100 % |
| MonoSpectro frente al espectrofotómetro comercial | Mismo orden de las señales y relación aproximadamente lineal |
| Traslado | El espectro sin filtrar del laboratorio se parece al de campo; si no, anotar cuánto cambia |
| Logística | 3 puntos y todo el laboratorio caben en un día |

Si una prueba no pasa, se decide antes de la campaña: más volumen de muestra, cubeta más larga o declarar el analito no evaluable.
