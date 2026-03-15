# SKU Schema: Firearm Optics, Parts & Accessories

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition
**Taxonomy ID:** `firearms.optics_parts_accessories`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | VT-DBK-10029, PA-SLX-1-6, HOL-HS510C |
| Product Name | text | Full product name including key specs such as type, magnification, and model | Vortex Diamondback Tactical 6-24x50 FFP Riflescope, Holosun HS510C Open Reflex Red Dot Sight |
| URL | text | Direct link to the product page | https://example.com/product/diamondback-tactical-6-24x50 |
| Price | number | Numeric unit price excluding currency symbol | 499.99, 309.99, 24.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary category of the item | Riflescope, Red Dot Sight, Prism Scope, Magnifier, Night Vision Device, Thermal Scope, Scope Mount, Scope Rings, Handguard, Stock, Grip, Trigger, Muzzle Device, Magazine, Bipod |
| Reticle Type | text | Name or style of the aiming reticle | EBR-2C MOA, ACSS Raptor, BDC, Crosshair, Duplex, Mil-Dot |
| Material | text | Primary construction material of the body or component | 6061-T6 Aluminum, 7075-T6 Aluminum, Polymer, Steel, Titanium |
| Battery Type | text | Battery required for electronic optics or accessories | CR2032, CR123A, AAA, CR1632 |
| Country of Origin | text | Country where the product is manufactured | USA, Japan, China, Philippines |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Model Number | text | Manufacturer model or part number | DBK-10029, HS510C, ACOG TA31, MOE SL |
| Magnification | text | Magnification power or range; fixed or variable | 1-6x, 6-24x, 3x, 1x, 5-25x |
| Focal Plane | enum | Reticle location in the optical path | First Focal Plane, Second Focal Plane |
| Illumination | text | Reticle or dot illumination type and color | Red, Green, Red/Green, None |
| Eye Relief | number (mm) | Safe distance from the eyepiece to the eye | 90, 95, 100, 102 |
| Field of View | text | Angular or linear field of view at a stated distance | 18-4.5 ft at 100 yds, 106.5 ft at 100 yds |
| Adjustment Graduation | text | Per-click adjustment value for windage and elevation turrets | 1/4 MOA, 1/10 MRAD, 1/2 MOA |
| Total Elevation Travel | text | Maximum elevation adjustment range | 65 MOA, 100 MOA, 25 MRAD |
| Parallax Adjustment | text | Parallax correction range or fixed setting | 10 yds to infinity, Fixed at 100 yds, 50 yds to infinity |
| Lens Coating | text | Anti-reflective or protective coating applied to lenses | Fully Multi-Coated, Multi-Coated, XR Plus, HD |
| Finish/Color | text | Surface finish or color of the product | Matte Black, Flat Dark Earth, OD Green, Anodized Black, Cerakote |
| Waterproof Rating | text | Water and environmental resistance specification | IPX7, O-Ring Sealed, Nitrogen Purged, IP67 |
| Firearm Compatibility | text (list) | Firearm platforms or models the part is designed for | AR-15, AR-10, AK-47, Picatinny, M-LOK, KeyMod, Glock 17/19, Remington 700 |
| Mounting Interface | text | Attachment or mounting standard used | Picatinny, Weaver, M-LOK, KeyMod, Direct Mount, Dovetail |
| Battery Life | text | Estimated operational battery life | 50000 hours, 20000 hours, 100 hours |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (MIL-STD-810, ITAR) | [Primary Arms](https://www.primaryarms.com/optics), [Vortex Optics](https://vortexoptics.com/optics/riflescopes.html), [Trijicon](https://www.scribd.com/document/865666541/PML4034-Rev-14-Trijicon-Catalog-2025-Copia), [OpticsPlanet](https://www.opticsplanet.com/gun-parts.html) |
