# SKU Schema: Insulation Materials

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.insulation`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | OCNGX-1-Single, RC-R23-1, JM-R30-UF |
| Product Name | product_name | text | — | yes | Full product name including key specs such as material, R-value, and dimensions | Owens Corning FOAMULAR NGX 250 4ft x 8ft x 1in, Rockwool Comfortbatt R-23 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/foamular-ngx-250 |
| Price | price | number | — | yes | Numeric price per unit (bag, board, roll, or bundle), excluding currency symbol | 52.55, 86.70, 48.27 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Material Type | material_type | enum | — | — | Primary insulation material composition | Fiberglass, Mineral Wool, XPS, EPS, Polyisocyanurate, Spray Foam, Cellulose |
| Product Form | product_form | enum | — | — | Physical form of the insulation product | Batt, Roll, Rigid Board, Loose Fill, Spray, Blown-In |
| Facing Type | facing_type | enum | — | — | Type of facing or vapour barrier applied to the insulation | Unfaced, Kraft Faced, Foil Faced, FSK, Poly-Wrapped |
| Fire Classification | fire_classification | text | — | — | Fire performance class per applicable standard | Class A, Class B, Euroclass A1, Euroclass A2-s1 d0 |
| Sound Transmission Class | sound_transmission_class | number | — | — | STC rating for sound blocking through partitions | 35, 43, 45, 52 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | USA, Canada, Denmark, Germany, Poland |
| R-Value | r-value | number | — | — | Total thermal resistance of the product as sold | 11, 13, 15, 19, 23, 30, 38, 49, 60 |
| R-Value per Inch | r-value_per_inch | number | — | — | Thermal resistance per inch of thickness | 2.2, 3.0, 3.7, 4.2, 5.0, 6.5 |
| Thermal Conductivity | thermal_conductivity | number | W/mK | — | Thermal conductivity (lambda value) at mean temperature | 0.032, 0.035, 0.040, 0.044 |
| Thickness | thickness | number | mm | — | Product thickness | 25, 50, 75, 89, 100, 140, 150, 184 |
| Width | width | number | mm | — | Product width | 380, 400, 580, 600, 1200, 1220 |
| Coverage Area | coverage_area | number | m2 | — | Area covered per package or unit | 2.23, 5.58, 8.36, 11.15 |
| Density | density | number | kg/m3 | — | Nominal density of the insulation material | 12, 24, 32, 48, 96, 128 |
| Compressive Strength | compressive_strength | number | kPa | — | Compressive strength at 10 percent deformation | 100, 172, 276, 414 |
| Flame Spread Index | flame_spread_index | number | — | — | Surface burning flame spread rating per ASTM E84 / UL 723 | 0, 5, 15, 25 |
| Smoke Developed Index | smoke_developed_index | number | — | — | Smoke developed rating per ASTM E84 / UL 723 | 0, 5, 25, 50, 450 |
| Noise Reduction Coefficient | noise_reduction_coefficient | number | — | — | NRC rating for sound absorption (0 to 1) | 0.75, 0.85, 0.95, 1.05 |
| Water Absorption | water_absorption | text | — | — | Moisture uptake characteristic or percentage | Less than 0.3%, Negligible, Less than 1% by volume |
| Application | application | text (list) | — | — | Primary intended uses for the product | Wall Cavity, Ceiling, Attic, Floor, Basement, Exterior Sheathing, Pipe Wrap, Duct Wrap |
| Applicable Standard | applicable_standard | text (list) | — | — | Industry or test standards the product meets | ASTM C665, ASTM C726, ASTM C1289, EN 13162, EN 13164, EN 13165 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ASTM C665, ASTM E84, EN 13162) | [Insulation4US](https://insulation4us.com/collections/mineral-wool), [Owens Corning](https://www.owenscorning.com/en-us/insulation/residential), [Johns Manville](https://www.jm.com/en/building-insulation/residential/fiberglass/), [Rockwool](https://www.buildsite.com/pdf/rockwool/ROCKWOOL-AFB-evo-Insulation-Batts-Guide-Specifications-2112204.pdf) |
