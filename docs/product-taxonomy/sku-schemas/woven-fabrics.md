# SKU Schema: Woven Fabrics

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 10-19188, FWD-WV-4420, MMI-T300 |
| Product Name | text | Full product name including fabric type, composition, and key characteristics | 100% Cotton Poplin Solid White 58/60 in, Nomex IIIA Twill 6.0 oz FR Fabric, Organic Linen Chambray Natural 54 in |
| URL | text | Direct link to the product page | https://example.com/product/cotton-poplin-12345 |
| Price | number | Numeric price per unit of measure (yard, metre, or bolt) excluding currency symbol | 3.99, 12.50, 48.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Brand/Mill | text | Fabric mill, brand, or supplier name | Robert Kaufman, Milliken, Burlington, Tex Tech Industries, Liberty Fabrics |
| Fabric Type | text | Named fabric classification based on weave and finish | Poplin, Twill, Denim, Satin, Sateen, Chambray, Canvas, Chiffon, Organza, Taffeta, Broadcloth, Muslin, Duck |
| Weave Structure | enum | Fundamental interlacing pattern of warp and weft yarns | Plain, Twill, Satin, Basket, Dobby, Jacquard, Leno |
| Fiber Content | text | Complete fiber composition with percentages | 100% Cotton, 65% Polyester / 35% Cotton, 100% Linen, 55% Linen / 45% Rayon |
| Primary Fiber | enum | Dominant fiber family in the blend | Cotton, Polyester, Linen, Silk, Wool, Rayon, Nylon, Viscose, Tencel, Bamboo, Aramid |
| Fabric Weight | number (g/m2) | Weight per square metre (GSM) | 110, 170, 240, 350 |
| Fabric Weight oz | number (oz/yd2) | Weight per square yard in ounces | 3.2, 5.0, 7.5, 10.0 |
| Width | number (in) | Usable width of the fabric from selvage to selvage | 44, 54, 58, 60, 108 |
| Thread Count | number | Total number of warp and weft threads per square inch | 60, 132, 200, 400 |
| Ends Per Inch | number | Number of warp threads per inch | 68, 80, 110, 144 |
| Picks Per Inch | number | Number of weft threads per inch | 60, 72, 96, 120 |
| Yarn Count | text | Yarn fineness expressed in the relevant system (Ne for cotton, Nm for metric, denier for filament) | 40s Ne, 60/2 Ne, 150D, 30 Nm |
| Color | text | Fabric color or dye name | White, Natural, Indigo, Black, Navy, Khaki, Multicolor |
| Pattern | text | Visual pattern or print on the fabric | Solid, Plaid, Stripe, Floral, Geometric, Paisley, Polka Dot, Animal Print, Camo |
| Dye Method | text | Technique used to color the fabric | Piece dyed, Yarn dyed, Solution dyed, Printed, Pigment dyed, Undyed |
| Finish | text (list) | Surface treatments or chemical finishes applied | Mercerized, Sanforized, Calendered, Brushed, Water-repellent (DWR), Wrinkle-free, Anti-pilling, Flame retardant |
| Shrinkage | number (%) | Maximum dimensional change after washing per test standard | 1, 2, 3, 5 |
| Colorfastness Rating | number | Colorfastness grade on 1-5 scale per ISO 105 | 3, 4, 5 |
| Abrasion Resistance | number (cycles) | Martindale abrasion test result in cycles before fabric breakdown | 10000, 25000, 50000, 100000 |
| Pilling Rating | number | Pilling resistance on 1-5 scale per ISO 12945 | 3, 4, 5 |
| Stretch | boolean | Whether the fabric has mechanical or spandex-based stretch | true, false |
| Stretch Percentage | number (%) | Amount of stretch in the fabric if applicable | 2, 5, 10, 25 |
| Application | text (list) | Intended end uses for the fabric | Shirting, Suiting, Dressmaking, Upholstery, Outerwear, Quilting, Industrial, Drapery |
| Bolt Length | number (yd) | Standard length per bolt or roll | 15, 25, 50, 100 |
| Certification | text (list) | Sustainability or safety certifications | OEKO-TEX Standard 100, GOTS, Bluesign, GRS, REACH compliant |
| Country of Origin | text | Country where the fabric was woven and finished | China, India, Japan, Italy, Turkey, USA, Pakistan |
| Minimum Order Quantity | number (yd) | Minimum yardage required for wholesale purchase | 1, 10, 50, 500 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus ISO 12947 (abrasion), ISO 12945 (pilling), and ISO 105 (colorfastness) testing standards | [Fabric Merchants](https://www.fabricmerchants.com/woven-fabrics/), [Fabric Wholesale Direct](https://fabricwholesaledirect.com/collections/woven-fabric), [MMI Textiles](https://www.mmitextiles.com/product-lines/woven-fabric/), [World Collective Technical Fabric Guide](https://world-collective.com/blogs/news/technical-fabric-properties-guide-gsm-weaves-finishes-and-testing) |
