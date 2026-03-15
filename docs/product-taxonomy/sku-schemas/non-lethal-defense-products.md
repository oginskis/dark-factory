# SKU Schema: Non-Lethal Defense Products

**Last updated:** 2026-03-15
**Parent category:** Firearms & Ammunition

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SABRE-RS-T-01, TASER-PULSE2, BYRNA-SD-KIT |
| Product Name | text | Full product name including key specs such as type and model | SABRE Red Pepper Gel with Snap Clip, TASER Pulse 2 Self-Defense Kit, Byrna SD Launcher Universal Kit |
| URL | text | Direct link to the product page | https://example.com/product/sabre-red-pepper-gel |
| Price | number | Numeric unit price excluding currency symbol | 14.99, 449.99, 379.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the defense product manufacturer | SABRE, TASER/Axon, Byrna, Mace, Fox Labs, Kimber |
| Product Type | enum | Primary category of the non-lethal defense product | Pepper Spray, Pepper Gel, Stun Gun, Conducted Energy Device, Pepper Ball Launcher, Personal Alarm, Tactical Flashlight, Baton |
| Active Agent | text | Chemical or mechanism used for incapacitation | OC (Oleoresin Capsicum), CS (Orthochlorobenzalmalononitrile), Electrical Discharge, Kinetic Impact, UV Marking Dye |
| OC Concentration | text | Percentage of oleoresin capsicum in the formula (pepper products) | 1.33% MC, 2%, 10% OC |
| Scoville Heat Units | number (SHU) | Heat intensity rating of pepper-based formulas | 2000000, 3000000, 5300000 |
| Spray Pattern | enum | Delivery pattern of the defense spray | Stream, Cone, Fog, Gel, Foam |
| Effective Range | number (ft) | Maximum effective deployment distance | 10, 12, 15, 18, 60 |
| Number of Bursts | number | Approximate number of deployments per canister or cartridge | 5, 25, 35, 50 |
| Discharge Duration | text | Total spray or discharge time per activation | 0.5 seconds, 5 seconds, 30 seconds |
| Voltage | number (V) | Peak electrical output for stun or conducted energy devices | 50000, 200000, 1000000 |
| Charge Output | text | Electrical charge delivered per cycle (conducted energy devices) | 63 microcoulombs, 26 microcoulombs |
| Caliber | text | Projectile size for launcher-type devices | .68 caliber |
| Velocity | number (fps) | Projectile muzzle velocity for launcher-type devices | 285, 300, 340 |
| Magazine Capacity | number | Number of rounds per magazine or cartridge for launchers | 5, 7, 12 |
| Power Source | text | Battery or propellant type | Lithium Battery, CR123A, 8g CO2 Cartridge, 12g CO2 Cartridge |
| Battery Life | text | Number of firings or estimated shelf life of the power source | 50 firings, 5 year shelf life, 15-20 shots per cartridge |
| Safety Mechanism | text | Type of accidental discharge prevention feature | Flip Top, Twist Lock, Trigger Guard, Safety Switch |
| UV Marking Dye | boolean | Whether the formula includes UV-reactive dye for suspect identification | true, false |
| Weight | number (g) | Total weight of the product ready to use | 39, 227, 590 |
| Length | number (mm) | Overall length of the device | 114, 133, 200 |
| Width | number (mm) | Overall width of the device | 22, 32, 45 |
| Height | number (mm) | Overall height of the device | 25, 121, 152 |
| Material | text | Primary housing or body material | Polymer, ABS Plastic, Aluminum, Steel |
| Color | text | Available color options for the device body | Black, Pink, Safety Orange, FDE |
| Certifications | text (list) | Applicable industry or safety certifications | SEI Certified, ASTM E3187-19, Health Canada Registered |
| Shelf Life | text | Product expiration or replacement interval | 2 years, 4 years, 5 years |
| Country of Origin | text | Country where the product is manufactured | USA, China, South Africa |
| Model Number | text | Manufacturer model or part number | PULSE2, SD-68, PG-120 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ASTM E3187, SEI certification) | [SABRE](https://www.sabrered.com/pepper-spray-and-personal-safety-products), [TASER/Axon](https://taser.com/), [Byrna](https://byrna.com/products/byrna-sd-non-lethal-self-defense-pistol), [The Home Security Superstore](https://www.thehomesecuritysuperstore.com/collections/stun-guns) |
