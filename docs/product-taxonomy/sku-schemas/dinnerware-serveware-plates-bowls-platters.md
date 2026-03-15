# SKU Schema: Dinnerware & Serveware (Plates, Bowls, Platters)

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Unique product identifier assigned by the manufacturer or retailer | 303KSE21, 1042392620, 8034-406D |
| Product Name | text | Human-readable name of the dinnerware item, typically including type, size, and collection | 10.5 Coupe Dinner Plate Set of 4, Bright White Square Porcelain Plate 12 in, Matte Slate Round Deep Plate |
| URL | text | Link to the product page or catalog listing | https://example.com/products/dinner-plate-10 |
| Price | number | Numeric price value per unit or per set, excluding currency symbol | 24.99, 79.99, 10.33 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name of the product | Villeroy & Boch, Noritake, RAK Porcelain, CAC China, Acopa, Bon Chef |
| Manufacturer Part Number | text | Part or model number assigned by the manufacturer, which may differ from the retailer SKU | CN-B7, MFFDGD26GB, 8034 |
| UPC | text | Universal Product Code barcode identifier | 400012040849, 037725606545 |
| Collection | text | Named product line, series, or collection the item belongs to | Manufacture, Colorwave, Metal Fusion, Crafted, Simplicity |
| Pattern | text | Decorative pattern or design name applied to the item | Graphite, Bright White, Matte Slate, Bloomington Road, French Garden |
| Product Type | enum | Functional type of the dinnerware piece | Dinner Plate, Salad Plate, Dessert Plate, Bread Plate, Charger Plate, Soup Bowl, Cereal Bowl, Pasta Bowl, Serving Bowl, Platter, Deep Plate |
| Material | enum | Primary material composition of the item | Porcelain, Bone China, Stoneware, Melamine, Fine China, Earthenware, Glass, Vitrified Porcelain |
| Shape | enum | Overall geometric shape of the item | Round, Square, Coupe, Oval, Rectangular, Triangular |
| Rim Style | enum | Edge or rim design of plates and bowls | Wide Rim, Raised Rim, Coupe (Rimless), Narrow Rim, Slimline |
| Color | text | Primary visible color of the item | Bright White, Black, Graphite, Cream, Midnight Blue, Matte Slate |
| Finish | enum | Surface finish or texture of the glaze | Glossy, Matte, Reactive Glaze, Crackle Glaze, Unglazed |
| Diameter | number (inches) | Diameter of round items or longest dimension of non-round items | 10.5, 12, 7.125, 10.67 |
| Length | number (inches) | Overall length of the item, relevant for rectangular or oval pieces | 12, 13, 14.5 |
| Width | number (inches) | Overall width of the item | 12, 7.25, 8.25 |
| Height | number (inches) | Overall height or depth of the item | 1.125, 0.83, 4, 2.75 |
| Capacity | number (oz) | Volume capacity for bowls and deep plates | 16, 27, 32, 40, 23.7 |
| Weight | number (oz) | Weight of a single piece | 19.93, 32.28 |
| Dishwasher Safe | boolean | Whether the item is safe for dishwasher cleaning | Yes, No |
| Microwave Safe | boolean | Whether the item is safe for microwave use | Yes, No |
| Oven Safe | boolean | Whether the item is safe for conventional oven use | Yes, No |
| Oven Safe Temperature | number (F) | Maximum oven-safe temperature in degrees Fahrenheit | 450, 572 |
| Freezer Safe | boolean | Whether the item is safe for freezer storage | Yes, No |
| Lead Free | boolean | Whether the item is manufactured without lead additives | Yes, No |
| BPA Free | boolean | Whether the item is free of bisphenol A, applicable to melamine and plastic items | Yes, No |
| Chip Resistant | boolean | Whether the item is designed to resist chipping under normal use | Yes, No |
| Country of Origin | text | Country where the item was manufactured | USA, Germany, United Arab Emirates, Japan, China |
| Case Quantity | number | Number of individual pieces per case or carton for commercial purchasing | 6, 12, 24, 48 |
| Pieces Per Set | number | Number of pieces included when sold as a set | 1, 4, 6, 12, 16 |
| Service For | number | Number of place settings covered by a set | 4, 6, 8, 12 |
| Edge Chip Warranty | text | Manufacturer warranty against edge chipping | 1-year, Lifetime, None |
| Certifications | text (list) | Food safety and quality certifications the item holds | NSF, SGS, ISO 9001, CE, LFGB |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 33 attributes from 4 companies covering B2B distributor, premium manufacturers, and commercial hospitality suppliers | [WebstaurantStore](https://www.webstaurantstore.com/restaurant-dinnerware.html), [Villeroy & Boch](https://www.villeroy-boch.com/c/dinnerware/plates/), [RAK Porcelain](https://www.rakporcelain.com/wr-en), [Noritake](https://noritakechina.com/) |
