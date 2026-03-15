# SKU Schema: Machine Tools (Lathes, Mills, Grinders)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | ST-30, VF-3, GP-34FII, MiniMill |
| Product Name | text | Full product name including key specs such as type, brand, and model | Haas VF-3 Vertical Machining Center, Mazak Quick Turn 250 CNC Turning Center, Okuma GP-34F II CNC Cylindrical Grinder |
| URL | text | Direct link to the product page | https://example.com/product/haas-vf-3 |
| Price | number | Numeric price per unit excluding currency symbol | 15900, 52900, 125000, 350000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | Haas, Mazak, DMG Mori, Okuma, Clausing, Sharp Industries, Kent, Hardinge |
| Machine Type | enum | Primary machine tool category | CNC Lathe, CNC Mill, Manual Lathe, Manual Mill, Surface Grinder, Cylindrical Grinder, CNC Turning Center, 5-Axis Machining Center |
| CNC/Manual | enum | Whether the machine is CNC controlled or manually operated | CNC, Manual, CNC with Manual Override |
| CNC Control System | text | CNC controller brand and model | Haas NGC, Mazak SmoothAi, Fanuc 0i-TF, Siemens 840D |
| Number of Axes | number | Total number of controlled axes | 2, 3, 4, 5 |
| Spindle Speed Range | text (RPM) | Minimum to maximum spindle speed | 0-6000, 50-4000, 1-10000, 100-15000 |
| Spindle Taper | text | Spindle tooling interface standard | CAT 40, BT 40, BT 50, CAT 50, HSK-A63 |
| Spindle Motor Power | number (kW) | Continuous or rated spindle motor power | 5.6, 14.9, 22.4, 30 |
| Spindle Torque | number (Nm) | Maximum spindle torque | 68, 122, 340, 500 |
| Spindle Bore | number (mm) | Through-bore diameter of the spindle (lathes) | 52, 66, 80, 102, 180 |
| Table Size (L x W) | text (mm) | Working table dimensions for milling machines | 914 x 305, 1219 x 457, 1524 x 660 |
| X-Axis Travel | number (mm) | Maximum travel along the X axis | 305, 508, 762, 1016 |
| Y-Axis Travel | number (mm) | Maximum travel along the Y axis | 254, 406, 508, 610 |
| Z-Axis Travel | number (mm) | Maximum travel along the Z axis | 305, 406, 508, 610 |
| Swing Over Bed | number (mm) | Maximum workpiece diameter that clears the lathe bed | 356, 533, 660, 806 |
| Max Turning Diameter | number (mm) | Maximum diameter of workpiece that can be turned (lathes) | 254, 409, 457, 711 |
| Max Turning Length | number (mm) | Maximum length of workpiece that can be turned (lathes) | 406, 533, 813, 1524 |
| Distance Between Centers | number (mm) | Maximum distance between headstock and tailstock center (lathes, grinders) | 350, 500, 1000, 1500 |
| Chuck Size | number (mm) | Diameter of the workholding chuck (lathes) | 165, 210, 254, 305, 406 |
| Grinding Wheel Diameter | number (mm) | Maximum grinding wheel diameter (grinders) | 180, 305, 405, 610 |
| Grinding Wheel Width | number (mm) | Width of the grinding wheel (grinders) | 13, 25, 50, 125 |
| Turret Stations | number | Number of tool positions on the turret (CNC lathes) | 8, 10, 12, 16 |
| Tool Changer Capacity | number | Number of tools in the automatic tool changer (mills) | 10, 20, 24, 40 |
| Rapid Traverse Rate | text (m/min) | Maximum rapid positioning speed per axis | X/Y: 25.4, Z: 15.2 |
| Positioning Accuracy | number (mm) | Positional accuracy of the machine axes | 0.005, 0.008, 0.010 |
| Repeatability | number (mm) | Axis repeatability specification | 0.0025, 0.005, 0.008 |
| Coolant System | text | Type of coolant delivery system | Flood, Through-Spindle, Mist, Air Blast |
| Machine Dimensions (L x W x H) | text (mm) | Overall machine footprint and height | 2692 x 1879 x 2642, 3600 x 2100 x 2800 |
| Machine Weight | number (kg) | Total shipping or installed weight of the machine | 1800, 3175, 6800, 12000 |
| Power Supply | text | Electrical supply requirements | 208V/3-phase/60Hz, 400V/3-phase/50Hz, 480V/3-phase/60Hz |
| Certifications | text (list) | Safety and compliance certifications | CE, ISO 9001, ANSI, CSA, UL |
| Country of Origin | text | Country where the machine was manufactured | USA, Japan, Germany, Taiwan, South Korea |
| Warranty | text | Manufacturer warranty duration | 1 year, 2 years |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus ISO and ANSI machine tool standards | [Haas](https://www.haascnc.com/machines/vertical-mills/mini-mills/models/minimill.html), [Mazak](https://www.mazak.com/ca-en/products/quick-turn/), [DMG Mori](https://en.dmgmori.com/products/machines), [Okuma](https://www.okuma.co.jp/english/product/nccg/index.php) |
