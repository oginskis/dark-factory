# SKU Schema: Veterinary Pharmaceuticals

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Distributor, veterinary supplier, or manufacturer product identifier | ZTS-APQ-16, MRK-NUF-250, ELN-GAL-INJ |
| Product Name | text | Full product name including brand, active ingredient, strength, and dosage form | Apoquel 16 mg Film-Coated Tablets for Dogs, Nuflor 300 mg/mL Solution for Injection, Drontal Plus Taste Tablets for Dogs |
| URL | text | Direct link to the product page | https://example.com/product/apoquel-16mg-tablets |
| Price | number | Numeric price per unit or per package excluding currency symbol | 2.85, 125.00, 45.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand Name | text | Proprietary trade name of the veterinary drug | Apoquel, Nuflor, Drontal, Rimadyl, Convenia, Cytopoint |
| Generic Name | text | International nonproprietary name of the active substance | oclacitinib maleate, florfenicol, praziquantel/pyrantel/febantel, carprofen |
| Manufacturer | text | Name of the marketing authorization holder or manufacturer | Zoetis, Merck Animal Health, Elanco, Dechra, Boehringer Ingelheim, Vetoquinol |
| Target Species | text (list) | Animal species for which the product is approved | Dogs, Cats, Cattle, Horses, Swine, Sheep, Poultry, Goats |
| Dosage Form | text | Physical form of the veterinary product | Tablet, Film-Coated Tablet, Injectable Solution, Oral Suspension, Paste, Topical Spot-On, Bolus, Intramammary Syringe, Pour-On, Premix |
| Strength | text | Amount of active ingredient per dosage unit or per defined volume | 16 mg, 300 mg/mL, 50 mg/mL, 5%, 10 mg/kg |
| Route of Administration | text | Method by which the drug is delivered to the animal | Oral, Subcutaneous Injection, Intramuscular Injection, Intravenous, Topical, Pour-On, Intramammary, In-Feed |
| Indication | text (list) | Diseases, conditions, or parasites the product is approved to treat or prevent | Atopic Dermatitis, Bovine Respiratory Disease, Gastrointestinal Nematodes, Mastitis, Pain and Inflammation |
| Therapeutic Class | text | Pharmacologic or therapeutic category | Janus Kinase Inhibitor, Antimicrobial, Anthelmintic, NSAID, Antiparasitic, Corticosteroid |
| NADA/ANADA Number | text | FDA New Animal Drug Application or Abbreviated New Animal Drug Application number | NADA 141-345, ANADA 200-597, NADA 141-230 |
| Regulatory Status | enum | Prescription or dispensing classification of the veterinary product | Veterinary Prescription (Rx), OTC, Veterinary Feed Directive (VFD) |
| Withdrawal Period | text | Mandatory time between last dose and slaughter or milk collection for food-producing animals | Meat 28 days, Milk 36 hours, Eggs 0 days, Not Applicable (Companion Animal) |
| Controlled Substance Schedule | text | DEA schedule classification if the product contains controlled substances | Schedule II, Schedule III, Schedule IV, Not Scheduled |
| Package Size | text | Quantity of dosage units or volume per commercial package | 100 Tablets, 250 mL Vial, 20 mL Tube, 6 Intramammary Syringes, 1 L Bottle |
| Package Type | text | Container closure system | Bottle, Vial, Tube, Blister Pack, Sachet, Intramammary Syringe, Pour-On Container |
| NDC | text | National Drug Code for US market identification | 54771-6494-1, 00061-0850-01, 58198-4301-3 |
| Active Ingredient | text (list) | Chemical substance(s) responsible for the therapeutic effect | Oclacitinib Maleate, Florfenicol, Praziquantel and Pyrantel Pamoate and Febantel |
| Inactive Ingredients | text (list) | Excipients included in the formulation | Microcrystalline Cellulose, Polyethylene Glycol, Propylene Glycol, Artificial Beef Flavor |
| Animal Weight Range | text | Body weight range for which the dosage is intended | Dogs 6.1-9.0 kg, Cattle over 100 kg, Horses 250-600 kg |
| Storage Conditions | text | Required storage temperature and handling instructions | Store below 25C, Refrigerate 2-8C, Store in Original Container, Protect From Light |
| Shelf Life | number (months) | Duration the product retains acceptable quality from date of manufacture | 24, 36, 48 |
| Country of Origin | text | Country where the finished product is manufactured | USA, UK, Belgium, France, India, Australia |
| GMP Compliance | text | Manufacturing quality certification applicable to the production facility | FDA cGMP, EU GMP, WHO GMP |
| Palatability | text | Flavor or palatability features to aid voluntary administration | Beef Flavored, Liver Flavored, Unflavored, Taste Tab |
| Contraindicated Species | text (list) | Animal species for which the product must not be used | Cats, Horses, Animals Intended For Food Production, Breeding Animals |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus FDA Green Book and USP veterinary monograph standards | [Zoetis Products](https://www.zoetis.com/products-and-science/products/all-products), [Merck Animal Health USA](https://www.merck-animal-health-usa.com/products/), [FDA Green Book](https://www.fda.gov/animal-veterinary/products/approved-animal-drug-products-green-book), [Drugs.com Veterinary](https://www.drugs.com/vet/) |
