# SKU Schema: Fitness & Exercise Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.fitness_exercise`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | ROG-BAR2, LF-IC7, NT-X16, PEL-TR01 |
| Product Name | text | Full product name including brand, model, and key specs | Rogue Ohio Bar 2.0 Cerakote 20kg, NordicTrack X16 Incline Treadmill, Life Fitness IC7 Indoor Cycle |
| URL | text | Direct link to the product page | https://example.com/product/ohio-bar-cerakote |
| Price | number | Numeric retail price excluding currency symbol | 295.00, 1499.00, 3499.00, 6995.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Equipment Type | text | Specific equipment category | Treadmill, Elliptical, Stationary Bike, Barbell, Dumbbell, Kettlebell, Power Rack, Rowing Machine, Cable Machine, Bench |
| Material | text | Primary construction material | Steel, Aluminum, Cast Iron, Stainless Steel, Chrome, Rubber-Coated Steel |
| Resistance Type | text | Method used to generate resistance | Magnetic, Friction, Air, Water, Hydraulic, Weight Stack, Plate-Loaded |
| Display Type | text | Technology used for the console display | LCD, LED, HD Touchscreen, Full HD Touchscreen |
| Country of Origin | text | Country where the equipment was manufactured | USA, China, Taiwan, Germany, Italy |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Dimensions (Assembled) | text (mm) | Length x width x height when assembled and ready for use | 1965 x 897 x 1524, 2440 x 813 x 1524 |
| Dimensions (Folded) | text (mm) | Length x width x height in folded or stored position | 1016 x 897 x 1830 |
| Finish | text | Surface treatment or coating on the equipment | Cerakote, Black Zinc, E-Coat, Stainless Steel, Powder Coat, Chrome, Matte Black |
| Motor Power | text | Motor output rating for motorized equipment | 3.0 CHP, 4.25 CHP, 2.0 HP |
| Speed Range | text | Minimum to maximum speed for treadmills and bikes | 0-12.5 mph, 0-22 kph |
| Incline Range | text | Incline and decline range for treadmills and ellipticals | -3% to 15%, 0 to 40%, -6% to 40% |
| Resistance Levels | number | Number of discrete resistance settings on bikes and ellipticals | 16, 20, 24, 26, 100 |
| Preset Programs | number | Number of built-in workout programs | 0, 20, 40, 50 |
| Connectivity | text (list) | Wireless and wired connectivity options | Bluetooth, WiFi, ANT+, USB, Ethernet |
| Heart Rate Monitoring | text (list) | Methods of heart rate tracking supported | Contact Grip Sensors, Chest Strap Compatible, Bluetooth HR Strap, Wrist Sensor |
| Running Surface | text (mm) | Length x width of the tread belt for treadmills | 1524 x 508, 1702 x 559 |
| Tensile Strength | text (PSI) | Yield or tensile strength rating of a barbell shaft | 190000, 205000 |
| Foldable | boolean | Whether the equipment folds for storage | Yes, No |
| Power Source | text | Energy source required to operate the equipment | AC Mains (120V), AC Mains (240V), Self-Powered, Battery, None |
| Warranty Frame | text | Warranty duration for the structural frame | 2 Years, 5 Years, 10 Years, Lifetime |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ASTM F2276, EN 957, and ISO 20957 fitness equipment standards | [Rogue Fitness](https://www.roguefitness.com/), [NordicTrack](https://www.nordictrack.com/), [Life Fitness](https://www.lifefitness.com/), [Peloton](https://www.onepeloton.com/) |
