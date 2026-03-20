# SKU Schema: Packaging Machinery

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.packaging_machinery`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | VF-1200, SVE-2510, CCW-RV-214, MK-GS30 |
| Product Name | product_name | text | — | yes | Full product name including machine type, series, and key capability | Paxiom VF 1200 Continuous Motion VFFS Bagger, Syntegon SVE 2510 Vertical Form Fill Seal Machine, Ishida CCW-RV 14-Head Multihead Weigher |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/vf-1200 |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 15000, 65000, 250000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Machine Type | machine_type | enum | — | — | Primary classification of the packaging machine | VFFS (Vertical Form Fill Seal), HFFS (Horizontal Form Fill Seal), Flow Wrapper, Case Packer, Cartoner, Palletizer, Stretch Wrapper, Shrink Wrapper, Labeler, Multihead Weigher, Filling Machine, Sealing Machine, Strapping Machine |
| Film Types | film_types | text (list) | — | — | Compatible packaging film materials | Polyethylene (PE), Polypropylene (OPP/BOPP), Polyester (PET), Laminate, Paper, Aluminum Foil, Biodegradable |
| Filling System Type | filling_system_type | text | — | — | Method used to dose product into packages | Volumetric Cup, Auger, Multihead Weigher, Liquid Pump, Piston Filler, Net Weigher, Linear Weigher, Vibratory Feeder |
| Seal Type | seal_type | text (list) | — | — | Sealing methods available on the machine | Heat Seal, Ultrasonic Seal, Impulse Seal, Continuous Band Seal, Crimp Seal, Fin Seal, Lap Seal |
| Motion Type | motion_type | enum | — | — | Mechanism of operation for the forming and sealing cycle | Intermittent, Continuous, Servo-Driven |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Construction Material | construction_material | text | — | — | Primary material of the machine frame and contact surfaces | Stainless Steel 304, Stainless Steel 316L, Anodized Aluminum, Painted Carbon Steel |
| Product Type Compatibility | product_type_compatibility | text (list) | — | — | Types of products the machine can package | Powders, Granules, Liquids, Pastes, Solids, Frozen Foods, Snacks, Fresh Produce, Hardware, Pharmaceuticals |
| Country of Origin | country_of_origin | text | — | — | Country where the machine was manufactured | Germany, Italy, Japan, USA, China, Switzerland |
| Product Series | product_series | text | — | — | Manufacturer product series or model family | SVE Series, VF Series, CCW-RV, Mercury, X-Line, R 085 |
| Packaging Speed | packaging_speed | text | — | — | Maximum output rate in packages or cycles per unit time | 60 bags/min, 150 bags/min, 300 bags/min, 200 packs/min, 25 cases/min |
| Bag/Package Width Range | bagpackage_width_range | text | mm | — | Minimum and maximum width of the package the machine can produce | 60-250 mm, 80-400 mm, 50-330 mm, 100-600 mm |
| Film Width Range | film_width_range | text | mm | — | Minimum and maximum width of packaging film the machine accepts | 100-520 mm, 150-700 mm, 200-1000 mm |
| Seal Bar Width | seal_bar_width | number | mm | — | Width of the sealing jaw or bar | 5, 10, 15, 20, 25 |
| Machine Dimensions L x W x H | machine_dimensions_l_x_w_x_h | text | mm | — | Overall physical dimensions of the machine | 1200 x 900 x 2100, 2500 x 1500 x 3500, 4000 x 2000 x 3800 |
| Power Supply | power_supply | text | — | — | Required electrical supply specification | 220V/1PH/60Hz, 380V/3PH/50Hz, 208-480V/3PH/50-60Hz |
| Power Consumption | power_consumption | text | kW | — | Average or maximum electrical power draw during operation | 2.5, 5.0, 8.5, 15.0, 25.0 |
| Compressed Air Requirement | compressed_air_requirement | text | — | — | Air supply pressure and consumption rate | 6 bar / 100 NL/min, 0.6 MPa / 200 NL/min, 90 PSI / 5 CFM |
| Weighing Accuracy | weighing_accuracy | text | — | — | Precision of the weighing or dosing system | +/- 0.5 g, +/- 1.0 g, +/- 0.1%, +/- 0.5% |
| Number of Weighing Heads | number_of_weighing_heads | number | — | — | Count of weighing buckets on multihead weigher models | 10, 14, 16, 20, 24 |
| Changeover Time | changeover_time | text | — | — | Time required to switch between different package sizes or products | 5 min, 10 min, 15 min, 30 min, Tool-Free |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (PMMI, OMAC PackML) | [Syntegon](https://www.syntegon.com/solutions/food/vffs-machine/), [Paxiom](https://www.paxiom.com/vf-1200-high-speed-continuous-motion-bagger/), [Ishida](https://www.ishida.com/ww/en/products/weighing/ccw/), [Matrix Packaging](https://www.matrixpm.com/products/vertical-form-fill-seal-solutions/vffs-product-machines/) |
