# Field and laboratory templates

| File | Purpose |
| --- | --- |
| `field_log.csv` | 20 planned bottles: 15 primary stations plus one independent P2 field duplicate per lake. |
| `assays.csv` | 210 planned nutrient assay rows: four levels for each analyte and primary sample, plus P2 technical duplicates at 0 and 10L. |
| `chlorophyll.csv` | 15 planned chlorophyll-a reference records for the visible-signal positive control. |
| `optical_anchors.csv` | 15 planned visible-colour, optional A254, and turbidity records. |
| `field_log.pdf` | Six printable A4 landscape pages: one page per lake and one optical-reference page. |
| `assays.pdf` | Reusable printable A4 landscape assay sheet. |

The CSV headers are the required data schema. Blank cells mean that no measurement has been obtained. Do not enter zero for a missing value.

`sample_id` and `assay_id` remain immutable. `level_code` is the pre-planned design (`0`, `2L`, `5L`, `10L`), not a result. Calculate `actual_delta_mg_l` from certified stock concentration and recorded volumes. Retain the reporting species: `PO4-P` and `PO4`, `NH4-N` and `NH4`, and `NO2-N` and `NO2` are different mass bases.

`lat_wgs84` and `lon_wgs84` are signed decimal degrees. Record local clock values with the `Europe/Brussels` time zone. Write a missing-data explanation in `notes` or `qc_note`. A reference below the lower quantification limit is entered as `&lt;L` and is not replaced with a number.

Keep unmodified MonoSpectro exports under `data/raw/`; write their relative paths in the two spectrum-path columns. Retain the matching native and reacted reagent-blank files for each lot. The chlorophyll spectrum is unfiltered. A nutrient spectrum pair uses the same filtration condition before and after colour development. No fictional spectra or concentrations are included.
