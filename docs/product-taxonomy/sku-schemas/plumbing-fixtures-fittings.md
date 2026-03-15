# SKU Schema: Plumbing Fixtures & Fittings

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | T6708BN, K-22036-CP, DLT-2559-SS |
| Product Name | text | Full product name including key specs such as fixture type, series, and finish | Moen Genta Two-Handle Widespread Bathroom Faucet Brushed Nickel, Kohler Highline Comfort Height Toilet |
| URL | text | Direct link to the product page | https://example.com/product/genta-widespread-faucet |
| Price | number | Numeric price per unit, excluding currency symbol | 89.99, 149.00, 329.50, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Moen, Delta, Kohler, American Standard, Grohe, Hansgrohe, TOTO, Pfister |
| Product Type | enum | General fixture or fitting category | Faucet, Toilet, Sink, Bathtub, Shower Head, Shower System, Valve, Pipe Fitting, Drain, Garbage Disposal |
| Sub-Type | text | Specific product variant within the type | Widespread, Centerset, Single-Hole, Wall-Mount, Pull-Down, Pull-Out, Touchless, Bridge, Pot Filler |
| Material | text | Primary body or housing material | Brass, Stainless Steel, Zinc Alloy, Copper, Cast Iron, Vitreous China, Acrylic, Fireclay |
| Finish | text | Surface finish or color of the fixture | Chrome, Brushed Nickel, Matte Black, Oil-Rubbed Bronze, Polished Brass, Stainless Steel, Spot Resist |
| Mounting Type | enum | How the fixture is installed | Deck Mount, Wall Mount, Floor Mount, Freestanding, Drop-In, Undermount, Vessel, Recessed |
| Number of Handles | enum | Handle configuration for faucets and valves | Single Handle, Two Handle, Touchless, Push-Button |
| Number of Faucet Holes | number | Mounting holes required for installation | 1, 2, 3, 4 |
| Flow Rate | number (GPM) | Water flow rate in gallons per minute | 0.5, 1.0, 1.2, 1.5, 1.8, 2.0, 2.5 |
| Flush Volume | number (GPF) | Gallons per flush for toilets and urinals | 0.5, 0.8, 1.0, 1.28, 1.6 |
| Valve Type | text | Internal valve or cartridge mechanism | Ceramic Disc, Ball, Compression, Cartridge, Pressure Balance, Thermostatic |
| Connection Size | text | Pipe or supply line connection diameter and thread type | 3/8 in Compression, 1/2 in IPS, 1/2 in Push Connect, 3/4 in FPT |
| Spout Height | number (mm) | Height of the spout from the mounting surface | 102, 152, 203, 254, 330 |
| Spout Reach | number (mm) | Horizontal projection of the spout from the center | 102, 127, 152, 203, 254 |
| Drain Type | text | Type of drain assembly included | Pop-Up, Push-Button, Grid, Click-Clack, None |
| Overall Height | number (mm) | Total height of the fixture | 120, 305, 380, 711, 762 |
| Overall Width | number (mm) | Total width or diameter of the fixture | 200, 356, 508, 610, 762 |
| Overall Depth | number (mm) | Front-to-back dimension of the fixture | 200, 381, 508, 610, 711 |
| Weight | number (kg) | Product weight for shipping and installation | 1.5, 3.2, 8.5, 22.0, 45.0 |
| WaterSense Certified | boolean | Whether the product meets EPA WaterSense criteria | true, false |
| ADA Compliant | boolean | Whether the product meets ADA accessibility requirements | true, false |
| Certification | text (list) | Product certifications and standards compliance | WaterSense, ADA, NSF/ANSI 61, NSF/ANSI 372, CSA, IAPMO/UPC, ASME A112.18.1 |
| Bowl Shape | text | Toilet bowl shape (toilets only) | Round, Elongated, Compact Elongated |
| Rough-In Distance | number (mm) | Distance from finished wall to center of drain (toilets) | 254, 305 |
| Application | text (list) | Intended installation locations | Kitchen, Bathroom, Laundry, Commercial, Outdoor, Bar, Utility |
| Country of Origin | text | Country where the product was manufactured | USA, Mexico, China, Germany, Japan, Thailand |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (NSF/ANSI 61, ASME A112.18.1) | [Moen](https://www.moen.com/), [Ferguson Plumbing](https://www.ferguson.com/category/kitchen-plumbing/kitchen-bar-faucets/), [Standard Plumbing Supply](https://www.standardplumbing.com/catalogs/plumbing-fittings/170000), [PlumbersStock](https://www.plumbersstock.com/moen-t6708bn-genta.html) |
