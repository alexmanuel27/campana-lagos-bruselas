"""Regenerate empty English campaign CSV and printable PDF templates."""
import csv
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "templates"
OUT.mkdir(exist_ok=True)

FIELD_COLUMNS = """sample_id lake_id lake_name point_id field_duplicate local_date local_time time_zone lat_wgs84 lon_wgs84 collection_depth_m total_depth_m temperature_c conductivity_us_cm ph dissolved_oxygen_mg_l dissolved_oxygen_pct turbidity_value turbidity_unit operator weather probe_id probe_calibration_time turbidimeter_id turbidimeter_calibration_time filtration_time transport_temperature_c total_volume_ml aliquot_destinations notes""".split()
ASSAY_COLUMNS = """assay_id sample_id lake_id point_id analyte level_code technical_duplicate assay_date native_read_time c0_value c0_unit matrix_dilution kit_manufacturer kit_sku kit_lot kit_expiry kit_lower_limit_mg_l kit_upper_limit_mg_l reported_species kit_wavelength_nm cuvette_mm standard_lot standard_concentration_mg_l sample_volume_ml stock_volume_ml blank_volume_ml final_volume_ml actual_delta_mg_l native_spectrum_time native_spectrum_file reagent_time reacted_spectrum_time reacted_spectrum_file reaction_time_min reaction_temperature_c reagent_blank_value certified_control_value measured_control_value reference_kit_value reference_kit_unit reference_time operator qc_note native_blank_file reacted_blank_file filtered_045_um""".split()
CHLOROPHYLL_COLUMNS = "sample_id lake_id chlorophyll_ug_l uncertainty_ug_l extraction_method fluorometer_id reference_date native_spectrum_file qc_note".split()
ANCHOR_COLUMNS = "sample_id lake_id measurement_date filtration_time filter_um visible_colour_a440 colour_path_length_cm colour_instrument_id filtered_a254 uv_path_length_cm uv_instrument_id turbidity_value turbidity_unit turbidity_instrument_id qc_note".split()


def write_csv(name, columns, rows):
    with (OUT / name).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


field_rows, assay_rows, chlorophyll_rows, anchor_rows = [], [], [], []
for lake in range(1, 6):
    lake_id = f"L{lake:02}"
    for point in ("P1", "P2", "P3", "P2-DUP"):
        field_rows.append({"sample_id": f"{lake_id}-{point}", "lake_id": lake_id, "point_id": point.replace("-DUP", ""), "field_duplicate": "YES" if point.endswith("DUP") else "NO", "time_zone": "Europe/Brussels"})
    for point in ("P1", "P2", "P3"):
        sample_id = f"{lake_id}-{point}"
        chlorophyll_rows.append({"sample_id": sample_id, "lake_id": lake_id})
        anchor_rows.append({"sample_id": sample_id, "lake_id": lake_id, "filter_um": "0.45"})
        for analyte in ("orthophosphate", "ammonium", "nitrite"):
            for level in ("0", "2L", "5L", "10L"):
                assay_rows.append({"assay_id": f"{sample_id}-{analyte}-{level}", "sample_id": sample_id, "lake_id": lake_id, "point_id": point, "analyte": analyte, "level_code": level, "technical_duplicate": "NO"})
            if point == "P2":
                for level in ("0", "10L"):
                    assay_rows.append({"assay_id": f"{sample_id}-{analyte}-{level}-DUP", "sample_id": sample_id, "lake_id": lake_id, "point_id": point, "analyte": analyte, "level_code": level, "technical_duplicate": "YES"})

write_csv("field_log.csv", FIELD_COLUMNS, field_rows)
write_csv("assays.csv", ASSAY_COLUMNS, assay_rows)
write_csv("chlorophyll.csv", CHLOROPHYLL_COLUMNS, chlorophyll_rows)
write_csv("optical_anchors.csv", ANCHOR_COLUMNS, anchor_rows)

PAGE_W, PAGE_H = landscape(A4)
NAVY, GREY, MUTED = colors.HexColor("#123047"), colors.HexColor("#C9D8DE"), colors.HexColor("#5B6B78")


def title(pdf, heading, subtitle):
    pdf.setFillColor(NAVY); pdf.setFont("Helvetica-Bold", 18); pdf.drawString(32, PAGE_H - 42, heading)
    pdf.setFillColor(MUTED); pdf.setFont("Helvetica", 9); pdf.drawString(32, PAGE_H - 58, subtitle)
    pdf.setStrokeColor(GREY); pdf.line(32, PAGE_H - 68, PAGE_W - 32, PAGE_H - 68)


def line(pdf, x, y, label, width):
    pdf.setFont("Helvetica", 8); pdf.setFillColor(NAVY); pdf.drawString(x, y, label)
    pdf.setStrokeColor(GREY); pdf.line(x + stringWidth(label, "Helvetica", 8) + 5, y - 1, x + width, y - 1)


def table(pdf, x, top, widths, headers, rows, row_height):
    pdf.setFillColor(NAVY); pdf.rect(x, top - 22, sum(widths), 22, fill=1, stroke=0)
    cursor = x; pdf.setFillColor(colors.white); pdf.setFont("Helvetica-Bold", 7)
    for header, width in zip(headers, widths):
        pdf.drawString(cursor + 4, top - 14, header); cursor += width
    y = top - 22
    for row in rows:
        pdf.setStrokeColor(GREY); pdf.rect(x, y - row_height, sum(widths), row_height, fill=0, stroke=1)
        cursor = x; pdf.setFillColor(NAVY); pdf.setFont("Helvetica", 7)
        for value, width in zip(row, widths):
            pdf.drawString(cursor + 4, y - row_height / 2 - 2, str(value)); cursor += width
        y -= row_height
    return y


field_pdf = canvas.Canvas(str(OUT / "field_log.pdf"), pagesize=landscape(A4))
for lake in range(1, 6):
    lake_id = f"L{lake:02}"
    title(field_pdf, f"Field log - {lake_id}", "Complete every required field | one printed page per candidate lake")
    line(field_pdf, 32, PAGE_H - 91, "Lake name:", 310); line(field_pdf, 365, PAGE_H - 91, "Date / operator:", 420)
    line(field_pdf, 32, PAGE_H - 114, "Manager and collection condition:", 490); line(field_pdf, 544, PAGE_H - 114, "Weather:", 241)
    line(field_pdf, 32, PAGE_H - 137, "Aqua TROLL ID / calibration:", 375); line(field_pdf, 427, PAGE_H - 137, "Turbidity ID / calibration:", 358)
    field_pdf.setFillColor(NAVY); field_pdf.setFont("Helvetica-Bold", 10); field_pdf.drawString(32, PAGE_H - 164, "Collections (WGS84; depth in m; conductivity in uS/cm)")
    headers = ["ID", "Time", "Lat", "Lon", "Depth", "Total", "Temp C", "Cond.", "pH", "DO mg/L", "DO %", "Turb."]
    widths = [96, 53, 64, 64, 49, 49, 56, 60, 34, 59, 48, 62]
    rows = [[f"{lake_id}-{point}", "", "", "", "", "", "", "", "", "", "", ""] for point in ("P1", "P2", "P3", "P2-DUP")]
    y = table(field_pdf, 32, PAGE_H - 178, widths, headers, rows, 38)
    field_pdf.setFillColor(NAVY); field_pdf.setFont("Helvetica-Bold", 10); field_pdf.drawString(32, y - 24, "Filtration, custody, and aliquots")
    headers = ["ID", "Filter time", "Transport temp", "Volume mL", "Aliquots / destination", "Notes"]
    widths = [96, 105, 120, 90, 205, 178]
    rows = [[f"{lake_id}-{point}", "", "", "", "", ""] for point in ("P1", "P2", "P3", "P2-DUP")]
    y = table(field_pdf, 32, y - 36, widths, headers, rows, 28)
    field_pdf.setFillColor(MUTED); field_pdf.setFont("Helvetica", 8)
    field_pdf.drawString(32, y - 17, "Collection depth: 0.30 m; if total depth is below 0.50 m, use mid-water and remain at least 0.10 m above sediment.")
    field_pdf.drawString(32, y - 30, "Do not enter the water. Keep the P2 duplicate independent. Record nutrient chemistry on the assay sheet.")
    field_pdf.setFont("Helvetica", 7); field_pdf.drawRightString(PAGE_W - 32, 20, f"MonoSpectro Brussels lake campaign | {lake}/5")
    field_pdf.showPage()
title(field_pdf, "Optical references and co-anchors", "One row per primary matrix | chlorophyll extraction, visible colour, optional A254, and turbidity")
headers = ["Sample ID", "Chl-a ug/L", "Uncertainty", "A440", "A254 UV", "Turbidity", "Date / instrument / notes"]
widths = [95, 90, 90, 90, 90, 80, 238]
rows = [[f"L{lake:02}-P{point}", "", "", "", "", "", ""] for lake in range(1, 6) for point in range(1, 4)]
y = table(field_pdf, 32, PAGE_H - 105, widths, headers, rows, 24)
field_pdf.setFillColor(MUTED); field_pdf.setFont("Helvetica", 8)
field_pdf.drawString(32, y - 18, "A254 is recorded only with a UV instrument. MonoSpectro does not measure 254 nm. Keep the chlorophyll native spectrum unfiltered.")
field_pdf.setFont("Helvetica", 7); field_pdf.drawRightString(PAGE_W - 32, 20, "MonoSpectro Brussels lake campaign | optical references")
field_pdf.showPage(); field_pdf.save()

assay_pdf = canvas.Canvas(str(OUT / "assays.pdf"), pagesize=landscape(A4))
title(assay_pdf, "Assay and paired-spectrum log", "Copy for each lake and analyte | every row needs a native and a reacted liquid spectrum")
line(assay_pdf, 32, PAGE_H - 91, "Lake / station / date:", 350); line(assay_pdf, 403, PAGE_H - 91, "Analyte / operator:", 380)
line(assay_pdf, 32, PAGE_H - 114, "Kit manufacturer / SKU / lot / expiry:", 470); line(assay_pdf, 518, PAGE_H - 114, "L / U / species / unit:", 265)
line(assay_pdf, 32, PAGE_H - 137, "Wavelength / cuvette / blank files:", 370); line(assay_pdf, 421, PAGE_H - 137, "Standard lot / concentration:", 362)
assay_pdf.setFillColor(NAVY); assay_pdf.setFont("Helvetica-Bold", 10); assay_pdf.drawString(32, PAGE_H - 164, "Preparation: actual volumes and calculated increment")
headers = ["Assay ID", "Level", "Dup.", "Sample mL", "Stock mL", "Blank mL", "Final mL", "Actual delta", "Prep time"]
widths = [166, 55, 48, 85, 85, 85, 85, 90, 94]
y = table(assay_pdf, 32, PAGE_H - 173, widths, headers, [["", "", "", "", "", "", "", "", ""] for _ in range(6)], 21)
assay_pdf.setFillColor(NAVY); assay_pdf.setFont("Helvetica-Bold", 10); assay_pdf.drawString(32, y - 18, "Readings: paired files, reaction condition, and commercial reference")
headers = ["Assay ID", "Native time", "Native file", "Reagent time", "Reacted time", "Reacted file", "Kit value", "QC / notes"]
widths = [112, 63, 130, 74, 63, 130, 77, 144]
y = table(assay_pdf, 32, y - 25, widths, headers, [["", "", "", "", "", "", "", ""] for _ in range(6)], 21)
assay_pdf.setFillColor(MUTED); assay_pdf.setFont("Helvetica", 8)
assay_pdf.drawString(32, y - 17, "Levels: 0, 2L, 5L, 10L. At P2, repeat 0 and 10L. Store original sample and blank CSV files.")
assay_pdf.drawString(32, y - 30, "Record reaction time and temperature, reference time, and any out-of-range or QC event in the CSV.")
assay_pdf.setFont("Helvetica", 7); assay_pdf.drawRightString(PAGE_W - 32, 20, "MonoSpectro Brussels lake campaign | reusable template")
assay_pdf.showPage(); assay_pdf.save()
print(OUT)
