# SKU Schema: Wire & Wire Products

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.wire_products`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | NW-BW-12GA-100, CW-SS316-010 |
| Product Name | product_name | text | — | yes | Full product name including material, type, gauge, and packaging | 12 Gauge Galvanized Steel Baling Wire 100lb Coil, 316L Stainless Steel Fine Wire 0.010in Spool |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/12ga-galvanized-baling-wire |
| Price | price | number | — | yes | Numeric unit price (per spool, per coil, per foot, or per pound) excluding currency symbol | 45.00, 89.95, 0.35, 2.80 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Wire Type | wire_type | enum | — | — | Primary product classification | Bare Wire, Welding Wire, Baling Wire, Fencing Wire, Spring Wire, Music Wire, Tie Wire, Barbed Wire, Mesh/Screen, Rope/Strand, Electrical Wire, MIG Wire, Armature Wire |
| Material | material | text | — | — | Base metal or alloy of the wire | Low Carbon Steel, High Carbon Steel, Stainless Steel 302, Stainless Steel 304, Stainless Steel 316, Aluminum, Copper, Brass, Phosphor Bronze, Nickel, Titanium, Nichrome |
| Tensile Strength Class | tensile_strength_class | text | — | — | Tensile strength classification per applicable standard | Low, Medium, High, Extra High, Music Wire Grade |
| Packaging Type | packaging_type | text | — | — | Form of packaging for the wire product | Spool, Coil, Reel, Carrier, Bale, Drum, Cut Lengths |
| Country of Origin | country_of_origin | text | — | — | Country where the wire was manufactured | USA, Germany, Belgium, China, India, South Korea |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Gauge (AWG/SWG) | gauge_awgswg | text | — | — | Wire gauge number per American Wire Gauge or Standard Wire Gauge | 7, 9, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28 |
| Tensile Strength | tensile_strength | number | psi | — | Minimum tensile strength of the wire | 50000, 75000, 110000, 180000, 230000, 300000 |
| Temper | temper | text | — | — | Mechanical condition of the wire | Annealed (Dead Soft), Quarter Hard, Half Hard, Full Hard, Spring Temper, Extra Spring |
| Coating/Surface | coatingsurface | text | — | — | Surface treatment or protective coating | Bright (Uncoated), Hot-Dip Galvanized, Electro-Galvanized, Tin Plated, Copper Coated, PVC Coated, Nylon Coated, Aluminum-Zinc Coated, Phosphate |
| Conductivity | conductivity | number | % IACS | — | Electrical conductivity as percentage of IACS for conductive wire | 100, 97, 61, 3, 2 |
| Elongation | elongation | number | % | — | Minimum elongation at break | 1, 3, 10, 15, 25, 35 |
| Specification | specification | text (list) | — | — | Applicable ASTM, AWS, or industry standards | ASTM A641, ASTM A228, ASTM A580, ASTM A510, AWS A5.18, AISI Standard |
| Certification | certification | text (list) | — | — | Quality and compliance certifications | ISO 9001, RoHS, REACH, Mill Test Report, CE |
| Application | application | text (list) | — | — | Primary intended uses | Binding, Baling, Fencing, Spring Making, Welding, Electrical, Mesh Fabrication, Reinforcement |
| Diameter | diameter | number | in | — | Wire diameter in inches | 0.001, 0.010, 0.032, 0.048, 0.062, 0.080, 0.105, 0.162 |
| Diameter (mm) | diameter_mm | number | mm | — | Wire diameter in millimetres for metric specifications | 0.025, 0.25, 0.50, 0.80, 1.20, 2.00, 3.00, 4.00 |
| Coating Weight | coating_weight | text | — | — | Zinc or other coating weight class per ASTM | Class 1 (0.28 oz/ft2), Class 2 (0.60 oz/ft2), Class 3 (0.80 oz/ft2) |
| Spool/Package Weight | spoolpackage_weight | number | lbs | — | Net weight of wire per spool, coil, or reel | 2, 5, 10, 25, 50, 100, 500, 2000 |
| Length per Package | length_per_package | number | ft | — | Total wire length per package | 50, 100, 250, 500, 1000, 5000 |
| Mesh Size | mesh_size | text | — | — | Opening size for wire mesh and screen products | 2x2, 4x4, 1/4 in, 1/2 in, 1 in, 2 in |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 27 attributes from 4 companies plus ASTM wire standards (A641, A228, A580) and AWG/SWG gauge systems | [Nucor Wire Products](https://nucor.com/products/wire-products), [Bekaert](https://www.bekaert.com/), [Central Wire Industries](https://centralwire.com/), [Baling Wire Direct](https://www.balingwiredirect.com/) |
