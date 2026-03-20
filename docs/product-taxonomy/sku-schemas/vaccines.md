# SKU Schema: Vaccines

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.vaccines`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Distributor or pharmacy product identifier | VSH-PFZ-PCV20, CDC-FLU-QIV, MCK-VAX-0045 |
| Product Name | product_name | text | — | yes | Full product name including brand name, valency, and target disease | Prevnar 20 Pneumococcal 20-Valent Conjugate Vaccine, Fluzone High-Dose Quadrivalent, Shingrix Recombinant Adjuvanted Vaccine |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/prevnar-20 |
| Price | price | number | — | yes | Numeric price per dose or per package excluding currency symbol | 269.00, 80.75, 195.50 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CHF, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Vaccine Type | vaccine_type | text | — | — | Technology or platform used to produce the vaccine | Conjugate, Inactivated, Live Attenuated, mRNA, Recombinant Protein, Toxoid, Viral Vector |
| Antigen Composition | antigen_composition | text | — | — | Description of the antigenic components and their quantities per dose | 20 pneumococcal polysaccharide serotypes conjugated to CRM197 carrier protein, 15 mcg HA per strain |
| Dosage Form | dosage_form | text | — | — | Physical form of the vaccine product | Suspension for Injection, Lyophilized Powder for Reconstitution, Solution for Injection, Emulsion for Injection |
| Country of Origin | country_of_origin | text | — | — | Country where the finished vaccine is manufactured | USA, Belgium, France, India, UK, Germany |
| Package Size | package_size | text | — | — | Number of doses or units per commercial package | 10 Prefilled Syringes, 10 Single-Dose Vials, 1 Carton of 50 Vials |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Brand Name | brand_name | text | — | — | Proprietary trade name of the vaccine | Prevnar 20, Fluzone, Shingrix, Gardasil 9, MMR-II, Vaxelis |
| Manufacturer | manufacturer | text | — | — | Name of the vaccine manufacturer or marketing authorization holder | Pfizer, Sanofi Pasteur, GlaxoSmithKline, Merck, Moderna, Serum Institute of India |
| Disease Target | disease_target | text (list) | — | — | Disease(s) or pathogen(s) the vaccine protects against | Pneumococcal Disease, Influenza, Herpes Zoster, HPV, Measles Mumps Rubella, COVID-19 |
| Valency | valency | text | — | — | Number of serotypes or strains covered by the vaccine | Monovalent, 4-Valent, 9-Valent, 13-Valent, 20-Valent, 23-Valent |
| Adjuvant | adjuvant | text | — | — | Immune-enhancing substance included in the formulation | Aluminum Phosphate, AS01B, AS04, MF59, None |
| Preservative | preservative | text | — | — | Antimicrobial preservative included in multi-dose formulations | Thimerosal, 2-Phenoxyethanol, None (Preservative Free) |
| Dose Volume | dose_volume | number | mL | — | Volume of a single dose | 0.5, 0.25, 1.0 |
| Route of Administration | route_of_administration | text | — | — | Method by which the vaccine is delivered | Intramuscular, Subcutaneous, Intradermal, Oral, Intranasal |
| Presentation | presentation | text | — | — | Container type and configuration | Prefilled Syringe, Single-Dose Vial, Multi-Dose Vial, Nasal Spray |
| Doses Per Container | doses_per_container | number | — | — | Number of doses contained in a single vial or device | 1, 5, 10, 20 |
| Approved Age Group | approved_age_group | text | — | — | Age range for which the vaccine is approved or recommended | 6 Weeks and Older, 2 Months Through 17 Years, 50 Years and Older, 12 Years and Older |
| Schedule | schedule | text | — | — | Recommended dosing schedule (number of doses and intervals) | Single Dose, 2 Doses 2-6 Months Apart, 3 Doses at 0-1-6 Months, Annual |
| NDC | ndc | text | — | — | National Drug Code for US market identification | 00005-1971-05, 49281-0718-50, 58160-0823-52 |
| Storage Temperature | storage_temperature | text | — | — | Required storage temperature range | 2-8C (36-46F), -25 to -15C, -80 to -60C |
| Cold Chain Required | cold_chain_required | enum | — | — | Whether the product requires continuous cold chain storage and transport | Yes (Refrigerated), Yes (Frozen), Yes (Ultra-Cold) |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus WHO prequalification standards and EMA vaccine guidelines | [WHO Prequalification - BCG Vaccine](https://extranet.who.int/prequal/vaccines/p/bcg-vaccine-1), [VaccineShoppe](https://www.vaccineshoppe.com/Product-Catalog/c/1), [Prevnar 20 Prescribing Information](https://labeling.pfizer.com/ShowLabeling.aspx?id=15010), [Sanofi Vaccine Products](https://www.sanofi.us/en/your-health/products/vaccine-products) |
