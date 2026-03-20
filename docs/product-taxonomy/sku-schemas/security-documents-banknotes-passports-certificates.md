# SKU Schema: Security Documents (Banknotes, Passports, Certificates)

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.security_documents`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer, issuing authority, or catalog reference identifier | GD-BN-EUR50-2024, TOPS-PP-V3, LQ-DURA-A4 |
| Product Name | product_name | text | — | yes | Full product or solution name including document type and key feature | Durasafe Composite Banknote Substrate, TOPPAN E-Passport Polycarbonate Datapage, A1 Security Watermarked Certificate Paper |
| URL | url | text | — | yes | Direct link to the product page or specification sheet | https://example.com/products/banknote-substrate |
| Price | price | number | — | yes | Numeric unit price or price per thousand sheets, excluding currency symbol | 0.12, 85.00, 350.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CHF |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Document Type | document_type | enum | — | — | Classification of the security document product | Banknote Substrate, Passport Booklet, Passport Datapage, Identity Card, Certificate Paper, Visa Sticker, Tax Stamp, Diploma, Birth Certificate |
| Substrate Material | substrate_material | enum | — | — | Base material of the document | Cotton Fiber Paper, Polymer (BOPP), Composite (Paper-Polymer-Paper), Polycarbonate, Linen Blend, Abaca Fiber, Teslin |
| Watermark Type | watermark_type | text (list) | — | — | Types of watermark embedded in the substrate during manufacturing | Multi-Tone, Electrotype, Cylinder Mould, Mould-Made, Shadow, Bright |
| Security Thread Type | security_thread_type | text | — | — | Classification of embedded security thread | Windowed, Fully Embedded, Magnetic, Fluorescent, Microprinted, Color-Shifting, De-Metallized |
| Country of Origin | country_of_origin | text | — | — | Country where the security product is manufactured | Germany, Japan, UK, Switzerland, South Korea, France |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Width | width | number | mm | — | Finished width of the document | 127, 125, 156, 210 |
| Height | height | number | mm | — | Finished height of the document | 67, 88, 105, 297 |
| Thickness | thickness | number | um | — | Total thickness of the document substrate in micrometres | 80, 95, 110, 760 |
| Intaglio Printing | intaglio_printing | enum | — | — | Whether intaglio (raised ink) printing is applied | Yes, No |
| Optically Variable Feature | optically_variable_feature | text (list) | — | — | Types of optically variable devices or inks present | OVI (Optically Variable Ink), Hologram, DOVID, Kinegram, Color-Shifting Patch, Iridescent Stripe, Diffractive Element |
| UV Fluorescent Elements | uv_fluorescent_elements | enum | — | — | Whether UV-reactive fluorescent inks or fibers are present | Yes, No |
| Infrared Feature | infrared_feature | enum | — | — | Whether IR-readable security elements are incorporated | Yes, No |
| Machine-Readable Feature | machine-readable_feature | text (list) | — | — | Types of machine-readable security elements | Magnetic Ink, RFID/NFC Chip, Phosphorescent Ink, Barcode, MRZ (Machine Readable Zone) |
| RFID/NFC Chip | rfidnfc_chip | enum | — | — | Whether the document contains an embedded contactless chip | Yes (ICAO 9303 compliant), Yes (ISO 14443), No |
| Biometric Data Support | biometric_data_support | text (list) | — | — | Types of biometric data stored on the chip for identity documents | Facial Image, Fingerprint, Iris, Digital Signature |
| Printing Techniques | printing_techniques | text (list) | — | — | All printing methods used in document production | Intaglio, Offset, Letterpress, Screen, Digital, Gravure, Laser Engraving, Laser Perforation |
| Durability Rating | durability_rating | text | — | — | Expected circulation life or durability specification | 5 years, 10 years, 2.5x paper equivalent, 10000 folds |
| Tamper Evidence | tamper_evidence | text (list) | — | — | Anti-tampering features that reveal unauthorized modification | Laser Personalization, Heat-Sensitive Ink, Chemically Sensitive Substrate, Secure Hinge, Perforated Number |
| Compliance Standard | compliance_standard | text (list) | — | — | International standards the document product conforms to | ICAO 9303, ISO 14443, ISO 1831, ISO 12757, ISO 14298 |
| Minimum Order Quantity | minimum_order_quantity | number | — | — | Smallest order quantity accepted by the manufacturer | 1000, 10000, 100000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus international standards (ICAO 9303, ISO 14443, ISO 14298 security printing) | [Giesecke+Devrient Substrates](https://www.gi-de.com/en/currency-technology/banknote-solutions/banknote-production/substrates), [TOPPAN Security Passports](https://toppansecurity.com/passports/), [Landqart Durasafe](https://www.landqart.com/en/products/durasafe/), [A1 Security Print](https://www.a1securityprint.com/security-paper/) |
