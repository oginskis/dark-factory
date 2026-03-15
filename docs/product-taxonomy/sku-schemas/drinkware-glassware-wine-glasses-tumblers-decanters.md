# SKU Schema: Drinkware & Glassware (Wine Glasses, Tumblers, Decanters)

**Last updated:** 2026-03-15
**Parent category:** Kitchenware, Tableware & Housewares
**Taxonomy ID:** `kitchen.drinkware_glassware`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or retailer product identifier, article number, or item number | 6409/07, 9104RL, G1747-09-301 |
| Product Name | product_name | text | Full product name including collection and glass type | Heart to Heart Pinot Noir, Vervino All-Purpose Wine Glass, Arc Tumbler 260ml |
| URL | url | text | Direct link to the product page | https://www.example.com/shop/product-name |
| Price | price | number | Numeric price per selling unit, excluding tax and shipping | 59.00, 102.00, 30.00 |
| Currency | currency | text | ISO 4217 currency code for the listed price | USD, EUR, GBP, AUD |
| Glass Type | glass_type | text | Functional type of drinkware | Red Wine Glass, White Wine Glass, Champagne Flute, Tumbler, Decanter, Highball, Rocks Glass, Martini Glass |
| Material | material | text | Primary material composition | Crystal Glass, Tritan Crystal, Lead-Free Crystal, Soda-Lime Glass, Borosilicate Glass |
| Country of Origin | country_of_origin | text | Country where the glass is manufactured | Germany, Austria, USA, Poland, Czech Republic |
| Rim Type | rim_type | enum | Treatment or type of rim finish | cut, fire-polished, rolled, tempered |
| Capacity | capacity | number (oz) | Volume capacity of the glass in fluid ounces | 9.4, 15.0, 23.2, 27.0, 30.0 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Collection | collection | text | Product line, series, or collection name | Sommeliers, Veritas, Allure, Forte, Arc |
| Intended Beverage | intended_beverage | text (list) | Wine varietal, spirit, or drink type the glass is designed for | Pinot Noir, Cabernet Sauvignon, Champagne, Whisky, Gin, Water |
| Height | height | number (inches) | Overall height of the glass in inches | 8.125, 9.1, 9.567, 10.63, 13.78 |
| Height Metric | height_metric | number (mm) | Overall height of the glass in millimetres | 206, 235, 243, 270, 350 |
| Lead Free | lead_free | boolean | Whether the glass is certified lead-free | true, false |
| Manufacturing Method | manufacturing_method | enum | How the glass is produced | handmade, machine-made, hand-finished, mouth-blown |
| Style | style | enum | Whether the glass has a stem or is stemless | stemmed, stemless |
| Dishwasher Safe | dishwasher_safe | boolean | Whether the glass is safe for dishwasher cleaning | true, false |
| Year of Design | year_of_design | number | Year the glass design was originally introduced | 1973, 2011, 2018, 2025 |
| Color | color | text | Color of the glass body or stem | Clear, Black, Red, Blue, Green, Turquoise |
| UPC | upc | text | Universal Product Code barcode identifier | 10031009326935 |
| Pattern | pattern | text | Decorative cut pattern or design motif name | Lismore, Diamond, Fluted |
| Suitable Grapes | suitable_grapes | text (list) | Specific grape varietals the glass is optimized for, used by varietal-specific glassware | Pinot Noir, Cabernet Sauvignon, Riesling, Chardonnay, Sauvignon Blanc, Shiraz |
| Capacity Metric | capacity_metric | number (ml) | Volume capacity of the glass in millilitres | 260, 459, 770, 860 |
| Diameter | diameter | number (inches) | Maximum diameter or width of the bowl in inches | 2.9, 3.2, 3.5, 4.1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 5 companies covering wine glasses, tumblers, and decanters across manufacturer, B2B distributor, and specialty retail channels | [Riedel](https://www.riedel.com), [Schott Zwiesel / Sur La Table](https://www.surlatable.com/product/schott-zwiesel-vervino-all-purpose-wine-glasses/6497978), [Libbey / WebstaurantStore](https://www.webstaurantstore.com/libbey-9104rl-allure-6-5-oz-wine-glass-12-case/5519104RL.html), [Waterford](https://www.waterford.com/en-us/glassware-and-bar), [LSA International](https://www.lsa-international.com/en-us/products/arc-tumbler-260ml) |
