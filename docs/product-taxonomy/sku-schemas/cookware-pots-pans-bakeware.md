# SKU Schema: Cookware (Pots, Pans, Bakeware)

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.cookware`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer product identifier, model number, or item code | LS2501-2867, 64090-001, 80116/247DS, L8SK3, 1070LC |
| Product Name | text | Full product name including type, collection, material, and size where applicable | Signature Round Dutch Oven 5.5 Qt, Spirit 3-Ply 10-Pc Stainless Steel Cookware Set, Tri-Ply Clad 12-Inch Skillet |
| URL | text | Direct link to the product page or listing | https://www.example.com/shop/product-name |
| Price | number | Numeric price per selling unit, excluding tax and shipping | 19.90, 79.95, 249.95, 399.95 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, CAD |
| Cookware Type | text | Functional type of the cookware piece | Skillet, Fry Pan, Saute Pan, Saucepan, Saucier, Stockpot, Dutch Oven, Roasting Pan, Wok, Griddle, Grill Pan, Brazier, Sheet Pan, Cake Pan, Loaf Pan, Muffin Pan, Pie Pan, Springform Pan |
| Material | text | Primary body material of the cookware | Cast Iron, Enameled Cast Iron, Stainless Steel, Aluminum, Aluminized Steel, Hard-Anodized Aluminum, Copper, Carbon Steel |
| Coating Type | text | Specific nonstick or protective coating applied to the cooking surface | Americoat Plus, Ceraforce XTREME Ceramic, PTFE, Silicone Nonstick, Enamel, None |
| Lid Material | text | Material of the included lid | Stainless Steel, Tempered Glass, Cast Iron, Enameled Cast Iron |
| Handle Type | text | Style and attachment method of the primary handle | Long Riveted, Loop, Dual Loop, Stay-Cool Riveted, V-Shaped Riveted, Helper Handle, Ergonomic |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Handle Material | text | Material used for the handles | Stainless Steel, Cast Iron, Silicone, Bakelite, Wood |
| Country of Origin | text | Country where the cookware is manufactured | USA, France, China, Vietnam, Brazil, Italy, Belgium |
| Collection | text | Product line, series, or named collection grouping related items | Signature, D3 Stainless Everyday, Chef Collection, Blacklock, Spirit 3-Ply, Naturals, Tri-Ply Clad |
| Construction | text | Layering or build method describing how the cookware body is formed | Tri-Ply Clad, 5-Ply Bonded, Fully Clad, Single-Ply, Cast, Stamped, Drawn |
| Interior Surface | text | Interior cooking surface material or coating type | 18/10 Stainless Steel, Seasoned, Enamel, Ceramic Nonstick, PTFE Nonstick, Bare Cast Iron, Aluminized Steel |
| Exterior Surface | text | Exterior finish material or coating | Mirror-Polished Stainless Steel, Magnetic Stainless Steel, Enamel, Hard-Anodized, Pre-Seasoned |
| Dimensions | text (inches) | Overall exterior dimensions as Length x Width x Height | 10 x 10 x 6.75, 17.75 x 12.75 x 1, 20.98 x 13.98 x 8.98 |
| Shape | enum | Overall shape of the cookware piece | round, oval, square, rectangular |
| Color | text | Exterior color or enamel color of the cookware | Silver, Black, Cerise, Marseille, Flame, White, Indigo, Matte Black, Oyster |
| Lid Included | boolean | Whether a matching lid is included with the piece | true, false |
| Oven Safe Temperature | number (F) | Maximum safe oven temperature in degrees Fahrenheit | 400, 450, 500, 600 |
| Cooktop Compatibility | text (list) | Types of cooktops the cookware is compatible with | Induction, Gas, Electric, Ceramic Glass, Halogen |
| Induction Compatible | boolean | Whether the cookware works on induction cooktops | true, false |
| Dishwasher Safe | boolean | Whether the cookware is safe for dishwasher cleaning | true, false |
| Metal Utensil Safe | boolean | Whether the cooking surface is safe for use with metal utensils | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 35 attributes from 5 companies covering cast iron, enameled cast iron, stainless steel clad, aluminum bakeware, and ceramic nonstick cookware across manufacturer, B2B distributor, and specialty retailer channels | [Lodge](https://www.lodgecastiron.com/pages/cast-iron-product-guide), [Le Creuset / KitchenKapers](https://www.kitchenkapers.com/products/le-creuset-signature-4-5-quart-round-dutch-oven), [Zwilling / Sur La Table](https://www.surlatable.com/product/zwilling-clad-cfx-ceramic-nonstick-10-piece-cookware-set/6697221), [All-Clad](https://www.all-clad.com/cookware/collections/d3-stainless.html), [Tramontina](https://www.tramontina.com/products/signature-tri-ply-clad-stainless-steel-cookware-set) |
