# SKU Schema: Yarn, Thread & Cordage

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | ST-T60-BLK, YRN-WS-100, RC-NY-3/8 |
| Product Name | text | Full product name including key specs such as material, size, and construction | Bonded Nylon Thread Tex 70 Black, 3-Strand Polypropylene Rope 3/8in |
| URL | text | Direct link to the product page | https://example.com/product/bonded-nylon-tex70 |
| Price | number | Numeric price per unit (per spool, skein, cone, or foot), excluding currency symbol | 4.99, 12.50, 85.00, 249.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Brand, mill, or supplier name | Service Thread, Coats, Guetermann, Samtex, Samson Rope |
| Product Category | enum | Primary product classification within the subcategory | Sewing Thread, Industrial Yarn, Knitting/Craft Yarn, Rope, Cordage, Twine, Webbing |
| Material | text | Primary fiber or material composition | Polyester, Nylon, Polypropylene, Cotton, Aramid, HMPE, Manila, Wool, Acrylic |
| Fiber Blend | text | Full composition with percentages for blended products | 100% Polyester, 80% Wool 20% Nylon, 65% Cotton 35% Polyester |
| Denier | number | Linear density in grams per 9000 metres of filament | 210, 420, 630, 840, 1300, 55000 |
| Tex | number | Linear density in grams per 1000 metres | 27, 45, 60, 70, 135, 400 |
| Yarn Weight Category | enum | Standard weight classification for craft and knitting yarns (CYC system) | 0 - Lace, 1 - Superfine, 2 - Fine, 3 - Light, 4 - Medium, 5 - Bulky, 6 - Super Bulky, 7 - Jumbo |
| Ply Count | number | Number of individual strands twisted together | 2, 3, 4, 6, 8, 12 |
| Construction | enum | Method of strand assembly | Twisted, Braided, Cabled, Core Spun, Air Entangled, Monofilament, Plied |
| Twist Direction | enum | Direction of the final twist | S-Twist, Z-Twist |
| Diameter | number (mm) | Cross-section diameter for rope and cordage products | 1.0, 3.0, 6.0, 10.0, 25.0, 50.0 |
| Tensile Strength | number (lbs) | Breaking strength measured per ASTM D2256 (thread/yarn) or ASTM D4268 (rope) | 8, 25, 315, 1125, 46000 |
| Elongation at Break | number (%) | Maximum stretch at the point of failure | 2, 15, 20, 26, 31 |
| Working Load Limit | number (lbs) | Maximum recommended load for safe use, typically a fraction of breaking strength | 50, 150, 500, 2000 |
| Abrasion Resistance | enum | Qualitative rating of resistance to surface wear | Excellent, Good, Fair, Poor |
| UV Resistance | enum | Resistance to degradation from ultraviolet light exposure | Excellent, Good, Fair, Poor |
| Colorfastness to Light | text | Light fastness grade per ISO 105-B02 (1 = very poor, 8 = outstanding) | 3, 4, 5, 6, 7 |
| Color | text | Thread, yarn, or rope color | Black, White, Natural, Navy, Red, Olive Drab |
| Max Operating Temperature | number (F) | Maximum continuous-use temperature in degrees Fahrenheit | 275, 300, 400, 800 |
| Put-Up Length | number | Length of product per unit (yards, metres, or feet depending on product type) | 100, 246, 500, 3000, 6000 |
| Put-Up Weight | number (g) | Net weight per package unit | 50, 100, 200, 454, 2000 |
| Package Type | enum | How the product is wound or packaged | Spool, Cone, Skein, Hank, Coil, Reel, Bobbin |
| Recommended Needle Size | text | Suggested sewing machine needle or knitting needle size | 14, 16, 18, US 7, US 9, 4.5mm |
| Application | text (list) | Primary intended uses | Apparel Sewing, Upholstery, Sailmaking, Rigging, Mooring, Industrial Bag Closing, Geotextile Seaming |
| Certification | text (list) | Product and process certifications | ISO 9001, Mil-Spec, OEKO-TEX, Cordage Institute CI, UL |
| Country of Origin | text | Country where the product was manufactured | USA, Germany, China, India, Turkey |
| Linear Density per Foot | number (lbs/100ft) | Weight per 100 feet of rope or cordage | 1.50, 5.25, 16.70, 108.00 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ASTM D2256, ASTM D4268, Cordage Institute, CYC yarn weight system) | [Service Thread](https://www.servicethread.com), [CutSew Industrial Thread Guide](https://www.cutsew.com/Basics-of-Industrial-Sewing-Thread), [Industrial Rope Cordage Charts](https://industrialrope.com/catalog-fiber-rope/cordage-comparative-weight-strength-and-working-load-chart/), [Yarn Weight Standards](https://ariyarn.com/blog/the-ultimate-guide-to-yarn-weights-how-to-choose-the-right-yarn-for-your-project) |
