# SKU Schema: Building Sets & Construction Toys

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.building_sets_construction_toys`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 75367, 10318, GJD23, HLC87 |
| Product Name | product_name | text | — | yes | Full product name including theme and set description | LEGO Star Wars Venator-Class Republic Attack Cruiser, MEGA Pokemon Squirtle Building Toy Kit |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/lego-75367 |
| Price | price | number | — | yes | Numeric retail price excluding currency symbol | 19.99, 49.99, 149.99, 649.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, DKK, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Brick Material | brick_material | text | — | — | Primary material used for the building elements | ABS Plastic, Bio-PE, Wood, Magnetic Plastic, Nylon |
| Category | category | enum | — | — | Brickset/industry classification of the set type | Normal, Gear, Extended, Collection, Book |
| Country of Origin | country_of_origin | text | — | — | Country where the set is manufactured | Denmark, Czech Republic, Hungary, China, Mexico |
| Piece Count | piece_count | number | — | — | Total number of individual pieces or elements in the set | 24, 379, 682, 5374 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Set Number | set_number | text | — | — | Manufacturer-assigned set identification number. Primary identifier for LEGO and similar brands | 75367, 10318, 21348, 42151 |
| Theme | theme | text | — | — | Product line or franchise theme the set belongs to | Star Wars, City, Technic, Creator Expert, Icons, Friends, Ninjago, Pokemon |
| Subtheme | subtheme | text | — | — | More specific grouping within the main theme | Ultimate Collector Series, Speed Champions, Architecture Skyline |
| Age Recommendation | age_recommendation | text | — | — | Recommended age range printed on the box | 4+, 6+, 9+, 14+, 18+ |
| Difficulty Level | difficulty_level | enum | — | — | Relative building complexity for the target audience | Beginner, Intermediate, Advanced, Expert |
| Assembled Dimensions (L x W x H) | assembled_dimensions_l_x_w_x_h | text | cm | — | Dimensions of the completed model | 13 x 24 x 6, 53 x 43 x 30, 110 x 66 x 40 |
| Package Dimensions (L x W x H) | package_dimensions_l_x_w_x_h | text | cm | — | Outer box dimensions | 26 x 19 x 6, 48 x 37 x 9, 58 x 47 x 18 |
| Brick Compatibility | brick_compatibility | text | — | — | Compatibility with other building systems | LEGO Compatible, MEGA Compatible, Proprietary |
| Motorized/Electronic | motorizedelectronic | boolean | — | — | Whether the set includes motors, lights, or electronic components | Yes, No |
| App-Enabled | app-enabled | boolean | — | — | Whether the set integrates with a companion mobile app for instructions or control | Yes, No |
| Number of Instruction Booklets | number_of_instruction_booklets | number | — | — | Count of printed instruction manuals included | 1, 2, 4, 6 |
| Building Techniques | building_techniques | text (list) | — | — | Special construction methods featured in the set | Technic Gears, Ball Joints, SNOT (Studs Not On Top), Modular, Brick-Built |
| Play Features | play_features | text (list) | — | — | Interactive or functional features of the completed model | Opening Doors, Rotating Turret, Working Crane, Light Brick, Spring-Loaded Shooter |
| Display Stand Included | display_stand_included | boolean | — | — | Whether a display stand or nameplate is included | Yes, No |
| Series/Collection | seriescollection | text | — | — | Named product collection or series | Botanical Collection, Ideas, Modular Buildings, Marvel Super Heroes |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 sources plus EN 71 and ASTM F963 toy safety standards | [LEGO Shop](https://www.lego.com/), [Brickset](https://brickset.com/), [MEGA/Amazon](https://www.amazon.com/Mega-Construx/s?k=Mega+Construx), [BrickLink](https://www.bricklink.com/) |
