# SKU Schema: Batteries & Grid-Scale Energy Storage

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.batteries_grid_storage`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | MGPK-2XL, EnerC-306-4MWH, MC-CUBE-T-6432 |
| Product Name | product_name | text | Full product name including model and capacity designation | Tesla Megapack 2XL, CATL EnerC+ 306 4MWh Container, BYD MC Cube-T 6.4 MWh |
| URL | url | text | Direct link to the product page | https://www.tesla.com/megapack |
| Price | price | number | Numeric price per unit or per kWh, excluding currency symbol | 1200000, 850000, 180 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, AUD |
| Cooling Type | cooling_type | text | Thermal management method | Liquid cooling, Air cooling, Immersion cooling |
| Enclosure Type | enclosure_type | text | Physical form factor of the system | 20-ft container, 40-ft container, Outdoor cabinet, Rack |
| Country of Origin | country_of_origin | text | Country where the system is manufactured or assembled | China, USA, Germany, South Korea, Australia |
| Rated Energy Capacity | rated_energy_capacity | number (kWh) | Usable AC energy storage capacity per unit | 372.7, 3720, 4073, 5000, 6432 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Manufacturer | manufacturer | text | System integrator or battery OEM name | Tesla, CATL, BYD, Fluence, Sungrow, Samsung SDI |
| Rated Power | rated_power | number (kW) | Maximum continuous AC discharge power | 500, 1000, 1860, 2500 |
| Battery Chemistry | battery_chemistry | text | Electrochemical cell type | LFP, NMC, LTO, Sodium-ion, Vanadium redox flow |
| Round-Trip Efficiency | round-trip_efficiency | number (%) | Ratio of energy discharged to energy charged (AC-to-AC) | 85, 88, 91, 93.7 |
| Cycle Life | cycle_life | number | Number of charge-discharge cycles to 80% retained capacity | 6000, 8000, 10000, 12000 |
| C-Rate | c-rate | text | Ratio of charge/discharge power to energy capacity | 0.25C, 0.5C, 1C, 2C |
| Depth of Discharge | depth_of_discharge | number (%) | Usable percentage of total installed capacity | 90, 95, 100 |
| Duration | duration | number (h) | Rated discharge duration at maximum power | 1, 2, 4, 8 |
| Dimensions | dimensions | text (mm) | External length x width x height of the enclosure | 6058 x 2438 x 2896, 8534 x 2438 x 2896 |
| IP Rating | ip_rating | text | Ingress protection rating of the enclosure | IP55, IP66, IP67 |
| Operating Temperature Range | operating_temperature_range | text | Ambient temperature for normal operation | -30 to +55 C, -20 to +50 C, -10 to +50 C |
| Communication Protocols | communication_protocols | text (list) | Supported monitoring and control interfaces | Modbus TCP, CAN bus, DNP3, IEC 61850, MQTT |
| System Configuration | system_configuration | text | Cell-to-module-to-rack topology string | 1P416S, 10P416S, 2P208S |
| Fire Suppression System | fire_suppression_system | text | Integrated fire detection and suppression type | Aerosol, Water mist, Gas-based, Liquid cooling with detection |
| Certifications | certifications | text (list) | Safety and grid compliance standards | UL 9540, UL 9540A, IEC 62619, IEC 62477, UN38.3, CE |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus UL 9540 and IEC standards | [Tesla Megapack](https://www.tesla.com/megapack), [CATL EnerOne/EnerC](https://www.evlithium.com/energy-storage-system-solutions/catl-outdoor-indoor-enerone-battery.html), [BYD MC Cube-T](https://cnevpost.com/2024/04/11/byd-launches-energy-storage-mc-cube-t/), [FlexPower BESS Specs](https://flex-power.energy/school-of-flex/technical-specifications-battery-storage-bess/) |
