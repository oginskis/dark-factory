# SKU Schema: Passenger Cars & Light Trucks

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.passenger_cars_light_trucks`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer stock or inventory identifier, often a VIN-based code or dealer stock number | STK-28451, A12345 |
| Product Name | product_name | text | — | yes | Full vehicle name including year, make, model, and trim | 2025 Toyota Camry LE Hybrid, 2025 Ford F-150 XLT SuperCrew 4x4 |
| URL | url | text | — | yes | Direct link to the vehicle listing or product page | https://example.com/inventory/2025-toyota-camry-le |
| Price | price | number | — | yes | Manufacturer suggested retail price or listed sale price | 29495, 42350, 56800 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Engine Type | engine_type | text | — | — | Engine configuration and displacement | 2.5L 4-Cylinder Hybrid, 3.5L V6 Twin-Turbo, 5.0L V8 |
| Fuel Type | fuel_type | enum | — | — | Primary energy source | Gasoline, Diesel, Hybrid, Plug-In Hybrid, Battery Electric, Hydrogen Fuel Cell |
| Battery Capacity | battery_capacity | number | kWh | — | Traction battery capacity for electric and plug-in hybrid vehicles | 13.6, 72.6, 92.0, 100.0 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Make | make | text | — | — | Vehicle manufacturer or brand | Toyota, Ford, Honda, BMW, Chevrolet, Hyundai |
| Model | model | text | — | — | Vehicle model name | Camry, F-150, Civic, 3 Series, Silverado, Tucson |
| Model Year | model_year | number | — | — | Production model year | 2024, 2025, 2026 |
| Trim Level | trim_level | text | — | — | Trim or equipment level designation | LE, XLE, XSE, Limited, Sport, Premium |
| Body Style | body_style | enum | — | — | Vehicle body configuration | Sedan, SUV, Crossover, Pickup Truck, Hatchback, Coupe, Convertible, Wagon, Minivan |
| Drivetrain | drivetrain | enum | — | — | Drive wheel configuration | FWD, RWD, AWD, 4WD |
| Horsepower | horsepower | number | HP | — | Peak engine or system horsepower | 225, 310, 450, 670 |
| Torque | torque | number | lb-ft | — | Peak engine or system torque | 163, 350, 510, 590 |
| Transmission | transmission | text | — | — | Transmission type and number of speeds | 8-Speed Automatic, CVT, 6-Speed Manual, 10-Speed Automatic, Single-Speed Direct Drive |
| Electric Range | electric_range | number | mi | — | EPA-estimated all-electric driving range | 25, 53, 270, 350 |
| Fuel Economy City | fuel_economy_city | number | MPG | — | EPA-rated city fuel economy in miles per gallon | 25, 33, 51, 53 |
| Fuel Economy Highway | fuel_economy_highway | number | MPG | — | EPA-rated highway fuel economy in miles per gallon | 30, 38, 47, 50 |
| Fuel Economy Combined | fuel_economy_combined | number | MPG | — | EPA-rated combined fuel economy in miles per gallon | 28, 36, 49, 51 |
| Exterior Width | exterior_width | number | in | — | Overall vehicle width excluding mirrors | 72.4, 73.3, 79.9, 80.2 |
| Exterior Height | exterior_height | number | in | — | Overall vehicle height | 56.9, 60.1, 68.4, 75.6 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 sources plus EPA and NHTSA standards | [Edmunds Toyota Camry 2025](https://www.edmunds.com/toyota/camry/2025/features-specs/), [Cars.com Camry Specs](https://www.cars.com/research/toyota-camry-2025/specs/), [KBB Camry 2025](https://www.kbb.com/toyota/camry/2025/specs/), [Consumer Reports New Cars](https://www.consumerreports.org/cars/new-cars-on-the-horizon-a1920770135/) |
