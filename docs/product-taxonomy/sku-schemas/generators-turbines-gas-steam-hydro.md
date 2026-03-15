# SKU Schema: Generators & Turbines (Gas, Steam, Hydro)

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.generators_turbines`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | SGT-800-62, CAT-C32-1100, C2750D6E, SST-800 |
| Product Name | product_name | text | Full product name including model series and power rating | Siemens SGT-800 62 MW Gas Turbine, Caterpillar C32 1100 kW Diesel Generator Set, Cummins C2750D6E Centum Series |
| URL | url | text | Direct link to the product page | https://www.siemens-energy.com/us/en/home/products-services/product/sgt-800.html |
| Price | price | number | Numeric price per unit, excluding currency symbol | 85000, 210000, 5000000 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Equipment Type | equipment_type | enum | Primary classification of the power generation equipment | Gas turbine, Steam turbine, Diesel generator set, Gas generator set, Hydro turbine |
| Power Rating Type | power_rating_type | enum | Operating duty classification | Standby, Prime, Continuous, Base load, Peak |
| Fuel Type | fuel_type | text (list) | Compatible fuel sources | Natural gas, Diesel No. 2, Dual fuel, Heavy fuel oil, Biogas, Hydrogen blend, Steam |
| Cooling Type | cooling_type | text | Primary cooling or heat rejection method | Radiator, Air-to-air aftercooler, Water-cooled, Condensing |
| Enclosure Type | enclosure_type | text | Housing or packaging configuration | Open skid, Weather-protective enclosure, Sound-attenuated enclosure, Indoor package |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the unit is manufactured or assembled | USA, Germany, UK, Japan, India, China |
| Manufacturer | manufacturer | text | OEM name | Siemens Energy, Caterpillar, Cummins, GE Vernova, Mitsubishi Power, MAN Energy Solutions |
| Rated Power Output | rated_power_output | number (kW) | Nameplate electrical power output at rated conditions | 1100, 2750, 45000, 62000, 593000 |
| Rated Power kVA | rated_power_kva | number (kVA) | Apparent power rating for generator sets | 1375, 3438, 56250, 77500 |
| Electrical Efficiency | electrical_efficiency | number (%) | Net electrical efficiency at rated load (LHV basis for turbines) | 35.0, 38.5, 41.1, 44.0 |
| Heat Rate | heat_rate | number (kJ/kWh) | Thermal energy input per unit of electrical output | 8759, 9381, 10200, 11500 |
| Exhaust Temperature | exhaust_temperature | number (C) | Flue gas or exhaust steam temperature at turbine outlet | 340, 480, 560, 596 |
| Exhaust Mass Flow | exhaust_mass_flow | number (kg/s) | Mass flow rate of exhaust gas | 5.2, 18.0, 115.1, 135.5 |
| Inlet Pressure | inlet_pressure | number (bar) | Inlet steam pressure for steam turbines | 30, 103, 140, 165, 180 |
| Inlet Temperature | inlet_temperature | number (C) | Inlet steam temperature for steam turbines | 400, 540, 565 |
| Pressure Ratio | pressure_ratio | text | Compressor pressure ratio for gas turbines | 14.0:1, 18.3:1, 22.0:1, 24.0:1 |
| Speed | speed | number (rpm) | Rotational speed of the turbine or engine shaft | 1500, 1800, 3000, 3600, 6600, 13300 |
| Frequency | frequency | text (Hz) | Output electrical frequency | 50, 60, 50/60 |
| Number of Cylinders | number_of_cylinders | number | Cylinder count for reciprocating engine generator sets | 6, 12, 16 |
| Displacement | displacement | number (L) | Engine displacement for reciprocating generator sets | 8.3, 32.1, 51.8, 69.1, 95.3 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus ISO 8528 and IEC standards | [Siemens Energy Gas Turbines](https://www.siemens-energy.com/us/en/home/products-services/product-offerings/gas-turbines.html), [Siemens Energy Steam Turbines](https://www.siemens-energy.com/global/en/home/products-services/product/industrial-steam-turbines.html), [Caterpillar Generators](https://powergenenterprises.com/cat-generator-guide-models-specs-pricing-2026/), [Cummins QSK95](https://www.cummins.com/generators/qsk95) |
