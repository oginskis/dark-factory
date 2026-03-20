# SKU Schema: Plumbing Fixtures & Fittings

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.plumbing_fixtures_fittings`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | T6708BN, K-22036-CP, DLT-2559-SS |
| Product Name | product_name | text | — | yes | Full product name including key specs such as fixture type, series, and finish | Moen Genta Two-Handle Widespread Bathroom Faucet Brushed Nickel, Kohler Highline Comfort Height Toilet |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/genta-widespread-faucet |
| Price | price | number | — | yes | Numeric price per unit, excluding currency symbol | 89.99, 149.00, 329.50, 1250.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | General fixture or fitting category | Faucet, Toilet, Sink, Bathtub, Shower Head, Shower System, Valve, Pipe Fitting, Drain, Garbage Disposal |
| Sub-Type | sub-type | text | — | — | Specific product variant within the type | Widespread, Centerset, Single-Hole, Wall-Mount, Pull-Down, Pull-Out, Touchless, Bridge, Pot Filler |
| Material | material | text | — | — | Primary body or housing material | Brass, Stainless Steel, Zinc Alloy, Copper, Cast Iron, Vitreous China, Acrylic, Fireclay |
| Mounting Type | mounting_type | enum | — | — | How the fixture is installed | Deck Mount, Wall Mount, Floor Mount, Freestanding, Drop-In, Undermount, Vessel, Recessed |
| Valve Type | valve_type | text | — | — | Internal valve or cartridge mechanism | Ceramic Disc, Ball, Compression, Cartridge, Pressure Balance, Thermostatic |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Drain Type | drain_type | text | — | — | Type of drain assembly included | Pop-Up, Push-Button, Grid, Click-Clack, None |
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | USA, Mexico, China, Germany, Japan, Thailand |
| Finish | finish | text | — | — | Surface finish or color of the fixture | Chrome, Brushed Nickel, Matte Black, Oil-Rubbed Bronze, Polished Brass, Stainless Steel, Spot Resist |
| Number of Handles | number_of_handles | enum | — | — | Handle configuration for faucets and valves | Single Handle, Two Handle, Touchless, Push-Button |
| Number of Faucet Holes | number_of_faucet_holes | number | — | — | Mounting holes required for installation | 1, 2, 3, 4 |
| Flow Rate | flow_rate | number | GPM | — | Water flow rate in gallons per minute | 0.5, 1.0, 1.2, 1.5, 1.8, 2.0, 2.5 |
| Flush Volume | flush_volume | number | GPF | — | Gallons per flush for toilets and urinals | 0.5, 0.8, 1.0, 1.28, 1.6 |
| Spout Height | spout_height | number | mm | — | Height of the spout from the mounting surface | 102, 152, 203, 254, 330 |
| Spout Reach | spout_reach | number | mm | — | Horizontal projection of the spout from the center | 102, 127, 152, 203, 254 |
| Overall Height | overall_height | number | mm | — | Total height of the fixture | 120, 305, 380, 711, 762 |
| Overall Width | overall_width | number | mm | — | Total width or diameter of the fixture | 200, 356, 508, 610, 762 |
| Overall Depth | overall_depth | number | mm | — | Front-to-back dimension of the fixture | 200, 381, 508, 610, 711 |
| WaterSense Certified | watersense_certified | boolean | — | — | Whether the product meets EPA WaterSense criteria | true, false |
| ADA Compliant | ada_compliant | boolean | — | — | Whether the product meets ADA accessibility requirements | true, false |
| Certification | certification | text (list) | — | — | Product certifications and standards compliance | WaterSense, ADA, NSF/ANSI 61, NSF/ANSI 372, CSA, IAPMO/UPC, ASME A112.18.1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (NSF/ANSI 61, ASME A112.18.1) | [Moen](https://www.moen.com/), [Ferguson Plumbing](https://www.ferguson.com/category/kitchen-plumbing/kitchen-bar-faucets/), [Standard Plumbing Supply](https://www.standardplumbing.com/catalogs/plumbing-fittings/170000), [PlumbersStock](https://www.plumbersstock.com/moen-t6708bn-genta.html) |
