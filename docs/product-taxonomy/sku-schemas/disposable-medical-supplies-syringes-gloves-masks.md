# SKU Schema: Disposable Medical Supplies (Syringes, Gloves, Masks)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.disposable_medical_supplies`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor catalog number | 309589, FG3001, 1500PF-L, N95-1860 |
| Product Name | product_name | text | Full product name including type, material, and size | BD 3 mL Luer-Lok Syringe with 23G x 1-1/2 in Needle, Medline FitGuard Nitrile Exam Gloves Large, 3M 1860 N95 Surgical Respirator |
| URL | url | text | Direct link to the product page | https://example.com/product/bd-syringe-309589 |
| Price | price | number | Price per box or case as listed | 6.50, 12.99, 45.00, 125.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary disposable supply category | Syringe, Hypodermic Needle, Exam Glove, Surgical Glove, Face Mask, N95 Respirator, Surgical Gown, Drape, IV Catheter, Wound Dressing, Suture |
| Material | material | text | Primary material composition | Nitrile, Latex, Vinyl, Polypropylene, Polyethylene, Neoprene, Silicone |
| Tip Type | tip_type | enum | Syringe tip connection style | Luer-Lok, Luer Slip, Catheter Tip, Eccentric Tip |
| Mask Type | mask_type | enum | Face covering classification | Surgical Mask (ASTM Level 1/2/3), N95 Respirator, KN95, Procedure Mask |
| Regulatory Classification | regulatory_classification | text | Medical device regulatory class | FDA Class I, FDA Class II, CE Class I, CE Class IIa |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Syringe Volume | syringe_volume | number (mL) | Nominal syringe fill capacity | 1, 3, 5, 10, 20, 30, 60 |
| Needle Gauge | needle_gauge | text (G) | Needle outer diameter gauge number (higher number = thinner needle) | 18G, 20G, 21G, 22G, 23G, 25G, 27G, 30G |
| Needle Included | needle_included | enum | Whether a needle is pre-attached to the syringe | Yes (Attached), No (Syringe Only) |
| Glove Thickness (Finger) | glove_thickness_finger | number (mil) | Finger thickness measurement in thousandths of an inch | 3.1, 4.0, 5.5, 6.0, 8.0 |
| Glove Thickness (Palm) | glove_thickness_palm | number (mil) | Palm thickness measurement in thousandths of an inch | 2.4, 3.0, 4.0, 5.0 |
| Cuff Style | cuff_style | enum | Glove cuff design | Beaded, Extended, Rolled |
| Texture | texture | enum | Surface texture pattern for grip | Textured Fingertips, Fully Textured, Smooth, Micro-Textured |
| Powder Status | powder_status | enum | Whether the product contains glove powder | Powder-Free, Powdered |
| Sterility | sterility | enum | Sterile or non-sterile designation | Sterile, Non-Sterile |
| Filtration Level | filtration_level | text | Bacterial or particulate filtration efficiency | BFE greater than 98%, PFE greater than 95%, NIOSH N95 (95% filtration) |
| AQL | aql | number | Acceptable Quality Level (defects per 100 units per ASTM D5151) | 0.65, 1.0, 1.5, 2.5 |
| Chemo Tested | chemo_tested | enum | Whether the product is tested for chemotherapy drug permeation per ASTM D6978 | Yes, No |
| Latex Free | latex_free | enum | Whether the product is free of natural rubber latex | Yes, No |
| Units per Box | units_per_box | number | Number of individual items per inner box | 50, 100, 200, 250 |
| Boxes per Case | boxes_per_case | number | Number of boxes per shipping case | 4, 10, 12, 20 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus ASTM (D6319, D3578, F2100) and ISO (7864, 7886) standards | [BD Luer-Lok Syringe Product Page](https://www.bd.com/en-us/products-and-solutions/products/product-page.309589), [SurgiMac Disposable Medical Supplies](https://surgimac.com/collections/disposable-medical-supplies), [Medline FitGuard Gloves](https://www.medline.com/product/Critical-Response-Nitrile-Exam-Gloves/Z05-PF105686), [MFI Medical Essential Supplies 2025](https://mfimedical.com/blogs/news/essential-medical-supplies-for-clinics-and-hospitals-in-2025) |
