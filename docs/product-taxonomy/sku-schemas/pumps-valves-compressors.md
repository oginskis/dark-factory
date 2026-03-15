# SKU Schema: Pumps, Valves & Compressors

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | GP200, GA55, KPH-85229, PCM600S |
| Product Name | text | Full product name including key specs such as type, brand, and model | Grundfos CR 32-2 Vertical Multistage Centrifugal Pump, Parker Hannifin GP200 Solenoid Valve, Atlas Copco GA 55 Rotary Screw Compressor |
| URL | text | Direct link to the product page | https://example.com/product/grundfos-cr-32-2 |
| Price | number | Numeric price per unit excluding currency symbol | 125.00, 2500.00, 35000.00, 85000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | Grundfos, Flowserve, Parker Hannifin, Atlas Copco, Ingersoll Rand, Sulzer, Emerson, IMI |
| Product Type | enum | Primary equipment category | Centrifugal Pump, Positive Displacement Pump, Submersible Pump, Ball Valve, Gate Valve, Globe Valve, Check Valve, Butterfly Valve, Solenoid Valve, Control Valve, Reciprocating Compressor, Rotary Screw Compressor, Scroll Compressor, Diaphragm Pump |
| Model Number | text | Manufacturer model or part number | CR 32-2, GP200, GA 55 FF, KPH 85229 |
| Flow Rate | text | Maximum or rated volumetric flow rate with unit | 10.7 m3/h, 280 m3/h, 150 GPM, 1206 CFM |
| Head/Pressure Rating | text | Maximum operating pressure or pump head | 95 m, 10 bar, 150 PSI, 250 bar, ANSI Class 300 |
| Max Working Pressure | number (bar) | Maximum allowable working pressure | 4, 10, 16, 25, 250 |
| Cv Flow Coefficient | number | Valve flow coefficient for sizing (valves only) | 0.98, 3.6, 15, 50, 200 |
| Free Air Delivery | text | Actual volume of air delivered at rated pressure (compressors only) | 4.9 l/s, 16.4 l/s, 10.7 m3/min, 378 CFM |
| Motor Power | number (kW) | Rated motor power | 0.75, 2.2, 7.5, 55, 250 |
| Motor Speed | number (RPM) | Motor rotational speed | 1450, 1750, 2900, 3500 |
| Voltage | text (V) | Electrical supply voltage | 115, 230, 400, 460, 230/400 |
| Phase | enum | Electrical supply phase | Single Phase, Three Phase |
| Frequency | text (Hz) | Electrical supply frequency | 50, 60, 50/60 |
| Port Size | text | Inlet and outlet connection size | 1/4 NPT, 1/2 NPT, DN50, DN100, 2 inch ANSI, 4 inch flanged |
| Connection Type | text | Pipe or port connection method | Threaded NPT, Flanged ANSI, Flanged DIN, Tri-Clamp, Welded, Compression |
| Body Material | text | Material of the pump casing, valve body, or compressor housing | Cast Iron, Stainless Steel 316, Bronze, Carbon Steel, Ductile Iron, PVDF, Hastelloy |
| Impeller/Trim Material | text | Material of the impeller (pumps) or trim (valves) | Stainless Steel 316, Bronze, Noryl, PTFE, Hastelloy C, Duplex |
| Seal Type | text | Primary shaft or body sealing method | Mechanical Seal, Packed Gland, O-Ring, PTFE Seat, Metal Seat, Lip Seal, Magnetic Drive |
| Operating Temperature Range | text | Minimum to maximum fluid or ambient operating temperature | -20 to 120 C, -40 to 200 C, -10 to 80 C |
| Fluid Compatibility | text (list) | Types of media the equipment can handle | Water, Oil, Gas, Corrosive Chemicals, Steam, Compressed Air, Slurry |
| Tank Capacity | number (L) | Receiver tank volume for compressors | 24, 50, 200, 500, 1000 |
| NPSH Required | number (m) | Net Positive Suction Head required to avoid cavitation (pumps) | 1.5, 2.8, 5.0, 8.0 |
| Efficiency | number (%) | Pump, valve, or compressor operating efficiency at design point | 65, 78, 85, 92 |
| Noise Level | number (dB) | Sound pressure level at rated operating conditions | 61, 66, 72, 78, 85 |
| Duty Cycle | text | Maximum continuous operating percentage or run time | 100%, 75%, 60% |
| Actuation | text | Valve or compressor control mechanism | Manual, Pneumatic, Electric, Hydraulic, Solenoid, Self-Acting |
| Dimensions (L x W x H) | text (mm) | Overall equipment dimensions | 500 x 300 x 400, 1870 x 1240 x 1660 |
| Weight | number (kg) | Equipment dry weight | 0.5, 25, 165, 1025, 5000 |
| IP/NEMA Rating | text | Enclosure or motor ingress protection rating | IP55, IP65, NEMA 4, NEMA 4X |
| ATEX Zone | text | Explosive atmosphere certification zone, if applicable | Zone 1, Zone 2, Zone 21, Not Classified |
| Certifications | text (list) | Safety, quality, and compliance certifications | CE, ISO 9001, ATEX, PED, API 610, API 600, ASME, UL, FM |
| Country of Origin | text | Country where the equipment was manufactured | Denmark, Germany, USA, UK, India, Japan, Sweden |
| Warranty | text | Manufacturer warranty duration | 1 year, 2 years, 3 years |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus API, ASME, and ISO valve/pump standards | [Grundfos](https://product-selection.grundfos.com/us/products), [Parker Hannifin](https://www.parker.com/), [Atlas Copco](https://www.atlascopco.com/en-us/compressors/general/engineering-compressor-specification-sheets), [Flowserve](https://www.flowserve.com/products/products-catalog/pumps) |
