# SKU Schema: Cabinetry & Storage Furniture

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.cabinetry_storage`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 803.290.18, B36-SS, W3630-GD |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, material, and dimensions | KALLAX Shelf Unit 4x4 White, Shaker Base Cabinet 36 in Gray, BESTA Storage Combination with Doors 120x42x193 cm |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/kallax-shelf-unit |
| Price | price | number | — | yes | Numeric price per unit excluding currency symbol | 89.99, 285.00, 1450.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Specific type of cabinetry or storage furniture | Base Cabinet, Wall Cabinet, Tall/Pantry Cabinet, Vanity Cabinet, Bookcase, Storage Cabinet, Sideboard/Buffet, TV Stand, Shelf Unit, Wardrobe |
| Box Material | box_material | text | — | — | Material of the cabinet carcass/box | Plywood, Particleboard, MDF, Solid Wood (Birch), Furniture Board |
| Door Material | door_material | text | — | — | Material of the door panels | Solid Wood (Maple), MDF with Thermofoil, Plywood with Veneer, Solid Birch, Lacquered MDF |
| Drawer Glide Type | drawer_glide_type | text | — | — | Type of drawer slide mechanism | Full-Extension Ball Bearing, Undermount Soft-Close, European Roller, Side-Mount |
| Drawer Box Material | drawer_box_material | text | — | — | Material of the drawer box sides and bottom | Solid Hardwood Dovetail, Plywood, Engineered Wood, Metal |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Hinge Type | hinge_type | text | — | — | Type of door hinge mechanism | Concealed European (6-Way Adjustable), Soft-Close Blum, Overlay, Inset, Surface Mount |
| Back Panel Material | back_panel_material | text | — | — | Material of the rear panel | 3mm HDF, 6mm Plywood, 3mm Fiberboard |
| Assembly Type | assembly_type | enum | — | — | How the product is delivered relative to assembly | Ready to Assemble (RTA), Fully Assembled, Semi-Assembled |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | China, USA, Canada, Vietnam, Sweden, Poland |
| Overall Width | overall_width | number | mm | — | Total outer width of the unit | 300, 600, 900, 1200, 1800 |
| Overall Depth | overall_depth | number | mm | — | Total outer depth of the unit | 280, 350, 400, 600 |
| Overall Height | overall_height | number | mm | — | Total outer height of the unit | 720, 850, 1470, 2000, 2400 |
| Box Thickness | box_thickness | number | mm | — | Thickness of the side and top/bottom panels | 12, 16, 18, 19 |
| Door Style | door_style | text | — | — | Front door panel design | Shaker, Flat Panel (Slab), Raised Panel, Glass Insert, Louvered, Beadboard, Open (No Door) |
| Finish | finish | text | — | — | Surface finish or color | White, Espresso, Natural Oak, Grey, Black-Brown, Painted (Custom Color), Walnut Effect |
| Number of Doors | number_of_doors | number | — | — | Count of front-facing doors | 0, 1, 2, 3, 4 |
| Number of Shelves | number_of_shelves | number | — | — | Count of internal shelves (both fixed and adjustable) | 1, 2, 3, 4, 6 |
| Adjustable Shelves | adjustable_shelves | boolean | — | — | Whether the shelf positions are adjustable | true, false |
| Shelf Spacing | shelf_spacing | number | mm | — | Increment between shelf pin holes | 32, 37.5 |
| Number of Drawers | number_of_drawers | number | — | — | Count of drawers in the unit | 0, 1, 2, 3, 4, 6, 8 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (KCMA, ANSI/BHMA A156.9, AWS) | [IKEA](https://www.ikea.com/us/en/cat/cabinets-cupboards-st002/), [J and K Cabinetry](https://www.jk-cabinetry.com/catalog), [Cabinet Joint](https://www.cabinetjoint.com/cabinet-specifications/), [Shenandoah Cabinetry](https://shenandoahcabinetry.com/) |
