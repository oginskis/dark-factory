# SKU Schema: Abrasives

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.abrasives`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | SAIT-20063, 3M-90036, NOR66252940148 |
| Product Name | product_name | text | — | yes | Full product name including type, size, grit, and grain | SAIT TrimBack Flap Disc 4.5in 60 Grit Zirconia, 3M Cubitron II Depressed Center Grinding Wheel 4.5x0.25 36+ |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/flap-disc-4-5-60-zirconia |
| Price | price | number | — | yes | Numeric price per unit or per pack excluding currency symbol | 4.99, 12.50, 89.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary abrasive product category | Grinding Wheel, Cut-Off Wheel, Flap Disc, Fiber Disc, Sanding Belt, Sanding Disc, Sanding Sheet, Wire Brush, Mounted Point, Diamond Blade |
| Abrasive Grain Type | abrasive_grain_type | enum | — | — | Type of abrasive mineral used | Aluminum Oxide, Zirconia Alumina, Ceramic Alumina, Silicon Carbide, Diamond, CBN, Precision Shaped Ceramic |
| Grit Classification | grit_classification | enum | — | — | Coarseness category | Extra Coarse, Coarse, Medium, Fine, Very Fine, Ultra Fine |
| Wheel Type/Shape | wheel_typeshape | text | — | — | ANSI/ISO shape designation | Type 1, Type 27, Type 28, Type 29, Type 41, Type 42 |
| Bond Type | bond_type | enum | — | — | Bonding material holding the abrasive grains | Resinoid, Vitrified, Rubber, Metal, Electroplated |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Backing Material | backing_material | text | — | — | Substrate material for coated abrasives | Fiber, Paper, Cloth, Polyester Film, Fiberglass, Plastic, Vulcanized |
| Coating Type | coating_type | enum | — | — | How abrasive grain is distributed on the backing | Open Coat, Closed Coat, Semi-Open |
| Application Material | application_material | text (list) | — | — | Materials the abrasive is designed to work on | Steel, Stainless Steel, Aluminum, Cast Iron, Concrete, Wood, Non-Ferrous Metals |
| Application Type | application_type | text (list) | — | — | Intended operations | Grinding, Cutting, Blending, Deburring, Surface Conditioning, Polishing, Weld Removal |
| Wheel Hardness Grade | wheel_hardness_grade | text | — | — | Hardness of the bond in bonded abrasives (A=soft to Z=hard) | F, H, J, M, P, R, T |
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | USA, Germany, Italy, China, Brazil |
| Thickness | thickness | number | in | — | Thickness of the wheel or disc | 0.045, 0.090, 0.25, 0.50, 1.0 |
| Maximum RPM | maximum_rpm | number | rpm | — | Maximum safe operating speed in revolutions per minute | 4140, 8600, 13300, 15200 |
| Attachment Method | attachment_method | enum | — | — | How the product mounts to the tool | Arbor Hole, Quick-Change (SAIT-LOK), Hook and Loop, PSA, Snap-On, Threaded Hub |
| Density | density | enum | — | — | Grain density for flap discs and non-woven products | Regular, High Density |
| Structure Number | structure_number | text | — | — | Grain spacing in bonded abrasives (1=dense to 15=open) | 5, 7, 8, 10, 12 |
| Pack Quantity | pack_quantity | number | — | — | Number of pieces per retail package or box | 1, 5, 10, 25, 50 |
| Safety Standard | safety_standard | text (list) | — | — | Safety certifications and compliance standards | ANSI B7.1, EN 12413, oSa, OSHA |
| Shelf Life | shelf_life | text | — | — | Maximum recommended storage period | 3 years from manufacture date |
| Grit Size | grit_size | text | — | — | Coarseness rating of the abrasive grain | 24, 36, 60, 80, 120, 220, 400 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 28 attributes from 4 companies plus industry standards (ANSI B7.1, EN 12413, FEPA grit standards) | [United Abrasives/SAIT](https://www.unitedabrasives.com/), [3M Abrasives](https://www.3m.com/3M/en_US/metalworking-us/products/grinding-wheels/), [Benchmark Abrasives](https://benchmarkabrasives.com/), [Norton Abrasives](https://www.nortonabrasives.com/en-us/grinding-wheel-basics) |
