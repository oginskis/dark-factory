# SKU Schema: Household Linens & Towels

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HT-2750-WHT, 4532100, BLS-BT-27X54 |
| Product Name | text | Full product name including key specs such as product type, material, and dimensions | 100% Cotton Ring-Spun Bath Towel 27x54 White 14 lb/dz, T-300 Percale Queen Flat Sheet |
| URL | text | Direct link to the product page | https://example.com/product/bath-towel-27x54 |
| Price | number | Numeric price per selling unit (piece, dozen, case), excluding currency symbol | 3.49, 42.99, 189.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Brand or manufacturer name | American Soft Linen, 1888 Mills, Standard Textile, Welspun |
| Product Type | enum | Type of household linen product | Bath Towel, Hand Towel, Washcloth, Bath Sheet, Bath Mat, Flat Sheet, Fitted Sheet, Pillowcase, Duvet Cover, Table Napkin, Tablecloth, Kitchen Towel, Beach Towel |
| Material Composition | text | Fiber content with percentages | 100% Cotton, 86% Cotton / 14% Polyester, 100% Linen, 60% Cotton / 40% Polyester |
| Cotton Type | text | Specific cotton variety or yarn construction when applicable | Ring-Spun, Combed, Egyptian, Pima, Supima, Turkish, Open-End |
| GSM | number (g/m2) | Fabric weight in grams per square metre, primary indicator of thickness and quality for towels | 400, 550, 700 |
| Weight per Dozen | number (lbs) | Total weight of twelve units in pounds, used in commercial and hospitality purchasing | 8.0, 14.0, 18.0 |
| Thread Count | number | Number of horizontal and vertical threads per square inch, primary quality indicator for sheets | 200, 300, 400, 600, 800 |
| Width | number (cm) | Product width or shorter dimension | 33, 41, 69, 152 |
| Length | number (cm) | Product length or longer dimension | 33, 69, 137, 259 |
| Weave Type | enum | Method used to interlace yarns that determines texture and performance | Terry, Percale, Sateen, Jacquard, Dobby, Waffle, Twill, Plain |
| Border Type | text | Decorative or structural border style on towels and linens | Dobby Border, Cam Border, Hemmed, Piano Key, Stripe, No Border |
| Pile Type | enum | Loop construction of terry fabric | Single Loop, Double Loop, Zero Twist, Low Twist |
| Color | text | Product color or pattern name | White, Ivory, Navy, Sage Green, Charcoal Grey, Striped |
| Hem Type | text | Edge finishing method | Double-Stitched Hem, Single Fold, Mitered Corner, Overlock |
| Bed Size | enum | Standard bed size for fitted sheets, flat sheets, and duvet covers | Twin, Full, Queen, King, California King |
| Pocket Depth | number (cm) | Depth of the fitted sheet pocket for mattress fit | 25, 30, 38, 46 |
| Shrinkage | text (%) | Expected dimensional change after laundering | Less than 3%, Less than 5% |
| Absorbency Rating | text | Qualitative absorbency classification for towels | Standard, High, Premium |
| Quick Dry | boolean | Whether the product is engineered for accelerated drying | true, false |
| Anti-Microbial Treatment | boolean | Whether an antimicrobial finish has been applied | true, false |
| Colorfastness | text | Resistance to color loss during washing, rated on a grey scale or qualitative descriptor | Grade 4-5, Excellent, Good |
| Certification | text (list) | Quality, safety, or sustainability certifications | OEKO-TEX Standard 100, GOTS, USDA Organic, ISO 9001, Fair Trade |
| Pack Quantity | number | Number of pieces per selling unit (pack, case, or dozen) | 1, 6, 12, 24, 60 |
| Selling Unit | enum | How the product is sold | Piece, Dozen, Case, Pack |
| Country of Origin | text | Country where the product was manufactured | India, Pakistan, Turkey, China, Portugal, USA |
| Laundering Cycles | text | Expected durability measured in number of industrial wash cycles | 200+, 300+, 500+ |
| Care Instructions | text | Recommended washing and drying guidelines | Machine wash warm, tumble dry medium, no bleach |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (GSM measurement, thread count standards, OEKO-TEX) | [American Soft Linen](https://americansoftlinen.com/collections/wholesale), [Bulk Linen Supply](https://bulklinensupply.com/), [Direct Textile Store](https://directtextilestore.com/standard-towels), [Towel Super Center](https://www.towelsupercenter.com/hotel-towels/) |
