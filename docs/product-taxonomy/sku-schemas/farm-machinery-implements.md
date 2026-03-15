# SKU Schema: Farm Machinery & Implements

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.farm_machinery_implements`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | TG-60-Y, 76683, BW15060, 5120M |
| Product Name | text | Full product name including key specs such as type, brand, model, and working width | King Kutter Gear-Driven Rotary Tiller 60 in, John Deere 5120M Utility Tractor, Land Pride RTA1274 Rotary Tiller |
| URL | text | Direct link to the product page | https://example.com/product/rotary-tiller-60in |
| Price | number | Numeric price per unit, excluding currency symbol | 1899.99, 64500.00, 3249.00, 425.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Model Number | text | Manufacturer model designation | 5120M, TG-60-Y, RTA1274, RT1560, CS165 |
| Equipment Type | enum | Primary classification of the machinery or implement | Tractor, Rotary Tiller, Disc Harrow, Plow, Mower, Planter, Combine, Sprayer, Baler, Cultivator, Seeder, Spreader, Post Hole Digger, Box Blade, Scrape Blade |
| Equipment Category | enum | Whether the item is a self-propelled machine or a tractor-mounted implement | Self-Propelled, Towed, Three-Point Mounted, Skid Steer Attachment, Front-Mounted |
| Hitch Category | enum | Three-point hitch category determining pin sizes and spacing | Category 0, Category 1, Category 2, Category 3, Category 4, Quick Hitch |
| Drivetrain Type | enum | Power transmission method for implements | Gear Drive, Chain Drive, Belt Drive, Direct Drive, Hydraulic |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Transmission Type | text | Transmission type for self-propelled equipment | Hydrostatic, Synchronized, Power Shuttle, CVT, Powershift |
| Drive Type | enum | Wheel or track drive configuration | 2WD, 4WD, MFWD, Track |
| Fuel Type | enum | Engine fuel type | Diesel, Gasoline, Electric, Propane |
| Cab Type | enum | Operator station configuration | Open Station, Cab, Premium Cab, Enclosed Cab with HVAC |
| Country of Origin | text | Country where the equipment was manufactured | USA, Japan, India, Italy, Germany, Brazil |
| Engine Horsepower | number (hp) | Gross engine horsepower rating for self-propelled equipment | 65, 120, 225, 410 |
| PTO Horsepower | number (hp) | Power take-off horsepower rating delivered to implements | 53, 105, 180, 360 |
| PTO Speed | text (rpm) | Required or available PTO shaft speed | 540, 540/1000, 540E, 1000 |
| Working Width | number (mm) | Effective cutting, tilling, or working width of the implement | 1219, 1524, 1829, 2134 |
| Working Depth | number (mm) | Maximum working depth for tillage or digging implements | 152, 200, 305, 457 |
| Number of Tines or Blades | number | Count of active cutting or tilling elements | 36, 42, 54, 66 |
| HP Range Required | text | Tractor horsepower range needed to operate the implement | 15-35, 25-50, 40-100, 80-225 |
| Number of Gears | text | Forward and reverse gear count for tractors | 9F/3R, 16F/16R, 32F/16R, 12F/12R |
| Hydraulic Flow Rate | number (L/min) | Hydraulic pump output flow rate | 43.1, 94.0, 97.0, 189.0 |
| Hydraulic System Pressure | number (bar) | Maximum hydraulic system operating pressure | 180, 195, 200, 210 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus SAE 3-point hitch standards (Category 0-4) and ISO tractor classification standards | [John Deere](https://www.deere.com/en/tractors/utility-tractors/5-family-utility-tractors/5120m-utility-tractor/), [TractorData](https://www.tractordata.com/farm-tractors/005/7/9/5792-john-deere-5065e.html), [King Kutter](https://kingkutter.com/rotary-tillers-4), [Agri Supply](https://www.agrisupply.com/farm-machinery-tractor-implements/c/2000000/) |
