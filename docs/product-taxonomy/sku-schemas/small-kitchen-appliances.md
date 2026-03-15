# SKU Schema: Small Kitchen Appliances

**Last updated:** 2026-03-15
**Parent category:** Household Appliances

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer model or part number | K45SSWH, BN601, BOV800XL, 5200 |
| Product Name | text | Full product name including brand, appliance type, and key specs | KitchenAid Classic 4.5 Qt Tilt-Head Stand Mixer White, Vitamix 5200 64oz Blender Black, Breville Smart Oven 1800W |
| URL | text | Direct link to the product page | https://example.com/product/kitchenaid-classic-mixer |
| Price | number | Numeric price per unit, excluding currency symbol | 29.99, 99.95, 349.95, 499.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Appliance manufacturer or brand name | KitchenAid, Vitamix, Breville, Ninja, Cuisinart, Hamilton Beach, Oster, De'Longhi |
| Appliance Type | text | Primary small appliance classification | Blender, Stand Mixer, Hand Mixer, Food Processor, Toaster, Toaster Oven, Coffee Maker, Espresso Machine, Air Fryer, Slow Cooker, Electric Kettle, Juicer, Waffle Maker |
| Wattage | number (W) | Rated electrical power of the motor or heating element | 250, 450, 850, 1000, 1500, 1800 |
| Motor Power | number (HP) | Motor horsepower rating, common for blenders and food processors | 0.5, 1.0, 2.0, 2.2, 3.5 |
| Voltage | text | Electrical supply voltage and frequency requirement | 120V 60Hz, 220-240V 50/60Hz |
| Amperage | number (A) | Maximum electrical current draw | 5, 8, 11.5, 15 |
| Capacity | number (oz) | Jar, bowl, or internal cavity volume in fluid ounces | 14, 32, 48, 64, 72 |
| Capacity (Quarts) | number (qt) | Bowl or container volume in quarts, common for mixers | 3.5, 4.5, 5.0, 5.5, 7.0 |
| Number of Speed Settings | number | Count of selectable speed levels | 2, 3, 5, 10, 11 |
| Speed Range | text (RPM) | Minimum and maximum rotational speed of the motor | 40-200, 50-300, up to 37000 |
| Cooking Functions | text (list) | Available cooking or processing modes for multifunction appliances | Toast, Bake, Broil, Roast, Air Fry, Convection, Reheat, Dehydrate, Slow Cook, Proof |
| Number of Slice/Serving Capacity | number | Toaster slice count or appliance serving size indicator | 2, 4, 6, 12 |
| Interior Dimensions (L x W x H) | text (in) | Usable interior cavity dimensions for toaster ovens and air fryers | 12 x 10 x 4.25, 13.5 x 11.5 x 5.5 |
| Temperature Range Min | number (deg F) | Lowest selectable temperature for heating appliances | 100, 150, 200 |
| Temperature Range Max | number (deg F) | Highest selectable temperature for heating appliances | 400, 450, 480, 500 |
| Colour/Finish | text | Exterior colour or surface finish | White, Black, Red, Empire Red, Contour Silver, Brushed Stainless Steel, Matte Black |
| Material | text | Primary construction material of the body or housing | Stainless Steel, Die-Cast Metal, BPA-Free Tritan, Glass, Plastic, Cast Iron |
| Blade Material | text | Material of cutting blades for blenders and food processors | Stainless Steel, Hardened Stainless Steel, Laser-Cut Stainless Steel |
| Dimensions (L x W x H) | text (in) | Overall exterior dimensions of the appliance | 9 x 8 x 18, 14.1 x 9 x 14, 16.5 x 18.5 x 11.4 |
| Weight | number (lbs) | Product weight without packaging | 4.0, 10.5, 11.9, 22.0, 26.0 |
| Cord Length | number (ft) | Length of the power cord | 2, 3, 4, 6 |
| Lid Type | text | Closure mechanism for blenders and food processors | Snap-On, Twist-Lock, Locking, Vented |
| Dishwasher-Safe Parts | boolean | Whether removable parts are dishwasher safe | true, false |
| BPA Free | boolean | Whether food-contact materials are free of bisphenol A | true, false |
| Included Accessories | text (list) | Additional items included with the product | Tamper, Dough Hook, Wire Whip, Flat Beater, Chopping Blade, Slicing Disc, Recipe Book |
| Warranty | number (years) | Manufacturer warranty period | 1, 2, 3, 5, 7 |
| Certifications | text (list) | Safety and regulatory approvals | UL, ETL, CSA, CE, RoHS, NSF |
| Country of Origin | text | Country where the appliance was manufactured | USA, China, Germany, Italy, Australia |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 sources plus industry standards (IEC 60335, UL 982, NSF/ANSI 2) | [KitchenAid](https://www.kitchenaid.com/countertop-appliances/stand-mixers/tilt-head-stand-mixers/p.classic-series-4-5-quart-tilt-head-stand-mixer.K45SSWH.html), [Vitamix](https://www.vitamix.com/us/en_us/products/5200-standard-getting-started), [Breville](https://www.breville.com/us/en/products/clp.html), [Best Buy](https://www.bestbuy.com/site/home-appliances/small-appliances/abcat0912000.c) |
