# SKU Schema: Office Seating (Ergonomic & Task Chairs)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.office_seating`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | AER1B23DWALPG1G1G1BBBK23103, 442A40, ST63137 |
| Product Name | text | Full product name including brand, model, and key features | Herman Miller Aeron Remastered Size B Graphite, Steelcase Gesture with Headrest Black |
| URL | text | Direct link to the product page | https://store.hermanmiller.com/office-chairs/aeron-chair/2195348.html |
| Price | number | Numeric unit price excluding currency symbol | 1395.00, 599.99, 249.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Chair Type | enum | Primary classification of the chair | Task Chair, Executive Chair, Conference Chair, Stool, Drafting Chair |
| Back Material | text | Material used for the backrest surface | 8Z Pellicle Mesh, 3D Knit, Mesh, Upholstered Fabric, Leather |
| Seat Material | text | Material used for the seat surface | Foam with Fabric, Mesh Suspension, Leather, Vinyl |
| Frame Material | text | Material of the structural frame and base | Die-Cast Aluminum, Nylon, Polished Aluminum, Steel |
| Arm Type | enum | Type of armrests included or available | Fully Adjustable 4D, Height Adjustable, Fixed, Armless |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Caster Type | text | Type of casters fitted to the chair base | Hard Floor Casters, Carpet Casters, Soft Casters, Glides |
| Country of Origin | text | Country where the chair is manufactured | USA, China, Mexico, Germany |
| Model/Series | text | Product model or series name | Aeron, Gesture, Fern, Zody, Leap, Embody |
| Seat Height Range | text (mm) | Adjustable seat height range from lowest to highest position | 366-490, 381-521, 406-521 |
| Seat Width | number (mm) | Width of the seat pan | 475, 508, 520 |
| Seat Depth | number (mm) | Depth of the seat pan or adjustable depth range | 406, 419-470, 432 |
| Overall Height | text (mm) | Overall height range of the chair from floor to top of backrest | 869-978, 935-1044, 1016-1153 |
| Overall Width | text (mm) | Overall width range including arms at widest setting | 699-744, 719-772, 660 |
| Overall Depth | text (mm) | Overall depth of the chair | 686-699, 699-719, 660 |
| Tilt Mechanism | text | Type of recline or tilt system | Synchro-Tilt, Harmonic 2 Tilt, Multi-Tilt, Knee-Tilt |
| Lumbar Support | text | Type of lumbar support included | Adjustable PostureFit SL, Height-Adjustable Lumbar, Fixed Lumbar, None |
| Headrest | enum | Whether a headrest is included or optional | Included, Optional, Not Available |
| Number of Caster Points | number | Number of legs on the base | 5 |
| Upholstery Color | text | Color or colorway of the primary upholstery | Black, Graphite, Mineral, Nightfall, Licorice, Cosmo Lunar |
| Frame Color | text | Color or finish of the hard components | Graphite, Dark Carbon, Polished Aluminum, Platinum, Black |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus BIFMA standards | [Herman Miller Aeron Specs](https://www.hermanmiller.com/products/seating/office-chairs/aeron-chair/specs/), [Steelcase Gesture](https://www.steelcase.com/products/office-chairs/gesture/), [Haworth Fern](https://store.haworth.com/products/fern-office-chair), [Staples Office Chairs](https://www.staples.com/Office-Chairs/cat_CL166253) |
