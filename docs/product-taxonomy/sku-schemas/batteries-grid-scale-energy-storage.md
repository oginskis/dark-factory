# SKU Schema: Batteries & Grid-Scale Energy Storage

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | MGPK-2XL, EnerC-306-4MWH, MC-CUBE-T-6432 |
| Product Name | text | Full product name including model and capacity designation | Tesla Megapack 2XL, CATL EnerC+ 306 4MWh Container, BYD MC Cube-T 6.4 MWh |
| URL | text | Direct link to the product page | https://www.tesla.com/megapack |
| Price | number | Numeric price per unit or per kWh, excluding currency symbol | 1200000, 850000, 180 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, AUD |
| Manufacturer | text | System integrator or battery OEM name | Tesla, CATL, BYD, Fluence, Sungrow, Samsung SDI |
| Rated Energy Capacity | number (kWh) | Usable AC energy storage capacity per unit | 372.7, 3720, 4073, 5000, 6432 |
| Rated Power | number (kW) | Maximum continuous AC discharge power | 500, 1000, 1860, 2500 |
| Battery Chemistry | text | Electrochemical cell type | LFP, NMC, LTO, Sodium-ion, Vanadium redox flow |
| Cell Capacity | number (Ah) | Rated capacity of individual battery cells | 280, 302, 306, 314 |
| Nominal Voltage | number (V) | System-level nominal DC bus voltage | 1200, 1331.2, 1500 |
| Voltage Range | text (V) | Operating DC voltage window | 800-1400, 1040-1500, 960-1500 |
| Round-Trip Efficiency | number (%) | Ratio of energy discharged to energy charged (AC-to-AC) | 85, 88, 91, 93.7 |
| Cycle Life | number | Number of charge-discharge cycles to 80% retained capacity | 6000, 8000, 10000, 12000 |
| C-Rate | text | Ratio of charge/discharge power to energy capacity | 0.25C, 0.5C, 1C, 2C |
| Depth of Discharge | number (%) | Usable percentage of total installed capacity | 90, 95, 100 |
| Duration | number (h) | Rated discharge duration at maximum power | 1, 2, 4, 8 |
| Dimensions | text (mm) | External length x width x height of the enclosure | 6058 x 2438 x 2896, 8534 x 2438 x 2896 |
| Weight | number (kg) | Total mass of the unit including batteries and enclosure | 3500, 35000, 38000, 42000 |
| Cooling Type | text | Thermal management method | Liquid cooling, Air cooling, Immersion cooling |
| IP Rating | text | Ingress protection rating of the enclosure | IP55, IP66, IP67 |
| Operating Temperature Range | text | Ambient temperature for normal operation | -30 to +55 C, -20 to +50 C, -10 to +50 C |
| Communication Protocols | text (list) | Supported monitoring and control interfaces | Modbus TCP, CAN bus, DNP3, IEC 61850, MQTT |
| System Configuration | text | Cell-to-module-to-rack topology string | 1P416S, 10P416S, 2P208S |
| Fire Suppression System | text | Integrated fire detection and suppression type | Aerosol, Water mist, Gas-based, Liquid cooling with detection |
| Enclosure Type | text | Physical form factor of the system | 20-ft container, 40-ft container, Outdoor cabinet, Rack |
| Certifications | text (list) | Safety and grid compliance standards | UL 9540, UL 9540A, IEC 62619, IEC 62477, UN38.3, CE |
| Grid Connection | text | AC coupling method and inverter topology | Integrated inverter, External PCS, DC-coupled |
| Response Time | text (ms) | Time from command to full power delivery | Less than 100, Less than 200, Less than 500 |
| Degradation Rate | number (%/year) | Annual capacity loss under warranted conditions | 1.5, 2.0, 2.5, 3.0 |
| Design Life | number (years) | Expected operational lifespan of the system | 15, 20, 25 |
| Augmentation Strategy | text | Approach to maintaining capacity over time | Modular rack addition, Cell replacement, Oversizing |
| Corrosion Protection | text | Enclosure corrosion resistance classification | C3, C4, C5 |
| Energy Density | number (kWh/m2) | Usable energy per unit of ground footprint area | 200, 250, 270, 300 |
| Warranty Period | number (years) | Manufacturer performance warranty duration | 10, 12, 15, 20 |
| Country of Origin | text | Country where the system is manufactured or assembled | China, USA, Germany, South Korea, Australia |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus UL 9540 and IEC standards | [Tesla Megapack](https://www.tesla.com/megapack), [CATL EnerOne/EnerC](https://www.evlithium.com/energy-storage-system-solutions/catl-outdoor-indoor-enerone-battery.html), [BYD MC Cube-T](https://cnevpost.com/2024/04/11/byd-launches-energy-storage-mc-cube-t/), [FlexPower BESS Specs](https://flex-power.energy/school-of-flex/technical-specifications-battery-storage-bess/) |
