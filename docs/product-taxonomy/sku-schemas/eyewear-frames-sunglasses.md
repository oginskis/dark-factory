# SKU Schema: Eyewear (Frames & Sunglasses)

**Last updated:** 2026-03-15
**Parent category:** Jewelry, Watches & Accessories
**Taxonomy ID:** `jewelry.eyewear`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | RB-RB3025, OAK-OO9208, ZEN-689316, WP-DURAND |
| Product Name | product_name | text | — | Full product name including brand, model, and variant | Ray-Ban Aviator Classic RB3025, Oakley Holbrook OO9102 Prizm, Warby Parker Durand |
| URL | url | text | — | Direct link to the product page | https://example.com/product/aviator-classic |
| Price | price | number | — | Numeric retail price excluding currency symbol | 19.00, 169.00, 263.00, 450.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Product Type | product_type | enum | — | Primary product category | Sunglasses, Optical Frames, Reading Glasses, Safety Glasses, Sport Glasses, Clip-On |
| Frame Material | frame_material | text | — | Material of the frame construction | Acetate, Metal, Titanium, TR-90, Stainless Steel, Carbon Fiber, Nylon, Injection Molded |
| Rim Type | rim_type | enum | — | Extent of frame around the lenses | Full Rim, Semi-Rimless, Rimless |
| Fit Type | fit_type | text | — | Face shape and size suitability designation | Standard, Low Bridge Fit, High Bridge Fit, Asian Fit, Small, Medium, Large |
| Lens Material | lens_material | text | — | Material of the lens | Plutonite, Polycarbonate, Glass (Crown or Crystal), CR-39, Trivex, High-Index 1.67 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Hinge Type | hinge_type | text | — | Type of temple hinge mechanism | Standard Barrel, Spring Hinge, Flex, Hingeless |
| Nose Pad Type | nose_pad_type | text | — | Type of nose support | Integrated, Adjustable Silicone, Removable, Saddle Bridge |
| Lens Category | lens_category | text | — | ISO 12312-1 filter category for light transmission | Category 0, Category 1, Category 2, Category 3, Category 4 |
| Country of Origin | country_of_origin | text | — | Country where the eyewear was manufactured | Italy, China, Japan, France, USA |
| Frame Color | frame_color | text | — | Color or pattern of the frame | Black, Tortoise, Gold, Matte Black, Havana, Crystal Clear, Blue Gradient |
| Frame Shape | frame_shape | text | — | Geometric shape classification of the frame | Aviator, Wayfarer, Round, Rectangle, Cat Eye, Square, Oval, Clubmaster, Wrap, Pilot |
| Lens Width | lens_width | number | mm | Horizontal width of one lens | 50, 51, 55, 58, 61, 62 |
| Bridge Width | bridge_width | number | mm | Distance between lenses across the nose | 14, 16, 17, 18, 20, 22 |
| Lens Height | lens_height | number | mm | Vertical measurement of the lens | 26, 36, 40, 44, 50 |
| Frame Width | frame_width | number | mm | Total horizontal width of the frame across the face | 125, 130, 132, 138, 142 |
| Lens Color/Tint | lens_colortint | text | — | Color of the sunglass lens or tint applied | Grey, Green G-15, Brown Gradient, Blue Mirror, Prizm Ruby, Rose |
| Lens Technology | lens_technology | text (list) | — | Special coatings or technologies on the lens | Polarized, Photochromic, Anti-Reflective, Blue Light Blocking, Mirror, Gradient |
| UV Protection | uv_protection | text | — | Level of ultraviolet light filtering | 100% UVA/UVB/UVC (UV400), UV380 |
| Prescription Available | prescription_available | boolean | — | Whether the frame can accept prescription lenses | Yes, No |
| PD Range | pd_range | text | mm | Supported pupillary distance range for prescription fitting | 57-72, 54-74 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ISO 12312-1, ANSI Z87.1, and EN 166 standards | [Ray-Ban](https://www.ray-ban.com/usa/sunglasses), [Oakley](https://www.oakley.com/en-us/category/sunglasses), [Zenni Optical](https://www.zennioptical.com/), [Warby Parker](https://www.warbyparker.com/) |
