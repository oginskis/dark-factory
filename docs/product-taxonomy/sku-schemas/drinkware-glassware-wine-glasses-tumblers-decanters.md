# SKU Schema: Drinkware & Glassware (Wine Glasses, Tumblers, Decanters)

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer product identifier, article number, or item number | 6409/07, 9104RL, G1747-09-301 |
| Product Name | text | Full product name including collection and glass type | Heart to Heart Pinot Noir, Vervino All-Purpose Wine Glass, Arc Tumbler 260ml |
| URL | text | Direct link to the product page | https://www.example.com/shop/product-name |
| Price | number | Numeric price per selling unit, excluding tax and shipping | 59.00, 102.00, 30.00 |
| Currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, AUD |
| Brand | text | Manufacturer or brand name | Schott Zwiesel, Waterford, Libbey, LSA International |
| Collection | text | Product line, series, or collection name | Sommeliers, Veritas, Allure, Forte, Arc |
| Glass Type | text | Functional type of drinkware | Red Wine Glass, White Wine Glass, Champagne Flute, Tumbler, Decanter, Highball, Rocks Glass, Martini Glass |
| Intended Beverage | text (list) | Wine varietal, spirit, or drink type the glass is designed for | Pinot Noir, Cabernet Sauvignon, Champagne, Whisky, Gin, Water |
| Capacity | number (oz) | Volume capacity of the glass in fluid ounces | 9.4, 15.0, 23.2, 27.0, 30.0 |
| Capacity Metric | number (ml) | Volume capacity of the glass in millilitres | 260, 459, 770, 860 |
| Height | number (inches) | Overall height of the glass in inches | 8.125, 9.1, 9.567, 10.63, 13.78 |
| Height Metric | number (mm) | Overall height of the glass in millimetres | 206, 235, 243, 270, 350 |
| Diameter | number (inches) | Maximum diameter or width of the bowl in inches | 2.9, 3.2, 3.5, 4.1 |
| Material | text | Primary material composition | Crystal Glass, Tritan Crystal, Lead-Free Crystal, Soda-Lime Glass, Borosilicate Glass |
| Lead Free | boolean | Whether the glass is certified lead-free | true, false |
| Manufacturing Method | enum | How the glass is produced | handmade, machine-made, hand-finished, mouth-blown |
| Set Size | number | Number of pieces included in the selling unit | 1, 2, 4, 6, 8, 12 |
| Style | enum | Whether the glass has a stem or is stemless | stemmed, stemless |
| Dishwasher Safe | boolean | Whether the glass is safe for dishwasher cleaning | true, false |
| Year of Design | number | Year the glass design was originally introduced | 1973, 2011, 2018, 2025 |
| Country of Origin | text | Country where the glass is manufactured | Germany, Austria, USA, Poland, Czech Republic |
| Color | text | Color of the glass body or stem | Clear, Black, Red, Blue, Green, Turquoise |
| Weight | number (g) | Weight of a single glass in grams | 150, 181, 230, 2330 |
| Case Pack Size | number | Number of selling units per shipping case, relevant for B2B/foodservice | 12, 24, 36 |
| UPC | text | Universal Product Code barcode identifier | 10031009326935 |
| Rim Type | enum | Treatment or type of rim finish | cut, fire-polished, rolled, tempered |
| Decanter Size | enum | For decanters, the bottle capacity it is designed for | Half Bottle, Standard Bottle, Magnum, Double Magnum |
| Pattern | text | Decorative cut pattern or design motif name | Lismore, Diamond, Fluted |
| Suitable Grapes | text (list) | Specific grape varietals the glass is optimized for, used by varietal-specific glassware | Pinot Noir, Cabernet Sauvignon, Riesling, Chardonnay, Sauvignon Blanc, Shiraz |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 30 attributes from 5 companies covering wine glasses, tumblers, and decanters across manufacturer, B2B distributor, and specialty retail channels | [Riedel](https://www.riedel.com), [Schott Zwiesel / Sur La Table](https://www.surlatable.com/product/schott-zwiesel-vervino-all-purpose-wine-glasses/6497978), [Libbey / WebstaurantStore](https://www.webstaurantstore.com/libbey-9104rl-allure-6-5-oz-wine-glass-12-case/5519104RL.html), [Waterford](https://www.waterford.com/en-us/glassware-and-bar), [LSA International](https://www.lsa-international.com/en-us/products/arc-tumbler-260ml) |
