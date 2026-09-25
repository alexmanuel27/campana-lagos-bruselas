# Setup and data contract

## Software

Python 3.10+ and NumPy are sufficient. The analysis does not use scikit-learn or external services.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
```

MonoSpectro is installed and calibrated through its own repository. Its expected export has `Pixel`, `Wavelength_nm`, and `abs` columns covering the calibrated 420-780 nm range. Store original exports unchanged under `data/raw/`.

## Before collecting water

- Confirm the manager and water-collection condition for each candidate site. Public access is not a collection permission.
- Confirm each assay kit's manufacturer, SKU, lot, reporting species and unit, lower and upper quantification limits, wavelength, cuvette, reaction time, preservation condition, and compatible certified standard.
- Confirm the temperature, conductivity, pH, dissolved-oxygen, turbidity, and chlorophyll reference instruments.
- Set up cuvettes, reagent blanks before and after reaction, 0.45 um filters where required by the kit, labels, transport storage, and aliquots.
- Test the optical workflow with a clearly labelled pilot if one is used. Pilot data are excluded from campaign training, validation, and results.

## Analysis inputs

The CSV files in `templates/` are empty schemas. Copy completed versions into `data/processed/` without changing the headers or identifiers.

- `assays.csv`: paired native/reacted spectra, paired reagent blanks, kit reference result, real standard-addition increment, and method metadata. A technical duplicate is retained for QC and never enlarges the training set.
- `chlorophyll.csv`: unfiltered native spectrum and the independent chlorophyll-a reference for each primary sample.
- `field_log.csv`: location, collection depth, metadata, and in-situ sensors. It enables the sensor and spectrum-plus-sensor ablations.
- `optical_anchors.csv`: filtered visible colour at 440 nm, A254 only when a UV instrument exists, and turbidity.

For a nutrient assay, the analysis subtracts the paired reagent blank:

```text
(reacted sample - native sample) - (reacted blank - native blank)
```

It extracts the kit wavelength and its two neighbouring points at plus/minus 10 nm. Native and reacted spectra must use the same filtration condition. `&lt;L` or `&lt;LOQ` references are retained as censored records and are never numerically imputed. Chemical species are not converted automatically: for example, `PO4-P` and `PO4` remain distinct reporting bases.
