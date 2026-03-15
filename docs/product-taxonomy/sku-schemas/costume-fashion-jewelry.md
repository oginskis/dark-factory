# SKU Schema: Costume & Fashion Jewelry

**Last updated:** 2026-03-15
**Parent category:** Jewelry, Watches & Accessories
**Taxonomy ID:** `jewelry.costume_fashion`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | PAN-590702, KS-4217704879, SW-5649776 |
| Product Name | text | Full product name including style, material, and decorative details | Sparkling Pave Tennis Bracelet Silver, Elisa Gold Pendant Necklace in Ivory Mother-of-Pearl |
| URL | text | Direct link to the product page | https://example.com/product/pave-tennis-bracelet |
| Price | number | Numeric retail price excluding currency symbol | 29.99, 65.00, 195.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Jewelry Type | enum | Primary product category | Necklace, Bracelet, Earrings, Ring, Anklet, Brooch, Hair Accessory, Charm, Body Jewelry |
| Stone Type | text (list) | Decorative stones or crystals used | Cubic Zirconia, Swarovski Crystal, Glass, Resin, Acrylic, Rhinestone, Simulated Pearl |
| Material Description | text | Full material composition as stated by the seller | 925 Sterling Silver with 14K Gold Plating and Cubic Zirconia, Brass with Rhodium Plating |
| Closure Type | text | Type of fastening mechanism | Lobster Clasp, Toggle, Magnetic, Sliding Knot, Post with Butterfly Back, Hook, Barrel |
| Country of Origin | text | Country where the piece was manufactured | China, Thailand, India, Denmark, Italy |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Base Metal | text | Core metal or alloy before plating | Brass, Stainless Steel, Copper, Zinc Alloy, Sterling Silver, Mixed Metal Blend |
| Plating | text | Surface metal finish applied over the base metal | 14K Gold Plated, 18K Gold Plated, Rhodium Plated, Rose Gold Plated, Silver Plated, Ruthenium Plated |
| Stone Color | text | Primary color of decorative stones or crystals | Clear, Emerald Green, Sapphire Blue, Rose, Champagne, Aurora Borealis |
| Nickel Free | boolean | Whether the item is certified nickel-free or hypoallergenic | Yes, No |
| Color | text | Predominant visible color of the finished piece | Gold, Silver, Rose Gold, Multi-Color, Black, White, Turquoise |
| Collection | text | Named design collection or seasonal line | Pandora Timeless, Elisa, Constella, Millenia, Holiday 2026 |
| Style | text | Design style or aesthetic category | Minimalist, Statement, Bohemian, Vintage, Classic, Layering, Cocktail |
| Earring Style | text | Subtype of earring construction | Stud, Drop, Hoop, Huggie, Crawler, Chandelier, Clip-On, Threader |
| Pendant Dimensions | text (mm) | Height x width of pendant or charm | 12 x 10, 25 x 18, 15 x 15 |
| Adjustable | boolean | Whether the piece has an adjustable length or size | Yes, No |
| Number of Stones | number | Total count of decorative stones or crystals | 1, 12, 48, 96 |
| Pack Quantity | number | Number of pieces included if sold as a set | 1, 2, 3, 5 |
| Target Gender | enum | Intended wearer demographic | Women, Men, Unisex, Girls, Boys |
| Theme | text | Decorative motif or symbolic design element | Heart, Infinity, Cross, Butterfly, Star, Celestial, Floral, Evil Eye |
| Tarnish Resistant | boolean | Whether the finish is treated to resist tarnishing | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry material standards | [Pandora](https://us.pandora.net/en/jewelry/), [Kendra Scott](https://www.kendrascott.com/jewelry/), [Swarovski](https://www.swarovski.com/en-US/c-01/Categories/Jewelry/), [BaubleBar](https://www.baublebar.com/categories/jewelry) |
