# SKU Schema: Table Linens & Accessories

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier for the table linen item | TL-90132-WHT, 160NP2020BK, SP-120R-IVY |
| Product Name | text | Full product name typically including color, size, shape, and fabric line | White 90x132 Rectangular Spun Polyester Tablecloth, Black 20x20 Hemmed Cloth Napkin, Ivory Jacquard Table Runner 14x72 |
| URL | text | Direct link to the product page or listing | https://example.com/product/tablecloth-90x132-white |
| Price | number | Numeric price per selling unit, excluding currency symbol | 5.46, 18.14, 43.39, 213.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Brand or manufacturer name | Milliken, Riegel, Snap Drape, Intedge, Monarch Brands |
| Product Type | enum | Type of table linen product | Tablecloth, Napkin, Table Runner, Placemat, Table Overlay, Table Skirt, Chair Cover, Chair Sash, Table Topper, Bistro Napkin, Cocktail Napkin |
| Material Composition | text | Fiber content with percentages | 100% Polyester, 100% Cotton, 100% Linen, 55% Cotton / 45% Polyester, Cotton-Linen Blend |
| Fabric Type | text | Specific fabric line or construction category describing the textile | Spun Polyester, Poly Premier, Signature Plus, Visa Plus, Damask, Momie Weave, Jacquard, Satin Band, Spandex |
| GSM | number (g/m2) | Fabric weight in grams per square metre, indicator of thickness and quality | 150, 180, 200, 250 |
| Length | number (cm) | Product length or longer dimension | 51, 132, 203, 335, 396 |
| Width | number (cm) | Product width or shorter dimension | 51, 132, 152, 228 |
| Diameter | number (cm) | Diameter for round tablecloths and overlays | 132, 152, 228, 274, 305, 335 |
| Shape | enum | Shape of the table linen product | Round, Square, Rectangular, Oval, Fitted, Serpentine |
| Color | text | Product color name | White, Ivory, Black, Navy, Burgundy, Gold, Mauve, Aqua, Charcoal, Forest Green |
| Color Family | enum | Broad color grouping used for filtering and categorization | White, Black, Blue, Red, Green, Yellow, Brown, Pink, Purple, Orange, Grey, Neutral |
| Pattern | enum | Visual design pattern of the fabric | Solid, Checkered, Striped, Jacquard, Damask, Floral, Geometric, Gingham |
| Design Style | text | Aesthetic style classification for decorative linens | Classic, Minimalist, Bohemian, Floral and Nature, Landscape, Christmas, Seasonal |
| Weave Type | enum | Method used to interlace yarns that determines texture and drape | Plain, Twill, Satin, Jacquard, Momie, Dobby, Birds Eye |
| Hem Type | text | Edge finishing method that affects durability and appearance | Hemmed, Baby Hem, Mitered Corner, Serged, Rolled Hem, Merrow Edge, Unhemmed |
| Coating/Treatment | text | Surface treatment or finish applied to the fabric for performance | Stain Resistant, Soil Release, Wrinkle Resistant, Waterproof Coating, Flame Retardant, ColorSeal |
| Stain Resistance | enum | Qualitative rating of how well the fabric resists staining | Low, Moderate, High, Premium |
| Wrinkle Resistance | enum | Qualitative rating of how well the fabric resists wrinkling | Low, Moderate, High, Premium |
| Drop Length | number (cm) | Overhang distance from the table edge to the bottom of the tablecloth | 15, 20, 25, 38, 74 |
| Table Size Fit | text | Recommended table dimensions or guest capacity the linen is designed for | 60 inch round, 6ft banquet, 2/4 guests, 8/10 guests |
| Umbrella Hole | boolean | Whether the tablecloth has a built-in umbrella hole for outdoor patio tables | true, false |
| Care Instructions | text | Recommended washing and drying guidelines | Machine wash warm, tumble dry low, iron on low heat, do not bleach |
| Maximum Wash Temperature | number (C) | Maximum recommended water temperature for laundering | 40, 50, 60 |
| Flame Retardant | boolean | Whether the product meets flame resistance standards for commercial use | true, false |
| Certification | text (list) | Quality, safety, or sustainability certifications held by the product | OEKO-TEX Standard 100, GOTS, ISO 9001 |
| Country of Origin | text | Country where the product was manufactured | USA, China, India, Turkey, France, Pakistan |
| Pack Quantity | number | Number of pieces per selling unit | 1, 6, 12, 50, 300 |
| Selling Unit | enum | How the product is sold and priced | Piece, Pack, Dozen, Case, Set |
| Minimum Order Quantity | number | Minimum number of units required per order for wholesale purchases | 1, 12, 50, 300 |
| Custom Size Available | boolean | Whether the product can be ordered in non-standard custom dimensions | true, false |
| Intended Use | text | Primary application or setting the product is designed for | Restaurant, Hotel, Banquet, Wedding, Catering, Residential, Outdoor Patio |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 5 companies covering B2B wholesale, commercial restaurant supply, premium retail, and hospitality segments | [Premier Table Linens](https://premiertablelinens.com/), [Restaurant Table Linens / Milliken](https://www.restauranttablelinens.com/napkins-tablecloths), [WebstaurantStore](https://www.webstaurantstore.com/3929/linens-table-covers.html), [CV Linens](https://www.cvlinens.com/), [Le Jacquard Francais](https://www.le-jacquard-francais.com/table-linen/) |
