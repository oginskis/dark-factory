# SKU Schema: Small Kitchen Appliances

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.small_kitchen`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer model or part number | K45SSWH, BN601, BOV800XL, 5200 |
| Product Name | product_name | text | — | yes | Full product name including brand, appliance type, and key specs | KitchenAid Classic 4.5 Qt Tilt-Head Stand Mixer White, Vitamix 5200 64oz Blender Black, Breville Smart Oven 1800W |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/kitchenaid-classic-mixer |
| Price | price | number | — | yes | Numeric price per unit, excluding currency symbol | 29.99, 99.95, 349.95, 499.95 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Appliance Type | appliance_type | text | — | — | Primary small appliance classification | Blender, Stand Mixer, Hand Mixer, Food Processor, Toaster, Toaster Oven, Coffee Maker, Espresso Machine, Air Fryer, Slow Cooker, Electric Kettle, Juicer, Waffle Maker |
| Material | material | text | — | — | Primary construction material of the body or housing | Stainless Steel, Die-Cast Metal, BPA-Free Tritan, Glass, Plastic, Cast Iron |
| Blade Material | blade_material | text | — | — | Material of cutting blades for blenders and food processors | Stainless Steel, Hardened Stainless Steel, Laser-Cut Stainless Steel |
| Lid Type | lid_type | text | — | — | Closure mechanism for blenders and food processors | Snap-On, Twist-Lock, Locking, Vented |
| Country of Origin | country_of_origin | text | — | — | Country where the appliance was manufactured | USA, China, Germany, Italy, Australia |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Wattage | wattage | number | W | — | Rated electrical power of the motor or heating element | 250, 450, 850, 1000, 1500, 1800 |
| Motor Power | motor_power | number | HP | — | Motor horsepower rating, common for blenders and food processors | 0.5, 1.0, 2.0, 2.2, 3.5 |
| Amperage | amperage | number | A | — | Maximum electrical current draw | 5, 8, 11.5, 15 |
| Number of Speed Settings | number_of_speed_settings | number | — | — | Count of selectable speed levels | 2, 3, 5, 10, 11 |
| Speed Range | speed_range | text | RPM | — | Minimum and maximum rotational speed of the motor | 40-200, 50-300, up to 37000 |
| Cooking Functions | cooking_functions | text (list) | — | — | Available cooking or processing modes for multifunction appliances | Toast, Bake, Broil, Roast, Air Fry, Convection, Reheat, Dehydrate, Slow Cook, Proof |
| Interior Dimensions (L x W x H) | interior_dimensions_l_x_w_x_h | text | in | — | Usable interior cavity dimensions for toaster ovens and air fryers | 12 x 10 x 4.25, 13.5 x 11.5 x 5.5 |
| Temperature Range Min | temperature_range_min | number | deg F | — | Lowest selectable temperature for heating appliances | 100, 150, 200 |
| Temperature Range Max | temperature_range_max | number | deg F | — | Highest selectable temperature for heating appliances | 400, 450, 480, 500 |
| Colour/Finish | colourfinish | text | — | — | Exterior colour or surface finish | White, Black, Red, Empire Red, Contour Silver, Brushed Stainless Steel, Matte Black |
| Dimensions (L x W x H) | dimensions_l_x_w_x_h | text | in | — | Overall exterior dimensions of the appliance | 9 x 8 x 18, 14.1 x 9 x 14, 16.5 x 18.5 x 11.4 |
| Dishwasher-Safe Parts | dishwasher-safe_parts | boolean | — | — | Whether removable parts are dishwasher safe | true, false |
| BPA Free | bpa_free | boolean | — | — | Whether food-contact materials are free of bisphenol A | true, false |
| Included Accessories | included_accessories | text (list) | — | — | Additional items included with the product | Tamper, Dough Hook, Wire Whip, Flat Beater, Chopping Blade, Slicing Disc, Recipe Book |
| Warranty | warranty | number | years | — | Manufacturer warranty period | 1, 2, 3, 5, 7 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 sources plus industry standards (IEC 60335, UL 982, NSF/ANSI 2) | [KitchenAid](https://www.kitchenaid.com/countertop-appliances/stand-mixers/tilt-head-stand-mixers/p.classic-series-4-5-quart-tilt-head-stand-mixer.K45SSWH.html), [Vitamix](https://www.vitamix.com/us/en_us/products/5200-standard-getting-started), [Breville](https://www.breville.com/us/en/products/clp.html), [Best Buy](https://www.bestbuy.com/site/home-appliances/small-appliances/abcat0912000.c) |
