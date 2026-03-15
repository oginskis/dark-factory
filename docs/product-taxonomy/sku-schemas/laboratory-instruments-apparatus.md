# SKU Schema: Laboratory Instruments & Apparatus

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.laboratory_instruments`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor catalog/part number | 75009513, G1312C, 5065-4401, 022620601 |
| Product Name | product_name | text | Full product name including brand, model, and key specification | Thermo Scientific SL4 Plus Centrifuge 120V, Agilent 1260 Infinity II Quaternary Pump, Eppendorf Centrifuge 5430 R |
| URL | url | text | Direct link to the product page | https://example.com/product/sl4-plus-centrifuge |
| Price | price | number | List or catalog price per unit | 850, 4500, 12000, 45000, 125000 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Instrument Category | instrument_category | enum | Primary laboratory instrument classification | Centrifuge, Analytical Balance, Spectrophotometer, HPLC System, pH Meter, Pipette, Incubator, Autoclave, Microscope, PCR Thermal Cycler, Fume Hood, Water Purification System, Hotplate/Stirrer, Freeze Dryer |
| Display Type | display_type | text | User interface display | 7-inch Color Touchscreen, 5.7-inch LCD, LED Push-Button Panel, PC Software Control Only |
| Motor Type | motor_type | text | Drive motor technology | Direct Brushless Induction, Stepper Motor, Servo Motor |
| Construction Material | construction_material | text | Primary housing or chamber material | Stainless Steel Bowl, Powder-Coated Steel, Chemical-Resistant Polypropylene |
| Capacity | capacity | text | Sample or vessel capacity in relevant units | 40 x 50 mL tubes, 196 x 5/7 mL blood tubes, 6 microplates, 4 x 1000 mL bottles, 220 g |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Model | model | text | Specific model or series designation | SL4 Plus, 1260 Infinity II, 5430 R, XPR226DR/AC, UV-1900i |
| Application Area | application_area | text (list) | Intended scientific disciplines or workflows | Clinical Chemistry, Molecular Biology, Pharmaceutical QC, Environmental Testing, Food Safety, Materials Science, Proteomics |
| Measurement Principle | measurement_principle | text | Core analytical or physical operating principle | Centrifugal Force, Electromagnetic Force Compensation, UV-Vis Absorption, Reversed-Phase Chromatography, Electrochemical (Glass Electrode), Fluorescence |
| Max Speed | max_speed | number (RPM) | Maximum rotational speed for centrifuges, mixers, or stirrers | 4500, 14000, 15000, 25000, 30000 |
| Max RCF | max_rcf | number (x g) | Maximum relative centrifugal force | 3220, 5590, 17000, 25830, 30130 |
| Readability/Resolution | readabilityresolution | text | Smallest displayed increment for balances, meters, or detectors | 0.001 mg, 0.01 mg, 0.1 pH, 0.001 AU, 1 nm |
| Measurement Range | measurement_range | text | Operating measurement span | 0-14 pH, 190-1100 nm, 0-3 AU, 0-220 g, 0-100 C |
| Accuracy/Linearity | accuracylinearity | text | Stated accuracy or linearity specification | ±0.002 pH, ±0.1 mg, ±0.5 nm, ±1% RCF |
| Temperature Range | temperature_range | text (C) | Operating or controlled temperature range | -10 to 40 C, 4 to 60 C, -20 to 100 C, ambient to 300 C |
| Temperature Control | temperature_control | enum | Whether the instrument includes active temperature regulation | Refrigerated, Heated, Both, Ventilated (non-refrigerated), None |
| Number of Rotor/Accessory Options | number_of_rotoraccessory_options | number | Available interchangeable rotors, columns, or modules | 4, 8, 13, 17, 24 |
| Flow Rate Range | flow_rate_range | text | Liquid flow rate range for pumps and chromatography systems | 0.001-10 mL/min, 0.2-5 L/min |
| Pressure Range | pressure_range | text | Maximum operating pressure for HPLC or compressed-gas instruments | 600 bar, 1000 bar, 1300 bar |
| Run Time | run_time | text | Maximum continuous operation duration | 9 hours 59 minutes, 99 hours 59 minutes, Continuous |
| Noise Level | noise_level | number (dBA) | Acoustic noise emission at rated speed | 50, 56, 64, 68, 72 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus IEC 61010 and 21 CFR Part 11 standards | [Thermo Fisher SL4 Plus Centrifuge](https://www.thermofisher.com/order/catalog/product/75009513), [Agilent InfinityLab LC Series](https://www.agilent.com/en/product/liquid-chromatography/hplc-systems), [METTLER TOLEDO Lab Instruments](https://www.mt.com/us/en/home/products/lab-solutions/lab-instruments.html), [Labcompare Buyer Guide](https://www.labcompare.com/) |
