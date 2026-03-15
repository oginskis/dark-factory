# SKU Schema: Basic Organic Chemicals

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier catalog number or product identifier | A6283, 109088, 818755, 64-19-7-500ML |
| Product Name | text | Full product name including chemical name, grade, and purity | Acetic Acid glacial ReagentPlus 99%, Ethanol absolute for analysis 99.8%, Methanol HPLC grade 99.9% |
| URL | text | Direct link to the product page | https://example.com/product/acetic-acid-a6283 |
| Price | number | Numeric price per package unit excluding currency symbol | 28.50, 75.00, 142.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Chemical Name | text | IUPAC or common chemical name of the substance | Acetic acid, Ethanol, Methanol, Toluene, Acetone, Formaldehyde |
| CAS Number | text | Chemical Abstracts Service registry number uniquely identifying the substance | 64-19-7, 64-17-5, 67-56-1, 108-88-3, 67-64-1 |
| Molecular Formula | text | Empirical molecular formula showing atom counts | C2H4O2, C2H6O, CH4O, C7H8, C3H6O |
| Linear Formula | text | Structural formula showing connectivity of atoms | CH3COOH, C2H5OH, CH3OH, C6H5CH3, CH3COCH3 |
| Molecular Weight | number (g/mol) | Molar mass of the compound | 60.05, 46.07, 32.04, 92.14, 58.08 |
| EC Number | text | European Community number (EINECS/ELINCS) for regulatory identification | 200-580-7, 200-578-6, 200-659-6 |
| Purity | text | Minimum purity as a percentage or assay specification | 99%, 99.5%, 99.7%, 99.8%, 99.9%, 99.99% |
| Grade | text | Quality grade designation indicating intended application | ACS Reagent, ReagentPlus, HPLC, Spectroscopic, Technical, Pharma, Food |
| Form | enum | Physical state of the product as supplied | Liquid, Solid, Powder, Crystals, Pellets, Gas, Solution |
| Appearance | text | Visual description of the substance | Colorless liquid, White crystalline powder, Clear solution, Yellow liquid |
| Density | number (g/mL) | Density at standard temperature, typically 20 degC | 1.049, 0.789, 0.791, 0.866, 1.372 |
| Boiling Point | text (degC) | Boiling point or range at standard pressure | 118, 78.4, 64.7, 110.6, 56.1 |
| Melting Point | text (degC) | Melting point or freezing point at standard pressure | 16.6, -114, -98, -95, -95 |
| Flash Point | number (degC) | Lowest temperature at which vapours ignite near an ignition source | 39, 13, 9.7, 4, -20 |
| Refractive Index | number | Index of refraction measured at 20 degC using the sodium D-line | 1.3720, 1.3611, 1.3284, 1.4969, 1.3588 |
| Vapor Pressure | number (hPa) | Vapour pressure at 20 degC | 15.7, 58.6, 128, 29.1, 240 |
| Specific Gravity | number | Ratio of density to water at the same temperature | 1.05, 0.79, 0.87, 1.26 |
| Viscosity | text (mPa.s) | Dynamic viscosity at standard temperature | 1.13, 1.07, 0.59, 0.56, 0.32 |
| pH | text | pH value of the substance or its aqueous solution at a stated concentration | 2.4 (1 M), 7.0, Not applicable |
| Solubility in Water | text | Qualitative or quantitative solubility in water at 20 degC | Miscible, 1000 g/L, 0.47 g/L, Immiscible |
| Autoignition Temperature | number (degC) | Temperature at which the substance self-ignites without an external spark | 427, 363, 455, 480, 465 |
| Packaging Size | text | Available package quantities | 100 mL, 500 mL, 1 L, 2.5 L, 4 L, 25 L, 200 L |
| Packaging Type | text | Container type used for shipping and storage | Glass bottle, Amber glass bottle, HDPE bottle, Metal drum, IBC |
| GHS Hazard Pictograms | text (list) | Globally Harmonized System hazard pictogram codes on the product label | GHS02 Flame, GHS05 Corrosion, GHS07 Exclamation Mark, GHS06 Skull, GHS08 Health Hazard |
| Signal Word | enum | GHS signal word indicating severity of hazard | Danger, Warning |
| Hazard Statements | text (list) | GHS H-code hazard statements applicable to the substance | H226 Flammable liquid and vapour, H314 Causes severe skin burns, H332 Harmful if inhaled |
| Storage Class | text | Storage classification for safe warehousing, often per national or insurer guidelines | Flammable liquids, Corrosive substances, Oxidisers |
| Storage Temperature | text (degC) | Recommended storage temperature range | Room temperature, 2-8, 15-25, Below -20 |
| Shelf Life | text | Recommended maximum storage period from date of manufacture | 24 months, 36 months, 60 months |
| Country of Origin | text | Country where the chemical was manufactured | Germany, USA, China, India, Japan |
| Manufacturer | text | Name of the producing company | Sigma-Aldrich, Merck, Thermo Fisher, TCI, BASF, Dow |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (GHS Rev.9, CAS Registry, EC/EINECS) | [Sigma-Aldrich](https://www.sigmaaldrich.com/US/en/substance/aceticacid600564197), [Thermo Fisher](https://www.thermofisher.com/us/en/home/chemicals/specialty-chemicals-bulk-custom/organic-organometallic-chemicals.html), [TCI Chemicals](https://www.tcichemicals.com/US/en/categories/A0001), [ChemExper](https://www.chemexper.com/) |
