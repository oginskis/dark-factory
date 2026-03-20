# SKU Schema: Non-Lethal Defense Products

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition
**Taxonomy ID:** `firearms.non_lethal_defense`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | SABRE-RS-T-01, TASER-PULSE2, BYRNA-SD-KIT |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type and model | SABRE Red Pepper Gel with Snap Clip, TASER Pulse 2 Self-Defense Kit, Byrna SD Launcher Universal Kit |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/sabre-red-pepper-gel |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 14.99, 449.99, 379.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary category of the non-lethal defense product | Pepper Spray, Pepper Gel, Stun Gun, Conducted Energy Device, Pepper Ball Launcher, Personal Alarm, Tactical Flashlight, Baton |
| Material | material | text | — | — | Primary housing or body material | Polymer, ABS Plastic, Aluminum, Steel |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, China, South Africa |
| Model Number | model_number | text | — | — | Manufacturer model or part number | PULSE2, SD-68, PG-120 |
| Voltage | voltage | number | V | — | Peak electrical output for stun or conducted energy devices | 50000, 200000, 1000000 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Active Agent | active_agent | text | — | — | Chemical or mechanism used for incapacitation | OC (Oleoresin Capsicum), CS (Orthochlorobenzalmalononitrile), Electrical Discharge, Kinetic Impact, UV Marking Dye |
| OC Concentration | oc_concentration | text | — | — | Percentage of oleoresin capsicum in the formula (pepper products) | 1.33% MC, 2%, 10% OC |
| Scoville Heat Units | scoville_heat_units | number | SHU | — | Heat intensity rating of pepper-based formulas | 2000000, 3000000, 5300000 |
| Spray Pattern | spray_pattern | enum | — | — | Delivery pattern of the defense spray | Stream, Cone, Fog, Gel, Foam |
| Effective Range | effective_range | number | ft | — | Maximum effective deployment distance | 10, 12, 15, 18, 60 |
| Number of Bursts | number_of_bursts | number | — | — | Approximate number of deployments per canister or cartridge | 5, 25, 35, 50 |
| Discharge Duration | discharge_duration | text | — | — | Total spray or discharge time per activation | 0.5 seconds, 5 seconds, 30 seconds |
| Charge Output | charge_output | text | — | — | Electrical charge delivered per cycle (conducted energy devices) | 63 microcoulombs, 26 microcoulombs |
| Caliber | caliber | text | — | — | Projectile size for launcher-type devices | .68 caliber |
| Velocity | velocity | number | fps | — | Projectile muzzle velocity for launcher-type devices | 285, 300, 340 |
| Power Source | power_source | text | — | — | Battery or propellant type | Lithium Battery, CR123A, 8g CO2 Cartridge, 12g CO2 Cartridge |
| Battery Life | battery_life | text | — | — | Number of firings or estimated shelf life of the power source | 50 firings, 5 year shelf life, 15-20 shots per cartridge |
| Safety Mechanism | safety_mechanism | text | — | — | Type of accidental discharge prevention feature | Flip Top, Twist Lock, Trigger Guard, Safety Switch |
| UV Marking Dye | uv_marking_dye | boolean | — | — | Whether the formula includes UV-reactive dye for suspect identification | true, false |
| Width | width | number | mm | — | Overall width of the device | 22, 32, 45 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ASTM E3187, SEI certification) | [SABRE](https://www.sabrered.com/pepper-spray-and-personal-safety-products), [TASER/Axon](https://taser.com/), [Byrna](https://byrna.com/products/byrna-sd-non-lethal-self-defense-pistol), [The Home Security Superstore](https://www.thehomesecuritysuperstore.com/collections/stun-guns) |
