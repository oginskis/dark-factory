# SKU Schema: Power Tools (Drills, Saws, Sanders)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer article number uniquely identifying the product | 576721, DCD999B, 2904-20 |
| Product Name | text | Full product name including model designation | Plunge-cut saw TS 60 KEBQ-Plus, 20V MAX 1/2 in. Brushless Cordless Hammer Drill/Driver |
| URL | text | Direct link to the product page on the manufacturer or retailer site | https://www.festool.com/products/saws/plunge-saws/576721---ts-60-kebq-plus |
| Price | number | Numeric price value without currency symbol, representing MSRP or list price | 549.00, 199.00, 329.99 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP |
| Brand | text | Manufacturer or brand name | Festool, DeWalt, Milwaukee, Makita, Bosch |
| Model Number | text | Manufacturer model or type designation, often encoding tool class and features | TS 60 KEBQ-Plus, DCD999B, XFD10Z |
| EAN | text | European Article Number or Universal Product Code barcode identifier | 4014549373620, 885911838252 |
| Tool Type | text | Specific type of power tool within the subcategory | Plunge-cut saw, Hammer drill, Random orbit sander, Router, Jigsaw, Angle grinder, Impact driver |
| Product Series | text | Product line or family name grouping related tools | CARVEX, ROTEX, M18 FUEL, XR, LXT |
| Power Source | enum | How the tool is powered | Corded, Cordless, Pneumatic |
| Voltage | number (V) | Nominal voltage of the battery platform for cordless tools, or supply voltage for corded | 18, 20, 36, 110, 230 |
| Battery Capacity | number (Ah) | Amp-hour capacity of the battery when included or specified | 2.0, 4.0, 5.0, 6.0, 8.0 |
| Battery Included | boolean | Whether a battery is included with the tool | true, false |
| Power Rating | number (W) | Rated input power consumption for corded tools or equivalent power for cordless | 1500, 1200, 720, 300 |
| No-Load Speed | text | Maximum rotational speed under no-load conditions, may include multiple speed ranges | 6800 rpm, 0-450/0-1300/0-2000 rpm, 3000-6800 rpm |
| Max Torque | number (Nm) | Maximum torque output of the motor | 54, 135, 158 |
| Number of Speed Settings | number | Count of discrete mechanical speed ranges | 1, 2, 3 |
| Impact Rate | number (bpm) | Blows or impacts per minute for hammer drills and impact drivers | 38250, 33000 |
| Chuck Size | number (mm) | Diameter of the drill chuck opening | 10, 13, 16 |
| Chuck Type | enum | Mechanism used to hold drill bits or accessories | Keyless, Keyed, SDS-plus, SDS-max |
| Blade Diameter | number (mm) | Diameter of the saw blade or cutting disc | 168, 210, 254, 125 |
| Max Cutting Depth at 90 | number (mm) | Maximum cutting depth at perpendicular angle | 62, 55, 75, 85 |
| Max Cutting Depth at 45 | number (mm) | Maximum cutting depth at 45-degree bevel angle | 40, 45, 43 |
| Sanding Pad Diameter | number (mm) | Diameter or dimension of the sanding pad or plate | 125, 150, 80x133 |
| Orbit Diameter | number (mm) | Diameter of the sanding orbit for random orbit sanders | 2.5, 3, 5, 6 |
| Collet Size | number (mm) | Size of the router collet for bit mounting | 6, 8, 12, 1/4 in, 1/2 in |
| Dust Extraction Port | number (mm) | Diameter of the dust extraction connection | 27, 36, 35 |
| Tool Weight | number (kg) | Weight of the bare tool without battery or accessories | 1.5, 3.3, 4.7 |
| Tool Length | number (mm) | Overall length of the tool body | 175, 287, 396 |
| Cable Length | number (m) | Length of the power cord for corded tools | 4.0, 2.5, 5.0 |
| Motor Type | enum | Type of electric motor | Brushed, Brushless |
| Number of Clutch Settings | number | Count of torque-limiting clutch positions for drills and drivers | 11, 18, 21 |
| Sound Power Level | number (dB(A)) | A-weighted sound power level per EN/IEC standards | 101, 96, 88 |
| Vibration Level | number (m/s2) | Triaxial vibration emission value per EN/IEC standards | 2.5, 9.4, 11.7 |
| Included Accessories | text (list) | Items included in the standard delivery scope | Saw blade, Guide rail, Side handle, Systainer, Carrying case |
| Country of Origin | text | Country where the tool is manufactured | Germany, China, Japan, USA |
| Certifications | text (list) | Safety and compliance certifications held by the product | CE, UL, CSA, RoHS, IEC 62841 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 3 manufacturers covering drills, saws, and sanders | [Festool](https://www.festool.com/products), [DeWalt](https://www.dewalt.com/product/dcd999b), [Milwaukee](https://www.milwaukeetool.com/Products/Power-Tools/Drilling/Hammer-Drills/2904-20) |
