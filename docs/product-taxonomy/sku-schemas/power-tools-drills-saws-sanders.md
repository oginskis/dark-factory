# SKU Schema: Power Tools (Drills, Saws, Sanders)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.power_tools`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or retailer article number uniquely identifying the product | 576721, DCD999B, 2904-20 |
| Product Name | product_name | text | — | Full product name including model designation | Plunge-cut saw TS 60 KEBQ-Plus, 20V MAX 1/2 in. Brushless Cordless Hammer Drill/Driver |
| URL | url | text | — | Direct link to the product page on the manufacturer or retailer site | https://www.festool.com/products/saws/plunge-saws/576721---ts-60-kebq-plus |
| Price | price | number | — | Numeric price value without currency symbol, representing MSRP or list price | 549.00, 199.00, 329.99 |
| Currency | currency | text | — | ISO 4217 currency code for the listed price | USD, EUR, GBP |
| Model Number | model_number | text | — | Manufacturer model or type designation, often encoding tool class and features | TS 60 KEBQ-Plus, DCD999B, XFD10Z |
| Tool Type | tool_type | text | — | Specific type of power tool within the subcategory | Plunge-cut saw, Hammer drill, Random orbit sander, Router, Jigsaw, Angle grinder, Impact driver |
| Chuck Type | chuck_type | enum | — | Mechanism used to hold drill bits or accessories | Keyless, Keyed, SDS-plus, SDS-max |
| Motor Type | motor_type | enum | — | Type of electric motor | Brushed, Brushless |
| Country of Origin | country_of_origin | text | — | Country where the tool is manufactured | Germany, China, Japan, USA |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| EAN | ean | text | — | European Article Number or Universal Product Code barcode identifier | 4014549373620, 885911838252 |
| Product Series | product_series | text | — | Product line or family name grouping related tools | CARVEX, ROTEX, M18 FUEL, XR, LXT |
| Power Source | power_source | enum | — | How the tool is powered | Corded, Cordless, Pneumatic |
| Battery Included | battery_included | boolean | — | Whether a battery is included with the tool | true, false |
| Power Rating | power_rating | number | W | Rated input power consumption for corded tools or equivalent power for cordless | 1500, 1200, 720, 300 |
| No-Load Speed | no-load_speed | text | — | Maximum rotational speed under no-load conditions, may include multiple speed ranges | 6800 rpm, 0-450/0-1300/0-2000 rpm, 3000-6800 rpm |
| Max Torque | max_torque | number | Nm | Maximum torque output of the motor | 54, 135, 158 |
| Number of Speed Settings | number_of_speed_settings | number | — | Count of discrete mechanical speed ranges | 1, 2, 3 |
| Impact Rate | impact_rate | number | bpm | Blows or impacts per minute for hammer drills and impact drivers | 38250, 33000 |
| Max Cutting Depth at 90 | max_cutting_depth_at_90 | number | mm | Maximum cutting depth at perpendicular angle | 62, 55, 75, 85 |
| Max Cutting Depth at 45 | max_cutting_depth_at_45 | number | mm | Maximum cutting depth at 45-degree bevel angle | 40, 45, 43 |
| Dust Extraction Port | dust_extraction_port | number | mm | Diameter of the dust extraction connection | 27, 36, 35 |
| Number of Clutch Settings | number_of_clutch_settings | number | — | Count of torque-limiting clutch positions for drills and drivers | 11, 18, 21 |
| Included Accessories | included_accessories | text (list) | — | Items included in the standard delivery scope | Saw blade, Guide rail, Side handle, Systainer, Carrying case |
| Certifications | certifications | text (list) | — | Safety and compliance certifications held by the product | CE, UL, CSA, RoHS, IEC 62841 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 3 manufacturers covering drills, saws, and sanders | [Festool](https://www.festool.com/products), [DeWalt](https://www.dewalt.com/product/dcd999b), [Milwaukee](https://www.milwaukeetool.com/Products/Power-Tools/Drilling/Hammer-Drills/2904-20) |
