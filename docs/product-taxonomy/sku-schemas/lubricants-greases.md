# SKU Schema: Lubricants & Greases

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | 122115, LE-1275, SHELL-GR-EP2 |
| Product Name | text | Full product name including brand, product line, grade, and formulation | Mobilgrease XHP 462 Moly, Shell Gadus S2 V220AC 2, Lubrication Engineers Almagard Vari-Purpose Lubricant |
| URL | text | Direct link to the product data sheet or listing page | https://example.com/product/mobilgrease-xhp-462 |
| Price | number | Numeric price per container, excluding currency symbol | 12.99, 89.50, 425.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or product brand name | Mobil, Shell, Lubrication Engineers, Castrol, Chevron, Total, Fuchs, SKF |
| Product Type | enum | Primary lubricant form | Grease, Engine Oil, Gear Oil, Hydraulic Fluid, Compressor Oil, Cutting Fluid, Chain Lubricant, Way Oil |
| Product Line | text | Sub-brand or product series name | Mobilgrease XHP, Gadus, Almagard, Alvania, Delvac, Rimula |
| NLGI Grade | text | National Lubricating Grease Institute consistency grade from 000 (fluid) to 6 (block) | 000, 00, 0, 1, 1.5, 2, 3 |
| Base Oil Viscosity at 40C | number (mm2/s) | Kinematic viscosity of the base oil at 40 degrees C | 100, 150, 220, 460, 1500 |
| Base Oil Viscosity at 100C | number (mm2/s) | Kinematic viscosity of the base oil at 100 degrees C | 11.4, 14.5, 19.1, 30.8 |
| ISO Viscosity Grade | text | ISO VG classification of the base oil | ISO VG 68, ISO VG 100, ISO VG 150, ISO VG 220, ISO VG 460 |
| Viscosity Index | number | Measure of viscosity change with temperature (higher = more stable) | 85, 96, 120, 160 |
| Thickener Type | text | Chemical thickener used in grease formulation | Lithium Complex, Calcium Sulfonate Complex, Aluminum Complex, Polyurea, Clay (Bentone), Fumed Silica |
| Base Oil Type | enum | Base stock classification | Mineral, Synthetic (PAO), Synthetic (Ester), Semi-Synthetic, Bio-Based |
| Dropping Point | number (deg C) | Temperature at which grease begins to flow from a cup per ASTM D2265 | 180, 260, 300, None (clay-based) |
| Operating Temperature Range | text (deg C) | Recommended continuous operating temperature range | -30 to 120, -40 to 150, -20 to 180, -25 to 200 |
| Four-Ball Weld Point | number (kgf) | Extreme pressure performance per ASTM D2596 | 250, 315, 400, 620 |
| Four-Ball Wear Scar | number (mm) | Wear protection performance per ASTM D2266 | 0.4, 0.5, 0.65 |
| Timken OK Load | number (lb) | Load-carrying capacity per ASTM D2509 | 40, 50, 60, 75 |
| Water Resistance | enum | Ability to resist water washout per ASTM D1264 or spray-off | Excellent, Good, Fair |
| Copper Corrosion | text | Copper strip corrosion rating per ASTM D4048 | 1A, 1B, 2A |
| Oxidation Stability | number (kPa) | Pressure drop in oxygen bomb test per ASTM D942 | 13.8, 28, 35 |
| Solid Additives | text (list) | Solid lubricant additives in the formulation | Molybdenum Disulfide (MoS2), Graphite, PTFE, None |
| Food Grade | boolean | Whether the product is NSF H1 registered for incidental food contact | true, false |
| Container Size | text | Package or container size | 14 oz cartridge, 35 lb pail, 120 lb drum, 400 lb drum |
| Applicable Standards | text (list) | Industry specifications the product meets or exceeds | DIN 51825, ISO 6743, ASTM D4950, MIL-PRF-23827 |
| Application | text (list) | Primary intended equipment or use | Bearings, Open Gears, Wire Rope, Centralized Systems, Electric Motors, Food Processing, Marine |
| Hazmat Class | text | DOT or UN hazardous materials classification | Not Regulated, UN1993 Class 3 |
| Country of Origin | text | Country where the product is manufactured | USA, UK, Germany, France, Singapore |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus NLGI, ASTM, and DIN lubricant standards | [ExxonMobil Mobilgrease XHP 462](https://www.mobil.com/en/lubricants/for-businesses/industrial/lubricants/products/products/mobilgrease-xhp-462-moly), [Shell Product Catalogue](https://www.epc.shell.com/), [Lubrication Engineers](https://lelubricants.com/lubricants/industrial-greases/), [SKF Grease Technical Data](https://www.skf.com/us/products/lubrication-management/lubricants/Understanding-technical-data-of-greases) |
