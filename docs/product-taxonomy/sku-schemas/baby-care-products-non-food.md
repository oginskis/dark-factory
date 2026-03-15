# SKU Schema: Baby Care Products (Non-Food)

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.baby_care`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | H01WPS000, SP_229437, 2498023 |
| Product Name | text | Full product name including brand, product type, variant, and size | Graco 4Ever DLX 4-in-1 Car Seat, The Honest Company Clean Conscious Wipes, Dr. Browns Natural Flow Bottle 8oz |
| URL | text | Direct link to the product page | https://example.com/product/baby-wipes-sensitive |
| Price | number | Numeric price per unit or pack, excluding currency symbol | 6.99, 24.99, 249.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Primary product type within baby care | Wipes, Bottles, Pacifiers, Strollers, Car Seats, Baby Monitors, Bath Products, Skin Care, Nursing Accessories |
| Material | text (list) | Primary materials or fabric composition | BPA-Free Plastic, Silicone, Stainless Steel, Cotton, Bamboo |
| Active Ingredients | text (list) | Key active or functional ingredients | Zinc Oxide, Aloe, Chamomile Extract, Shea Butter |
| Country of Origin | text | Country where the product is manufactured | USA, China, Italy, Mexico |
| Size/Volume | text | Product size, volume, or capacity depending on category | 4 oz, 8 oz, 10 fl oz, 64 count, 22 lbs folded |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Product Line | text | Sub-brand or product series within the brand | Clean Conscious, Natural Flow, SnugRide, KeyFit, VISTA |
| Target Age Range | text | Recommended age or developmental stage | Newborn, 0-6 months, 6-12 months, Toddler 1-3 years |
| Pack Quantity | number | Number of individual items per pack | 1, 3, 72, 288 |
| Scent/Fragrance | text | Scent variant or fragrance-free designation | Fragrance-Free, Lavender, Sweet Orange Vanilla, Sensitive |
| Hypoallergenic | boolean | Whether the product is hypoallergenic | true, false |
| Dermatologist Tested | boolean | Whether the product has been dermatologist or pediatrician tested | true, false |
| Free-From Claims | text (list) | Ingredients or substances the product is free from | Parabens, Phthalates, Fragrance, Alcohol, Sulfates, Dyes |
| Folded Dimensions | text (in) | Folded or collapsed dimensions for strollers, playards | 18 x 24 x 34, 11 x 11 x 30 |
| Safety Certifications | text (list) | Applicable safety standards met | ASTM F833, JPMA Certified, CPSC Compliant, ASTM F2085, EN 1888 |
| EWG Verified | boolean | Whether the product carries the Environmental Working Group Verified mark | true, false |
| BPA Free | boolean | Whether the product is free of Bisphenol-A | true, false |
| Recommended Use | text (list) | Intended use or application | Bath Time, Diaper Change, Feeding, Travel, Skin Protection |
| Color/Pattern | text | Available color or print pattern | White, Cloud Island Blue, Pandas, Classic Stripes |
| UPC | text | Universal Product Code barcode number | 047406165735, 810022912345 |
| Expiration Date Applicable | boolean | Whether the product has a shelf life or expiration date | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus safety standards (ASTM F833, CPSC 16 CFR 1227) | [The Honest Company](https://www.honest.com/baby-products/view-all-baby), [Graco Baby](https://www.gracobaby.com/shop/car-seats/), [Chicco](https://motherhoodcommunity.com/chicco-vs-graco/), [Target Baby Shop](https://www.target.com/c/baby/-/N-5xtly) |
