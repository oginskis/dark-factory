# SKU Schema: Cosmetics & Color Cosmetics

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.cosmetics`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 999NAC0000112, P411885, M6TN01 |
| Product Name | product_name | text | — | Full product name including brand, line, shade, and finish | MAC MACximal Silky Matte Lipstick Velvet Teddy, NARS Soft Matte Complete Foundation Deauville |
| URL | url | text | — | Direct link to the product page | https://www.maccosmetics.com/product/13854/123863/products/makeup/lips/lipstick/macximal-silky-matte-lipstick |
| Price | price | number | — | Numeric unit price excluding currency symbol | 25.00, 40.00, 14.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Type | product_type | enum | — | Primary product classification | Lipstick, Foundation, Concealer, Blush, Eyeshadow, Mascara, Eyeliner, Brow Product, Powder, Bronzer, Highlighter, Lip Gloss, Primer, Setting Spray |
| Finish Type | finish_type | enum | — | Surface finish of the product | Matte, Satin, Glossy, Shimmer, Metallic, Cream, Dewy, Velvet, Frost, Luminous |
| Formulation | formulation | enum | — | Physical form of the product | Liquid, Cream, Powder, Stick, Pencil, Gel, Mousse, Cushion, Pressed, Loose |
| Key Ingredients | key_ingredients | text (list) | — | Featured beneficial ingredients | Coconut Oil, Shea Butter, Hyaluronic Acid, Vitamin E, Niacinamide, Retinol |
| INCI Ingredients | inci_ingredients | text | — | Full INCI ingredient list from packaging | Octyldodecanol, Neopentyl Glycol Diheptanoate, Synthetic Wax, Silica |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Skin Type | skin_type | text (list) | — | Targeted skin type | Normal, Dry, Oily, Combination, Sensitive, All |
| Applicator Type | applicator_type | text | — | Type of application tool included | Bullet, Doe Foot, Brush, Sponge Tip, Wand, Pencil, Built-In Brush, None |
| Packaging Material | packaging_material | text | — | Primary packaging material | Plastic, Glass, Metal, Refillable Case, PCR Plastic |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, France, Italy, Japan, South Korea, China |
| Volume | volume | number | ml | Volume for liquid products | 30, 35, 8, 6.5 |
| Shade Name | shade_name | text | — | Name of the specific color shade | Velvet Teddy, Ruby Woo, Deauville, Gobi, Fenty 240 |
| Shade Number | shade_number | text | — | Numeric or alphanumeric shade identifier | NC15, NW25, 240, 02, 1.5 |
| Shade Family | shade_family | enum | — | General color grouping | Nude, Pink, Red, Orange, Berry, Coral, Brown, Neutral, Cool, Warm |
| Undertone | undertone | enum | — | Undertone classification for face products | Cool, Warm, Neutral |
| Coverage | coverage | enum | — | Level of coverage for face products | Sheer, Light, Medium, Full, Buildable |
| SPF | spf | number | — | Sun protection factor when present | 15, 25, 30, 40, 50 |
| Wear Time | wear_time | number | hours | Claimed duration of product wear | 8, 12, 16, 24 |
| Waterproof | waterproof | enum | — | Whether the product is water-resistant or waterproof | Yes, No, Water-Resistant |
| Transfer-Resistant | transfer-resistant | enum | — | Whether the product resists transfer to clothing or surfaces | Yes, No |
| Fragrance Free | fragrance_free | enum | — | Whether the product is fragrance-free | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus FDA cosmetic product codes and EU regulations | [MAC MACximal Silky Matte Lipstick](https://www.maccosmetics.com/product/13854/123863/products/makeup/lips/lipstick/macximal-silky-matte-lipstick), [NARS Soft Matte Foundation](https://www.narscosmetics.com/USA/soft-matte-complete-foundation/999NAC0000112.html), [Sephora Foundations](https://www.sephora.com/shop/foundation-makeup), [FDA Cosmetic Product Categories](https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products/cosmetic-product-categories-and-codes) |
