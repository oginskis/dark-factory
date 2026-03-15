# SKU Schema: Active Pharmaceutical Ingredients

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.active_pharma_ingredients`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or manufacturer catalog identifier | B0005-464900, API-1234, DR-ABR-001 |
| Product Name | text | International Non-proprietary Name (INN) or common chemical name of the API | Abiraterone Acetate, Metformin Hydrochloride, Ibuprofen |
| URL | text | Direct link to the product page | https://example.com/api/abiraterone-acetate |
| Price | number | Numeric price per unit of sale (per kg, per g, or per pack), excluding currency symbol | 245.00, 1200.00, 38.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, INR, CNY, GBP |
| Molecular Formula | text | Chemical formula expressing the number and type of atoms | C26H33NO2, C4H11N5.HCl, C13H18O2 |
| Therapeutic Category | text | Primary therapeutic or pharmacological classification | Anti-Cancer/Oncology, Antidiabetic, Anti-Inflammatory, Cardiovascular, CNS |
| Pharmacological Class | text | Mechanism-based classification of the API | CYP17 Inhibitor, Biguanide, COX Inhibitor, ACE Inhibitor |
| DMF Type | enum | Type of Drug Master File | Type II, Type III, Type IV, Type V |
| Pharmacopoeial Grade | text (list) | Pharmacopoeia monograph compliance | USP, EP, BP, JP, IP, ChP |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Physical Form | text | Macroscopic appearance and form of the bulk API | White crystalline powder, Off-white granules, Pale yellow amorphous solid |
| Polymorphic Form | text | Crystal form designation when polymorphism is relevant | Form I, Form A, Amorphous, Anhydrous |
| Country of Origin | text | Country where the API is manufactured | India, China, Italy, USA, Spain |
| Dosage Form Suitability | text (list) | Dosage forms the API grade is intended to support | Oral Solid, Injectable, Topical, Ophthalmic, Inhalation |
| CAS Number | text | Chemical Abstracts Service registry number uniquely identifying the substance | 154229-19-3, 1115-70-4, 15687-27-1 |
| UNII | text | FDA Unique Ingredient Identifier code | G819A456D0, 9100L32L2N, WK2XYI10QM |
| DMF Number | text | US Drug Master File number filed with the FDA | DMF 12345, DMF 29876 |
| Regulatory Status | text (list) | Regulatory filings and approvals held by the manufacturer | US DMF, CEP/COS, WHO Prequalification, KDMF, JDMF |
| GMP Compliance | text (list) | Good Manufacturing Practice certifications held by the manufacturing site | US FDA, EU GMP, WHO GMP, PMDA, TGA |
| Purity | text | Assay value or purity specification as stated by the supplier | >=99.0%, 98.0-102.0%, NLT 99.5% |
| Solubility | text | Key solubility characteristics in common solvents | Freely soluble in methanol, Slightly soluble in water, Sparingly soluble in ethanol |
| Melting Point | text (C) | Melting point or melting range in degrees Celsius | 219-223, 148-152, 75-78 |
| Residual Solvents | text | Residual solvent limits per ICH Q3C guideline | Meets ICH Q3C Class 2 limits, Acetone NMT 5000 ppm |
| Heavy Metals | text | Heavy metal content specification | NMT 10 ppm, Meets USP 233 |
| Impurity Profile | text | Total and specified impurity limits | Total impurities NMT 0.5%, Any single impurity NMT 0.10% |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ICH Q7, USP, EP monographs, WHO Prequalification) | [Dr. Reddys API](https://api.drreddys.com/product), [LGM Pharma](https://lgmpharma.com/api-products/), [BOC Sciences](https://www.bocsci.com/apis-list-46.html), [PharmaCompass](https://www.pharmacompass.com/active-pharmaceutical-ingredients/octoxynol) |
