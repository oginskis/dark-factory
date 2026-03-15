# SKU Schema: Bicycles & Bicycle Components

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 37059, 3713, SH-RD-R8150 |
| Product Name | text | Full product name including brand, model, and key identifiers | Trek Domane SLR 7 Gen 4, Canyon Endurace CF 7, Shimano Ultegra Di2 RD-R8150 Rear Derailleur |
| URL | text | Direct link to the product page | https://example.com/bikes/domane-slr-7 |
| Price | number | Numeric price per unit excluding currency symbol | 2499.00, 6699.00, 10138.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | Trek, Canyon, Specialized, Giant, Shimano, SRAM, Campagnolo |
| Product Type | enum | Whether the product is a complete bicycle or a component | Complete Bicycle, Frameset, Component, Accessory |
| Component Category | text | Specific component type if not a complete bicycle | Frame, Fork, Rear Derailleur, Front Derailleur, Crankset, Cassette, Chain, Brakes, Wheels, Tires, Handlebar, Stem, Seatpost, Saddle, Pedals, Shifters, Bottom Bracket, Headset |
| Bicycle Type | enum | Intended riding discipline for complete bicycles or frames | Road, Mountain, Gravel, Cyclocross, Triathlon, Hybrid, City, BMX, E-Bike |
| Frame Material | enum | Primary material of the bicycle frame | Carbon (CF), Carbon (CFR), Aluminum (AL), Steel, Titanium |
| Frame Size | text | Frame size designation; may be letter, number, or centimetres | XS, S, M, L, XL, 2XL, 47cm, 50cm, 52cm, 54cm, 56cm, 58cm |
| Wheel Size | text | Wheel diameter standard | 700c, 650b (27.5), 29, 26, 20, 16 |
| Groupset Brand | text | Brand of the drivetrain groupset on complete bicycles | Shimano, SRAM, Campagnolo |
| Groupset Model | text | Specific groupset model or tier | Dura-Ace Di2, Ultegra Di2, 105, SRAM RED AXS, SRAM Force AXS, SRAM Rival, Campagnolo Super Record |
| Number of Speeds | text | Total gear count expressed as front rings x rear sprockets | 1x11, 1x12, 2x11, 2x12, 2x13 |
| Shifting Type | enum | Mechanism used for gear shifting | Electronic, Mechanical, Wireless Electronic |
| Chainring Sizes | text | Number of teeth on the front chainring or chainrings | 50/34T, 52/36T, 48/35T, 40T, 34T |
| Cassette Range | text | Range of sprocket teeth on the rear cassette | 11-28T, 11-30T, 11-34T, 10-36T, 10-52T |
| Brake Type | enum | Type of braking system | Hydraulic Disc, Mechanical Disc, Rim Brake |
| Brake Rotor Size | number (mm) | Diameter of disc brake rotors | 140, 160, 180, 200, 203 |
| Tire Width | text (mm) | Width of stock tires or maximum tire clearance for frames | 25c, 28c, 30c, 32c, 38c, 2.25, 2.40 |
| Tire Clearance | number (mm) | Maximum tire width the frame can accommodate | 28, 32, 35, 38, 40, 45, 2.40 |
| Rim Material | enum | Material of the wheel rims | Carbon (CF), Aluminum (AL) |
| Rim Depth | number (mm) | Depth of the wheel rim profile, affects aerodynamics | 30, 37, 45, 50, 60, 80 |
| Handlebar Width | number (mm) | Width of the handlebar, centre to centre | 380, 400, 420, 440, 460 |
| Seatpost Diameter | number (mm) | Outer diameter of the seatpost | 27.2, 30.9, 31.6, 34.9 |
| Bottom Bracket Standard | text | Type and width of the bottom bracket shell | BSA 68mm, BB86, PF30, T47, BB30, Press Fit |
| Headset Standard | text | Headset bearing type and steerer tube configuration | IS42/28.6 - IS52/40 (tapered), ZS44/28.6 (straight) |
| Axle Standard | text | Front and rear axle type and dimensions | 12x100mm QR front / 12x142mm thru-axle rear, 15x110mm Boost front / 12x148mm Boost rear |
| Weight | number (kg) | Total weight of the complete bicycle or individual component | 7.32, 7.89, 8.50, 10.20, 0.256 |
| Rider Weight Limit | number (kg) | Maximum combined rider and cargo weight the bicycle is rated for | 110, 120, 130, 150 |
| Motor Type | text | Type and brand of electric assist motor for e-bikes. Blank for non-electric bicycles | Shimano EP8, Bosch Performance CX, Fazua Ride 60, TQ HPR 50 |
| Battery Capacity | number (Wh) | Battery capacity for e-bikes in watt-hours | 250, 360, 500, 625, 750 |
| Color | text | Frame or component color as listed by the manufacturer | Sparkle Stealth, Axinite Flip/Trek Black, Metallic White Silver |
| Warranty | text | Manufacturer warranty period for the frame or component | Lifetime frame, 6 years, 2 years |
| Country of Assembly | text | Country where the bicycle or component is assembled | Taiwan, China, Germany, USA, Cambodia |
| Certification | text (list) | Safety and compliance certifications | ISO 4210, EN 15194, CPSC, UL 2849 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (ISO 4210, EN 15194, ETRTO) | [Trek Bikes](https://www.trekbikes.com/us/en_US/bikes/road-bikes/performance-road-bikes/domane/domane-slr/), [Canyon](https://www.canyon.com/en-us/road-bikes/), [Specialized](https://www.specialized.com/us/en/shop/bikes/road-bikes), [Shimano](https://productinfo.shimano.com/en) |
