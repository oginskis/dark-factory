# SKU Schema: Major Appliances (Refrigerators, Ovens, Washers)

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.major_appliances`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer model or part number | GFE26JYMFS, WFW5605MW, NX60A6511SS |
| Product Name | product_name | text | Full product name including brand, type, capacity, and key features | GE 25.6 cu. ft. French Door Refrigerator Fingerprint Resistant Stainless Steel, Samsung 30-in 6.0 cu. ft. Gas Range with Convection |
| URL | url | text | Direct link to the product page | https://example.com/product/ge-french-door-fridge |
| Price | price | number | Numeric price per unit, excluding currency symbol | 699.00, 1299.00, 2499.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Appliance Type | appliance_type | enum | Primary appliance classification | Refrigerator, Range, Wall Oven, Cooktop, Dishwasher, Washing Machine, Dryer, Microwave |
| Appliance Subtype | appliance_subtype | text | More specific configuration within the appliance type | French Door, Side-by-Side, Top Freezer, Bottom Freezer, Top Load, Front Load, Freestanding, Slide-In, Built-In |
| Fuel/Power Type | fuelpower_type | enum | Energy source the appliance uses | Electric, Gas, Dual Fuel |
| Energy Efficiency Class | energy_efficiency_class | text | Energy label rating per EU or regional labelling scheme | A, B, C, D, E, F, G |
| Country of Origin | country_of_origin | text | Country where the appliance was manufactured | USA, Mexico, South Korea, China, Germany |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Amperage | amperage | number (A) | Electrical current draw at rated load | 15, 20, 30, 40, 50 |
| BTU Rating | btu_rating | number (BTU) | Total thermal output for gas burners or heating elements | 5000, 12000, 18000, 55000 |
| Number of Burners/Elements | number_of_burnerselements | number | Count of cooktop burners or heating elements | 4, 5, 6 |
| Spin Speed | spin_speed | number (RPM) | Maximum drum rotation speed for washing machines | 1000, 1200, 1400, 1600 |
| Number of Wash Cycles | number_of_wash_cycles | number | Count of selectable wash programs | 6, 10, 12, 14 |
| Convection | convection | boolean | Whether the oven includes a convection fan for even heat distribution | true, false |
| Self-Cleaning | self-cleaning | boolean | Whether the oven has a built-in self-cleaning cycle | true, false |
| Ice Maker | ice_maker | boolean | Whether the refrigerator includes a built-in ice maker | true, false |
| Water Dispenser | water_dispenser | enum | Type of water dispenser in a refrigerator | External, Internal, None |
| Finish/Colour | finishcolour | text | Exterior surface finish and colour | Stainless Steel, Fingerprint Resistant Stainless, Black Stainless, White, Slate, Matte Black |
| Width | width | number (in) | Overall exterior width of the appliance | 24, 28, 30, 33, 36, 48 |
| Height | height | number (in) | Overall exterior height of the appliance | 33.5, 36, 46.5, 69.25, 70 |
| Depth | depth | number (in) | Overall exterior depth of the appliance (excluding handles) | 24, 27, 29, 33.62, 35.75 |
| ADA Compliant | ada_compliant | boolean | Whether the appliance meets ADA accessibility requirements | true, false |
| Noise Level | noise_level | number (dBA) | Sound level during operation, measured in A-weighted decibels | 38, 42, 50, 72, 77 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus industry standards (AHAM, IEC 60335, EU Energy Labelling) | [GE Appliances](https://www.geappliances.com/ge-appliances/kitchen/refrigerators/), [Best Buy](https://www.bestbuy.com/site/electronics/home-appliances/abcat0900000.c), [Lowes](https://www.lowes.com/c/Appliances), [Whirlpool](https://www.whirlpool.com/blog/kitchen/how-many-btus-for-gas-range.html) |
