# SKU Schema: Fuel Cells

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.fuel_cells`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | BES-6.5-325, FCgen-HPS-140, GS-MW-1000 |
| Product Name | product_name | text | Full product name including model, technology type, and power rating | Bloom Energy Server 6.5 325 kW, Ballard FCgen-HPS 140 kW Stack, Plug Power GenSure MW-Scale 1 MW |
| URL | url | text | Direct link to the product page | https://www.bloomenergy.com/technology/ |
| Price | price | number | Numeric price per unit or per kW, excluding currency symbol | 750000, 1200000, 5000 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Fuel Cell Type | fuel_cell_type | enum | Electrochemical technology classification | SOFC, PEM, PAFC, MCFC, AFC, DMFC |
| Fuel Type | fuel_type | text (list) | Compatible hydrogen or hydrocarbon fuel sources | Pure hydrogen, Natural gas, Biogas, Methanol, Ammonia, Hydrogen blend |
| Installation Type | installation_type | enum | Deployment configuration | Indoor, Outdoor, Rooftop, Skid-mounted, Containerised |
| Country of Origin | country_of_origin | text | Country where the system or stack is manufactured | USA, Canada, UK, South Korea, Japan, Germany |
| Output Voltage | output_voltage | number (V) | Electrical output voltage (DC for stacks, AC for systems) | 48, 187, 202, 400, 480 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Manufacturer | manufacturer | text | Fuel cell OEM or system integrator name | Bloom Energy, Ballard Power Systems, Plug Power, Ceres Power, FuelCell Energy, Hyzon Motors |
| Rated Power Output | rated_power_output | number (kW) | Nameplate AC or DC electrical output per unit or stack | 0.4, 3.3, 93, 140, 200, 325, 1000 |
| Electrical Efficiency | electrical_efficiency | number (%) | Net electrical conversion efficiency (LHV basis) | 42, 50, 53, 60, 65 |
| CHP Efficiency | chp_efficiency | number (%) | Combined heat and power efficiency when waste heat is recovered | 80, 85, 90 |
| Grid Frequency | grid_frequency | text (Hz) | AC output frequency for grid-connected systems | 50, 60, 50/60 |
| Cooling Method | cooling_method | enum | Thermal management approach | Air cooled, Liquid cooled, Self-cooling (SOFC) |
| Operating Temperature | operating_temperature | text | Internal cell or stack operating temperature range | 60-95 C, 120-200 C, 600-1000 C |
| Ambient Temperature Range | ambient_temperature_range | text | Allowable ambient temperature for installation | -28 to +52 C, -40 to +52 C, -20 to +50 C |
| Dimensions | dimensions | text (mm) | Overall length x width x height of the unit or stack | 5690 x 2130 x 2060, 500 x 300 x 400 |
| Power Density Volumetric | power_density_volumetric | number (kW/L) | Power output per unit volume of the stack | 3.1, 4.3, 5.0 |
| Power Density Gravimetric | power_density_gravimetric | number (kW/kg) | Power output per unit mass of the stack | 0.5, 1.0, 2.1 |
| Hydrogen Consumption | hydrogen_consumption | number (kg/h) | Hydrogen fuel consumption at rated output | 0.06, 1.2, 5.0, 15.0 |
| Water Consumption | water_consumption | text | Water usage during normal operation | Zero, Minimal startup only, 0.5 L/kWh |
| Noise Level | noise_level | number (dB(A)) | Sound pressure level at specified distance | 55, 60, 65, 72 |
| Emissions CO2 | emissions_co2 | number (g/kWh) | Carbon dioxide emissions per unit of electricity (zero for pure hydrogen) | 0, 280, 350, 400 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus IEC 62282 fuel cell standards | [Bloom Energy](https://www.bloomenergy.com/technology/), [Ballard Power FCgen](https://www.ballard.com/fcgen/), [Plug Power GenSure](https://www.plugpower.com/fuel-cell-power/gensure-stationary-power-systems/gensure-mw-scale-power/), [FuelCell Energy - Wikipedia Bloom Energy Server](https://en.wikipedia.org/wiki/Bloom_Energy_Server) |
