# SKU Schema: Home Decor (Curtains, Cushions, Wall Art)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.home_decor`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | WC-8432-NVY, DD-CUR-120, ART-CVS-3624 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, material, and dimensions | Eclipse Blackout Curtain Panel 52x84 in Navy, Sunbrella Outdoor Throw Pillow 20x20 in Natural, Abstract Canvas Wall Art Set of 3 24x36 in |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/blackout-curtain-navy |
| Price | price | number | — | yes | Numeric price per unit or per set excluding currency symbol | 14.99, 39.00, 89.95, 245.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Specific type of home decor product | Curtain Panel, Curtain Pair, Valance, Throw Pillow, Pillow Cover, Floor Cushion, Canvas Print, Framed Print, Metal Wall Art, Tapestry, Wall Mirror, Decorative Object, Throw Blanket |
| Fabric/Material | fabricmaterial | text | — | — | Primary material of the product | Polyester, Cotton, Linen, Velvet, Faux Silk, Canvas, Jute, Burlap, Metal, Wood, Glass |
| Fill Material | fill_material | text | — | — | Stuffing or insert material for cushions and pillows | Polyester Fiberfill, Down Alternative, Feather/Down Blend, Foam, Kapok |
| Header/Hanging Type | headerhanging_type | text | — | — | How the curtain attaches to the rod or the art hangs on the wall | Rod Pocket, Grommet (Eyelet), Pinch Pleat, Tab Top, Back Tab, Ring Top, D-Ring Hanger, Sawtooth Hanger, Wire System |
| Frame Material | frame_material | text | — | — | Material of the frame for framed prints or mirrors | Wood, Metal (Aluminum), PS (Polystyrene), Floater Frame, Unframed (Gallery Wrap) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | China, India, Turkey, Portugal, USA, Belgium |
| Panel Width | panel_width | number | mm | — | Width of a single curtain panel or art piece | 520, 1050, 1320 |
| Art Width | art_width | number | mm | — | Width of wall art, mirror, or decorative piece | 300, 450, 600, 900, 1200 |
| Art Height | art_height | number | mm | — | Height of wall art, mirror, or decorative piece | 300, 450, 600, 900 |
| Art Depth | art_depth | number | mm | — | Depth or profile thickness of wall art including frame or stretcher bars | 15, 20, 38, 50 |
| Cushion Dimensions | cushion_dimensions | text | mm | — | Width x height or diameter of cushion or pillow | 450 x 450, 500 x 500, 300 x 500, 600 Diameter |
| Color | color | text | — | — | Primary color or color family | Navy, Ivory, Charcoal, Blush Pink, Sage Green, Rust, Gold, Multicolor |
| Pattern | pattern | text | — | — | Visual pattern or motif | Solid, Striped, Geometric, Floral, Abstract, Damask, Plaid, Botanical, Ombre |
| Opacity/Light Filtering | opacitylight_filtering | enum | — | — | Light blocking level for curtain panels | Sheer, Light Filtering, Room Darkening, Blackout, Total Blackout |
| Lining | lining | text | — | — | Type of backing or lining on curtains | Unlined, Cotton Lining, Blackout Lining, Thermal Lining, Interlining |
| Pieces per Set | pieces_per_set | number | — | — | Number of panels, art pieces, or cushions included | 1, 2, 3, 4, 5 |
| Washable | washable | boolean | — | — | Whether the product is machine washable or removable cover is washable | true, false |
| Care Instructions | care_instructions | text | — | — | Recommended cleaning method | Machine Wash Cold, Dry Clean Only, Spot Clean, Wipe with Damp Cloth |
| Indoor/Outdoor | indooroutdoor | enum | — | — | Whether the product is rated for outdoor or indoor use only | Indoor Only, Outdoor, Indoor/Outdoor |
| UV Resistant | uv_resistant | boolean | — | — | Whether the fabric or material resists UV fading | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus industry standards (ASTM D3691, EN 13120, OEKO-TEX) | [Wayfair](https://www.wayfair.com/decor-pillows/sb0/curtains-drapes-c215008.html), [D Decor](https://www.ddecor.com/), [Accent Decor](https://www.accentdecor.com/home/room-decor/wall-decor), [Touch of Class](https://www.touchofclass.com/window/c/208/) |
