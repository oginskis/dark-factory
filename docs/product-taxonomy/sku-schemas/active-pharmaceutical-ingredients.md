# SKU Schema: Active Pharmaceutical Ingredients

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or manufacturer catalog identifier | B0005-464900, API-1234, DR-ABR-001 |
| Product Name | text | International Non-proprietary Name (INN) or common chemical name of the API | Abiraterone Acetate, Metformin Hydrochloride, Ibuprofen |
| URL | text | Direct link to the product page | https://example.com/api/abiraterone-acetate |
| Price | number | Numeric price per unit of sale (per kg, per g, or per pack), excluding currency symbol | 245.00, 1200.00, 38.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, INR, CNY, GBP |
| CAS Number | text | Chemical Abstracts Service registry number uniquely identifying the substance | 154229-19-3, 1115-70-4, 15687-27-1 |
| Molecular Formula | text | Chemical formula expressing the number and type of atoms | C26H33NO2, C4H11N5.HCl, C13H18O2 |
| Molecular Weight | number (g/mol) | Molecular weight in grams per mole | 391.55, 165.62, 206.28 |
| UNII | text | FDA Unique Ingredient Identifier code | G819A456D0, 9100L32L2N, WK2XYI10QM |
| Therapeutic Category | text | Primary therapeutic or pharmacological classification | Anti-Cancer/Oncology, Antidiabetic, Anti-Inflammatory, Cardiovascular, CNS |
| Pharmacological Class | text | Mechanism-based classification of the API | CYP17 Inhibitor, Biguanide, COX Inhibitor, ACE Inhibitor |
| DMF Number | text | US Drug Master File number filed with the FDA | DMF 12345, DMF 29876 |
| DMF Type | enum | Type of Drug Master File | Type II, Type III, Type IV, Type V |
| Regulatory Status | text (list) | Regulatory filings and approvals held by the manufacturer | US DMF, CEP/COS, WHO Prequalification, KDMF, JDMF |
| GMP Compliance | text (list) | Good Manufacturing Practice certifications held by the manufacturing site | US FDA, EU GMP, WHO GMP, PMDA, TGA |
| Pharmacopoeial Grade | text (list) | Pharmacopoeia monograph compliance | USP, EP, BP, JP, IP, ChP |
| Physical Form | text | Macroscopic appearance and form of the bulk API | White crystalline powder, Off-white granules, Pale yellow amorphous solid |
| Purity | text | Assay value or purity specification as stated by the supplier | >=99.0%, 98.0-102.0%, NLT 99.5% |
| Particle Size | text | Particle size distribution specification, typically D50 or sieve fraction | D50 10-50 um, NMT 100 mesh, 20-80 um |
| Polymorphic Form | text | Crystal form designation when polymorphism is relevant | Form I, Form A, Amorphous, Anhydrous |
| Solubility | text | Key solubility characteristics in common solvents | Freely soluble in methanol, Slightly soluble in water, Sparingly soluble in ethanol |
| Melting Point | text (C) | Melting point or melting range in degrees Celsius | 219-223, 148-152, 75-78 |
| Residual Solvents | text | Residual solvent limits per ICH Q3C guideline | Meets ICH Q3C Class 2 limits, Acetone NMT 5000 ppm |
| Heavy Metals | text | Heavy metal content specification | NMT 10 ppm, Meets USP 233 |
| Impurity Profile | text | Total and specified impurity limits | Total impurities NMT 0.5%, Any single impurity NMT 0.10% |
| Storage Conditions | text | Recommended storage temperature, humidity, and light conditions | 2-8C protected from light, 15-25C in a dry place, Below 30C |
| Shelf Life | text | Retest or expiry period from date of manufacture | 36 months, 24 months, Retest 2 years |
| Packaging | text | Primary packaging configuration and material | 25 kg HDPE drums with double PE liner, 5 kg aluminum bag, 1 kg glass bottle |
| Pack Size | text | Available quantity per unit of sale | 1 kg, 5 kg, 25 kg, 50 kg, 100 kg |
| Country of Origin | text | Country where the API is manufactured | India, China, Italy, USA, Spain |
| Manufacturer | text | Name of the API manufacturing company | Dr. Reddys Laboratories, Teva API, BASF Pharma, Divi's Laboratories |
| CEP/COS Number | text | European Certificate of Suitability of Monographs number | R0-CEP 2019-123-Rev 01 |
| Sterility | enum | Whether the API is supplied in sterile form | Sterile, Non-Sterile |
| Endotoxin Level | text | Bacterial endotoxin specification for injectable-grade APIs | NMT 0.25 EU/mg, NMT 10 EU/g |
| Dosage Form Suitability | text (list) | Dosage forms the API grade is intended to support | Oral Solid, Injectable, Topical, Ophthalmic, Inhalation |
| Chiral Purity | text | Enantiomeric excess or optical rotation specification | >=99.5% ee, Specific rotation -33 to -36 degrees |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ICH Q7, USP, EP monographs, WHO Prequalification) | [Dr. Reddys API](https://api.drreddys.com/product), [LGM Pharma](https://lgmpharma.com/api-products/), [BOC Sciences](https://www.bocsci.com/apis-list-46.html), [PharmaCompass](https://www.pharmacompass.com/active-pharmaceutical-ingredients/octoxynol) |
