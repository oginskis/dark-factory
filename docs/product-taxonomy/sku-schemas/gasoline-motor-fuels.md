# SKU Schema: Gasoline & Motor Fuels

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or distributor product identifier | EXX-UNL87, SHL-VPWR93, BP-E15-REG |
| Product Name | text | Full product name including brand, grade, and formulation | Shell V-Power NiTRO+ Premium 93, ExxonMobil Synergy Regular 87, bp Amoco Ultimate 93 |
| URL | text | Direct link to the product data sheet or listing page | https://example.com/fuels/premium-93 |
| Price | number | Numeric price per gallon or litre at time of listing, excluding currency symbol | 3.29, 3.89, 4.19 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Fuel brand or refiner name | Shell, ExxonMobil, bp, Chevron, Marathon, Valero, Phillips 66 |
| Fuel Type | enum | Primary fuel classification | Conventional Gasoline, Reformulated Gasoline (RFG), E85 Flex Fuel, Racing Fuel, Aviation Gasoline |
| Octane Rating (AKI) | number | Anti-Knock Index (R+M)/2 as posted at the pump | 87, 89, 91, 93, 100 |
| Research Octane Number (RON) | number | Octane measured via the Research method | 91, 95, 98, 100 |
| Motor Octane Number (MON) | number | Octane measured via the Motor method | 82, 85, 87, 89 |
| Grade | enum | Market grade designation | Regular, Midgrade, Premium, Super Premium |
| Ethanol Content | text (% vol) | Volume percentage of ethanol blended into the fuel | E0 (0%), E10 (10%), E15 (15%), E85 (85%) |
| Oxygenate Type | text | Type of oxygenate blended into the fuel | Ethanol, MTBE, ETBE, None |
| Reid Vapor Pressure (RVP) | number (psi) | Vapor pressure measured at 100 degrees F per ASTM D323 or D5191 | 7.0, 9.0, 10.0, 15.0 |
| Sulfur Content | number (ppm) | Maximum sulfur content in parts per million | 10, 30, 80 |
| Benzene Content | number (% vol) | Maximum benzene content by volume | 0.62, 1.0, 1.3 |
| API Gravity | number | Density measurement on the API gravity scale | 57, 60, 62 |
| Specific Gravity | number | Density relative to water at 60 degrees F | 0.720, 0.745, 0.765 |
| Distillation T50 | number (deg F) | Temperature at which 50 percent of the fuel has evaporated | 170, 200, 220 |
| Distillation T90 | number (deg F) | Temperature at which 90 percent of the fuel has evaporated | 300, 330, 365 |
| Driveability Index (DI) | number | Calculated index of fuel volatility performance per ASTM D4814 | 1000, 1150, 1200 |
| Detergent Additive Package | text | Proprietary additive technology included | Synergy, Invigorate, Techron, V-Power NiTRO+ |
| TOP TIER Certified | boolean | Whether the fuel meets TOP TIER Detergent Gasoline standards | true, false |
| Seasonal Class | enum | Volatility class designation per ASTM D4814 for seasonal conditions | Class AA (summer), Class C (shoulder), Class E (winter) |
| Applicable Standard | text | Primary specification standard the product meets | ASTM D4814, EN 228, Worldwide Fuel Charter Category 4 |
| Volume Unit | enum | Unit of sale for pricing and delivery | Gallon, Litre, Barrel (42 gal) |
| Delivery Method | enum | How the product is supplied | Pump (Retail), Bulk Terminal, Tank Truck, Pipeline, Rail Car |
| Hazmat Class | text | DOT or UN hazardous materials classification | UN1203 Class 3 Flammable Liquid |
| Flash Point | number (deg F) | Minimum temperature at which vapors ignite | -45 |
| Country of Origin | text | Country where the fuel was refined | USA, Canada, UK, Netherlands |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM D4814 and Worldwide Fuel Charter specifications | [ExxonMobil Fuels](https://www.exxon.com/en/our-fuels), [Shell V-Power](https://en.wikipedia.org/wiki/Shell_V-Power), [bp Fuels](https://www.bp.com/en_us/united-states/home/products-and-services/fuels.html), [EIA Gasoline Explained](https://www.eia.gov/energyexplained/gasoline/octane-in-depth.php) |
