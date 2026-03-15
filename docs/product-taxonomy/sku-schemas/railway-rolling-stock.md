# SKU Schema: Railway Rolling Stock

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.railway_rolling_stock`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or catalog product identifier | EMD-SD70ACE, STAD-FLIRT3-3C, NS-BXC-60P |
| Product Name | text | Full product designation including manufacturer, model, and variant | EMD SD70ACe Diesel-Electric Locomotive, Stadler FLIRT 3 Three-Car EMU, Norfolk Southern 60ft Plate F Boxcar |
| URL | text | Direct link to the product or specification page | https://example.com/locomotives/sd70ace |
| Price | number | Numeric price or lease rate per unit excluding currency symbol | 2500000, 5800000, 125000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, JPY |
| Rolling Stock Type | enum | Primary classification of the vehicle | Diesel Locomotive, Electric Locomotive, Electric Multiple Unit, Diesel Multiple Unit, Passenger Coach, Freight Wagon, Metro Car, Light Rail Vehicle, Shunting Locomotive |
| Freight Car Type | enum | Specific type for freight wagons (if applicable) | Boxcar, Covered Hopper, Open Hopper, Gondola, Flat Car, Tank Car, Refrigerator Car, Center-Beam, Intermodal Well Car, Coil Car, Autorack |
| Traction Motor Type | text | Type and model of traction motors | GM A3432 AC, CRRC Permanent Magnet Synchronous |
| Bogie Type | text | Bogie or truck model designation | HTC-RII, Flexifloat, Y25, SG-3 |
| Country of Origin | text | Country where the vehicle was manufactured | USA, Switzerland, Germany, France, China, India, Japan |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Manufacturer | text | Rolling stock manufacturer or builder name | ProgressRail/EMD, Stadler, Alstom, Siemens Mobility, CRRC, Wabtec/GE, Bombardier, National Steel Car |
| Model/Series | text | Manufacturer model name or product series | SD70ACe, FLIRT 3, Traxx, Vectron, ES44AC, Coradia iLint |
| Track Gauge | number (mm) | Track gauge the vehicle is designed for | 1000, 1067, 1435, 1520, 1668 |
| Number of Axles | number | Total axle count across all bogies | 4, 6, 8 |
| Axle Configuration | text | UIC or AAR wheel arrangement notation | Co-Co, Bo-Bo, C-C, 1A2 2 2Bo |
| Traction Power | number (kW) | Total rated traction motor output power | 3000, 3940, 5280 |
| Horsepower | number (hp) | Rated engine or motor power in horsepower (primarily for diesel) | 3000, 4300, 4400 |
| Tractive Effort Starting | number (lb) | Maximum tractive effort at standstill | 148000, 191000, 200000 |
| Tractive Effort Continuous | number (lb) | Continuous rated tractive effort | 109000, 155000, 175000 |
| Maximum Speed | number (km/h) | Maximum certified operating speed | 70, 120, 160, 200, 320 |
| Width | number (m) | Maximum body width | 2.88, 3.05, 3.26 |
| Height | number (m) | Maximum height from rail to roof | 4.12, 4.27, 4.52 |
| Axle Load | number (t) | Maximum weight per axle | 12.5, 18, 22.5, 32.5 |
| Load Limit | number (lb) | Maximum payload weight for freight cars | 182500, 209500, 222400, 223500 |
| Number of Cars | number | Number of cars in a fixed-formation trainset | 2, 3, 4, 6, 8 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 sources plus industry standards (AAR, UIC, TSI, EN standards) | [ProgressRail EMD](https://www.thedieselshop.us/Data%20EMD%20SD70ACe.HTML), [Stadler Rail](https://www.stadlerrail.com/en/solutions/rolling-stock), [Norfolk Southern Railcar Guide](https://www.norfolksouthern.com/en/ship-by-rail/shipping-tools/equipment/railcar-guide), [locomotive-specs.com](https://locomotive-specs.com/train/stadler/flirt-3-38-15kv) |
