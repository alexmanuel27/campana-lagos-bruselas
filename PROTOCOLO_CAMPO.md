# Protocolo de campo: versión corta (v2.0)

Un lago por día, del 5 al 9 de octubre. Explicación completa y motivos: [PROTOCOLO_CONGELADO.md](PROTOCOLO_CONGELADO.md).
**Sin permiso escrito del gestor, no se toma agua.**

## Antes de salir (laboratorio)
- [ ] Calibrar la sonda (pH, conductividad, O₂) y el turbidímetro. Anotar la hora.
- [ ] Preparar los patrones de trabajo del día (fosfato, amonio, nitrito) y el control independiente.
- [ ] Etiquetar botellas y tubos: `Lxx-P1`, `Lxx-P2`, `Lxx-P3`, `Lxx-P2-DUP`.
- [ ] Llevar a la nevera: acumuladores, jeringas, filtros de 0,2 µm, filtros GF/F con portafiltros y bomba, maletín JBL, agua destilada, garrafa de residuos, guantes y hojas de campo.

## En el lago (3 estaciones: P1 entrada, P2 medio, P3 salida)
En cada estación:
1. [ ] Coordenadas GPS, hora y foto.
2. [ ] Sonda a 0,30 m: temperatura, conductividad, pH y O₂. Anotar.
3. [ ] Enjuagar la botella 3 veces y llenarla a 0,30 m. En P2, llenar una segunda botella (`DUP`).
4. [ ] **Filtrar por 0,2 µm antes de 15 min**, a los tubos de nutrientes.
5. [ ] Filtrar un volumen conocido por GF/F para la clorofila. Filtro en aluminio y congelado.
6. [ ] Guardar el agua sin filtrar en la nevera (espectro de clorofila y turbidez).
7. [ ] Cribado JBL (NH₄, NO₂, NO₃, PO₄). Anotar el valor. Residuos a la garrafa.

Al terminar, todo a la nevera, a oscuras, y anotar la hora de salida.

## En el laboratorio (empezar antes de 4 h desde la toma)
1. [ ] Espectrofotómetro de referencia: curva de calibrado (blanco + 5 patrones) y control independiente (80–120 %).
2. [ ] Turbidez y espectro **sin filtrar** en MonoSpectro (clorofila).
3. [ ] Para cada estación y analito, 4 tubos **al mismo volumen final**: 0 · 2L · 5L · 10L. En P2, repetir 0 y 10L.
4. [ ] Espectro de cada tubo en MonoSpectro **antes** del reactivo (native).
5. [ ] Añadir el reactivo según el prospecto y esperar el tiempo exacto.
6. [ ] La misma cubeta: primero MonoSpectro (reacted) y luego el espectrofotómetro de referencia.
7. [ ] Blanco de reactivo por lote: sin reactivo y con reactivo.
8. [ ] Nitrato con el kit Roche, solo en las muestras sin enriquecer.
9. [ ] Filtros de clorofila a Daniela (extracción y fluorómetro).
10. [ ] Copiar los CSV de MonoSpectro, sin tocarlos, a `data/raw/AAAA-MM-DD/`.

## Reglas que no se rompen
- La referencia es el kit leído en el espectrofotómetro. **El JBL no es referencia.**
- Celda vacía = no medido. Valor por debajo del límite del kit = `<L`. Nunca 0.
- No se excluye nada porque "salga raro". Toda exclusión se anota con su motivo.
- Nada vuelve al lago.
