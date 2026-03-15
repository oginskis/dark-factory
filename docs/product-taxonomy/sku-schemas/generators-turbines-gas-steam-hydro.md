# SKU Schema: Generators & Turbines (Gas, Steam, Hydro)

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.generators_turbines`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | SGT-800-62, CAT-C32-1100, C2750D6E, SST-800 |
| Product Name | text | Full product name including model series and power rating | Siemens SGT-800 62 MW Gas Turbine, Caterpillar C32 1100 kW Diesel Generator Set, Cummins C2750D6E Centum Series |
| URL | text | Direct link to the product page | https://www.siemens-energy.com/us/en/home/products-services/product/sgt-800.html |
| Price | number | Numeric price per unit, excluding currency symbol | 85000, 210000, 5000000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Equipment Type | enum | Primary classification of the power generation equipment | Gas turbine, Steam turbine, Diesel generator set, Gas generator set, Hydro turbine |
| Power Rating Type | enum | Operating duty classification | Standby, Prime, Continuous, Base load, Peak |
| Fuel Type | text (list) | Compatible fuel sources | Natural gas, Diesel No. 2, Dual fuel, Heavy fuel oil, Biogas, Hydrogen blend, Steam |
| Cooling Type | text | Primary cooling or heat rejection method | Radiator, Air-to-air aftercooler, Water-cooled, Condensing |
| Enclosure Type | text | Housing or packaging configuration | Open skid, Weather-protective enclosure, Sound-attenuated enclosure, Indoor package |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the unit is manufactured or assembled | USA, Germany, UK, Japan, India, China |
| Manufacturer | text | OEM name | Siemens Energy, Caterpillar, Cummins, GE Vernova, Mitsubishi Power, MAN Energy Solutions |
| Rated Power Output | number (kW) | Nameplate electrical power output at rated conditions | 1100, 2750, 45000, 62000, 593000 |
| Rated Power kVA | number (kVA) | Apparent power rating for generator sets | 1375, 3438, 56250, 77500 |
| Electrical Efficiency | number (%) | Net electrical efficiency at rated load (LHV basis for turbines) | 35.0, 38.5, 41.1, 44.0 |
| Heat Rate | number (kJ/kWh) | Thermal energy input per unit of electrical output | 8759, 9381, 10200, 11500 |
| Exhaust Temperature | number (C) | Flue gas or exhaust steam temperature at turbine outlet | 340, 480, 560, 596 |
| Exhaust Mass Flow | number (kg/s) | Mass flow rate of exhaust gas | 5.2, 18.0, 115.1, 135.5 |
| Inlet Pressure | number (bar) | Inlet steam pressure for steam turbines | 30, 103, 140, 165, 180 |
| Inlet Temperature | number (C) | Inlet steam temperature for steam turbines | 400, 540, 565 |
| Pressure Ratio | text | Compressor pressure ratio for gas turbines | 14.0:1, 18.3:1, 22.0:1, 24.0:1 |
| Speed | number (rpm) | Rotational speed of the turbine or engine shaft | 1500, 1800, 3000, 3600, 6600, 13300 |
| Frequency | text (Hz) | Output electrical frequency | 50, 60, 50/60 |
| Number of Cylinders | number | Cylinder count for reciprocating engine generator sets | 6, 12, 16 |
| Displacement | number (L) | Engine displacement for reciprocating generator sets | 8.3, 32.1, 51.8, 69.1, 95.3 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus ISO 8528 and IEC standards | [Siemens Energy Gas Turbines](https://www.siemens-energy.com/us/en/home/products-services/product-offerings/gas-turbines.html), [Siemens Energy Steam Turbines](https://www.siemens-energy.com/global/en/home/products-services/product/industrial-steam-turbines.html), [Caterpillar Generators](https://powergenenterprises.com/cat-generator-guide-models-specs-pricing-2026/), [Cummins QSK95](https://www.cummins.com/generators/qsk95) |
