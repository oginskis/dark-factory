# SKU Schema: Bicycles & Bicycle Components

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.bicycles_components`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 37059, 3713, SH-RD-R8150 |
| Product Name | product_name | text | Full product name including brand, model, and key identifiers | Trek Domane SLR 7 Gen 4, Canyon Endurace CF 7, Shimano Ultegra Di2 RD-R8150 Rear Derailleur |
| URL | url | text | Direct link to the product page | https://example.com/bikes/domane-slr-7 |
| Price | price | number | Numeric price per unit excluding currency symbol | 2499.00, 6699.00, 10138.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Type | product_type | enum | Whether the product is a complete bicycle or a component | Complete Bicycle, Frameset, Component, Accessory |
| Component Category | component_category | text | Specific component type if not a complete bicycle | Frame, Fork, Rear Derailleur, Front Derailleur, Crankset, Cassette, Chain, Brakes, Wheels, Tires, Handlebar, Stem, Seatpost, Saddle, Pedals, Shifters, Bottom Bracket, Headset |
| Bicycle Type | bicycle_type | enum | Intended riding discipline for complete bicycles or frames | Road, Mountain, Gravel, Cyclocross, Triathlon, Hybrid, City, BMX, E-Bike |
| Frame Material | frame_material | enum | Primary material of the bicycle frame | Carbon (CF), Carbon (CFR), Aluminum (AL), Steel, Titanium |
| Shifting Type | shifting_type | enum | Mechanism used for gear shifting | Electronic, Mechanical, Wireless Electronic |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Brake Type | brake_type | enum | Type of braking system | Hydraulic Disc, Mechanical Disc, Rim Brake |
| Rim Material | rim_material | enum | Material of the wheel rims | Carbon (CF), Aluminum (AL) |
| Motor Type | motor_type | text | Type and brand of electric assist motor for e-bikes. Blank for non-electric bicycles | Shimano EP8, Bosch Performance CX, Fazua Ride 60, TQ HPR 50 |
| Groupset Brand | groupset_brand | text | Brand of the drivetrain groupset on complete bicycles | Shimano, SRAM, Campagnolo |
| Groupset Model | groupset_model | text | Specific groupset model or tier | Dura-Ace Di2, Ultegra Di2, 105, SRAM RED AXS, SRAM Force AXS, SRAM Rival, Campagnolo Super Record |
| Number of Speeds | number_of_speeds | text | Total gear count expressed as front rings x rear sprockets | 1x11, 1x12, 2x11, 2x12, 2x13 |
| Cassette Range | cassette_range | text | Range of sprocket teeth on the rear cassette | 11-28T, 11-30T, 11-34T, 10-36T, 10-52T |
| Tire Width | tire_width | text (mm) | Width of stock tires or maximum tire clearance for frames | 25c, 28c, 30c, 32c, 38c, 2.25, 2.40 |
| Tire Clearance | tire_clearance | number (mm) | Maximum tire width the frame can accommodate | 28, 32, 35, 38, 40, 45, 2.40 |
| Rim Depth | rim_depth | number (mm) | Depth of the wheel rim profile, affects aerodynamics | 30, 37, 45, 50, 60, 80 |
| Handlebar Width | handlebar_width | number (mm) | Width of the handlebar, centre to centre | 380, 400, 420, 440, 460 |
| Bottom Bracket Standard | bottom_bracket_standard | text | Type and width of the bottom bracket shell | BSA 68mm, BB86, PF30, T47, BB30, Press Fit |
| Headset Standard | headset_standard | text | Headset bearing type and steerer tube configuration | IS42/28.6 - IS52/40 (tapered), ZS44/28.6 (straight) |
| Axle Standard | axle_standard | text | Front and rear axle type and dimensions | 12x100mm QR front / 12x142mm thru-axle rear, 15x110mm Boost front / 12x148mm Boost rear |
| Color | color | text | Frame or component color as listed by the manufacturer | Sparkle Stealth, Axinite Flip/Trek Black, Metallic White Silver |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (ISO 4210, EN 15194, ETRTO) | [Trek Bikes](https://www.trekbikes.com/us/en_US/bikes/road-bikes/performance-road-bikes/domane/domane-slr/), [Canyon](https://www.canyon.com/en-us/road-bikes/), [Specialized](https://www.specialized.com/us/en/shop/bikes/road-bikes), [Shimano](https://productinfo.shimano.com/en) |
