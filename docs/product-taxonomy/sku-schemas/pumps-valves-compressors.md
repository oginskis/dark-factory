# SKU Schema: Pumps, Valves & Compressors

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.pumps_valves_compressors`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | GP200, GA55, KPH-85229, PCM600S |
| Product Name | product_name | text | — | Full product name including key specs such as type, brand, and model | Grundfos CR 32-2 Vertical Multistage Centrifugal Pump, Parker Hannifin GP200 Solenoid Valve, Atlas Copco GA 55 Rotary Screw Compressor |
| URL | url | text | — | Direct link to the product page | https://example.com/product/grundfos-cr-32-2 |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 125.00, 2500.00, 35000.00, 85000.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Type | product_type | enum | — | Primary equipment category | Centrifugal Pump, Positive Displacement Pump, Submersible Pump, Ball Valve, Gate Valve, Globe Valve, Check Valve, Butterfly Valve, Solenoid Valve, Control Valve, Reciprocating Compressor, Rotary Screw Compressor, Scroll Compressor, Diaphragm Pump |
| Model Number | model_number | text | — | Manufacturer model or part number | CR 32-2, GP200, GA 55 FF, KPH 85229 |
| Connection Type | connection_type | text | — | Pipe or port connection method | Threaded NPT, Flanged ANSI, Flanged DIN, Tri-Clamp, Welded, Compression |
| Body Material | body_material | text | — | Material of the pump casing, valve body, or compressor housing | Cast Iron, Stainless Steel 316, Bronze, Carbon Steel, Ductile Iron, PVDF, Hastelloy |
| Impeller/Trim Material | impellertrim_material | text | — | Material of the impeller (pumps) or trim (valves) | Stainless Steel 316, Bronze, Noryl, PTFE, Hastelloy C, Duplex |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Seal Type | seal_type | text | — | Primary shaft or body sealing method | Mechanical Seal, Packed Gland, O-Ring, PTFE Seat, Metal Seat, Lip Seal, Magnetic Drive |
| Country of Origin | country_of_origin | text | — | Country where the equipment was manufactured | Denmark, Germany, USA, UK, India, Japan, Sweden |
| Flow Rate | flow_rate | text | — | Maximum or rated volumetric flow rate with unit | 10.7 m3/h, 280 m3/h, 150 GPM, 1206 CFM |
| Head/Pressure Rating | headpressure_rating | text | — | Maximum operating pressure or pump head | 95 m, 10 bar, 150 PSI, 250 bar, ANSI Class 300 |
| Max Working Pressure | max_working_pressure | number | bar | Maximum allowable working pressure | 4, 10, 16, 25, 250 |
| Cv Flow Coefficient | cv_flow_coefficient | number | — | Valve flow coefficient for sizing (valves only) | 0.98, 3.6, 15, 50, 200 |
| Free Air Delivery | free_air_delivery | text | — | Actual volume of air delivered at rated pressure (compressors only) | 4.9 l/s, 16.4 l/s, 10.7 m3/min, 378 CFM |
| Motor Power | motor_power | number | kW | Rated motor power | 0.75, 2.2, 7.5, 55, 250 |
| Motor Speed | motor_speed | number | RPM | Motor rotational speed | 1450, 1750, 2900, 3500 |
| Phase | phase | enum | — | Electrical supply phase | Single Phase, Three Phase |
| Frequency | frequency | text | Hz | Electrical supply frequency | 50, 60, 50/60 |
| Operating Temperature Range | operating_temperature_range | text | — | Minimum to maximum fluid or ambient operating temperature | -20 to 120 C, -40 to 200 C, -10 to 80 C |
| Fluid Compatibility | fluid_compatibility | text (list) | — | Types of media the equipment can handle | Water, Oil, Gas, Corrosive Chemicals, Steam, Compressed Air, Slurry |
| NPSH Required | npsh_required | number | m | Net Positive Suction Head required to avoid cavitation (pumps) | 1.5, 2.8, 5.0, 8.0 |
| Efficiency | efficiency | number | % | Pump, valve, or compressor operating efficiency at design point | 65, 78, 85, 92 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus API, ASME, and ISO valve/pump standards | [Grundfos](https://product-selection.grundfos.com/us/products), [Parker Hannifin](https://www.parker.com/), [Atlas Copco](https://www.atlascopco.com/en-us/compressors/general/engineering-compressor-specification-sheets), [Flowserve](https://www.flowserve.com/products/products-catalog/pumps) |
