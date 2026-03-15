# SKU Schema: Biologics & Biosimilars

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.biologics_biosimilars`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer, wholesaler, or specialty pharmacy product identifier | PFZ-BIO-4012, ABI-HUM-40, SPH-RIT-100 |
| Product Name | product_name | text | Full product name including brand name, active substance, strength, and presentation | Humira 40 mg/0.4 mL Prefilled Syringe, Avastin 400 mg/16 mL Injection, Hadlima 40 mg/0.8 mL Pen |
| URL | url | text | Direct link to the product page | https://example.com/product/humira-40mg-syringe |
| Price | price | number | Numeric price per unit or per package excluding currency symbol | 1289.00, 6780.50, 450.25 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CHF, JPY |
| Product Category | product_category | enum | Whether the product is an originator biologic, biosimilar, or interchangeable biosimilar | Originator Biologic, Biosimilar, Interchangeable Biosimilar |
| Dosage Form | dosage_form | text | Physical form of the biologic product | Solution for Injection, Lyophilized Powder for Reconstitution, Concentrate for Solution for Infusion |
| Molecule Type | molecule_type | text | Class of biologic molecule | Monoclonal Antibody (IgG1), Fusion Protein, Recombinant Protein, Antibody-Drug Conjugate |
| Country of Origin | country_of_origin | text | Country where the finished product is manufactured | USA, Ireland, South Korea, Switzerland, Germany |
| Molecular Weight | molecular_weight | number (kDa) | Approximate molecular weight of the biologic molecule | 148, 149, 145, 150 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| NDC | ndc | text | National Drug Code — 3-segment identifier for labeler, product, and package | 0074-3799-02, 50242-060-01, 61755-006-01 |
| Brand Name | brand_name | text | Proprietary or trade name of the biologic or biosimilar product | Humira, Avastin, Herceptin, Hadlima, Zirabev, Mvasi |
| INN | inn | text | International nonproprietary name of the active biologic substance including any suffix for biosimilars | adalimumab, bevacizumab, trastuzumab, adalimumab-bwwd, bevacizumab-awwb |
| Manufacturer | manufacturer | text | Name of the biologic license holder or marketing authorization holder | AbbVie, Roche/Genentech, Pfizer, Samsung Bioepis, Amgen |
| Reference Product | reference_product | text | Name of the originator biologic to which a biosimilar is compared, if applicable | Humira, Avastin, Herceptin, Remicade |
| BLA Number | bla_number | text | FDA Biologics License Application number | BLA 125057, BLA 125085, BLA 761024 |
| Strength | strength | text | Concentration or amount of active substance per unit | 40 mg/0.8 mL, 100 mg/4 mL, 440 mg/20 mL, 150 mg Lyophilized Powder |
| Route of Administration | route_of_administration | text | Method by which the biologic is delivered | Subcutaneous, Intravenous Infusion, Intravitreal, Intramuscular |
| Presentation | presentation | text | Delivery device or container type | Prefilled Syringe, Prefilled Pen, Single-Dose Vial, Multi-Dose Vial, Autoinjector |
| Mechanism of Action | mechanism_of_action | text | Primary pharmacological mechanism of the biologic | TNF-alpha Inhibitor, VEGF Inhibitor, HER2 Receptor Antagonist, CD20-directed Cytolytic Antibody |
| Therapeutic Area | therapeutic_area | text (list) | Disease areas or conditions the product is approved to treat | Rheumatoid Arthritis, Colorectal Cancer, Breast Cancer, Plaque Psoriasis, Crohns Disease |
| Storage Conditions | storage_conditions | text | Required storage temperature and handling instructions | Refrigerate 2-8C, Do Not Freeze, Protect From Light |
| Shelf Life | shelf_life | number (months) | Duration the product retains acceptable quality from date of manufacture | 18, 24, 36 |
| Package Contents | package_contents | text | Description of what is included in one commercial package | 2 Prefilled Syringes of 40 mg/0.8 mL, 1 Single-Dose Vial of 100 mg/4 mL |
| Adjuvant/Excipients | adjuvantexcipients | text (list) | Key excipients and stabilizers in the formulation | Polysorbate 80, Mannitol, Sodium Chloride, Sucrose, Histidine, Trehalose Dihydrate |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus FDA Purple Book and IDMP standards | [FDA Biosimilar Product Information](https://www.fda.gov/drugs/biosimilars/biosimilar-product-information), [Pfizer Biosimilars](https://www.pfizerbiosimilars.com/), [Humira Prescribing Information](https://www.rxabbvie.com/pdf/humira.pdf), [EMA Humira SmPC](https://www.medicines.org.uk/emc/product/9080/smpc) |
