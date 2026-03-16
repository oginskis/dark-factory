# SKU Schema: Ammunition (Centerfire, Rimfire, Shotshell)

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition
**Taxonomy ID:** `firearms.ammunition`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 223A, AE9DP100, WB12GT75, CC0025 |
| Product Name | product_name | text | — | Full product name including brand, line, caliber, grain weight, and bullet type | Federal Power-Shok .223 Rem 55gr JSP, Hornady Precision Hunter 6.5 Creedmoor 143gr ELD-X, Winchester Super-X 12 Gauge 2-3/4 1oz #8 Shot |
| URL | url | text | — | Direct link to the product page | https://example.com/product/federal-223a |
| Price | price | number | — | Numeric price per box excluding currency symbol | 14.99, 28.99, 41.99, 62.99, 129.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Ammunition Type | ammunition_type | enum | — | Broad ignition and platform classification | Centerfire Rifle, Centerfire Handgun, Rimfire, Shotshell |
| Bullet/Projectile Type | bulletprojectile_type | text | — | Construction and design of the projectile | Full Metal Jacket (FMJ), Jacketed Soft Point (JSP), Hollow Point (HP), ELD-X, Ballistic Tip, V-Max, Polymer Tip, Lead Round Nose |
| Case Material | case_material | text | — | Material used for the cartridge case | Brass, Nickel-Plated Brass, Steel, Aluminum, Polymer |
| Primer Type | primer_type | text | — | Type of primer used in the cartridge | Boxer, Berdan, Non-Corrosive, Lead-Free |
| Shot Material | shot_material | text | — | Material composition of the shot pellets | Lead, Steel, Bismuth, Tungsten, Copper-Plated Lead, Hevi-Shot |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Wad Type | wad_type | text | — | Type of wad or sabot used in shotshells | Plastic, Fiber, FliteControl, Wad-Less |
| Country of Origin | country_of_origin | text | — | Country where the ammunition is manufactured | USA, Czech Republic, Italy, Serbia, Israel, Sweden |
| Product Line | product_line | text | — | Named ammunition line or series within the brand | Power-Shok, American Eagle, Precision Hunter, Super-X, Gold Dot, Critical Defense, V-Max |
| Caliber/Gauge | calibergauge | text | — | Cartridge designation or shotshell gauge | .223 Rem, 9mm Luger, .308 Win, .22 LR, .22 WMR, 12 Gauge, 20 Gauge, .410 Bore |
| Muzzle Velocity | muzzle_velocity | number | fps | Speed of the projectile at the muzzle | 1030, 1180, 2350, 2700, 3050, 3240 |
| Muzzle Energy | muzzle_energy | number | ft-lbs | Kinetic energy of the projectile at the muzzle | 235, 356, 409, 2913 |
| Ballistic Coefficient (G1) | ballistic_coefficient_g1 | number | — | Aerodynamic efficiency of the bullet using the G1 drag model | 0.235, 0.371, 0.465, 0.625 |
| Sectional Density | sectional_density | number | — | Ratio of bullet mass to its cross-sectional area | 0.157, 0.186, 0.226, 0.264, 0.319 |
| Dram Equivalent | dram_equivalent | text | — | Historical powder charge equivalency rating for shotshells | 2-3/4, 3, 3-1/4, Max |
| Rounds Per Box | rounds_per_box | number | — | Number of cartridges or shells in the retail package | 5, 10, 15, 20, 25, 50, 100, 250, 325, 500 |
| New/Remanufactured | newremanufactured | enum | — | Whether the ammunition is factory-new or reloaded | New, Remanufactured |
| Intended Use | intended_use | text (list) | — | Primary application for the ammunition | Target/Range, Self-Defense, Big Game Hunting, Varmint, Waterfowl, Upland, Turkey, Competition, Training |
| Velocity at 100 Yards | velocity_at_100_yards | number | fps | Projectile speed at 100 yards downrange | 935, 1060, 2158, 2593, 2854 |
| Energy at 100 Yards | energy_at_100_yards | number | ft-lbs | Kinetic energy at 100 yards downrange | 190, 295, 2139 |
| Hazmat Shipping | hazmat_shipping | boolean | — | Whether the product requires hazardous materials shipping surcharge | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 sources plus SAAMI specifications and CIP standards | [Federal Premium](https://www.federalpremium.com/), [Hornady](https://www.hornady.com/), [CCI Ammunition](https://www.cci-ammunition.com/), [Winchester](https://winchester.com/) |
