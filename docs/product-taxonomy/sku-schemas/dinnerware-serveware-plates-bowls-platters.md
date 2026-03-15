# SKU Schema: Dinnerware & Serveware (Plates, Bowls, Platters)

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.dinnerware_serveware`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Unique product identifier assigned by the manufacturer or retailer | 303KSE21, 1042392620, 8034-406D |
| Product Name | product_name | text | Human-readable name of the dinnerware item, typically including type, size, and collection | 10.5 Coupe Dinner Plate Set of 4, Bright White Square Porcelain Plate 12 in, Matte Slate Round Deep Plate |
| URL | url | text | Link to the product page or catalog listing | https://example.com/products/dinner-plate-10 |
| Price | price | number | Numeric price value per unit or per set, excluding currency symbol | 24.99, 79.99, 10.33 |
| Currency | currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, JPY |
| Product Type | product_type | enum | Functional type of the dinnerware piece | Dinner Plate, Salad Plate, Dessert Plate, Bread Plate, Charger Plate, Soup Bowl, Cereal Bowl, Pasta Bowl, Serving Bowl, Platter, Deep Plate |
| Material | material | enum | Primary material composition of the item | Porcelain, Bone China, Stoneware, Melamine, Fine China, Earthenware, Glass, Vitrified Porcelain |
| Country of Origin | country_of_origin | text | Country where the item was manufactured | USA, Germany, United Arab Emirates, Japan, China |
| Diameter | diameter | number (inches) | Diameter of round items or longest dimension of non-round items | 10.5, 12, 7.125, 10.67 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Manufacturer Part Number | manufacturer_part_number | text | Part or model number assigned by the manufacturer, which may differ from the retailer SKU | CN-B7, MFFDGD26GB, 8034 |
| UPC | upc | text | Universal Product Code barcode identifier | 400012040849, 037725606545 |
| Collection | collection | text | Named product line, series, or collection the item belongs to | Manufacture, Colorwave, Metal Fusion, Crafted, Simplicity |
| Pattern | pattern | text | Decorative pattern or design name applied to the item | Graphite, Bright White, Matte Slate, Bloomington Road, French Garden |
| Shape | shape | enum | Overall geometric shape of the item | Round, Square, Coupe, Oval, Rectangular, Triangular |
| Rim Style | rim_style | enum | Edge or rim design of plates and bowls | Wide Rim, Raised Rim, Coupe (Rimless), Narrow Rim, Slimline |
| Color | color | text | Primary visible color of the item | Bright White, Black, Graphite, Cream, Midnight Blue, Matte Slate |
| Finish | finish | enum | Surface finish or texture of the glaze | Glossy, Matte, Reactive Glaze, Crackle Glaze, Unglazed |
| Width | width | number (inches) | Overall width of the item | 12, 7.25, 8.25 |
| Height | height | number (inches) | Overall height or depth of the item | 1.125, 0.83, 4, 2.75 |
| Dishwasher Safe | dishwasher_safe | boolean | Whether the item is safe for dishwasher cleaning | Yes, No |
| Microwave Safe | microwave_safe | boolean | Whether the item is safe for microwave use | Yes, No |
| Oven Safe | oven_safe | boolean | Whether the item is safe for conventional oven use | Yes, No |
| Oven Safe Temperature | oven_safe_temperature | number (F) | Maximum oven-safe temperature in degrees Fahrenheit | 450, 572 |
| Freezer Safe | freezer_safe | boolean | Whether the item is safe for freezer storage | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 33 attributes from 4 companies covering B2B distributor, premium manufacturers, and commercial hospitality suppliers | [WebstaurantStore](https://www.webstaurantstore.com/restaurant-dinnerware.html), [Villeroy & Boch](https://www.villeroy-boch.com/c/dinnerware/plates/), [RAK Porcelain](https://www.rakporcelain.com/wr-en), [Noritake](https://noritakechina.com/) |
