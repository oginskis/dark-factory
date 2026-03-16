# SKU Schema: Diagnostic Imaging Equipment (MRI, CT, X-Ray)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.diagnostic_imaging`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer model number or catalog identifier | SIGNA Premier, SOMATOM Force, Alphenix 4D CT |
| Product Name | product_name | text | — | Full product name including modality and key differentiator | GE SIGNA Premier 3.0T Wide Bore MRI, Siemens SOMATOM go.Up 64-Slice CT, Canon Radrex i5 Digital Radiography System |
| URL | url | text | — | Direct link to the product page | https://example.com/products/signa-premier |
| Price | price | number | — | Numeric list or quoted price per system, excluding currency symbol | 1500000, 850000, 250000 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Detector Type | detector_type | text | — | Detector technology used for image acquisition | Flat-Panel (amorphous silicon), Stellar UFC, GOS scintillator, CZT, Digital SiPM |
| Software Platform | software_platform | text | — | Core operating and reconstruction software platform | SIGNA Works, syngo.via, IntelliSpace Portal, Vitrea |
| IEC Classification | iec_classification | text | — | IEC 60601 classification and applied collateral standards | Class I Type B, IEC 60601-2-33, IEC 60601-2-44, IEC 60601-2-54 |
| Bore Diameter | bore_diameter | number | cm | Patient bore or gantry aperture diameter | 60, 70, 78, 80 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Manufacturer | manufacturer | text | — | Equipment manufacturer name | GE HealthCare, Siemens Healthineers, Philips Healthcare, Canon Medical Systems, United Imaging |
| Modality | modality | enum | — | Primary imaging modality of the system | MRI, CT, X-Ray, PET-CT, SPECT-CT, Fluoroscopy, Mammography |
| Field Strength | field_strength | number | T | Magnetic field strength in Tesla (MRI only) | 1.5, 3.0, 0.55, 7.0 |
| Detector Rows | detector_rows | number | — | Number of detector element rows along the z-axis (CT only) | 16, 64, 128, 192, 320 |
| Rotation Time | rotation_time | number | s | Minimum gantry rotation time in seconds (CT only) | 0.25, 0.35, 0.5, 1.0 |
| Tube Power | tube_power | number | kW | Maximum X-ray tube output power | 60, 80, 100, 120 |
| Gradient Strength | gradient_strength | number | mT/m | Maximum gradient amplitude (MRI only) | 33, 45, 60, 80 |
| Slew Rate | slew_rate | number | T/m/s | Maximum gradient slew rate (MRI only) | 110, 150, 200 |
| Number of RF Channels | number_of_rf_channels | number | — | Number of independent radio-frequency receiver channels (MRI only) | 16, 32, 48, 64, 128 |
| Field of View | field_of_view | number | cm | Maximum scan field of view diameter | 45, 50, 55, 70 |
| Spatial Resolution | spatial_resolution | text | — | Limiting spatial resolution of the imaging chain | 3.4 lp/mm, 0.23 mm isotropic, 5 lp/mm |
| Scan Coverage | scan_coverage | number | cm | Maximum anatomical coverage per rotation or per scan (CT z-coverage) | 2.4, 4.0, 8.0, 16.0 |
| Helium Volume | helium_volume | number | L | Liquid helium capacity for superconducting magnets (MRI only) | 7, 28, 1500 |
| System Dimensions | system_dimensions | text | m | Overall installed footprint length x width x height | 1.74 x 2.30 x 1.96, 2.10 x 2.30 x 1.80 |
| Power Requirements | power_requirements | text | — | Electrical supply specifications | 480V 3-phase 100A, 380V 3-phase 60A |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 manufacturers plus IEC 60601 standards and industry comparison data | [GE HealthCare MRI](https://www.gehealthcare.com/products/magnetic-resonance-imaging), [Siemens Healthineers CT](https://www.siemens-healthineers.com/en-us/computed-tomography/somatom/somatom-force), [Canon Medical Systems](https://us.medical.canon/products/), [Philips Diagnostic Imaging](https://www.usa.philips.com/healthcare/diagnostic-imaging) |
