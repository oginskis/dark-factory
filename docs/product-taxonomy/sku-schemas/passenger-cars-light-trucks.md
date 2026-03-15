# SKU Schema: Passenger Cars & Light Trucks

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer stock or inventory identifier, often a VIN-based code or dealer stock number | STK-28451, A12345 |
| Product Name | text | Full vehicle name including year, make, model, and trim | 2025 Toyota Camry LE Hybrid, 2025 Ford F-150 XLT SuperCrew 4x4 |
| URL | text | Direct link to the vehicle listing or product page | https://example.com/inventory/2025-toyota-camry-le |
| Price | number | Manufacturer suggested retail price or listed sale price | 29495, 42350, 56800 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, JPY |
| Make | text | Vehicle manufacturer or brand | Toyota, Ford, Honda, BMW, Chevrolet, Hyundai |
| Model | text | Vehicle model name | Camry, F-150, Civic, 3 Series, Silverado, Tucson |
| Model Year | number | Production model year | 2024, 2025, 2026 |
| Trim Level | text | Trim or equipment level designation | LE, XLE, XSE, Limited, Sport, Premium |
| Body Style | enum | Vehicle body configuration | Sedan, SUV, Crossover, Pickup Truck, Hatchback, Coupe, Convertible, Wagon, Minivan |
| Drivetrain | enum | Drive wheel configuration | FWD, RWD, AWD, 4WD |
| Engine Type | text | Engine configuration and displacement | 2.5L 4-Cylinder Hybrid, 3.5L V6 Twin-Turbo, 5.0L V8 |
| Horsepower | number (HP) | Peak engine or system horsepower | 225, 310, 450, 670 |
| Torque | number (lb-ft) | Peak engine or system torque | 163, 350, 510, 590 |
| Fuel Type | enum | Primary energy source | Gasoline, Diesel, Hybrid, Plug-In Hybrid, Battery Electric, Hydrogen Fuel Cell |
| Transmission | text | Transmission type and number of speeds | 8-Speed Automatic, CVT, 6-Speed Manual, 10-Speed Automatic, Single-Speed Direct Drive |
| Battery Capacity | number (kWh) | Traction battery capacity for electric and plug-in hybrid vehicles | 13.6, 72.6, 92.0, 100.0 |
| Electric Range | number (mi) | EPA-estimated all-electric driving range | 25, 53, 270, 350 |
| Fuel Economy City | number (MPG) | EPA-rated city fuel economy in miles per gallon | 25, 33, 51, 53 |
| Fuel Economy Highway | number (MPG) | EPA-rated highway fuel economy in miles per gallon | 30, 38, 47, 50 |
| Fuel Economy Combined | number (MPG) | EPA-rated combined fuel economy in miles per gallon | 28, 36, 49, 51 |
| Exterior Length | number (in) | Overall vehicle length | 182.3, 193.5, 209.1, 231.7 |
| Exterior Width | number (in) | Overall vehicle width excluding mirrors | 72.4, 73.3, 79.9, 80.2 |
| Exterior Height | number (in) | Overall vehicle height | 56.9, 60.1, 68.4, 75.6 |
| Wheelbase | number (in) | Distance between front and rear axle centers | 105.1, 111.2, 120.0, 145.4 |
| Curb Weight | number (lbs) | Vehicle weight empty with standard equipment and full fluids | 3200, 3450, 4500, 5600 |
| Seating Capacity | number | Maximum number of passenger seats | 4, 5, 7, 8 |
| Cargo Volume | number (cu ft) | Maximum cargo area volume with rear seats folded | 15.1, 36.3, 72.1, 89.1 |
| Towing Capacity | number (lbs) | Maximum trailer weight the vehicle is rated to tow | 1500, 3500, 7700, 13300 |
| Exterior Color | text | Exterior paint color name | Midnight Black Metallic, Ice Cap, Wind Chill Pearl |
| Safety Rating | text | Overall safety rating from NHTSA or Euro NCAP | 5-Star NHTSA, 5-Star Euro NCAP |
| Number of Airbags | number | Total standard airbags | 8, 10, 11 |
| ADAS Features | text (list) | Standard advanced driver-assistance features | Adaptive Cruise Control, Lane Departure Warning, Automatic Emergency Braking, Blind Spot Monitor |
| Infotainment Display | text (in) | Touchscreen display size and type | 8-inch Touchscreen, 12.3-inch Touchscreen, 14.5-inch OLED |
| Warranty (Basic) | text | Basic bumper-to-bumper warranty coverage | 3 years / 36000 miles, 5 years / 60000 miles |
| Country of Assembly | text | Country where the vehicle was assembled | USA, Japan, South Korea, Mexico, Germany |
| Tire Size | text | OEM tire specification | P215/55R17, 255/40R19, LT275/65R18 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 sources plus EPA and NHTSA standards | [Edmunds Toyota Camry 2025](https://www.edmunds.com/toyota/camry/2025/features-specs/), [Cars.com Camry Specs](https://www.cars.com/research/toyota-camry-2025/specs/), [KBB Camry 2025](https://www.kbb.com/toyota/camry/2025/specs/), [Consumer Reports New Cars](https://www.consumerreports.org/cars/new-cars-on-the-horizon-a1920770135/) |
