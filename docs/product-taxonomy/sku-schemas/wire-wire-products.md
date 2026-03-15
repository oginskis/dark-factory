# SKU Schema: Wire & Wire Products

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | NW-BW-12GA-100, CW-SS316-010 |
| Product Name | text | Full product name including material, type, gauge, and packaging | 12 Gauge Galvanized Steel Baling Wire 100lb Coil, 316L Stainless Steel Fine Wire 0.010in Spool |
| URL | text | Direct link to the product page | https://example.com/product/12ga-galvanized-baling-wire |
| Price | number | Numeric unit price (per spool, per coil, per foot, or per pound) excluding currency symbol | 45.00, 89.95, 0.35, 2.80 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Wire manufacturer or brand name | Bekaert, Nucor, Central Wire, Encore Wire, Polar Wire, Remington Industries |
| Wire Type | enum | Primary product classification | Bare Wire, Welding Wire, Baling Wire, Fencing Wire, Spring Wire, Music Wire, Tie Wire, Barbed Wire, Mesh/Screen, Rope/Strand, Electrical Wire, MIG Wire, Armature Wire |
| Material | text | Base metal or alloy of the wire | Low Carbon Steel, High Carbon Steel, Stainless Steel 302, Stainless Steel 304, Stainless Steel 316, Aluminum, Copper, Brass, Phosphor Bronze, Nickel, Titanium, Nichrome |
| Diameter | number (in) | Wire diameter in inches | 0.001, 0.010, 0.032, 0.048, 0.062, 0.080, 0.105, 0.162 |
| Gauge (AWG/SWG) | text | Wire gauge number per American Wire Gauge or Standard Wire Gauge | 7, 9, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28 |
| Diameter (mm) | number (mm) | Wire diameter in millimetres for metric specifications | 0.025, 0.25, 0.50, 0.80, 1.20, 2.00, 3.00, 4.00 |
| Tensile Strength | number (psi) | Minimum tensile strength of the wire | 50000, 75000, 110000, 180000, 230000, 300000 |
| Tensile Strength Class | text | Tensile strength classification per applicable standard | Low, Medium, High, Extra High, Music Wire Grade |
| Temper | text | Mechanical condition of the wire | Annealed (Dead Soft), Quarter Hard, Half Hard, Full Hard, Spring Temper, Extra Spring |
| Coating/Surface | text | Surface treatment or protective coating | Bright (Uncoated), Hot-Dip Galvanized, Electro-Galvanized, Tin Plated, Copper Coated, PVC Coated, Nylon Coated, Aluminum-Zinc Coated, Phosphate |
| Coating Weight | text | Zinc or other coating weight class per ASTM | Class 1 (0.28 oz/ft2), Class 2 (0.60 oz/ft2), Class 3 (0.80 oz/ft2) |
| Conductivity | number (% IACS) | Electrical conductivity as percentage of IACS for conductive wire | 100, 97, 61, 3, 2 |
| Elongation | number (%) | Minimum elongation at break | 1, 3, 10, 15, 25, 35 |
| Spool/Package Weight | number (lbs) | Net weight of wire per spool, coil, or reel | 2, 5, 10, 25, 50, 100, 500, 2000 |
| Packaging Type | text | Form of packaging for the wire product | Spool, Coil, Reel, Carrier, Bale, Drum, Cut Lengths |
| Length per Package | number (ft) | Total wire length per package | 50, 100, 250, 500, 1000, 5000 |
| Mesh Size | text | Opening size for wire mesh and screen products | 2x2, 4x4, 1/4 in, 1/2 in, 1 in, 2 in |
| Wire Count (Strand) | number | Number of individual wires in a stranded or rope product | 1, 7, 19, 37, 49 |
| Specification | text (list) | Applicable ASTM, AWS, or industry standards | ASTM A641, ASTM A228, ASTM A580, ASTM A510, AWS A5.18, AISI Standard |
| Certification | text (list) | Quality and compliance certifications | ISO 9001, RoHS, REACH, Mill Test Report, CE |
| Application | text (list) | Primary intended uses | Binding, Baling, Fencing, Spring Making, Welding, Electrical, Mesh Fabrication, Reinforcement |
| Country of Origin | text | Country where the wire was manufactured | USA, Germany, Belgium, China, India, South Korea |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 27 attributes from 4 companies plus ASTM wire standards (A641, A228, A580) and AWG/SWG gauge systems | [Nucor Wire Products](https://nucor.com/products/wire-products), [Bekaert](https://www.bekaert.com/), [Central Wire Industries](https://centralwire.com/), [Baling Wire Direct](https://www.balingwiredirect.com/) |
