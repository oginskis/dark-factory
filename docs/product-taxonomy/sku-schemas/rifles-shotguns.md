# SKU Schema: Rifles & Shotguns

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 57233, H024-3030, 85836, 50701 |
| Product Name | text | Full product name including manufacturer, model, caliber, and key variant details | Savage Axis .223 Rem Bolt-Action Rifle, Henry H024-3030 Side Gate Lever Action .30-30, Mossberg 500 12 Gauge Pump Shotgun |
| URL | text | Direct link to the product page | https://example.com/product/savage-axis-223 |
| Price | number | Numeric retail price excluding currency symbol | 349.99, 649.99, 1099.99, 2499.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that produces the firearm | Savage Arms, Henry, Mossberg, Remington, Benelli, Browning, Winchester, Ruger, Beretta, Franchi |
| Model | text | Specific model name or number | Axis, Model 110, 500, 870, Super Black Eagle 3, Model 94, M700 |
| Firearm Type | enum | Primary classification of the long gun | Bolt-Action Rifle, Lever-Action Rifle, Semi-Auto Rifle, Pump Shotgun, Semi-Auto Shotgun, Over/Under Shotgun, Side-by-Side Shotgun, Break-Action Shotgun, Single-Shot Rifle |
| Caliber/Gauge | text | Cartridge chambering for rifles or gauge for shotguns | .223 Rem, .308 Win, .30-06, 6.5 Creedmoor, .30-30 Win, 12 Gauge, 20 Gauge, .410 Bore |
| Action Type | text | Mechanism used to load, fire, and eject cartridges | Bolt, Lever, Semi-Automatic, Pump, Break-Action, Gas-Operated, Inertia-Driven |
| Chamber Length | text (inches) | Maximum shell length the shotgun chamber accepts | 2-3/4, 3, 3-1/2 |
| Magazine Capacity | number | Number of rounds the magazine or tube holds | 3, 4, 5, 6, 8, 10, 30 |
| Magazine Type | text | Type of ammunition feeding device | Detachable Box, Internal Box, Tubular, Rotary, Hinged Floorplate |
| Barrel Length | number (inches) | Length of the barrel from breech to muzzle | 18, 20, 22, 24, 26, 28, 30, 32 |
| Barrel Material | text | Material used for the barrel | Carbon Steel, Stainless Steel, Chrome-Moly, Chrome-Lined |
| Barrel Contour | text | Profile shape of the barrel | Sporter, Heavy/Bull, Fluted, Varmint, Pencil |
| Barrel Finish | text | Surface treatment on the barrel | Blued, Matte Black, Stainless, Cerakote, Parkerized |
| Rifling Twist Rate | text | Barrel rifling twist ratio for rifles | 1:7, 1:9, 1:10, 1:12 |
| Choke System | text | Type of choke installed or included with shotguns | Fixed (Modified), Interchangeable (Accu-Choke), Invector-Plus, ProBore, Crio |
| Chokes Included | text (list) | Set of choke tubes shipped with the shotgun | Full, Modified, Improved Cylinder, Skeet, Extra Full Turkey |
| Overall Length | number (inches) | Total length of the firearm | 35.25, 38.5, 42.5, 48, 52 |
| Weight | number (lbs) | Weight of the firearm unloaded | 5.5, 6.3, 7, 7.5, 8.2 |
| Stock Material | text | Material used for the buttstock and forend | Synthetic, Walnut, Laminate, Birch, Polymer, Carbon Fiber, Hardwood |
| Stock Type | text | Design style of the stock | Sporter, Thumbhole, Pistol Grip, Monte Carlo, Straight/English, Adjustable, Folding, Collapsible |
| Stock Finish | text | Surface treatment on the stock | Matte Black, Oil Finish, Satin, Camouflage Dip, Cerakote |
| Length of Pull | number (inches) | Distance from the trigger to the center of the buttpad | 12.5, 13.5, 13.75, 14 |
| Receiver Material | text | Material used for the receiver or action | Carbon Steel, Aluminum Alloy, Stainless Steel |
| Receiver Finish | text | Surface treatment on the receiver | Matte Black, Stainless, Anodized, Cerakote |
| Trigger Type | text | Type of trigger mechanism or model name | AccuTrigger, X-Mark Pro, Timney, Standard, Gold Trigger |
| Sighting System | text | Type of sights installed on the firearm | Iron Sights, Bead Sight, Drilled and Tapped (scope ready), Ghost Ring, Rifle Sights, Vent Rib |
| Optics Rail | text | Type of scope mounting system | Picatinny, Weaver, Proprietary, Drilled and Tapped, None |
| Recoil Pad | text | Type of buttpad for recoil management | Rubber, Inflex, Supercell, LimbSaver, Gel |
| Threaded Barrel | boolean | Whether the barrel is threaded for muzzle devices | Yes, No |
| Safety Type | text | Type of manual safety mechanism | Cross-Bolt, Tang, 2-Position, 3-Position, Slide |
| Camo Pattern | text | Camouflage pattern applied to the firearm | Mossy Oak Break-Up Country, Realtree Timber, True Timber Strata, Cerakote FDE |
| Intended Use | text (list) | Primary application for the firearm | Big Game Hunting, Waterfowl, Upland, Turkey, Home Defense, Target/Competition, Varmint |
| Country of Origin | text | Country where the firearm is manufactured | USA, Italy, Turkey, Japan, Belgium, Brazil |
| Warranty | text | Manufacturer warranty coverage | Limited Lifetime, Lifetime Service, 10 Year |
| UPC | text | Universal Product Code barcode identifier | 011356572332, 619835016126 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 39 attributes from 4 sources plus SAAMI standards and Firearms Guide database schema | [Savage Arms](https://savagearms.com/), [Mossberg](https://www.mossberg.com/), [Benelli](https://www.benelliusa.com/), [Henry Repeating Arms](https://www.henryusa.com/) |
