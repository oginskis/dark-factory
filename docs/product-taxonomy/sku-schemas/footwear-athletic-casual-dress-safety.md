# SKU Schema: Footwear (Athletic, Casual, Dress, Safety)

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.footwear`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 12W185, NM2190-001, W10563-12M |
| Product Name | text | Full product name including brand, style, and key features | Rocky AlphaForce 6 in Composite Toe Boot, Nike Pegasus 41 Road Running Shoe, Cole Haan Grand Ambition Wingtip Oxford |
| URL | text | Direct link to the product page | https://example.com/product/boot-12345 |
| Price | number | Numeric unit price excluding currency symbol | 129.99, 59.95, 245.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Footwear Category | enum | Primary use classification of the shoe | Athletic, Casual, Dress, Safety, Outdoor, Work & Duty |
| Upper Material | text | Primary material used for the shoe upper | Full-grain leather, Mesh, Nubuck, Suede, Synthetic, Canvas, Knit, Patent Leather |
| Outsole Material | text | Material used for the outsole | Rubber, EVA, Vibram, Polyurethane, TPU |
| Closure Type | enum | Method used to secure the shoe on the foot | Lace-Up, Slip-On, Zip, Buckle, Pull-On, Hook & Loop, Bungee |
| Toe Type | enum | Shape or protection type of the toe box | Round, Pointed, Square, Cap, Almond, Composite, Steel, Alloy, Carbon Fiber |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Lining Material | text | Interior lining material | Textile, Mesh, Leather, Synthetic, Gore-Tex |
| Country of Origin | text | Country where the shoe was manufactured | Vietnam, China, USA, Indonesia, Italy |
| Model Number | text | Manufacturer model or style number | NM2190, 10563, CW4555-001 |
| Style | text | Specific style type within the category | Sneaker, Oxford, Loafer, Boot, Chelsea, Moccasin, Sandal, Chukka, Derby, Monk Strap |
| Gender | enum | Target gender for the product | Men, Women, Unisex, Kids |
| Width | enum | Shoe width designation | Extra Narrow, Narrow, Medium, Wide, Extra Wide, Extra-Extra Wide |
| Color | text | Primary color or colorway name | Black, Brown, White/University Red, Midnight Navy |
| Midsole Technology | text | Cushioning or midsole system used | Nike React, Zoom Air, Fresh Foam, BOOST, EVA, Polyurethane |
| Heel Height | number (mm) | Height of the heel measured from the outsole | 10, 25, 38, 75 |
| Heel-to-Toe Drop | number (mm) | Difference in stack height between heel and forefoot | 0, 4, 8, 10, 12 |
| Waterproof | boolean | Whether the shoe provides waterproof protection | true, false |
| Slip Resistant | boolean | Whether the outsole is rated for slip resistance | true, false |
| Safety Standard | text | Applicable safety certification codes | ASTM F2413, EN ISO 20345, CSA Z195 |
| Safety Toe Rating | text | Impact and compression protection level | I/75 C/75, I/50 C/50, S3, S1P |
| Electrical Hazard | boolean | Whether the shoe provides electrical hazard protection per ASTM | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 32 attributes from 4 sources plus ASTM F2413 and EN ISO 20345 safety standards | [Zappos](https://www.zappos.com/men-shoes), [Grainger Safety Footwear](https://www.grainger.com/category/safety/footwear-and-footwear-accessories), [WorkBoots.com ASTM Guide](https://workboots.com/tradecraft/astm-osha-and-ansi-a-complete-guide-to-safety-footwear), [Nike](https://www.nike.com/) |
