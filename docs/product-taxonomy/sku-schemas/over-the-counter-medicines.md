# SKU Schema: Over-the-Counter Medicines

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.otc_medicines`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or distributor product identifier | CVS-449-05, WMT-8834210, AMZ-B00HSA0SRO |
| Product Name | product_name | text | Full product name including brand, variant, strength, and dosage form | Tylenol Extra Strength 500 mg Caplets, Advil Liqui-Gels 200 mg, CVS Health Maximum Strength Antacid Chewable Tablets |
| URL | url | text | Direct link to the product page | https://example.com/product/tylenol-extra-strength-500mg |
| Price | price | number | Numeric price per unit or per package excluding currency symbol | 9.99, 14.49, 5.79 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Active Ingredient | active_ingredient | text (list) | Therapeutic substance(s) and amount per dosage unit | Acetaminophen 500 mg, Ibuprofen 200 mg, Diphenhydramine HCl 25 mg, Guaifenesin 400 mg |
| Dosage Form | dosage_form | text | Physical form of the OTC product | Tablet, Caplet, Capsule, Liquid-Filled Capsule, Chewable Tablet, Oral Suspension, Cream, Ointment, Gel, Suppository, Patch |
| Indication Category | indication_category | text | Primary symptom or condition the product is intended to treat | Pain and Fever, Allergy, Cold and Flu, Digestive Health, Skin Care, Sleep Aid |
| Inactive Ingredients | inactive_ingredients | text (list) | Non-therapeutic excipients in the formulation | Microcrystalline Cellulose, Starch, Povidone, Stearic Acid, FD&C Red No. 40 |
| Package Type | package_type | text | Container closure system | Bottle, Blister Pack, Box, Tube, Jar, Sachet, Squeeze Bottle |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Product Form Modifier | product_form_modifier | text | Additional description of the dosage form variant | Regular Strength, Extra Strength, Maximum Strength, Rapid Release, Extended Release, PM |
| Country of Origin | country_of_origin | text | Country where the finished product is manufactured | USA, Canada, India, Germany, UK |
| OTC Monograph Category | otc_monograph_category | text | FDA OTC drug monograph under which the product is marketed | Analgesic, Antihistamine, Antacid, Cough Suppressant, External Analgesic |
| NDC | ndc | text | National Drug Code — 3-segment identifier for labeler, product, and package | 50580-449-05, 00573-0150-40, 62011-0201-01 |
| Brand Name | brand_name | text | Proprietary or store brand name | Tylenol, Advil, Benadryl, CVS Health, Equate, Up and Up |
| Manufacturer | manufacturer | text | Name of the labeler, manufacturer, or distributor | Johnson and Johnson, Pfizer Consumer Healthcare, Procter and Gamble, Bayer, Reckitt Benckiser |
| Purpose | purpose | text (list) | Pharmacologic category or action of each active ingredient as required on Drug Facts label | Pain Reliever/Fever Reducer, Antihistamine, Cough Suppressant, Nasal Decongestant |
| Strength | strength | text | Amount of active ingredient per dosage unit or per defined measure | 500 mg, 200 mg/5 mL, 10 mg/mL, 1%, 2.5 mg |
| Route of Administration | route_of_administration | text | Method by which the medicine is applied or taken | Oral, Topical, Rectal, Nasal, Ophthalmic |
| Uses | uses | text (list) | Specific symptoms or conditions listed on the Drug Facts label | Temporarily relieves minor aches and pains, Reduces fever, Relieves runny nose and sneezing |
| Age Group | age_group | text | Target age range for the product | Adults and Children 12 Years and Over, Children 2-11 Years, Adults 18 and Over |
| Directions | directions | text | Dosage instructions including amount, frequency, and duration | Take 2 caplets every 6 hours while symptoms last, Do not take more than 6 caplets in 24 hours |
| UPC | upc | text | Universal Product Code barcode for retail scanning | 300450449054, 305730150400 |
| Flavor | flavor | text | Added flavor for palatability, especially in liquid and chewable forms | Cherry, Grape, Berry, Mint, Unflavored |
| Storage Conditions | storage_conditions | text | Required storage temperature and handling instructions | Store at 20-25C (68-77F), Protect From Moisture, Keep From Freezing |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus FDA Drug Facts label requirements (21 CFR 201.66) | [FDA OTC Drug Facts Label](https://www.fda.gov/drugs/understanding-over-counter-medicines/over-counter-drug-facts-label), [DailyMed - Tylenol Regular Strength](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1622f694-4d63-4c56-8737-fae31f0ecfb7), [CVS OTC Products via Drugs.com](https://www.drugs.com/otc/763802/cvs-triple-antibiotic.html), [USP OTC Standards](https://www.usp.org/small-molecules/otc-standards) |
