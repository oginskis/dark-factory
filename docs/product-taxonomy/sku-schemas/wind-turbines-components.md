# SKU Schema: Wind Turbines & Components

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.wind_turbines`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | V150-4.2-IEC3B, HAL-X-14MW, SG14-222DD |
| Product Name | product_name | text | — | yes | Full product name including model designation, rated power, and rotor diameter | Vestas V150-4.2 MW EnVentus, GE Haliade-X 14 MW, Siemens Gamesa SG 14.0-222 DD |
| URL | url | text | — | yes | Direct link to the product page | https://www.vestas.com/en/energy-solutions/onshore-wind-turbines/enventus-platform/v150-4-2-mw |
| Price | price | number | — | yes | Numeric price per unit or per kW installed, excluding currency symbol | 3500000, 12000000, 1200 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, DKK, CNY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Blade Material | blade_material | text | — | — | Primary composite material of the blade | Carbon fibre reinforced epoxy, Glass fibre reinforced polyester, Glass/carbon hybrid |
| Tower Type | tower_type | text | — | — | Structural type of the tower | Steel tubular, Hybrid steel-concrete, Concrete, Lattice |
| IEC Wind Class | iec_wind_class | text | — | — | Design class per IEC 61400-1 defining wind regime suitability | IA, IIA, IIIA, IIIB, S, T |
| Generator Type | generator_type | text | — | — | Electrical generator technology used | PMSG, DFIG, DASG, Squirrel cage induction |
| Drivetrain Type | drivetrain_type | text | — | — | Mechanical power transmission configuration | Direct drive, Geared (3-stage), Medium-speed geared (2-stage) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Grid Connection Type | grid_connection_type | text | — | — | Power electronics topology for grid interface | Full converter IGBT, DFIG partial converter, Full quadrant IGBT |
| Country of Origin | country_of_origin | text | — | — | Country where the turbine is manufactured or assembled | Denmark, Germany, Spain, China, USA |
| Manufacturer | manufacturer | text | — | — | Turbine OEM name | Vestas, GE Vernova, Siemens Gamesa, Goldwind, Nordex, Enercon |
| Rated Power | rated_power | number | kW | — | Nameplate electrical output at rated wind speed | 4200, 6200, 14000, 15000 |
| Swept Area | swept_area | number | m2 | — | Circular area swept by the rotor blades | 17671, 20612, 38013, 43742 |
| Number of Blades | number_of_blades | number | — | — | Count of rotor blades | 3 |
| Hub Height | hub_height | number | m | — | Height from ground level to the rotor hub centre | 105, 135, 150, 166 |
| Cut-in Wind Speed | cut-in_wind_speed | number | m/s | — | Minimum wind speed at which the turbine begins generating | 3.0, 3.5, 4.0 |
| Rated Wind Speed | rated_wind_speed | number | m/s | — | Wind speed at which the turbine reaches nameplate output | 9.9, 10.1, 11.0, 12.0 |
| Cut-out Wind Speed | cut-out_wind_speed | number | m/s | — | Wind speed at which the turbine shuts down for protection | 22.5, 24.5, 25.0, 34.0 |
| Survival Wind Speed | survival_wind_speed | number | m/s | — | Maximum wind speed the turbine structure can withstand without damage | 52.5, 59.5, 71.3 |
| Grid Frequency | grid_frequency | text | Hz | — | Electrical grid frequency compatibility | 50, 60, 50/60 |
| Maximum Rotor Speed | maximum_rotor_speed | number | rpm | — | Peak rotational speed of the rotor | 7.8, 10.4, 11.5, 14.0 |
| Tip Speed | tip_speed | number | m/s | — | Maximum linear speed at the blade tip | 80, 82, 90 |
| Power Density | power_density | number | W/m2 | — | Ratio of rated power to swept area | 237.7, 300.8, 368.4 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus IEC 61400 standards | [Vestas V150-4.2](https://en.wind-turbine-models.com/turbines/1841-vestas-v150-4.2), [GE Haliade-X 14 MW](https://en.wind-turbine-models.com/turbines/2320-ge-vernova-ge-haliade-x-14-mw), [The Wind Power - Vestas V150](https://www.thewindpower.net/turbine_en_1490_vestas_v150-4000-4200.php), [Siemens Gamesa - Blackridge Research](https://www.blackridgeresearch.com/blog/top-wind-turbine-manufacturers-makers-companies-suppliers) |
