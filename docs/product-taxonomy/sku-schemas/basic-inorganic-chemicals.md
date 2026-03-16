# SKU Schema: Basic Inorganic Chemicals

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products
**Taxonomy ID:** `chemicals.basic_inorganic`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Supplier catalog number or product identifier | 30046436, S7653, 10305-500G, A144C-212 |
| Product Name | product_name | text | — | Full product name including chemical name, grade, and specification | Sodium Nitrite HQ free flowing non-food grade, Hydrochloric Acid 37% ACS Reagent, Sodium Hydroxide pellets 99% |
| URL | url | text | — | Direct link to the product page | https://example.com/products/sodium-nitrite-30046436 |
| Price | price | number | — | Numeric price per package unit excluding currency symbol | 18.50, 42.00, 95.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Molecular Formula | molecular_formula | text | — | Empirical molecular formula | NaNO2, HCl, NaOH, H2SO4, NH4Cl |
| Grade | grade | text | — | Quality grade designation indicating intended application | ACS Reagent, Technical, Food (E250), Pharma, Puriss, High Purity, Electronic |
| Form | form | enum | — | Physical state and morphology of the product as supplied | Powder, Pellets, Granules, Flakes, Crystals, Liquid, Solution, Lumps, Free flowing powder |
| Packaging Type | packaging_type | text | — | Container type used for shipping and storage | HDPE bottle, Glass bottle, Polyethylene bag, Fibre drum, Steel drum, IBC, Bulk |
| Country of Origin | country_of_origin | text | — | Country where the chemical was manufactured | Germany, USA, India, China, Japan |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Chemical Name | chemical_name | text | — | IUPAC or common chemical name of the substance | Sodium nitrite, Hydrochloric acid, Sodium hydroxide, Sulfuric acid, Ammonium chloride |
| CAS Number | cas_number | text | — | Chemical Abstracts Service registry number uniquely identifying the substance | 7632-00-0, 7647-01-0, 1310-73-2, 7664-93-9, 12125-02-9 |
| EC Number | ec_number | text | — | European Community number (EINECS/ELINCS) for regulatory identification | 231-555-9, 231-595-7, 215-185-5 |
| Assay/Purity | assaypurity | text | — | Minimum assay or purity as a percentage | 98%, 99%, 99.5%, 99.99% (metals basis), 37-38% (for solutions) |
| Appearance | appearance | text | — | Visual description of the substance | White crystalline powder, Colorless liquid, Clear solution, Yellow powder |
| Concentration | concentration | text | — | Concentration for products supplied as solutions, expressed as weight percent | 37%, 38-40%, 45%, 50%, 96% |
| Density | density | number | g/mL | Density at standard temperature, typically 20 degC | 2.17, 1.18, 2.13, 1.84, 1.53 |
| Melting Point | melting_point | text | degC | Melting or decomposition point at standard pressure | 271, -27, 318, 10.4, 338 |
| Boiling Point | boiling_point | text | degC | Boiling point at standard pressure for volatile compounds or solutions | 320 (decomp), 110, 1388, 337, 520 |
| pH | ph | text | — | pH of the substance in aqueous solution at a stated concentration | 9.0 (50 g/L), Less than 1 (37%), 14 (1 M), 4.5-5.0 (100 g/L) |
| Solubility in Water | solubility_in_water | text | — | Solubility in water at 20 degC expressed quantitatively or qualitatively | 820 g/L, Miscible, 1110 g/L, 370 g/L |
| Loss on Drying | loss_on_drying | text | — | Maximum weight loss when dried under specified conditions, as a percentage | 0.5% max, 1.0% max, 2.0% max |
| Residue on Ignition | residue_on_ignition | text | — | Residue remaining after ignition at specified temperature, as a percentage | 0.01% max, 0.05% max, 0.1% max |
| Heavy Metals Content | heavy_metals_content | text | — | Maximum allowable heavy metals expressed as lead (Pb) equivalent | 5 ppm max, 10 ppm max, 20 ppm max |
| Chloride Content | chloride_content | text | — | Maximum chloride impurity as a percentage or ppm | 0.001% max, 50 ppm max, 0.005% max |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (GHS Rev.9, CAS Registry, ACS Reagent Chemicals) | [BASF](https://chemicals.basf.com/global/en/Monomers/inorganic-chemicals), [Materion](https://www.materion.com/en/products/electronic-materials/advanced-chemicals/inorganic-chemicals-catalog), [Thermo Fisher](https://www.fishersci.com/us/en/scientific-products/featured-categories/thermo-scientific-featured-categories/thermo-scientific-chemicals.html), [GFS Chemicals](https://www.gfschemicals.com/) |
