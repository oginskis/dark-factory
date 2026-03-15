# SKU Schema: Air Fresheners & Candles

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | B00W8NNH34, 1625853, SC-WB3-LV |
| Product Name | text | Full product name including brand, scent, product type, and size | Yankee Candle Large Jar Clean Cotton 22 oz, Febreze PLUG Odor-Fighting Oil Warmer Gain Original |
| URL | text | Direct link to the product page | https://www.yankeecandle.com/product/clean-cotton/_/R-1010728 |
| Price | number | Numeric unit price excluding currency symbol | 29.50, 8.99, 4.97 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Yankee Candle, Bath and Body Works, Febreze, Glade, Air Wick, Diptyque, P.F. Candle Co., WoodWick |
| Product Type | enum | Primary product classification | Jar Candle, Pillar Candle, Votive Candle, Tealight, Taper Candle, Wax Melt, Plug-In Oil Diffuser, Aerosol Spray, Automatic Spray, Reed Diffuser, Incense, Room Spray, Car Air Freshener, Gel Air Freshener |
| Scent Name | text | Name of the fragrance | Clean Cotton, Lavender Vanilla, Balsam and Cedar, Gain Original, Linen and Sky |
| Scent Category | enum | Olfactory family or grouping of the scent | Floral, Fresh, Fruity, Woody, Spicy, Gourmand, Clean, Seasonal, Citrus |
| Top Notes | text (list) | Initial scent notes for candles and diffusers with complex profiles | Bergamot, Green Apple, Lemon Zest, Pear |
| Middle Notes | text (list) | Heart scent notes | Jasmine, Rose, Cotton Blossom, Cinnamon Bark |
| Base Notes | text (list) | Foundation scent notes | Musk, Vanilla, Sandalwood, Amber, Cedar |
| Wax Type | text | Type of wax used in candles and melts | Paraffin, Soy, Soy Blend, Beeswax, Coconut, Coconut Blend, Palm |
| Wick Material | text | Material used for candle wicks | Cotton, Wood, Cotton-Paper, Hemp |
| Number of Wicks | number | Count of wicks in the candle | 1, 2, 3 |
| Burn Time | number (hours) | Expected burn time under normal conditions | 25, 45, 80, 110, 150 |
| Net Weight | number (g) | Net weight of the wax or product fill | 104, 198, 411, 623 |
| Volume | number (ml) | Volume for liquid air freshener refills and sprays | 19, 20, 25, 250, 473 |
| Container Material | text | Material of the candle vessel or air freshener housing | Glass Jar, Tin, Ceramic, Plastic, Metal, Concrete |
| Container Dimensions | text (mm) | Diameter x height of the candle or container | 97x168, 76x93, 102x127 |
| Refill Available | enum | Whether refill cartridges or replacement units are sold separately | Yes, No |
| Refill Duration | number (days) | How long a plug-in or automatic refill lasts on lowest setting | 30, 45, 50, 60 |
| Intensity Adjustable | enum | Whether the scent intensity can be user-adjusted | Yes, No |
| Coverage Area | text | Recommended room size or area the product can effectively scent | Small Room, Medium Room, Large Room, Up to 100 sq ft, Up to 300 sq ft |
| Power Source | enum | Power requirement for electric air fresheners | Plug-In (AC), Battery, None (passive) |
| Lid/Cover Included | enum | Whether a lid or dust cover is included with the candle | Yes, No |
| Lead Free Wick | enum | Whether the wick is certified lead-free | Yes, No |
| Phthalate Free | enum | Whether the product is phthalate-free | Yes, No |
| Soot Level | enum | Expected soot production during candle burn | Low, Medium, High |
| Pack Quantity | number | Number of units per pack | 1, 2, 3, 4, 6, 12 |
| Certifications | text (list) | Product safety and quality certifications | ASTM F2417, EU CLP Regulation, IFRA Compliant, Clean Air Safe, ISO 22716 |
| Country of Origin | text | Country where the product is manufactured | USA, France, UK, China, India |
| Shelf Life | number (months) | Expected shelf life from date of manufacture | 12, 24, 36, 48 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus ASTM candle safety standards and IFRA fragrance guidelines | [Yankee Candle Burn Times](https://www.yankeecandle.com/burn-times.html), [Bath and Body Works 3-Wick Candles](https://www.bathandbodyworks.com/g/all-candles), [Febreze PLUG Air Freshener](https://www.febreze.com/en-us/products/products-by-type/plug-air-freshener), [Glade PlugIns Scented Oil](https://glade.com/en-us/products/plugins/scented-oil) |
