# SKU Schema: Commercial Trucks & Buses

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.commercial_trucks_buses`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or dealer stock/inventory number | STK-90214, UNIT-4587 |
| Product Name | product_name | text | — | yes | Full vehicle name including year, make, model, and configuration | 2025 Freightliner Cascadia 126 Day Cab, 2025 Volvo VNL 760 72-inch Sleeper |
| URL | url | text | — | yes | Direct link to the vehicle listing or product page | https://example.com/inventory/2025-cascadia-126 |
| Price | price | number | — | yes | MSRP or listed sale price | 145000, 185000, 275000, 450000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, SEK |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Vehicle Class | vehicle_class | enum | — | — | FHWA or FMCSA weight classification | Class 4, Class 5, Class 6, Class 7, Class 8 |
| Vehicle Type | vehicle_type | enum | — | — | Body or chassis configuration | Day Cab Tractor, Sleeper Tractor, Straight Truck, Coach Bus, Transit Bus, School Bus, Cutaway Chassis, Refuse Truck |
| Fuel Type | fuel_type | enum | — | — | Primary energy source | Diesel, Natural Gas (CNG/LNG), Battery Electric, Hydrogen Fuel Cell |
| Cab Type | cab_type | enum | — | — | Cab design configuration | Conventional, Cab-Over-Engine (COE), Low-Entry |
| Sleeper Size | sleeper_size | text | in | — | Sleeper berth length if equipped | 48, 60, 72, 76, N/A (Day Cab) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Make | make | text | — | — | Vehicle manufacturer or brand | Freightliner, Volvo, Kenworth, Peterbilt, Mack, International, Scania, MAN, Prevost, New Flyer |
| Model | model | text | — | — | Vehicle model designation | Cascadia, VNL 760, T680, 579, Anthem, LT, S 531 HD |
| Model Year | model_year | number | — | — | Production model year | 2024, 2025, 2026 |
| Engine Make | engine_make | text | — | — | Engine manufacturer | Detroit, Cummins, PACCAR, Volvo, Mercedes-Benz |
| Engine Model | engine_model | text | — | — | Specific engine model designation | DD15, DD13, X15, MX-13, D13TC |
| Horsepower | horsepower | number | HP | — | Rated engine horsepower | 370, 425, 455, 505, 525 |
| Torque | torque | number | lb-ft | — | Peak engine torque | 1250, 1550, 1650, 1850 |
| Emissions Standard | emissions_standard | text | — | — | Applicable emissions tier or regulation | EPA 2024, Euro VI-E, CARB Zero-Emission |
| Transmission | transmission | text | — | — | Transmission type, make, and model | Detroit DT12 12-Speed AMT, Eaton Endurant 12-Speed, Allison 3000 RDS 6-Speed Automatic |
| GVWR | gvwr | number | lbs | — | Gross Vehicle Weight Rating | 16000, 33000, 52000, 80000 |
| GCWR | gcwr | number | lbs | — | Gross Combined Weight Rating for tractor-trailer operation | 80000, 100000, 140000 |
| Front Axle Rating | front_axle_rating | number | lbs | — | Maximum rated front axle load capacity | 10000, 12000, 12500, 13300, 14600 |
| Rear Axle Rating | rear_axle_rating | number | lbs | — | Maximum rated rear axle load capacity (single or tandem) | 20000, 23000, 40000, 44000, 46000 |
| Axle Configuration | axle_configuration | text | — | — | Number of axles and drive layout | 4x2, 6x2, 6x4, 8x4 |
| BBC | bbc | number | in | — | Bumper-to-back-of-cab measurement | 116, 126, 132 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 sources plus FMCSA classification and EPA standards | [Freightliner Cascadia Specs](https://www.freightliner.com/trucks/cascadia/specifications/), [Volvo 9700 Specs](https://www.volvobuses.com/en/coaches/coaches/volvo-9700/specifications.html), [Price Digests Commercial Trucks](https://pricedigests.com/resource/commercial-trucks/), [Work Truck Online Spec Guide](https://www.worktruckonline.com/205109/commercial-vehicle-application-catalog-spec-guide) |
