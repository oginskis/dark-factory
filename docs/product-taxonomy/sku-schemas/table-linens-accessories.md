# SKU Schema: Table Linens & Accessories

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.table_linens_accessories`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier for the table linen item | TL-90132-WHT, 160NP2020BK, SP-120R-IVY |
| Product Name | product_name | text | — | Full product name typically including color, size, shape, and fabric line | White 90x132 Rectangular Spun Polyester Tablecloth, Black 20x20 Hemmed Cloth Napkin, Ivory Jacquard Table Runner 14x72 |
| URL | url | text | — | Direct link to the product page or listing | https://example.com/product/tablecloth-90x132-white |
| Price | price | number | — | Numeric price per selling unit, excluding currency symbol | 5.46, 18.14, 43.39, 213.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Type of table linen product | Tablecloth, Napkin, Table Runner, Placemat, Table Overlay, Table Skirt, Chair Cover, Chair Sash, Table Topper, Bistro Napkin, Cocktail Napkin |
| Material Composition | material_composition | text | — | Fiber content with percentages | 100% Polyester, 100% Cotton, 100% Linen, 55% Cotton / 45% Polyester, Cotton-Linen Blend |
| Fabric Type | fabric_type | text | — | Specific fabric line or construction category describing the textile | Spun Polyester, Poly Premier, Signature Plus, Visa Plus, Damask, Momie Weave, Jacquard, Satin Band, Spandex |
| Weave Type | weave_type | enum | — | Method used to interlace yarns that determines texture and drape | Plain, Twill, Satin, Jacquard, Momie, Dobby, Birds Eye |
| Hem Type | hem_type | text | — | Edge finishing method that affects durability and appearance | Hemmed, Baby Hem, Mitered Corner, Serged, Rolled Hem, Merrow Edge, Unhemmed |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, China, India, Turkey, France, Pakistan |
| GSM | gsm | number | g/m2 | Fabric weight in grams per square metre, indicator of thickness and quality | 150, 180, 200, 250 |
| Width | width | number | cm | Product width or shorter dimension | 51, 132, 152, 228 |
| Shape | shape | enum | — | Shape of the table linen product | Round, Square, Rectangular, Oval, Fitted, Serpentine |
| Color | color | text | — | Product color name | White, Ivory, Black, Navy, Burgundy, Gold, Mauve, Aqua, Charcoal, Forest Green |
| Color Family | color_family | enum | — | Broad color grouping used for filtering and categorization | White, Black, Blue, Red, Green, Yellow, Brown, Pink, Purple, Orange, Grey, Neutral |
| Pattern | pattern | enum | — | Visual design pattern of the fabric | Solid, Checkered, Striped, Jacquard, Damask, Floral, Geometric, Gingham |
| Design Style | design_style | text | — | Aesthetic style classification for decorative linens | Classic, Minimalist, Bohemian, Floral and Nature, Landscape, Christmas, Seasonal |
| Coating/Treatment | coatingtreatment | text | — | Surface treatment or finish applied to the fabric for performance | Stain Resistant, Soil Release, Wrinkle Resistant, Waterproof Coating, Flame Retardant, ColorSeal |
| Stain Resistance | stain_resistance | enum | — | Qualitative rating of how well the fabric resists staining | Low, Moderate, High, Premium |
| Wrinkle Resistance | wrinkle_resistance | enum | — | Qualitative rating of how well the fabric resists wrinkling | Low, Moderate, High, Premium |
| Umbrella Hole | umbrella_hole | boolean | — | Whether the tablecloth has a built-in umbrella hole for outdoor patio tables | true, false |
| Care Instructions | care_instructions | text | — | Recommended washing and drying guidelines | Machine wash warm, tumble dry low, iron on low heat, do not bleach |
| Maximum Wash Temperature | maximum_wash_temperature | number | C | Maximum recommended water temperature for laundering | 40, 50, 60 |
| Flame Retardant | flame_retardant | boolean | — | Whether the product meets flame resistance standards for commercial use | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 5 companies covering B2B wholesale, commercial restaurant supply, premium retail, and hospitality segments | [Premier Table Linens](https://premiertablelinens.com/), [Restaurant Table Linens / Milliken](https://www.restauranttablelinens.com/napkins-tablecloths), [WebstaurantStore](https://www.webstaurantstore.com/3929/linens-table-covers.html), [CV Linens](https://www.cvlinens.com/), [Le Jacquard Francais](https://www.le-jacquard-francais.com/table-linen/) |
