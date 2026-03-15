# SKU Schema: Cement & Concrete Products

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.cement_concrete`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | QR-1101-80, CX-RMC-4000, HD-1001560808 |
| Product Name | product_name | text | Full product name including product type, strength class, and bag size | QUIKRETE Concrete Mix 80 lb, Cemex Ready-Mix 4000 PSI, Sakrete Fast-Setting Concrete 50 lb |
| URL | url | text | Direct link to the product page | https://example.com/product/quikrete-concrete-80lb |
| Price | price | number | Numeric price per bag, per cubic yard, or per unit, excluding currency symbol | 5.48, 8.97, 145.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary product classification | Concrete Mix, Cement, Mortar Mix, Grout, Ready-Mix Concrete, Precast Unit, Resurfacer, Stucco Mix |
| Cement Type | cement_type | text | Portland cement type classification per ASTM C150 | Type I, Type II, Type III, Type I/II, Type V |
| Country of Origin | country_of_origin | text | Manufacturing country | USA, Mexico, Canada, Germany, India |
| Bag Size | bag_size | number (lb) | Weight of the packaged dry mix | 40, 50, 60, 80, 90 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Compressive Strength 28d | compressive_strength_28d | number (psi) | Compressive strength at 28 days of cure | 2500, 4000, 5000, 6000, 7000, 8000 |
| Compressive Strength 7d | compressive_strength_7d | number (psi) | Compressive strength at 7 days of cure | 1500, 2500, 3500, 4500 |
| Early Strength | early_strength | text | Rapid strength gain description if applicable | 3000 PSI at 3 hours, 5000 PSI at 24 hours |
| Set Time | set_time | text | Initial and final setting time | 20-30 minutes, 2-4 hours, 10-12 hours |
| Walk-on Time | walk-on_time | text | Time before surface can bear foot traffic | 20 minutes, 4 hours, 8 hours, 24 hours |
| Yield per Bag | yield_per_bag | number (cu ft) | Volume of mixed concrete per bag | 0.30, 0.375, 0.45, 0.60, 0.675 |
| Coverage | coverage | text | Area or volume coverage guidance | 4 sq ft at 2 in depth per 80 lb bag |
| Slump | slump | text (in) | Workability measurement of fresh concrete | 2-3, 3-4, 4-6 |
| Water Ratio | water_ratio | text | Recommended water to dry mix ratio | 3 quarts per 80 lb bag, 6 pints per 60 lb bag |
| Air Content | air_content | number (%) | Entrained air percentage in fresh concrete | 3, 5, 6, 7 |
| Application | application | text (list) | Primary intended uses | Foundations, Sidewalks, Driveways, Posts, Slabs, Steps, Patching, Countertops, Structural |
| Fiber Reinforced | fiber_reinforced | enum | Whether structural fibers are included in the mix | Yes, No |
| Polymer Modified | polymer_modified | enum | Whether polymer additives enhance performance | Yes, No |
| Freeze-Thaw Resistant | freeze-thaw_resistant | enum | Whether the product is rated for freeze-thaw cycling | Yes, No |
| ASTM Standard | astm_standard | text (list) | Governing ASTM specifications | ASTM C 150, ASTM C 387, ASTM C 39, ASTM C 270, ASTM C 476 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus ASTM standards (C 150, C 387, C 39) | [QUIKRETE](https://www.quikrete.com/), [Cemex](https://www.cemexusa.com/products-and-services/concrete), [Precast Concrete Sales](https://precastconcretesales.com/project/concrete-products/), [Home Depot](https://www.homedepot.com/b/Building-Materials-Concrete-Cement-Masonry/Pre-Mixed/N-5yc1vZarlkZ1z19a8s) |
