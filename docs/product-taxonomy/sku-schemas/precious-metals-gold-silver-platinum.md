# SKU Schema: Precious Metals (Gold, Silver, Platinum)

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.precious_metals`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or dealer product identifier | AGE-1OZ-2025, SML-1OZ-BU, PAMP-1OZ-BAR |
| Product Name | text | Full product name including metal, weight, mint, and year | 2025 1 oz American Gold Eagle BU, 1 oz PAMP Suisse Platinum Bar .9995 Fine |
| URL | text | Direct link to the product page | https://example.com/product/2025-1oz-american-gold-eagle |
| Price | number | Numeric unit price excluding currency symbol. Precious metals prices fluctuate with spot price | 2045.00, 31.50, 1025.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Metal Type | enum | Primary precious metal content | Gold, Silver, Platinum, Palladium |
| Product Type | enum | Physical form of the precious metal product | Coin, Bar, Round, Ingot, Wafer |
| Country of Origin | text | Country where the product was minted or refined | USA, Canada, Australia, Switzerland, Austria, South Africa, China |
| Weight (Troy oz) | number (oz) | Metal weight in troy ounces | 0.05, 0.10, 0.25, 0.50, 1.00, 5.00, 10.00, 100.00 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Dealer/Seller | text | Name of the bullion dealer or retailer | APMEX, JM Bullion, SD Bullion, BOLD Precious Metals, Kitco |
| Mint/Manufacturer | text | Sovereign mint or private refinery that produced the item | US Mint, Royal Canadian Mint, Perth Mint, PAMP Suisse, Valcambi, Scottsdale Mint, Sunshine Minting |
| Series/Program | text | Named coin program or product series | American Eagle, Canadian Maple Leaf, Austrian Philharmonic, Chinese Panda, Britannia, Krugerrand, American Buffalo |
| Year | text | Year of issue or production. May be N/A for generic bars and rounds | 2025, 2024, 2023, Random Year |
| Purity/Fineness | number | Metal purity expressed as decimal fineness | 0.999, 0.9999, 0.9167, 0.900, 0.9995 |
| Fineness Notation | text | Purity expressed in millesimal notation | 999, 9999, 916.7, 900, 999.5 |
| Actual Metal Content (Troy oz) | number (oz) | Fine metal content calculated as gross weight multiplied by fineness | 0.9675, 1.0000, 0.7234 |
| Face Value | number | Legal tender face value for sovereign-minted coins. 0 for bars and rounds | 50, 25, 10, 5, 1, 0 |
| Face Value Currency | text | Currency of the face value denomination | USD, CAD, AUD, GBP, EUR, ZAR |
| Thickness | number (mm) | Thickness of coins and rounds, or height of bars | 1.19, 1.78, 2.15, 2.87 |
| Condition | text | Physical condition or grade of the item | Brilliant Uncirculated (BU), Proof, Certified MS-70, Certified MS-69, Good, Very Good, Varied |
| Grading Service | text | Third-party coin grading service if applicable | NGC, PCGS, None |
| Mintage | number | Total number of pieces produced in a given year or run | 500000, 1000000, 5000, Unlimited |
| IRA Eligible | boolean | Whether the product qualifies for inclusion in a Precious Metals IRA | Yes, No |
| Packaging | text | How the item is packaged or presented | Mint Tube, Monster Box, Assay Card, Capsule, Sealed Mint Roll, Loose |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 dealers plus LBMA Good Delivery specifications and coin grading standards (NGC/PCGS) | [SD Bullion](https://sdbullion.com/gold), [JM Bullion](https://www.jmbullion.com/), [APMEX](https://www.apmex.com/), [BOLD Precious Metals](https://www.boldpreciousmetals.com/) |
