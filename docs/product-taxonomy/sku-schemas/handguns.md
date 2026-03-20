# SKU Schema: Handguns

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition
**Taxonomy ID:** `firearms.handguns`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | UA2650110, 164191, 13050, SW-686-6 |
| Product Name | product_name | text | — | yes | Full product name including manufacturer, model, caliber, and key variant details | Glock 19 Gen5 9mm, Smith and Wesson Model 686 Plus 2.5-Inch .357 Magnum, SIG Sauer P320 XCompact |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/glock-19-gen5 |
| Price | price | number | — | yes | Numeric retail price excluding currency symbol | 449.99, 699.99, 1039.00, 1899.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Handgun Type | handgun_type | enum | — | — | Primary action classification | Semi-Automatic Pistol, Revolver, Derringer, Single Shot |
| Action Type | action_type | text | — | — | Firing mechanism type | Striker-Fired, Single-Action (SA), Double-Action (DA), Double-Action/Single-Action (DA/SA), Double-Action Only (DAO) |
| Magazine Type | magazine_type | text | — | — | Type of ammunition feeding device | Detachable Box Magazine, Cylinder, Tube Magazine, Single Stack, Double Stack |
| Frame Material | frame_material | text | — | — | Material used for the grip frame or lower receiver | Polymer, Stainless Steel, Aluminum Alloy, Carbon Steel, Scandium Alloy, Titanium |
| Slide/Cylinder Material | slidecylinder_material | text | — | — | Material of the slide on pistols or cylinder on revolvers | Stainless Steel, Carbon Steel, Titanium, Aluminum |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Barrel Material | barrel_material | text | — | — | Material used for the barrel | Carbon Steel, Stainless Steel, Match Grade Stainless |
| Country of Origin | country_of_origin | text | — | — | Country where the firearm is manufactured | USA, Austria, Germany, Italy, Czech Republic, Brazil, Turkey |
| Model | model | text | — | — | Specific model name or number | G19 Gen5, Model 686 Plus, P320 XCompact, 1911, SR9, PDP |
| Caliber | caliber | text | — | — | Cartridge chambering of the firearm | 9mm Luger, .45 ACP, .40 S&W, .380 ACP, .357 Magnum, .38 Special, 10mm Auto, .22 LR |
| Overall Height | overall_height | number | inches | — | Height from the top of the slide/frame to the bottom of the grip or magazine baseplate | 4.02, 4.17, 4.81, 5.04, 5.47 |
| Overall Width | overall_width | number | inches | — | Maximum width of the firearm | 1.02, 1.06, 1.18, 1.26, 1.31 |
| Finish | finish | text | — | — | Surface treatment or coating on the firearm | Blued, Stainless, Nylon/nDLC, Cerakote, Nitride, Nickel, Two-Tone, FDE |
| Rifling Twist Rate | rifling_twist_rate | text | — | — | Barrel rifling twist ratio | 1:10, 1:16, 1:18.87 |
| Front Sight | front_sight | text | — | — | Type of front sight installed | Fixed Dot, Night Sight, Fiber Optic, Blade, Ramp |
| Rear Sight | rear_sight | text | — | — | Type of rear sight installed | Fixed Notch, Adjustable, Night Sight, U-Notch, Suppressor Height |
| Optics Ready | optics_ready | boolean | — | — | Whether the slide is pre-cut for a reflex/red dot optic | Yes, No |
| Grip | grip | text | — | — | Material and style of the grip | Polymer Textured, Rubber, Wood, G10, Hogue Overmold, Stippled |
| Safety Mechanisms | safety_mechanisms | text (list) | — | — | Built-in safety features | Trigger Safety, Firing Pin Block, Manual Thumb Safety, Grip Safety, Loaded Chamber Indicator, Magazine Disconnect |
| Accessory Rail | accessory_rail | text | — | — | Type of accessory rail for lights or lasers | Picatinny, M1913, Proprietary, None |
| Number of Magazines Included | number_of_magazines_included | number | — | — | Count of magazines shipped with the firearm | 1, 2, 3 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus SAAMI standards and ATF classification criteria | [Glock](https://www.glock.com/), [Smith and Wesson](https://www.smith-wesson.com/), [Handgun Hero](https://www.handgunhero.com/), [Genitron Handgun Database](https://www.genitron.com/Handgun-Database) |
