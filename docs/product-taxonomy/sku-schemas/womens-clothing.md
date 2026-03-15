# SKU Schema: Women's Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier, may include article number or reference code | WD-BLK-M-001, 77020365, E479071-000, 1310170003 |
| Product Name | text | Full product name including brand, garment type, and key differentiators | Floral Wrap Midi Dress, Rayon Blouse, Long Printed Dress, Printed Shirt Dress |
| URL | text | Direct link to the product page | https://example.com/product/floral-wrap-midi-dress |
| Price | number | Numeric retail price per unit, excluding currency symbol | 19.99, 49.99, 245.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Sale Price | number | Discounted or promotional price when the item is on sale, excluding currency symbol | 14.99, 39.99, 69.99 |
| Brand | text | Name of the clothing brand or designer | Zara, Mango, Uniqlo, H&M, Free People, Anthropologie |
| Gender | enum | Target gender for the garment | Women, Unisex |
| Garment Type | text | Type of clothing item | Dress, Blouse, Top, Skirt, Pants, Jeans, Jacket, Cardigan, Jumpsuit, Romper |
| Size | text | Garment size designation using letters, numbers, or both | XS, S, M, L, XL, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 |
| Size Type | enum | Cut or fit category that modifies the base size | Regular, Petite, Plus, Tall, Maternity |
| Size System | text | Country or regional sizing standard used | US, EU, UK, FR, IT, AU, JP |
| Fit | enum | How the garment is cut relative to the body | Slim, Regular, Relaxed, Oversized, Bodycon, Fitted, Loose, Straight |
| Color | text | Primary color of the garment | Black, Ivory, Blush, Emerald, Cobalt, Burgundy, Maroon, Purple |
| Pattern | text | Visual pattern or print on the fabric | Solid, Floral, Striped, Polka Dot, Animal Print, Geometric, Abstract, Printed |
| Material | text | Primary fabric composition with fiber percentages | 100% Silk, 76% Rayon 24% Polyester, 100% Polyester, 95% Cotton 5% Elastane |
| Fabric Type | text | Named weave, knit, or textile construction | Chiffon, Satin, Crepe, Jersey, Lace, Denim, Tweed, Organza, Velvet, Fluid |
| Fabric Weight | text | Weight classification or GSM of the fabric | Sheer, Lightweight, Midweight, Heavyweight, 120 GSM, 280 GSM |
| Fabric Technology | text | Proprietary or branded fabric technology or performance finish | HEATTECH, AIRism, DRY-EX, CoolMax, Thermalite, UV Cut |
| Neckline | text | Shape and style of the neckline or collar | V-Neck, Round, Square, Sweetheart, Off-Shoulder, Halter, Boat, Cowl, Shirt Collar |
| Sleeve Length | text | Length of the sleeve | Sleeveless, Cap, Short, Elbow, Three-Quarter, Long, Bell |
| Sleeve Style | text | Design or shape of the sleeve | Set-In, Raglan, Puff, Bishop, Dolman, Flutter, Lantern, Balloon |
| Hem Length | text | Where the garment falls on the body | Crop, Waist, Hip, Mini, Above-Knee, Knee, Midi, Tea, Maxi, Floor |
| Silhouette | text | Overall shape or outline of the garment | A-Line, Sheath, Shift, Empire, Fit-and-Flare, Wrap, Straight, Mermaid |
| Closure Type | text | Primary fastening mechanism of the garment | Zipper, Button, Hook and Eye, Snap, Pull-On, Wrap Tie, Drawstring, No Closure |
| Lining | enum | Whether the garment includes a lining | Fully Lined, Partially Lined, Unlined |
| Waist Style | text | Position and style of the waistline | Natural, High-Rise, Mid-Rise, Low-Rise, Empire, Drop, Elastic |
| Occasion | text (list) | Intended wearing contexts for the garment | Casual, Work, Cocktail, Formal, Active, Vacation, Lounge, Bridal |
| Season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season, Resort |
| Care Instructions | text | Cleaning and maintenance directions | Machine wash cold, Dry clean only, Hand wash, Do not tumble dry, Iron low |
| Country of Origin | text | Country where the garment was manufactured | China, India, Turkey, Bangladesh, Vietnam, Cambodia, Morocco, Italy |
| Sustainability Certification | text (list) | Environmental or ethical certifications held by the product | OEKO-TEX, GOTS, Fair Trade, BCI, Bluesign, GRS |
| UPC | text | Universal Product Code barcode number | 194501234567, 012345678905 |
| Features | text (list) | Functional design details and enhancements | Stretch, Wrinkle-resistant, Pockets, Built-in bra, Moisture-wicking, UV protection, Recycled materials |
| Collection | text | Seasonal or thematic product line name | Spring 2026, Resort Collection, Essentials, Limited Edition |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Added: Sale Price, Gender, Fabric Technology. Updated descriptions and example values for SKU, Product Name, Size, Fit, Color, Pattern, Material, Fabric Type, Neckline, Closure Type, Care Instructions, Country of Origin, Features to incorporate findings from 3 new retailers. Deprecated: none. | [Uniqlo](https://www.uniqlo.com/us/en/products/E479071-000/00), [Mango](https://shop.mango.com/us/en/p/women/dresses-and-jumpsuits/dresses/long-printed-dress_77020365), [Zara](https://www.zara.com/us/en/woman-dresses-l1066.html) |
| 2026-03-15 | Initial schema — 32 attributes from 4 retailers plus Google Merchant Center apparel data specification | [Target](https://www.target.com/c/women/-/N-5xtd3), [ASOS](https://www.asos.com/women/), [Walmart](https://www.walmart.com/browse/womens-clothing/5438_133162), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
