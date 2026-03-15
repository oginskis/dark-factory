# SKU Schema: Plywood & Engineered Wood Panels (OSB, Particle Board)

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber
**Taxonomy ID:** `wood.plywood_engineered_panels`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer product identifier | RIG-PLY-18-BB, WISA-BIRCH-12, OSB3-1220 |
| Product Name | text | Full product name including brand and variant | Riga Ply, WISA-Birch BB/BB, Edge Gold Enhanced Floor Panel |
| URL | text | Direct link to the product page or listing | https://example.com/products/riga-ply/ |
| Price | number | Numeric price value per panel or per unit, no currency symbol | 45.99, 128.50 |
| Currency | text | ISO 4217 currency code | EUR, USD, GBP |
| Panel Type | enum | Type of engineered wood panel | Plywood, OSB, MDF, Particle board, LVL, HDF |
| Surface Grade Front | text | Quality grade of the front (face) veneer per EN 635 or equivalent | S (II), BB (III), B, A, WGE, CP |
| Surface Grade Back | text | Quality grade of the back veneer per EN 635 or equivalent | BB (III), WG (IV), C, CP, WGE |
| Glue Type | enum | Adhesive bonding classification indicating moisture and weather resistance | WBP (weather and boil proof), MR (moisture resistant), Interior, Phenol-formaldehyde, Melamine |
| Structural Class | text | Structural use classification per EN 636 for plywood or EN 300 for OSB | EN 636-2S, EN 636-3S, OSB/2, OSB/3, OSB/4 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Formaldehyde Emission Class | text | Formaldehyde emission rating per applicable standard | E1, E0, CARB Phase 2, F4-star |
| Moisture Resistance Class | text | Bond quality class per EN 314-2 indicating service conditions | Class 1 (dry), Class 2 (humid), Class 3 (exterior) |
| Fire Reaction Class | text | Reaction to fire classification per EN 13501-1 | D-s2 d0, B-s1 d0, C-s2 d0 |
| Country of Origin | text | Country where the panel was manufactured | Latvia, Finland, Estonia, Germany, Canada, USA |
| Manufacturer | text | Company that manufactures the panel | Latvijas Finieris, UPM-Kymmene, Weyerhaeuser |
| Wood Species | text | Primary wood species used in the panel | Birch, Spruce, Pine, Fir, Poplar, Mixed hardwood |
| Thickness | number (mm) | Nominal panel thickness in millimeters | 6.5, 12, 18, 21, 27 |
| Width | number (mm) | Panel width in millimeters | 1220, 1250, 1500, 1525, 2440 |
| Number of Plies | number | Number of veneer layers in the panel, applicable to plywood and LVL | 3, 5, 7, 9, 13, 15 |
| Density | number (kg/m3) | Panel density in kilograms per cubic meter | 460, 630, 680, 750 |
| Surface Treatment | enum | Type of surface coating or overlay applied to the panel | Uncoated, Film-faced, Textured overlay, HPL, Lacquered, Painted, Melamine, Primed |
| Overlay Pattern | text | Pattern or texture of the surface overlay, if applicable | Hexagonal, Diamond, Wire mesh, Smooth, Rhomb, Dot |
| Overlay Color | text | Color of the surface overlay or film | Dark brown, Light brown, Black, Green, Silver grey, Natural birch |
| Bending Strength | number (N/mm2) | Characteristic bending strength parallel to face grain per EN 310 | 30, 40, 55, 70 |
| Modulus of Elasticity | number (N/mm2) | Modulus of elasticity in bending parallel to face grain per EN 310 | 5000, 7000, 10000, 12000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies and EN standards research | [Latvijas Finieris](https://www.finieris.com/products/), [UPM/WISA Plywood](https://www.wisaplywood.com/specifying-wisa/), [Latham Timber](https://www.lathamtimber.co.uk/products/panels/plywood/birch-plywood/birch-plywood-specifications), [Weyerhaeuser](https://www.weyerhaeuser.com/woodproducts/osb-panels/) |
