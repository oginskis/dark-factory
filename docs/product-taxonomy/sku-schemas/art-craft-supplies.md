# SKU Schema: Art & Craft Supplies

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.art_craft_supplies`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 00620-1019, LQ-1046151, WN-0114466 |
| Product Name | product_name | text | — | Full product name including brand, medium, color or variant, and size | Liquitex Heavy Body Acrylic Cadmium Yellow Medium 59mL, Winsor and Newton Professional Watercolour Burnt Sienna 5mL, Faber-Castell Polychromos Colored Pencil Set of 60 |
| URL | url | text | — | Direct link to the product page | https://example.com/product/heavy-body-acrylic-cadmium-yellow |
| Price | price | number | — | Numeric price per unit or set, excluding currency symbol | 3.49, 8.99, 74.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | product_category | enum | — | Primary product type | Acrylic Paint, Oil Paint, Watercolor, Colored Pencils, Pastels, Brushes, Canvas, Paper, Ink, Clay, Markers, Drawing Pencils |
| Grade | grade | enum | — | Quality tier indicating pigment load and binder quality | Student, Studio, Artist, Professional |
| Medium Type | medium_type | text | — | Specific medium or vehicle used in the product | Linseed Oil, Safflower Oil, Acrylic Polymer Emulsion, Gum Arabic, Wax |
| Brush Hair Type | brush_hair_type | text | — | Bristle material for brush products | Synthetic, Hog Bristle, Sable, Taklon, Squirrel |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, UK, France, Germany, Japan, Switzerland |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Product Line | product_line | text | — | Sub-brand or product series name | Heavy Body, Basics, Professional Watercolour, Polychromos, Artists Oil Colour |
| Color Name | color_name | text | — | Manufacturer-specified color name | Cadmium Yellow Medium, Burnt Sienna, Ultramarine Blue, Titanium White |
| Color Index Name | color_index_name | text | — | International Color Index designation identifying the pigment used | PY35, PBr7, PB29, PW6 |
| Pigment Number | pigment_number | text | — | Manufacturer pigment or color number | 161, 074, 263, 644 |
| Series Number | series_number | number | — | Price series number indicating pigment cost tier (higher = more expensive) | 1, 2, 3, 4, 5 |
| Lightfastness Rating | lightfastness_rating | text | — | Permanence rating per ASTM D4303 or manufacturer scale | ASTM I (Excellent), ASTM II (Very Good), ASTM III (Fair), Permanent, Moderately Durable |
| Opacity | opacity | enum | — | Transparency classification of the color | Transparent, Semi-Transparent, Semi-Opaque, Opaque |
| Viscosity | viscosity | enum | — | Flow consistency for paints | Heavy Body, Soft Body, Fluid, Ink, Super Heavy, Spray |
| Finish | finish | enum | — | Dried surface finish characteristic | Matte, Satin, Gloss, Semi-Gloss |
| Surface Compatibility | surface_compatibility | text (list) | — | Recommended surfaces for the product | Canvas, Paper, Wood, Metal, Fabric, Glass, Ceramic |
| Brush Shape | brush_shape | text | — | Shape of brush head for brush products | Round, Flat, Filbert, Fan, Liner, Bright, Mop |
| Paper Texture | paper_texture | enum | — | Surface texture for paper products | Hot Press (Smooth), Cold Press (Medium), Rough |
| Acid Free | acid_free | boolean | — | Whether the product is acid-free for archival quality | true, false |
| Non-Toxic | non-toxic | boolean | — | Whether the product carries an AP (Approved Product) non-toxic seal | true, false |
| Certifications | certifications | text (list) | — | Safety or quality certifications | ACMI AP Seal, ASTM D4236 Compliant, CE, FSC |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM D4303 lightfastness standard and Color Index International system | [Liquitex](https://www.liquitex.com/us/products/basics/range/colors/), [Blick Art Materials](https://www.dickblick.com/products/blick-artists-acrylic/), [Winsor and Newton](https://www.winsornewton.com/na/education/composition-permanence/terms-explained/), [United Art and Education](https://www.unitednow.com/art-catalog) |
