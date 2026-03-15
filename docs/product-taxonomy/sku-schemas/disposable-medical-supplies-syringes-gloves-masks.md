# SKU Schema: Disposable Medical Supplies (Syringes, Gloves, Masks)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor catalog number | 309589, FG3001, 1500PF-L, N95-1860 |
| Product Name | text | Full product name including type, material, and size | BD 3 mL Luer-Lok Syringe with 23G x 1-1/2 in Needle, Medline FitGuard Nitrile Exam Gloves Large, 3M 1860 N95 Surgical Respirator |
| URL | text | Direct link to the product page | https://example.com/product/bd-syringe-309589 |
| Price | number | Price per box or case as listed | 6.50, 12.99, 45.00, 125.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Product manufacturer or brand name | BD (Becton Dickinson), Medline, 3M, Cardinal Health, Halyard, Ansell, Teleflex, B. Braun, McKesson |
| Product Type | enum | Primary disposable supply category | Syringe, Hypodermic Needle, Exam Glove, Surgical Glove, Face Mask, N95 Respirator, Surgical Gown, Drape, IV Catheter, Wound Dressing, Suture |
| Material | text | Primary material composition | Nitrile, Latex, Vinyl, Polypropylene, Polyethylene, Neoprene, Silicone |
| Size | text | Product size designation | Small, Medium, Large, X-Large, 3 mL, 5 mL, 10 mL, 20 mL, 60 mL |
| Syringe Volume | number (mL) | Nominal syringe fill capacity | 1, 3, 5, 10, 20, 30, 60 |
| Tip Type | enum | Syringe tip connection style | Luer-Lok, Luer Slip, Catheter Tip, Eccentric Tip |
| Needle Gauge | text (G) | Needle outer diameter gauge number (higher number = thinner needle) | 18G, 20G, 21G, 22G, 23G, 25G, 27G, 30G |
| Needle Length | text (in) | Needle length from hub to tip | 1/2, 5/8, 1, 1-1/4, 1-1/2 |
| Needle Included | enum | Whether a needle is pre-attached to the syringe | Yes (Attached), No (Syringe Only) |
| Glove Thickness (Finger) | number (mil) | Finger thickness measurement in thousandths of an inch | 3.1, 4.0, 5.5, 6.0, 8.0 |
| Glove Thickness (Palm) | number (mil) | Palm thickness measurement in thousandths of an inch | 2.4, 3.0, 4.0, 5.0 |
| Glove Length | number (in) | Cuff-to-fingertip measurement | 9.5, 12, 16 |
| Cuff Style | enum | Glove cuff design | Beaded, Extended, Rolled |
| Texture | enum | Surface texture pattern for grip | Textured Fingertips, Fully Textured, Smooth, Micro-Textured |
| Powder Status | enum | Whether the product contains glove powder | Powder-Free, Powdered |
| Sterility | enum | Sterile or non-sterile designation | Sterile, Non-Sterile |
| Mask Type | enum | Face covering classification | Surgical Mask (ASTM Level 1/2/3), N95 Respirator, KN95, Procedure Mask |
| Filtration Level | text | Bacterial or particulate filtration efficiency | BFE greater than 98%, PFE greater than 95%, NIOSH N95 (95% filtration) |
| AQL | number | Acceptable Quality Level (defects per 100 units per ASTM D5151) | 0.65, 1.0, 1.5, 2.5 |
| Chemo Tested | enum | Whether the product is tested for chemotherapy drug permeation per ASTM D6978 | Yes, No |
| Latex Free | enum | Whether the product is free of natural rubber latex | Yes, No |
| Units per Box | number | Number of individual items per inner box | 50, 100, 200, 250 |
| Boxes per Case | number | Number of boxes per shipping case | 4, 10, 12, 20 |
| Color | text | Product color | Blue, Purple, White, Green, Amber, Clear |
| Hub Color Code | text | Color-coded needle hub per ISO 6009 for gauge identification | Pink (18G), Yellow (20G), Green (21G), Black (22G), Blue (23G), Orange (25G) |
| Regulatory Classification | text | Medical device regulatory class | FDA Class I, FDA Class II, CE Class I, CE Class IIa |
| Standards Compliance | text (list) | Applicable material and performance standards | ASTM D6319 (Nitrile Gloves), ASTM D3578 (Latex Gloves), ASTM D6978 (Chemo), ASTM F2100 (Masks), ISO 7864 (Needles), ISO 7886 (Syringes) |
| Shelf Life | text | Product shelf life from date of manufacture | 3 years, 5 years |
| Storage Conditions | text | Recommended storage environment | Cool, dry place away from direct sunlight, 15-30 C |
| Country of Manufacture | text | Country where the product is produced | USA, Malaysia, China, Mexico, Thailand |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus ASTM (D6319, D3578, F2100) and ISO (7864, 7886) standards | [BD Luer-Lok Syringe Product Page](https://www.bd.com/en-us/products-and-solutions/products/product-page.309589), [SurgiMac Disposable Medical Supplies](https://surgimac.com/collections/disposable-medical-supplies), [Medline FitGuard Gloves](https://www.medline.com/product/Critical-Response-Nitrile-Exam-Gloves/Z05-PF105686), [MFI Medical Essential Supplies 2025](https://mfimedical.com/blogs/news/essential-medical-supplies-for-clinics-and-hospitals-in-2025) |
