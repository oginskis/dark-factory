# SKU Schema: Grain, Oilseeds & Raw Crop Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Seller or trading platform lot identifier | LOT-2026-03-0451, GRN-W-HRW-001, SOY-BR-2025 |
| Product Name | text | Full commodity description including grain type, class, grade, and origin | US No. 2 Hard Red Winter Wheat, Brazilian Soybean Non-GMO, US No. 1 Yellow Corn |
| URL | text | Direct link to the product listing or specification sheet | https://example.com/commodity/hrw-wheat-lot-451 |
| Price | number | Numeric price per unit (bushel, metric ton, or hundredweight), excluding currency symbol | 5.85, 245.00, 14.50, 380.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, BRL, CAD, AUD, ARS |
| Commodity Type | enum | Primary grain or oilseed classification | Corn, Wheat, Soybeans, Sorghum, Oats, Barley, Rice, Canola, Sunflower Seed, Flaxseed, Rye |
| Commodity Class | text | Sub-classification within the commodity type, particularly for wheat | Hard Red Winter, Hard Red Spring, Soft Red Winter, Hard White, Soft White, Durum, Yellow, White |
| USDA Grade | enum | Official numerical grade per USDA Grain Standards Act or equivalent national standard | US No. 1, US No. 2, US No. 3, US No. 4, US No. 5, Sample Grade |
| Test Weight | number (kg/hL) | Bulk density measured as weight per volume, an indicator of grain soundness and milling yield | 76.0, 78.5, 72.0, 56.0 |
| Moisture Content | number (%) | Water content of the grain at time of analysis | 12.5, 13.5, 14.0, 15.5 |
| Protein Content | number (%) | Total protein percentage on a dry-weight or as-is basis | 10.5, 12.0, 13.5, 14.5 |
| Oil Content | number (%) | Total oil or fat percentage, primarily relevant for oilseeds | 18.5, 20.0, 34.0, 44.0 |
| Damaged Kernels | number (%) | Percentage of kernels showing material damage from heat, insects, disease, frost, or mold | 0.5, 1.0, 2.0, 4.0 |
| Heat-Damaged Kernels | number (%) | Percentage of kernels materially discolored by heat | 0.1, 0.2, 0.5, 3.0 |
| Foreign Material | number (%) | Percentage of non-grain matter remaining after dockage removal | 0.5, 1.0, 2.0, 3.0 |
| Dockage | number (%) | Percentage of all non-grain material mixed with the commodity before cleaning | 0.3, 0.6, 1.0, 2.0 |
| Broken Kernels or Splits | number (%) | Percentage of broken corn or split soybeans in the sample | 2.0, 3.0, 5.0, 7.0 |
| Total Defects | number (%) | Aggregate percentage of all grading defect factors combined | 2.0, 4.0, 6.0, 8.0 |
| Falling Number | number (s) | Indicator of alpha-amylase enzyme activity in wheat; higher values indicate less sprout damage | 250, 300, 350, 400 |
| Aflatoxin Level | number (ppb) | Concentration of aflatoxin mycotoxin contamination | 0, 5, 15, 20 |
| Vomitoxin Level | number (ppm) | Concentration of deoxynivalenol (DON) mycotoxin | 0.5, 1.0, 2.0, 5.0 |
| Country of Origin | text | Country where the crop was harvested | USA, Brazil, Argentina, Canada, Ukraine, Australia, France |
| Crop Year | text | Harvest year or marketing year for the commodity | 2025, 2025/26, 2026 |
| Variety | text | Specific cultivar or variety name when known | Pioneer P1197AM, Dekalb DKC67-44, WestBred WB4303 |
| GMO Status | enum | Genetic modification status of the commodity | Conventional, GMO, Non-GMO, Identity Preserved Non-GMO |
| Organic Certified | boolean | Whether the crop is certified organic under USDA NOP, EU organic, or equivalent standard | true, false |
| Lot Size | number (metric tons) | Quantity available in the trading lot | 25, 100, 500, 5000, 50000 |
| Pricing Unit | enum | Unit of measure for the quoted price | Per Bushel, Per Metric Ton, Per Short Ton, Per CWT |
| Delivery Terms | text | Trade delivery terms or Incoterm | FOB, CIF, FAS, Ex-Warehouse, Delivered |
| Delivery Location | text | Named port, elevator, or warehouse for delivery | Gulf Coast, Pacific Northwest, Santos, Rotterdam, Vancouver |
| Shipment Period | text | Expected loading or delivery window | March 2026, Apr-May 2026, Prompt, Spot |
| Packaging | enum | How the commodity is packaged for transport | Bulk, Bagged 25 kg, Bagged 50 kg, Container, Big Bag 1 MT |
| Certification | text (list) | Quality, sustainability, or supply chain certifications | USDA Organic, ProTerra, RTRS, ISCC, IP Non-GMO, Kosher |
| HTS Code | text | Harmonized Tariff Schedule code for international trade classification | 1001.99, 1005.90, 1201.90, 1005.10 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus USDA Grain Standards Act grading factors (7 CFR 810), S&P Global Platts grain specifications, and CME Group contract standards | [The Andersons](https://www.andersonsgrain.com/products-and-services/products/grains-oilseeds/), [COFCO International](https://www.cofcointernational.com/products-services/grains-oilseeds/), [Interra International](https://interrainternational.com/products/grain/), [Cargill](https://www.cargill.com.cn/en/grain-and-oilseeds) |
