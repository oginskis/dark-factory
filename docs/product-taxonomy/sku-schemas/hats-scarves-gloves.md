# SKU Schema: Hats, Scarves & Gloves

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | GS-2450, DY-BN-101, 819WP-L |
| Product Name | text | Full product name including brand, style, and key features | Grand Sierra Cable Knit Beanie, Brooks Brothers Cashmere Fringed Scarf, Ergodyne ProFlex 819WP Extreme Thermal Waterproof Gloves |
| URL | text | Direct link to the product page | https://example.com/product/beanie-12345 |
| Price | number | Numeric unit price excluding currency symbol | 9.99, 89.50, 57.75 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Grand Sierra, Ergodyne, The North Face, Patagonia, Brooks Brothers |
| Product Type | enum | Primary classification of the accessory | Hat, Beanie, Cap, Visor, Headband, Scarf, Infinity Scarf, Shawl, Stole, Gloves, Mittens, Earmuffs |
| Gender | enum | Target gender for the product | Men, Women, Unisex, Kids |
| Size | text | Size designation | S, M, L, XL, One Size, 7 1/4, S/M, L/XL |
| Size Type | enum | How sizing is expressed | Alpha (S/M/L), Numeric, One Size, Age Range |
| Color | text | Primary color or pattern name | Black, Heather Grey, Navy, Burgundy, Camel, Assorted |
| Pattern | text | Visual pattern or design on the product | Solid, Cable Knit, Fair Isle, Plaid, Striped, Herringbone, Argyle |
| Primary Material | text | Main material or fiber composition | 100% Cashmere, 100% Merino Wool, Acrylic, Fleece, Polyester, Leather, Silk |
| Material Blend | text | Full fiber composition with percentages when blended | 80% Wool / 20% Nylon, 50% Cashmere / 50% Silk, 93% Nomex / 5% Kevlar / 2% Antistatic |
| Construction | enum | How the product is made | Knit, Woven, Felted, Sewn, Molded |
| Lining Material | text | Interior lining fabric if present | Fleece, Sherpa, Silk, Cotton, Unlined |
| Insulation Type | text | Thermal insulation material and weight if applicable | 3M Thinsulate 80g, 3M Thinsulate 150g, PrimaLoft, Down, None |
| Waterproof | boolean | Whether the product provides waterproof protection | true, false |
| Windproof | boolean | Whether the product blocks wind penetration | true, false |
| Touchscreen Compatible | boolean | Whether glove fingertips work with capacitive touchscreens | true, false |
| Closure Type | text | Adjustment or closure mechanism | Adjustable snapback, Fitted, Stretch fit, Hook and loop, Buckle, Drawstring, Elastic cuff |
| Crown Height | enum | Height profile of a hat or cap crown | Low, Mid, High |
| Brim Type | text | Style and shape of hat brim or visor | Flat, Curved, Pre-curved, Wide brim, No brim |
| Panel Count | number | Number of panels in a structured cap | 5, 6, 7 |
| Scarf Length | number (cm) | Total length of a scarf including fringe | 170, 190, 260 |
| Scarf Width | number (cm) | Width of a scarf | 12, 30, 70 |
| Fringe | boolean | Whether the scarf has fringe or tassel trim | true, false |
| Grip Type | text | Palm or finger grip material on gloves | Silicone, Leather palm, PVC dots, Latex dip, None |
| Safety Standard | text | Applicable safety or performance certification | EN 388, EN 511, ANSI/ISEA 105, ASTM F3325 |
| Minimum Temperature Rating | number (C) | Lowest recommended operating temperature in degrees Celsius | -10, -20, -30 |
| Country of Origin | text | Country where the product was manufactured | China, Scotland, Mongolia, Bangladesh, Nepal |
| Pack Quantity | number | Number of items per pack or set; 1 if sold individually | 1, 3, 24 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus EN 388 and EN 511 cold protection standards | [Grand Sierra](https://grandsierragloves.com/), [Ergodyne ProFlex 819WP](https://www.ergodyne.com/proflex-819wp-extreme-thermal-waterproof-gloves.html), [Brooks Brothers Scarves](https://www.brooksbrothers.com/cashmere-fringed-scarf/MT00515.html), [OTTO CAP](https://ottocap.com/blog/cap-101-comprehensive-guide) |
