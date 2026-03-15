# SKU Schema: Ammunition (Centerfire, Rimfire, Shotshell)

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 223A, AE9DP100, WB12GT75, CC0025 |
| Product Name | text | Full product name including brand, line, caliber, grain weight, and bullet type | Federal Power-Shok .223 Rem 55gr JSP, Hornady Precision Hunter 6.5 Creedmoor 143gr ELD-X, Winchester Super-X 12 Gauge 2-3/4 1oz #8 Shot |
| URL | text | Direct link to the product page | https://example.com/product/federal-223a |
| Price | number | Numeric price per box excluding currency symbol | 14.99, 28.99, 41.99, 62.99, 129.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that produces the ammunition | Federal Premium, Hornady, Winchester, CCI, Remington, Speer, Sig Sauer, Norma, Fiocchi |
| Product Line | text | Named ammunition line or series within the brand | Power-Shok, American Eagle, Precision Hunter, Super-X, Gold Dot, Critical Defense, V-Max |
| Ammunition Type | enum | Broad ignition and platform classification | Centerfire Rifle, Centerfire Handgun, Rimfire, Shotshell |
| Caliber/Gauge | text | Cartridge designation or shotshell gauge | .223 Rem, 9mm Luger, .308 Win, .22 LR, .22 WMR, 12 Gauge, 20 Gauge, .410 Bore |
| Bullet/Projectile Weight | number (grains) | Weight of the bullet or slug in grains | 36, 55, 115, 124, 143, 147, 150, 180, 210 |
| Bullet/Projectile Type | text | Construction and design of the projectile | Full Metal Jacket (FMJ), Jacketed Soft Point (JSP), Hollow Point (HP), ELD-X, Ballistic Tip, V-Max, Polymer Tip, Lead Round Nose |
| Bullet Diameter | number (inches) | Cross-sectional diameter of the bullet | 0.224, 0.264, 0.277, 0.308, 0.355, 0.452 |
| Muzzle Velocity | number (fps) | Speed of the projectile at the muzzle | 1030, 1180, 2350, 2700, 3050, 3240 |
| Muzzle Energy | number (ft-lbs) | Kinetic energy of the projectile at the muzzle | 235, 356, 409, 2913 |
| Ballistic Coefficient (G1) | number | Aerodynamic efficiency of the bullet using the G1 drag model | 0.235, 0.371, 0.465, 0.625 |
| Sectional Density | number | Ratio of bullet mass to its cross-sectional area | 0.157, 0.186, 0.226, 0.264, 0.319 |
| Case Material | text | Material used for the cartridge case | Brass, Nickel-Plated Brass, Steel, Aluminum, Polymer |
| Primer Type | text | Type of primer used in the cartridge | Boxer, Berdan, Non-Corrosive, Lead-Free |
| Cartridge Overall Length | number (inches) | Total length of the loaded cartridge | 1.169, 2.260, 2.800, 3.340, 3.650 |
| Shell Length | text (inches) | Fired hull length for shotshells | 1-3/4, 2-1/2, 2-3/4, 3, 3-1/2 |
| Shot Size | text | Pellet diameter designation for shotshells and rimfire shotshells | #4, #6, #7.5, #8, #9, #12, BB, T, 00 Buck |
| Shot Weight | number (oz) | Total weight of shot payload in shotshells | 0.5, 0.875, 1, 1.125, 1.25, 1.5, 2 |
| Shot Material | text | Material composition of the shot pellets | Lead, Steel, Bismuth, Tungsten, Copper-Plated Lead, Hevi-Shot |
| Wad Type | text | Type of wad or sabot used in shotshells | Plastic, Fiber, FliteControl, Wad-Less |
| Dram Equivalent | text | Historical powder charge equivalency rating for shotshells | 2-3/4, 3, 3-1/4, Max |
| Rounds Per Box | number | Number of cartridges or shells in the retail package | 5, 10, 15, 20, 25, 50, 100, 250, 325, 500 |
| New/Remanufactured | enum | Whether the ammunition is factory-new or reloaded | New, Remanufactured |
| Intended Use | text (list) | Primary application for the ammunition | Target/Range, Self-Defense, Big Game Hunting, Varmint, Waterfowl, Upland, Turkey, Competition, Training |
| Velocity at 100 Yards | number (fps) | Projectile speed at 100 yards downrange | 935, 1060, 2158, 2593, 2854 |
| Energy at 100 Yards | number (ft-lbs) | Kinetic energy at 100 yards downrange | 190, 295, 2139 |
| Hazmat Shipping | boolean | Whether the product requires hazardous materials shipping surcharge | Yes, No |
| Temperature Sensitivity | text | Performance consistency across temperature extremes | Temperature Stable, Standard |
| Country of Origin | text | Country where the ammunition is manufactured | USA, Czech Republic, Italy, Serbia, Israel, Sweden |
| UPC | text | Universal Product Code barcode identifier | 029465063351, 090255810035 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 sources plus SAAMI specifications and CIP standards | [Federal Premium](https://www.federalpremium.com/), [Hornady](https://www.hornady.com/), [CCI Ammunition](https://www.cci-ammunition.com/), [Winchester](https://winchester.com/) |
