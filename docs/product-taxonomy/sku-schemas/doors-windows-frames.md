# SKU Schema: Doors, Windows & Frames

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.doors_windows_frames`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | AW-400DH-3652, PEL-250-CS, MRV-ESS-AW |
| Product Name | text | Full product name including key specs such as type, series, and size | Andersen 400 Series Double-Hung Window 36x52, Pella 250 Series Vinyl Casement |
| URL | text | Direct link to the product page | https://example.com/product/400-series-double-hung |
| Price | number | Numeric price per unit, excluding currency symbol | 285.00, 549.99, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Whether the product is a door, window, or frame | Window, Exterior Door, Interior Door, Patio Door, Skylight, Frame |
| Operation Type | enum | How the product opens and closes | Double-Hung, Single-Hung, Casement, Awning, Gliding, Fixed/Picture, Bay, Bow, Pivot, Swing, Sliding, Folding, Tilt-Turn |
| Frame Material | enum | Primary material of the frame or sash | Vinyl, Wood, Fiberglass, Aluminum, Clad Wood, Composite, Steel |
| Glass Type | text | Glazing unit construction and coating description | Double-Pane Low-E, Triple-Pane Low-E Argon, Tempered, Laminated, Impact-Rated |
| Country of Origin | text | Country where the product was manufactured | USA, Canada, Denmark, Germany, Poland |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Exterior Cladding | text | Material cladding the exterior face of the frame | Aluminum, Fiberglass, PVC, None |
| Interior Finish | text | Interior frame finish or species | Primed Pine, Stainable Wood, White Vinyl, Prefinished |
| U-Factor | number | NFRC-rated thermal transmittance of the entire unit (lower is better) | 0.17, 0.25, 0.30, 0.42, 1.10 |
| Solar Heat Gain Coefficient | number | NFRC-rated fraction of solar radiation admitted (0 to 1) | 0.17, 0.21, 0.25, 0.35, 0.44 |
| Visible Transmittance | number | NFRC-rated fraction of visible light transmitted (0 to 1) | 0.32, 0.41, 0.51, 0.62 |
| Air Leakage | number (cfm/ft2) | NFRC-rated air infiltration rate | 0.10, 0.20, 0.30 |
| Condensation Resistance | number | NFRC condensation resistance rating (1 to 100, higher is better) | 35, 51, 62, 71 |
| Design Pressure Rating | number (Pa) | Structural wind load resistance rating | 1440, 1920, 2400, 3600 |
| Rough Opening Width | number (mm) | Required rough opening width for installation | 610, 762, 914, 1220, 1524, 1829 |
| Rough Opening Height | number (mm) | Required rough opening height for installation | 610, 914, 1220, 1524, 1829, 2134 |
| Unit Width | number (mm) | Overall width of the finished unit | 600, 750, 900, 1200, 1500, 1800 |
| Unit Height | number (mm) | Overall height of the finished unit | 600, 900, 1200, 1500, 1800, 2100 |
| Frame Depth | number (mm) | Depth of the frame from interior to exterior face | 83, 105, 114, 130, 165 |
| Grid Pattern | text | Muntin or grid configuration | Colonial, Prairie, None, Custom, SDL, GBG |
| Exterior Color | text | Color of the exterior frame surface | White, Black, Dark Bronze, Sandtone, Terratone, Forest Green, Custom |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus NFRC rating standards | [Andersen](https://www.andersenwindows.com/windows/), [Pella](https://www.pella.com/support/performance-information/), [Marvin](https://www.marvin.com/windows), [Lowes Windows and Doors](https://www.lowes.com/c/Windows-doors) |
