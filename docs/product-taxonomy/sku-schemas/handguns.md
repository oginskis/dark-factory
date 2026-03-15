# SKU Schema: Handguns

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | UA2650110, 164191, 13050, SW-686-6 |
| Product Name | text | Full product name including manufacturer, model, caliber, and key variant details | Glock 19 Gen5 9mm, Smith and Wesson Model 686 Plus 2.5-Inch .357 Magnum, SIG Sauer P320 XCompact |
| URL | text | Direct link to the product page | https://example.com/product/glock-19-gen5 |
| Price | number | Numeric retail price excluding currency symbol | 449.99, 699.99, 1039.00, 1899.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that produces the firearm | Glock, Smith and Wesson, SIG Sauer, Ruger, Springfield Armory, Beretta, CZ, Walther, Kimber, Taurus |
| Model | text | Specific model name or number | G19 Gen5, Model 686 Plus, P320 XCompact, 1911, SR9, PDP |
| Handgun Type | enum | Primary action classification | Semi-Automatic Pistol, Revolver, Derringer, Single Shot |
| Caliber | text | Cartridge chambering of the firearm | 9mm Luger, .45 ACP, .40 S&W, .380 ACP, .357 Magnum, .38 Special, 10mm Auto, .22 LR |
| Action Type | text | Firing mechanism type | Striker-Fired, Single-Action (SA), Double-Action (DA), Double-Action/Single-Action (DA/SA), Double-Action Only (DAO) |
| Capacity | number | Number of rounds the magazine or cylinder holds | 5, 6, 7, 10, 13, 15, 17, 21 |
| Magazine Type | text | Type of ammunition feeding device | Detachable Box Magazine, Cylinder, Tube Magazine, Single Stack, Double Stack |
| Barrel Length | number (inches) | Length of the barrel from breech to muzzle | 2.17, 3.1, 3.39, 4.01, 4.49, 5.31, 6 |
| Overall Length | number (inches) | Total length of the firearm from end to end | 6.26, 6.85, 7.32, 7.5, 8.5 |
| Overall Height | number (inches) | Height from the top of the slide/frame to the bottom of the grip or magazine baseplate | 4.02, 4.17, 4.81, 5.04, 5.47 |
| Overall Width | number (inches) | Maximum width of the firearm | 1.02, 1.06, 1.18, 1.26, 1.31 |
| Weight Unloaded | number (oz) | Weight of the firearm without ammunition | 17.95, 21, 22, 23, 26.1, 30, 38.3 |
| Frame Material | text | Material used for the grip frame or lower receiver | Polymer, Stainless Steel, Aluminum Alloy, Carbon Steel, Scandium Alloy, Titanium |
| Frame Size | text | Manufacturer size classification for the frame | Compact, Subcompact, Full-Size, Micro, J-Frame, K-Frame, L-Frame, N-Frame, X-Frame |
| Slide/Cylinder Material | text | Material of the slide on pistols or cylinder on revolvers | Stainless Steel, Carbon Steel, Titanium, Aluminum |
| Finish | text | Surface treatment or coating on the firearm | Blued, Stainless, Nylon/nDLC, Cerakote, Nitride, Nickel, Two-Tone, FDE |
| Barrel Material | text | Material used for the barrel | Carbon Steel, Stainless Steel, Match Grade Stainless |
| Rifling Twist Rate | text | Barrel rifling twist ratio | 1:10, 1:16, 1:18.87 |
| Front Sight | text | Type of front sight installed | Fixed Dot, Night Sight, Fiber Optic, Blade, Ramp |
| Rear Sight | text | Type of rear sight installed | Fixed Notch, Adjustable, Night Sight, U-Notch, Suppressor Height |
| Optics Ready | boolean | Whether the slide is pre-cut for a reflex/red dot optic | Yes, No |
| Grip | text | Material and style of the grip | Polymer Textured, Rubber, Wood, G10, Hogue Overmold, Stippled |
| Trigger Pull Weight | number (lbs) | Force required to fire the weapon | 4.5, 5.5, 6, 8, 10, 12 |
| Safety Mechanisms | text (list) | Built-in safety features | Trigger Safety, Firing Pin Block, Manual Thumb Safety, Grip Safety, Loaded Chamber Indicator, Magazine Disconnect |
| Accessory Rail | text | Type of accessory rail for lights or lasers | Picatinny, M1913, Proprietary, None |
| Threaded Barrel | boolean | Whether the barrel is threaded for suppressor attachment | Yes, No |
| Number of Magazines Included | number | Count of magazines shipped with the firearm | 1, 2, 3 |
| Country of Origin | text | Country where the firearm is manufactured | USA, Austria, Germany, Italy, Czech Republic, Brazil, Turkey |
| Warranty | text | Manufacturer warranty coverage | Lifetime Service, Limited Lifetime, 1 Year |
| UPC | text | Universal Product Code barcode identifier | 764503037023, 022188141986 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus SAAMI standards and ATF classification criteria | [Glock](https://www.glock.com/), [Smith and Wesson](https://www.smith-wesson.com/), [Handgun Hero](https://www.handgunhero.com/), [Genitron Handgun Database](https://www.genitron.com/Handgun-Database) |
