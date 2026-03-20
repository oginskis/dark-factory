# SKU Schema: Outdoor & Patio Furniture

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.outdoor_patio`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | FP-CUB-5PC-CH, 303.118.24, OD-SEC-GRY |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, material, and seating capacity | Nantucket 5-Piece Teak Dining Set, APPLARO Table 4 Armchairs Outdoor Brown Stained, Montecito Aluminum Sectional Sofa with Sunbrella Cushions |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/nantucket-5pc-dining |
| Price | price | number | — | yes | Numeric price per unit or set excluding currency symbol | 249.00, 899.99, 3450.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Furniture Type | furniture_type | enum | — | — | Specific type of outdoor furniture | Dining Set, Dining Table, Dining Chair, Lounge Chair, Sofa/Sectional, Chaise Lounge, Adirondack Chair, Bench, Bistro Set, Swing, Daybed, Umbrella, Bar Set |
| Frame Material | frame_material | text | — | — | Primary structural frame material | Teak, Powder-Coated Aluminum, Cast Aluminum, Wrought Iron, Poly Lumber (HDPE), Eucalyptus, Stainless Steel, Resin Wicker |
| Wicker/Weave Material | wickerweave_material | text | — | — | Material of woven elements if present | PE Rattan (HDPE), PVC Rattan, Natural Rattan, Resin Wicker |
| Table Top Material | table_top_material | text | — | — | Material of the dining or side table top | Tempered Glass, Teak Slat, Ceramic Tile, Aluminum, Polywood, Stone Composite |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, China, Indonesia, Vietnam, Italy, India |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Number of Pieces | number_of_pieces | number | — | — | Count of items in a set (table, chairs, cushions) | 1, 3, 5, 7, 9 |
| Overall Width | overall_width | number | mm | — | Total width of a single piece or assembled set | 600, 900, 1500, 2400 |
| Overall Depth | overall_depth | number | mm | — | Total depth from front to back | 600, 850, 1000, 1800 |
| Overall Height | overall_height | number | mm | — | Total height from ground to top | 700, 850, 900, 2200 |
| Seat Height | seat_height | number | mm | — | Height from ground to top of seat surface | 330, 380, 430, 480 |
| Frame Finish | frame_finish | text | — | — | Surface treatment applied to the frame | Powder Coated (Black), Oiled Teak, Weathered Grey, Bronze, White, Natural |
| Cushion Included | cushion_included | boolean | — | — | Whether seat and/or back cushions are included | true, false |
| Cushion Fabric | cushion_fabric | text | — | — | Fabric type and brand of included cushions | Sunbrella Acrylic, Olefin, Polyester, Solution-Dyed Acrylic |
| Cushion Color | cushion_color | text | — | — | Color of included cushions | Navy, Canvas Natural, Charcoal, Beige, Forest Green |
| Cushion Thickness | cushion_thickness | number | mm | — | Thickness of the seat cushion | 50, 75, 100, 130 |
| UV Resistant | uv_resistant | boolean | — | — | Whether materials are treated to resist UV fading | true, false |
| Weather Resistant | weather_resistant | boolean | — | — | Whether the product is rated for outdoor weather exposure without covers | true, false |
| Rust Resistant | rust_resistant | boolean | — | — | Whether metal components resist corrosion | true, false |
| Stackable | stackable | boolean | — | — | Whether chairs or components can be stacked for compact storage | true, false |
| Foldable | foldable | boolean | — | — | Whether the piece folds flat for storage | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (BIFMA, EN 581, ASTM F2613) | [IKEA](https://www.ikea.com/us/en/cat/outdoor-patio-furniture-od003/), [Florida Patio](https://floridapatio.net/), [Polywood](https://polyoutdoorfurniture.com/catalog/), [Brilliance Outdoor](https://brillianceoutdoor.com/product-catalog/) |
