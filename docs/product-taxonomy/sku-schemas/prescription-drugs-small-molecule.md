# SKU Schema: Prescription Drugs (Small Molecule)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.prescription_drugs`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer, wholesaler, or pharmacy product identifier | MCK-4901234, ABC12345, 0003-0894-31 |
| Product Name | text | Full product name including brand or generic name, strength, and dosage form | Eliquis 5 mg Film-Coated Tablets, Metformin HCl ER 500 mg Tablets, Atorvastatin Calcium 20 mg Tablets |
| URL | text | Direct link to the product page | https://example.com/product/eliquis-5mg-tablets |
| Price | number | Numeric price per unit or per package excluding currency symbol | 12.50, 549.99, 0.85 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, JPY |
| Dosage Form | text | Physical form of the drug product | Tablet Film Coated, Capsule, Extended-Release Tablet, Solution, Injection |
| Therapeutic Class | text | Pharmacologic or therapeutic category of the drug | Anticoagulant, HMG-CoA Reductase Inhibitor, Biguanide, SSRI |
| Marketing Category | text | Regulatory approval pathway under which the product is marketed | NDA, ANDA, NDA Authorized Generic, OTC Monograph |
| Package Type | text | Container closure system used for the drug product | Bottle, Blister Pack, Vial, Ampule, Prefilled Syringe |
| Active Ingredient | text | Chemical substance responsible for the therapeutic effect | apixaban, atorvastatin calcium trihydrate, metformin hydrochloride |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Inactive Ingredients | text (list) | Excipients included in the formulation | Microcrystalline Cellulose, Lactose Monohydrate, Croscarmellose Sodium, Magnesium Stearate |
| Product Type | enum | Regulatory classification of the product | Human Prescription Drug, Human OTC Drug |
| Country of Origin | text | Country where the finished dosage form is manufactured | USA, India, Ireland, Israel, Germany |
| NDC | text | National Drug Code — 3-segment identifier for labeler, product, and package | 0003-0894-31, 0591-2411-30, 59651-606-90 |
| Brand Name | text | Proprietary or trade name of the drug product | Eliquis, Lipitor, Glucophage, Zoloft |
| Generic Name | text | International nonproprietary name (INN) or United States adopted name (USAN) of the active ingredient | apixaban, atorvastatin calcium, metformin hydrochloride, sertraline hydrochloride |
| Manufacturer | text | Name of the labeler, manufacturer, or marketing authorization holder | Bristol-Myers Squibb, Pfizer, Teva Pharmaceuticals, Aurobindo Pharma |
| Strength | text | Amount of active ingredient per dosage unit | 5 mg, 500 mg, 10 mg/mL, 20 mg/5 mL |
| Route of Administration | text | Method by which the drug is delivered to the body | Oral, Intravenous, Intramuscular, Subcutaneous, Topical, Transdermal |
| ATC Code | text | WHO Anatomical Therapeutic Chemical classification code | B01AF02, C10AA05, A10BA02, N06AB06 |
| DEA Schedule | text | US Drug Enforcement Administration controlled substance schedule, if applicable | Schedule II, Schedule III, Schedule IV, Not Scheduled |
| NDA/ANDA Number | text | FDA New Drug Application or Abbreviated New Drug Application number | NDA 202155, ANDA 091438, NDA 021071 |
| Reference Listed Drug | text | Brand-name product to which a generic is compared for bioequivalence, if applicable | Lipitor, Glucophage XR, Eliquis |
| UPC | text | Universal Product Code barcode for retail identification | 300650482036, 378395277 |
| Tablet/Capsule Description | text | Physical appearance including shape, color, size, and imprint | Pink oval film-coated tablet debossed 894 and 5, White round tablet scored on one side |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus IDMP/ISO 11615 and FDA NDC standards | [DailyMed](https://dailymed.nlm.nih.gov/), [NDCList - Atorvastatin](https://ndclist.com/ndc/72205-024), [FDA Orange Book](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files), [Drugs.com - Eliquis](https://www.drugs.com/pro/eliquis.html) |
