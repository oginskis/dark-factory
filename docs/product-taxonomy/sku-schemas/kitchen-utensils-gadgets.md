# SKU Schema: Kitchen Utensils & Gadgets

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer item number uniquely identifying the product | 92252010, 37160-032-0, 407PW10, PRO-1007525 |
| Product Name | text | Full product name including brand, size, and type designation | 10" High Heat Silicone Spatula, Pro Tools Silicone Frying Pan Turner, 12" Stainless Steel Piano Whisk |
| URL | text | Direct link to the product page on the manufacturer or retailer site | https://www.zwilling.com/us/zwilling-pro-tools-silicone-spatula-37160-032/37160-032-0.html |
| Price | number | Numeric unit price without currency symbol, representing MSRP or list price | 4.19, 15.99, 21.99, 55.00 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | OXO, Zwilling, Vollrath, Joseph Joseph, KitchenAid, Ateco, Mercer Culinary |
| Manufacturer Part Number | text | Manufacturer-assigned model or part number distinct from the retailer SKU | 52010, 37160-032, 1388, 74391 |
| UPC | text | Universal Product Code or EAN barcode identifier | 719812003160, 014963013885, 4009839402036 |
| Utensil Type | text | Specific type of utensil or gadget within the subcategory | Spatula, Tongs, Whisk, Peeler, Garlic press, Ladle, Turner, Grater, Can opener, Pizza cutter, Masher |
| Product Line | text | Product series, collection, or family name | Good Grips, Pro Tools, Elevate, Classic, Nest, Z-Cut |
| Primary Material | text | Main material the functional part of the utensil is made from | Stainless steel, Silicone, Nylon, Wood, Plastic, Exoglass |
| Handle Material | text | Material of the handle or grip portion | Stainless steel, Wood, Nylon, Polypropylene, Silicone, Rubber |
| Color | text | Primary color or finish of the product | Black, Red, Silver, White, Gray, Blue, Green, Multicolor |
| Overall Length | number (inches) | Total length of the utensil from end to end | 8.25, 10, 12, 13.8, 14.8 |
| Blade Length | number (inches) | Length of the functional blade, head, or working end where applicable | 3.25, 4.75, 8, 10 |
| Blade Width | number (inches) | Width of the functional blade or head where applicable | 1.25, 2, 2.25, 3.38 |
| Handle Length | number (inches) | Length of the handle portion | 4.92, 5.06, 6.63 |
| Weight | number (lbs) | Net weight of the individual utensil | 0.15, 0.28, 0.31 |
| Max Temperature | number (F) | Maximum safe operating temperature for heat-resistant utensils | 400, 450, 480, 500 |
| Dishwasher Safe | boolean | Whether the utensil is safe for dishwasher cleaning | true, false |
| Nonstick Safe | boolean | Whether the utensil is safe for use on nonstick cookware surfaces | true, false |
| BPA Free | boolean | Whether the product is certified free of bisphenol A | true, false |
| Style | enum | Functional style variant affecting how the utensil works | Solid, Slotted, Perforated, Grooved |
| Edge Style | enum | Shape or finish of the working edge | Straight, Beveled, Rounded, Scalloped, Serrated, Square |
| Set Size | number | Number of pieces included when sold as a set, 1 for individual items | 1, 5, 6, 10, 15, 20 |
| Set Contents | text (list) | Items included in a utensil set | Spatula, Ladle, Slotted spoon, Tongs, Peeler, Whisk, Measuring cups |
| Hanging Feature | enum | Storage feature for hanging the utensil | Hanging hole, Hanging loop, None |
| Locking Mechanism | boolean | Whether the utensil has a locking feature for compact storage | true, false |
| NSF Certified | boolean | Whether the product holds NSF International food safety certification | true, false |
| Food Contact Certifications | text (list) | Food safety and material compliance certifications | CE, ISO 9001, LFGB, EU 1935/2004 |
| Country of Origin | text | Country where the product is manufactured | China, USA, Germany, Japan, France |
| Shipping Weight | number (lbs) | Weight of the product including packaging for shipping | 0.05, 0.24, 0.32, 1.0 |
| Care Instructions | enum | Recommended cleaning method | Hand wash only, Dishwasher safe, Hand wash recommended |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 5 companies spanning manufacturer, B2B distributor, specialty retailer, and e-commerce channels | [WebstaurantStore](https://www.webstaurantstore.com/56699/spatulas-spoonulas.html), [Zwilling](https://www.zwilling.com/us/zwilling-pro-tools-silicone-spatula-37160-032/37160-032-0.html), [OXO via Target](https://www.target.com/p/oxo-12-tongs/-/A-13567297), [Joseph Joseph](https://us.josephjoseph.com/collections/gadgets-utensils), [KitchenAid via EverythingKitchens](https://www.everythingkitchens.com/ka-5-piece-classic-utensil-set-ekb-lbclassic5.html) |
