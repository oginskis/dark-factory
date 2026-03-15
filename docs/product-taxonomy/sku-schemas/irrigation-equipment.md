# SKU Schema: Irrigation Equipment

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.irrigation_equipment`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or retailer product identifier, article number, or part number | 970545901, 900978801, PGJ-04 |
| Product Name | product_name | text | Full product name including model designation and key specs | I-20 Stainless Steel Rotor, Classic Circular Sprinkler Samba, UniRam AS XR 16mm |
| URL | url | text | Direct link to the product page or catalog listing | https://example.com/products/sprinklers/i-20.html |
| Price | price | number | Numeric price value without currency symbol | 24.99, 149.00, 0.85 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP |
| Product Type | product_type | enum | Primary functional classification of the irrigation product | Rotor, Spray Head, Drip Emitter, Dripline, Valve, Controller, Sensor, Nozzle, Sprinkler, Pump, Hose Fitting, Filter |
| Application Type | application_type | enum | Intended use environment | Residential, Commercial, Agricultural, Golf, Greenhouse |
| Installation Type | installation_type | enum | How the product is installed or mounted | Pop-up, Fixed, Surface Mount, Underground, In-line, Wall Mount |
| Material | material | text | Primary construction material | ABS Plastic, Stainless Steel, Brass, PVC, Polypropylene |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | Germany, USA, Israel, China |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Product Series | product_series | text | Product line, family, or collection name within the brand | 1800 Series, PGJ, SILENO, UniRam AS, MP Rotator |
| Spray Radius Min | spray_radius_min | number (m) | Minimum spray or throw distance | 0.5, 2.0, 5.2 |
| Spray Radius Max | spray_radius_max | number (m) | Maximum spray or throw distance | 3.0, 14.0, 18.0 |
| Arc Range | arc_range | text | Adjustable spray arc range in degrees | 50-360, 90-210, 0-360 Fixed |
| Flow Rate Min | flow_rate_min | number (L/h) | Minimum water flow rate | 1.4, 60, 230 |
| Flow Rate Max | flow_rate_max | number (L/h) | Maximum water flow rate | 4.0, 1360, 3360 |
| Operating Pressure Min | operating_pressure_min | number (bar) | Minimum operating water pressure | 0.2, 1.0, 1.7 |
| Operating Pressure Max | operating_pressure_max | number (bar) | Maximum operating water pressure | 4.0, 4.8, 7.0 |
| Area Coverage Min | area_coverage_min | number (m2) | Minimum irrigatable area | 9, 50, 200 |
| Area Coverage Max | area_coverage_max | number (m2) | Maximum irrigatable area | 250, 700, 2500 |
| Precipitation Rate | precipitation_rate | number (mm/h) | Average precipitation or application rate | 5.0, 10.0, 15.0 |
| Nozzle Trajectory | nozzle_trajectory | number (degrees) | Spray trajectory angle above horizontal | 13, 15, 25 |
| Pop-up Height | pop-up_height | text | Height the riser extends above ground when active | 4 in, 6 in, 12 in, Shrub |
| Pressure Compensated | pressure_compensated | boolean | Whether the emitter maintains constant flow regardless of pressure variations | true, false |
| Dripper Spacing | dripper_spacing | number (m) | Distance between emitters in a dripline | 0.2, 0.3, 0.5, 1.0 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies covering sprinklers, rotors, drip irrigation, and garden watering equipment | [Hunter Industries](https://www.hunterirrigation.com/products), [Gardena](https://www.gardena.com/int/products/watering/), [Netafim](https://www.netafim.com/en/products-and-solutions/product-offering/drip-irrigation-products/), [Sprinkler Supply Store](https://sprinklersupplystore.com/collections/hunter-sprinklers) |
