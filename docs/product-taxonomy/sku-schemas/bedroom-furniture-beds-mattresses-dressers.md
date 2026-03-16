# SKU Schema: Bedroom Furniture (Beds, Mattresses, Dressers)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.bedroom`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 890.066.63, B553-77, TN-QN-10 |
| Product Name | product_name | text | — | Full product name including key specs such as type, size, and style | MALM Queen Bed Frame with 4 Storage Boxes Black-Brown, Willowton King Panel Bed, Sealy Posturepedic Plus Mount Auburn 13 in Plush Queen Mattress |
| URL | url | text | — | Direct link to the product page | https://example.com/product/malm-bed-frame |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 299.00, 849.99, 1599.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | product_type | enum | — | Specific type of bedroom furniture | Bed Frame, Platform Bed, Panel Bed, Mattress, Dresser, Nightstand, Chest of Drawers, Wardrobe, Vanity, Headboard |
| Frame Material | frame_material | text | — | Primary structural material of the bed frame or dresser | Solid Pine, Engineered Wood, Metal, Solid Oak, Walnut Veneer, Upholstered |
| Storage Type | storage_type | text | — | Type of built-in storage in beds or dressers | Under-Bed Drawers, Ottoman Lift, Bookcase Headboard, Felt-Lined Top Drawer, None |
| Mattress Type | mattress_type | enum | — | Construction category for mattresses | Innerspring, Pocket Coil, Memory Foam, Latex, Hybrid, Pillow Top |
| Comfort Layer Material | comfort_layer_material | text | — | Material of the top comfort layers in mattresses | Gel Memory Foam, Latex, Pillow Top Fiber, Copper-Infused Foam |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | China, Vietnam, USA, Sweden, Malaysia, Mexico |
| Mattress Dimensions | mattress_dimensions | text | mm | Mattress length x width as specified by the size standard | 1905 x 990, 1905 x 1370, 2030 x 1525, 2030 x 1930, 2135 x 1830 |
| Overall Width | overall_width | number | mm | Total outer width of the piece | 1000, 1540, 1670, 2000 |
| Overall Height | overall_height | number | mm | Total height from floor to top (headboard for beds, top surface for dressers) | 1000, 1200, 850, 780 |
| Headboard Height | headboard_height | number | mm | Height of the headboard measured from the floor | 1100, 1300, 1450 |
| Footboard Height | footboard_height | number | mm | Height of the footboard measured from the floor | 300, 450, 600 |
| Clearance Under Bed | clearance_under_bed | number | mm | Space between the floor and the bed base for under-bed storage | 100, 200, 260, 350 |
| Finish | finish | text | — | Surface finish or color of the piece | White, Black-Brown, Natural Oak, Espresso, Grey Wash, Weathered Pine |
| Slat System | slat_system | text | — | Type of mattress support system included in bed frames | Slatted Base Included, Platform (No Slats), Bunkie Board Required, Foundation Required |
| Number of Drawers | number_of_drawers | number | — | Count of storage drawers in beds with storage, dressers, or nightstands | 2, 3, 4, 6, 8 |
| Firmness Level | firmness_level | text | — | Comfort firmness rating for mattresses | Plush, Medium, Medium-Firm, Firm, Extra Firm |
| Mattress Thickness | mattress_thickness | number | mm | Total height/profile of the mattress | 200, 254, 305, 356 |
| Coil Gauge | coil_gauge | number | — | Wire gauge of the coils (lower number equals firmer) | 13, 14, 15, 16 |
| Assembly Required | assembly_required | boolean | — | Whether the product requires assembly | true, false |
| Style | style | text | — | Design or aesthetic style | Modern, Farmhouse, Traditional, Mid-Century, Industrial, Coastal |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (BIFMA, EN 1725, ASTM F1566) | [IKEA](https://www.ikea.com/us/en/cat/beds-bm003/), [Ashley Furniture](https://www.ashleyfurniture.com/c/bedroom/beds/), [ESF Wholesale Furniture](https://www.esfwholesalefurniture.com/catalog/Bedroom-Furniture/), [Casper](https://casper.com/blogs/article/mattress-firmness-scale) |
