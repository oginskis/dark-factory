# SKU Schema: Surgical Instruments & Tools

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.surgical_instruments`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor catalog reference number | FC004R, 87-86402, BD520R, PM-4508 |
| Product Name | product_name | text | — | Full product name including eponym, instrument type, and key dimensions | JENKNER Tunneler 440 mm Conical Tip, METZENBAUM Scissors Curved 180 mm, DEBAKEY Forceps Atraumatic 200 mm |
| URL | url | text | — | Direct link to the product page | https://example.com/instruments/fc004r |
| Price | price | number | — | Numeric price per unit, excluding currency symbol | 85.00, 320.00, 42.50, 1250.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Instrument Category | instrument_category | text | — | Broad functional class of the instrument | Scissors, Forceps, Retractors, Clamps, Needle Holders, Dissectors, Elevators, Rongeurs, Curettes |
| Material | material | text | — | Primary construction material of the working surfaces and body | Stainless Steel, Titanium, Tungsten Carbide Insert, German Stainless Steel, Surgical Grade 420 |
| Tip Type | tip_type | text | — | Configuration and sharpness of the instrument tip or jaw | Sharp/Sharp, Sharp/Blunt, Blunt/Blunt, Conical, Serrated, Atraumatic, Toothed, Fenestrated |
| Handle Type | handle_type | text | — | Design and shape of the handle or grip | Ring Handle, Round Handle, Bayonet Handle, Spring Handle, Flat Handle, Ergonomic, Ratchet |
| Overall Length | overall_length | number | mm | Total instrument length from tip to end of handle | 110, 180, 250, 440, 340 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Surgical Specialty | surgical_specialty | text (list) | — | Medical specialties the instrument is designed for | General Surgery, Orthopedic, Cardiovascular, Neurosurgery, ENT, Ophthalmic, Plastic, OB-GYN, Urology |
| Surface Finish | surface_finish | text | — | Surface treatment or coating applied to the instrument | Satin, Mirror Polish, Black Ceramic Coating, Gold Handle (TC), Dia-Dust Coating |
| Tip Profile | tip_profile | text | — | Shape and geometry of the working tip or jaw | Straight, Curved, Angled 45 degrees, Bayonet, S-Shaped, Double-Action |
| Jaw Width | jaw_width | number | mm | Width of the grasping jaw or platform at the tip | 0.80, 1.5, 3.0, 5.0 |
| Ratchet/Lock Mechanism | ratchetlock_mechanism | enum | — | Presence and type of locking mechanism | Ratchet Lock, Box Lock, Bayonet Lock, None |
| Single Use vs Reusable | single_use_vs_reusable | enum | — | Whether the instrument is designed for single use or reprocessing | Reusable, Single Use (Disposable) |
| Sterility | sterility | enum | — | Sterile status at point of delivery | Sterile, Non-Sterile |
| Sterilization Method | sterilization_method | text (list) | — | Compatible sterilization methods for reusable instruments | Autoclave (Steam 134C), Ethylene Oxide, Low-Temperature Plasma |
| Max Sterilization Cycles | max_sterilization_cycles | number | — | Maximum number of sterilization cycles before end of life (reusable instruments) | 250, 500, 1000 |
| EAN/GTIN | eangtin | text | — | European Article Number / Global Trade Item Number barcode | 4038653065080, 5060123456789 |
| HCPCS Code | hcpcs_code | text | — | Healthcare Common Procedure Coding System code for reimbursement | L8699, A4649 |
| Regulatory Clearance | regulatory_clearance | text (list) | — | Medical device regulatory clearances | FDA 510(k), CE Mark (MDR Class I), ISO 13485 |
| Instrument Set Compatibility | instrument_set_compatibility | text | — | Name of the surgical set or tray the instrument belongs to | Basic Laparotomy Set, Micro Neurosurgery Tray, Cardiac Cannulation Set |
| Insulation | insulation | enum | — | Whether the instrument is electrically insulated for electrosurgery | Insulated, Non-Insulated |
| Compatible Power Systems | compatible_power_systems | text | — | Power handpiece or generator compatibility for powered instruments | Stryker System 8, Synthes AO Power, Aesculap Acculan 4 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ISO 7153 (surgical instrument materials), ISO 13485 (quality management), and HCPCS coding standards | [B. Braun Aesculap](https://surgical-instruments.bbraun.com/en-01), [McKesson Medical-Surgical](https://mms.mckesson.com/catalog?node=5631124+8962), [KLS Martin](https://www.klsmartin.com/en/products/surgical-instruments/), [Millennium Surgical](https://www.surgicalinstruments.com/) |
