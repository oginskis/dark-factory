# SKU Schema: Home Decor (Curtains, Cushions, Wall Art)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | WC-8432-NVY, DD-CUR-120, ART-CVS-3624 |
| Product Name | text | Full product name including key specs such as type, material, and dimensions | Eclipse Blackout Curtain Panel 52x84 in Navy, Sunbrella Outdoor Throw Pillow 20x20 in Natural, Abstract Canvas Wall Art Set of 3 24x36 in |
| URL | text | Direct link to the product page | https://example.com/product/blackout-curtain-navy |
| Price | number | Numeric price per unit or per set excluding currency symbol | 14.99, 39.00, 89.95, 245.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Brand/Manufacturer | text | Brand or manufacturer name | Eclipse, Pottery Barn, D Decor, Threshold (Target), Rifle Paper Co, Uttermost |
| Product Type | enum | Specific type of home decor product | Curtain Panel, Curtain Pair, Valance, Throw Pillow, Pillow Cover, Floor Cushion, Canvas Print, Framed Print, Metal Wall Art, Tapestry, Wall Mirror, Decorative Object, Throw Blanket |
| Panel Width | number (mm) | Width of a single curtain panel or art piece | 520, 1050, 1320 |
| Panel Length/Height | number (mm) | Length/drop of a curtain panel or height of wall art | 1600, 2130, 2440, 2740 |
| Art Width | number (mm) | Width of wall art, mirror, or decorative piece | 300, 450, 600, 900, 1200 |
| Art Height | number (mm) | Height of wall art, mirror, or decorative piece | 300, 450, 600, 900 |
| Art Depth | number (mm) | Depth or profile thickness of wall art including frame or stretcher bars | 15, 20, 38, 50 |
| Cushion Dimensions | text (mm) | Width x height or diameter of cushion or pillow | 450 x 450, 500 x 500, 300 x 500, 600 Diameter |
| Fabric/Material | text | Primary material of the product | Polyester, Cotton, Linen, Velvet, Faux Silk, Canvas, Jute, Burlap, Metal, Wood, Glass |
| Fabric Weight | number (g/m2) | Weight of the fabric per square metre (curtains and cushions) | 120, 180, 250, 300 |
| Fill Material | text | Stuffing or insert material for cushions and pillows | Polyester Fiberfill, Down Alternative, Feather/Down Blend, Foam, Kapok |
| Color | text | Primary color or color family | Navy, Ivory, Charcoal, Blush Pink, Sage Green, Rust, Gold, Multicolor |
| Pattern | text | Visual pattern or motif | Solid, Striped, Geometric, Floral, Abstract, Damask, Plaid, Botanical, Ombre |
| Header/Hanging Type | text | How the curtain attaches to the rod or the art hangs on the wall | Rod Pocket, Grommet (Eyelet), Pinch Pleat, Tab Top, Back Tab, Ring Top, D-Ring Hanger, Sawtooth Hanger, Wire System |
| Opacity/Light Filtering | enum | Light blocking level for curtain panels | Sheer, Light Filtering, Room Darkening, Blackout, Total Blackout |
| Lining | text | Type of backing or lining on curtains | Unlined, Cotton Lining, Blackout Lining, Thermal Lining, Interlining |
| Pieces per Set | number | Number of panels, art pieces, or cushions included | 1, 2, 3, 4, 5 |
| Washable | boolean | Whether the product is machine washable or removable cover is washable | true, false |
| Care Instructions | text | Recommended cleaning method | Machine Wash Cold, Dry Clean Only, Spot Clean, Wipe with Damp Cloth |
| Indoor/Outdoor | enum | Whether the product is rated for outdoor or indoor use only | Indoor Only, Outdoor, Indoor/Outdoor |
| UV Resistant | boolean | Whether the fabric or material resists UV fading | true, false |
| Mounting Hardware Included | boolean | Whether wall art includes hooks, wires, or other hanging hardware | true, false |
| Medium/Technique | text | Artistic medium or reproduction technique for wall art | Giclee on Canvas, Screen Print, Hand Painted, Photographic Print, Mixed Media, Metal Sculpture |
| Frame Material | text | Material of the frame for framed prints or mirrors | Wood, Metal (Aluminum), PS (Polystyrene), Floater Frame, Unframed (Gallery Wrap) |
| Product Weight | number (kg) | Total weight of the product | 0.3, 0.8, 2.5, 5.0, 12.0 |
| Style | text | Design or aesthetic style | Modern, Bohemian, Farmhouse, Coastal, Minimalist, Traditional, Eclectic, Glam |
| Certification | text (list) | Environmental or safety certifications | OEKO-TEX Standard 100, GREENGUARD Gold, GOTS, Fair Trade |
| Country of Origin | text | Country where the product is manufactured | China, India, Turkey, Portugal, USA, Belgium |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus industry standards (ASTM D3691, EN 13120, OEKO-TEX) | [Wayfair](https://www.wayfair.com/decor-pillows/sb0/curtains-drapes-c215008.html), [D Decor](https://www.ddecor.com/), [Accent Decor](https://www.accentdecor.com/home/room-decor/wall-decor), [Touch of Class](https://www.touchofclass.com/window/c/208/) |
