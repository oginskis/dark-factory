# SKU Schema: Cement & Concrete Products

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | QR-1101-80, CX-RMC-4000, HD-1001560808 |
| Product Name | text | Full product name including product type, strength class, and bag size | QUIKRETE Concrete Mix 80 lb, Cemex Ready-Mix 4000 PSI, Sakrete Fast-Setting Concrete 50 lb |
| URL | text | Direct link to the product page | https://example.com/product/quikrete-concrete-80lb |
| Price | number | Numeric price per bag, per cubic yard, or per unit, excluding currency symbol | 5.48, 8.97, 145.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | QUIKRETE, Cemex, Sakrete, LafargeHolcim, CRH, Heidelberg Materials |
| Product Type | enum | Primary product classification | Concrete Mix, Cement, Mortar Mix, Grout, Ready-Mix Concrete, Precast Unit, Resurfacer, Stucco Mix |
| Cement Type | text | Portland cement type classification per ASTM C150 | Type I, Type II, Type III, Type I/II, Type V |
| Compressive Strength 28d | number (psi) | Compressive strength at 28 days of cure | 2500, 4000, 5000, 6000, 7000, 8000 |
| Compressive Strength 7d | number (psi) | Compressive strength at 7 days of cure | 1500, 2500, 3500, 4500 |
| Early Strength | text | Rapid strength gain description if applicable | 3000 PSI at 3 hours, 5000 PSI at 24 hours |
| Set Time | text | Initial and final setting time | 20-30 minutes, 2-4 hours, 10-12 hours |
| Walk-on Time | text | Time before surface can bear foot traffic | 20 minutes, 4 hours, 8 hours, 24 hours |
| Bag Size | number (lb) | Weight of the packaged dry mix | 40, 50, 60, 80, 90 |
| Yield per Bag | number (cu ft) | Volume of mixed concrete per bag | 0.30, 0.375, 0.45, 0.60, 0.675 |
| Coverage | text | Area or volume coverage guidance | 4 sq ft at 2 in depth per 80 lb bag |
| Slump | text (in) | Workability measurement of fresh concrete | 2-3, 3-4, 4-6 |
| Unit Weight | number (pcf) | Density of cured concrete in pounds per cubic foot | 130, 140, 145, 150 |
| Water Ratio | text | Recommended water to dry mix ratio | 3 quarts per 80 lb bag, 6 pints per 60 lb bag |
| Air Content | number (%) | Entrained air percentage in fresh concrete | 3, 5, 6, 7 |
| Application | text (list) | Primary intended uses | Foundations, Sidewalks, Driveways, Posts, Slabs, Steps, Patching, Countertops, Structural |
| Aggregate Size | text | Maximum aggregate particle size | 3/8 in, 3/4 in, 1 in, 1-1/2 in, Pea Gravel |
| Fiber Reinforced | enum | Whether structural fibers are included in the mix | Yes, No |
| Polymer Modified | enum | Whether polymer additives enhance performance | Yes, No |
| Freeze-Thaw Resistant | enum | Whether the product is rated for freeze-thaw cycling | Yes, No |
| ASTM Standard | text (list) | Governing ASTM specifications | ASTM C 150, ASTM C 387, ASTM C 39, ASTM C 270, ASTM C 476 |
| Certification | text (list) | Third-party compliance listings | UL, ICC-ES, NSF 61, Green Seal |
| Shelf Life | text | Maximum storage time before use | 12 months, 6 months |
| Pallet Quantity | number | Number of bags per pallet | 35, 42, 56, 63, 80 |
| Country of Origin | text | Manufacturing country | USA, Mexico, Canada, Germany, India |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus ASTM standards (C 150, C 387, C 39) | [QUIKRETE](https://www.quikrete.com/), [Cemex](https://www.cemexusa.com/products-and-services/concrete), [Precast Concrete Sales](https://precastconcretesales.com/project/concrete-products/), [Home Depot](https://www.homedepot.com/b/Building-Materials-Concrete-Cement-Masonry/Pre-Mixed/N-5yc1vZarlkZ1z19a8s) |
