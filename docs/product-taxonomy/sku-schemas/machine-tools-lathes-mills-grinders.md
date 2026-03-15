# SKU Schema: Machine Tools (Lathes, Mills, Grinders)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.machine_tools`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | ST-30, VF-3, GP-34FII, MiniMill |
| Product Name | product_name | text | Full product name including key specs such as type, brand, and model | Haas VF-3 Vertical Machining Center, Mazak Quick Turn 250 CNC Turning Center, Okuma GP-34F II CNC Cylindrical Grinder |
| URL | url | text | Direct link to the product page | https://example.com/product/haas-vf-3 |
| Price | price | number | Numeric price per unit excluding currency symbol | 15900, 52900, 125000, 350000 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Machine Type | machine_type | enum | Primary machine tool category | CNC Lathe, CNC Mill, Manual Lathe, Manual Mill, Surface Grinder, Cylindrical Grinder, CNC Turning Center, 5-Axis Machining Center |
| Country of Origin | country_of_origin | text | Country where the machine was manufactured | USA, Japan, Germany, Taiwan, South Korea |
| Table Size (L x W) | table_size_l_x_w | text (mm) | Working table dimensions for milling machines | 914 x 305, 1219 x 457, 1524 x 660 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| CNC/Manual | cncmanual | enum | Whether the machine is CNC controlled or manually operated | CNC, Manual, CNC with Manual Override |
| CNC Control System | cnc_control_system | text | CNC controller brand and model | Haas NGC, Mazak SmoothAi, Fanuc 0i-TF, Siemens 840D |
| Number of Axes | number_of_axes | number | Total number of controlled axes | 2, 3, 4, 5 |
| Spindle Speed Range | spindle_speed_range | text (RPM) | Minimum to maximum spindle speed | 0-6000, 50-4000, 1-10000, 100-15000 |
| Spindle Taper | spindle_taper | text | Spindle tooling interface standard | CAT 40, BT 40, BT 50, CAT 50, HSK-A63 |
| Spindle Motor Power | spindle_motor_power | number (kW) | Continuous or rated spindle motor power | 5.6, 14.9, 22.4, 30 |
| Spindle Torque | spindle_torque | number (Nm) | Maximum spindle torque | 68, 122, 340, 500 |
| Spindle Bore | spindle_bore | number (mm) | Through-bore diameter of the spindle (lathes) | 52, 66, 80, 102, 180 |
| X-Axis Travel | x-axis_travel | number (mm) | Maximum travel along the X axis | 305, 508, 762, 1016 |
| Y-Axis Travel | y-axis_travel | number (mm) | Maximum travel along the Y axis | 254, 406, 508, 610 |
| Z-Axis Travel | z-axis_travel | number (mm) | Maximum travel along the Z axis | 305, 406, 508, 610 |
| Swing Over Bed | swing_over_bed | number (mm) | Maximum workpiece diameter that clears the lathe bed | 356, 533, 660, 806 |
| Distance Between Centers | distance_between_centers | number (mm) | Maximum distance between headstock and tailstock center (lathes, grinders) | 350, 500, 1000, 1500 |
| Grinding Wheel Width | grinding_wheel_width | number (mm) | Width of the grinding wheel (grinders) | 13, 25, 50, 125 |
| Turret Stations | turret_stations | number | Number of tool positions on the turret (CNC lathes) | 8, 10, 12, 16 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus ISO and ANSI machine tool standards | [Haas](https://www.haascnc.com/machines/vertical-mills/mini-mills/models/minimill.html), [Mazak](https://www.mazak.com/ca-en/products/quick-turn/), [DMG Mori](https://en.dmgmori.com/products/machines), [Okuma](https://www.okuma.co.jp/english/product/nccg/index.php) |
