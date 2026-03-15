# SKU Schema: Yarn, Thread & Cordage

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.yarn_thread_cordage`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | ST-T60-BLK, YRN-WS-100, RC-NY-3/8 |
| Product Name | product_name | text | Full product name including key specs such as material, size, and construction | Bonded Nylon Thread Tex 70 Black, 3-Strand Polypropylene Rope 3/8in |
| URL | url | text | Direct link to the product page | https://example.com/product/bonded-nylon-tex70 |
| Price | price | number | Numeric price per unit (per spool, skein, cone, or foot), excluding currency symbol | 4.99, 12.50, 85.00, 249.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | product_category | enum | Primary product classification within the subcategory | Sewing Thread, Industrial Yarn, Knitting/Craft Yarn, Rope, Cordage, Twine, Webbing |
| Material | material | text | Primary fiber or material composition | Polyester, Nylon, Polypropylene, Cotton, Aramid, HMPE, Manila, Wool, Acrylic |
| Yarn Weight Category | yarn_weight_category | enum | Standard weight classification for craft and knitting yarns (CYC system) | 0 - Lace, 1 - Superfine, 2 - Fine, 3 - Light, 4 - Medium, 5 - Bulky, 6 - Super Bulky, 7 - Jumbo |
| Package Type | package_type | enum | How the product is wound or packaged | Spool, Cone, Skein, Hank, Coil, Reel, Bobbin |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | USA, Germany, China, India, Turkey |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Fiber Blend | fiber_blend | text | Full composition with percentages for blended products | 100% Polyester, 80% Wool 20% Nylon, 65% Cotton 35% Polyester |
| Denier | denier | number | Linear density in grams per 9000 metres of filament | 210, 420, 630, 840, 1300, 55000 |
| Tex | tex | number | Linear density in grams per 1000 metres | 27, 45, 60, 70, 135, 400 |
| Construction | construction | enum | Method of strand assembly | Twisted, Braided, Cabled, Core Spun, Air Entangled, Monofilament, Plied |
| Twist Direction | twist_direction | enum | Direction of the final twist | S-Twist, Z-Twist |
| Tensile Strength | tensile_strength | number (lbs) | Breaking strength measured per ASTM D2256 (thread/yarn) or ASTM D4268 (rope) | 8, 25, 315, 1125, 46000 |
| Elongation at Break | elongation_at_break | number (%) | Maximum stretch at the point of failure | 2, 15, 20, 26, 31 |
| Working Load Limit | working_load_limit | number (lbs) | Maximum recommended load for safe use, typically a fraction of breaking strength | 50, 150, 500, 2000 |
| Abrasion Resistance | abrasion_resistance | enum | Qualitative rating of resistance to surface wear | Excellent, Good, Fair, Poor |
| UV Resistance | uv_resistance | enum | Resistance to degradation from ultraviolet light exposure | Excellent, Good, Fair, Poor |
| Colorfastness to Light | colorfastness_to_light | text | Light fastness grade per ISO 105-B02 (1 = very poor, 8 = outstanding) | 3, 4, 5, 6, 7 |
| Color | color | text | Thread, yarn, or rope color | Black, White, Natural, Navy, Red, Olive Drab |
| Max Operating Temperature | max_operating_temperature | number (F) | Maximum continuous-use temperature in degrees Fahrenheit | 275, 300, 400, 800 |
| Application | application | text (list) | Primary intended uses | Apparel Sewing, Upholstery, Sailmaking, Rigging, Mooring, Industrial Bag Closing, Geotextile Seaming |
| Certification | certification | text (list) | Product and process certifications | ISO 9001, Mil-Spec, OEKO-TEX, Cordage Institute CI, UL |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ASTM D2256, ASTM D4268, Cordage Institute, CYC yarn weight system) | [Service Thread](https://www.servicethread.com), [CutSew Industrial Thread Guide](https://www.cutsew.com/Basics-of-Industrial-Sewing-Thread), [Industrial Rope Cordage Charts](https://industrialrope.com/catalog-fiber-rope/cordage-comparative-weight-strength-and-working-load-chart/), [Yarn Weight Standards](https://ariyarn.com/blog/the-ultimate-guide-to-yarn-weights-how-to-choose-the-right-yarn-for-your-project) |
