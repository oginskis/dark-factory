# SKU Schema: Biologics & Biosimilars

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.biologics_biosimilars`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer, wholesaler, or specialty pharmacy product identifier | PFZ-BIO-4012, ABI-HUM-40, SPH-RIT-100 |
| Product Name | text | Full product name including brand name, active substance, strength, and presentation | Humira 40 mg/0.4 mL Prefilled Syringe, Avastin 400 mg/16 mL Injection, Hadlima 40 mg/0.8 mL Pen |
| URL | text | Direct link to the product page | https://example.com/product/humira-40mg-syringe |
| Price | number | Numeric price per unit or per package excluding currency symbol | 1289.00, 6780.50, 450.25 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, JPY |
| Product Category | enum | Whether the product is an originator biologic, biosimilar, or interchangeable biosimilar | Originator Biologic, Biosimilar, Interchangeable Biosimilar |
| Dosage Form | text | Physical form of the biologic product | Solution for Injection, Lyophilized Powder for Reconstitution, Concentrate for Solution for Infusion |
| Molecule Type | text | Class of biologic molecule | Monoclonal Antibody (IgG1), Fusion Protein, Recombinant Protein, Antibody-Drug Conjugate |
| Country of Origin | text | Country where the finished product is manufactured | USA, Ireland, South Korea, Switzerland, Germany |
| Molecular Weight | number (kDa) | Approximate molecular weight of the biologic molecule | 148, 149, 145, 150 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| NDC | text | National Drug Code — 3-segment identifier for labeler, product, and package | 0074-3799-02, 50242-060-01, 61755-006-01 |
| Brand Name | text | Proprietary or trade name of the biologic or biosimilar product | Humira, Avastin, Herceptin, Hadlima, Zirabev, Mvasi |
| INN | text | International nonproprietary name of the active biologic substance including any suffix for biosimilars | adalimumab, bevacizumab, trastuzumab, adalimumab-bwwd, bevacizumab-awwb |
| Manufacturer | text | Name of the biologic license holder or marketing authorization holder | AbbVie, Roche/Genentech, Pfizer, Samsung Bioepis, Amgen |
| Reference Product | text | Name of the originator biologic to which a biosimilar is compared, if applicable | Humira, Avastin, Herceptin, Remicade |
| BLA Number | text | FDA Biologics License Application number | BLA 125057, BLA 125085, BLA 761024 |
| Strength | text | Concentration or amount of active substance per unit | 40 mg/0.8 mL, 100 mg/4 mL, 440 mg/20 mL, 150 mg Lyophilized Powder |
| Route of Administration | text | Method by which the biologic is delivered | Subcutaneous, Intravenous Infusion, Intravitreal, Intramuscular |
| Presentation | text | Delivery device or container type | Prefilled Syringe, Prefilled Pen, Single-Dose Vial, Multi-Dose Vial, Autoinjector |
| Mechanism of Action | text | Primary pharmacological mechanism of the biologic | TNF-alpha Inhibitor, VEGF Inhibitor, HER2 Receptor Antagonist, CD20-directed Cytolytic Antibody |
| Therapeutic Area | text (list) | Disease areas or conditions the product is approved to treat | Rheumatoid Arthritis, Colorectal Cancer, Breast Cancer, Plaque Psoriasis, Crohns Disease |
| Storage Conditions | text | Required storage temperature and handling instructions | Refrigerate 2-8C, Do Not Freeze, Protect From Light |
| Shelf Life | number (months) | Duration the product retains acceptable quality from date of manufacture | 18, 24, 36 |
| Package Contents | text | Description of what is included in one commercial package | 2 Prefilled Syringes of 40 mg/0.8 mL, 1 Single-Dose Vial of 100 mg/4 mL |
| Adjuvant/Excipients | text (list) | Key excipients and stabilizers in the formulation | Polysorbate 80, Mannitol, Sodium Chloride, Sucrose, Histidine, Trehalose Dihydrate |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus FDA Purple Book and IDMP standards | [FDA Biosimilar Product Information](https://www.fda.gov/drugs/biosimilars/biosimilar-product-information), [Pfizer Biosimilars](https://www.pfizerbiosimilars.com/), [Humira Prescribing Information](https://www.rxabbvie.com/pdf/humira.pdf), [EMA Humira SmPC](https://www.medicines.org.uk/emc/product/9080/smpc) |
