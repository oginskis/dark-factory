# SKU Schema: Precious Metals (Gold, Silver, Platinum)

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.precious_metals`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or dealer product identifier | AGE-1OZ-2025, SML-1OZ-BU, PAMP-1OZ-BAR |
| Product Name | product_name | text | — | yes | Full product name including metal, weight, mint, and year | 2025 1 oz American Gold Eagle BU, 1 oz PAMP Suisse Platinum Bar .9995 Fine |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/2025-1oz-american-gold-eagle |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol. Precious metals prices fluctuate with spot price | 2045.00, 31.50, 1025.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Metal Type | metal_type | enum | — | — | Primary precious metal content | Gold, Silver, Platinum, Palladium |
| Product Type | product_type | enum | — | — | Physical form of the precious metal product | Coin, Bar, Round, Ingot, Wafer |
| Country of Origin | country_of_origin | text | — | — | Country where the product was minted or refined | USA, Canada, Australia, Switzerland, Austria, South Africa, China |
| Weight (Troy oz) | weight_troy_oz | number | oz | — | Metal weight in troy ounces | 0.05, 0.10, 0.25, 0.50, 1.00, 5.00, 10.00, 100.00 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Dealer/Seller | dealerseller | text | — | — | Name of the bullion dealer or retailer | APMEX, JM Bullion, SD Bullion, BOLD Precious Metals, Kitco |
| Mint/Manufacturer | mintmanufacturer | text | — | — | Sovereign mint or private refinery that produced the item | US Mint, Royal Canadian Mint, Perth Mint, PAMP Suisse, Valcambi, Scottsdale Mint, Sunshine Minting |
| Series/Program | seriesprogram | text | — | — | Named coin program or product series | American Eagle, Canadian Maple Leaf, Austrian Philharmonic, Chinese Panda, Britannia, Krugerrand, American Buffalo |
| Year | year | text | — | — | Year of issue or production. May be N/A for generic bars and rounds | 2025, 2024, 2023, Random Year |
| Purity/Fineness | purityfineness | number | — | — | Metal purity expressed as decimal fineness | 0.999, 0.9999, 0.9167, 0.900, 0.9995 |
| Fineness Notation | fineness_notation | text | — | — | Purity expressed in millesimal notation | 999, 9999, 916.7, 900, 999.5 |
| Actual Metal Content (Troy oz) | actual_metal_content_troy_oz | number | oz | — | Fine metal content calculated as gross weight multiplied by fineness | 0.9675, 1.0000, 0.7234 |
| Face Value | face_value | number | — | — | Legal tender face value for sovereign-minted coins. 0 for bars and rounds | 50, 25, 10, 5, 1, 0 |
| Face Value Currency | face_value_currency | text | — | — | Currency of the face value denomination | USD, CAD, AUD, GBP, EUR, ZAR |
| Thickness | thickness | number | mm | — | Thickness of coins and rounds, or height of bars | 1.19, 1.78, 2.15, 2.87 |
| Condition | condition | text | — | — | Physical condition or grade of the item | Brilliant Uncirculated (BU), Proof, Certified MS-70, Certified MS-69, Good, Very Good, Varied |
| Grading Service | grading_service | text | — | — | Third-party coin grading service if applicable | NGC, PCGS, None |
| Mintage | mintage | number | — | — | Total number of pieces produced in a given year or run | 500000, 1000000, 5000, Unlimited |
| IRA Eligible | ira_eligible | boolean | — | — | Whether the product qualifies for inclusion in a Precious Metals IRA | Yes, No |
| Packaging | packaging | text | — | — | How the item is packaged or presented | Mint Tube, Monster Box, Assay Card, Capsule, Sealed Mint Roll, Loose |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 dealers plus LBMA Good Delivery specifications and coin grading standards (NGC/PCGS) | [SD Bullion](https://sdbullion.com/gold), [JM Bullion](https://www.jmbullion.com/), [APMEX](https://www.apmex.com/), [BOLD Precious Metals](https://www.boldpreciousmetals.com/) |
