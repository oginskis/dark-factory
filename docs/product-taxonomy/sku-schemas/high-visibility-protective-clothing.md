# SKU Schema: High-Visibility & Protective Clothing

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.high_visibility_protective_clothing`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | US466-HVY-BLK-L, 25023, ERG-8384 |
| Product Name | product_name | text | — | Full product name including key specs such as garment type, class, and color | Portwest US466 ANSI Class 3 Hi-Vis Contrast Traffic Jacket Yellow/Black, Ergodyne GloWear 8310HL Class 3 Economy Vest Lime |
| URL | url | text | — | Direct link to the product page | https://example.com/product/portwest-us466-hivis-jacket |
| Price | price | number | — | Numeric unit price excluding currency symbol | 9.99, 34.95, 89.50 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Garment Type | garment_type | enum | — | Primary type of hi-vis garment | Vest, Jacket, Coat, Shirt, T-Shirt, Sweatshirt, Hoodie, Pants, Coverall, Bib Overalls, Rain Jacket, Bomber Jacket |
| ANSI/ISEA Type | ansiisea_type | enum | — | Garment type classification per ANSI/ISEA 107-2020 | Type O (Off-Road), Type R (Roadway), Type P (Public Safety) |
| ANSI/ISEA Class | ansiisea_class | enum | — | Minimum visibility performance class per ANSI/ISEA 107-2020 | Class 1, Class 2, Class 3 |
| EN ISO 20471 Class | en_iso_20471_class | enum | — | European high-visibility classification | Class 1, Class 2, Class 3 |
| Background Material Color | background_material_color | enum | — | Fluorescent base fabric color | Fluorescent Yellow-Green, Fluorescent Orange-Red, Fluorescent Red |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Shell Material | shell_material | text | — | Primary fabric of the garment outer shell | 100% Polyester, Polyester/Cotton Blend, 300D Oxford Polyester, Nylon, Modacrylic |
| Material Weight | material_weight | text | — | Fabric weight or density | 150 gsm, 5.5 oz, 300D |
| Lining Material | lining_material | text | — | Inner lining or insulation material if applicable | Polyester Fleece, Quilted Polyester, Mesh, None |
| Closure Type | closure_type | text | — | Primary garment closure mechanism | Full Zipper, Hook and Loop, Snaps, Elastic, Open Front |
| Country of Origin | country_of_origin | text | — | Country where the garment is manufactured | Bangladesh, China, Vietnam, India, USA |
| Model Number | model_number | text | — | Manufacturer model or part number | US466, 8310HL, 25023, V1025 |
| Reflective Tape Color | reflective_tape_color | text | — | Color of the retroreflective striping | Silver, Prismatic Silver, Segmented Silver, Yellow |
| Reflective Tape Width | reflective_tape_width | text | — | Width of the retroreflective bands | 2 inch, 50 mm, 1 inch |
| Reflective Tape Configuration | reflective_tape_configuration | text | — | Placement pattern of reflective bands on the garment | 360-Degree, Two Horizontal/Two Vertical, X-Back, Two Horizontal |
| Waterproof/Water Resistant | waterproofwater_resistant | text | — | Water protection level of the garment | Waterproof (Sealed Seams), Water Resistant, PU Coated, None |
| Breathability | breathability | text | — | Moisture vapor transmission or mesh ventilation features | Mesh Back Panel, Moisture Wicking, Ventilated, Sealed |
| Pockets | pockets | text | — | Number and type of pockets | 2 Front, 1 Chest, 1 Inside, 2 Cargo, 4 Total |
| Flame Resistance | flame_resistance | text | — | Fire-resistant treatment or inherent flame resistance | FR Treated, NFPA 2112, NFPA 70E CAT 2, HRC 2, None |
| Arc Rating | arc_rating | text | — | Arc thermal performance value for electrical hazard protection | 8.8 cal/sq cm, 12 cal/sq cm, None |
| Fit | fit | enum | — | Garment fit style | Regular, Tall, Extended, Unisex |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI/ISEA 107-2020, EN ISO 20471, CSA Z96) | [HiVis Supply](https://www.hivissupply.com/hivis-safety-clothing.html), [Portwest](https://www.portwest.com/), [Ergodyne](https://www.ergodyne.com/blog/understanding-hi-vis-standards-ansi-isea-107), [PIP Global](https://us.pipglobal.com/en/products/hi-vis-apparel-experts/) |
