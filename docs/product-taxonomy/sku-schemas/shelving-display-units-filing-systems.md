# SKU Schema: Shelving, Display Units & Filing Systems

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.shelving_display_filing`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | H-2169BL, 695620, 80275887 |
| Product Name | text | Full product name including type, dimensions, and key features | Lateral File Cabinet 36in Wide 4 Drawer Black, KALLAX Shelf Unit White 30x58in |
| URL | text | Direct link to the product page | https://www.uline.com/Product/Detail/H-2169BL/Office-Storage/Lateral-File-Cabinet |
| Price | number | Numeric unit price excluding currency symbol | 469.00, 89.99, 249.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary product classification | Lateral File Cabinet, Vertical File Cabinet, Bookcase, Shelving Unit, Display Unit, Flat File Cabinet, Mobile Shelving, Wire Rack |
| Material | text | Primary construction material | Steel, Engineered Wood, Solid Wood, Wire, Aluminum, MDF |
| Mounting Type | enum | How the unit is installed or positioned | Freestanding, Wall-Mounted, Both |
| Country of Origin | text | Country where the product is manufactured | USA, China, Sweden, Mexico |
| Product Weight | number (kg) | Net weight of the unit | 82.6, 45.0, 28.0 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Overall Width | number (mm) | Overall exterior width | 914, 762, 900 |
| Overall Depth | number (mm) | Overall exterior depth | 457, 381, 390 |
| Overall Height | number (mm) | Overall exterior height | 1372, 1524, 2020 |
| Finish | text | Surface finish or coating type | Powder Coated, Laminated, Veneer, Chrome, Galvanized, Melamine |
| Color | text | Primary color of the unit | Black, White, Light Gray, Tan, Oak Effect, Walnut |
| Number of Shelves | number | Total count of shelves or tiers included | 3, 4, 5, 6 |
| Number of Drawers | number | Total count of drawers for filing or storage units | 2, 3, 4, 5 |
| Adjustable Shelves | enum | Whether shelf positions are adjustable | Yes, No |
| Shelf Spacing | text (mm) | Distance between shelves or spacing increments | 32, 178, Adjustable |
| Locking Mechanism | enum | Type of lock for drawers or doors | Keyed Lock, Combination Lock, Electronic Lock, None |
| Drawer Suspension | text | Type of drawer slide mechanism | Full-Extension Ball Bearing, 3/4-Extension, Telescopic |
| Safety Interlock | enum | Whether a single-drawer interlock system is present | Yes, No |
| Assembly Required | enum | Whether assembly is needed | Yes, No, Minimal |
| Stackable | enum | Whether units can be stacked on top of each other | Yes, No |
| Mobile/Casters | enum | Whether the unit includes wheels or casters | Yes, No, Optional |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus ANSI/BIFMA standards | [ULINE Lateral File Cabinet](https://www.uline.com/Product/Detail/H-2169BL/Office-Storage/Lateral-File-Cabinet-36-Wide-4-Drawer-Black), [ULINE Retail Shelves](https://www.uline.com/BL_1425/Uline-Retail-Tables-and-Shelves), [IKEA KALLAX](https://www.ikea.com/us/en/p/kallax-shelf-unit-white-80275887/), [Global Industrial File Cabinets](https://www.globalindustrial.com/c/storage/cabinets/file_cabinets) |
