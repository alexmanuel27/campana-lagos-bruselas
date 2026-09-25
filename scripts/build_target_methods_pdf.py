"""Build the English pre-field measurement decision sheet."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "target-compounds-and-methods.pdf"
OUTPUT.parent.mkdir(exist_ok=True)

NAVY = colors.HexColor("#123047")
TEAL = colors.HexColor("#047C86")
PALE = colors.HexColor("#EAF4F5")
INK = colors.HexColor("#22313F")
MUTED = colors.HexColor("#5B6B78")
LINE = colors.HexColor("#C9D8DE")
WARN = colors.HexColor("#FFF2D6")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCampaign", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=22, leading=26, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Subhead", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
    leading=13, textColor=MUTED, alignment=TA_CENTER, spaceAfter=12,
))
styles.add(ParagraphStyle(
    name="SectionCampaign", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=13, leading=16, textColor=NAVY, spaceBefore=7, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="BodyCampaign", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.3,
    leading=11.2, textColor=INK, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="SmallCampaign", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.1,
    leading=8.8, textColor=INK,
))
styles.add(ParagraphStyle(
    name="TableHead", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.1,
    leading=8.4, textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.5,
    leading=11.5, textColor=NAVY,
))


def p(text, style="BodyCampaign"):
    return Paragraph(text, styles[style])


def section(title):
    return Paragraph(title, styles["SectionCampaign"])


def grid(rows, widths, header=True, font_size=7.1):
    converted = []
    for index, row in enumerate(rows):
        style = "TableHead" if header and index == 0 else "SmallCampaign"
        converted.append([Paragraph(str(cell), styles[style]) for cell in row])
    table = Table(converted, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        commands += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    for i in range(1 if header else 0, len(rows)):
        if i % 2 == 0:
            commands.append(("BACKGROUND", (0, i), (-1, i), PALE))
    table.setStyle(TableStyle(commands))
    return table


def bullet(text):
    return p(f"<b>-</b> {text}")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(18 * mm, 9 * mm, "MonoSpectro Brussels Lake Correlation Campaign | pre-field decision sheet")
    canvas.drawRightString(A4[0] - 18 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


story = [
    Spacer(1, 8 * mm),
    p("TARGET COMPOUNDS AND MEASUREMENT PLAN", "TitleCampaign"),
    p("English pre-field purchasing and method decision sheet | MonoSpectro Brussels Lake Correlation Campaign", "Subhead"),
    Table([[p("<b>Purpose.</b> Define what is measured, with which instrument, and which liquid reagents are required. The list supports the campaign's paired-spectrum and standard-addition falsification test; it contains no field results.", "Callout")]], colWidths=[174 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE), ("BOX", (0, 0), (-1, -1), 0.8, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ])),
    Spacer(1, 5 * mm),
    section("1. Measurement system at a glance"),
    grid([
        ["Measurement", "Campaign instrument", "Role in the evidence chain", "Consumables or reference"],
        ["Temperature, conductivity, pH, dissolved oxygen, turbidity", "Aqua TROLL, using the modules already configured", "In-situ context and sensor ablation; not a nutrient reference", "Calibration standards and maintenance supplies specified by the Aqua TROLL configuration"],
        ["Native visible spectrum", "MonoSpectro", "Chlorophyll-a positive control and matrix-correlation test", "Clean cuvettes, blank water, original CSV export, calibration record"],
        ["Chlorophyll-a", "MonoSpectro plus independent extraction and fluorometer", "Positive control with a genuine visible pigment signal", "Glass-fibre filters, validated extraction solvent and fluorometer calibration material from the laboratory method"],
        ["Filtered visible colour", "MonoSpectro at 440 nm", "Co-anchor and matrix descriptor", "0.45 um filter and blank water; A254 needs a separate UV instrument"],
        ["Orthophosphate, ammonium, nitrite", "MonoSpectro after a liquid colour reaction; kit result as reference", "Standard-addition test of a reagent-created signal", "One liquid colorimetric kit and certified standard per analyte, matched blank, control, and compatible cuvette"],
    ], [35 * mm, 39 * mm, 54 * mm, 46 * mm]),
    Spacer(1, 4 * mm),
    p("<b>Rule:</b> MonoSpectro is not an A254 instrument. It measures the native visible spectrum and, for nutrients, the liquid colour generated after reagent addition. Every nutrient aliquot keeps a native spectrum, a reacted spectrum, and paired reagent blanks."),
    section("2. Target compounds and reagent routes"),
    grid([
        ["Target", "Liquid reaction and useful visible region", "Minimum purchase for a defensible measurement", "Compatibility decision"],
        ["Orthophosphate", "Molybdate chemistry (molybdate, acid, reducer; some variants include antimony). Select a kit whose insert specifies a reading within 430-770 nm.", "Sealed liquid/tablet/powder kit for a cuvette, certified phosphate standard, reagent blank, control, 0.45 um filter if required.", "Do not select a classic 880 nm PhosVer 3 configuration for MonoSpectro. Confirm the exact kit wavelength before purchase."],
        ["Ammonium", "Salicylate/indophenol (Berthelot family): salicylate, hypochlorite, catalyst and alkaline buffer. A common colourimetric setting is near 655 nm.", "Cuvette-compatible ammonia/ammonium colour kit, certified standard, reagent blank, control, compatible pipettes.", "Potentially compatible with MonoSpectro. Confirm the kit's stated wavelength, range, species, and reaction condition."],
        ["Nitrite", "Griess diazotization: sulfanilamide and N-(1-naphthyl)ethylenediamine in acid. A common setting is near 515 nm.", "Cuvette-compatible nitrite colour kit, certified nitrite standard, reagent blank, control, compatible pipettes.", "Compatible in principle with MonoSpectro's visible range. Confirm the exact kit procedure and reporting basis."],
        ["Chlorophyll-a", "No colour reagent for the native-spectrum test. Independent extraction and fluorometer value are the reference.", "Follow Daniela's validated extraction/fluorometer protocol; keep the native MonoSpectro aliquot unfiltered before pigment retention.", "Required positive control. Failure prevents nutrient quantification claims."],
    ], [28 * mm, 50 * mm, 53 * mm, 43 * mm]),
    PageBreak(),
    Spacer(1, 7 * mm),
    section("3. Paper strips and a handheld Raman: what they can and cannot do"),
    grid([
        ["Option", "Useful role", "Why it cannot be the campaign's nutrient reference", "Decision"],
        ["Paper test strips", "Cheap screening, station triage, and a rough field note.", "They are normally read by visual comparison or strip reflectance. They do not provide the paired liquid absorbance spectrum, reagent blank, certified concentration, or standard-addition response required by this protocol.", "Buy only if a quick screening aid is useful. Do not use as the reference concentration or as the primary spectral chemistry."],
        ["Handheld Raman", "Potential future research instrument for a separate, well-funded project on chemical fingerprinting or supported Raman methods.", "Conventional Raman scattering is weak for dilute aqueous ions and natural-water fluorescence/background can dominate. Low-concentration Raman studies commonly require longer integrations, pre-concentration, enhanced Raman substrates, or a dedicated validation programme. It does not replace the planned liquid colour reactions.", "Do not buy it for this campaign's phosphate, ammonium, and nitrite evidence chain. Consider only with a separate budget, liquid-cell workflow, standards, and validation plan."],
        ["Cuvette liquid colour kits", "Matched before/after MonoSpectro spectra, kit reference, blanks, controls, and standard additions.", "They still require careful lot control, a compatible wavelength, exact reporting species, and a certified standard.", "Minimum defensible purchase for the nutrient triad."],
    ], [30 * mm, 38 * mm, 68 * mm, 38 * mm]),
    Spacer(1, 4 * mm),
    Table([[p("<b>Recommended low-cost route.</b> Keep the Aqua TROLL and MonoSpectro already available. Purchase one small cuvette-compatible liquid colour kit for each nutrient plus the three certified standards, blanks, and controls. Use paper strips only as a non-quantitative screening note. Do not redirect this campaign's budget to a handheld Raman.", "Callout")]], colWidths=[174 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WARN), ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#C98500")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ])),
    section("4. Purchase checklist"),
    KeepTogether([
        bullet("Existing instruments: MonoSpectro, Aqua TROLL, and the laboratory fluorometer/extraction path for chlorophyll-a."),
        bullet("Three cuvette-compatible liquid colorimetric kits: orthophosphate, ammonium, and nitrite. Choose the exact product only after the manufacturer insert confirms wavelength, range, species/unit, cuvette path, filtration, reaction time, and preservation condition."),
        bullet("Three certified standards on the same reporting basis as the selected kit, plus reagent blanks and control material."),
        bullet("Class A or calibrated pipettes, clean compatible cuvettes, labels, blank water, and filters only where the kit method requires them."),
        bullet("For every selected kit, retain the insert, SKU, lot, expiry, wavelength, reaction condition, and the original spectrum file paths in `templates/assays.csv`."),
    ]),
    section("5. Pre-purchase acceptance test"),
    grid([
        ["Check", "Accept only if"],
        ["Spectral range", "The reaction's stated reading wavelength is inside MonoSpectro's calibrated 420-780 nm range. Use a practical 430-770 nm acceptance window for the three-point feature around the kit wavelength."],
        ["Liquid measurement", "The reaction occurs in a cuvette or equivalent liquid cell. A paper strip alone is not accepted."],
        ["Quantification", "The kit declares a lower limit L and reporting species/unit. A certified standard is available on the same basis."],
        ["Controls", "Native and reacted reagent blanks plus a certified control can be run for every lot."],
        ["Economy", "Compare local price per usable assay after applying all the checks above. The cheapest product that fails a check is not a usable campaign method."],
    ], [40 * mm, 134 * mm]),
    Spacer(1, 4 * mm),
    section("Evidence notes"),
    p("Hach documentation describes nitrite diazotization read at 515 nm, ammonia salicylate methods near 655 nm, and orthophosphate configurations that may be near 600 nm or, for classic PhosVer 3, 880 nm. The 880 nm version is outside MonoSpectro's range. Raman water-monitoring reviews show that low-concentration work can require fluorescence suppression, pre-concentration, or enhanced Raman methods. Confirm current manufacturer inserts and prices before ordering."),
    p("Sources: Hach method 8048 PhosVer 3 documentation; Hach DR300 parameter sheet; Hach nitrite TNT method; Qi et al., <i>Raman Spectroscopy for In-Line Water Quality Monitoring - Instrumentation and Potential</i>, Sensors 2014. Links are retained in the repository's protocol and decision history.", "SmallCampaign"),
]

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
    topMargin=16 * mm, bottomMargin=20 * mm, title="Target compounds and measurement plan",
    author="MonoSpectro Brussels Lake Correlation Campaign",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
