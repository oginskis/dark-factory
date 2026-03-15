# SKU Schema: Asphalt & Bituminous Products

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.asphalt_bituminous`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | MPC-PG6422, TB-60/70, AI-CRS2 |
| Product Name | text | Full product name including manufacturer, product type, and grade | Marathon PG 64-22 Paving Grade Asphalt, Tiger Bitumen Penetration Grade 60/70, CRS-2 Cationic Rapid-Setting Emulsion |
| URL | text | Direct link to the product data sheet or listing page | https://example.com/product/pg-64-22-asphalt |
| Price | number | Numeric price per ton or gallon, excluding currency symbol | 450.00, 625.00, 3.25 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary bituminous product classification | Paving Grade Asphalt, Asphalt Emulsion, Cutback Asphalt, Oxidized (Blown) Bitumen, Roofing Flux, Polymer Modified Binder, Crumb Rubber Modified Binder |
| Performance Grade | text | Superpave PG designation — high and low temperature capability in degrees C | PG 46-28, PG 58-28, PG 64-22, PG 67-22, PG 76-22 |
| Penetration Grade | text | Penetration value range at 25 degrees C in tenths of mm per ASTM D5 | 20/30, 40/50, 60/70, 80/100, 100/150, 160/220 |
| Viscosity Grade | text | Absolute viscosity grading per ASTM D3381 | AC-5, AC-10, AC-20, AC-30, AC-40 |
| Cutback Solvent Type | text | Diluent used in cutback asphalts | Naphtha (Rapid Cure), Kerosene (Medium Cure), Fuel Oil (Slow Cure) |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Cutback Grade | text | Viscosity-based grade designation for cutback asphalts | RC-70, RC-250, MC-30, MC-250, MC-800, SC-250, SC-800 |
| Hazmat Class | text | DOT or UN hazardous materials classification | UN1999 Class 3, UN3257 Class 9, Not Regulated (emulsions) |
| Country of Origin | text | Country where the product was refined or produced | USA, Canada, Mexico, Iran, Singapore |
| Manufacturer | text | Refiner or producer name | Marathon Petroleum, Ergon Asphalt, Calumet, Nynas, Shell Bitumen, Tiger Bitumen |
| Grading System | enum | Classification system used | Performance Grade (PG), Penetration Grade, Viscosity Grade (AC), Emulsion Grade |
| Softening Point | number (deg C) | Ring-and-Ball softening point per ASTM D36 | 45, 48, 52, 60, 95 |
| Penetration at 25C | number (dmm) | Needle penetration depth in decimillimetres at 25 degrees C per ASTM D5 | 25, 50, 65, 85, 150 |
| Absolute Viscosity at 60C | number (Pa.s) | Viscosity at 60 degrees C per ASTM D2171 | 100, 200, 400, 800 |
| Kinematic Viscosity at 135C | number (mm2/s) | Viscosity at 135 degrees C per ASTM D2170 | 200, 300, 450 |
| Ductility at 25C | number (cm) | Elongation before breaking at 25 degrees C per ASTM D113 | 50, 100, 150 |
| Flash Point | number (deg C) | Minimum temperature at which vapors will ignite per ASTM D92 | 230, 260, 300, 340 |
| Solubility in Trichloroethylene | number (%) | Purity measure — percentage soluble per ASTM D2042 | 99.0, 99.5, 99.9 |
| Specific Gravity at 25C | number | Density relative to water at 25 degrees C | 1.00, 1.01, 1.03, 1.05 |
| Polymer Modifier | text | Type of polymer used in modified binders | SBS, SBR, EVA, Crumb Rubber, None |
| Emulsion Charge | enum | Electrical charge of emulsion droplets | Anionic, Cationic, Nonionic |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM D6373, AASHTO M 320, and Asphalt Institute specifications | [Marathon Petroleum Asphalt](https://www.mpcasphalt.com/Products/), [Petronaft Bitumen Grades](https://www.petronaftco.com/different-grades-of-bitumen/), [Asphalt Institute](https://www.asphaltinstitute.org/engineering/specification-databases/), [Pavement Interactive Superpave](https://pavementinteractive.org/reference-desk/materials/asphalt/superpave-performance-grading/) |
