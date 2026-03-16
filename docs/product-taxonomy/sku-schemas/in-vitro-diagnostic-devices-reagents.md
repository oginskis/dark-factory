# SKU Schema: In-Vitro Diagnostic Devices & Reagents

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.ivd_reagents`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer catalog or part number | 06531853190, 04489357190, 309589 |
| Product Name | product_name | text | — | Full product name including analyte or system designation | cobas c 311 Analyzer, Roche Cholesterol Gen.2 Reagent, Abbott i-STAT CG4+ Cartridge |
| URL | url | text | — | Direct link to the product page | https://example.com/product/cobas-c-311 |
| Price | price | number | — | List or catalog price per unit or per kit | 125.00, 450.00, 85000.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Type | product_type | enum | — | Broad IVD product classification | Analyzer/Instrument, Reagent Kit, Calibrator, Control Material, Test Cartridge, Consumable |
| IVD Category | ivd_category | enum | — | Diagnostic discipline or testing area | Clinical Chemistry, Immunoassay, Hematology, Coagulation, Molecular Diagnostics, Urinalysis, Microbiology, Point-of-Care |
| Sample Types | sample_types | text (list) | — | Compatible biological specimen types | Serum, Plasma, Whole Blood, Urine, Cerebrospinal Fluid, Capillary Blood |
| Reagent Format | reagent_format | enum | — | Physical format of the reagent | Liquid Ready-to-Use, Lyophilized, Cartridge, Cassette, Barcoded Pack |
| Regulatory Classification | regulatory_classification | enum | — | Regulatory risk class | FDA Class I, FDA Class II, FDA Class III, CE-IVD (EU IVDR Class A/B/C/D), RUO (Research Use Only) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Hazard Classification | hazard_classification | text | — | Biosafety or hazard designation | Biohazard, Non-Hazardous, Contains Sodium Azide |
| Analyte/Test Name | analytetest_name | text | — | Specific analyte or test measured by the reagent or cartridge | Glucose, Troponin I, HbA1c, TSH, HIV Ag/Ab Combo, Cholesterol, Calcium |
| Test Methodology | test_methodology | text | — | Analytical principle or detection method | Photometry, Electrochemiluminescence (ECL), Chemiluminescence, Enzyme Immunoassay, Turbidimetry, Ion-Selective Electrode, PCR |
| Analyzer Compatibility | analyzer_compatibility | text (list) | — | Instruments the reagent or consumable is validated for use with | cobas c 311, cobas c 503, Atellica CH, Alinity c, ARCHITECT i2000SR |
| Throughput | throughput | number | tests/hr | Maximum test processing rate for instruments | 120, 300, 440, 2000 |
| Tests per Kit | tests_per_kit | number | — | Number of tests or determinations per reagent kit or pack | 100, 200, 500, 800 |
| Sensitivity/LoD | sensitivitylod | text | — | Limit of detection or analytical sensitivity | 0.003 ng/mL, 1 mg/dL, 0.5 mIU/L |
| Measuring Range | measuring_range | text | — | Reportable analytical measurement range | 0.1-25.0 mIU/L, 3-800 mg/dL, 0.006-50 ng/mL |
| Reagent Positions | reagent_positions | number | — | Number of onboard reagent positions or slots (instruments) | 28, 42, 45, 70, 160 |
| Onboard Stability | onboard_stability | text | — | Duration reagent remains stable once loaded on analyzer | 14 days, 28 days, 63 days, 90 days |
| Storage Temperature | storage_temperature | text | — | Required storage temperature range | 2-8 C (Refrigerated), 15-30 C (Room Temperature), -20 C (Frozen) |
| Shelf Life | shelf_life | text | — | Total product shelf life from date of manufacture when stored properly | 12 months, 18 months, 24 months |
| FDA Clearance/Approval | fda_clearanceapproval | text | — | FDA 510(k) clearance or PMA approval number if applicable | K201234, P200045, De Novo DEN200001 |
| CE Mark | ce_mark | enum | — | Whether the product bears a CE-IVD mark under EU IVDR | Yes, No |
| Dimensions (L x W x H) | dimensions_l_x_w_x_h | text | mm | External dimensions of the instrument or packaging | 1310 x 620 x 550, 200 x 100 x 50 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 sources plus FDA 21 CFR 809 and EU IVDR classification standards | [Roche cobas c 311](https://diagnostics.roche.com/us/en/products/instruments/cobas-c-311-ins-2043.html), [Abbott Point-of-Care Catalog](https://www.globalpointofcare.abbott/us/en/products-solutions/product-catalog.html), [Siemens Healthineers Atellica](https://www.siemens-healthineers.com/laboratory-diagnostics/clinical-chemistry-and-immunoassay-systems/atellica-solution-analyzers), [FDA IVD Regulations 21 CFR 809](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-809) |
