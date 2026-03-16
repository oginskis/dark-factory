# SKU Schema: Textile & Food Processing Machinery

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.textile_food_processing_machinery`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | GEA-CG1500, 4146-SS, R37-600, LMW-LK64 |
| Product Name | product_name | text | — | Full product name including key specs such as machine type, model, and capacity | GEA ComboGrind 1500/250 Industrial Meat Grinder, Rieter R 37 Rotor Spinning Machine 600 Positions |
| URL | url | text | — | Direct link to the product page | https://example.com/product/combogrind-1500 |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 85000, 245000, 1250000 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CHF, INR |
| Machine Category | machine_category | enum | — | High-level category distinguishing textile from food processing | Textile Machinery, Food Processing Machinery |
| Machine Type | machine_type | text | — | Specific type of machine within the category | Ring Spinning Machine, Rapier Loom, Meat Grinder, Industrial Mixer, Packaging Machine, Air-Jet Loom |
| Model Number | model_number | text | — | Manufacturer model or series designation | G 38, R 37, CookStar 1000, 4146, ComboGrind 1500/250 |
| Material of Construction | material_of_construction | text | — | Primary construction material for food-contact or structural parts | Stainless Steel, Cast Iron, Alloy Steel, Hot Tin Dipped |
| Yarn/Material Compatibility | yarnmaterial_compatibility | text (list) | — | Types of raw material the machine can handle | Cotton, Polyester, Wool, Beef, Pork, Poultry, Synthetic Filament |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Output Product Form | output_product_form | text | — | Form of the finished or intermediate product | Yarn on bobbin, Woven fabric, Ground meat, Packaged liquid, Nonwoven web |
| Country of Origin | country_of_origin | text | — | Country where the machine is manufactured | Germany, Switzerland, Italy, China, India, USA |
| Application | application | text (list) | — | Primary intended uses or industries served | Yarn Spinning, Fabric Weaving, Meat Processing, Dairy Processing, Baking, Beverage Filling |
| Motor Power | motor_power | text | — | Total installed motor power | 55 kW, 5 HP, 40 HP, 75 kW |
| Phase | phase | text | — | Electrical phase configuration | Single Phase, 3-Phase |
| Frequency | frequency | text | Hz | Electrical supply frequency | 50, 60, 50/60 |
| Operating Speed | operating_speed | text | — | Primary operating speed metric relevant to the machine type (RPM, PPM, m/min) | 28000 RPM, 1500 PPM, 200 m/min, 215 RPM |
| Working Width | working_width | number | mm | Maximum working or processing width for textile machinery | 1900, 2200, 3400, 3800 |
| Machine Dimensions (L x W x H) | machine_dimensions_l_x_w_x_h | text | mm | Overall machine footprint and height | 2500 x 1914 x 1952 mm, 6200 x 2100 x 3500 mm |
| Automation Level | automation_level | enum | — | Degree of automation and control | Manual, Semi-Automatic, Fully Automatic, CNC Controlled |
| Control System | control_system | text | — | Type of control interface or automation system | PLC, HMI Touchscreen, Computerized, Mechanical |
| Number of Motors | number_of_motors | number | — | Count of separate drive motors in the system | 1, 2, 3, 5 |
| Feed Mechanism | feed_mechanism | text | — | How material is loaded or fed into the machine | Gravity Feed, Conveyor Belt, Hopper with Agitator, Creel, Automatic Bobbin Changer |
| Cutting/Tooling Configuration | cuttingtooling_configuration | text | — | Tooling setup such as grinding plates, knife count, or loom shedding type | 3-piece knife set, 250 mm cutting set, Cam shedding, Dobby, Jacquard |
| Noise Level | noise_level | number | dB | Sound pressure level during operation | 78, 82, 85, 92 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (ISO, CE, FDA/GMP for food, textile machinery classification) | [GEA Food Processing](https://www.gea.com/en/products/meat-preparation/grinding/gea-combogrind-industrial-meat-grinder/), [Rieter Spinning](https://www.rieter.com/products/systems), [Hobart Food Equipment](https://www.hobartcorp.com/products/food-prep/meat-room/choppers-grinders), [Vietextile Weaving Machines](https://vietextile.com/en/industrial-weaving-machine/) |
