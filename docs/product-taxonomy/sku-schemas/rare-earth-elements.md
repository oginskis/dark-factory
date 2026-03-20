# SKU Schema: Rare Earth Elements

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.rare_earth`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier or manufacturer product identifier | REE-NdOx-4N-1KG, AEM-Dy-5N-500G, MSE-CeO2-5N |
| Product Name | product_name | text | — | yes | Full product name including element, compound type, purity, and form | Neodymium Oxide (Nd2O3) 99.99% 4N Powder, Dysprosium Metal 99.999% 5N Ingot, Cerium Oxide Polishing Grade 98% TREO |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/products/neodymium-oxide-4n |
| Price | price | number | — | yes | Numeric price per unit (per kg, per g, or per package), excluding currency symbol | 45.00, 250.00, 1800.00, 5500.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, CNY, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Compound Type | compound_type | enum | — | — | Chemical form of the product | Oxide, Metal, Fluoride, Chloride, Carbonate, Nitrate, Acetate, Hydroxide, Sulfate, Bromide, Iodide, Alloy |
| Chemical Formula | chemical_formula | text | — | — | Molecular formula of the product | Nd2O3, CeO2, La2O3, Dy2O3, NdFeB, PrNd alloy |
| Physical Form | physical_form | enum | — | — | Physical form of the product as supplied | Powder, Granules, Ingot, Lumps, Sputtering Target, Solution, Nanopowder, Pellets, Rod |
| Country of Origin | country_of_origin | text | — | — | Country where the element was extracted or refined | China, USA, Australia, Myanmar, India, Japan |
| Hazmat Classification | hazmat_classification | text | — | — | Transport hazard classification if applicable | Non-hazardous, UN3178 (flammable solid), UN3089 (metal powder) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Element Name | element_name | text | — | — | Name of the rare earth element | Lanthanum, Cerium, Praseodymium, Neodymium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Thulium, Ytterbium, Lutetium, Yttrium, Scandium |
| Element Symbol | element_symbol | text | — | — | Chemical symbol of the element | La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Y, Sc |
| CAS Number | cas_number | text | — | — | Chemical Abstracts Service registry number | 1313-97-9, 1306-38-3, 1314-37-0, 12061-16-4 |
| Purity (REO Basis) | purity_reo_basis | text | — | — | Chemical purity on a rare earth oxide basis, often expressed in N notation | 99% (2N), 99.9% (3N), 99.99% (4N), 99.999% (5N), 99.9999% (6N) |
| TREO Content | treo_content | number | % | — | Total rare earth oxide content as percentage of total product weight | 85.0, 92.0, 98.0, 99.5 |
| Density | density | number | g/cm3 | — | Measured or theoretical density of the product | 5.22, 6.77, 7.01, 7.54, 8.55 |
| Melting Point | melting_point | number | degC | — | Melting point of the element or compound | 798, 920, 1021, 1529, 2600 |
| Specific Surface Area | specific_surface_area | number | m2/g | — | BET specific surface area for powder and nano products | 0.5, 2.0, 5.0, 10.0, 50.0 |
| Trace Impurities | trace_impurities | text | — | — | Key metallic impurities reported on the Certificate of Analysis | Fe less than 5 ppm, Ca less than 10 ppm, Si less than 20 ppm |
| Packaging | packaging | text | — | — | Container or packaging type | Glass bottle, Plastic bottle, Sealed drum, Vacuum-sealed bag |
| Application | application | text (list) | — | — | Primary intended industrial uses | Permanent Magnets, Catalysts, Polishing, Phosphors, Lasers, Glass Additives, Ceramics, Nuclear, Battery Materials |
| Element Group | element_group | enum | — | — | Classification within the rare earth series | Light Rare Earth (LREE), Heavy Rare Earth (HREE) |
| Certificate of Analysis | certificate_of_analysis | enum | — | — | Whether a CoA is provided with shipment | Included, Available on Request, Not Available |
| Certification | certification | text (list) | — | — | Quality or regulatory certifications | ISO 9001, ISO 14001, REACH registered, RoHS compliant |
| Shelf Life | shelf_life | text | — | — | Recommended storage duration | 12 months, 24 months, 36 months, Indefinite if sealed |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM rare earth specifications, ISO purity standards, TREO conventions) | [American Elements](https://www.americanelements.com/rare-earths.html), [AEM REE](https://www.aemree.com/), [MSE Supplies](https://www.msesupplies.com/collections/high-purity-inorganic-chemicals/rare-earth-oxide), [Stanford Advanced Materials](https://www.samaterials.com/) |
