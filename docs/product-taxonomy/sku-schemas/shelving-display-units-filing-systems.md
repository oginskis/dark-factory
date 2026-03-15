# SKU Schema: Shelving, Display Units & Filing Systems

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | H-2169BL, 695620, 80275887 |
| Product Name | text | Full product name including type, dimensions, and key features | Lateral File Cabinet 36in Wide 4 Drawer Black, KALLAX Shelf Unit White 30x58in |
| URL | text | Direct link to the product page | https://www.uline.com/Product/Detail/H-2169BL/Office-Storage/Lateral-File-Cabinet |
| Price | number | Numeric unit price excluding currency symbol | 469.00, 89.99, 249.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | ULINE, IKEA, Global Industrial, HON, Steelcase |
| Product Type | enum | Primary product classification | Lateral File Cabinet, Vertical File Cabinet, Bookcase, Shelving Unit, Display Unit, Flat File Cabinet, Mobile Shelving, Wire Rack |
| Overall Width | number (mm) | Overall exterior width | 914, 762, 900 |
| Overall Depth | number (mm) | Overall exterior depth | 457, 381, 390 |
| Overall Height | number (mm) | Overall exterior height | 1372, 1524, 2020 |
| Product Weight | number (kg) | Net weight of the unit | 82.6, 45.0, 28.0 |
| Material | text | Primary construction material | Steel, Engineered Wood, Solid Wood, Wire, Aluminum, MDF |
| Finish | text | Surface finish or coating type | Powder Coated, Laminated, Veneer, Chrome, Galvanized, Melamine |
| Color | text | Primary color of the unit | Black, White, Light Gray, Tan, Oak Effect, Walnut |
| Number of Shelves | number | Total count of shelves or tiers included | 3, 4, 5, 6 |
| Number of Drawers | number | Total count of drawers for filing or storage units | 2, 3, 4, 5 |
| Shelf Capacity | number (kg) | Maximum weight per individual shelf | 22.7, 50, 79.4 |
| Total Weight Capacity | number (kg) | Maximum total load the unit can support | 136, 272, 454 |
| Drawer Capacity | number (kg) | Maximum weight per drawer | 34, 50, 56.7 |
| File Size | text (list) | Supported paper/file sizes for filing cabinets | Letter, Legal, A4 |
| Adjustable Shelves | enum | Whether shelf positions are adjustable | Yes, No |
| Shelf Spacing | text (mm) | Distance between shelves or spacing increments | 32, 178, Adjustable |
| Locking Mechanism | enum | Type of lock for drawers or doors | Keyed Lock, Combination Lock, Electronic Lock, None |
| Drawer Suspension | text | Type of drawer slide mechanism | Full-Extension Ball Bearing, 3/4-Extension, Telescopic |
| Safety Interlock | enum | Whether a single-drawer interlock system is present | Yes, No |
| Assembly Required | enum | Whether assembly is needed | Yes, No, Minimal |
| Mounting Type | enum | How the unit is installed or positioned | Freestanding, Wall-Mounted, Both |
| Stackable | enum | Whether units can be stacked on top of each other | Yes, No |
| Mobile/Casters | enum | Whether the unit includes wheels or casters | Yes, No, Optional |
| Indoor/Outdoor | enum | Intended use environment | Indoor, Outdoor, Both |
| Certifications | text (list) | Product safety and environmental certifications | ANSI/BIFMA X5.9, GREENGUARD, FSC, CARB Phase 2 |
| Leveling Guides | enum | Whether adjustable floor levelers are included | Yes, No |
| Country of Origin | text | Country where the product is manufactured | USA, China, Sweden, Mexico |
| Warranty Duration | text | Length of the manufacturer warranty | Limited Lifetime, 10 Years, 5 Years, 1 Year |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus ANSI/BIFMA standards | [ULINE Lateral File Cabinet](https://www.uline.com/Product/Detail/H-2169BL/Office-Storage/Lateral-File-Cabinet-36-Wide-4-Drawer-Black), [ULINE Retail Shelves](https://www.uline.com/BL_1425/Uline-Retail-Tables-and-Shelves), [IKEA KALLAX](https://www.ikea.com/us/en/p/kallax-shelf-unit-white-80275887/), [Global Industrial File Cabinets](https://www.globalindustrial.com/c/storage/cabinets/file_cabinets) |
