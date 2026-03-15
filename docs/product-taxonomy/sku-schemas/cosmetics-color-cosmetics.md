# SKU Schema: Cosmetics & Color Cosmetics

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 999NAC0000112, P411885, M6TN01 |
| Product Name | text | Full product name including brand, line, shade, and finish | MAC MACximal Silky Matte Lipstick Velvet Teddy, NARS Soft Matte Complete Foundation Deauville |
| URL | text | Direct link to the product page | https://www.maccosmetics.com/product/13854/123863/products/makeup/lips/lipstick/macximal-silky-matte-lipstick |
| Price | number | Numeric unit price excluding currency symbol | 25.00, 40.00, 14.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | MAC, NARS, Maybelline, L'Oreal, Estee Lauder, NYX, Fenty Beauty |
| Product Type | enum | Primary product classification | Lipstick, Foundation, Concealer, Blush, Eyeshadow, Mascara, Eyeliner, Brow Product, Powder, Bronzer, Highlighter, Lip Gloss, Primer, Setting Spray |
| Net Weight | number (g) | Net weight of the product | 3.5, 30, 7.0, 1.2 |
| Volume | number (ml) | Volume for liquid products | 30, 35, 8, 6.5 |
| Shade Name | text | Name of the specific color shade | Velvet Teddy, Ruby Woo, Deauville, Gobi, Fenty 240 |
| Shade Number | text | Numeric or alphanumeric shade identifier | NC15, NW25, 240, 02, 1.5 |
| Shade Family | enum | General color grouping | Nude, Pink, Red, Orange, Berry, Coral, Brown, Neutral, Cool, Warm |
| Undertone | enum | Undertone classification for face products | Cool, Warm, Neutral |
| Finish Type | enum | Surface finish of the product | Matte, Satin, Glossy, Shimmer, Metallic, Cream, Dewy, Velvet, Frost, Luminous |
| Coverage | enum | Level of coverage for face products | Sheer, Light, Medium, Full, Buildable |
| Formulation | enum | Physical form of the product | Liquid, Cream, Powder, Stick, Pencil, Gel, Mousse, Cushion, Pressed, Loose |
| SPF | number | Sun protection factor when present | 15, 25, 30, 40, 50 |
| Wear Time | number (hours) | Claimed duration of product wear | 8, 12, 16, 24 |
| Key Ingredients | text (list) | Featured beneficial ingredients | Coconut Oil, Shea Butter, Hyaluronic Acid, Vitamin E, Niacinamide, Retinol |
| INCI Ingredients | text | Full INCI ingredient list from packaging | Octyldodecanol, Neopentyl Glycol Diheptanoate, Synthetic Wax, Silica |
| Skin Type | text (list) | Targeted skin type | Normal, Dry, Oily, Combination, Sensitive, All |
| Waterproof | enum | Whether the product is water-resistant or waterproof | Yes, No, Water-Resistant |
| Transfer-Resistant | enum | Whether the product resists transfer to clothing or surfaces | Yes, No |
| Fragrance Free | enum | Whether the product is fragrance-free | Yes, No |
| Cruelty Free | enum | Whether the product is certified cruelty-free | Yes, No |
| Vegan | enum | Whether the product contains no animal-derived ingredients | Yes, No |
| Refillable | enum | Whether the product packaging supports refills | Yes, No |
| Number of Shades | number | Total shades available in the product line | 34, 40, 50, 24 |
| Applicator Type | text | Type of application tool included | Bullet, Doe Foot, Brush, Sponge Tip, Wand, Pencil, Built-In Brush, None |
| Certifications | text (list) | Regulatory and quality certifications | EU Cosmetics Regulation, FDA Registered, ISO 22716, Leaping Bunny, PETA |
| Packaging Material | text | Primary packaging material | Plastic, Glass, Metal, Refillable Case, PCR Plastic |
| Country of Origin | text | Country where the product is manufactured | USA, France, Italy, Japan, South Korea, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus FDA cosmetic product codes and EU regulations | [MAC MACximal Silky Matte Lipstick](https://www.maccosmetics.com/product/13854/123863/products/makeup/lips/lipstick/macximal-silky-matte-lipstick), [NARS Soft Matte Foundation](https://www.narscosmetics.com/USA/soft-matte-complete-foundation/999NAC0000112.html), [Sephora Foundations](https://www.sephora.com/shop/foundation-makeup), [FDA Cosmetic Product Categories](https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products/cosmetic-product-categories-and-codes) |
