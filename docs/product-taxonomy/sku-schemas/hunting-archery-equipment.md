# SKU Schema: Hunting & Archery Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.hunting_archery`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 1141533, BLK-DIST-70, BA-A12CL30070 |
| Product Name | product_name | text | — | Full product name including key specs such as type, model, and draw weight | BlackOut Distinct Compound Bow Package 70 lb, TenPoint Titan 400 Crossbow Package, Ravin R26X Crossbow |
| URL | url | text | — | Direct link to the product page | https://example.com/product/blackout-distinct-bow |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 499.99, 1299.99, 249.97 |
| Currency | currency | text | — | ISO 4217 currency code | USD, CAD, EUR, GBP |
| Product Type | product_type | enum | — | Primary equipment category | Compound Bow, Recurve Bow, Crossbow, Longbow, Arrow, Broadhead, Quiver, Release Aid, Bow Sight |
| Riser Material | riser_material | text | — | Material used for the bow riser or crossbow rail | Aluminum, Machined Aluminum, Carbon, Magnesium |
| Limb Material | limb_material | text | — | Material used for the bow limbs | Fiberglass, Carbon, Composite, Split Limb |
| String/Cable Material | stringcable_material | text | — | Material of the bowstring and cables | BCY-X, Dyneema, Fast Flight, 452X |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, China, Taiwan, Canada |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Let-Off | let-off | text | % | Percentage of draw weight reduced at full draw on a compound bow | 65, 75, 80, 85, 90 |
| Brace Height | brace_height | number | inches | Distance from the bowstring to the deepest part of the grip at rest | 6.25, 6.375, 7, 7.5 |
| IBO/ATA Speed | iboata_speed | number | fps | Arrow speed rating measured under IBO or ATA standards | 330, 370, 400, 415 |
| Power Stroke | power_stroke | number | inches | Distance the crossbow string travels from rest to the latch. Crossbow-specific | 12, 12.75, 13.5, 13.8 |
| Kinetic Energy | kinetic_energy | number | ft-lbs | Energy delivered to the arrow at the rated speed | 100, 146, 157 |
| Width Cocked | width_cocked | number | inches | Axle-to-axle width of a crossbow when cocked | 6, 9.5, 10.5 |
| Width Uncocked | width_uncocked | number | inches | Axle-to-axle width of a crossbow at rest | 14, 25.37, 30.62 |
| Hand Orientation | hand_orientation | enum | — | Designed for left-hand or right-hand draw | Right Hand, Left Hand, Ambidextrous |
| Cam System | cam_system | text | — | Type of cam or module system on a compound bow | Single Cam, Binary Cam, Hybrid Cam, Dual Cam |
| Cocking Mechanism | cocking_mechanism | text | — | Device used to cock a crossbow | ACUdraw, ACUslide, Rope Cocker, Crank, Integrated Silent Crank |
| Scope/Sight Included | scopesight_included | text | — | Type of sighting device included in a package | Multi-Line Scope, RangeMaster 100, Illuminated 3-Dot, Multi-Reticle, None |
| Arrow/Bolt Compatibility | arrowbolt_compatibility | text | — | Recommended arrow or bolt length and weight specifications | 20-inch carbon bolts, 350-500 grain arrows, 400 spine |
| Finish/Camo Pattern | finishcamo_pattern | text | — | Surface finish or camouflage pattern | Mossy Oak Break-Up Country, Realtree Edge, TrueTimber Strata, Matte Black |
| Package Contents | package_contents | text (list) | — | Accessories included with a bow or crossbow package | Sight, Rest, Stabilizer, Quiver, Peep Sight, D-Loop, Bolts, Cocking Device |
| Intended Use | intended_use | text (list) | — | Primary hunting or target application | Whitetail Deer, Elk, Turkey, Target Shooting, 3D Archery |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus ATA/IBO standards | [Bass Pro Shops](https://www.basspro.com/), [Cabelas](https://www.cabelas.com/), [Lancaster Archery](https://lancasterarchery.com/), [Bear Archery](https://www.beararchery.com/) |
