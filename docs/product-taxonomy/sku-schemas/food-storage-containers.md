# SKU Schema: Food Storage Containers

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.food_storage_containers`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Unique product identifier or article number assigned by manufacturer or retailer | FG572024CLR, 11233400, 19567111, 1139099 |
| Product Name | product_name | text | Full product name including brand, line, and capacity descriptor | CamSquare 4 Qt Clear Square Polycarbonate Food Storage Container, Simply Store 6-Piece Glass Storage Set, One Touch Fresh Rectangular 12 Cup |
| URL | url | text | Direct link to the product page or listing on the manufacturer or retailer website | https://www.rubbermaidcommercial.com/foodservice/food-storage/round-storage-containers/ |
| Price | price | number | Unit price of the container or set, excluding tax and shipping | 8.29, 13.00, 24.00, 11.99, 27.49 |
| Currency | currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, CAD |
| Lid Material | lid_material | text | Material of the lid or cover, if included or sold separately | Polypropylene, Silicone rubber, BPA-free plastic, Polycarbonate |
| Lid Type | lid_type | text | Closure mechanism or style of the lid | Snap-lock, Push-button airtight, Silicone vacuum, Screw-on, Sliding |
| Seal Type | seal_type | enum | Type of seal provided by the lid | Airtight, Leak-proof, Vacuum, Standard, Splash-proof |
| Country of Origin | country_of_origin | text | Country where the product is manufactured | USA, China, France, Belgium |
| Capacity | capacity | text | Volume the container holds, expressed in common units | 4 qt, 12 cup, 2.85 L, 34 oz, 1.4 L, 6.0 qt |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Product Line | product_line | text | Named product series or collection within the brand | CamSquare Classic, Simply Store, One Touch Fresh, POP, IKEA 365+, Modular Mates, Voila Glass |
| Shape | shape | enum | Geometric shape of the container | Round, Square, Rectangular |
| Width | width | number (in) | Outer width of the container | 7.25, 6.0, 4.72 |
| Height | height | number (in) | Outer height of the container | 7.4, 2.25, 14.0 |
| Color | color | text | Color of the container body or lid | Clear, White, Translucent, Red lid, Yellow lid, Green |
| Lid Included | lid_included | boolean | Whether a lid is sold with the container or must be purchased separately | true, false |
| Microwave Safe | microwave_safe | boolean | Whether the container is safe for use in a microwave oven | true, false |
| Freezer Safe | freezer_safe | boolean | Whether the container is safe for freezer storage | true, false |
| Dishwasher Safe | dishwasher_safe | boolean | Whether the container is safe for dishwasher cleaning | true, false |
| Oven Safe | oven_safe | boolean | Whether the container is safe for use in a conventional oven | true, false |
| Temperature Range Min | temperature_range_min | number (F) | Minimum safe operating or storage temperature in Fahrenheit | -40, -13, 32 |
| Temperature Range Max | temperature_range_max | number (F) | Maximum safe operating or storage temperature in Fahrenheit | 150, 210, 572 |
| BPA Free | bpa_free | boolean | Whether the product is certified free of bisphenol A | true, false |
| Graduation Markings | graduation_markings | boolean | Whether the container has measurement markings for portioning | true, false |
| Stackable | stackable | boolean | Whether containers can be stacked on top of each other for space-efficient storage | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 5 companies spanning manufacturer, distributor, and retail sources | [Tupperware](https://www.tupperware.com/collections/food-storage), [Rubbermaid Commercial](https://www.rubbermaidcommercial.com/foodservice/food-storage/), [Cambro via WebstaurantStore](https://www.webstaurantstore.com/cambro-4sfscw135-4-qt-clear-square-polycarbonate-food-storage-container-with-winter-rose-gradations/2144SFSCW.html), [IKEA](https://www.ikea.com/us/en/cat/food-storage-organizing-15937/), [Pyrex](https://pyrexhome.com/products/pyrex-simply-store-6-piece-glass-storage-set) |
