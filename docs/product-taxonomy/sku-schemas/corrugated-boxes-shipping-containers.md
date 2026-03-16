# SKU Schema: Corrugated Boxes & Shipping Containers

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.corrugated_boxes_shipping`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | UL-S4040404, BER-v4400K01, PCA-RSC-2412 |
| Product Name | product_name | text | — | Full product name including key dimensions and construction type | 32 ECT Single Wall RSC 12x10x6, Double Wall Heavy Duty Box 24x18x18, White Corrugated Mailer 11x8x4 |
| URL | url | text | — | Direct link to the product page | https://example.com/boxes/rsc-12x10x6 |
| Price | price | number | — | Numeric price per unit or per bundle, excluding currency symbol | 0.85, 7.02, 70.58 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Flute Type | flute_type | enum | — | Flute profile designation indicating flute height and density | A-Flute, B-Flute, C-Flute, E-Flute, F-Flute, BC-Double Wall, AC-Double Wall |
| Board Grade | board_grade | text | — | Combined weight designation of liners and medium, e.g., 200# or ECT-rated | 200 lb/ECT-32, 275 lb/ECT-44, 350 lb/ECT-51 |
| Liner Material | liner_material | enum | — | Material of the outer and inner flat facing sheets | Kraft (Brown), White Kraft, Test Liner, Mottled White |
| Medium Material | medium_material | enum | — | Material of the corrugated fluting medium | Semi-Chemical, Recycled, Straw |
| Country of Origin | country_of_origin | text | — | Country where the corrugated box is manufactured | USA, Canada, Mexico, Germany, China |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Box Style | box_style | enum | — | Structural configuration of the corrugated container | RSC (Regular Slotted Container), HSC (Half Slotted Container), FOL (Full Overlap), Telescope, Die-Cut, Mailer, Wrap-Around |
| Internal Width | internal_width | number | mm | Inside width dimension of the box | 102, 254, 381, 457, 914 |
| Internal Height | internal_height | number | mm | Inside height (depth) dimension of the box | 102, 152, 305, 457, 610 |
| Wall Construction | wall_construction | enum | — | Number of corrugated flute layers in the board | Single Wall, Double Wall, Triple Wall |
| Flute Height | flute_height | number | mm | Approximate height of the corrugated medium flute | 0.8, 1.0, 2.5, 3.2, 4.0, 4.8 |
| ECT Rating | ect_rating | number | lb/in | Edge Crush Test rating measuring vertical compression strength per TAPPI T 811 | 23, 32, 44, 51, 55, 71, 82 |
| Burst Strength | burst_strength | number | psi | Mullen Burst Test rating measuring puncture resistance per TAPPI T 810 | 125, 175, 200, 275, 350 |
| Board Thickness | board_thickness | number | mm | Overall caliper of the combined corrugated board | 1.0, 2.5, 4.0, 5.5, 7.0, 10.0 |
| Color | color | enum | — | Exterior color appearance of the box | Brown Kraft, White, Custom Printed |
| Printing | printing | text | — | Description of any printing applied to the exterior | Unprinted, 1-Color Flexo, 2-Color Flexo, Full Color Litho-Laminate, Custom |
| Moisture Resistance | moisture_resistance | enum | — | Whether the board has been treated for moisture or water resistance | None, Wax Coated, Wax Cascade, Water-Resistant Coating |
| Closure Method | closure_method | enum | — | How the box is sealed for shipping | Tape, Staple, Glue, Self-Locking, Interlocking Tabs |
| Ships Flat | ships_flat | enum | — | Whether the box is shipped and stored in knocked-down flat form | Yes, No |
| Bundle Quantity | bundle_quantity | number | — | Number of boxes per bundle or bale as sold | 10, 15, 20, 25, 50 |
| Pallet Quantity | pallet_quantity | number | — | Number of boxes (or bundles) per standard pallet | 200, 400, 600, 1000, 2400 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (TAPPI T 810/T 811, ASTM D5118, Fibre Box Association ECT guide) | [ULINE Corrugated Boxes](https://www.uline.com/Grp_9/Corrugated-Boxes), [Berlin Packaging](https://www.berlinpackaging.com/standard-corrugated-boxes/), [Anchor Box Strength Guide](https://anchorbox.com/corrugated-box-strength/), [Acme Corrugated Board Grades](https://www.acmebox.com/product-offerings/board-grades/) |
