# SKU Schema: Tobacco Products (Cigarettes, Cigars, Smokeless, Vaping Devices)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.tobacco`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | PM-MARLBORO-KS-20, ACID-BLONDIE, JUUL-VIR-5PCT |
| Product Name | product_name | text | — | Full product name including brand, variant, and size | Marlboro Red King Size Box 20ct, Acid Blondie Cigar, JUUL Virginia Tobacco Pods 4-Pack |
| URL | url | text | — | Direct link to the product page | https://example.com/products/marlboro-red-ks |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 8.99, 6.50, 21.99, 34.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Category | product_category | enum | — | High-level tobacco product type | Cigarette, Cigar, Cigarillo, Pipe Tobacco, Smokeless Tobacco, Vaping Device, E-Liquid, Nicotine Pouch |
| Subcategory | subcategory | text | — | More specific product classification within the category | Filtered Cigarette, Premium Cigar, Machine-Made Cigar, Moist Snuff, Long Cut, Disposable Vape, Pod System |
| Cigarette Size Class | cigarette_size_class | enum | — | Standard size classification for cigarettes | Regular, King Size, 100s, 120s, Slim, Super Slim |
| Filter Type | filter_type | text | — | Type of filter on the cigarette or cigarillo | Cellulose Acetate, Charcoal, Recessed, None |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, Dominican Republic, Nicaragua, Honduras, Cuba, Sweden, China |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Flavor | flavor | text | — | Primary flavor or blend description | Original, Menthol, Virginia Tobacco, Maduro, Wintergreen, Mint, Mango, Natural |
| Nicotine Content | nicotine_content | number | mg | Nicotine content per unit as stated on labelling | 0.8, 1.2, 3, 5, 6, 50 |
| Nicotine Strength | nicotine_strength | text | — | Descriptive nicotine strength tier for pouches and e-liquids | 0 mg, 3 mg, 5%, 6 mg/mL, Strong, Extra Strong |
| Ring Gauge | ring_gauge | number | — | Cigar diameter measured in sixty-fourths of an inch | 32, 42, 50, 52, 54, 60 |
| Cigar Shape | cigar_shape | enum | — | Shape classification of the cigar | Parejo, Torpedo, Figurado, Perfecto, Churchill, Robusto, Corona, Toro, Panatela |
| Wrapper Origin | wrapper_origin | text | — | Country or region of the cigar wrapper leaf | Connecticut, Habano, Cameroon, Sumatra, Maduro, Corojo, Ecuadorian |
| Body Strength | body_strength | enum | — | Perceived strength or intensity of the tobacco product | Mild, Mild-Medium, Medium, Medium-Full, Full |
| Coil Resistance | coil_resistance | number | ohm | Heating element resistance for vaping devices | 0.4, 0.6, 1.0, 1.2, 1.8 |
| Age Restriction | age_restriction | number | years | Minimum legal purchase age in the selling jurisdiction | 18, 21 |
| Health Warning Label | health_warning_label | boolean | — | Whether the product carries a mandatory health warning | true, false |
| Manufacturer | manufacturer | text | — | Parent company or manufacturer name | Philip Morris International, British American Tobacco, Altria, Swedish Match, JUUL Labs, General Cigar |
| Cigarette Length | cigarette_length | number | mm | Overall length of the cigarette stick including filter | 70, 84, 100, 120 |
| Cigarette Diameter | cigarette_diameter | number | mm | Diameter of the cigarette stick | 5.0, 5.4, 7.8, 8.0 |
| Cigar Length | cigar_length | number | inches | Length of the cigar in inches | 4.0, 5.0, 5.5, 6.0, 7.0, 9.0 |
| Tobacco Weight | tobacco_weight | number | g | Weight of tobacco in the product per unit | 0.4, 0.7, 0.9, 30, 340 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus WHO FCTC labelling standards and cigarette dimension standards | [Phillips and King](https://www.phillipsandking.com/), [Cigars International](https://www.cigarsinternational.com/cigar-101/cigar-ring-gauges/1818022/), [CDC Vaping Products](https://www.cdc.gov/tobacco/e-cigarettes/about.html), [Citi Packaging Cigarette Sizes](https://citipackaging.com/blog/cigarette-size-chart-global-standards-exact-measurements/) |
