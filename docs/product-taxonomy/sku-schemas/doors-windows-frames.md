# SKU Schema: Doors, Windows & Frames

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.doors_windows_frames`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | AW-400DH-3652, PEL-250-CS, MRV-ESS-AW |
| Product Name | product_name | text | — | Full product name including key specs such as type, series, and size | Andersen 400 Series Double-Hung Window 36x52, Pella 250 Series Vinyl Casement |
| URL | url | text | — | Direct link to the product page | https://example.com/product/400-series-double-hung |
| Price | price | number | — | Numeric price per unit, excluding currency symbol | 285.00, 549.99, 1250.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | product_category | enum | — | Whether the product is a door, window, or frame | Window, Exterior Door, Interior Door, Patio Door, Skylight, Frame |
| Operation Type | operation_type | enum | — | How the product opens and closes | Double-Hung, Single-Hung, Casement, Awning, Gliding, Fixed/Picture, Bay, Bow, Pivot, Swing, Sliding, Folding, Tilt-Turn |
| Frame Material | frame_material | enum | — | Primary material of the frame or sash | Vinyl, Wood, Fiberglass, Aluminum, Clad Wood, Composite, Steel |
| Glass Type | glass_type | text | — | Glazing unit construction and coating description | Double-Pane Low-E, Triple-Pane Low-E Argon, Tempered, Laminated, Impact-Rated |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, Canada, Denmark, Germany, Poland |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Exterior Cladding | exterior_cladding | text | — | Material cladding the exterior face of the frame | Aluminum, Fiberglass, PVC, None |
| Interior Finish | interior_finish | text | — | Interior frame finish or species | Primed Pine, Stainable Wood, White Vinyl, Prefinished |
| U-Factor | u-factor | number | — | NFRC-rated thermal transmittance of the entire unit (lower is better) | 0.17, 0.25, 0.30, 0.42, 1.10 |
| Solar Heat Gain Coefficient | solar_heat_gain_coefficient | number | — | NFRC-rated fraction of solar radiation admitted (0 to 1) | 0.17, 0.21, 0.25, 0.35, 0.44 |
| Visible Transmittance | visible_transmittance | number | — | NFRC-rated fraction of visible light transmitted (0 to 1) | 0.32, 0.41, 0.51, 0.62 |
| Air Leakage | air_leakage | number | cfm/ft2 | NFRC-rated air infiltration rate | 0.10, 0.20, 0.30 |
| Condensation Resistance | condensation_resistance | number | — | NFRC condensation resistance rating (1 to 100, higher is better) | 35, 51, 62, 71 |
| Design Pressure Rating | design_pressure_rating | number | Pa | Structural wind load resistance rating | 1440, 1920, 2400, 3600 |
| Rough Opening Width | rough_opening_width | number | mm | Required rough opening width for installation | 610, 762, 914, 1220, 1524, 1829 |
| Rough Opening Height | rough_opening_height | number | mm | Required rough opening height for installation | 610, 914, 1220, 1524, 1829, 2134 |
| Unit Width | unit_width | number | mm | Overall width of the finished unit | 600, 750, 900, 1200, 1500, 1800 |
| Unit Height | unit_height | number | mm | Overall height of the finished unit | 600, 900, 1200, 1500, 1800, 2100 |
| Frame Depth | frame_depth | number | mm | Depth of the frame from interior to exterior face | 83, 105, 114, 130, 165 |
| Grid Pattern | grid_pattern | text | — | Muntin or grid configuration | Colonial, Prairie, None, Custom, SDL, GBG |
| Exterior Color | exterior_color | text | — | Color of the exterior frame surface | White, Black, Dark Bronze, Sandtone, Terratone, Forest Green, Custom |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus NFRC rating standards | [Andersen](https://www.andersenwindows.com/windows/), [Pella](https://www.pella.com/support/performance-information/), [Marvin](https://www.marvin.com/windows), [Lowes Windows and Doors](https://www.lowes.com/c/Windows-doors) |
