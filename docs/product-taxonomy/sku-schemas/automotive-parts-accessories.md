# SKU Schema: Automotive Parts & Accessories

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.parts_accessories`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor stock keeping unit | MGD1273MH, 17-792, BP929C, NAP-625142 |
| Product Name | text | Full product name including brand, part type, and key specification | Raybestos R-Line Metallic Disc Brake Pad Set, Bosch 9619 Premium Oil Filter, Moog K80066 Front Sway Bar End Link |
| URL | text | Direct link to the product page | https://example.com/parts/brake-pads/mgd1273mh |
| Price | number | Numeric unit price excluding currency symbol | 12.99, 34.50, 189.00, 450.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Part Type | text | Standardized category of the part within the ACES/PIES classification | Disc Brake Pad Set, Oil Filter, Control Arm, Oxygen Sensor, Alternator, Spark Plug |
| Part Category | text | Higher-level grouping of the part | Brake and Wheel Hub, Engine, Cooling System, Electrical, Fuel and Air, Drivetrain, Suspension, Exhaust and Emission |
| Material | text | Primary material composition of the part | Ceramic, Semi-Metallic, Metallic, Steel, Aluminum, Rubber, Copper, Silicone |
| Country of Origin | text | Country where the part was manufactured | USA, Germany, Japan, China, Mexico, South Korea, India |
| Hazardous Material | boolean | Whether the part is classified as hazardous for shipping | Yes, No |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Manufacturer Part Number | text | Manufacturer-assigned unique part identifier | MGD1273MH, 9619, K80066, 917-143, 234-4018 |
| OEM Part Number | text | Original equipment manufacturer reference number | 68028493AA, 15400-PLM-A02, 4F0-501-529-J |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 049707320144, 4006633395397 |
| Vehicle Fitment | text (list) | Compatible vehicle year, make, model, and submodel combinations | 2011-2017 Jeep Wrangler, 2012-2019 Dodge Grand Caravan, 2008-2015 Honda Accord 2.4L |
| Position | text | Installation location on the vehicle | Front, Rear, Left, Right, Upper, Lower, Inner, Outer |
| Finish | text | Surface treatment or coating | Zinc Plated, Chrome, Black Oxide, Powder Coated, E-Coated, Anodized, Raw |
| Width | number (in) | Part width dimension | 1.2, 5.8, 10.0 |
| Height | number (in) | Part height or thickness dimension | 0.24, 3.5, 6.0 |
| Quantity per Pack | number | Number of pieces included in the package | 1, 2, 4, 6 |
| Hardware Included | boolean | Whether mounting hardware is included | Yes, No |
| Interchange Part Numbers | text (list) | Cross-reference numbers from other brands that are equivalent | AC Delco 17D1273M, Wagner ZD1273, Centric 104.12730 |
| Part Condition | enum | Whether the part is new, remanufactured, or used | New, Remanufactured, Used, NOS (New Old Stock) |
| OE Replacement | boolean | Whether the part meets or exceeds original equipment specifications | Yes, No |
| Warranty | text | Manufacturer warranty coverage period or terms | Limited Lifetime, 2-Year/24000-Mile, 3-Year, 90-Day |
| Certification | text (list) | Industry or regulatory certifications | ISO 9001, IATF 16949, ECE R90, FMVSS 135, SAE, D-mark |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry data standards (ACES, PIES, SAE, FMVSS) | [RockAuto](https://www.rockauto.com/en/partsearch/), [NAPA Online](https://www.napaonline.com/en/auto-parts), [PartCatalog](https://www.partcatalog.com/), [APA Engineering ACES/PIES Guide](https://apaengineering.com/technology-article/aces-and-pies-for-beginners/) |
