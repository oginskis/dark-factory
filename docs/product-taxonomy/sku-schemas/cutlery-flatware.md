# SKU Schema: Cutlery & Flatware

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.cutlery_flatware`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer product identifier, article number, or item code | 22772-345, B1011020Al21, H147020A, 5.4003.12 |
| Product Name | text | Full product name including pattern, piece type, and set size where applicable | Vintage 45-pc Flatware Set, Bistro 5 Piece Place Setting, Patriot Dinner Fork |
| URL | text | Direct link to the product page or listing | https://www.example.com/shop/product-name |
| Price | number | Numeric price per selling unit, excluding tax and shipping | 29.99, 79.95, 149.99, 525.00 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, AUD |
| Piece Type | text | Functional type of the individual flatware piece | Dinner Fork, Salad Fork, Dinner Knife, Steak Knife, Butter Spreader, Teaspoon, Soup Spoon, Tablespoon, Dessert Spoon, Iced Tea Spoon, Serving Spoon, Serving Fork, Sugar Spoon, Demitasse Spoon, Gravy Ladle |
| Material | text | Primary material composition of the flatware body | 18/10 Stainless Steel, 18/8 Stainless Steel, 18/0 Stainless Steel, Sterling Silver, Silver-Plated, Gold-Plated |
| Stainless Steel Grade | text | Chromium/nickel alloy ratio indicating corrosion resistance and quality tier | 18/10, 18/8, 18/0, 13/0 |
| Blade Material | text | Material used for knife blades, which may differ from handles | 13/0 Stainless Steel, 18/10 Stainless Steel, High-Carbon Stainless Steel |
| Weight Class | enum | Industry weight classification indicating gauge thickness | medium, heavy, extra heavy, forged |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the flatware is manufactured | USA, China, Vietnam, France, Italy, Indonesia, Germany, Portugal |
| Set Composition | text | Breakdown of piece types included in a set | 8 Dinner Forks, 8 Salad Forks, 8 Dinner Knives, 8 Soup Spoons, 8 Teaspoons, 1 Serving Spoon, 1 Serving Fork, 1 Butter Knife, 1 Sugar Spoon |
| Edge Type | enum | Profile of the knife blade edge | serrated, straight, micro-serrated |
| Collection | text | Product line, pattern, or series name grouping related designs | Vintage, Bistro, Patriot, Albi, Monolith, Royal Pacific |
| Service For | number | Number of place settings the set is designed to serve | 1, 4, 8, 12 |
| Finish | text | Surface treatment or visual finish of the flatware | Mirror Polish, Brushed, Satin, Matte, Antiqued, Hammered, Distressed, Tumbled, Sandblasted |
| Color | text | Primary color or coating color of the flatware | Silver, Gold, Matte Black, Rose Gold, Copper, Champagne |
| Construction Method | enum | Manufacturing process used to form the flatware | forged, stamped |
| Handle Construction | enum | Whether knife handles are solid or hollow | solid, hollow-handle |
| Sizing Standard | enum | Whether the flatware follows American or European dimensional conventions | American, Continental/European |
| Handle Style | text | Decorative design category of the handle | Plain, Beaded, Hammered, Shell, Floral/Scroll, Textured, Rimmed, Square |
| Dishwasher Safe | boolean | Whether the flatware is safe for dishwasher cleaning | true, false |
| Warranty | text | Duration or type of manufacturer warranty | 25 Year, Lifetime, Limited Lifetime |
| UPC | text | Universal Product Code barcode identifier | 845033013531, 079914029114 |
| PVD Coating | boolean | Whether the flatware has a Physical Vapor Deposition coating for color durability | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 5 companies covering stainless steel and silver flatware across manufacturer, B2B distributor, and retail channels | [ZWILLING](https://www.zwilling.com/us/zwilling-vintage-45-pc-flatware-set-18%2F10-stainless-steel--22772-345/22772-345-0.html), [Oneida / EverythingKitchens](https://www.everythingkitchens.com/oneida-monolith-18-0-stainless-steel-20-piece-flatware-set.html), [Fortessa](https://www.fortessa.com/flatware), [Liberty Tabletop / Silver Superstore](https://www.silversuperstore.com/Liberty-Tabletop-Stainless-Steel-Flatware/departments/4076/), [WebstaurantStore](https://www.webstaurantstore.com/3897/flatware.html) |
