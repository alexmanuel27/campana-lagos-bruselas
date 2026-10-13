"""Genera map/lagos.pdf: tabla de lagos + mapa de situación. Uso: python3 build_pdf.py <geojson> <salida.pdf> <mapa.jpg>"""
import json, sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer

src, out = sys.argv[1], sys.argv[2]
feats = json.load(open(src))["features"]
CONTACT = {"City of Brussels": "espacesverts@brucity.be", "Brussels Environment": "info@environnement.brussels"}
sites = [(f["properties"], f["geometry"]["coordinates"][1], f["geometry"]["coordinates"][0]) for f in feats]

MAPA = sys.argv[3]  # captura del mapa (map/lagos-mapa.jpg), hecha desde sampling-map.html

ss = getSampleStyleSheet(); small = ParagraphStyle("s", parent=ss["Normal"], fontSize=8, leading=10)
link = lambda url, txt: f'<link href="{url}" color="blue"><u>{txt}</u></link>'
rows = [["ID", "Lago", "Latitud", "Longitud", "Gestor / contacto", "Permiso", "Abrir"]]
for p, lat, lon in sites:
    osm = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=17/{lat}/{lon}"
    gm = f"https://www.google.com/maps?q={lat},{lon}"
    rows.append([p["id"], Paragraph(p["name"], small), f"{lat:.6f}", f"{lon:.6f}",
                 Paragraph(f"{p['manager']}<br/>{CONTACT.get(p['manager'], '')}", small),
                 Paragraph("POR CONFIRMAR", small), Paragraph(link(osm, "OSM") + " · " + link(gm, "Google"), small)])
t = Table(rows, colWidths=[1.0*cm, 3.6*cm, 1.9*cm, 1.9*cm, 4.4*cm, 2.2*cm, 2.3*cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTSIZE", (0, 0), (-1, -1), 8), ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EEF3F8")])]))
doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm,
                        title="Lagos candidatos – campaña Bruselas")
doc.build([Paragraph("Lagos candidatos · Campaña Bruselas, 5–9 oct 2026", ss["Title"]),
    Paragraph("Coordenadas WGS84 del centro aproximado de cada lago, para planificar el acceso. No son las estaciones P1–P3: "
              "esas se registran en campo. Ningún lago tiene aún permiso de toma de agua confirmado.", ss["Normal"]),
    Spacer(1, 8), t, Spacer(1, 8), Image(MAPA, width=14*cm, height=14*cm*1120/1092),
    Paragraph("Mapa: © OpenStreetMap contributors. Versión interactiva: <b>map/sampling-map.html</b>.", small)])
print(out)
