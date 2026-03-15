# SKU Schema: Fasteners (Bolts, Nuts, Screws, Rivets)

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.fasteners`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | HCS-38-16X2-GR5-ZN, SS-10-32-FH-18-8 |
| Product Name | product_name | text | Full product name including type, size, material, and finish | Grade 5 Hex Cap Screw 3/8-16 x 2in Zinc Plated, 18-8 Stainless Steel Flat Head Machine Screw 10-32 x 1in |
| URL | url | text | Direct link to the product page | https://example.com/product/gr5-hex-cap-screw-3-8-16x2 |
| Price | price | number | Numeric unit price (per piece or per box/bag) excluding currency symbol | 0.12, 4.50, 18.99 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Fastener Type | fastener_type | enum | Primary fastener category | Hex Bolt, Hex Cap Screw, Carriage Bolt, Socket Head Cap Screw, Machine Screw, Sheet Metal Screw, Self-Drilling Screw, Wood Screw, Lag Screw, Hex Nut, Lock Nut, Wing Nut, Flange Nut, Flat Washer, Lock Washer, Blind Rivet, Solid Rivet, Structural Bolt, Anchor Bolt, Set Screw, Threaded Rod |
| Head Type | head_type | text | Shape of the fastener head | Hex, Socket Head, Button Head, Flat (Countersunk), Pan, Truss, Round, Oval, Fillister, Flanged Hex |
| Drive Type | drive_type | text | Tool engagement style for screws | Hex (Wrench), Phillips, Slotted, Torx, Allen (Hex Socket), Square (Robertson), Combo, Star, Tamper-Resistant |
| Thread Type | thread_type | enum | Thread standard system | UNC (Coarse), UNF (Fine), Metric Coarse, Metric Fine, ACME, Buttress |
| Material | material | text | Base material of the fastener | Carbon Steel, Alloy Steel, 18-8 Stainless Steel, 316 Stainless Steel, Brass, Silicon Bronze, Aluminum, Nylon, Titanium |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Grade/Class | gradeclass | text | Strength grade per applicable standard | Grade 2, Grade 5, Grade 8, Class 8.8, Class 10.9, Class 12.9, A2-70, A4-80 |
| Point Type | point_type | text | Tip style of the fastener | Flat, Cone, Cup, Dog, Pilot, Self-Drilling, Type A, Type AB, Type B |
| Country of Origin | country_of_origin | text | Country where the fastener was manufactured | USA, Taiwan, Japan, Germany, India, China |
| Finish/Coating | finishcoating | text | Surface treatment or protective coating | Zinc Plated, Hot-Dip Galvanized, Black Oxide, Dacromet, Geomet, Cadmium Plated, Plain (Uncoated), Chrome Plated, Phosphate |
| Tensile Strength | tensile_strength | number (psi) | Minimum tensile strength of the fastener | 60000, 120000, 150000, 170000 |
| Proof Load | proof_load | number (psi) | Minimum proof load stress | 55000, 85000, 120000 |
| Nut Height | nut_height | number (in) | Height of nuts when applicable | 0.188, 0.328, 0.448, 0.575 |
| Washer OD | washer_od | number (in) | Outside diameter for washers | 0.562, 0.813, 1.062, 1.375 |
| Grip Range | grip_range | text (in) | Thickness range a rivet or anchor can fasten | 0.020-0.125, 0.126-0.250, 0.251-0.500 |
| Quantity per Pack | quantity_per_pack | number | Number of pieces per sales unit (box, bag, or each) | 1, 10, 25, 50, 100, 500, 1000 |
| Corrosion Resistance | corrosion_resistance | enum | Relative corrosion resistance level | Low, Moderate, High, Very High |
| Specification | specification | text (list) | Applicable ASTM, SAE, ISO, or DIN standards | ASTM A307, ASTM A325, ASTM A490, SAE J429, ISO 898-1, DIN 933, DIN 934 |
| Certification | certification | text (list) | Quality and compliance certifications | ISO 9001, IFI, DFARS Compliant, RoHS, PPAP |
| Thread Size | thread_size | text | Nominal diameter and threads per inch (imperial) or diameter and pitch (metric) | 1/4-20, 3/8-16, 1/2-13, M6x1.0, M8x1.25, M10x1.5, M12x1.75 |
| Length | length | text (in) | Fastener length measured per standard conventions | 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus SAE J429 grade system and ISO 898 property class standards | [Fastener SuperStore](https://www.fastenersuperstore.com/), [Bolt Depot](https://boltdepot.com/), [Albany County Fasteners](https://www.albanycountyfasteners.com/), [MSC Industrial](https://www.mscdirect.com/browse/Fasteners) |
