# SKU Schema: Laboratory Instruments & Apparatus

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor catalog/part number | 75009513, G1312C, 5065-4401, 022620601 |
| Product Name | text | Full product name including brand, model, and key specification | Thermo Scientific SL4 Plus Centrifuge 120V, Agilent 1260 Infinity II Quaternary Pump, Eppendorf Centrifuge 5430 R |
| URL | text | Direct link to the product page | https://example.com/product/sl4-plus-centrifuge |
| Price | number | List or catalog price per unit | 850, 4500, 12000, 45000, 125000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Instrument manufacturer or brand | Thermo Fisher Scientific, Agilent Technologies, Eppendorf, METTLER TOLEDO, Shimadzu, PerkinElmer, Sartorius, Hettich, Waters, Beckman Coulter |
| Instrument Category | enum | Primary laboratory instrument classification | Centrifuge, Analytical Balance, Spectrophotometer, HPLC System, pH Meter, Pipette, Incubator, Autoclave, Microscope, PCR Thermal Cycler, Fume Hood, Water Purification System, Hotplate/Stirrer, Freeze Dryer |
| Model | text | Specific model or series designation | SL4 Plus, 1260 Infinity II, 5430 R, XPR226DR/AC, UV-1900i |
| Application Area | text (list) | Intended scientific disciplines or workflows | Clinical Chemistry, Molecular Biology, Pharmaceutical QC, Environmental Testing, Food Safety, Materials Science, Proteomics |
| Measurement Principle | text | Core analytical or physical operating principle | Centrifugal Force, Electromagnetic Force Compensation, UV-Vis Absorption, Reversed-Phase Chromatography, Electrochemical (Glass Electrode), Fluorescence |
| Capacity | text | Sample or vessel capacity in relevant units | 40 x 50 mL tubes, 196 x 5/7 mL blood tubes, 6 microplates, 4 x 1000 mL bottles, 220 g |
| Max Speed | number (RPM) | Maximum rotational speed for centrifuges, mixers, or stirrers | 4500, 14000, 15000, 25000, 30000 |
| Max RCF | number (x g) | Maximum relative centrifugal force | 3220, 5590, 17000, 25830, 30130 |
| Readability/Resolution | text | Smallest displayed increment for balances, meters, or detectors | 0.001 mg, 0.01 mg, 0.1 pH, 0.001 AU, 1 nm |
| Measurement Range | text | Operating measurement span | 0-14 pH, 190-1100 nm, 0-3 AU, 0-220 g, 0-100 C |
| Accuracy/Linearity | text | Stated accuracy or linearity specification | ±0.002 pH, ±0.1 mg, ±0.5 nm, ±1% RCF |
| Temperature Range | text (C) | Operating or controlled temperature range | -10 to 40 C, 4 to 60 C, -20 to 100 C, ambient to 300 C |
| Temperature Control | enum | Whether the instrument includes active temperature regulation | Refrigerated, Heated, Both, Ventilated (non-refrigerated), None |
| Number of Rotor/Accessory Options | number | Available interchangeable rotors, columns, or modules | 4, 8, 13, 17, 24 |
| Flow Rate Range | text | Liquid flow rate range for pumps and chromatography systems | 0.001-10 mL/min, 0.2-5 L/min |
| Pressure Range | text | Maximum operating pressure for HPLC or compressed-gas instruments | 600 bar, 1000 bar, 1300 bar |
| Run Time | text | Maximum continuous operation duration | 9 hours 59 minutes, 99 hours 59 minutes, Continuous |
| Noise Level | number (dBA) | Acoustic noise emission at rated speed | 50, 56, 64, 68, 72 |
| Display Type | text | User interface display | 7-inch Color Touchscreen, 5.7-inch LCD, LED Push-Button Panel, PC Software Control Only |
| Connectivity | text (list) | Data interfaces and communication ports | USB, RS-232, Ethernet (LAN), Bluetooth, CAN Bus, GPIB, Wi-Fi |
| Software Compatibility | text (list) | Compatible data acquisition or control software | Chromeleon, OpenLab CDS, LabSolutions, STARe Excellence, UNICORN |
| GLP/GMP Features | text (list) | Regulatory compliance features built into the instrument | Audit Trail, User Access Control, Electronic Signatures (21 CFR Part 11), Automatic Calibration Logging |
| Dimensions (W x D x H) | text (mm) | External footprint and height of the instrument | 690 x 566 x 362, 345 x 460 x 140, 600 x 500 x 400 |
| Weight | number (kg) | Net weight of the instrument without accessories | 5.5, 12, 45, 89, 135 |
| Power Requirements | text | Electrical supply specification | 100-240 V AC, 50/60 Hz, 1300 W |
| Ingress Protection | text | IP rating for environmental resistance | IP21, IP30, IP54 |
| Safety Certifications | text (list) | Electrical safety and quality certifications | IEC 61010-1, UL 61010-1, CSA C22.2, CE, ISO 13485, ISO 9001 |
| Motor Type | text | Drive motor technology | Direct Brushless Induction, Stepper Motor, Servo Motor |
| Construction Material | text | Primary housing or chamber material | Stainless Steel Bowl, Powder-Coated Steel, Chemical-Resistant Polypropylene |
| Warranty | text | Standard manufacturer warranty period and coverage | 2 years parts and labor, 5 years limited, 1 year |
| Country of Manufacture | text | Country where the instrument is produced | Germany, USA, Japan, Switzerland, United Kingdom |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus IEC 61010 and 21 CFR Part 11 standards | [Thermo Fisher SL4 Plus Centrifuge](https://www.thermofisher.com/order/catalog/product/75009513), [Agilent InfinityLab LC Series](https://www.agilent.com/en/product/liquid-chromatography/hplc-systems), [METTLER TOLEDO Lab Instruments](https://www.mt.com/us/en/home/products/lab-solutions/lab-instruments.html), [Labcompare Buyer Guide](https://www.labcompare.com/) |
