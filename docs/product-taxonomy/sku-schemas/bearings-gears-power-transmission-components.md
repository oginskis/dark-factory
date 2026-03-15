# SKU Schema: Bearings, Gears & Power Transmission Components

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.bearings_gears_power_transmission`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 6205-2RS1, 32008-X, R133ZZ, SA47DRE80M4 |
| Product Name | product_name | text | Full product name including type, series, and key dimensions | SKF 6205-2RS1 Deep Groove Ball Bearing 25x52x15mm, SEW Eurodrive SA47 Helical-Worm Gearmotor |
| URL | url | text | Direct link to the product page | https://example.com/product/6205-2rs1 |
| Price | price | number | Numeric unit price excluding currency symbol | 8.50, 42.00, 350.00, 2500.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Component Type | component_type | enum | Primary classification of the power transmission component | Ball Bearing, Roller Bearing, Gear Reducer, Gearmotor, Sprocket, Chain, Belt, Coupling, Shaft, Pulley/Sheave, Linear Guide |
| Bearing Type | bearing_type | text | Specific bearing classification | Deep Groove Ball, Angular Contact Ball, Tapered Roller, Cylindrical Roller, Spherical Roller, Needle Roller, Thrust Ball |
| Seal/Shield Type | sealshield_type | text | Sealing arrangement to retain lubricant and exclude contaminants | Open, Shielded (2Z), Sealed (2RS1), Contact Seal, Non-Contact Seal |
| Cage Material | cage_material | text | Material of the rolling element retainer | Pressed Steel, Machined Brass, Polyamide (PA66), PEEK |
| Material | material | text | Primary material of the bearing rings or gear teeth | Chrome Steel (100Cr6), Stainless Steel (440C), Case-Hardened Steel, Cast Iron, Bronze |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Mounting Type | mounting_type | text | Method of installation for gear reducers and bearings | Foot Mount, Flange Mount, Shaft Mount, Hollow Shaft, Shrink Disc, Pillow Block, Bearing Housing |
| Tolerance Class | tolerance_class | text | Dimensional and running accuracy classification | P0 (Normal), P6, P5, P4, P2, ABEC 1, ABEC 5, ABEC 7 |
| Gear Type | gear_type | text | Classification of gear geometry | Spur, Helical, Bevel, Worm, Planetary, Hypoid |
| Country of Origin | country_of_origin | text | Country where the component was manufactured | Sweden, Germany, Japan, USA, China, Romania |
| Product Series | product_series | text | Manufacturer product series or family name | 6200 Series, 32000 Series, R Series, KR CYBERTECH, SA, K Series, HK Series |
| Width | width | number (mm) | Axial width of the bearing or face width of a gear | 4, 8, 14, 15, 17, 25, 65 |
| Dynamic Load Rating | dynamic_load_rating | number (kN) | Basic dynamic load rating per ISO 281 indicating fatigue life under rotation | 2.7, 14.8, 35.1, 95.6, 296 |
| Static Load Rating | static_load_rating | number (kN) | Basic static load rating per ISO 76 for non-rotating or slow conditions | 1.5, 7.8, 19.5, 62.0, 296 |
| Limiting Speed | limiting_speed | number (rpm) | Maximum recommended operating speed | 5000, 11000, 19000, 32000, 56000 |
| Reference Speed | reference_speed | number (rpm) | Thermal reference speed per ISO 15312 for grease or oil lubrication | 8500, 13000, 22000, 43000 |
| Contact Angle | contact_angle | number (degrees) | Angle of contact between rolling elements and raceway for angular bearings | 15, 25, 30, 40 |
| Internal Clearance | internal_clearance | text | Radial or axial play classification within the bearing | C2, Normal (CN), C3, C4, C5 |
| Gear Ratio | gear_ratio | text | Input to output speed ratio for gear reducers | 3:1, 7.5:1, 25:1, 60:1, 112:1, 450:1 |
| Output Torque | output_torque | text | Maximum continuous torque at the output shaft of a gear reducer | 50 Nm, 200 Nm, 1603 kNm, 575000 lb-in |
| Input Power | input_power | text | Rated motor input power for gearmotors | 0.12 kW, 0.55 kW, 1.5 kW, 7.5 kW, 22 kW |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ISO 281, ISO 76, ABMA, AGMA) | [SKF](https://www.nodeshk.com/skf/ball-bearings/), [Timken](https://www.timken.com/resources/timken-engineering-manual/), [SEW Eurodrive](https://www.seweurodrive.com/products/gear-units/gear-units.html), [AutomationDirect](https://www.automationdirect.com/adc/overview/catalog/power_transmission_(mechanical)) |
