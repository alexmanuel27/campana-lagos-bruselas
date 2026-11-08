> **Obsoleta desde la v3.0 (05/11/2026):** la campaña pasa a acuarios. Procedimiento diario: §5 de [PROTOCOLO_CONGELADO.md](PROTOCOLO_CONGELADO.md).

# Protocolo de campo: versión corta (v2.3)

**Un solo lago** (el más eutrófico, POR CONFIRMAR) · **6–8 puntos de orilla fijos**, los mismos cada día · **≥ 5 días** · sin barca.
Explicación completa: [PROTOCOLO_CONGELADO.md](PROTOCOLO_CONGELADO.md).
**Sin permiso escrito, no se toma agua.** Hora local con desfase `+01:00`.

## Antes del primer día (una sola vez)
- [ ] Elegir el lago y anotar el criterio en `map/sites.md`.
- [ ] Fijar P1…P8 con coordenadas y foto.
- [ ] Anotar los 2 puntos de NOx: P1 y el más alejado de P1.

## Antes de salir (cada día)
- [ ] Calibrar la sonda.
- [ ] Poner en hora MonoSpectro, ajustar la exposición (**ningún píxel saturado**) y medir el **oscuro** con esa exposición.
- [ ] Llevar:
  - sonda, cubo limpio, botellas;
  - jeringas + filtros de 0,2 µm;
  - GF/F + portafiltros + bomba, aluminio;
  - nevera, JBL;
  - MonoSpectro, fluorómetro;
  - agua destilada, garrafa de residuos, guantes.

## En cada punto
1. [ ] GPS + hora + foto.
2. [ ] Sonda **en el lago**, 0,30 m, 2 min.
3. [ ] Cubo enjuagado 3 veces y llenado sin remover el fondo. Anotar la profundidad real.
4. [ ] JBL **solo en P1 y en el punto más alejado** (los de NOx).
5. [ ] **Remover el cubo** antes de cada alícuota.
6. [ ] MonoSpectro sin filtrar, **3 réplicas**.
7. [ ] Fluorómetro sin filtrar, con blanco de agua destilada, **3 réplicas**.
8. [ ] GF/F con volumen conocido → aluminio → congelar.
9. [ ] **Antes de 15 min:** filtrar por 0,2 µm (nutrientes).
10. [ ] Guardar una porción sin filtrar. Nevera, a oscuras.

## En el laboratorio (antes de 4 h)
1. [ ] Espectrofotómetro comercial: espectro de la muestra sin filtrar y de la filtrada.
2. [ ] MonoSpectro sin filtrar otra vez, y filtrada.
3. [ ] Kits NH₄ y PO₄ sobre la porción filtrada → espectrofotómetro comercial + MonoSpectro. 5 blancos de reactivo por kit.
4. [ ] NOx (kit Roche, solo con enzima):
   - 1 blanco + los 2 puntos fijos;
   - control positivo el primer día de cada frasco de enzima y el último día;
   - día 1: además, comprobación de nitrito (1 blanco + 1 muestra sin enzima).
5. [ ] Extracción de los GF/F → espectrofotómetro comercial (ISO 10260).
6. [ ] Copiar los archivos crudos, sin tocarlos, a `data/raw/DD-MM/`.

Celda vacía = no medido · `<L` = por debajo del límite · nada vuelve al lago.
