# SKU Schema: Outdoor & Patio Furniture

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.outdoor_patio`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | FP-CUB-5PC-CH, 303.118.24, OD-SEC-GRY |
| Product Name | text | Full product name including key specs such as type, material, and seating capacity | Nantucket 5-Piece Teak Dining Set, APPLARO Table 4 Armchairs Outdoor Brown Stained, Montecito Aluminum Sectional Sofa with Sunbrella Cushions |
| URL | text | Direct link to the product page | https://example.com/product/nantucket-5pc-dining |
| Price | number | Numeric price per unit or set excluding currency symbol | 249.00, 899.99, 3450.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Furniture Type | enum | Specific type of outdoor furniture | Dining Set, Dining Table, Dining Chair, Lounge Chair, Sofa/Sectional, Chaise Lounge, Adirondack Chair, Bench, Bistro Set, Swing, Daybed, Umbrella, Bar Set |
| Frame Material | text | Primary structural frame material | Teak, Powder-Coated Aluminum, Cast Aluminum, Wrought Iron, Poly Lumber (HDPE), Eucalyptus, Stainless Steel, Resin Wicker |
| Wicker/Weave Material | text | Material of woven elements if present | PE Rattan (HDPE), PVC Rattan, Natural Rattan, Resin Wicker |
| Table Top Material | text | Material of the dining or side table top | Tempered Glass, Teak Slat, Ceramic Tile, Aluminum, Polywood, Stone Composite |
| Country of Origin | text | Country where the product is manufactured | USA, China, Indonesia, Vietnam, Italy, India |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Number of Pieces | number | Count of items in a set (table, chairs, cushions) | 1, 3, 5, 7, 9 |
| Overall Width | number (mm) | Total width of a single piece or assembled set | 600, 900, 1500, 2400 |
| Overall Depth | number (mm) | Total depth from front to back | 600, 850, 1000, 1800 |
| Overall Height | number (mm) | Total height from ground to top | 700, 850, 900, 2200 |
| Seat Height | number (mm) | Height from ground to top of seat surface | 330, 380, 430, 480 |
| Frame Finish | text | Surface treatment applied to the frame | Powder Coated (Black), Oiled Teak, Weathered Grey, Bronze, White, Natural |
| Cushion Included | boolean | Whether seat and/or back cushions are included | true, false |
| Cushion Fabric | text | Fabric type and brand of included cushions | Sunbrella Acrylic, Olefin, Polyester, Solution-Dyed Acrylic |
| Cushion Color | text | Color of included cushions | Navy, Canvas Natural, Charcoal, Beige, Forest Green |
| Cushion Thickness | number (mm) | Thickness of the seat cushion | 50, 75, 100, 130 |
| UV Resistant | boolean | Whether materials are treated to resist UV fading | true, false |
| Weather Resistant | boolean | Whether the product is rated for outdoor weather exposure without covers | true, false |
| Rust Resistant | boolean | Whether metal components resist corrosion | true, false |
| Stackable | boolean | Whether chairs or components can be stacked for compact storage | true, false |
| Foldable | boolean | Whether the piece folds flat for storage | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (BIFMA, EN 581, ASTM F2613) | [IKEA](https://www.ikea.com/us/en/cat/outdoor-patio-furniture-od003/), [Florida Patio](https://floridapatio.net/), [Polywood](https://polyoutdoorfurniture.com/catalog/), [Brilliance Outdoor](https://brillianceoutdoor.com/product-catalog/) |
