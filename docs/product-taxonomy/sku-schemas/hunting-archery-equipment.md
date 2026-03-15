# SKU Schema: Hunting & Archery Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 1141533, BLK-DIST-70, BA-A12CL30070 |
| Product Name | text | Full product name including key specs such as type, model, and draw weight | BlackOut Distinct Compound Bow Package 70 lb, TenPoint Titan 400 Crossbow Package, Ravin R26X Crossbow |
| URL | text | Direct link to the product page | https://example.com/product/blackout-distinct-bow |
| Price | number | Numeric price per unit excluding currency symbol | 499.99, 1299.99, 249.97 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, GBP |
| Brand/Manufacturer | text | Company that produces the equipment | Mathews, Hoyt, Bear Archery, TenPoint, Ravin, PSE |
| Product Type | enum | Primary equipment category | Compound Bow, Recurve Bow, Crossbow, Longbow, Arrow, Broadhead, Quiver, Release Aid, Bow Sight |
| Axle-to-Axle Length | number (inches) | Distance between the axle pins on a compound bow or crossbow when measured at rest | 28, 30, 31, 33 |
| Draw Weight | text (lbs) | Peak poundage required to fully draw the bow. May be a range for adjustable bows | 25-70, 50-60, 70, 180, 230 |
| Draw Length | text (inches) | Distance the bowstring travels from rest to full draw. May be a range for adjustable bows | 19-30, 26-30.5, 27-32 |
| Let-Off | text (%) | Percentage of draw weight reduced at full draw on a compound bow | 65, 75, 80, 85, 90 |
| Brace Height | number (inches) | Distance from the bowstring to the deepest part of the grip at rest | 6.25, 6.375, 7, 7.5 |
| IBO/ATA Speed | number (fps) | Arrow speed rating measured under IBO or ATA standards | 330, 370, 400, 415 |
| Power Stroke | number (inches) | Distance the crossbow string travels from rest to the latch. Crossbow-specific | 12, 12.75, 13.5, 13.8 |
| Kinetic Energy | number (ft-lbs) | Energy delivered to the arrow at the rated speed | 100, 146, 157 |
| Overall Length | number (inches) | Total length of the bow or crossbow from tip to tip | 31, 33, 35, 62 |
| Width Cocked | number (inches) | Axle-to-axle width of a crossbow when cocked | 6, 9.5, 10.5 |
| Width Uncocked | number (inches) | Axle-to-axle width of a crossbow at rest | 14, 25.37, 30.62 |
| Physical Weight | number (lbs) | Weight of the bow or crossbow without accessories | 4.2, 5.7, 6.3, 6.8 |
| Hand Orientation | enum | Designed for left-hand or right-hand draw | Right Hand, Left Hand, Ambidextrous |
| Cam System | text | Type of cam or module system on a compound bow | Single Cam, Binary Cam, Hybrid Cam, Dual Cam |
| Riser Material | text | Material used for the bow riser or crossbow rail | Aluminum, Machined Aluminum, Carbon, Magnesium |
| Limb Material | text | Material used for the bow limbs | Fiberglass, Carbon, Composite, Split Limb |
| String/Cable Material | text | Material of the bowstring and cables | BCY-X, Dyneema, Fast Flight, 452X |
| Cocking Mechanism | text | Device used to cock a crossbow | ACUdraw, ACUslide, Rope Cocker, Crank, Integrated Silent Crank |
| Scope/Sight Included | text | Type of sighting device included in a package | Multi-Line Scope, RangeMaster 100, Illuminated 3-Dot, Multi-Reticle, None |
| Arrow/Bolt Compatibility | text | Recommended arrow or bolt length and weight specifications | 20-inch carbon bolts, 350-500 grain arrows, 400 spine |
| Finish/Camo Pattern | text | Surface finish or camouflage pattern | Mossy Oak Break-Up Country, Realtree Edge, TrueTimber Strata, Matte Black |
| Package Contents | text (list) | Accessories included with a bow or crossbow package | Sight, Rest, Stabilizer, Quiver, Peep Sight, D-Loop, Bolts, Cocking Device |
| Intended Use | text (list) | Primary hunting or target application | Whitetail Deer, Elk, Turkey, Target Shooting, 3D Archery |
| Noise/Vibration Dampening | text | Vibration reduction technology built into the bow or crossbow | Limb Dampeners, String Suppressors, Harmonic Stabilizer, Dead End String Stop |
| Safety Certification | text (list) | Applicable safety or compliance standards | ATA Compliant, IBO Certified, CE |
| Country of Origin | text | Country where the product is manufactured | USA, China, Taiwan, Canada |
| Warranty | text | Manufacturer warranty duration or type | Lifetime, 5 Year, Limited Lifetime |
| UPC | text | Universal Product Code barcode identifier | 010847573001, 788130029527 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus ATA/IBO standards | [Bass Pro Shops](https://www.basspro.com/), [Cabelas](https://www.cabelas.com/), [Lancaster Archery](https://lancasterarchery.com/), [Bear Archery](https://www.beararchery.com/) |
