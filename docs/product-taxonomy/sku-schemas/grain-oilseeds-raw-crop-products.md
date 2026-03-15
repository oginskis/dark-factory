# SKU Schema: Grain, Oilseeds & Raw Crop Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.grain_oilseeds_raw_crops`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Seller or trading platform lot identifier | LOT-2026-03-0451, GRN-W-HRW-001, SOY-BR-2025 |
| Product Name | product_name | text | Full commodity description including grain type, class, grade, and origin | US No. 2 Hard Red Winter Wheat, Brazilian Soybean Non-GMO, US No. 1 Yellow Corn |
| URL | url | text | Direct link to the product listing or specification sheet | https://example.com/commodity/hrw-wheat-lot-451 |
| Price | price | number | Numeric price per unit (bushel, metric ton, or hundredweight), excluding currency symbol | 5.85, 245.00, 14.50, 380.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, BRL, CAD, AUD, ARS |
| Commodity Type | commodity_type | enum | Primary grain or oilseed classification | Corn, Wheat, Soybeans, Sorghum, Oats, Barley, Rice, Canola, Sunflower Seed, Flaxseed, Rye |
| Commodity Class | commodity_class | text | Sub-classification within the commodity type, particularly for wheat | Hard Red Winter, Hard Red Spring, Soft Red Winter, Hard White, Soft White, Durum, Yellow, White |
| USDA Grade | usda_grade | enum | Official numerical grade per USDA Grain Standards Act or equivalent national standard | US No. 1, US No. 2, US No. 3, US No. 4, US No. 5, Sample Grade |
| Foreign Material | foreign_material | number (%) | Percentage of non-grain matter remaining after dockage removal | 0.5, 1.0, 2.0, 3.0 |
| Country of Origin | country_of_origin | text | Country where the crop was harvested | USA, Brazil, Argentina, Canada, Ukraine, Australia, France |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Moisture Content | moisture_content | number (%) | Water content of the grain at time of analysis | 12.5, 13.5, 14.0, 15.5 |
| Protein Content | protein_content | number (%) | Total protein percentage on a dry-weight or as-is basis | 10.5, 12.0, 13.5, 14.5 |
| Oil Content | oil_content | number (%) | Total oil or fat percentage, primarily relevant for oilseeds | 18.5, 20.0, 34.0, 44.0 |
| Damaged Kernels | damaged_kernels | number (%) | Percentage of kernels showing material damage from heat, insects, disease, frost, or mold | 0.5, 1.0, 2.0, 4.0 |
| Heat-Damaged Kernels | heat-damaged_kernels | number (%) | Percentage of kernels materially discolored by heat | 0.1, 0.2, 0.5, 3.0 |
| Dockage | dockage | number (%) | Percentage of all non-grain material mixed with the commodity before cleaning | 0.3, 0.6, 1.0, 2.0 |
| Broken Kernels or Splits | broken_kernels_or_splits | number (%) | Percentage of broken corn or split soybeans in the sample | 2.0, 3.0, 5.0, 7.0 |
| Total Defects | total_defects | number (%) | Aggregate percentage of all grading defect factors combined | 2.0, 4.0, 6.0, 8.0 |
| Falling Number | falling_number | number (s) | Indicator of alpha-amylase enzyme activity in wheat; higher values indicate less sprout damage | 250, 300, 350, 400 |
| Aflatoxin Level | aflatoxin_level | number (ppb) | Concentration of aflatoxin mycotoxin contamination | 0, 5, 15, 20 |
| Vomitoxin Level | vomitoxin_level | number (ppm) | Concentration of deoxynivalenol (DON) mycotoxin | 0.5, 1.0, 2.0, 5.0 |
| Crop Year | crop_year | text | Harvest year or marketing year for the commodity | 2025, 2025/26, 2026 |
| Variety | variety | text | Specific cultivar or variety name when known | Pioneer P1197AM, Dekalb DKC67-44, WestBred WB4303 |
| GMO Status | gmo_status | enum | Genetic modification status of the commodity | Conventional, GMO, Non-GMO, Identity Preserved Non-GMO |
| Organic Certified | organic_certified | boolean | Whether the crop is certified organic under USDA NOP, EU organic, or equivalent standard | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus USDA Grain Standards Act grading factors (7 CFR 810), S&P Global Platts grain specifications, and CME Group contract standards | [The Andersons](https://www.andersonsgrain.com/products-and-services/products/grains-oilseeds/), [COFCO International](https://www.cofcointernational.com/products-services/grains-oilseeds/), [Interra International](https://interrainternational.com/products/grain/), [Cargill](https://www.cargill.com.cn/en/grain-and-oilseeds) |
