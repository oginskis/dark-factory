# SKU Schema: Men's Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | E422992-000, FON0409WHT, T28/4960A, 143312924 |
| Product Name | text | Full product name including brand, garment type, and key differentiators | Slim Fit Oxford Button-Down Shirt, Non-Iron Twill Spread Collar Shirt, Stretch Chino Pants |
| URL | text | Direct link to the product page | https://example.com/product/slim-fit-oxford-shirt |
| Price | number | Numeric retail price per unit, excluding currency symbol | 14.90, 49.99, 129.00, 198.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD, SEK |
| Brand | text | Name of the clothing brand or designer | Uniqlo, Brooks Brothers, Levi's, Ralph Lauren, H&M, Charles Tyrwhitt, Marks & Spencer |
| Garment Type | text | Type of clothing item | T-Shirt, Dress Shirt, Polo, Jacket, Pants, Shorts, Sweater, Coat, Suit, Blazer, Overshirt |
| Size | text | Garment size designation | XS, S, M, L, XL, XXL, 3XL, 4XL, 15/32, 32x30, 38R |
| Size System | text | Country or regional sizing standard used | US, EU, UK, JP, AU, IT, FR |
| Size Type | enum | Body type or proportioning category for the garment | Regular, Tall, Big, Plus, Petite, Athletic |
| Fit | enum | How the garment is cut relative to the body | Slim, Regular, Classic, Relaxed, Oversized, Athletic, Tailored, Extra Slim, Skinny |
| Color | text | Primary color of the garment | Black, Navy, White, Charcoal, Olive, Burgundy, Sky Blue, Pink, Ivory |
| Pattern | text | Visual pattern or print on the fabric | Solid, Striped, Plaid, Checkered, Herringbone, Paisley, Floral, Camo, Geometric, Polka Dot, Textured |
| Material | text | Primary fabric composition with percentages | 100% Cotton, 98% Cotton 2% Spandex, 60% Cotton 40% Polyester, 97% Cotton 3% Elastane |
| Fabric Type | text | Named weave or knit construction of the fabric | Oxford, Broadcloth, Twill, Jersey, Flannel, Denim, Fleece, Poplin, Chambray, Linen, Corduroy, Seersucker |
| Fabric Weight | text | Weight classification or GSM of the fabric | Lightweight, Midweight, Heavyweight, 150 GSM, 280 GSM |
| Collar Type | text | Style of collar on shirts and jackets | Button-Down, Spread, Semi-Spread, Classic, Point, Band, Cuban, Revere, Grandad, Wing, Notch Lapel, Shawl |
| Sleeve Length | text | Length of the sleeve | Short, Long, Three-Quarter, Sleeveless, Roll-Up |
| Cuff Type | text | Style of the sleeve cuff on dress shirts | Single, Double, Barrel, French, Mitered, Button, Elastic |
| Neckline | text | Style of the neckline on knit tops | Crew Neck, V-Neck, Henley, Mock Neck, Turtleneck, Scoop |
| Closure Type | text | Primary fastening mechanism of the garment | Button, Zipper, Snap, Pull-On, Drawstring, Hook and Eye |
| Garment Length | enum | Overall length classification of the garment | Regular, Short, Long, Cropped |
| Lining Material | text | Fabric used for the interior lining of jackets, coats, and suits | 100% Polyester, 100% Viscose, Silk, Cupro, Unlined |
| Pocket Style | text (list) | Types of pockets featured on the garment | Patch, Welt, Flap, Side Seam, Cargo, Chest Pocket, None |
| Iron Level | enum | Ease-of-care classification for ironing and wrinkle resistance | Non-Iron, Easy-Iron, Iron Required |
| Inseam | number (inches) | Interior leg length from crotch to hem on pants | 28, 30, 32, 34, 36 |
| Waist Size | number (inches) | Waist measurement on pants and shorts | 28, 30, 32, 34, 36, 38, 40 |
| Neck Size | number (inches) | Collar circumference on dress shirts | 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18 |
| Chest Size | number (inches) | Chest circumference for jackets and suits | 36, 38, 40, 42, 44, 46, 48 |
| Rise | enum | Vertical distance from crotch seam to waistband on pants | Low, Mid, High |
| Occasion | text (list) | Intended wearing contexts for the garment | Casual, Business, Formal, Active, Outdoor, Lounge, Party, Wedding |
| Season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season, Spring-Summer, Fall-Winter |
| Care Instructions | text | Cleaning and maintenance directions | Machine wash cold, Tumble dry low, Dry clean only, Hand wash |
| Country of Origin | text | Country where the garment was manufactured | China, Vietnam, Bangladesh, India, Turkey, Portugal, Italy, Cambodia |
| Sustainability Certification | text (list) | Environmental or ethical certifications | OEKO-TEX, GOTS, Fair Trade, BCI, Bluesign, GRS |
| Gender | enum | Target gender for the garment, used for product feed classification | Male, Unisex |
| Age Group | enum | Target age demographic for the garment | Adults, Young Adults |
| UPC | text | Universal Product Code or EAN barcode number | 194501234567, 012345678905, 4062838000112 |
| Product Technology | text (list) | Proprietary or named fabric technologies | AIRism, DRY-EX, HEATTECH, Dri-FIT, COOLMAX, Gore-Tex, Supima |
| Features | text (list) | Functional design details and enhancements | Moisture-wicking, Stretch, Wrinkle-resistant, UV protection, Odor control, Water-repellent, Non-iron finish |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Added: Size Type, Garment Length, Lining Material, Pocket Style, Iron Level, Gender, Age Group. Updated descriptions and example values for Collar Type, Cuff Type, Fit, Pattern, Occasion, Season, Garment Type, Size, Size System, Material, Fabric Type, UPC, SKU, Color, Features, Country of Origin, Brand. Deprecated: none. Total attributes now 40. | [Charles Tyrwhitt](https://www.charlestyrwhitt.com/us/mens-shirts/), [Marks & Spencer](https://www.marksandspencer.com/l/men/mens-shirts), [ASOS](https://www.asos.com/us/men/shirts/cat/?cid=3602), [Zalando](https://partner.zalando.com/university/pp/attributes-images-and-silhouettes), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
| 2026-03-15 | Initial schema — 33 attributes from 4 retailers plus Google Merchant Center apparel data specification | [Uniqlo](https://www.uniqlo.com/us/en/men/tops/t-shirts), [Brooks Brothers](https://www.brooksbrothers.com/mens/dress-shirts), [REI](https://www.rei.com/c/mens-clothing), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
