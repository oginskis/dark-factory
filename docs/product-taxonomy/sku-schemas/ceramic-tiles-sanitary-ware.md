# SKU Schema: Ceramic Tiles & Sanitary Ware

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.ceramic_tiles_sanitary`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | RAK-MP60120R, DAL-LV081224, SOM-GT3060-WT |
| Product Name | product_name | text | — | Full product name including key specs such as product type, look, and size | RAK Ceramics Marble Effect Polished 60x120cm, Daltile Linden Valley Wood-Look 8x24, Somany Wall Tile Glossy 30x60cm |
| URL | url | text | — | Direct link to the product page | https://example.com/product/marble-polished-60x120 |
| Price | price | number | — | Numeric price per square metre or per piece, excluding currency symbol | 8.50, 15.99, 32.00, 55.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, INR, SAR, AED |
| Product Category | product_category | enum | — | Whether the product is a tile or sanitary ware item | Floor Tile, Wall Tile, Decorative Tile, Mosaic, Trim/Bullnose, Toilet/WC, Wash Basin, Bidet, Urinal, Bathtub, Shower Tray, Pedestal |
| Tile Material | tile_material | enum | — | Primary material composition (tiles only) | Ceramic, Porcelain, Full-Body Porcelain, Glazed Porcelain, Vitrified, Glass Mosaic |
| Sanitary Ware Material | sanitary_ware_material | text | — | Body material for sanitary ware items | Vitreous China, Fine Fireclay, Glazed Stoneware, Solid Surface, Cast Mineral, Acrylic |
| Flush Type | flush_type | text | — | Flushing mechanism for toilets and WCs | Dual Flush, Rimless, Washdown, Siphonic, Tornado Flush |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | UAE, USA, Spain, Italy, India, Saudi Arabia, Germany, China, Turkey, Brazil |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Design Effect | design_effect | text | — | Visual aesthetic the tile is designed to replicate | Marble-Look, Wood-Look, Stone-Look, Concrete-Look, Fabric-Look, Metallic-Look, Terrazzo-Look, Solid Color |
| Tile Width | tile_width | number | mm | Face width of the tile | 50, 75, 100, 150, 200, 300, 450, 600, 750, 900, 1200 |
| Tile Thickness | tile_thickness | number | mm | Thickness of the tile body | 6, 7, 8, 9, 10, 11, 12, 14, 20 |
| Tile Shape | tile_shape | text | — | Geometric shape of the tile | Square, Rectangle/Plank, Hexagon, Arabesque, Chevron, Penny Round, Picket, Brick |
| Surface Finish | surface_finish | enum | — | Surface texture and sheen of the tile | Glossy, Matte, Satin, Polished, Honed, Lappato, Structured, Textured, Anti-Slip |
| Color | color | text | — | Primary color or color family | White, Ivory, Beige, Gray, Charcoal, Black, Brown, Blue, Green, Multi |
| Shade Variation | shade_variation | enum | — | Degree of visual variation between pieces per ANSI A137.1 | V0 Uniform, V1 Slight, V2 Moderate, V3 Substantial, V4 Random |
| Rectified | rectified | boolean | — | Whether tile edges are precision-ground to exact dimensions allowing minimal grout joints | true, false |
| PEI Rating | pei_rating | enum | — | Porcelain Enamel Institute wear rating for glazed tiles (0 to 5) | PEI 0, PEI 1, PEI 2, PEI 3, PEI 4, PEI 5 |
| Water Absorption | water_absorption | text | — | Water absorption classification per ISO 10545-3 / ASTM C373 | Less than 0.1%, Less than 0.5% (Impervious), 0.5-3% (Vitreous), 3-7% (Semi-Vitreous), Over 7% (Non-Vitreous) |
| DCOF (Wet) | dcof_wet | number | — | Wet Dynamic Coefficient of Friction per ANSI A326.3 (minimum 0.42 recommended for wet areas) | 0.42, 0.48, 0.55, 0.60, 0.70 |
| Breaking Strength | breaking_strength | number | N | Minimum breaking strength per ISO 10545-4 | 600, 1000, 1300, 2000 |
| Frost Resistant | frost_resistant | boolean | — | Whether the tile is rated frost-proof per ISO 10545-12 | true, false |
| Chemical Resistance | chemical_resistance | text | — | Chemical resistance classification per ISO 10545-13 | Class AA, Class A, Class B, Class C |
| Application Area | application_area | text (list) | — | Recommended installation locations | Floor, Wall, Countertop, Backsplash, Exterior, Pool, Shower, Wet Room, Facade |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus industry standards (ANSI A137.1, ISO 10545, ANSI A326.3) | [RAK Ceramics](https://onlineshop.rakceramics.com/), [Daltile](https://www.daltile.com/tile-product-category), [Somany Ceramics](https://www.somanyceramics.com/catalogues), [Standard Tile NJ](https://standardtilenj.com/blogs/blog/understanding-tile-ratings-pei-cof-and-more) |
