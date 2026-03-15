# SKU Schema: Air Fresheners & Candles

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.air_fresheners_candles`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | B00W8NNH34, 1625853, SC-WB3-LV |
| Product Name | product_name | text | Full product name including brand, scent, product type, and size | Yankee Candle Large Jar Clean Cotton 22 oz, Febreze PLUG Odor-Fighting Oil Warmer Gain Original |
| URL | url | text | Direct link to the product page | https://www.yankeecandle.com/product/clean-cotton/_/R-1010728 |
| Price | price | number | Numeric unit price excluding currency symbol | 29.50, 8.99, 4.97 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary product classification | Jar Candle, Pillar Candle, Votive Candle, Tealight, Taper Candle, Wax Melt, Plug-In Oil Diffuser, Aerosol Spray, Automatic Spray, Reed Diffuser, Incense, Room Spray, Car Air Freshener, Gel Air Freshener |
| Scent Category | scent_category | enum | Olfactory family or grouping of the scent | Floral, Fresh, Fruity, Woody, Spicy, Gourmand, Clean, Seasonal, Citrus |
| Wax Type | wax_type | text | Type of wax used in candles and melts | Paraffin, Soy, Soy Blend, Beeswax, Coconut, Coconut Blend, Palm |
| Wick Material | wick_material | text | Material used for candle wicks | Cotton, Wood, Cotton-Paper, Hemp |
| Country of Origin | country_of_origin | text | Country where the product is manufactured | USA, France, UK, China, India |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Scent Name | scent_name | text | Name of the fragrance | Clean Cotton, Lavender Vanilla, Balsam and Cedar, Gain Original, Linen and Sky |
| Top Notes | top_notes | text (list) | Initial scent notes for candles and diffusers with complex profiles | Bergamot, Green Apple, Lemon Zest, Pear |
| Middle Notes | middle_notes | text (list) | Heart scent notes | Jasmine, Rose, Cotton Blossom, Cinnamon Bark |
| Base Notes | base_notes | text (list) | Foundation scent notes | Musk, Vanilla, Sandalwood, Amber, Cedar |
| Number of Wicks | number_of_wicks | number | Count of wicks in the candle | 1, 2, 3 |
| Burn Time | burn_time | number (hours) | Expected burn time under normal conditions | 25, 45, 80, 110, 150 |
| Volume | volume | number (ml) | Volume for liquid air freshener refills and sprays | 19, 20, 25, 250, 473 |
| Container Dimensions | container_dimensions | text (mm) | Diameter x height of the candle or container | 97x168, 76x93, 102x127 |
| Refill Available | refill_available | enum | Whether refill cartridges or replacement units are sold separately | Yes, No |
| Refill Duration | refill_duration | number (days) | How long a plug-in or automatic refill lasts on lowest setting | 30, 45, 50, 60 |
| Intensity Adjustable | intensity_adjustable | enum | Whether the scent intensity can be user-adjusted | Yes, No |
| Coverage Area | coverage_area | text | Recommended room size or area the product can effectively scent | Small Room, Medium Room, Large Room, Up to 100 sq ft, Up to 300 sq ft |
| Power Source | power_source | enum | Power requirement for electric air fresheners | Plug-In (AC), Battery, None (passive) |
| Lid/Cover Included | lidcover_included | enum | Whether a lid or dust cover is included with the candle | Yes, No |
| Lead Free Wick | lead_free_wick | enum | Whether the wick is certified lead-free | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus ASTM candle safety standards and IFRA fragrance guidelines | [Yankee Candle Burn Times](https://www.yankeecandle.com/burn-times.html), [Bath and Body Works 3-Wick Candles](https://www.bathandbodyworks.com/g/all-candles), [Febreze PLUG Air Freshener](https://www.febreze.com/en-us/products/products-by-type/plug-air-freshener), [Glade PlugIns Scented Oil](https://glade.com/en-us/products/plugins/scented-oil) |
