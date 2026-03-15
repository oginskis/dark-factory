# SKU Schema: Men's Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | E422992-000, 1016781, MCS-SLM-BLU-L |
| Product Name | text | Full product name including brand, garment type, and key differentiators | Slim Fit Oxford Button-Down Shirt, AIRism Cotton Crew Neck T-Shirt, Stretch Chino Pants |
| URL | text | Direct link to the product page | https://example.com/product/slim-fit-oxford-shirt |
| Price | number | Numeric retail price per unit, excluding currency symbol | 14.90, 49.99, 198.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand | text | Name of the clothing brand or designer | Uniqlo, Brooks Brothers, Levi's, Ralph Lauren, H&M |
| Garment Type | text | Type of clothing item | T-Shirt, Dress Shirt, Polo, Jacket, Pants, Shorts, Sweater, Coat, Suit |
| Size | text | Garment size designation | XS, S, M, L, XL, XXL, 15/32, 32x30, 38R |
| Size System | text | Country or regional sizing standard used | US, EU, UK, JP, AU |
| Fit | enum | How the garment is cut relative to the body | Slim, Regular, Classic, Relaxed, Oversized, Athletic, Tailored |
| Color | text | Primary color of the garment | Black, Navy, White, Charcoal, Olive, Burgundy |
| Pattern | text | Visual pattern or print on the fabric | Solid, Striped, Plaid, Checkered, Herringbone, Paisley, Floral, Camo |
| Material | text | Primary fabric composition with percentages | 100% Cotton, 98% Cotton 2% Spandex, 60% Cotton 40% Polyester |
| Fabric Type | text | Named weave or knit construction of the fabric | Oxford, Broadcloth, Twill, Jersey, Flannel, Denim, Fleece, Poplin, Chambray |
| Fabric Weight | text | Weight classification or GSM of the fabric | Lightweight, Midweight, Heavyweight, 150 GSM, 280 GSM |
| Collar Type | text | Style of collar on shirts and jackets | Button-Down, Spread, Point, Band, Mandarin, Notch Lapel, Shawl |
| Sleeve Length | text | Length of the sleeve | Short, Long, Three-Quarter, Sleeveless, Roll-Up |
| Cuff Type | text | Style of the sleeve cuff on dress shirts | Barrel, French, Mitered, Button, Elastic |
| Neckline | text | Style of the neckline on knit tops | Crew Neck, V-Neck, Henley, Mock Neck, Turtleneck, Scoop |
| Closure Type | text | Primary fastening mechanism of the garment | Button, Zipper, Snap, Pull-On, Drawstring, Hook and Eye |
| Inseam | number (inches) | Interior leg length from crotch to hem on pants | 28, 30, 32, 34, 36 |
| Waist Size | number (inches) | Waist measurement on pants and shorts | 28, 30, 32, 34, 36, 38, 40 |
| Neck Size | number (inches) | Collar circumference on dress shirts | 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5 |
| Chest Size | number (inches) | Chest circumference for jackets and suits | 36, 38, 40, 42, 44, 46, 48 |
| Rise | enum | Vertical distance from crotch seam to waistband on pants | Low, Mid, High |
| Occasion | text (list) | Intended wearing contexts for the garment | Casual, Business, Formal, Active, Outdoor, Lounge |
| Season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season |
| Care Instructions | text | Cleaning and maintenance directions | Machine wash cold, Tumble dry low, Dry clean only, Hand wash |
| Country of Origin | text | Country where the garment was manufactured | China, Vietnam, Bangladesh, India, Turkey, Portugal, Italy |
| Sustainability Certification | text (list) | Environmental or ethical certifications | OEKO-TEX, GOTS, Fair Trade, BCI, Bluesign, GRS |
| UPC | text | Universal Product Code barcode number | 194501234567, 012345678905 |
| Product Technology | text (list) | Proprietary or named fabric technologies | AIRism, DRY-EX, HEATTECH, Dri-FIT, COOLMAX, Gore-Tex |
| Features | text (list) | Functional design details and enhancements | Moisture-wicking, Stretch, Wrinkle-resistant, UV protection, Odor control, Water-repellent |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 retailers plus Google Merchant Center apparel data specification | [Uniqlo](https://www.uniqlo.com/us/en/men/tops/t-shirts), [Brooks Brothers](https://www.brooksbrothers.com/mens/dress-shirts), [REI](https://www.rei.com/c/mens-clothing), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
