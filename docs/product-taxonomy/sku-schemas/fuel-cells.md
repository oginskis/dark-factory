# SKU Schema: Fuel Cells

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | BES-6.5-325, FCgen-HPS-140, GS-MW-1000 |
| Product Name | text | Full product name including model, technology type, and power rating | Bloom Energy Server 6.5 325 kW, Ballard FCgen-HPS 140 kW Stack, Plug Power GenSure MW-Scale 1 MW |
| URL | text | Direct link to the product page | https://www.bloomenergy.com/technology/ |
| Price | number | Numeric price per unit or per kW, excluding currency symbol | 750000, 1200000, 5000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Manufacturer | text | Fuel cell OEM or system integrator name | Bloom Energy, Ballard Power Systems, Plug Power, Ceres Power, FuelCell Energy, Hyzon Motors |
| Fuel Cell Type | enum | Electrochemical technology classification | SOFC, PEM, PAFC, MCFC, AFC, DMFC |
| Rated Power Output | number (kW) | Nameplate AC or DC electrical output per unit or stack | 0.4, 3.3, 93, 140, 200, 325, 1000 |
| Electrical Efficiency | number (%) | Net electrical conversion efficiency (LHV basis) | 42, 50, 53, 60, 65 |
| CHP Efficiency | number (%) | Combined heat and power efficiency when waste heat is recovered | 80, 85, 90 |
| Fuel Type | text (list) | Compatible hydrogen or hydrocarbon fuel sources | Pure hydrogen, Natural gas, Biogas, Methanol, Ammonia, Hydrogen blend |
| Output Voltage | number (V) | Electrical output voltage (DC for stacks, AC for systems) | 48, 187, 202, 400, 480 |
| Grid Frequency | text (Hz) | AC output frequency for grid-connected systems | 50, 60, 50/60 |
| Cooling Method | enum | Thermal management approach | Air cooled, Liquid cooled, Self-cooling (SOFC) |
| Operating Temperature | text | Internal cell or stack operating temperature range | 60-95 C, 120-200 C, 600-1000 C |
| Ambient Temperature Range | text | Allowable ambient temperature for installation | -28 to +52 C, -40 to +52 C, -20 to +50 C |
| Dimensions | text (mm) | Overall length x width x height of the unit or stack | 5690 x 2130 x 2060, 500 x 300 x 400 |
| Weight | number (kg) | Total mass of the complete unit or stack | 25, 68, 2500, 9100 |
| Power Density Volumetric | number (kW/L) | Power output per unit volume of the stack | 3.1, 4.3, 5.0 |
| Power Density Gravimetric | number (kW/kg) | Power output per unit mass of the stack | 0.5, 1.0, 2.1 |
| Hydrogen Consumption | number (kg/h) | Hydrogen fuel consumption at rated output | 0.06, 1.2, 5.0, 15.0 |
| Water Consumption | text | Water usage during normal operation | Zero, Minimal startup only, 0.5 L/kWh |
| Noise Level | number (dB(A)) | Sound pressure level at specified distance | 55, 60, 65, 72 |
| Emissions CO2 | number (g/kWh) | Carbon dioxide emissions per unit of electricity (zero for pure hydrogen) | 0, 280, 350, 400 |
| Emissions NOx | text (ppm) | Nitrogen oxide emissions (near zero for most fuel cells) | Less than 0.01, Less than 0.5, Negligible |
| Startup Time | text | Time from cold start to rated power | 30 seconds, 5 minutes, 2 hours, 24 hours |
| Response Time | text | Time to ramp between partial and full load | Milliseconds, 1 second, 5 seconds, 30 seconds |
| Durability | number (h) | Expected stack operating life before replacement | 10000, 25000, 40000, 80000 |
| Degradation Rate | number (%/1000h) | Power output decline rate over operating life | 0.2, 0.5, 1.0, 2.0 |
| Availability | number (%) | System uptime guarantee or demonstrated reliability | 95, 98, 99.5, 99.998 |
| Certifications | text (list) | Safety, performance, and emissions standards compliance | UL 2196, UL 1741, IEC 62282, CSA FC 1, CE, CARB |
| Installation Type | enum | Deployment configuration | Indoor, Outdoor, Rooftop, Skid-mounted, Containerised |
| Application | text (list) | Primary intended use cases | Baseload power, Backup power, Material handling, Marine propulsion, Data centre, Microgrid, CHP |
| Modularity | text | System scaling approach and minimum increment | 325 kW blocks, Stackable modules, Single unit |
| Design Life | number (years) | Expected operational lifespan of the complete system | 10, 15, 20, 25 |
| Country of Origin | text | Country where the system or stack is manufactured | USA, Canada, UK, South Korea, Japan, Germany |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus IEC 62282 fuel cell standards | [Bloom Energy](https://www.bloomenergy.com/technology/), [Ballard Power FCgen](https://www.ballard.com/fcgen/), [Plug Power GenSure](https://www.plugpower.com/fuel-cell-power/gensure-stationary-power-systems/gensure-mw-scale-power/), [FuelCell Energy - Wikipedia Bloom Energy Server](https://en.wikipedia.org/wiki/Bloom_Energy_Server) |
