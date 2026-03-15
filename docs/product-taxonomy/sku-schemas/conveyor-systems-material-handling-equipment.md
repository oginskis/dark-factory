# SKU Schema: Conveyor Systems & Material Handling Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 5VEJ2, DCM2200-24, HYT-TA200 |
| Product Name | text | Full product name including conveyor type, key dimensions, and series | Dorner 2200 Series Belt Conveyor 24 in x 10 ft, Hytrol Model TA Belt-Over-Roller Conveyor |
| URL | text | Direct link to the product page | https://example.com/product/belt-conveyor-2200 |
| Price | number | Numeric unit price excluding currency symbol | 2450.00, 8750.00, 15200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that manufactured or branded the conveyor | Dorner, Hytrol, Honeywell Intelligrated, Interroll, FlexLink |
| Conveyor Type | enum | Primary classification of the conveyor system | Belt, Roller, Chain, Modular Belt, Skate Wheel, Screw, Vibrating, Pneumatic, Magnetic |
| Series/Model | text | Manufacturer product series or model designation | 2200 Series, DCMove, FlexMove, PSB, Model TA |
| Belt/Bed Width | text (mm) | Usable width of the belt or conveyor bed. US sizes often in inches | 200, 450, 600, 900, 1200, 18 in, 24 in, 36 in |
| Overall Length | text (mm) | Total conveyor length including head and tail sections | 3000, 6000, 12000, 10 ft, 24 ft |
| Profile Height | number (mm) | Height of the conveyor frame profile from bottom to belt surface | 47, 85, 150, 300 |
| Belt Material | text | Material composition of the conveyor belt | PVC, Polyurethane, Rubber, Modular Plastic, Wire Mesh, Stainless Steel |
| Belt Surface | text | Surface finish or texture of the belt | Smooth, High-Friction, Textured, Cleated, Perforated, Anti-Static |
| Frame Material | enum | Primary material of the conveyor frame structure | Aluminum, Painted Steel, Stainless Steel, Galvanized Steel |
| Load Capacity per Unit Length | text | Maximum distributed load the conveyor can support per linear unit | 75 lbs/ft, 150 lbs/ft, 600 lbs/ft, 100 kg/m |
| Total Load Capacity | text | Maximum total weight the conveyor can carry at once | 250 lbs, 1000 lbs, 500 kg, 2000 kg |
| Belt Speed | text | Linear speed of the belt or conveyor surface | 0.1-1.5 m/s, 25-400 FPM, Variable |
| Motor Power | text | Rated power of the drive motor | 0.25 HP, 0.5 HP, 1 HP, 2 HP, 0.37 kW, 0.75 kW |
| Voltage | text | Electrical supply voltage requirement | 115V, 208/230/460V, 24VDC, 400V |
| Phase | enum | Electrical phase requirement | Single Phase, Three Phase, DC |
| Frequency | text (Hz) | Electrical frequency rating | 50, 60, 50/60 |
| Drive Type | text | Method used to propel the conveyor | Direct Drive, Gear Motor, Drum Motor, Motorized Roller, Variable Frequency Drive |
| Roller Diameter | number (mm) | Diameter of conveyor rollers for roller-type conveyors | 19, 38, 50, 63, 89 |
| Roller Pitch | number (mm) | Center-to-center spacing between adjacent rollers | 50, 75, 100, 150 |
| Incline Angle | text | Maximum operating angle of incline or decline in degrees | 0, 5, 15, 30, 45, 90 |
| Duty Rating | enum | Load duty classification of the conveyor | Light-Duty, Medium-Duty, Heavy-Duty, Extra Heavy-Duty |
| Operating Temperature | text | Ambient or product temperature range the conveyor supports | -10 to 40 C, -20 to 80 C, Up to 200 C |
| IP Rating | text | Ingress protection rating for the drive and electrical components | IP54, IP65, IP67, IP69K |
| Conveyor Configuration | text | Layout or shape of the conveyor path | Straight, Curved, Spiral, Incline, Decline, Z-Frame, Alpine |
| Application | text (list) | Primary intended uses for the conveyor | Accumulation, Sortation, Transport, Metering, Merging, Diverting, Palletizing |
| Industry | text (list) | Target industry sectors for the equipment | Food and Beverage, Pharmaceutical, Packaging, Automotive, E-Commerce, Logistics |
| Compliance/Certification | text (list) | Regulatory and industry certifications | CE, UL, FDA, USDA, ATEX, BISSC, ISO 9001 |
| Weight | number (kg) | Net weight of the conveyor unit as shipped | 25, 75, 150, 500 |
| Country of Origin | text | Country where the conveyor was manufactured | USA, Germany, Sweden, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (CEMA belt standards, ISO 21069) | [Dorner Conveyors](https://www.dornerconveyors.com/industries/material-handling), [Hytrol](https://hytrol.com/products/transport/belt-over-conveyor/), [Grainger](https://www.grainger.com/category/material-handling/transporting/conveyors-components/), [Honeywell Intelligrated](https://sps.honeywell.com/us/en/products/automation/solutions-by-technology/conveyor-systems) |
