# SKU Schema: Woven Fabrics

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.woven_fabrics`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 10-19188, FWD-WV-4420, MMI-T300 |
| Product Name | product_name | text | — | Full product name including fabric type, composition, and key characteristics | 100% Cotton Poplin Solid White 58/60 in, Nomex IIIA Twill 6.0 oz FR Fabric, Organic Linen Chambray Natural 54 in |
| URL | url | text | — | Direct link to the product page | https://example.com/product/cotton-poplin-12345 |
| Price | price | number | — | Numeric price per unit of measure (yard, metre, or bolt) excluding currency symbol | 3.99, 12.50, 48.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Fabric Type | fabric_type | text | — | Named fabric classification based on weave and finish | Poplin, Twill, Denim, Satin, Sateen, Chambray, Canvas, Chiffon, Organza, Taffeta, Broadcloth, Muslin, Duck |
| Country of Origin | country_of_origin | text | — | Country where the fabric was woven and finished | China, India, Japan, Italy, Turkey, USA, Pakistan |
| Fabric Weight | fabric_weight | number | g/m2 | Weight per square metre (GSM) | 110, 170, 240, 350 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Brand/Mill | brandmill | text | — | Fabric mill, brand, or supplier name | Robert Kaufman, Milliken, Burlington, Tex Tech Industries, Liberty Fabrics |
| Weave Structure | weave_structure | enum | — | Fundamental interlacing pattern of warp and weft yarns | Plain, Twill, Satin, Basket, Dobby, Jacquard, Leno |
| Fiber Content | fiber_content | text | — | Complete fiber composition with percentages | 100% Cotton, 65% Polyester / 35% Cotton, 100% Linen, 55% Linen / 45% Rayon |
| Primary Fiber | primary_fiber | enum | — | Dominant fiber family in the blend | Cotton, Polyester, Linen, Silk, Wool, Rayon, Nylon, Viscose, Tencel, Bamboo, Aramid |
| Width | width | number | in | Usable width of the fabric from selvage to selvage | 44, 54, 58, 60, 108 |
| Ends Per Inch | ends_per_inch | number | — | Number of warp threads per inch | 68, 80, 110, 144 |
| Picks Per Inch | picks_per_inch | number | — | Number of weft threads per inch | 60, 72, 96, 120 |
| Color | color | text | — | Fabric color or dye name | White, Natural, Indigo, Black, Navy, Khaki, Multicolor |
| Pattern | pattern | text | — | Visual pattern or print on the fabric | Solid, Plaid, Stripe, Floral, Geometric, Paisley, Polka Dot, Animal Print, Camo |
| Dye Method | dye_method | text | — | Technique used to color the fabric | Piece dyed, Yarn dyed, Solution dyed, Printed, Pigment dyed, Undyed |
| Finish | finish | text (list) | — | Surface treatments or chemical finishes applied | Mercerized, Sanforized, Calendered, Brushed, Water-repellent (DWR), Wrinkle-free, Anti-pilling, Flame retardant |
| Shrinkage | shrinkage | number | % | Maximum dimensional change after washing per test standard | 1, 2, 3, 5 |
| Colorfastness Rating | colorfastness_rating | number | — | Colorfastness grade on 1-5 scale per ISO 105 | 3, 4, 5 |
| Abrasion Resistance | abrasion_resistance | number | cycles | Martindale abrasion test result in cycles before fabric breakdown | 10000, 25000, 50000, 100000 |
| Pilling Rating | pilling_rating | number | — | Pilling resistance on 1-5 scale per ISO 12945 | 3, 4, 5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus ISO 12947 (abrasion), ISO 12945 (pilling), and ISO 105 (colorfastness) testing standards | [Fabric Merchants](https://www.fabricmerchants.com/woven-fabrics/), [Fabric Wholesale Direct](https://fabricwholesaledirect.com/collections/woven-fabric), [MMI Textiles](https://www.mmitextiles.com/product-lines/woven-fabric/), [World Collective Technical Fabric Guide](https://world-collective.com/blogs/news/technical-fabric-properties-guide-gsm-weaves-finishes-and-testing) |
