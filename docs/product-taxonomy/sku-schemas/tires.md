# SKU Schema: Tires

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 407285374, 5492, T431320 |
| Product Name | text | Full product name including brand, model, and size designation | Goodyear Assurance All-Season 225/65R17, Michelin Defender 2 235/55R18, Continental PremiumContact 7 205/55R16 |
| URL | text | Direct link to the product page | https://example.com/tires/goodyear-assurance-225-65r17 |
| Price | number | Numeric price per tire excluding currency symbol | 111.00, 189.99, 246.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Tire manufacturer or brand name | Goodyear, Michelin, Continental, Bridgestone, Pirelli, Hankook, Yokohama |
| Model/Product Line | text | Tire model or product line name | Assurance All-Season, Defender 2, PremiumContact 7, Pilot Sport 5, CrossClimate 2 |
| Tire Type | enum | Vehicle application category | Passenger (P), Light Truck (LT), Special Trailer (ST), Temporary Spare (T) |
| Season | enum | Seasonal classification of the tire | Summer, Winter, All-Season, All-Weather |
| Section Width | number (mm) | Nominal cross-section width of the tire in millimetres | 185, 205, 225, 245, 275, 315 |
| Aspect Ratio | number | Sidewall height as a percentage of section width | 30, 40, 45, 50, 55, 60, 65, 70 |
| Construction | enum | Internal construction method of the tire | R (Radial), D (Diagonal/Bias), B (Belted-Bias) |
| Rim Diameter | number (in) | Diameter of the wheel rim the tire fits, in inches | 14, 15, 16, 17, 18, 19, 20, 22 |
| Load Index | number | Standardised code indicating maximum load capacity per tire | 91, 97, 102, 105, 117 |
| Speed Rating | text | Letter code indicating maximum rated speed capability | S (180 km/h), H (210 km/h), V (240 km/h), W (270 km/h), Y (300 km/h) |
| Load Range | text | Ply-equivalent strength rating used primarily on light truck and trailer tires | SL, XL, C, D, E |
| UTQG Treadwear | number | Uniform Tire Quality Grading treadwear rating; higher values indicate longer tread life | 100, 300, 500, 700, 900 |
| UTQG Traction | enum | UTQG traction grade indicating wet stopping distance performance | AA, A, B, C |
| UTQG Temperature | enum | UTQG temperature resistance grade | A, B, C |
| Overall Diameter | number (mm) | Total outer diameter of the inflated tire | 632, 680, 724, 756 |
| Tread Depth | number (mm) | Depth of the tread grooves when new, measured from tread surface to groove bottom | 7.5, 8.5, 9.5, 10.5, 12.0 |
| Tire Weight | number (kg) | Weight of a single unmounted tire | 8.2, 10.5, 12.8, 15.3 |
| Approved Rim Width Range | text (in) | Minimum and maximum rim widths the tire can be safely mounted on | 6.0-7.5, 6.5-8.0, 7.0-9.0 |
| Max Inflation Pressure | number (kPa) | Maximum cold inflation pressure moulded on the sidewall | 240, 300, 340, 350, 550 |
| Max Load Capacity | number (kg) | Maximum load the tire can carry at its rated inflation pressure | 580, 710, 850, 1030, 1360 |
| Revolutions per Kilometre | number | Number of full revolutions the tire makes per kilometre of travel | 468, 498, 530, 575 |
| Sidewall Type | enum | Visual style of the sidewall | BSW (Black Sidewall), WSW (White Sidewall), OWL (Outlined White Letters), RWL (Raised White Letters), BSL (Black Serrated Letters) |
| Run Flat | boolean | Whether the tire includes self-supporting run-flat technology | Yes, No |
| Snowflake Rated (3PMSF) | boolean | Whether the tire bears the Three-Peak Mountain Snowflake symbol for severe snow traction | Yes, No |
| M+S Rated | boolean | Whether the tire carries the Mud and Snow marking based on tread geometry | Yes, No |
| EU Label - Fuel Efficiency | enum | EU tire energy label rolling resistance class | A, B, C, D, E |
| EU Label - Wet Grip | enum | EU tire energy label wet braking performance class | A, B, C, D, E |
| EU Label - Noise Level | number (dB) | External rolling noise measured in decibels for the EU tire energy label | 67, 69, 71, 72 |
| OE Marking | text | Original equipment marking indicating vehicle-manufacturer approval | MO (Mercedes), N0 (Porsche), AO (Audi), star (BMW), HN (Hyundai/Kia) |
| DOT Code | text | US Department of Transportation Tire Identification Number including plant code, size code, and date of manufacture | DOT XXXX XXXX 2524 |
| Warranty Mileage | number (km) | Limited tread-life warranty distance provided by the manufacturer | 65000, 80000, 105000, 130000 |
| Country of Manufacture | text | Country where the tire was produced | USA, Germany, Japan, South Korea, Thailand, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ETRTO, UTQG, EU Tire Regulation 2020/740) | [Bridgestone](https://tires.bridgestone.com/en-us/learn/shopping-for-tires/tire-specs), [Goodyear](https://www.goodyear.com/en-US/tires/assurance-all-season/sizes-specs), [Continental](https://www.continental-tires.com/products/b2c/tire-knowledge/eu-tire-label/), [Michelin](https://www.michelinman.com/auto/auto-tips-and-advice/tires-101/tire-markings-explained) |
