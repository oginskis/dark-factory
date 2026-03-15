# SKU Schema: Generators & Turbines (Gas, Steam, Hydro)

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | SGT-800-62, CAT-C32-1100, C2750D6E, SST-800 |
| Product Name | text | Full product name including model series and power rating | Siemens SGT-800 62 MW Gas Turbine, Caterpillar C32 1100 kW Diesel Generator Set, Cummins C2750D6E Centum Series |
| URL | text | Direct link to the product page | https://www.siemens-energy.com/us/en/home/products-services/product/sgt-800.html |
| Price | number | Numeric price per unit, excluding currency symbol | 85000, 210000, 5000000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Manufacturer | text | OEM name | Siemens Energy, Caterpillar, Cummins, GE Vernova, Mitsubishi Power, MAN Energy Solutions |
| Equipment Type | enum | Primary classification of the power generation equipment | Gas turbine, Steam turbine, Diesel generator set, Gas generator set, Hydro turbine |
| Rated Power Output | number (kW) | Nameplate electrical power output at rated conditions | 1100, 2750, 45000, 62000, 593000 |
| Rated Power kVA | number (kVA) | Apparent power rating for generator sets | 1375, 3438, 56250, 77500 |
| Power Rating Type | enum | Operating duty classification | Standby, Prime, Continuous, Base load, Peak |
| Electrical Efficiency | number (%) | Net electrical efficiency at rated load (LHV basis for turbines) | 35.0, 38.5, 41.1, 44.0 |
| Heat Rate | number (kJ/kWh) | Thermal energy input per unit of electrical output | 8759, 9381, 10200, 11500 |
| Fuel Type | text (list) | Compatible fuel sources | Natural gas, Diesel No. 2, Dual fuel, Heavy fuel oil, Biogas, Hydrogen blend, Steam |
| Exhaust Temperature | number (C) | Flue gas or exhaust steam temperature at turbine outlet | 340, 480, 560, 596 |
| Exhaust Mass Flow | number (kg/s) | Mass flow rate of exhaust gas | 5.2, 18.0, 115.1, 135.5 |
| Inlet Pressure | number (bar) | Inlet steam pressure for steam turbines | 30, 103, 140, 165, 180 |
| Inlet Temperature | number (C) | Inlet steam temperature for steam turbines | 400, 540, 565 |
| Pressure Ratio | text | Compressor pressure ratio for gas turbines | 14.0:1, 18.3:1, 22.0:1, 24.0:1 |
| Speed | number (rpm) | Rotational speed of the turbine or engine shaft | 1500, 1800, 3000, 3600, 6600, 13300 |
| Frequency | text (Hz) | Output electrical frequency | 50, 60, 50/60 |
| Voltage | number (V) | Generator output voltage | 380, 480, 4160, 11000, 13800 |
| Number of Cylinders | number | Cylinder count for reciprocating engine generator sets | 6, 12, 16 |
| Displacement | number (L) | Engine displacement for reciprocating generator sets | 8.3, 32.1, 51.8, 69.1, 95.3 |
| Emissions Tier | text | Regulatory emissions compliance level | EPA Tier 2, EPA Tier 4 Final, EU Stage V, Low NOx |
| NOx Emissions | text (ppmvd) | Nitrogen oxide emissions at rated load | 9, 15, 25, 50 |
| Dimensions | text (mm) | Overall length x width x height of the package or skid | 4500 x 2000 x 2500, 20800 x 7300 x 6600, 22000 x 4700 x 5300 |
| Weight | number (kg) | Total dry weight of the unit or package | 12000, 42000, 285000, 305000 |
| Cooling Type | text | Primary cooling or heat rejection method | Radiator, Air-to-air aftercooler, Water-cooled, Condensing |
| Fuel Consumption | number (L/h) | Fuel consumption at rated load for reciprocating engines | 55, 120, 280, 520 |
| Noise Level | number (dB(A)) | Sound pressure level at specified distance | 75, 85, 95, 105 |
| Control System | text | Integrated control panel or system designation | Caterpillar EMCP 4.4, Cummins PowerCommand, Siemens SPPA-T3000 |
| Enclosure Type | text | Housing or packaging configuration | Open skid, Weather-protective enclosure, Sound-attenuated enclosure, Indoor package |
| Start-up Time | text | Time from command to full load | 10 seconds, 5 minutes, 30 minutes, 2 hours |
| Maintenance Interval | number (h) | Operating hours between major overhauls | 8000, 30000, 50000, 60000 |
| Availability | number (%) | Guaranteed or fleet average technical uptime | 95, 97, 99.1 |
| Certifications | text (list) | Safety and performance standards compliance | ISO 8528, ISO 3046, IEC 60034, NFPA 110, CE, UL 2200, CSA |
| Application | text (list) | Primary intended use cases | Standby power, CHP, CCPP, Oil and gas, Marine, District heating, Industrial process |
| Country of Origin | text | Country where the unit is manufactured or assembled | USA, Germany, UK, Japan, India, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus ISO 8528 and IEC standards | [Siemens Energy Gas Turbines](https://www.siemens-energy.com/us/en/home/products-services/product-offerings/gas-turbines.html), [Siemens Energy Steam Turbines](https://www.siemens-energy.com/global/en/home/products-services/product/industrial-steam-turbines.html), [Caterpillar Generators](https://powergenenterprises.com/cat-generator-guide-models-specs-pricing-2026/), [Cummins QSK95](https://www.cummins.com/generators/qsk95) |
