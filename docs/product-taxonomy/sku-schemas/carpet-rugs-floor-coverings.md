# SKU Schema: Carpet, Rugs & Floor Coverings

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.carpet_rugs_floor_coverings`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | CT-1234, BL-5678, RG-90120 |
| Product Name | product_name | text | — | yes | Full product name including collection, pattern, and color | Visual Edge Angled Perception Dark Charcoal, Striation Tile Denim Blue |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/visual-edge-dark-charcoal |
| Price | price | number | — | yes | Numeric price per unit (per square yard, square foot, tile, or each for rugs), excluding currency symbol | 2.50, 18.99, 42.00, 350.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Form | product_form | enum | — | — | Physical format of the floor covering | Carpet Tile, Broadloom, Area Rug, Runner, Carpet Roll, Cushion-Back Tile |
| Construction Type | construction_type | enum | — | — | Method of manufacture | Tufted, Woven, Knitted, Needlepunched, Fusion Bonded, Hand Knotted, Hand Tufted, Flatweave |
| Pile Type | pile_type | enum | — | — | Style of the carpet pile surface | Level Loop, Cut Pile, Cut and Loop, Textured, Plush, Frieze, Shag, Berber, Patterned Loop |
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | USA, UK, Netherlands, Australia, Belgium |
| Face Weight | face_weight | number | oz/yd2 | — | Weight of pile yarns per square yard, excluding backing | 14, 18, 22, 28, 36, 48 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Pile Fiber | pile_fiber | text | — | — | Fiber material used in the pile surface | Nylon 6, Nylon 6,6, Solution-Dyed Nylon, PET Polyester, PTT Polyester, Wool, Polypropylene |
| Fiber Brand | fiber_brand | text | — | — | Branded or proprietary fiber name if applicable | Antron, Colorstrand SD, Econyl, StainMaster, Sorona |
| Dye Method | dye_method | enum | — | — | How the color is applied to the fiber or yarn | Solution Dyed, Yarn Dyed, Piece Dyed, Space Dyed, Printed, Injection Dyed |
| Pile Height | pile_height | number | mm | — | Distance from the backing surface to the tip of the pile tufts | 2.5, 3.5, 5.0, 6.0, 8.0, 12.0 |
| Total Thickness | total_thickness | number | mm | — | Overall product thickness including backing | 6.0, 8.0, 9.0, 10.5, 12.0 |
| Gauge | gauge | text | — | — | Spacing of tufting needles, expressed as a fraction of an inch | 1/8, 5/64, 1/10, 1/12, 1/13 |
| Stitch Rate | stitch_rate | number | — | — | Number of pile tufts per running inch in the machine direction | 8.0, 9.5, 10.2, 12.5 |
| Tuft Density | tuft_density | number | tufts/m2 | — | Number of tufts per square metre | 62000, 130000, 180000, 260700 |
| Roll Width | roll_width | number | ft | — | Width for broadloom and rolled carpet | 6, 12, 13.5, 15 |
| Primary Backing | primary_backing | text | — | — | Material used for the primary backing layer | Woven Polypropylene, Nonwoven Polyester, ActionBac |
| Secondary Backing | secondary_backing | text | — | — | Material used for the secondary backing or cushion layer | PVC, Polyurethane, Bitumen, EcoFlex Matrix, StableShield, WellBAC |
| Pattern | pattern | text | — | — | Visual design or pattern name | Solid, Linear, Geometric, Abstract, Random, Plaid |
| Color | color | text | — | — | Primary color name or number | Dark Charcoal, Denim Blue, Sandstone, Crimson, Bone 103 |
| Colors Available | colors_available | number | — | — | Number of colorways offered for this pattern or style | 6, 12, 18, 24 |
| Flammability Rating | flammability_rating | text | — | — | Fire performance classification | CRI FF1-70 / CPSC FF1-70, ASTM E648 Class I, EN 13501-1 Bfl-s1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus CRI and ASTM carpet standards | [Interface](https://www.interface.com/US/en-US.html), [Mohawk Group](https://www.mohawkgroup.com/), [Milliken](https://www.milliken.com/en-us/businesses/floor-covering), [Carpet & Rug Institute Specification](https://carpet-rug.org/wp-content/uploads/2019/03/Model-Specification-for-Commercial-Carpet-2018.pdf) |
