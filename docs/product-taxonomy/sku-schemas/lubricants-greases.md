# SKU Schema: Lubricants & Greases

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.lubricants_greases`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | 122115, LE-1275, SHELL-GR-EP2 |
| Product Name | product_name | text | — | Full product name including brand, product line, grade, and formulation | Mobilgrease XHP 462 Moly, Shell Gadus S2 V220AC 2, Lubrication Engineers Almagard Vari-Purpose Lubricant |
| URL | url | text | — | Direct link to the product data sheet or listing page | https://example.com/product/mobilgrease-xhp-462 |
| Price | price | number | — | Numeric price per container, excluding currency symbol | 12.99, 89.50, 425.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary lubricant form | Grease, Engine Oil, Gear Oil, Hydraulic Fluid, Compressor Oil, Cutting Fluid, Chain Lubricant, Way Oil |
| NLGI Grade | nlgi_grade | text | — | National Lubricating Grease Institute consistency grade from 000 (fluid) to 6 (block) | 000, 00, 0, 1, 1.5, 2, 3 |
| ISO Viscosity Grade | iso_viscosity_grade | text | — | ISO VG classification of the base oil | ISO VG 68, ISO VG 100, ISO VG 150, ISO VG 220, ISO VG 460 |
| Thickener Type | thickener_type | text | — | Chemical thickener used in grease formulation | Lithium Complex, Calcium Sulfonate Complex, Aluminum Complex, Polyurea, Clay (Bentone), Fumed Silica |
| Base Oil Type | base_oil_type | enum | — | Base stock classification | Mineral, Synthetic (PAO), Synthetic (Ester), Semi-Synthetic, Bio-Based |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Food Grade | food_grade | boolean | — | Whether the product is NSF H1 registered for incidental food contact | true, false |
| Hazmat Class | hazmat_class | text | — | DOT or UN hazardous materials classification | Not Regulated, UN1993 Class 3 |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, UK, Germany, France, Singapore |
| Product Line | product_line | text | — | Sub-brand or product series name | Mobilgrease XHP, Gadus, Almagard, Alvania, Delvac, Rimula |
| Base Oil Viscosity at 40C | base_oil_viscosity_at_40c | number | mm2/s | Kinematic viscosity of the base oil at 40 degrees C | 100, 150, 220, 460, 1500 |
| Base Oil Viscosity at 100C | base_oil_viscosity_at_100c | number | mm2/s | Kinematic viscosity of the base oil at 100 degrees C | 11.4, 14.5, 19.1, 30.8 |
| Viscosity Index | viscosity_index | number | — | Measure of viscosity change with temperature (higher = more stable) | 85, 96, 120, 160 |
| Dropping Point | dropping_point | number | deg C | Temperature at which grease begins to flow from a cup per ASTM D2265 | 180, 260, 300, None (clay-based) |
| Operating Temperature Range | operating_temperature_range | text | deg C | Recommended continuous operating temperature range | -30 to 120, -40 to 150, -20 to 180, -25 to 200 |
| Four-Ball Weld Point | four-ball_weld_point | number | kgf | Extreme pressure performance per ASTM D2596 | 250, 315, 400, 620 |
| Four-Ball Wear Scar | four-ball_wear_scar | number | mm | Wear protection performance per ASTM D2266 | 0.4, 0.5, 0.65 |
| Timken OK Load | timken_ok_load | number | lb | Load-carrying capacity per ASTM D2509 | 40, 50, 60, 75 |
| Water Resistance | water_resistance | enum | — | Ability to resist water washout per ASTM D1264 or spray-off | Excellent, Good, Fair |
| Copper Corrosion | copper_corrosion | text | — | Copper strip corrosion rating per ASTM D4048 | 1A, 1B, 2A |
| Oxidation Stability | oxidation_stability | number | kPa | Pressure drop in oxygen bomb test per ASTM D942 | 13.8, 28, 35 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus NLGI, ASTM, and DIN lubricant standards | [ExxonMobil Mobilgrease XHP 462](https://www.mobil.com/en/lubricants/for-businesses/industrial/lubricants/products/products/mobilgrease-xhp-462-moly), [Shell Product Catalogue](https://www.epc.shell.com/), [Lubrication Engineers](https://lelubricants.com/lubricants/industrial-greases/), [SKF Grease Technical Data](https://www.skf.com/us/products/lubrication-management/lubricants/Understanding-technical-data-of-greases) |
