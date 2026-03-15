# SKU Schema: Men's Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.mens_clothing`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | E422992-000, FON0409WHT, T28/4960A, 143312924 |
| Product Name | product_name | text | Full product name including brand, garment type, and key differentiators | Slim Fit Oxford Button-Down Shirt, Non-Iron Twill Spread Collar Shirt, Stretch Chino Pants |
| URL | url | text | Direct link to the product page | https://example.com/product/slim-fit-oxford-shirt |
| Price | price | number | Numeric retail price per unit, excluding currency symbol | 14.90, 49.99, 129.00, 198.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD, SEK |
| Garment Type | garment_type | text | Type of clothing item | T-Shirt, Dress Shirt, Polo, Jacket, Pants, Shorts, Sweater, Coat, Suit, Blazer, Overshirt |
| Size Type | size_type | enum | Body type or proportioning category for the garment | Regular, Tall, Big, Plus, Petite, Athletic |
| Material | material | text | Primary fabric composition with percentages | 100% Cotton, 98% Cotton 2% Spandex, 60% Cotton 40% Polyester, 97% Cotton 3% Elastane |
| Fabric Type | fabric_type | text | Named weave or knit construction of the fabric | Oxford, Broadcloth, Twill, Jersey, Flannel, Denim, Fleece, Poplin, Chambray, Linen, Corduroy, Seersucker |
| Collar Type | collar_type | text | Style of collar on shirts and jackets | Button-Down, Spread, Semi-Spread, Classic, Point, Band, Cuban, Revere, Grandad, Wing, Notch Lapel, Shawl |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Cuff Type | cuff_type | text | Style of the sleeve cuff on dress shirts | Single, Double, Barrel, French, Mitered, Button, Elastic |
| Closure Type | closure_type | text | Primary fastening mechanism of the garment | Button, Zipper, Snap, Pull-On, Drawstring, Hook and Eye |
| Lining Material | lining_material | text | Fabric used for the interior lining of jackets, coats, and suits | 100% Polyester, 100% Viscose, Silk, Cupro, Unlined |
| Country of Origin | country_of_origin | text | Country where the garment was manufactured | China, Vietnam, Bangladesh, India, Turkey, Portugal, Italy, Cambodia |
| Fit | fit | enum | How the garment is cut relative to the body | Slim, Regular, Classic, Relaxed, Oversized, Athletic, Tailored, Extra Slim, Skinny |
| Color | color | text | Primary color of the garment | Black, Navy, White, Charcoal, Olive, Burgundy, Sky Blue, Pink, Ivory |
| Pattern | pattern | text | Visual pattern or print on the fabric | Solid, Striped, Plaid, Checkered, Herringbone, Paisley, Floral, Camo, Geometric, Polka Dot, Textured |
| Neckline | neckline | text | Style of the neckline on knit tops | Crew Neck, V-Neck, Henley, Mock Neck, Turtleneck, Scoop |
| Pocket Style | pocket_style | text (list) | Types of pockets featured on the garment | Patch, Welt, Flap, Side Seam, Cargo, Chest Pocket, None |
| Iron Level | iron_level | enum | Ease-of-care classification for ironing and wrinkle resistance | Non-Iron, Easy-Iron, Iron Required |
| Inseam | inseam | number (inches) | Interior leg length from crotch to hem on pants | 28, 30, 32, 34, 36 |
| Rise | rise | enum | Vertical distance from crotch seam to waistband on pants | Low, Mid, High |
| Occasion | occasion | text (list) | Intended wearing contexts for the garment | Casual, Business, Formal, Active, Outdoor, Lounge, Party, Wedding |
| Season | season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season, Spring-Summer, Fall-Winter |
| Care Instructions | care_instructions | text | Cleaning and maintenance directions | Machine wash cold, Tumble dry low, Dry clean only, Hand wash |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Added: Size Type, Garment Length, Lining Material, Pocket Style, Iron Level, Gender, Age Group. Updated descriptions and example values for Collar Type, Cuff Type, Fit, Pattern, Occasion, Season, Garment Type, Size, Size System, Material, Fabric Type, UPC, SKU, Color, Features, Country of Origin, Brand. Deprecated: none. Total attributes now 40. | [Charles Tyrwhitt](https://www.charlestyrwhitt.com/us/mens-shirts/), [Marks & Spencer](https://www.marksandspencer.com/l/men/mens-shirts), [ASOS](https://www.asos.com/us/men/shirts/cat/?cid=3602), [Zalando](https://partner.zalando.com/university/pp/attributes-images-and-silhouettes), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
| 2026-03-15 | Initial schema — 33 attributes from 4 retailers plus Google Merchant Center apparel data specification | [Uniqlo](https://www.uniqlo.com/us/en/men/tops/t-shirts), [Brooks Brothers](https://www.brooksbrothers.com/mens/dress-shirts), [REI](https://www.rei.com/c/mens-clothing), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
