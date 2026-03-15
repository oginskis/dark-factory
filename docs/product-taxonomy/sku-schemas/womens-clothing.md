# SKU Schema: Women's Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | WD-BLK-M-001, 87654321, ASOS-29876 |
| Product Name | text | Full product name including brand, garment type, and key differentiators | Floral Wrap Midi Dress, High-Rise Skinny Jeans, Cashmere V-Neck Sweater |
| URL | text | Direct link to the product page | https://example.com/product/floral-wrap-midi-dress |
| Price | number | Numeric retail price per unit, excluding currency symbol | 19.99, 68.00, 245.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand | text | Name of the clothing brand or designer | Zara, ASOS, Free People, Anthropologie, Eileen Fisher, Lululemon |
| Garment Type | text | Type of clothing item | Dress, Blouse, Top, Skirt, Pants, Jeans, Jacket, Cardigan, Jumpsuit, Romper |
| Size | text | Garment size designation | XS, S, M, L, XL, 0, 2, 4, 6, 8, 10, 12, 14, 16 |
| Size Type | enum | Cut or fit category that modifies the base size | Regular, Petite, Plus, Tall, Maternity |
| Size System | text | Country or regional sizing standard used | US, EU, UK, FR, IT, AU, JP |
| Fit | enum | How the garment is cut relative to the body | Slim, Regular, Relaxed, Oversized, Bodycon, Fitted, Loose |
| Color | text | Primary color of the garment | Black, Ivory, Blush, Emerald, Cobalt, Burgundy, Mauve |
| Pattern | text | Visual pattern or print on the fabric | Solid, Floral, Striped, Polka Dot, Animal Print, Geometric, Abstract, Tie-Dye |
| Material | text | Primary fabric composition with percentages | 100% Silk, 95% Polyester 5% Elastane, 70% Viscose 30% Linen |
| Fabric Type | text | Named weave, knit, or textile construction | Chiffon, Satin, Crepe, Jersey, Lace, Denim, Tweed, Organza, Velvet |
| Fabric Weight | text | Weight classification or GSM of the fabric | Sheer, Lightweight, Midweight, Heavyweight, 120 GSM, 280 GSM |
| Neckline | text | Shape and style of the neckline or collar | V-Neck, Round, Square, Sweetheart, Off-Shoulder, Halter, Boat, Cowl, Keyhole |
| Sleeve Length | text | Length of the sleeve | Sleeveless, Cap, Short, Elbow, Three-Quarter, Long, Bell |
| Sleeve Style | text | Design or shape of the sleeve | Set-In, Raglan, Puff, Bishop, Dolman, Flutter, Lantern, Balloon |
| Hem Length | text | Where the garment falls on the body | Crop, Waist, Hip, Mini, Above-Knee, Knee, Midi, Tea, Maxi, Floor |
| Silhouette | text | Overall shape or outline of the garment | A-Line, Sheath, Shift, Empire, Fit-and-Flare, Wrap, Straight, Mermaid |
| Closure Type | text | Primary fastening mechanism of the garment | Zipper, Button, Hook and Eye, Snap, Pull-On, Wrap Tie, Drawstring |
| Lining | enum | Whether the garment includes a lining | Fully Lined, Partially Lined, Unlined |
| Waist Style | text | Position and style of the waistline | Natural, High-Rise, Mid-Rise, Low-Rise, Empire, Drop, Elastic |
| Occasion | text (list) | Intended wearing contexts for the garment | Casual, Work, Cocktail, Formal, Active, Vacation, Lounge, Bridal |
| Season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season, Resort |
| Care Instructions | text | Cleaning and maintenance directions | Machine wash cold, Dry clean only, Hand wash, Line dry, Iron low |
| Country of Origin | text | Country where the garment was manufactured | China, India, Turkey, Bangladesh, Vietnam, Romania, Italy |
| Sustainability Certification | text (list) | Environmental or ethical certifications | OEKO-TEX, GOTS, Fair Trade, BCI, Bluesign, GRS |
| UPC | text | Universal Product Code barcode number | 194501234567, 012345678905 |
| Features | text (list) | Functional design details and enhancements | Stretch, Wrinkle-resistant, Pockets, Built-in bra, Moisture-wicking, UV protection |
| Collection | text | Seasonal or thematic product line name | Spring 2026, Resort Collection, Essentials, Limited Edition |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 retailers plus Google Merchant Center apparel data specification | [Target](https://www.target.com/c/women/-/N-5xtd3), [ASOS](https://www.asos.com/women/), [Walmart](https://www.walmart.com/browse/womens-clothing/5438_133162), [Google Merchant Center](https://support.google.com/merchants/answer/7052112) |
