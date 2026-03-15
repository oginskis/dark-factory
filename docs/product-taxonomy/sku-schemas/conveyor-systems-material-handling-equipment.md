# SKU Schema: Conveyor Systems & Material Handling Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.conveyors_material_handling`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 5VEJ2, DCM2200-24, HYT-TA200 |
| Product Name | product_name | text | Full product name including conveyor type, key dimensions, and series | Dorner 2200 Series Belt Conveyor 24 in x 10 ft, Hytrol Model TA Belt-Over-Roller Conveyor |
| URL | url | text | Direct link to the product page | https://example.com/product/belt-conveyor-2200 |
| Price | price | number | Numeric unit price excluding currency symbol | 2450.00, 8750.00, 15200.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Conveyor Type | conveyor_type | enum | Primary classification of the conveyor system | Belt, Roller, Chain, Modular Belt, Skate Wheel, Screw, Vibrating, Pneumatic, Magnetic |
| Belt Material | belt_material | text | Material composition of the conveyor belt | PVC, Polyurethane, Rubber, Modular Plastic, Wire Mesh, Stainless Steel |
| Frame Material | frame_material | enum | Primary material of the conveyor frame structure | Aluminum, Painted Steel, Stainless Steel, Galvanized Steel |
| Drive Type | drive_type | text | Method used to propel the conveyor | Direct Drive, Gear Motor, Drum Motor, Motorized Roller, Variable Frequency Drive |
| Country of Origin | country_of_origin | text | Country where the conveyor was manufactured | USA, Germany, Sweden, China |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Series/Model | seriesmodel | text | Manufacturer product series or model designation | 2200 Series, DCMove, FlexMove, PSB, Model TA |
| Belt/Bed Width | beltbed_width | text (mm) | Usable width of the belt or conveyor bed. US sizes often in inches | 200, 450, 600, 900, 1200, 18 in, 24 in, 36 in |
| Profile Height | profile_height | number (mm) | Height of the conveyor frame profile from bottom to belt surface | 47, 85, 150, 300 |
| Belt Surface | belt_surface | text | Surface finish or texture of the belt | Smooth, High-Friction, Textured, Cleated, Perforated, Anti-Static |
| Belt Speed | belt_speed | text | Linear speed of the belt or conveyor surface | 0.1-1.5 m/s, 25-400 FPM, Variable |
| Motor Power | motor_power | text | Rated power of the drive motor | 0.25 HP, 0.5 HP, 1 HP, 2 HP, 0.37 kW, 0.75 kW |
| Phase | phase | enum | Electrical phase requirement | Single Phase, Three Phase, DC |
| Frequency | frequency | text (Hz) | Electrical frequency rating | 50, 60, 50/60 |
| Roller Pitch | roller_pitch | number (mm) | Center-to-center spacing between adjacent rollers | 50, 75, 100, 150 |
| Incline Angle | incline_angle | text | Maximum operating angle of incline or decline in degrees | 0, 5, 15, 30, 45, 90 |
| Duty Rating | duty_rating | enum | Load duty classification of the conveyor | Light-Duty, Medium-Duty, Heavy-Duty, Extra Heavy-Duty |
| Operating Temperature | operating_temperature | text | Ambient or product temperature range the conveyor supports | -10 to 40 C, -20 to 80 C, Up to 200 C |
| IP Rating | ip_rating | text | Ingress protection rating for the drive and electrical components | IP54, IP65, IP67, IP69K |
| Conveyor Configuration | conveyor_configuration | text | Layout or shape of the conveyor path | Straight, Curved, Spiral, Incline, Decline, Z-Frame, Alpine |
| Application | application | text (list) | Primary intended uses for the conveyor | Accumulation, Sortation, Transport, Metering, Merging, Diverting, Palletizing |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (CEMA belt standards, ISO 21069) | [Dorner Conveyors](https://www.dornerconveyors.com/industries/material-handling), [Hytrol](https://hytrol.com/products/transport/belt-over-conveyor/), [Grainger](https://www.grainger.com/category/material-handling/transporting/conveyors-components/), [Honeywell Intelligrated](https://sps.honeywell.com/us/en/products/automation/solutions-by-technology/conveyor-systems) |
