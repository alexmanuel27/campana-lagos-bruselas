# Frozen protocol - Brussels lake correlation campaign

**Version 1.0 - 25 September 2026 - committed before campaign water is collected.** No campaign samples had been collected when this version was written. It fixes the design and decision rules before field data are observed. The manuscript is maintained in a separate repository.

Any departure is added to the change record with its date, reason, and whether campaign data had already been seen. Earlier text is not rewritten.

## 1. Questions and admissible claims

1. **Positive control.** Can a native MonoSpectro spectrum in the calibrated 420-780 nm range predict chlorophyll-a against an independent extraction and fluorometer reference?
2. **Matrix control.** Does a native-spectrum nutrient model only exploit covariation with pigments, colour, or turbidity? A colourless standard addition must not create a nutrient-visible band in the native spectrum. A prediction that changes after such an addition requires an artefact investigation; it does not establish nutrient detection.
3. **Chemical signal.** Does the spectrum change caused by the colour reagent respond to known nutrient additions and transfer to an unseen lake? Orthophosphate, ammonium, and nitrite are assessed independently. The commercial kit is the reference measurement, not the model.

Native visible spectra will not be claimed to directly detect a nutrient. A254 requires a separate UV instrument; if one is unavailable, the study reports filtered visible colour at 440 nm only and does not label it A254 or a CDOM concentration.

## 2. Candidate sites, stations, and depth

The candidate water bodies are fixed in [SAMPLING_SITES.md](SAMPLING_SITES.md). Their planning centres are visible in [docs/sampling-map.html](docs/sampling-map.html). A candidate can be sampled only after its manager confirms the collection condition. There is no site substitution after campaign field data have been observed.

At each sampled lake, define three accessible shoreline stations: P1 near an identifiable inflow, P3 near an identifiable outflow, and P2 between them. Where inflow or outflow cannot be identified, use the accessible north end for P1, south end for P3, and a midpoint for P2; record that rule. Aim for at least 30 m separation where site geometry allows. Record the final WGS84 coordinates, access route, and depth for every station. Do not enter the water or disturb the shoreline.

Collect one independent bottle at each station at 0.30 m below the surface. If total depth is below 0.50 m, collect at mid-water while remaining at least 0.10 m above sediment; otherwise mark the station invalid. Collect one independent P2 field duplicate per lake. The planned design is 15 primary matrices and five field duplicates.

## 3. Sample record and allocation

Use the immutable identifiers `Lxx-Py` and `Lxx-P2-DUP`. Record date, local time, WGS84 location, collection and total depth, temperature, conductivity, pH, dissolved oxygen, turbidity, weather, operator, instrument IDs, calibration state, and observations. The required fields are defined in `templates/field_log.csv`.

Split every primary bottle with labels and traceability for: unfiltered chlorophyll-a and its native spectrum; nutrients; filtered colour or A254 when available; PlanktoScope; and a reserve aliquot. Record filtration time, transport temperature, volumes, and destination. Nutrient pre- and post-reaction spectra must come from the same filtration condition and the same prepared aliquot. Do not subtract a filtered spectrum from an unfiltered spectrum.

Follow the kit's preservation and reaction instructions. If a nutrient result is outside the documented holding condition, mark it invalid for quantitative analysis. Method-specific reaction and preservation windows are experimental validity controls, not project-delivery dates.

## 4. Instrument records and paired spectra

Preserve each raw MonoSpectro CSV with `Pixel`, `Wavelength_nm`, and `abs`, along with calibration configuration, cuvette, optical path, blank, exposure, and measurement time. Use only the calibrated 420-780 nm range.

For each nutrient preparation retain two paired spectra: native and reacted. Record both file paths, the paired native and reacted reagent blanks, kit manufacturer/SKU/lot/expiry, certified-standard lot and concentration, actual volumes, dilution, reaction time and temperature, and commercial-kit result. Include a reagent blank, control standard, and native sample in every kit lot. Do not reuse a cuvette carrying reactant residue without verified cleaning.

The intended chemistries are Griess for nitrite, Berthelot for ammonium, and molybdenum blue for orthophosphate. Kit SKU, reporting species/unit, quantification range, cuvette, wavelength, filtration requirement, and optical compatibility remain **TO CONFIRM** before use. If a kit cannot produce a valid response in MonoSpectro's calibrated range, that analyte is reported as not evaluable by MonoSpectro.

## 5. Standard additions and replication

For every primary matrix, prepare an independent series for each analyte without mixing kit reagents. The final increments over the native matrix are `0`, `2L`, `5L`, and `10L`, where `L` is the kit's lower quantification limit in the declared analyte species and unit. Record the certified stock concentration, actual volumes, total volume, dilution, and calculated `actual_delta_mg_l`.

At P2, prepare independent technical duplicates at `0` and `10L` for each analyte. Planned volume: 15 primary matrices x 3 analytes x 4 levels = 180 assays, plus 5 lakes x 3 analytes x 2 technical duplicates = 30 assays. Each assay has two sample spectra, before and after reaction, plus documented blanks and controls.

## 6. Predefined QC and exclusions

Exclude a spectrum from quantitative analysis if its original file is missing, wavelength axis is uncalibrated or non-monotonic, values are non-finite, the detector is saturated, or the paired blank is invalid. Exclude a kit series with an expired standard, unknown volume, out-of-range reference, or a reaction outside the kit's documented condition; retain it and its exclusion reason in the audit trail.

A kit blank at or above `L`, or a certified control outside 80-120% of its certified value, invalidates that analytical lot. Technical duplicate results at `10L` must agree within 20% of their mean; otherwise report the failure rate and invalidate that lake/analyte series unless it can be repeated within the kit condition. `&lt;L` and `&lt;LOQ` references are censored, retained, and never numerically imputed. No observation is excluded merely because it is high, low, or worsens a metric.

## 7. Partitions, models, and metrics

The independent unit is a sampling station, never a spectrum or aliquot. Primary validation is **leave-one-lake-out**: all matrices, duplicates, and levels from the held lake remain outside fitting, scaling, feature selection, and calibration. No random spectrum split is used. Technical and field duplicates never increase the effective training count. Results are reported overall and per held lake.

The fixed model is linear ridge regression with intercept and alpha = 1.0. Inputs are centred and scaled using training data only. Spectra are interpolated to 420-780 nm at 5 nm spacing. Chlorophyll-a and native nutrient models use the native spectrum. Each reacted nutrient model uses `(reacted sample - native sample) - (reacted blank - native blank)` at the kit wavelength and the two neighbours at plus/minus 10 nm. Ablations compare spectrum, in-situ sensors, spectrum-plus-sensors, and the training-median baseline. Lake ID, time, coordinates, and nominal addition level are never features.

Held-lake metrics are MAE, mean bias, R2 when variance permits it, and skill `S = 1 - MAE_model / MAE_median`. The standard-addition response slope is `b = sum(delta_real * delta_predicted) / sum(delta_real^2)`, where `delta_predicted` is paired to the 0-level prediction within each matrix. Report it overall, by lake, and across technical duplicates.

## 8. Predefined failure criteria

- Fewer than five legally cleared lakes with at least two valid stations each, or fewer than ten valid primary matrices, fails the new-lake generalization design.
- If more than 20% of series for an analyte are invalid for holding condition, reference, or spectra, that analyte is **inconclusive**.
- If native chlorophyll-a does not reach pooled `S >= 0.25` and `S > 0` in at least four held lakes, MonoSpectro has failed its visible-signal positive control. No nutrient quantification claim is made from those campaign data.
- For a native nutrient model, `|b| > 0.20` triggers an investigation of file identity, preparation, dilution, and label leakage. If it persists, the negative control fails and any claim for that nutrient is invalid. If `|b| <= 0.20`, native apparent accuracy is reported as a matrix association, not nutrient detection.
- A reacted nutrient model passes only with pooled `0.80 <= b <= 1.20`, `0.70 <= b <= 1.30` in at least four held lakes, and pooled leave-one-lake-out `S >= 0.25`. Otherwise MonoSpectro plus that kit does not quantify that analyte transferably in these matrices.
- Passing a reacted-signal test does not establish sub-`2L` sensitivity or a causal native-spectrum nutrient signal. A documented failure of matrix inference is a valid result.

## 9. Record of dependencies

Before a candidate lake is sampled, record its manager's collection condition, final P1-P3 coordinates, access evidence, and any restrictions. Before an analyte is interpreted, record kit/SKU, range, wavelength, cuvette, reporting basis, reaction and preservation instructions, standards, and optical compatibility. A pilot, if used, is explicitly labelled and excluded from campaign training, validation, and results.

## 10. Sources and change record

- Doctoral planning file: `doctorado/Orbital/plan-sep-dic-2026.md`; precedent: `series-Sentinel-2/PROTOCOLO_CONGELADO.md`.
- [Brussels Environment: surface-water context](https://environnement.brussels/citoyen/documentation-et-outils/etat-des-lieux-de-lenvironnement/eaux-de-surface-qualite-biologie-et-emissions-de-polluants) and [pond management](https://environnement.brussels/pro/reglementation-et-inspection/obligations-et-autorisations/la-gestion-et-la-protection-des-cours-deau-non-navigables-et-des-etangs-bruxellois).
- [Regional water ordinance](https://refli.be/fr/lex/2019012903) and [regional park rules](https://environnement.brussels/citoyen/reglementation-et-inspection/obligations-et-autorisations/que-peut-faire-et-ne-pas-faire-dans-les-parcs-regionaux-bruxellois).
- [US EPA holding-time guidance](https://www.epa.gov/hw-sw846/holding-time-preservation), [USGS standard-addition method](https://pubs.usgs.gov/twri/twri5a6/pdf/TWRI_5-A6.pdf), and [Merck phosphate kit certificate](https://www.merckmillipore.com/deepweb/assets/sigmaaldrich/product/documents/374/742/114543dat-mk.pdf).

| Date | Change | Campaign data seen? |
| --- | --- | --- |
| 2026-09-25 | Version 1.0: English repository structure, named candidate sites, planning-centre map, standard additions, validation, and failure criteria fixed. | No |
