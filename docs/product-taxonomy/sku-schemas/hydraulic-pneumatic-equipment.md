# SKU Schema: Hydraulic & Pneumatic Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.hydraulic_pneumatic`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DSBC-40-160-PPVA-N3, CQ2B25-10D, HY08-1117 |
| Product Name | text | Full product name including type, series, bore, and stroke | Festo DSBC Standard Cylinder 40mm Bore 160mm Stroke, SMC CQ2 Compact Pneumatic Cylinder 25mm x 10mm |
| URL | text | Direct link to the product page | https://example.com/product/dsbc-40-160 |
| Price | number | Numeric unit price excluding currency symbol | 85.50, 245.00, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Equipment Type | enum | Primary classification of the hydraulic or pneumatic component | Cylinder, Pump, Motor, Valve, Filter, Accumulator, FRL Unit, Fitting, Hose, Manifold |
| Port Thread Type | enum | Thread standard used for port connections | Metric, BSPP, BSPT, NPT, SAE |
| Seal Material | text | Material of the sealing elements | Buna-N (NBR), Viton (FKM), EPDM, Polyurethane, PTFE |
| Body Material | text | Material of the cylinder or component body | Aluminum, Stainless Steel, Steel, Brass, Cast Iron, Composite |
| Valve Type | text | Functional classification for valves | Directional Control, Pressure Relief, Flow Control, Check, Proportional, Servo |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the component was manufactured | Germany, Japan, USA, China, UK |
| Product Series | text | Manufacturer product series or family designation | DSBC, CQ2, DNC, 2H, 3L, HMI, MB, HPP |
| Actuation Medium | enum | Whether the component operates on hydraulic fluid or compressed air | Hydraulic, Pneumatic |
| Operating Pressure Range | text | Minimum to maximum working pressure | 0.6-12 bar, 0-10 bar, 0-210 bar, 500-3000 PSI |
| Maximum Operating Pressure | text | Maximum rated working pressure | 10 bar, 210 bar, 315 bar, 2000 PSI, 3000 PSI, 4000 PSI |
| Mounting Style | text | Method of mounting the component to machinery | Flange, Clevis, Trunnion, Foot, Tie-Rod, Front Flange, Rear Flange, Pivot |
| Cylinder Action | enum | Operating mode of the cylinder | Single-Acting, Double-Acting |
| Rod Configuration | enum | Piston rod arrangement | Single Rod, Double Rod, Through Rod, Non-Rotating Rod |
| Cushioning | text | End-of-stroke deceleration method | Adjustable Air Cushion, Rubber Bumper, Hydraulic Cushion, None |
| Operating Temperature | text | Permissible ambient and fluid temperature range | -10 to 80 C, -20 to 200 C, -40 to 120 C, 14-176 F |
| Flow Rate | text | Maximum fluid flow capacity for valves, pumps, and filters | 5 L/min, 24 GPM, 100 L/min, 300 GPM |
| Displacement | text | Volumetric displacement per revolution for pumps and motors | 4.9 cc/rev, 16 cc/rev, 63 cc/rev, 250 cc/rev |
| Valve Configuration | text | Port and position notation for directional valves | 2/2, 3/2, 4/2, 4/3, 5/2, 5/3 |
| Actuation Method | text | How the valve is actuated | Solenoid, Manual, Pilot Operated, Mechanical, Pneumatic |
| Filtration Rating | text | Particle size rating for hydraulic and pneumatic filters | 3 micron, 5 micron, 10 micron, 25 micron, 40 micron |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ISO 15552, ISO 6020/2, NFPA) | [Festo](https://www.festo.com/us/en/c/products/actuators-and-drives/pneumatic-cylinders-id_pim135/), [SMC](https://www.smcusa.com/products/actuators/linear-actuators/standard~53387), [Parker Hannifin](https://www.parker.com/content/dam/Parker-com/Literature/Industrial-Cylinder/cylinder/cat/english/HY08-1117-1_NA.pdf), [Bosch Rexroth](https://www.boschrexroth.com/en/us/products/industrial-solutions/industrial-hydraulics/valves/) |
