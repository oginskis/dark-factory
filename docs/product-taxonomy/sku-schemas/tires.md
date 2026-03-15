# SKU Schema: Tires

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.tires`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 407285374, 5492, T431320 |
| Product Name | text | Full product name including brand, model, and size designation | Goodyear Assurance All-Season 225/65R17, Michelin Defender 2 235/55R18, Continental PremiumContact 7 205/55R16 |
| URL | text | Direct link to the product page | https://example.com/tires/goodyear-assurance-225-65r17 |
| Price | number | Numeric price per tire excluding currency symbol | 111.00, 189.99, 246.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Tire Type | enum | Vehicle application category | Passenger (P), Light Truck (LT), Special Trailer (ST), Temporary Spare (T) |
| Sidewall Type | enum | Visual style of the sidewall | BSW (Black Sidewall), WSW (White Sidewall), OWL (Outlined White Letters), RWL (Raised White Letters), BSL (Black Serrated Letters) |
| Rim Diameter | number (in) | Diameter of the wheel rim the tire fits, in inches | 14, 15, 16, 17, 18, 19, 20, 22 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Model/Product Line | text | Tire model or product line name | Assurance All-Season, Defender 2, PremiumContact 7, Pilot Sport 5, CrossClimate 2 |
| Season | enum | Seasonal classification of the tire | Summer, Winter, All-Season, All-Weather |
| Section Width | number (mm) | Nominal cross-section width of the tire in millimetres | 185, 205, 225, 245, 275, 315 |
| Aspect Ratio | number | Sidewall height as a percentage of section width | 30, 40, 45, 50, 55, 60, 65, 70 |
| Construction | enum | Internal construction method of the tire | R (Radial), D (Diagonal/Bias), B (Belted-Bias) |
| Load Index | number | Standardised code indicating maximum load capacity per tire | 91, 97, 102, 105, 117 |
| Speed Rating | text | Letter code indicating maximum rated speed capability | S (180 km/h), H (210 km/h), V (240 km/h), W (270 km/h), Y (300 km/h) |
| Load Range | text | Ply-equivalent strength rating used primarily on light truck and trailer tires | SL, XL, C, D, E |
| UTQG Treadwear | number | Uniform Tire Quality Grading treadwear rating; higher values indicate longer tread life | 100, 300, 500, 700, 900 |
| UTQG Traction | enum | UTQG traction grade indicating wet stopping distance performance | AA, A, B, C |
| UTQG Temperature | enum | UTQG temperature resistance grade | A, B, C |
| Tread Depth | number (mm) | Depth of the tread grooves when new, measured from tread surface to groove bottom | 7.5, 8.5, 9.5, 10.5, 12.0 |
| Approved Rim Width Range | text (in) | Minimum and maximum rim widths the tire can be safely mounted on | 6.0-7.5, 6.5-8.0, 7.0-9.0 |
| Max Inflation Pressure | number (kPa) | Maximum cold inflation pressure moulded on the sidewall | 240, 300, 340, 350, 550 |
| Revolutions per Kilometre | number | Number of full revolutions the tire makes per kilometre of travel | 468, 498, 530, 575 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ETRTO, UTQG, EU Tire Regulation 2020/740) | [Bridgestone](https://tires.bridgestone.com/en-us/learn/shopping-for-tires/tire-specs), [Goodyear](https://www.goodyear.com/en-US/tires/assurance-all-season/sizes-specs), [Continental](https://www.continental-tires.com/products/b2c/tire-knowledge/eu-tire-label/), [Michelin](https://www.michelinman.com/auto/auto-tips-and-advice/tires-101/tire-markings-explained) |
