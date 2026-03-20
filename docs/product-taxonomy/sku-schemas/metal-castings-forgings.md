# SKU Schema: Metal Castings & Forgings

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.castings_forgings`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | CF-A36-OD-5000, IC-316-FLANGE-6IN |
| Product Name | product_name | text | — | yes | Full product name including process, material, and key dimensions | A36 Open Die Forged Round Bar 5in OD x 120in, 316 Stainless Investment Cast Flange 6in 150# |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/a36-open-die-forged-round |
| Price | price | number | — | yes | Numeric unit price (per piece or per pound) excluding currency symbol | 450.00, 1250.00, 8.50 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Material Type | material_type | enum | — | — | Broad category of the base metal | Carbon Steel, Alloy Steel, Stainless Steel, Aluminum, Copper Alloy, Nickel Alloy, Titanium, Ductile Iron, Gray Iron |
| Material Grade | material_grade | text | — | — | Specific alloy grade or specification | ASTM A105, AISI 4140, AISI 4340, 316L, A356, C95400, Inconel 718, Grade 65-45-12 |
| Weight Range Class | weight_range_class | text | — | — | General weight category for capability matching | Under 10 lbs, 10-100 lbs, 100-1000 lbs, 1000-10000 lbs, Over 10000 lbs |
| Country of Origin | country_of_origin | text | — | — | Country where the part was produced | USA, India, Germany, Japan, China, Italy |
| Outside Diameter | outside_diameter | number | in | — | Outer diameter for round and ring shapes | 4, 12, 36, 72, 120 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Manufacturer | manufacturer | text | — | — | Name of the foundry or forge shop | Scot Forge, Bharat Forge, PCC Structurals, Hitachi Metals, Signicast |
| Manufacturing Process | manufacturing_process | enum | — | — | Primary production method | Open Die Forging, Closed Die Forging, Ring Rolling, Seamless Rolled Ring, Sand Casting, Investment Casting, Die Casting, Permanent Mold Casting, Centrifugal Casting |
| Part Shape | part_shape | text | — | — | General shape or form of the finished casting or forging | Round Bar, Disc, Ring, Block, Flange, Shaft, Hub, Cylinder, Custom |
| Width | width | number | in | — | Width for rectangular blocks and custom shapes | 6, 12, 24, 48 |
| Wall Thickness | wall_thickness | number | in | — | Wall thickness for hollow castings and rolled rings | 0.125, 0.250, 1.0, 3.0, 6.0 |
| Heat Treatment | heat_treatment | text | — | — | Post-process thermal treatment applied | Normalized, Quenched and Tempered, Annealed, Solution Treated, Aged, Stress Relieved, None |
| Surface Condition | surface_condition | text | — | — | Surface finish state after processing | As-Forged, As-Cast, Rough Machined, Finish Machined, Shot Blasted, Ground |
| Dimensional Tolerance | dimensional_tolerance | text | — | — | Achievable dimensional tolerance class | ASTM A788 Standard, ISO 8062 CT4-CT8, NADCA Standard, Near Net Shape |
| Surface Roughness | surface_roughness | number | Ra um | — | Surface roughness in micrometres Ra | 0.8, 1.6, 3.2, 6.3, 12.5, 25.0 |
| Tensile Strength | tensile_strength | number | ksi | — | Minimum ultimate tensile strength of the finished part | 60, 75, 95, 120, 150 |
| Yield Strength | yield_strength | number | ksi | — | Minimum yield strength of the finished part | 36, 45, 65, 100, 130 |
| Elongation | elongation | number | % | — | Minimum elongation at break | 4, 10, 15, 20, 25 |
| Hardness | hardness | text | — | — | Hardness measurement of the finished part | HRB 70, HRC 22-28, BHN 170-220 |
| Impact Test | impact_test | text | — | — | Charpy V-notch impact test results or requirements if applicable | 15 ft-lbs at -20F, 25 ft-lbs at -50F, N/A |
| NDE/Testing | ndetesting | text (list) | — | — | Non-destructive examination methods performed | UT (Ultrasonic), MT (Magnetic Particle), RT (Radiographic), PT (Dye Penetrant), VT (Visual), None |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM forging/casting standards (A788, A781, A105) and NADCA die casting product specification standards | [Scot Forge](https://www.scotforge.com/), [Integrated Solutions](https://www.integratedsolutionsco.com/products-services/castings-forging/), [EB Castworld](https://ebcastworld.com/), [Bunty LLC](https://buntyllc.com/castings/) |
