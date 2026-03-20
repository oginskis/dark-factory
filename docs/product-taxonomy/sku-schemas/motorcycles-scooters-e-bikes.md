# SKU Schema: Motorcycles, Scooters & E-Bikes

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.motorcycles_scooters_ebikes`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or dealer product identifier | CBR1000RR-SP25, GROM125S, Z900-ABS |
| Product Name | product_name | text | — | yes | Full product name including year, make, model, and variant | 2025 Honda Fury, 2025 Kawasaki Z900 ABS, 2025 Zero SR/F Premium |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/motorcycle/2025-honda-fury |
| Price | price | number | — | yes | Manufacturer suggested retail price | 4499, 9299, 14995, 21795 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Vehicle Type | vehicle_type | enum | — | — | Primary vehicle classification | Cruiser, Sport, Adventure Touring, Standard, Touring, Sport-Touring, Off-Road, Scooter, E-Bike, Track |
| Engine Type | engine_type | text | — | — | Engine configuration description | Liquid-Cooled V-Twin, Air-Cooled Parallel Twin, Single-Cylinder 4-Stroke, Permanent Magnet AC Motor |
| Battery Capacity | battery_capacity | number | kWh | — | Traction battery energy capacity for electric models | 1.4, 3.6, 14.4, 17.3 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Make | make | text | — | — | Vehicle manufacturer or brand | Honda, Yamaha, Kawasaki, Ducati, BMW, Harley-Davidson, Zero, Vespa, KTM |
| Model | model | text | — | — | Vehicle model name | Fury, CBR1000RR, MT-07, Z900, Multistrada V4, R 1300 GS |
| Model Year | model_year | number | — | — | Production model year | 2024, 2025, 2026 |
| Displacement | displacement | number | cc | — | Engine displacement in cubic centimeters (ICE only) | 125, 321, 649, 998, 1301, 1868 |
| Bore x Stroke | bore_x_stroke | text | mm | — | Cylinder bore and stroke dimensions | 76.0 x 55.0, 80.0 x 49.7, 100.0 x 66.0 |
| Compression Ratio | compression_ratio | text | — | — | Engine compression ratio | 10.0:1, 11.5:1, 13.2:1, 14.0:1 |
| Horsepower | horsepower | number | HP | — | Peak engine or motor power output | 9.7, 54, 120, 210 |
| Torque | torque | number | lb-ft | — | Peak torque output | 8.6, 34.5, 52, 100, 140 |
| Fuel System | fuel_system | text | — | — | Fuel delivery method | PGM-FI (Programmed Fuel Injection), EFI, Carbureted, N/A (Electric) |
| Transmission | transmission | text | — | — | Gearbox type and number of speeds | 5-Speed Manual, 6-Speed Manual, CVT, 6-Speed with Quick Shifter, Clutchless Direct Drive |
| Final Drive | final_drive | enum | — | — | Power delivery to rear wheel | Chain, Belt, Shaft |
| Motor Power | motor_power | number | kW | — | Continuous or peak motor output for electric models | 3, 11, 15, 82, 110 |
| Electric Range | electric_range | number | mi | — | Estimated range on full charge in city conditions | 30, 60, 110, 171 |
| Seat Height | seat_height | number | in | — | Height of the seat measured from ground level | 26.2, 28.9, 30.7, 31.5, 33.5 |
| Overall Width | overall_width | number | in | — | Total vehicle width including mirrors or handlebars | 27.0, 30.3, 33.0, 36.6 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus EPA/Euro 5 standards | [Motorcycle.com 2025 Specs](https://www.motorcycle.com/specs/2025.html), [Honda Powersports 2025 Fury](https://powersports.honda.com/motorcycle/cruiser/fury/2025/fury), [Total Motorcycle 2025 Models](https://www.totalmotorcycle.com/2025-motorcycle-models/), [MotorbikeCatalog Database](https://www.motorbikecatalog.com/) |
