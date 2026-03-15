# SKU Schema: 3D Printing Filaments & Resins

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.printing_3d_filaments_resins`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | BL-ABS-BK, HB-PLA-1KG-BLK, FF-RPLA-175 |
| Product Name | text | Full product name including material, diameter, and color | Bambu Lab ABS Filament 1.75 mm Black 1 kg, Formlabs Tough 2000 Resin 1 L |
| URL | text | Direct link to the product page | https://example.com/product/abs-filament-black-1kg |
| Price | number | Numeric price per spool or per bottle, excluding currency symbol | 19.99, 24.99, 149.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Form | enum | Whether the product is filament or resin | Filament, Resin |
| Material Type | text | Base polymer or resin chemistry | PLA, ABS, PETG, ASA, TPU, Nylon, PC, PEEK, PEI, Standard Resin, ABS-Like Resin, Tough Resin, Flexible Resin |
| Compatible Printer Type | text (list) | Types of 3D printers compatible with this material | FDM, SLA, DLP, LCD/MSLA |
| Spool Type | enum | Whether the spool is standard, refill, or cardboard | Standard Plastic Spool, Refill, Cardboard Spool, Masterless |
| Country of Origin | text | Manufacturing country | USA, China, Czech Republic, Netherlands, Germany |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Spool/Bottle Volume | text | Container size or volume for resins | 250 g, 500 g, 1 kg, 1 L, 5 L |
| Color | text | Material color | Black, White, Red, Blue, Silver, Orange, Transparent, Gray |
| Print Temperature | text (C) | Recommended nozzle or hotend temperature range | 190-220, 230-260, 240-270, 280-310 |
| Bed Temperature | text (C) | Recommended heated bed temperature range | 25-60, 60-80, 80-110, 90-120 |
| Layer Exposure Time | number (s) | Per-layer UV exposure time for resin (resin only) | 1.5, 2.0, 3.0, 6.0, 8.0 |
| Viscosity | number (mPa s) | Liquid resin viscosity at 25 C (resin only) | 100, 150, 250, 450 |
| Density | number (g/cm3) | Material density in cured or solid state | 1.04, 1.10, 1.14, 1.24, 1.27 |
| Tensile Strength | number (MPa) | Maximum tensile stress before failure of printed part | 37, 46, 50, 60, 65 |
| Elongation at Break | number (%) | Percentage stretch before failure of printed part | 2, 6, 10, 25, 50, 100 |
| Flexural Modulus | number (MPa) | Stiffness of printed part under bending | 1200, 1800, 2200, 2800, 3500 |
| Shore Hardness | text | Surface hardness of cured or printed part | 50A, 80A, 75D, 83D, 86D |
| Heat Deflection Temperature | number (C) | Temperature at which printed part deforms under load | 52, 60, 73, 87, 140, 289 |
| Impact Strength | number (kJ/m2) | IZOD or Charpy impact resistance of printed part | 2.5, 5.0, 12.0, 25.0 |
| Shrinkage | number (%) | Dimensional shrinkage after printing or curing | 0.3, 0.5, 0.8, 1.5 |
| Drying Temperature | number (C) | Recommended drying temperature before printing (filament only) | 45, 55, 65, 80 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus material science properties (ISO 527, ASTM D638) | [Bambu Lab](https://us.store.bambulab.com/products/abs-filament), [Hatchbox](https://www.hatchbox3d.com/), [FormFutura](https://www.formfutura.com/), [Formlabs](https://formlabs.com/materials/) |
