# SKU Schema: Kitchen Utensils & Gadgets

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.utensils_gadgets`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or retailer item number uniquely identifying the product | 92252010, 37160-032-0, 407PW10, PRO-1007525 |
| Product Name | product_name | text | — | yes | Full product name including brand, size, and type designation | 10" High Heat Silicone Spatula, Pro Tools Silicone Frying Pan Turner, 12" Stainless Steel Piano Whisk |
| URL | url | text | — | yes | Direct link to the product page on the manufacturer or retailer site | https://www.zwilling.com/us/zwilling-pro-tools-silicone-spatula-37160-032/37160-032-0.html |
| Price | price | number | — | yes | Numeric unit price without currency symbol, representing MSRP or list price | 4.19, 15.99, 21.99, 55.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code for the listed price | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Utensil Type | utensil_type | text | — | — | Specific type of utensil or gadget within the subcategory | Spatula, Tongs, Whisk, Peeler, Garlic press, Ladle, Turner, Grater, Can opener, Pizza cutter, Masher |
| Primary Material | primary_material | text | — | — | Main material the functional part of the utensil is made from | Stainless steel, Silicone, Nylon, Wood, Plastic, Exoglass |
| Handle Material | handle_material | text | — | — | Material of the handle or grip portion | Stainless steel, Wood, Nylon, Polypropylene, Silicone, Rubber |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | China, USA, Germany, Japan, France |
| Overall Length | overall_length | number | inches | — | Total length of the utensil from end to end | 8.25, 10, 12, 13.8, 14.8 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Manufacturer Part Number | manufacturer_part_number | text | — | — | Manufacturer-assigned model or part number distinct from the retailer SKU | 52010, 37160-032, 1388, 74391 |
| UPC | upc | text | — | — | Universal Product Code or EAN barcode identifier | 719812003160, 014963013885, 4009839402036 |
| Product Line | product_line | text | — | — | Product series, collection, or family name | Good Grips, Pro Tools, Elevate, Classic, Nest, Z-Cut |
| Color | color | text | — | — | Primary color or finish of the product | Black, Red, Silver, White, Gray, Blue, Green, Multicolor |
| Blade Width | blade_width | number | inches | — | Width of the functional blade or head where applicable | 1.25, 2, 2.25, 3.38 |
| Max Temperature | max_temperature | number | F | — | Maximum safe operating temperature for heat-resistant utensils | 400, 450, 480, 500 |
| Dishwasher Safe | dishwasher_safe | boolean | — | — | Whether the utensil is safe for dishwasher cleaning | true, false |
| Nonstick Safe | nonstick_safe | boolean | — | — | Whether the utensil is safe for use on nonstick cookware surfaces | true, false |
| BPA Free | bpa_free | boolean | — | — | Whether the product is certified free of bisphenol A | true, false |
| Style | style | enum | — | — | Functional style variant affecting how the utensil works | Solid, Slotted, Perforated, Grooved |
| Edge Style | edge_style | enum | — | — | Shape or finish of the working edge | Straight, Beveled, Rounded, Scalloped, Serrated, Square |
| Set Contents | set_contents | text (list) | — | — | Items included in a utensil set | Spatula, Ladle, Slotted spoon, Tongs, Peeler, Whisk, Measuring cups |
| Hanging Feature | hanging_feature | enum | — | — | Storage feature for hanging the utensil | Hanging hole, Hanging loop, None |
| Locking Mechanism | locking_mechanism | boolean | — | — | Whether the utensil has a locking feature for compact storage | true, false |
| NSF Certified | nsf_certified | boolean | — | — | Whether the product holds NSF International food safety certification | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 5 companies spanning manufacturer, B2B distributor, specialty retailer, and e-commerce channels | [WebstaurantStore](https://www.webstaurantstore.com/56699/spatulas-spoonulas.html), [Zwilling](https://www.zwilling.com/us/zwilling-pro-tools-silicone-spatula-37160-032/37160-032-0.html), [OXO via Target](https://www.target.com/p/oxo-12-tongs/-/A-13567297), [Joseph Joseph](https://us.josephjoseph.com/collections/gadgets-utensils), [KitchenAid via EverythingKitchens](https://www.everythingkitchens.com/ka-5-piece-classic-utensil-set-ekb-lbclassic5.html) |
