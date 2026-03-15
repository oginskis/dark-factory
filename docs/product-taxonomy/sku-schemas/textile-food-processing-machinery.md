# SKU Schema: Textile & Food Processing Machinery

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | GEA-CG1500, 4146-SS, R37-600, LMW-LK64 |
| Product Name | text | Full product name including key specs such as machine type, model, and capacity | GEA ComboGrind 1500/250 Industrial Meat Grinder, Rieter R 37 Rotor Spinning Machine 600 Positions |
| URL | text | Direct link to the product page | https://example.com/product/combogrind-1500 |
| Price | number | Numeric price per unit excluding currency symbol | 85000, 245000, 1250000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, INR |
| Brand/Manufacturer | text | Equipment manufacturer or brand name | GEA, Rieter, Hobart, Picanol, Trützschler, Tetra Pak, Oerlikon |
| Machine Category | enum | High-level category distinguishing textile from food processing | Textile Machinery, Food Processing Machinery |
| Machine Type | text | Specific type of machine within the category | Ring Spinning Machine, Rapier Loom, Meat Grinder, Industrial Mixer, Packaging Machine, Air-Jet Loom |
| Model Number | text | Manufacturer model or series designation | G 38, R 37, CookStar 1000, 4146, ComboGrind 1500/250 |
| Application | text (list) | Primary intended uses or industries served | Yarn Spinning, Fabric Weaving, Meat Processing, Dairy Processing, Baking, Beverage Filling |
| Processing Capacity | text | Throughput or production rate with units as stated by the seller | 60-65 lbs/min, 1500 kg/hr, 200 m/min, 1500 picks/min |
| Motor Power | text | Total installed motor power | 55 kW, 5 HP, 40 HP, 75 kW |
| Voltage | text | Input electrical voltage requirement | 208-230/460V, 380V, 400V, 480V |
| Phase | text | Electrical phase configuration | Single Phase, 3-Phase |
| Frequency | text (Hz) | Electrical supply frequency | 50, 60, 50/60 |
| Operating Speed | text | Primary operating speed metric relevant to the machine type (RPM, PPM, m/min) | 28000 RPM, 1500 PPM, 200 m/min, 215 RPM |
| Working Width | number (mm) | Maximum working or processing width for textile machinery | 1900, 2200, 3400, 3800 |
| Spindle/Position Count | number | Number of spindles, spinning positions, or processing stations | 600, 1824, 2016 |
| Hopper/Bowl Capacity | text | Capacity of feed hopper, mixing bowl, or holding tank | 800L, 1500L, 180 liters, 150 lbs |
| Machine Dimensions (L x W x H) | text (mm) | Overall machine footprint and height | 2500 x 1914 x 1952 mm, 6200 x 2100 x 3500 mm |
| Machine Weight | number (kg) | Total weight of the machine without packaging | 1900, 350, 12000, 45000 |
| Material of Construction | text | Primary construction material for food-contact or structural parts | Stainless Steel, Cast Iron, Alloy Steel, Hot Tin Dipped |
| Automation Level | enum | Degree of automation and control | Manual, Semi-Automatic, Fully Automatic, CNC Controlled |
| Control System | text | Type of control interface or automation system | PLC, HMI Touchscreen, Computerized, Mechanical |
| Number of Motors | number | Count of separate drive motors in the system | 1, 2, 3, 5 |
| Feed Mechanism | text | How material is loaded or fed into the machine | Gravity Feed, Conveyor Belt, Hopper with Agitator, Creel, Automatic Bobbin Changer |
| Cutting/Tooling Configuration | text | Tooling setup such as grinding plates, knife count, or loom shedding type | 3-piece knife set, 250 mm cutting set, Cam shedding, Dobby, Jacquard |
| Yarn/Material Compatibility | text (list) | Types of raw material the machine can handle | Cotton, Polyester, Wool, Beef, Pork, Poultry, Synthetic Filament |
| Output Product Form | text | Form of the finished or intermediate product | Yarn on bobbin, Woven fabric, Ground meat, Packaged liquid, Nonwoven web |
| Noise Level | number (dB) | Sound pressure level during operation | 78, 82, 85, 92 |
| Safety Features | text (list) | Built-in safety mechanisms | Emergency Stop, Interlocked Guards, Overload Protection, Automatic Thread Break Detection |
| Certifications | text (list) | Compliance and quality certifications | CE, ISO 9001, UL, ATEX, FDA, GMP, HACCP, 3-A Sanitary |
| Utility Requirements | text | Additional utilities required beyond electricity | Compressed Air 6 bar, Water Supply, Steam, Chilled Water |
| Country of Origin | text | Country where the machine is manufactured | Germany, Switzerland, Italy, China, India, USA |
| Warranty Period | text | Manufacturer warranty duration | 12 months, 24 months, 1 year parts and labor |
| IP Rating | text | Ingress protection rating for electrical enclosure | IP54, IP55, IP65 |
| Shipping Weight | number (kg) | Gross weight including packaging for transport | 2100, 500, 14000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (ISO, CE, FDA/GMP for food, textile machinery classification) | [GEA Food Processing](https://www.gea.com/en/products/meat-preparation/grinding/gea-combogrind-industrial-meat-grinder/), [Rieter Spinning](https://www.rieter.com/products/systems), [Hobart Food Equipment](https://www.hobartcorp.com/products/food-prep/meat-room/choppers-grinders), [Vietextile Weaving Machines](https://vietextile.com/en/industrial-weaving-machine/) |
