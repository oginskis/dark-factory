# SKU Schema: Building Sets & Construction Toys

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 75367, 10318, GJD23, HLC87 |
| Product Name | text | Full product name including theme and set description | LEGO Star Wars Venator-Class Republic Attack Cruiser, MEGA Pokemon Squirtle Building Toy Kit |
| URL | text | Direct link to the product page | https://example.com/product/lego-75367 |
| Price | number | Numeric retail price excluding currency symbol | 19.99, 49.99, 149.99, 649.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, DKK, JPY |
| Brand/Manufacturer | text | Company that produces the building set | LEGO, MEGA, Playmobil, K-NEX, Cobi, Magformers, Plus-Plus |
| Set Number | text | Manufacturer-assigned set identification number. Primary identifier for LEGO and similar brands | 75367, 10318, 21348, 42151 |
| Piece Count | number | Total number of individual pieces or elements in the set | 24, 379, 682, 5374 |
| Minifigure/Figure Count | number | Number of character figures included in the set | 0, 1, 3, 5, 8 |
| Theme | text | Product line or franchise theme the set belongs to | Star Wars, City, Technic, Creator Expert, Icons, Friends, Ninjago, Pokemon |
| Subtheme | text | More specific grouping within the main theme | Ultimate Collector Series, Speed Champions, Architecture Skyline |
| Age Recommendation | text | Recommended age range printed on the box | 4+, 6+, 9+, 14+, 18+ |
| Difficulty Level | enum | Relative building complexity for the target audience | Beginner, Intermediate, Advanced, Expert |
| Assembled Dimensions (L x W x H) | text (cm) | Dimensions of the completed model | 13 x 24 x 6, 53 x 43 x 30, 110 x 66 x 40 |
| Package Dimensions (L x W x H) | text (cm) | Outer box dimensions | 26 x 19 x 6, 48 x 37 x 9, 58 x 47 x 18 |
| Product Weight | number (kg) | Total weight of the set including packaging | 0.25, 0.85, 2.50, 7.80 |
| Brick Material | text | Primary material used for the building elements | ABS Plastic, Bio-PE, Wood, Magnetic Plastic, Nylon |
| Brick Compatibility | text | Compatibility with other building systems | LEGO Compatible, MEGA Compatible, Proprietary |
| Motorized/Electronic | boolean | Whether the set includes motors, lights, or electronic components | Yes, No |
| App-Enabled | boolean | Whether the set integrates with a companion mobile app for instructions or control | Yes, No |
| Number of Instruction Booklets | number | Count of printed instruction manuals included | 1, 2, 4, 6 |
| Building Techniques | text (list) | Special construction methods featured in the set | Technic Gears, Ball Joints, SNOT (Studs Not On Top), Modular, Brick-Built |
| Play Features | text (list) | Interactive or functional features of the completed model | Opening Doors, Rotating Turret, Working Crane, Light Brick, Spring-Loaded Shooter |
| Display Stand Included | boolean | Whether a display stand or nameplate is included | Yes, No |
| Category | enum | Brickset/industry classification of the set type | Normal, Gear, Extended, Collection, Book |
| Series/Collection | text | Named product collection or series | Botanical Collection, Ideas, Modular Buildings, Marvel Super Heroes |
| Retired/Active | enum | Whether the set is currently in production or discontinued | Active, Retired |
| Price Per Piece | number | Calculated ratio of price to piece count | 0.05, 0.08, 0.10, 0.12 |
| Safety Certification | text (list) | Applicable toy safety standards and markings | ASTM F963, EN 71, CE, CPSIA |
| Country of Origin | text | Country where the set is manufactured | Denmark, Czech Republic, Hungary, China, Mexico |
| UPC/EAN | text | Universal Product Code or European Article Number | 5702017462479, 0673419388979 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 sources plus EN 71 and ASTM F963 toy safety standards | [LEGO Shop](https://www.lego.com/), [Brickset](https://brickset.com/), [MEGA/Amazon](https://www.amazon.com/Mega-Construx/s?k=Mega+Construx), [BrickLink](https://www.bricklink.com/) |
