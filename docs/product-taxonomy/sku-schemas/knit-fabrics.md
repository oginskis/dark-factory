# SKU Schema: Knit Fabrics

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | KF-2041, ITK-J100, 89012345 |
| Product Name | text | Full product name including key specs such as fiber content, knit type, and weight | Cotton Jersey Knit 180 GSM 60in, Rayon Spandex Interlock Black |
| URL | text | Direct link to the product page | https://example.com/product/cotton-jersey-knit-180gsm |
| Price | number | Numeric price per unit (typically per yard or per metre), excluding currency symbol | 7.99, 14.50, 24.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Fabric brand, mill, or supplier name | Pine Crest Fabrics, Mood Fabrics, Telio, Robert Kaufman |
| Knit Type | enum | Primary knit construction category | Jersey, Interlock, Rib Knit, French Terry, Ponte, Sweater Knit, Double Knit, Tricot |
| Fiber Content | text | Full fiber composition with percentages | 95% Cotton 5% Spandex, 100% Polyester, 66% Polyester 33% Rayon 1% Spandex |
| Primary Fiber | text | Dominant fiber in the composition | Cotton, Polyester, Rayon, Nylon, Bamboo, Modal, Wool |
| Fabric Weight | number (GSM) | Mass per unit area in grams per square metre | 120, 180, 245, 440 |
| Fabric Weight Oz | number (oz/yd2) | Mass per unit area in ounces per square yard | 4.0, 5.3, 7.2, 12.9 |
| Weight Class | enum | General weight classification | Lightweight, Medium Weight, Heavyweight |
| Width | number (in) | Usable fabric width in inches | 48, 58, 60, 62, 70 |
| Stretch Direction | enum | Direction in which the fabric stretches | 2-Way Stretch, 4-Way Stretch, Mechanical Stretch, No Stretch |
| Stretch Percentage | number (%) | Maximum stretch as a percentage of relaxed length | 25, 50, 75, 100 |
| Recovery | enum | How well the fabric returns to its original shape after stretching | Excellent, Good, Moderate, Poor |
| Courses Per Inch | number | Number of horizontal stitch rows per inch, indicating knit density | 28, 36, 44, 56 |
| Wales Per Inch | number | Number of vertical stitch columns per inch, indicating knit density | 24, 32, 40, 48 |
| Gauge | text | Machine gauge used in production, indicating stitch fineness | 18 GG, 24 GG, 28 GG, 32 GG |
| Color | text | Fabric color or print description | Black, White, Navy, Heather Grey, Floral Print |
| Pattern | text | Surface pattern or print type | Solid, Striped, Printed, Heathered, Melange, Tie-Dye |
| Finish | text | Surface treatment or finishing applied | Brushed, Peached, Mercerized, Enzyme Washed, Anti-Pilling |
| Opacity | enum | Light-blocking characteristic of the fabric | Opaque, Semi-Opaque, Semi-Sheer, Sheer |
| Hand Feel | text | Tactile quality of the fabric surface | Soft, Silky, Crisp, Plush, Smooth |
| Pilling Resistance | enum | Resistance to surface pilling per ISO 12945 (1 = severe, 5 = none) | 1, 2, 3, 4, 5 |
| Colorfastness to Washing | enum | Color retention after washing per ISO 105-C06 (1 = poor, 5 = excellent) | 3, 4, 4-5, 5 |
| Shrinkage | number (%) | Expected dimensional change after washing | 2, 3, 5, 8 |
| Application | text (list) | Intended end-use categories for the fabric | T-Shirts, Activewear, Loungewear, Dresses, Leggings, Underwear, Baby Apparel |
| Certification | text (list) | Sustainability and safety certifications | OEKO-TEX Standard 100, GOTS, GRS, bluesign |
| Country of Origin | text | Country where the fabric was manufactured | China, South Korea, Turkey, India, USA, Pakistan |
| Minimum Order Quantity | number | Minimum purchase quantity in yards or metres | 1, 10, 15, 50 |
| Selling Unit | enum | Unit of measure for pricing and ordering | Yard, Metre, Roll, Kilogram |
| Roll Length | number (yd) | Standard length per roll or bolt | 25, 50, 80, 100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ISO 12945, ISO 105) | [Fabric Wholesale Direct](https://fabricwholesaledirect.com/collections/interlock-knit-fabric), [Pine Crest Fabrics](https://pinecrestfabrics.com/product-category/wholesale-fabric-supplier/stocked-fabrics/interlock-knit-fabric/), [Mood Fabrics](https://www.moodfabrics.com/collections/interlock-knit-fashion-fabrics), [Rockywoods Fabrics](https://rockywoods.com/products/heavyweight-nylon-spandex-jersey-in-team-colors) |
