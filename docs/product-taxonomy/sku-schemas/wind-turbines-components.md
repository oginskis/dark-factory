# SKU Schema: Wind Turbines & Components

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | V150-4.2-IEC3B, HAL-X-14MW, SG14-222DD |
| Product Name | text | Full product name including model designation, rated power, and rotor diameter | Vestas V150-4.2 MW EnVentus, GE Haliade-X 14 MW, Siemens Gamesa SG 14.0-222 DD |
| URL | text | Direct link to the product page | https://www.vestas.com/en/energy-solutions/onshore-wind-turbines/enventus-platform/v150-4-2-mw |
| Price | number | Numeric price per unit or per kW installed, excluding currency symbol | 3500000, 12000000, 1200 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, DKK, CNY |
| Manufacturer | text | Turbine OEM name | Vestas, GE Vernova, Siemens Gamesa, Goldwind, Nordex, Enercon |
| Rated Power | number (kW) | Nameplate electrical output at rated wind speed | 4200, 6200, 14000, 15000 |
| Rotor Diameter | number (m) | Tip-to-tip diameter of the rotor sweep | 150, 162, 220, 236 |
| Swept Area | number (m2) | Circular area swept by the rotor blades | 17671, 20612, 38013, 43742 |
| Number of Blades | number | Count of rotor blades | 3 |
| Blade Length | number (m) | Length of a single blade from root to tip | 73.65, 80, 107, 115.5 |
| Blade Material | text | Primary composite material of the blade | Carbon fibre reinforced epoxy, Glass fibre reinforced polyester, Glass/carbon hybrid |
| Hub Height | number (m) | Height from ground level to the rotor hub centre | 105, 135, 150, 166 |
| Tower Type | text | Structural type of the tower | Steel tubular, Hybrid steel-concrete, Concrete, Lattice |
| Cut-in Wind Speed | number (m/s) | Minimum wind speed at which the turbine begins generating | 3.0, 3.5, 4.0 |
| Rated Wind Speed | number (m/s) | Wind speed at which the turbine reaches nameplate output | 9.9, 10.1, 11.0, 12.0 |
| Cut-out Wind Speed | number (m/s) | Wind speed at which the turbine shuts down for protection | 22.5, 24.5, 25.0, 34.0 |
| Survival Wind Speed | number (m/s) | Maximum wind speed the turbine structure can withstand without damage | 52.5, 59.5, 71.3 |
| IEC Wind Class | text | Design class per IEC 61400-1 defining wind regime suitability | IA, IIA, IIIA, IIIB, S, T |
| Generator Type | text | Electrical generator technology used | PMSG, DFIG, DASG, Squirrel cage induction |
| Drivetrain Type | text | Mechanical power transmission configuration | Direct drive, Geared (3-stage), Medium-speed geared (2-stage) |
| Grid Frequency | text (Hz) | Electrical grid frequency compatibility | 50, 60, 50/60 |
| Generator Voltage | number (V) | Output voltage of the generator | 690, 800, 3300, 3323 |
| Maximum Rotor Speed | number (rpm) | Peak rotational speed of the rotor | 7.8, 10.4, 11.5, 14.0 |
| Tip Speed | number (m/s) | Maximum linear speed at the blade tip | 80, 82, 90 |
| Power Density | number (W/m2) | Ratio of rated power to swept area | 237.7, 300.8, 368.4 |
| Nacelle Weight | number (t) | Mass of the nacelle assembly including drivetrain and generator | 68, 140, 600 |
| Rotor Weight | number (t) | Combined mass of hub and blades | 55, 100, 225 |
| Tower Weight | number (t) | Mass of the complete tower structure | 180, 350, 1200 |
| Application | enum | Installation environment | Onshore, Offshore, Both |
| Power Control Method | text | Mechanism for regulating power output | Pitch, Active stall, Pitch with full converter |
| Noise Level | number (dB(A)) | Sound power level at rated conditions | 104, 106, 108 |
| Operating Temperature Range | text | Ambient temperature range for operation | -20 to +45 C, -30 to +40 C, -10 to +50 C |
| Design Lifetime | number (years) | Certified structural design life of the turbine | 20, 25, 30 |
| Certifications | text (list) | Type certificates and design standard compliance | IEC 61400-1, IEC 61400-22, DNV-SE-0441, GL2010 |
| Grid Connection Type | text | Power electronics topology for grid interface | Full converter IGBT, DFIG partial converter, Full quadrant IGBT |
| Country of Origin | text | Country where the turbine is manufactured or assembled | Denmark, Germany, Spain, China, USA |
| Annual Energy Production | number (GWh) | Estimated yearly output at reference wind conditions | 15.1, 25.0, 74.0 |
| Availability | number (%) | Guaranteed technical uptime percentage | 95, 97, 98 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus IEC 61400 standards | [Vestas V150-4.2](https://en.wind-turbine-models.com/turbines/1841-vestas-v150-4.2), [GE Haliade-X 14 MW](https://en.wind-turbine-models.com/turbines/2320-ge-vernova-ge-haliade-x-14-mw), [The Wind Power - Vestas V150](https://www.thewindpower.net/turbine_en_1490_vestas_v150-4000-4200.php), [Siemens Gamesa - Blackridge Research](https://www.blackridgeresearch.com/blog/top-wind-turbine-manufacturers-makers-companies-suppliers) |
