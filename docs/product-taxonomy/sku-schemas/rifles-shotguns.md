# SKU Schema: Rifles & Shotguns

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition
**Taxonomy ID:** `firearms.rifles_shotguns`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 57233, H024-3030, 85836, 50701 |
| Product Name | product_name | text | — | yes | Full product name including manufacturer, model, caliber, and key variant details | Savage Axis .223 Rem Bolt-Action Rifle, Henry H024-3030 Side Gate Lever Action .30-30, Mossberg 500 12 Gauge Pump Shotgun |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/savage-axis-223 |
| Price | price | number | — | yes | Numeric retail price excluding currency symbol | 349.99, 649.99, 1099.99, 2499.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Firearm Type | firearm_type | enum | — | — | Primary classification of the long gun | Bolt-Action Rifle, Lever-Action Rifle, Semi-Auto Rifle, Pump Shotgun, Semi-Auto Shotgun, Over/Under Shotgun, Side-by-Side Shotgun, Break-Action Shotgun, Single-Shot Rifle |
| Action Type | action_type | text | — | — | Mechanism used to load, fire, and eject cartridges | Bolt, Lever, Semi-Automatic, Pump, Break-Action, Gas-Operated, Inertia-Driven |
| Magazine Type | magazine_type | text | — | — | Type of ammunition feeding device | Detachable Box, Internal Box, Tubular, Rotary, Hinged Floorplate |
| Barrel Material | barrel_material | text | — | — | Material used for the barrel | Carbon Steel, Stainless Steel, Chrome-Moly, Chrome-Lined |
| Stock Material | stock_material | text | — | — | Material used for the buttstock and forend | Synthetic, Walnut, Laminate, Birch, Polymer, Carbon Fiber, Hardwood |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Stock Type | stock_type | text | — | — | Design style of the stock | Sporter, Thumbhole, Pistol Grip, Monte Carlo, Straight/English, Adjustable, Folding, Collapsible |
| Receiver Material | receiver_material | text | — | — | Material used for the receiver or action | Carbon Steel, Aluminum Alloy, Stainless Steel |
| Trigger Type | trigger_type | text | — | — | Type of trigger mechanism or model name | AccuTrigger, X-Mark Pro, Timney, Standard, Gold Trigger |
| Safety Type | safety_type | text | — | — | Type of manual safety mechanism | Cross-Bolt, Tang, 2-Position, 3-Position, Slide |
| Country of Origin | country_of_origin | text | — | — | Country where the firearm is manufactured | USA, Italy, Turkey, Japan, Belgium, Brazil |
| Model | model | text | — | — | Specific model name or number | Axis, Model 110, 500, 870, Super Black Eagle 3, Model 94, M700 |
| Caliber/Gauge | calibergauge | text | — | — | Cartridge chambering for rifles or gauge for shotguns | .223 Rem, .308 Win, .30-06, 6.5 Creedmoor, .30-30 Win, 12 Gauge, 20 Gauge, .410 Bore |
| Barrel Contour | barrel_contour | text | — | — | Profile shape of the barrel | Sporter, Heavy/Bull, Fluted, Varmint, Pencil |
| Barrel Finish | barrel_finish | text | — | — | Surface treatment on the barrel | Blued, Matte Black, Stainless, Cerakote, Parkerized |
| Rifling Twist Rate | rifling_twist_rate | text | — | — | Barrel rifling twist ratio for rifles | 1:7, 1:9, 1:10, 1:12 |
| Choke System | choke_system | text | — | — | Type of choke installed or included with shotguns | Fixed (Modified), Interchangeable (Accu-Choke), Invector-Plus, ProBore, Crio |
| Chokes Included | chokes_included | text (list) | — | — | Set of choke tubes shipped with the shotgun | Full, Modified, Improved Cylinder, Skeet, Extra Full Turkey |
| Stock Finish | stock_finish | text | — | — | Surface treatment on the stock | Matte Black, Oil Finish, Satin, Camouflage Dip, Cerakote |
| Receiver Finish | receiver_finish | text | — | — | Surface treatment on the receiver | Matte Black, Stainless, Anodized, Cerakote |
| Sighting System | sighting_system | text | — | — | Type of sights installed on the firearm | Iron Sights, Bead Sight, Drilled and Tapped (scope ready), Ghost Ring, Rifle Sights, Vent Rib |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 39 attributes from 4 sources plus SAAMI standards and Firearms Guide database schema | [Savage Arms](https://savagearms.com/), [Mossberg](https://www.mossberg.com/), [Benelli](https://www.benelliusa.com/), [Henry Repeating Arms](https://www.henryusa.com/) |
