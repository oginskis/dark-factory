# SKU Schema: Prosthetics & Implants

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.prosthetics_implants`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer article number or catalog identifier | 1C11, 1A1-2, 1C64, FC004R, PERSONA-TIB-09 |
| Product Name | text | Full product name including type, model designation, and key differentiator | Terion K2 Prosthetic Foot, Persona Personalized Knee System, 4.0/5.0mm Cannulated Screw System, Empower Microprocessor Foot |
| URL | text | Direct link to the product page | https://example.com/products/terion-k2 |
| Price | number | Numeric price per unit, excluding currency symbol | 4500.00, 12500.00, 85.00, 35000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Category | enum | Broad device category | Prosthetic Limb Component, Joint Implant, Trauma Fixation, Spinal Implant, Dental Implant, Cranial Implant |
| Device Subcategory | text | Specific device type within the category | Prosthetic Foot, Prosthetic Knee Joint, Total Knee Replacement, Hip Stem, Cannulated Screw, Locking Plate, Intervertebral Cage |
| Primary Material | text | Main structural material or alloy | Ti-6Al-4V ELI Titanium, CoCr (Cobalt-Chromium), Carbon Fiber, 316L Stainless Steel, Tivanium Alloy, PEEK |
| Bearing Surface Material | text | Articulating or bearing surface material (joint implants) | Highly Crosslinked Polyethylene, OXINIUM Oxidized Zirconium, Ceramic (Alumina), Vivacit-E Vitamin-E Polyethylene |
| Fixation Type | enum | Method of securing the implant to bone | Cemented, Cementless (Press-Fit), Hybrid, Screw Fixation |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Connector Type | text | Proximal or distal connection standard | Pyramid Adapter, Tube Clamp, Standard 4-hole, Aluminum Adapter, Morse Taper |
| Manufacturer | text | Device manufacturer name | Ottobock, Zimmer Biomet, Smith and Nephew, Stryker, DePuy Synthes, Ossur |
| Body Region | text | Anatomical region the device is intended for | Lower Limb, Upper Limb, Hip, Knee, Foot and Ankle, Spine, Cranio-Maxillofacial |
| Amputation/Indication Level | text | Specific amputation level or clinical indication | Transtibial, Transfemoral, Primary Total Knee Arthroplasty, Fracture Fixation, Degenerative Disc Disease |
| Surface Treatment | text | Surface coating or texturing applied to promote fixation or reduce wear | Type 2 Anodized, Trabecular Metal, Hydroxyapatite Coated, Plasma Spray Titanium, TiMax |
| Laterality | enum | Whether the device is side-specific | Left, Right, Universal |
| Activity Level | text | Mobility grade or activity classification for prosthetic components | K1, K2, K3, K4, Low Activity, Moderate, High Activity |
| Build Height | number (mm) | Minimum proximal build height required for fitting | 59, 70, 87, 203 |
| System Height | number (mm) | Total system height including all connectors and shell | 120, 175, 203 |
| Heel Height | number (mm) | Heel height specification for prosthetic feet | 0, 5, 10, 15 |
| Color Options | text (list) | Available cosmetic color options | Beige 4, Light Brown 15, Black |
| Sterility | enum | Sterile status at delivery | Sterile, Non-Sterile |
| HCPCS Code | text | US Healthcare Common Procedure Coding System code | L5972, L5986, L5856, L8699 |
| Regulatory Clearance | text (list) | Medical device regulatory clearances | FDA 510(k), CE Mark (EU MDR), ISO 13485, Health Canada |
| Biocompatibility Standard | text | Biocompatibility testing standard compliance | ISO 10993, ASTM F2129, USP Class VI |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ISO 13485 (quality management), ISO 10993 (biocompatibility), and HCPCS coding standards | [Ottobock US Shop](https://shop.ottobock.us/Prosthetics/Lower-Limb-Prosthetics/Feet---Mechanical/Terion-K2/p/1C11), [Zimmer Biomet](https://www.zimmerbiomet.com/en/products-and-solutions/specialties/knee/persona-knee-system.html), [Smith and Nephew](https://www.smith-nephew.com/en-us/health-care-professionals/products/orthopaedics/polarstem), [GPC Medical](https://www.gpcmedicalusa.com/) |
