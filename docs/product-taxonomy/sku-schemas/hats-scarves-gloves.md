# SKU Schema: Hats, Scarves & Gloves

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.hats_scarves_gloves`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | GS-2450, DY-BN-101, 819WP-L |
| Product Name | product_name | text | Full product name including brand, style, and key features | Grand Sierra Cable Knit Beanie, Brooks Brothers Cashmere Fringed Scarf, Ergodyne ProFlex 819WP Extreme Thermal Waterproof Gloves |
| URL | url | text | Direct link to the product page | https://example.com/product/beanie-12345 |
| Price | price | number | Numeric unit price excluding currency symbol | 9.99, 89.50, 57.75 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary classification of the accessory | Hat, Beanie, Cap, Visor, Headband, Scarf, Infinity Scarf, Shawl, Stole, Gloves, Mittens, Earmuffs |
| Size Type | size_type | enum | How sizing is expressed | Alpha (S/M/L), Numeric, One Size, Age Range |
| Primary Material | primary_material | text | Main material or fiber composition | 100% Cashmere, 100% Merino Wool, Acrylic, Fleece, Polyester, Leather, Silk |
| Material Blend | material_blend | text | Full fiber composition with percentages when blended | 80% Wool / 20% Nylon, 50% Cashmere / 50% Silk, 93% Nomex / 5% Kevlar / 2% Antistatic |
| Lining Material | lining_material | text | Interior lining fabric if present | Fleece, Sherpa, Silk, Cotton, Unlined |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Insulation Type | insulation_type | text | Thermal insulation material and weight if applicable | 3M Thinsulate 80g, 3M Thinsulate 150g, PrimaLoft, Down, None |
| Closure Type | closure_type | text | Adjustment or closure mechanism | Adjustable snapback, Fitted, Stretch fit, Hook and loop, Buckle, Drawstring, Elastic cuff |
| Brim Type | brim_type | text | Style and shape of hat brim or visor | Flat, Curved, Pre-curved, Wide brim, No brim |
| Grip Type | grip_type | text | Palm or finger grip material on gloves | Silicone, Leather palm, PVC dots, Latex dip, None |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | China, Scotland, Mongolia, Bangladesh, Nepal |
| Gender | gender | enum | Target gender for the product | Men, Women, Unisex, Kids |
| Color | color | text | Primary color or pattern name | Black, Heather Grey, Navy, Burgundy, Camel, Assorted |
| Pattern | pattern | text | Visual pattern or design on the product | Solid, Cable Knit, Fair Isle, Plaid, Striped, Herringbone, Argyle |
| Construction | construction | enum | How the product is made | Knit, Woven, Felted, Sewn, Molded |
| Waterproof | waterproof | boolean | Whether the product provides waterproof protection | true, false |
| Windproof | windproof | boolean | Whether the product blocks wind penetration | true, false |
| Touchscreen Compatible | touchscreen_compatible | boolean | Whether glove fingertips work with capacitive touchscreens | true, false |
| Crown Height | crown_height | enum | Height profile of a hat or cap crown | Low, Mid, High |
| Scarf Width | scarf_width | number (cm) | Width of a scarf | 12, 30, 70 |
| Fringe | fringe | boolean | Whether the scarf has fringe or tassel trim | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus EN 388 and EN 511 cold protection standards | [Grand Sierra](https://grandsierragloves.com/), [Ergodyne ProFlex 819WP](https://www.ergodyne.com/proflex-819wp-extreme-thermal-waterproof-gloves.html), [Brooks Brothers Scarves](https://www.brooksbrothers.com/cashmere-fringed-scarf/MT00515.html), [OTTO CAP](https://ottocap.com/blog/cap-101-comprehensive-guide) |
