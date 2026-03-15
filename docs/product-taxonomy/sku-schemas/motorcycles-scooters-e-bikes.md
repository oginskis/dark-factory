# SKU Schema: Motorcycles, Scooters & E-Bikes

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or dealer product identifier | CBR1000RR-SP25, GROM125S, Z900-ABS |
| Product Name | text | Full product name including year, make, model, and variant | 2025 Honda Fury, 2025 Kawasaki Z900 ABS, 2025 Zero SR/F Premium |
| URL | text | Direct link to the product page | https://example.com/motorcycle/2025-honda-fury |
| Price | number | Manufacturer suggested retail price | 4499, 9299, 14995, 21795 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Make | text | Vehicle manufacturer or brand | Honda, Yamaha, Kawasaki, Ducati, BMW, Harley-Davidson, Zero, Vespa, KTM |
| Model | text | Vehicle model name | Fury, CBR1000RR, MT-07, Z900, Multistrada V4, R 1300 GS |
| Model Year | number | Production model year | 2024, 2025, 2026 |
| Vehicle Type | enum | Primary vehicle classification | Cruiser, Sport, Adventure Touring, Standard, Touring, Sport-Touring, Off-Road, Scooter, E-Bike, Track |
| Engine Type | text | Engine configuration description | Liquid-Cooled V-Twin, Air-Cooled Parallel Twin, Single-Cylinder 4-Stroke, Permanent Magnet AC Motor |
| Displacement | number (cc) | Engine displacement in cubic centimeters (ICE only) | 125, 321, 649, 998, 1301, 1868 |
| Bore x Stroke | text (mm) | Cylinder bore and stroke dimensions | 76.0 x 55.0, 80.0 x 49.7, 100.0 x 66.0 |
| Compression Ratio | text | Engine compression ratio | 10.0:1, 11.5:1, 13.2:1, 14.0:1 |
| Horsepower | number (HP) | Peak engine or motor power output | 9.7, 54, 120, 210 |
| Torque | number (lb-ft) | Peak torque output | 8.6, 34.5, 52, 100, 140 |
| Fuel System | text | Fuel delivery method | PGM-FI (Programmed Fuel Injection), EFI, Carbureted, N/A (Electric) |
| Transmission | text | Gearbox type and number of speeds | 5-Speed Manual, 6-Speed Manual, CVT, 6-Speed with Quick Shifter, Clutchless Direct Drive |
| Final Drive | enum | Power delivery to rear wheel | Chain, Belt, Shaft |
| Motor Power | number (kW) | Continuous or peak motor output for electric models | 3, 11, 15, 82, 110 |
| Battery Capacity | number (kWh) | Traction battery energy capacity for electric models | 1.4, 3.6, 14.4, 17.3 |
| Electric Range | number (mi) | Estimated range on full charge in city conditions | 30, 60, 110, 171 |
| Fuel Capacity | number (gal) | Fuel tank volume | 1.6, 2.1, 3.4, 4.5, 6.3 |
| Seat Height | number (in) | Height of the seat measured from ground level | 26.2, 28.9, 30.7, 31.5, 33.5 |
| Overall Length | number (in) | Total vehicle length | 67.3, 78.0, 82.5, 90.2 |
| Overall Width | number (in) | Total vehicle width including mirrors or handlebars | 27.0, 30.3, 33.0, 36.6 |
| Overall Height | number (in) | Total vehicle height | 39.0, 42.5, 46.3, 55.1 |
| Wheelbase | number (in) | Distance between front and rear axle centers | 49.4, 54.3, 57.1, 62.0, 65.7 |
| Ground Clearance | number (in) | Minimum distance from ground to lowest point of chassis | 4.1, 5.3, 6.3, 8.7 |
| Curb Weight | number (lbs) | Vehicle weight ready to ride with full fluids | 224, 348, 414, 505, 655 |
| Front Suspension | text | Front suspension type and travel | 41mm Inverted Fork 120mm Travel, Showa SFF-BP 43mm, WP APEX 48mm |
| Rear Suspension | text | Rear suspension type and travel | Pro-Link Single Shock, Linkage-Assisted Monoshock, Twin Shocks 3.5-inch Travel |
| Front Brake | text | Front brake type, disc diameter, and caliper | Single 336mm Disc / 2-Piston Caliper, Dual 320mm Discs / Brembo 4-Piston Radial |
| Rear Brake | text | Rear brake type and disc diameter | Single 256mm Disc / 1-Piston Caliper, Single 220mm Disc |
| Front Tire | text | Front tire size specification | 90/90-21, 120/70ZR17, 120/80-14 |
| Rear Tire | text | Rear tire size specification | 200/55ZR17, 180/55ZR17, 140/70-14 |
| ABS | enum | Anti-lock braking system availability | Standard, Optional, Not Available |
| Traction Control | enum | Traction or stability control availability | Standard, Optional, Not Available |
| Color Options | text (list) | Available exterior color choices | Graphite Black, Grand Prix Red, Matte Gunpowder Black Metallic |
| Certification | text (list) | Regulatory and emissions compliance | EPA, CARB, Euro 5+, WMTC |
| Warranty | text | Standard manufacturer warranty period | 1 year unlimited mileage, 2 years, 5 years / 50000 miles |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus EPA/Euro 5 standards | [Motorcycle.com 2025 Specs](https://www.motorcycle.com/specs/2025.html), [Honda Powersports 2025 Fury](https://powersports.honda.com/motorcycle/cruiser/fury/2025/fury), [Total Motorcycle 2025 Models](https://www.totalmotorcycle.com/2025-motorcycle-models/), [MotorbikeCatalog Database](https://www.motorbikecatalog.com/) |
