# SKU Schema: Household Linens & Towels

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.household_linens_towels`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | HT-2750-WHT, 4532100, BLS-BT-27X54 |
| Product Name | product_name | text | Full product name including key specs such as product type, material, and dimensions | 100% Cotton Ring-Spun Bath Towel 27x54 White 14 lb/dz, T-300 Percale Queen Flat Sheet |
| URL | url | text | Direct link to the product page | https://example.com/product/bath-towel-27x54 |
| Price | price | number | Numeric price per selling unit (piece, dozen, case), excluding currency symbol | 3.49, 42.99, 189.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Type of household linen product | Bath Towel, Hand Towel, Washcloth, Bath Sheet, Bath Mat, Flat Sheet, Fitted Sheet, Pillowcase, Duvet Cover, Table Napkin, Tablecloth, Kitchen Towel, Beach Towel |
| Material Composition | material_composition | text | Fiber content with percentages | 100% Cotton, 86% Cotton / 14% Polyester, 100% Linen, 60% Cotton / 40% Polyester |
| Cotton Type | cotton_type | text | Specific cotton variety or yarn construction when applicable | Ring-Spun, Combed, Egyptian, Pima, Supima, Turkish, Open-End |
| Weave Type | weave_type | enum | Method used to interlace yarns that determines texture and performance | Terry, Percale, Sateen, Jacquard, Dobby, Waffle, Twill, Plain |
| Border Type | border_type | text | Decorative or structural border style on towels and linens | Dobby Border, Cam Border, Hemmed, Piano Key, Stripe, No Border |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Pile Type | pile_type | enum | Loop construction of terry fabric | Single Loop, Double Loop, Zero Twist, Low Twist |
| Hem Type | hem_type | text | Edge finishing method | Double-Stitched Hem, Single Fold, Mitered Corner, Overlock |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | India, Pakistan, Turkey, China, Portugal, USA |
| GSM | gsm | number (g/m2) | Fabric weight in grams per square metre, primary indicator of thickness and quality for towels | 400, 550, 700 |
| Width | width | number (cm) | Product width or shorter dimension | 33, 41, 69, 152 |
| Color | color | text | Product color or pattern name | White, Ivory, Navy, Sage Green, Charcoal Grey, Striped |
| Pocket Depth | pocket_depth | number (cm) | Depth of the fitted sheet pocket for mattress fit | 25, 30, 38, 46 |
| Shrinkage | shrinkage | text (%) | Expected dimensional change after laundering | Less than 3%, Less than 5% |
| Absorbency Rating | absorbency_rating | text | Qualitative absorbency classification for towels | Standard, High, Premium |
| Quick Dry | quick_dry | boolean | Whether the product is engineered for accelerated drying | true, false |
| Anti-Microbial Treatment | anti-microbial_treatment | boolean | Whether an antimicrobial finish has been applied | true, false |
| Colorfastness | colorfastness | text | Resistance to color loss during washing, rated on a grey scale or qualitative descriptor | Grade 4-5, Excellent, Good |
| Certification | certification | text (list) | Quality, safety, or sustainability certifications | OEKO-TEX Standard 100, GOTS, USDA Organic, ISO 9001, Fair Trade |
| Pack Quantity | pack_quantity | number | Number of pieces per selling unit (pack, case, or dozen) | 1, 6, 12, 24, 60 |
| Selling Unit | selling_unit | enum | How the product is sold | Piece, Dozen, Case, Pack |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (GSM measurement, thread count standards, OEKO-TEX) | [American Soft Linen](https://americansoftlinen.com/collections/wholesale), [Bulk Linen Supply](https://bulklinensupply.com/), [Direct Textile Store](https://directtextilestore.com/standard-towels), [Towel Super Center](https://www.towelsupercenter.com/hotel-towels/) |
