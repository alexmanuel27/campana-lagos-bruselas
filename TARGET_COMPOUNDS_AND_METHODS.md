# Target compounds and measurement plan

This editable pre-field decision sheet defines what is measured, with which instrument, and which liquid reagents are required. It supports the paired-spectrum and standard-addition falsification test. It contains no field results.

## Measurement system

| Measurement | Campaign instrument | Role | Consumables or reference |
| --- | --- | --- | --- |
| Temperature, conductivity, pH, dissolved oxygen, turbidity | Aqua TROLL with the configured modules | In-situ context and sensor ablation; not a nutrient reference | Calibration standards and maintenance supplies required by the Aqua TROLL configuration |
| Native visible spectrum | MonoSpectro | Chlorophyll-a positive control and matrix-correlation test | Clean cuvettes, blank water, original CSV export, calibration record |
| Chlorophyll-a | MonoSpectro plus independent extraction and fluorometer | Positive control with a genuine visible pigment signal | Glass-fibre filters, laboratory-validated extraction solvent, fluorometer calibration material |
| Filtered visible colour | MonoSpectro at 440 nm | Co-anchor and matrix descriptor | 0.45 um filter and blank water; A254 needs a separate UV instrument |
| Orthophosphate, ammonium, nitrite | MonoSpectro after a liquid colour reaction; kit result as reference | Standard-addition test of a reagent-created signal | One liquid colorimetric kit and certified standard per analyte, paired blanks, controls, compatible cuvettes |

MonoSpectro is not an A254 instrument. Every nutrient aliquot needs a native spectrum, a reacted spectrum, and paired native/reacted reagent blanks.

## Target compounds and reagent routes

| Target | Liquid reaction | Minimum purchase | Acceptance rule |
| --- | --- | --- | --- |
| Orthophosphate | Molybdate chemistry: molybdate, acid, reducer, and sometimes antimony | Cuvette-compatible colour kit, certified phosphate standard, reagent blank, control, and 0.45 um filter if required | The manufacturer insert must specify a reading in MonoSpectro's 430-770 nm practical range. Do not select a classic 880 nm PhosVer 3 configuration. |
| Ammonium | Salicylate/indophenol (Berthelot family): salicylate, hypochlorite, catalyst, alkaline buffer | Cuvette-compatible ammonia/ammonium kit, certified standard, reagent blank, control, compatible pipettes | Confirm wavelength, range, reporting species/unit, and reaction condition. A common colourimetric setting is near 655 nm. |
| Nitrite | Griess diazotization: sulfanilamide and N-(1-naphthyl)ethylenediamine in acid | Cuvette-compatible nitrite kit, certified standard, reagent blank, control, compatible pipettes | Confirm the method and reporting basis. A common colourimetric setting is near 515 nm. |
| Chlorophyll-a | No colour reagent for the native-spectrum test | Daniela's validated extraction/fluorometer method | Required positive control. If it fails, no nutrient quantification claim is made. |

## Paper strips and handheld Raman

| Option | Useful role | Decision for this campaign |
| --- | --- | --- |
| Paper test strips | Cheap station screening and rough field notes | Do not use as the reference concentration or primary spectral chemistry. Strips are usually read visually or by reflectance and do not provide the paired liquid spectrum, reagent blank, certified result, or standard-addition response required here. |
| Handheld Raman | Potential future instrument for a separately funded chemical-fingerprinting project | Do not buy for this nutrient evidence chain. Conventional Raman is weak for dilute aqueous ions and water matrices can introduce fluorescence/background; low-concentration work often requires dedicated validation, pre-concentration, or enhanced Raman methods. It does not replace the planned liquid colour reactions. |
| Cuvette liquid colour kits | Before/after MonoSpectro spectra, kit reference, blanks, controls, and standard additions | Minimum defensible purchase for orthophosphate, ammonium, and nitrite. |

## Recommended low-cost route

Use the existing Aqua TROLL and MonoSpectro. Purchase one small cuvette-compatible liquid colour kit for each nutrient, plus three certified standards, reagent blanks, controls, compatible pipettes, clean cuvettes, labels, blank water, and filters only where the selected method requires them.

Use paper strips only as non-quantitative screening. Do not redirect this campaign's budget to a handheld Raman.

## Pre-purchase acceptance test

| Check | Accept only if |
| --- | --- |
| Spectral range | The kit wavelength lies inside MonoSpectro's calibrated 420-780 nm range; use 430-770 nm for the three-point feature around the kit wavelength. |
| Liquid measurement | The reaction occurs in a cuvette or equivalent liquid cell. A paper strip alone is not accepted. |
| Quantification | The kit declares lower limit `L` and reporting species/unit, and a certified standard is available on the same basis. |
| Controls | Native and reacted reagent blanks plus a certified control can be run for each lot. |
| Economy | Compare local cost per usable assay after all checks. A cheaper product that fails a check is not a usable campaign method. |

For every selected kit, retain the insert, SKU, lot, expiry, wavelength, reaction condition, and original spectrum paths in `templates/assays.csv`.

## Evidence notes

Hach documents nitrite diazotization at 515 nm and salicylate ammonia methods near 655 nm. Orthophosphate kits vary: some configurations are compatible with visible instruments around 600 nm, while classic PhosVer 3 procedures read at 880-890 nm and are outside MonoSpectro's range. Confirm the current manufacturer insert before ordering.

Sources: [Hach nitrite method](https://cdn.hach.com/7FYZVWYB/at/pbtkfsv3693przvh2wmpc4js/Nitrite_TNT839_Method_with_SBS.pdf), [Hach pocket colourimeter parameter sheet](https://nz.hach.com/family-print.pdf.jsa?productCategoryId=54949031370), [Hach PhosVer 3 procedure](https://cdn.hach.com/7FYZVWYB/at/jbvj4tt7k9s4mpjv4c95cn8z/DR_2000_Spectrophotometer_Procedures_Manual__O-Z.pdf), and [Raman water-quality monitoring review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4208224/).
