# SKU Schema: Eyewear (Frames & Sunglasses)

**Last updated:** 2026-03-15
**Parent category:** Jewelry, Watches & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | RB-RB3025, OAK-OO9208, ZEN-689316, WP-DURAND |
| Product Name | text | Full product name including brand, model, and variant | Ray-Ban Aviator Classic RB3025, Oakley Holbrook OO9102 Prizm, Warby Parker Durand |
| URL | text | Direct link to the product page | https://example.com/product/aviator-classic |
| Price | number | Numeric retail price excluding currency symbol | 19.00, 169.00, 263.00, 450.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Brand/Manufacturer | text | Eyewear brand or manufacturer name | Ray-Ban, Oakley, Warby Parker, Zenni Optical, Persol, Maui Jim, Tom Ford |
| Product Type | enum | Primary product category | Sunglasses, Optical Frames, Reading Glasses, Safety Glasses, Sport Glasses, Clip-On |
| Frame Material | text | Material of the frame construction | Acetate, Metal, Titanium, TR-90, Stainless Steel, Carbon Fiber, Nylon, Injection Molded |
| Frame Color | text | Color or pattern of the frame | Black, Tortoise, Gold, Matte Black, Havana, Crystal Clear, Blue Gradient |
| Frame Shape | text | Geometric shape classification of the frame | Aviator, Wayfarer, Round, Rectangle, Cat Eye, Square, Oval, Clubmaster, Wrap, Pilot |
| Rim Type | enum | Extent of frame around the lenses | Full Rim, Semi-Rimless, Rimless |
| Lens Width | number (mm) | Horizontal width of one lens | 50, 51, 55, 58, 61, 62 |
| Bridge Width | number (mm) | Distance between lenses across the nose | 14, 16, 17, 18, 20, 22 |
| Temple Length | number (mm) | Length of the arm from hinge to tip | 130, 135, 138, 140, 145 |
| Lens Height | number (mm) | Vertical measurement of the lens | 26, 36, 40, 44, 50 |
| Frame Width | number (mm) | Total horizontal width of the frame across the face | 125, 130, 132, 138, 142 |
| Fit Type | text | Face shape and size suitability designation | Standard, Low Bridge Fit, High Bridge Fit, Asian Fit, Small, Medium, Large |
| Lens Material | text | Material of the lens | Plutonite, Polycarbonate, Glass (Crown or Crystal), CR-39, Trivex, High-Index 1.67 |
| Lens Color/Tint | text | Color of the sunglass lens or tint applied | Grey, Green G-15, Brown Gradient, Blue Mirror, Prizm Ruby, Rose |
| Lens Technology | text (list) | Special coatings or technologies on the lens | Polarized, Photochromic, Anti-Reflective, Blue Light Blocking, Mirror, Gradient |
| UV Protection | text | Level of ultraviolet light filtering | 100% UVA/UVB/UVC (UV400), UV380 |
| Prescription Available | boolean | Whether the frame can accept prescription lenses | Yes, No |
| PD Range | text (mm) | Supported pupillary distance range for prescription fitting | 57-72, 54-74 |
| Hinge Type | text | Type of temple hinge mechanism | Standard Barrel, Spring Hinge, Flex, Hingeless |
| Nose Pad Type | text | Type of nose support | Integrated, Adjustable Silicone, Removable, Saddle Bridge |
| Weight | number (g) | Total weight of the complete frame without lenses | 18, 22, 28, 35, 42 |
| Gender | enum | Target wearer demographic | Men, Women, Unisex, Kids |
| Includes Case | boolean | Whether a protective case is included | Yes, No |
| Lens Category | text | ISO 12312-1 filter category for light transmission | Category 0, Category 1, Category 2, Category 3, Category 4 |
| Country of Origin | text | Country where the eyewear was manufactured | Italy, China, Japan, France, USA |
| Certification | text (list) | Safety and quality certifications | CE, FDA, ANSI Z87.1, AS/NZS 1067, ISO 12312-1, EN 166 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ISO 12312-1, ANSI Z87.1, and EN 166 standards | [Ray-Ban](https://www.ray-ban.com/usa/sunglasses), [Oakley](https://www.oakley.com/en-us/category/sunglasses), [Zenni Optical](https://www.zennioptical.com/), [Warby Parker](https://www.warbyparker.com/) |
