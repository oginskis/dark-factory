# SKU Schema: Gasoline & Motor Fuels

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.gasoline_motor_fuels`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier or distributor product identifier | EXX-UNL87, SHL-VPWR93, BP-E15-REG |
| Product Name | product_name | text | — | yes | Full product name including brand, grade, and formulation | Shell V-Power NiTRO+ Premium 93, ExxonMobil Synergy Regular 87, bp Amoco Ultimate 93 |
| URL | url | text | — | yes | Direct link to the product data sheet or listing page | https://example.com/fuels/premium-93 |
| Price | price | number | — | yes | Numeric price per gallon or litre at time of listing, excluding currency symbol | 3.29, 3.89, 4.19 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Fuel Type | fuel_type | enum | — | — | Primary fuel classification | Conventional Gasoline, Reformulated Gasoline (RFG), E85 Flex Fuel, Racing Fuel, Aviation Gasoline |
| Grade | grade | enum | — | — | Market grade designation | Regular, Midgrade, Premium, Super Premium |
| Oxygenate Type | oxygenate_type | text | — | — | Type of oxygenate blended into the fuel | Ethanol, MTBE, ETBE, None |
| Seasonal Class | seasonal_class | enum | — | — | Volatility class designation per ASTM D4814 for seasonal conditions | Class AA (summer), Class C (shoulder), Class E (winter) |
| Hazmat Class | hazmat_class | text | — | — | DOT or UN hazardous materials classification | UN1203 Class 3 Flammable Liquid |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the fuel was refined | USA, Canada, UK, Netherlands |
| Octane Rating (AKI) | octane_rating_aki | number | — | — | Anti-Knock Index (R+M)/2 as posted at the pump | 87, 89, 91, 93, 100 |
| Research Octane Number (RON) | research_octane_number_ron | number | — | — | Octane measured via the Research method | 91, 95, 98, 100 |
| Motor Octane Number (MON) | motor_octane_number_mon | number | — | — | Octane measured via the Motor method | 82, 85, 87, 89 |
| Ethanol Content | ethanol_content | text | % vol | — | Volume percentage of ethanol blended into the fuel | E0 (0%), E10 (10%), E15 (15%), E85 (85%) |
| Reid Vapor Pressure (RVP) | reid_vapor_pressure_rvp | number | psi | — | Vapor pressure measured at 100 degrees F per ASTM D323 or D5191 | 7.0, 9.0, 10.0, 15.0 |
| Sulfur Content | sulfur_content | number | ppm | — | Maximum sulfur content in parts per million | 10, 30, 80 |
| Benzene Content | benzene_content | number | % vol | — | Maximum benzene content by volume | 0.62, 1.0, 1.3 |
| API Gravity | api_gravity | number | — | — | Density measurement on the API gravity scale | 57, 60, 62 |
| Specific Gravity | specific_gravity | number | — | — | Density relative to water at 60 degrees F | 0.720, 0.745, 0.765 |
| Distillation T50 | distillation_t50 | number | deg F | — | Temperature at which 50 percent of the fuel has evaporated | 170, 200, 220 |
| Distillation T90 | distillation_t90 | number | deg F | — | Temperature at which 90 percent of the fuel has evaporated | 300, 330, 365 |
| Driveability Index (DI) | driveability_index_di | number | — | — | Calculated index of fuel volatility performance per ASTM D4814 | 1000, 1150, 1200 |
| Detergent Additive Package | detergent_additive_package | text | — | — | Proprietary additive technology included | Synergy, Invigorate, Techron, V-Power NiTRO+ |
| TOP TIER Certified | top_tier_certified | boolean | — | — | Whether the fuel meets TOP TIER Detergent Gasoline standards | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM D4814 and Worldwide Fuel Charter specifications | [ExxonMobil Fuels](https://www.exxon.com/en/our-fuels), [Shell V-Power](https://en.wikipedia.org/wiki/Shell_V-Power), [bp Fuels](https://www.bp.com/en_us/united-states/home/products-and-services/fuels.html), [EIA Gasoline Explained](https://www.eia.gov/energyexplained/gasoline/octane-in-depth.php) |
