# SKU Schema: Ceramic Tiles & Sanitary Ware

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | RAK-MP60120R, DAL-LV081224, SOM-GT3060-WT |
| Product Name | text | Full product name including key specs such as product type, look, and size | RAK Ceramics Marble Effect Polished 60x120cm, Daltile Linden Valley Wood-Look 8x24, Somany Wall Tile Glossy 30x60cm |
| URL | text | Direct link to the product page | https://example.com/product/marble-polished-60x120 |
| Price | number | Numeric price per square metre or per piece, excluding currency symbol | 8.50, 15.99, 32.00, 55.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, INR, SAR, AED |
| Brand | text | Manufacturer or brand name | RAK Ceramics, Daltile, Somany, Saudi Ceramics, Porcelanosa, Marazzi, Villeroy and Boch, Roca, TOTO, Duravit, Kohler |
| Product Category | enum | Whether the product is a tile or sanitary ware item | Floor Tile, Wall Tile, Decorative Tile, Mosaic, Trim/Bullnose, Toilet/WC, Wash Basin, Bidet, Urinal, Bathtub, Shower Tray, Pedestal |
| Tile Material | enum | Primary material composition (tiles only) | Ceramic, Porcelain, Full-Body Porcelain, Glazed Porcelain, Vitrified, Glass Mosaic |
| Design Effect | text | Visual aesthetic the tile is designed to replicate | Marble-Look, Wood-Look, Stone-Look, Concrete-Look, Fabric-Look, Metallic-Look, Terrazzo-Look, Solid Color |
| Tile Width | number (mm) | Face width of the tile | 50, 75, 100, 150, 200, 300, 450, 600, 750, 900, 1200 |
| Tile Length | number (mm) | Face length of the tile | 50, 100, 200, 300, 450, 600, 750, 900, 1200, 1500, 1800, 2400 |
| Tile Thickness | number (mm) | Thickness of the tile body | 6, 7, 8, 9, 10, 11, 12, 14, 20 |
| Tile Shape | text | Geometric shape of the tile | Square, Rectangle/Plank, Hexagon, Arabesque, Chevron, Penny Round, Picket, Brick |
| Surface Finish | enum | Surface texture and sheen of the tile | Glossy, Matte, Satin, Polished, Honed, Lappato, Structured, Textured, Anti-Slip |
| Color | text | Primary color or color family | White, Ivory, Beige, Gray, Charcoal, Black, Brown, Blue, Green, Multi |
| Shade Variation | enum | Degree of visual variation between pieces per ANSI A137.1 | V0 Uniform, V1 Slight, V2 Moderate, V3 Substantial, V4 Random |
| Rectified | boolean | Whether tile edges are precision-ground to exact dimensions allowing minimal grout joints | true, false |
| PEI Rating | enum | Porcelain Enamel Institute wear rating for glazed tiles (0 to 5) | PEI 0, PEI 1, PEI 2, PEI 3, PEI 4, PEI 5 |
| Water Absorption | text | Water absorption classification per ISO 10545-3 / ASTM C373 | Less than 0.1%, Less than 0.5% (Impervious), 0.5-3% (Vitreous), 3-7% (Semi-Vitreous), Over 7% (Non-Vitreous) |
| DCOF (Wet) | number | Wet Dynamic Coefficient of Friction per ANSI A326.3 (minimum 0.42 recommended for wet areas) | 0.42, 0.48, 0.55, 0.60, 0.70 |
| Breaking Strength | number (N) | Minimum breaking strength per ISO 10545-4 | 600, 1000, 1300, 2000 |
| Frost Resistant | boolean | Whether the tile is rated frost-proof per ISO 10545-12 | true, false |
| Chemical Resistance | text | Chemical resistance classification per ISO 10545-13 | Class AA, Class A, Class B, Class C |
| Application Area | text (list) | Recommended installation locations | Floor, Wall, Countertop, Backsplash, Exterior, Pool, Shower, Wet Room, Facade |
| Sanitary Ware Material | text | Body material for sanitary ware items | Vitreous China, Fine Fireclay, Glazed Stoneware, Solid Surface, Cast Mineral, Acrylic |
| Flush Type | text | Flushing mechanism for toilets and WCs | Dual Flush, Rimless, Washdown, Siphonic, Tornado Flush |
| Mounting Style | text | Installation method for sanitary ware | Wall-Hung, Floor-Standing, Back-to-Wall, Countertop, Semi-Recessed, Inset, Freestanding |
| Sanitary Ware Dimensions | text (mm) | Overall dimensions (LxWxH) of the sanitary ware piece | 550x365x400, 600x450x200, 700x420x380, 1700x700x420 |
| Pieces per Box | number | Number of tiles per carton | 3, 4, 5, 6, 8, 10, 11, 17, 25 |
| Coverage per Box | number (m2) | Area covered per carton of tiles | 0.72, 1.08, 1.44, 1.80, 2.16, 3.24 |
| Weight per Box | number (kg) | Shipping weight per carton of tiles | 12, 18, 22, 26, 32, 38 |
| Certification | text (list) | Product and sustainability certifications | CE, ISO 13006, LEED, GREENGUARD, Porcelain Tile Certification Agency (PTCA), Green Label Plus |
| Country of Origin | text | Country where the product was manufactured | UAE, USA, Spain, Italy, India, Saudi Arabia, Germany, China, Turkey, Brazil |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus industry standards (ANSI A137.1, ISO 10545, ANSI A326.3) | [RAK Ceramics](https://onlineshop.rakceramics.com/), [Daltile](https://www.daltile.com/tile-product-category), [Somany Ceramics](https://www.somanyceramics.com/catalogues), [Standard Tile NJ](https://standardtilenj.com/blogs/blog/understanding-tile-ratings-pei-cof-and-more) |
