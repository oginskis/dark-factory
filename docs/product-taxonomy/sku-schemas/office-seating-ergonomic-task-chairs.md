# SKU Schema: Office Seating (Ergonomic & Task Chairs)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | AER1B23DWALPG1G1G1BBBK23103, 442A40, ST63137 |
| Product Name | text | Full product name including brand, model, and key features | Herman Miller Aeron Remastered Size B Graphite, Steelcase Gesture with Headrest Black |
| URL | text | Direct link to the product page | https://store.hermanmiller.com/office-chairs/aeron-chair/2195348.html |
| Price | number | Numeric unit price excluding currency symbol | 1395.00, 599.99, 249.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Herman Miller, Steelcase, Haworth, HON, Humanscale |
| Model/Series | text | Product model or series name | Aeron, Gesture, Fern, Zody, Leap, Embody |
| Chair Type | enum | Primary classification of the chair | Task Chair, Executive Chair, Conference Chair, Stool, Drafting Chair |
| Size | text | Chair size designation where applicable | A, B, C, Small, Medium, Large, One Size |
| Seat Height Range | text (mm) | Adjustable seat height range from lowest to highest position | 366-490, 381-521, 406-521 |
| Seat Width | number (mm) | Width of the seat pan | 475, 508, 520 |
| Seat Depth | number (mm) | Depth of the seat pan or adjustable depth range | 406, 419-470, 432 |
| Overall Height | text (mm) | Overall height range of the chair from floor to top of backrest | 869-978, 935-1044, 1016-1153 |
| Overall Width | text (mm) | Overall width range including arms at widest setting | 699-744, 719-772, 660 |
| Overall Depth | text (mm) | Overall depth of the chair | 686-699, 699-719, 660 |
| Weight Capacity | number (kg) | Maximum recommended user weight | 136, 159, 181 |
| Product Weight | number (kg) | Net weight of the chair as shipped | 19.1, 22.7, 17.5 |
| Back Material | text | Material used for the backrest surface | 8Z Pellicle Mesh, 3D Knit, Mesh, Upholstered Fabric, Leather |
| Seat Material | text | Material used for the seat surface | Foam with Fabric, Mesh Suspension, Leather, Vinyl |
| Frame Material | text | Material of the structural frame and base | Die-Cast Aluminum, Nylon, Polished Aluminum, Steel |
| Arm Type | enum | Type of armrests included or available | Fully Adjustable 4D, Height Adjustable, Fixed, Armless |
| Tilt Mechanism | text | Type of recline or tilt system | Synchro-Tilt, Harmonic 2 Tilt, Multi-Tilt, Knee-Tilt |
| Lumbar Support | text | Type of lumbar support included | Adjustable PostureFit SL, Height-Adjustable Lumbar, Fixed Lumbar, None |
| Headrest | enum | Whether a headrest is included or optional | Included, Optional, Not Available |
| Caster Type | text | Type of casters fitted to the chair base | Hard Floor Casters, Carpet Casters, Soft Casters, Glides |
| Number of Caster Points | number | Number of legs on the base | 5 |
| Upholstery Color | text | Color or colorway of the primary upholstery | Black, Graphite, Mineral, Nightfall, Licorice, Cosmo Lunar |
| Frame Color | text | Color or finish of the hard components | Graphite, Dark Carbon, Polished Aluminum, Platinum, Black |
| Swivel | enum | Whether the chair rotates 360 degrees | Yes, No |
| Adjustable Seat Depth | enum | Whether the seat depth is adjustable | Yes, No |
| Tilt Lock Positions | text | Number of recline lock positions available | 4 Position, 5 Position, Infinite, Upright Lock Only |
| Tilt Tension Adjustment | enum | Whether the user can adjust recline resistance | Yes, No |
| Warranty Duration | text | Length of the manufacturer warranty | 12 Years, Limited Lifetime, 5 Years, 3 Years |
| Certifications | text (list) | Product safety and environmental certifications | BIFMA X5.1, GREENGUARD, CarbonNeutral, level 2, SCS Indoor Advantage Gold |
| Indoor/Outdoor | enum | Intended use environment | Indoor, Indoor/Outdoor |
| Assembly Required | enum | Whether assembly is needed upon delivery | Yes, No, Minimal |
| Country of Origin | text | Country where the chair is manufactured | USA, China, Mexico, Germany |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus BIFMA standards | [Herman Miller Aeron Specs](https://www.hermanmiller.com/products/seating/office-chairs/aeron-chair/specs/), [Steelcase Gesture](https://www.steelcase.com/products/office-chairs/gesture/), [Haworth Fern](https://store.haworth.com/products/fern-office-chair), [Staples Office Chairs](https://www.staples.com/Office-Chairs/cat_CL166253) |
