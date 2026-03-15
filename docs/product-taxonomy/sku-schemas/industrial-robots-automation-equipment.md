# SKU Schema: Industrial Robots & Automation Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | IRB-1200-5/0.9, GP25-12, KR-16-R2010 |
| Product Name | text | Full product name including series, payload, and reach | ABB IRB 1200-5/0.9 Articulated Robot, FANUC M-710iC/70 Multipurpose Robot, KUKA KR 16 R2010 |
| URL | text | Direct link to the product page | https://example.com/product/irb-1200 |
| Price | number | Numeric unit price excluding currency symbol | 25000, 65000, 150000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Company that manufactured the robot or automation equipment | ABB, FANUC, KUKA, Yaskawa Motoman, Universal Robots, Staubli, Mitsubishi Electric, OMRON |
| Robot Type | enum | Mechanical structure classification per ISO 8373 | Articulated, SCARA, Delta/Parallel, Cartesian/Gantry, Collaborative (Cobot), Cylindrical |
| Product Series | text | Manufacturer product series or family | IRB, GP, KR AGILUS, KR QUANTEC, CRX, UR, M-Series, LBR iisy |
| Number of Axes | number | Degrees of freedom (number of independent joints) | 4, 5, 6, 7 |
| Payload Capacity | number (kg) | Maximum mass the robot can carry at its wrist including tooling | 0.5, 3, 7, 12.5, 25, 70, 210, 900, 2300 |
| Maximum Reach | number (mm) | Horizontal reach from the base center to the tool center point | 400, 580, 900, 1300, 1811, 2600, 3200, 4683 |
| Repeatability | number (mm) | Pose repeatability at the tool center point per ISO 9283 | 0.01, 0.02, 0.04, 0.05, 0.08, 0.3 |
| Robot Weight | number (kg) | Mass of the robot manipulator arm excluding controller | 25, 33.5, 52, 120, 250, 1200, 2300 |
| Mounting Position | text (list) | Supported installation orientations | Floor, Ceiling, Wall, Angle, Any Orientation |
| IP Rating | text | Ingress protection rating of the robot body and wrist | IP20, IP40, IP54, IP65, IP67, IP69K |
| Controller | text | Robot controller model or platform | IRC5, OmniCore, KR C5, DX200, YRC1000, UR Control Box, R-30iB Plus |
| Operating System | text | Software platform running on the controller | RobotStudio, iiQKA.OS, Polyscope, INFORM, iQ Works, FANUC iHMI |
| Motion Range Axis 1 | text (degrees) | Angular range of motion for joint 1 (base rotation) | +/-180, +/-170, +/-185, +/-360 |
| Maximum Speed TCP | number (mm/s) | Maximum linear speed at the tool center point | 1000, 2000, 4000, 7000, 11000 |
| Maximum Joint Speed | text (degrees/s) | Maximum angular velocity of the fastest joint | 250, 400, 610, 720 |
| Cycle Time | text | Typical pick-and-place cycle time for standard motion pattern | 0.27 s, 0.4 s, 0.58 s, 1.0 s |
| Power Consumption | text | Typical and maximum electrical power draw | 350 W typical, 615 W max, 2.5 kW, 7.5 kW |
| Power Supply | text | Required electrical supply voltage and frequency | 100-240VAC 50/60Hz, 200-600VAC 50/60Hz, 380-480VAC |
| Footprint | text | Base installation area or diameter | 190 mm dia, 320 x 320 mm, 550 x 550 mm, 780 x 780 mm |
| Communication Protocols | text (list) | Supported industrial network interfaces | EtherNet/IP, PROFINET, EtherCAT, DeviceNet, CC-Link, Modbus TCP |
| Application | text (list) | Primary intended robot applications | Arc Welding, Spot Welding, Assembly, Palletizing, Pick and Place, Machine Tending, Painting, Dispensing, Deburring, Inspection |
| Safety Features | text (list) | Integrated safety capabilities | Force/Torque Sensing, Speed Monitoring, Safety-Rated Soft Axis Limiting, Collision Detection, SafeMove |
| Operating Temperature | text | Permissible ambient temperature range | 0 to 45 C, 5 to 45 C, -10 to 55 C |
| Noise Level | number (dB) | Acoustic noise emission during operation | 65, 70, 72, 78 |
| Wrist Tooling Interface | text | Mechanical and electrical tool flange standard | ISO 9409-1-50-4-M6, ISO 9409-1-31.5-4-M5, DIN ISO 9409 |
| Protection Class | text | Special environment ratings beyond standard IP | Cleanroom ISO 5, Foundry, Food Grade, ESD Safe, Washdown |
| Certification | text (list) | Safety and regulatory certifications | CE, UL, ISO 10218-1, ISO/TS 15066, TUV, NRTL, KCs |
| Warranty | text | Standard manufacturer warranty period | 1 year, 2 years, 3 years |
| Country of Origin | text | Country where the robot was manufactured | Japan, Germany, Sweden, Switzerland, Denmark, USA, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (ISO 8373, ISO 9283, ISO 10218-1) | [ABB Robotics](https://new.abb.com/products/robotics), [FANUC](https://www.fanuc.eu/eu-en/m-2000-series), [KUKA](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots), [Universal Robots](https://www.universal-robots.com/media/1807466/ur10e_e-series_datasheets_web.pdf) |
