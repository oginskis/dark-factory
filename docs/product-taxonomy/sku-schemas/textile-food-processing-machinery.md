# SKU Schema: Textile & Food Processing Machinery

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.textile_food_processing_machinery`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | GEA-CG1500, 4146-SS, R37-600, LMW-LK64 |
| Product Name | text | Full product name including key specs such as machine type, model, and capacity | GEA ComboGrind 1500/250 Industrial Meat Grinder, Rieter R 37 Rotor Spinning Machine 600 Positions |
| URL | text | Direct link to the product page | https://example.com/product/combogrind-1500 |
| Price | number | Numeric price per unit excluding currency symbol | 85000, 245000, 1250000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, INR |
| Machine Category | enum | High-level category distinguishing textile from food processing | Textile Machinery, Food Processing Machinery |
| Machine Type | text | Specific type of machine within the category | Ring Spinning Machine, Rapier Loom, Meat Grinder, Industrial Mixer, Packaging Machine, Air-Jet Loom |
| Model Number | text | Manufacturer model or series designation | G 38, R 37, CookStar 1000, 4146, ComboGrind 1500/250 |
| Material of Construction | text | Primary construction material for food-contact or structural parts | Stainless Steel, Cast Iron, Alloy Steel, Hot Tin Dipped |
| Yarn/Material Compatibility | text (list) | Types of raw material the machine can handle | Cotton, Polyester, Wool, Beef, Pork, Poultry, Synthetic Filament |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Output Product Form | text | Form of the finished or intermediate product | Yarn on bobbin, Woven fabric, Ground meat, Packaged liquid, Nonwoven web |
| Country of Origin | text | Country where the machine is manufactured | Germany, Switzerland, Italy, China, India, USA |
| Application | text (list) | Primary intended uses or industries served | Yarn Spinning, Fabric Weaving, Meat Processing, Dairy Processing, Baking, Beverage Filling |
| Motor Power | text | Total installed motor power | 55 kW, 5 HP, 40 HP, 75 kW |
| Phase | text | Electrical phase configuration | Single Phase, 3-Phase |
| Frequency | text (Hz) | Electrical supply frequency | 50, 60, 50/60 |
| Operating Speed | text | Primary operating speed metric relevant to the machine type (RPM, PPM, m/min) | 28000 RPM, 1500 PPM, 200 m/min, 215 RPM |
| Working Width | number (mm) | Maximum working or processing width for textile machinery | 1900, 2200, 3400, 3800 |
| Machine Dimensions (L x W x H) | text (mm) | Overall machine footprint and height | 2500 x 1914 x 1952 mm, 6200 x 2100 x 3500 mm |
| Automation Level | enum | Degree of automation and control | Manual, Semi-Automatic, Fully Automatic, CNC Controlled |
| Control System | text | Type of control interface or automation system | PLC, HMI Touchscreen, Computerized, Mechanical |
| Number of Motors | number | Count of separate drive motors in the system | 1, 2, 3, 5 |
| Feed Mechanism | text | How material is loaded or fed into the machine | Gravity Feed, Conveyor Belt, Hopper with Agitator, Creel, Automatic Bobbin Changer |
| Cutting/Tooling Configuration | text | Tooling setup such as grinding plates, knife count, or loom shedding type | 3-piece knife set, 250 mm cutting set, Cam shedding, Dobby, Jacquard |
| Noise Level | number (dB) | Sound pressure level during operation | 78, 82, 85, 92 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (ISO, CE, FDA/GMP for food, textile machinery classification) | [GEA Food Processing](https://www.gea.com/en/products/meat-preparation/grinding/gea-combogrind-industrial-meat-grinder/), [Rieter Spinning](https://www.rieter.com/products/systems), [Hobart Food Equipment](https://www.hobartcorp.com/products/food-prep/meat-room/choppers-grinders), [Vietextile Weaving Machines](https://vietextile.com/en/industrial-weaving-machine/) |
