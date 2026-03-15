# SKU Schema: Diesel Fuel & Heating Oil

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.diesel_heating_oil`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or distributor product identifier | CITGO-1DS15, MPC-ULSD-2D, VT-HO2-ULS |
| Product Name | text | Full product name including brand, grade, and sulfur designation | CITGO No. 2 Diesel Ultra-Low Sulfur, Marathon No. 1-D S15 Winter Diesel, Premium Heating Oil No. 2 |
| URL | text | Direct link to the product data sheet or listing page | https://example.com/fuels/ulsd-no2 |
| Price | number | Numeric price per gallon or litre at time of listing, excluding currency symbol | 3.49, 3.89, 4.29 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Fuel Type | enum | Primary fuel classification | No. 1-D Diesel, No. 2-D Diesel, No. 4-D Diesel, No. 1 Fuel Oil (Kerosene), No. 2 Fuel Oil (Heating Oil), No. 4 Fuel Oil, No. 6 Fuel Oil (Bunker), Biodiesel Blend |
| ASTM Grade | text | Grade designation per ASTM D975 (diesel) or ASTM D396 (fuel oil) | No. 1-D S15, No. 2-D S500, No. 2-D S5000, No. 2 Oil |
| Sulfur Classification | enum | Sulfur tier designation | Ultra-Low Sulfur (S15), Low Sulfur (S500), High Sulfur (S5000) |
| Hazmat Class | text | DOT or UN hazardous materials classification | UN1202 Class 3 Flammable Liquid |
| Country of Origin | text | Country where the fuel was refined | USA, Canada, UK, Netherlands, Saudi Arabia |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Sulfur Content | number (ppm) | Maximum sulfur content in parts per million | 15, 500, 5000 |
| Cetane Number | number | Ignition quality rating — higher values mean easier ignition | 40, 45, 48, 55 |
| Cetane Index | number | Calculated cetane value from density and distillation data | 40, 42, 46 |
| Flash Point | number (deg C) | Minimum temperature at which fuel vapors will ignite | 38, 52, 55, 66 |
| Cloud Point | number (deg C) | Temperature at which wax crystals first appear, indicating cold-weather performance | -18, -12, -5, 0 |
| Pour Point | number (deg C) | Lowest temperature at which the fuel will flow | -30, -21, -12, -6 |
| Kinematic Viscosity at 40C | text (mm2/s) | Flow resistance measured at 40 degrees C per ASTM D445 | 1.3-2.4, 1.9-4.1, 5.5-24.0 |
| API Gravity | number | Density measurement on the API gravity scale | 34, 38, 40, 42 |
| Specific Gravity at 60F | number | Density relative to water at 60 degrees F | 0.820, 0.840, 0.860 |
| Distillation T90 | number (deg C) | Temperature at which 90 percent of the fuel has evaporated per ASTM D86 | 282, 338, 356 |
| Energy Content | number (BTU/gal) | Heat energy per gallon | 128000, 132000, 137500, 138700 |
| Biodiesel Blend Percentage | number (%) | Percentage of biodiesel (FAME) in the blend | 0, 2, 5, 20 |
| Lubricity (HFRR) | number (micron) | High-Frequency Reciprocating Rig wear scar diameter per ASTM D6079 | 460, 520 |
| Carbon Residue | number (%) | Residue after evaporation per ASTM D524 | 0.15, 0.35 |
| Water and Sediment | number (% vol) | Maximum water and sediment content | 0.02, 0.05, 0.50 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM D975 and ASTM D396 standards | [CITGO Diesel TDS](https://www.docs.citgo.com/msds_pi/ag1df.pdf), [Crown Oil Fuel Specs](https://www.crownoil.co.uk/guides/fuel-specifications-guide/), [ANSI Blog ASTM D975](https://blog.ansi.org/ansi/astm-d975-diesel-fuel-standard-specification/), [EIA Heating Oil](https://www.eia.gov/energyexplained/gasoline/octane-in-depth.php) |
