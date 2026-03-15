# SKU Schema: Diagnostic Imaging Equipment (MRI, CT, X-Ray)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer model number or catalog identifier | SIGNA Premier, SOMATOM Force, Alphenix 4D CT |
| Product Name | text | Full product name including modality and key differentiator | GE SIGNA Premier 3.0T Wide Bore MRI, Siemens SOMATOM go.Up 64-Slice CT, Canon Radrex i5 Digital Radiography System |
| URL | text | Direct link to the product page | https://example.com/products/signa-premier |
| Price | number | Numeric list or quoted price per system, excluding currency symbol | 1500000, 850000, 250000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Manufacturer | text | Equipment manufacturer name | GE HealthCare, Siemens Healthineers, Philips Healthcare, Canon Medical Systems, United Imaging |
| Modality | enum | Primary imaging modality of the system | MRI, CT, X-Ray, PET-CT, SPECT-CT, Fluoroscopy, Mammography |
| Field Strength | number (T) | Magnetic field strength in Tesla (MRI only) | 1.5, 3.0, 0.55, 7.0 |
| Bore Diameter | number (cm) | Patient bore or gantry aperture diameter | 60, 70, 78, 80 |
| Magnet Length | number (cm) | Total magnet length from front to rear of bore (MRI only) | 145, 160, 173 |
| Detector Rows | number | Number of detector element rows along the z-axis (CT only) | 16, 64, 128, 192, 320 |
| Slice Count | number | Maximum number of simultaneously acquired slices per rotation (CT only) | 16, 64, 128, 256, 640 |
| Rotation Time | number (s) | Minimum gantry rotation time in seconds (CT only) | 0.25, 0.35, 0.5, 1.0 |
| Tube Voltage Range | text (kV) | Available X-ray tube voltage settings | 70-150, 80-140, 40-150 |
| Tube Power | number (kW) | Maximum X-ray tube output power | 60, 80, 100, 120 |
| Gradient Strength | number (mT/m) | Maximum gradient amplitude (MRI only) | 33, 45, 60, 80 |
| Slew Rate | number (T/m/s) | Maximum gradient slew rate (MRI only) | 110, 150, 200 |
| Number of RF Channels | number | Number of independent radio-frequency receiver channels (MRI only) | 16, 32, 48, 64, 128 |
| Field of View | number (cm) | Maximum scan field of view diameter | 45, 50, 55, 70 |
| Detector Type | text | Detector technology used for image acquisition | Flat-Panel (amorphous silicon), Stellar UFC, GOS scintillator, CZT, Digital SiPM |
| Detector Size | text | Active detector dimensions (X-Ray/DR only) | 43 x 43 cm, 35 x 43 cm, 25 x 30 cm |
| Spatial Resolution | text | Limiting spatial resolution of the imaging chain | 3.4 lp/mm, 0.23 mm isotropic, 5 lp/mm |
| Scan Coverage | number (cm) | Maximum anatomical coverage per rotation or per scan (CT z-coverage) | 2.4, 4.0, 8.0, 16.0 |
| Helium Volume | number (L) | Liquid helium capacity for superconducting magnets (MRI only) | 7, 28, 1500 |
| Patient Table Capacity | number (kg) | Maximum patient weight supported by the imaging table | 200, 227, 307 |
| System Weight | number (kg) | Total installed weight of the imaging system | 3400, 5600, 8200 |
| System Dimensions | text (m) | Overall installed footprint length x width x height | 1.74 x 2.30 x 1.96, 2.10 x 2.30 x 1.80 |
| Minimum Room Size | text (m) | Required examination room dimensions length x width x height | 5.0 x 4.0 x 2.8, 6.5 x 5.5 x 3.0 |
| Power Requirements | text | Electrical supply specifications | 480V 3-phase 100A, 380V 3-phase 60A |
| Cooling Requirements | text | Heat dissipation and cooling infrastructure needs | Water-cooled chiller 25 kW, Air-cooled, Cryogen-free |
| Software Platform | text | Core operating and reconstruction software platform | SIGNA Works, syngo.via, IntelliSpace Portal, Vitrea |
| AI Capabilities | text (list) | Integrated AI-assisted features for acquisition or reconstruction | AIR Recon DL, ACS Deep Learning Reconstruction, iterative metal artifact reduction |
| Regulatory Clearance | text (list) | Medical device regulatory clearances held | FDA 510(k), CE Mark (MDR), PMDA, TGA, Health Canada |
| IEC Classification | text | IEC 60601 classification and applied collateral standards | Class I Type B, IEC 60601-2-33, IEC 60601-2-44, IEC 60601-2-54 |
| Warranty | text | Standard manufacturer warranty period | 1 year parts and labor, 5 year magnet warranty |
| Country of Manufacture | text | Country where the system is assembled | USA, Germany, Japan, China, Netherlands |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 manufacturers plus IEC 60601 standards and industry comparison data | [GE HealthCare MRI](https://www.gehealthcare.com/products/magnetic-resonance-imaging), [Siemens Healthineers CT](https://www.siemens-healthineers.com/en-us/computed-tomography/somatom/somatom-force), [Canon Medical Systems](https://us.medical.canon/products/), [Philips Diagnostic Imaging](https://www.usa.philips.com/healthcare/diagnostic-imaging) |
