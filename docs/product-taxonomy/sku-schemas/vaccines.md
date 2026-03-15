# SKU Schema: Vaccines

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Distributor or pharmacy product identifier | VSH-PFZ-PCV20, CDC-FLU-QIV, MCK-VAX-0045 |
| Product Name | text | Full product name including brand name, valency, and target disease | Prevnar 20 Pneumococcal 20-Valent Conjugate Vaccine, Fluzone High-Dose Quadrivalent, Shingrix Recombinant Adjuvanted Vaccine |
| URL | text | Direct link to the product page | https://example.com/product/prevnar-20 |
| Price | number | Numeric price per dose or per package excluding currency symbol | 269.00, 80.75, 195.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, JPY |
| Brand Name | text | Proprietary trade name of the vaccine | Prevnar 20, Fluzone, Shingrix, Gardasil 9, MMR-II, Vaxelis |
| Manufacturer | text | Name of the vaccine manufacturer or marketing authorization holder | Pfizer, Sanofi Pasteur, GlaxoSmithKline, Merck, Moderna, Serum Institute of India |
| Disease Target | text (list) | Disease(s) or pathogen(s) the vaccine protects against | Pneumococcal Disease, Influenza, Herpes Zoster, HPV, Measles Mumps Rubella, COVID-19 |
| Vaccine Type | text | Technology or platform used to produce the vaccine | Conjugate, Inactivated, Live Attenuated, mRNA, Recombinant Protein, Toxoid, Viral Vector |
| Antigen Composition | text | Description of the antigenic components and their quantities per dose | 20 pneumococcal polysaccharide serotypes conjugated to CRM197 carrier protein, 15 mcg HA per strain |
| Valency | text | Number of serotypes or strains covered by the vaccine | Monovalent, 4-Valent, 9-Valent, 13-Valent, 20-Valent, 23-Valent |
| Adjuvant | text | Immune-enhancing substance included in the formulation | Aluminum Phosphate, AS01B, AS04, MF59, None |
| Preservative | text | Antimicrobial preservative included in multi-dose formulations | Thimerosal, 2-Phenoxyethanol, None (Preservative Free) |
| Dosage Form | text | Physical form of the vaccine product | Suspension for Injection, Lyophilized Powder for Reconstitution, Solution for Injection, Emulsion for Injection |
| Dose Volume | number (mL) | Volume of a single dose | 0.5, 0.25, 1.0 |
| Route of Administration | text | Method by which the vaccine is delivered | Intramuscular, Subcutaneous, Intradermal, Oral, Intranasal |
| Presentation | text | Container type and configuration | Prefilled Syringe, Single-Dose Vial, Multi-Dose Vial, Nasal Spray |
| Doses Per Container | number | Number of doses contained in a single vial or device | 1, 5, 10, 20 |
| Approved Age Group | text | Age range for which the vaccine is approved or recommended | 6 Weeks and Older, 2 Months Through 17 Years, 50 Years and Older, 12 Years and Older |
| Schedule | text | Recommended dosing schedule (number of doses and intervals) | Single Dose, 2 Doses 2-6 Months Apart, 3 Doses at 0-1-6 Months, Annual |
| NDC | text | National Drug Code for US market identification | 00005-1971-05, 49281-0718-50, 58160-0823-52 |
| Storage Temperature | text | Required storage temperature range | 2-8C (36-46F), -25 to -15C, -80 to -60C |
| Cold Chain Required | enum | Whether the product requires continuous cold chain storage and transport | Yes (Refrigerated), Yes (Frozen), Yes (Ultra-Cold) |
| Shelf Life | number (months) | Duration the product retains acceptable potency from date of manufacture | 12, 18, 24, 36 |
| Diluent | text | Reconstitution fluid supplied with lyophilized vaccines | 0.9% Sodium Chloride, Sterile Water for Injection, AS01B Adjuvant Suspension, None (Ready to Use) |
| Vaccine Vial Monitor | text | Type of VVM indicator on the vial label for temperature exposure monitoring, primarily for WHO-prequalified products | VVM Type 7, VVM Type 14, VVM Type 30, Not Applicable |
| Package Size | text | Number of doses or units per commercial package | 10 Prefilled Syringes, 10 Single-Dose Vials, 1 Carton of 50 Vials |
| Excipients | text (list) | Non-antigenic components in the formulation | Polysorbate 80, Sodium Chloride, Aluminum Phosphate, Sucrose, Histidine |
| Country of Origin | text | Country where the finished vaccine is manufactured | USA, Belgium, France, India, UK, Germany |
| WHO Prequalification | enum | Whether the vaccine holds WHO prequalification status | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus WHO prequalification standards and EMA vaccine guidelines | [WHO Prequalification - BCG Vaccine](https://extranet.who.int/prequal/vaccines/p/bcg-vaccine-1), [VaccineShoppe](https://www.vaccineshoppe.com/Product-Catalog/c/1), [Prevnar 20 Prescribing Information](https://labeling.pfizer.com/ShowLabeling.aspx?id=15010), [Sanofi Vaccine Products](https://www.sanofi.us/en/your-health/products/vaccine-products) |
