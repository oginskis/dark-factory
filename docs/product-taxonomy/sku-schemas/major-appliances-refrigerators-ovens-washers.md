# SKU Schema: Major Appliances (Refrigerators, Ovens, Washers)

**Last updated:** 2026-03-15
**Parent category:** Household Appliances

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer model or part number | GFE26JYMFS, WFW5605MW, NX60A6511SS |
| Product Name | text | Full product name including brand, type, capacity, and key features | GE 25.6 cu. ft. French Door Refrigerator Fingerprint Resistant Stainless Steel, Samsung 30-in 6.0 cu. ft. Gas Range with Convection |
| URL | text | Direct link to the product page | https://example.com/product/ge-french-door-fridge |
| Price | number | Numeric price per unit, excluding currency symbol | 699.00, 1299.00, 2499.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Appliance manufacturer or brand name | GE, Samsung, LG, Whirlpool, Bosch, KitchenAid, Maytag, Frigidaire |
| Appliance Type | enum | Primary appliance classification | Refrigerator, Range, Wall Oven, Cooktop, Dishwasher, Washing Machine, Dryer, Microwave |
| Appliance Subtype | text | More specific configuration within the appliance type | French Door, Side-by-Side, Top Freezer, Bottom Freezer, Top Load, Front Load, Freestanding, Slide-In, Built-In |
| Total Capacity | number (cu ft) | Total usable interior volume of the appliance | 3.2, 5.8, 20.8, 25.6, 27.7 |
| Refrigerator Capacity | number (cu ft) | Fresh-food compartment volume for refrigerators | 14.1, 17.5, 18.9 |
| Freezer Capacity | number (cu ft) | Freezer compartment volume for refrigerators | 5.0, 7.1, 8.8 |
| Oven Capacity | number (cu ft) | Internal oven cavity volume for ranges and wall ovens | 4.8, 5.3, 5.8, 6.3 |
| Wash Capacity | number (cu ft) | Drum volume for washing machines | 4.2, 4.5, 5.0, 5.8 |
| Fuel/Power Type | enum | Energy source the appliance uses | Electric, Gas, Dual Fuel |
| Voltage | text | Electrical supply voltage requirement | 120V, 240V, 120V/240V |
| Amperage | number (A) | Electrical current draw at rated load | 15, 20, 30, 40, 50 |
| BTU Rating | number (BTU) | Total thermal output for gas burners or heating elements | 5000, 12000, 18000, 55000 |
| Number of Burners/Elements | number | Count of cooktop burners or heating elements | 4, 5, 6 |
| Spin Speed | number (RPM) | Maximum drum rotation speed for washing machines | 1000, 1200, 1400, 1600 |
| Number of Wash Cycles | number | Count of selectable wash programs | 6, 10, 12, 14 |
| Convection | boolean | Whether the oven includes a convection fan for even heat distribution | true, false |
| Self-Cleaning | boolean | Whether the oven has a built-in self-cleaning cycle | true, false |
| Ice Maker | boolean | Whether the refrigerator includes a built-in ice maker | true, false |
| Water Dispenser | enum | Type of water dispenser in a refrigerator | External, Internal, None |
| Finish/Colour | text | Exterior surface finish and colour | Stainless Steel, Fingerprint Resistant Stainless, Black Stainless, White, Slate, Matte Black |
| Width | number (in) | Overall exterior width of the appliance | 24, 28, 30, 33, 36, 48 |
| Height | number (in) | Overall exterior height of the appliance | 33.5, 36, 46.5, 69.25, 70 |
| Depth | number (in) | Overall exterior depth of the appliance (excluding handles) | 24, 27, 29, 33.62, 35.75 |
| Weight | number (lbs) | Shipping or product weight | 150, 225, 300, 400 |
| Counter Depth | boolean | Whether the refrigerator is designed to sit flush with standard kitchen counters | true, false |
| ADA Compliant | boolean | Whether the appliance meets ADA accessibility requirements | true, false |
| Noise Level | number (dBA) | Sound level during operation, measured in A-weighted decibels | 38, 42, 50, 72, 77 |
| Energy Star | boolean | Whether the appliance is Energy Star certified | true, false |
| Annual Energy Use | number (kWh) | Estimated yearly energy consumption per the energy label | 300, 450, 630, 700 |
| Energy Efficiency Class | text | Energy label rating per EU or regional labelling scheme | A, B, C, D, E, F, G |
| Annual Water Use | number (L) | Estimated yearly water consumption for washers and dishwashers | 7000, 9000, 11000 |
| Certifications | text (list) | Safety, performance, and environmental certifications | UL, CSA, CE, Energy Star, AHAM Verifide, NSF |
| Warranty | text | Manufacturer warranty summary | 1-Year Parts and Labour, 5-Year Compressor, 10-Year Motor |
| Country of Origin | text | Country where the appliance was manufactured | USA, Mexico, South Korea, China, Germany |
| Sabbath Mode | boolean | Whether the appliance includes a Sabbath/religious observance mode | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus industry standards (AHAM, IEC 60335, EU Energy Labelling) | [GE Appliances](https://www.geappliances.com/ge-appliances/kitchen/refrigerators/), [Best Buy](https://www.bestbuy.com/site/electronics/home-appliances/abcat0900000.c), [Lowes](https://www.lowes.com/c/Appliances), [Whirlpool](https://www.whirlpool.com/blog/kitchen/how-many-btus-for-gas-range.html) |
