# SKU Schema: Tobacco Products (Cigarettes, Cigars, Smokeless, Vaping Devices)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | PM-MARLBORO-KS-20, ACID-BLONDIE, JUUL-VIR-5PCT |
| Product Name | text | Full product name including brand, variant, and size | Marlboro Red King Size Box 20ct, Acid Blondie Cigar, JUUL Virginia Tobacco Pods 4-Pack |
| URL | text | Direct link to the product page | https://example.com/products/marlboro-red-ks |
| Price | number | Numeric price per unit excluding currency symbol | 8.99, 6.50, 21.99, 34.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Marlboro, Camel, Arturo Fuente, Padron, JUUL, Vuse, Copenhagen, Zyn |
| Product Category | enum | High-level tobacco product type | Cigarette, Cigar, Cigarillo, Pipe Tobacco, Smokeless Tobacco, Vaping Device, E-Liquid, Nicotine Pouch |
| Subcategory | text | More specific product classification within the category | Filtered Cigarette, Premium Cigar, Machine-Made Cigar, Moist Snuff, Long Cut, Disposable Vape, Pod System |
| Flavor | text | Primary flavor or blend description | Original, Menthol, Virginia Tobacco, Maduro, Wintergreen, Mint, Mango, Natural |
| Nicotine Content | number (mg) | Nicotine content per unit as stated on labelling | 0.8, 1.2, 3, 5, 6, 50 |
| Nicotine Strength | text | Descriptive nicotine strength tier for pouches and e-liquids | 0 mg, 3 mg, 5%, 6 mg/mL, Strong, Extra Strong |
| Cigarette Length | number (mm) | Overall length of the cigarette stick including filter | 70, 84, 100, 120 |
| Cigarette Diameter | number (mm) | Diameter of the cigarette stick | 5.0, 5.4, 7.8, 8.0 |
| Cigarette Size Class | enum | Standard size classification for cigarettes | Regular, King Size, 100s, 120s, Slim, Super Slim |
| Filter Type | text | Type of filter on the cigarette or cigarillo | Cellulose Acetate, Charcoal, Recessed, None |
| Cigar Length | number (inches) | Length of the cigar in inches | 4.0, 5.0, 5.5, 6.0, 7.0, 9.0 |
| Ring Gauge | number | Cigar diameter measured in sixty-fourths of an inch | 32, 42, 50, 52, 54, 60 |
| Cigar Shape | enum | Shape classification of the cigar | Parejo, Torpedo, Figurado, Perfecto, Churchill, Robusto, Corona, Toro, Panatela |
| Wrapper Origin | text | Country or region of the cigar wrapper leaf | Connecticut, Habano, Cameroon, Sumatra, Maduro, Corojo, Ecuadorian |
| Body Strength | enum | Perceived strength or intensity of the tobacco product | Mild, Mild-Medium, Medium, Medium-Full, Full |
| Tobacco Weight | number (g) | Weight of tobacco in the product per unit | 0.4, 0.7, 0.9, 30, 340 |
| Pack Size | number | Number of individual units per pack | 1, 5, 10, 20, 25 |
| Carton Size | number | Number of packs per carton or box | 5, 10, 20, 25, 50 |
| Battery Capacity | number (mAh) | Battery capacity for rechargeable vaping devices | 350, 500, 850, 1500, 3000 |
| Tank Capacity | number (mL) | E-liquid reservoir capacity for vaping devices | 1.0, 2.0, 4.0, 5.0, 20.0 |
| Puff Count | number | Estimated number of puffs for disposable vaping devices | 200, 600, 1500, 5000, 20000 |
| Coil Resistance | number (ohm) | Heating element resistance for vaping devices | 0.4, 0.6, 1.0, 1.2, 1.8 |
| Pouch Weight | number (g) | Weight per individual pouch for smokeless or nicotine pouch products | 0.3, 0.5, 0.8, 1.0, 1.5 |
| Country of Origin | text | Country where the product is manufactured | USA, Dominican Republic, Nicaragua, Honduras, Cuba, Sweden, China |
| Age Restriction | number (years) | Minimum legal purchase age in the selling jurisdiction | 18, 21 |
| Health Warning Label | boolean | Whether the product carries a mandatory health warning | true, false |
| Manufacturer | text | Parent company or manufacturer name | Philip Morris International, British American Tobacco, Altria, Swedish Match, JUUL Labs, General Cigar |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus WHO FCTC labelling standards and cigarette dimension standards | [Phillips and King](https://www.phillipsandking.com/), [Cigars International](https://www.cigarsinternational.com/cigar-101/cigar-ring-gauges/1818022/), [CDC Vaping Products](https://www.cdc.gov/tobacco/e-cigarettes/about.html), [Citi Packaging Cigarette Sizes](https://citipackaging.com/blog/cigarette-size-chart-global-standards-exact-measurements/) |
