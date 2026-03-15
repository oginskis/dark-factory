# SKU Schema: Carpet, Rugs & Floor Coverings

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | CT-1234, BL-5678, RG-90120 |
| Product Name | text | Full product name including collection, pattern, and color | Visual Edge Angled Perception Dark Charcoal, Striation Tile Denim Blue |
| URL | text | Direct link to the product page | https://example.com/product/visual-edge-dark-charcoal |
| Price | number | Numeric price per unit (per square yard, square foot, tile, or each for rugs), excluding currency symbol | 2.50, 18.99, 42.00, 350.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD |
| Brand/Manufacturer | text | Carpet or rug manufacturer name | Mohawk Group, Interface, Milliken, Shaw Contract, Tarkett, Masland |
| Product Form | enum | Physical format of the floor covering | Carpet Tile, Broadloom, Area Rug, Runner, Carpet Roll, Cushion-Back Tile |
| Construction Type | enum | Method of manufacture | Tufted, Woven, Knitted, Needlepunched, Fusion Bonded, Hand Knotted, Hand Tufted, Flatweave |
| Pile Type | enum | Style of the carpet pile surface | Level Loop, Cut Pile, Cut and Loop, Textured, Plush, Frieze, Shag, Berber, Patterned Loop |
| Pile Fiber | text | Fiber material used in the pile surface | Nylon 6, Nylon 6,6, Solution-Dyed Nylon, PET Polyester, PTT Polyester, Wool, Polypropylene |
| Fiber Brand | text | Branded or proprietary fiber name if applicable | Antron, Colorstrand SD, Econyl, StainMaster, Sorona |
| Dye Method | enum | How the color is applied to the fiber or yarn | Solution Dyed, Yarn Dyed, Piece Dyed, Space Dyed, Printed, Injection Dyed |
| Pile Height | number (mm) | Distance from the backing surface to the tip of the pile tufts | 2.5, 3.5, 5.0, 6.0, 8.0, 12.0 |
| Total Thickness | number (mm) | Overall product thickness including backing | 6.0, 8.0, 9.0, 10.5, 12.0 |
| Gauge | text | Spacing of tufting needles, expressed as a fraction of an inch | 1/8, 5/64, 1/10, 1/12, 1/13 |
| Stitch Rate | number | Number of pile tufts per running inch in the machine direction | 8.0, 9.5, 10.2, 12.5 |
| Tuft Density | number (tufts/m2) | Number of tufts per square metre | 62000, 130000, 180000, 260700 |
| Face Weight | number (oz/yd2) | Weight of pile yarns per square yard, excluding backing | 14, 18, 22, 28, 36, 48 |
| Total Weight | number (oz/yd2) | Combined weight of pile and backing per square yard | 80, 95, 110, 140 |
| Tile Size | text | Dimensions for carpet tiles, expressed as length x width | 24x24 in, 50x50 cm, 25x100 cm, 18x36 in, 48x48 in |
| Roll Width | number (ft) | Width for broadloom and rolled carpet | 6, 12, 13.5, 15 |
| Primary Backing | text | Material used for the primary backing layer | Woven Polypropylene, Nonwoven Polyester, ActionBac |
| Secondary Backing | text | Material used for the secondary backing or cushion layer | PVC, Polyurethane, Bitumen, EcoFlex Matrix, StableShield, WellBAC |
| Pattern | text | Visual design or pattern name | Solid, Linear, Geometric, Abstract, Random, Plaid |
| Color | text | Primary color name or number | Dark Charcoal, Denim Blue, Sandstone, Crimson, Bone 103 |
| Colors Available | number | Number of colorways offered for this pattern or style | 6, 12, 18, 24 |
| Flammability Rating | text | Fire performance classification | CRI FF1-70 / CPSC FF1-70, ASTM E648 Class I, EN 13501-1 Bfl-s1 |
| Static Propensity | number (kV) | Electrostatic charge generation measured per AATCC 134 | 1.5, 2.0, 3.0, 3.5 |
| Colorfastness to Light | text | Resistance to fading from light exposure per AATCC 16, rated 1-5 scale | 4, 4+, 5 |
| VOC Emissions | text | Indoor air quality certification for volatile organic compounds | CRI Green Label Plus, FloorScore, GREENGUARD Gold |
| Acoustic Rating | number (dB) | Sound absorption or impact sound reduction value | 20, 25, 30, 35 |
| Application | text (list) | Intended installation environments | Commercial Office, Hospitality, Education, Healthcare, Retail, Residential, Aviation |
| Certification | text (list) | Environmental and quality certifications | CRI Green Label Plus, NSF/ANSI 140, Cradle to Cradle, ISO 14001, Living Product Challenge |
| Country of Origin | text | Country where the product was manufactured | USA, UK, Netherlands, Australia, Belgium |
| Warranty | number (years) | Manufacturer warranty period | 10, 15, 20, Lifetime |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus CRI and ASTM carpet standards | [Interface](https://www.interface.com/US/en-US.html), [Mohawk Group](https://www.mohawkgroup.com/), [Milliken](https://www.milliken.com/en-us/businesses/floor-covering), [Carpet & Rug Institute Specification](https://carpet-rug.org/wp-content/uploads/2019/03/Model-Specification-for-Commercial-Carpet-2018.pdf) |
