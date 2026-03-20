# SKU Schema: Basic Organic Chemicals

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products
**Taxonomy ID:** `chemicals.basic_organic`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier catalog number or product identifier | A6283, 109088, 818755, 64-19-7-500ML |
| Product Name | product_name | text | — | yes | Full product name including chemical name, grade, and purity | Acetic Acid glacial ReagentPlus 99%, Ethanol absolute for analysis 99.8%, Methanol HPLC grade 99.9% |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/acetic-acid-a6283 |
| Price | price | number | — | yes | Numeric price per package unit excluding currency symbol | 28.50, 75.00, 142.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Molecular Formula | molecular_formula | text | — | — | Empirical molecular formula showing atom counts | C2H4O2, C2H6O, CH4O, C7H8, C3H6O |
| Linear Formula | linear_formula | text | — | — | Structural formula showing connectivity of atoms | CH3COOH, C2H5OH, CH3OH, C6H5CH3, CH3COCH3 |
| Grade | grade | text | — | — | Quality grade designation indicating intended application | ACS Reagent, ReagentPlus, HPLC, Spectroscopic, Technical, Pharma, Food |
| Form | form | enum | — | — | Physical state of the product as supplied | Liquid, Solid, Powder, Crystals, Pellets, Gas, Solution |
| Packaging Type | packaging_type | text | — | — | Container type used for shipping and storage | Glass bottle, Amber glass bottle, HDPE bottle, Metal drum, IBC |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Storage Class | storage_class | text | — | — | Storage classification for safe warehousing, often per national or insurer guidelines | Flammable liquids, Corrosive substances, Oxidisers |
| Country of Origin | country_of_origin | text | — | — | Country where the chemical was manufactured | Germany, USA, China, India, Japan |
| Chemical Name | chemical_name | text | — | — | IUPAC or common chemical name of the substance | Acetic acid, Ethanol, Methanol, Toluene, Acetone, Formaldehyde |
| CAS Number | cas_number | text | — | — | Chemical Abstracts Service registry number uniquely identifying the substance | 64-19-7, 64-17-5, 67-56-1, 108-88-3, 67-64-1 |
| EC Number | ec_number | text | — | — | European Community number (EINECS/ELINCS) for regulatory identification | 200-580-7, 200-578-6, 200-659-6 |
| Purity | purity | text | — | — | Minimum purity as a percentage or assay specification | 99%, 99.5%, 99.7%, 99.8%, 99.9%, 99.99% |
| Appearance | appearance | text | — | — | Visual description of the substance | Colorless liquid, White crystalline powder, Clear solution, Yellow liquid |
| Density | density | number | g/mL | — | Density at standard temperature, typically 20 degC | 1.049, 0.789, 0.791, 0.866, 1.372 |
| Boiling Point | boiling_point | text | degC | — | Boiling point or range at standard pressure | 118, 78.4, 64.7, 110.6, 56.1 |
| Melting Point | melting_point | text | degC | — | Melting point or freezing point at standard pressure | 16.6, -114, -98, -95, -95 |
| Flash Point | flash_point | number | degC | — | Lowest temperature at which vapours ignite near an ignition source | 39, 13, 9.7, 4, -20 |
| Refractive Index | refractive_index | number | — | — | Index of refraction measured at 20 degC using the sodium D-line | 1.3720, 1.3611, 1.3284, 1.4969, 1.3588 |
| Vapor Pressure | vapor_pressure | number | hPa | — | Vapour pressure at 20 degC | 15.7, 58.6, 128, 29.1, 240 |
| Specific Gravity | specific_gravity | number | — | — | Ratio of density to water at the same temperature | 1.05, 0.79, 0.87, 1.26 |
| Viscosity | viscosity | text | mPa.s | — | Dynamic viscosity at standard temperature | 1.13, 1.07, 0.59, 0.56, 0.32 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (GHS Rev.9, CAS Registry, EC/EINECS) | [Sigma-Aldrich](https://www.sigmaaldrich.com/US/en/substance/aceticacid600564197), [Thermo Fisher](https://www.thermofisher.com/us/en/home/chemicals/specialty-chemicals-bulk-custom/organic-organometallic-chemicals.html), [TCI Chemicals](https://www.tcichemicals.com/US/en/categories/A0001), [ChemExper](https://www.chemexper.com/) |
