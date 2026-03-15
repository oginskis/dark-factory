# SKU Schema: Bricks, Blocks & Masonry

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.bricks_blocks_masonry`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | RCP-8816P, CM-HRZ-8, HD-100002403 |
| Product Name | text | Full product name including type, size, and finish | Standard Concrete Block 8 x 8 x 16, Clay Face Brick King Size Red, Splitface CMU 12 in |
| URL | text | Direct link to the product page | https://example.com/product/cmu-8x8x16 |
| Price | number | Numeric price per unit or per thousand, excluding currency symbol | 1.85, 3.50, 650.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary masonry unit classification | Concrete Block, Clay Brick, Concrete Brick, Glass Block, Stone Veneer, Retaining Wall Block, Paver, Lintel Block |
| Material | enum | Base material of the unit | Concrete, Clay, Calcium Silicate, Natural Stone, Glass |
| Weight Classification | enum | Density classification per ASTM C 90 | Lightweight, Medium Weight, Normal Weight |
| Sound Transmission Class | number | STC rating for noise reduction in wall assemblies | 40, 45, 48, 52, 55 |
| Country of Origin | text | Manufacturing country | USA, Canada, Mexico, India, UK |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Nominal Width | number (in) | Nominal face-to-face width (includes mortar joint) | 4, 6, 8, 10, 12, 16 |
| Nominal Height | number (in) | Nominal top-to-bottom height (includes mortar joint) | 4, 8, 16 |
| Actual Width | number (in) | Manufactured width minus mortar allowance | 3.625, 5.625, 7.625, 9.625, 11.625 |
| Actual Height | number (in) | Manufactured height minus mortar allowance | 2.25, 3.625, 7.625 |
| Compressive Strength | number (psi) | Minimum net area compressive strength | 1900, 2000, 2500, 3000, 3500, 5000, 8000 |
| Core Configuration | enum | Hollow or solid designation | Hollow, Solid, Semi-Solid |
| Surface Finish | text | Exterior face texture or treatment | Smooth, Splitface, Ground Face, Shotblast, Scored, Burnished, Slump, Fluted |
| Color | text | Body color or face color of the unit | Gray, Tan, Red, Charcoal, Buff, Brown, White, Custom Blend |
| Water Absorption | number (%) | Maximum percentage of water absorbed | 8, 10, 13, 17 |
| Fire Resistance Rating | text (hours) | Fire endurance rating for wall assemblies | 1, 2, 3, 4 |
| Equivalent Thickness | number (in) | Solid thickness equivalent for fire-rating calculation | 2.8, 3.8, 4.4, 5.9, 7.0 |
| Linear Shrinkage | number (%) | Maximum drying shrinkage | 0.03, 0.045, 0.065 |
| Application | text (list) | Primary intended uses | Load-Bearing Wall, Partition Wall, Foundation, Retaining Wall, Veneer, Landscape, Paving |
| ASTM Standard | text (list) | Governing ASTM specifications | ASTM C 90, ASTM C 129, ASTM C 62, ASTM C 216, ASTM C 652, ASTM C 1006 |
| Certification | text (list) | Third-party certifications | LEED Eligible, ICC-ES, NCMA Certified |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus ASTM standards (C 90, C 216, C 62) | [RCP Block and Brick](https://www.rcpblock.com/block.html), [County Materials](https://www.countymaterials.com/products/masonry), [Home Depot](https://www.homedepot.com/b/Building-Materials-Concrete-Cement-Masonry-Cinder-Blocks/N-5yc1vZcdpe), [CMHA](https://www.cmha.org/resource/cmu-tec-001/) |
