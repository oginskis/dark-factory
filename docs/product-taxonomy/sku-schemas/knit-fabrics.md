# SKU Schema: Knit Fabrics

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.knit_fabrics`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | KF-2041, ITK-J100, 89012345 |
| Product Name | product_name | text | — | Full product name including key specs such as fiber content, knit type, and weight | Cotton Jersey Knit 180 GSM 60in, Rayon Spandex Interlock Black |
| URL | url | text | — | Direct link to the product page | https://example.com/product/cotton-jersey-knit-180gsm |
| Price | price | number | — | Numeric price per unit (typically per yard or per metre), excluding currency symbol | 7.99, 14.50, 24.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Knit Type | knit_type | enum | — | Primary knit construction category | Jersey, Interlock, Rib Knit, French Terry, Ponte, Sweater Knit, Double Knit, Tricot |
| Weight Class | weight_class | enum | — | General weight classification | Lightweight, Medium Weight, Heavyweight |
| Country of Origin | country_of_origin | text | — | Country where the fabric was manufactured | China, South Korea, Turkey, India, USA, Pakistan |
| Fabric Weight | fabric_weight | number | GSM | Mass per unit area in grams per square metre | 120, 180, 245, 440 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Fiber Content | fiber_content | text | — | Full fiber composition with percentages | 95% Cotton 5% Spandex, 100% Polyester, 66% Polyester 33% Rayon 1% Spandex |
| Primary Fiber | primary_fiber | text | — | Dominant fiber in the composition | Cotton, Polyester, Rayon, Nylon, Bamboo, Modal, Wool |
| Width | width | number | in | Usable fabric width in inches | 48, 58, 60, 62, 70 |
| Stretch Direction | stretch_direction | enum | — | Direction in which the fabric stretches | 2-Way Stretch, 4-Way Stretch, Mechanical Stretch, No Stretch |
| Stretch Percentage | stretch_percentage | number | % | Maximum stretch as a percentage of relaxed length | 25, 50, 75, 100 |
| Recovery | recovery | enum | — | How well the fabric returns to its original shape after stretching | Excellent, Good, Moderate, Poor |
| Courses Per Inch | courses_per_inch | number | — | Number of horizontal stitch rows per inch, indicating knit density | 28, 36, 44, 56 |
| Wales Per Inch | wales_per_inch | number | — | Number of vertical stitch columns per inch, indicating knit density | 24, 32, 40, 48 |
| Gauge | gauge | text | — | Machine gauge used in production, indicating stitch fineness | 18 GG, 24 GG, 28 GG, 32 GG |
| Color | color | text | — | Fabric color or print description | Black, White, Navy, Heather Grey, Floral Print |
| Pattern | pattern | text | — | Surface pattern or print type | Solid, Striped, Printed, Heathered, Melange, Tie-Dye |
| Finish | finish | text | — | Surface treatment or finishing applied | Brushed, Peached, Mercerized, Enzyme Washed, Anti-Pilling |
| Opacity | opacity | enum | — | Light-blocking characteristic of the fabric | Opaque, Semi-Opaque, Semi-Sheer, Sheer |
| Hand Feel | hand_feel | text | — | Tactile quality of the fabric surface | Soft, Silky, Crisp, Plush, Smooth |
| Pilling Resistance | pilling_resistance | enum | — | Resistance to surface pilling per ISO 12945 (1 = severe, 5 = none) | 1, 2, 3, 4, 5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ISO 12945, ISO 105) | [Fabric Wholesale Direct](https://fabricwholesaledirect.com/collections/interlock-knit-fabric), [Pine Crest Fabrics](https://pinecrestfabrics.com/product-category/wholesale-fabric-supplier/stocked-fabrics/interlock-knit-fabric/), [Mood Fabrics](https://www.moodfabrics.com/collections/interlock-knit-fashion-fabrics), [Rockywoods Fabrics](https://rockywoods.com/products/heavyweight-nylon-spandex-jersey-in-team-colors) |
