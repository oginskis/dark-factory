# SKU Schema: Surgical Instruments & Tools

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor catalog reference number | FC004R, 87-86402, BD520R, PM-4508 |
| Product Name | text | Full product name including eponym, instrument type, and key dimensions | JENKNER Tunneler 440 mm Conical Tip, METZENBAUM Scissors Curved 180 mm, DEBAKEY Forceps Atraumatic 200 mm |
| URL | text | Direct link to the product page | https://example.com/instruments/fc004r |
| Price | number | Numeric price per unit, excluding currency symbol | 85.00, 320.00, 42.50, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Instrument manufacturer or brand name | Aesculap (B. Braun), KLS Martin, Stryker, Integra, Codman |
| Instrument Category | text | Broad functional class of the instrument | Scissors, Forceps, Retractors, Clamps, Needle Holders, Dissectors, Elevators, Rongeurs, Curettes |
| Surgical Specialty | text (list) | Medical specialties the instrument is designed for | General Surgery, Orthopedic, Cardiovascular, Neurosurgery, ENT, Ophthalmic, Plastic, OB-GYN, Urology |
| Material | text | Primary construction material of the working surfaces and body | Stainless Steel, Titanium, Tungsten Carbide Insert, German Stainless Steel, Surgical Grade 420 |
| Surface Finish | text | Surface treatment or coating applied to the instrument | Satin, Mirror Polish, Black Ceramic Coating, Gold Handle (TC), Dia-Dust Coating |
| Overall Length | number (mm) | Total instrument length from tip to end of handle | 110, 180, 250, 440, 340 |
| Working Length | number (mm) | Usable working length from the pivot or shaft entry to the tip | 80, 150, 210, 400 |
| Shaft Diameter | number (mm) | Outer diameter of the instrument shaft or barrel | 3, 5, 9, 12 |
| Tip Type | text | Configuration and sharpness of the instrument tip or jaw | Sharp/Sharp, Sharp/Blunt, Blunt/Blunt, Conical, Serrated, Atraumatic, Toothed, Fenestrated |
| Tip Profile | text | Shape and geometry of the working tip or jaw | Straight, Curved, Angled 45 degrees, Bayonet, S-Shaped, Double-Action |
| Jaw Width | number (mm) | Width of the grasping jaw or platform at the tip | 0.80, 1.5, 3.0, 5.0 |
| Handle Type | text | Design and shape of the handle or grip | Ring Handle, Round Handle, Bayonet Handle, Spring Handle, Flat Handle, Ergonomic, Ratchet |
| Ratchet/Lock Mechanism | enum | Presence and type of locking mechanism | Ratchet Lock, Box Lock, Bayonet Lock, None |
| Weight | number (g) | Net instrument weight | 45, 112, 166, 325 |
| Gross Weight | number (g) | Packaged weight including any protective sleeve | 48, 115, 167, 330 |
| Single Use vs Reusable | enum | Whether the instrument is designed for single use or reprocessing | Reusable, Single Use (Disposable) |
| Sterility | enum | Sterile status at point of delivery | Sterile, Non-Sterile |
| Sterilization Method | text (list) | Compatible sterilization methods for reusable instruments | Autoclave (Steam 134C), Ethylene Oxide, Low-Temperature Plasma |
| Max Sterilization Cycles | number | Maximum number of sterilization cycles before end of life (reusable instruments) | 250, 500, 1000 |
| EAN/GTIN | text | European Article Number / Global Trade Item Number barcode | 4038653065080, 5060123456789 |
| HCPCS Code | text | Healthcare Common Procedure Coding System code for reimbursement | L8699, A4649 |
| Regulatory Clearance | text (list) | Medical device regulatory clearances | FDA 510(k), CE Mark (MDR Class I), ISO 13485 |
| Country of Manufacture | text | Country where the instrument is manufactured | Germany, Pakistan, USA, Japan, France |
| Instrument Set Compatibility | text | Name of the surgical set or tray the instrument belongs to | Basic Laparotomy Set, Micro Neurosurgery Tray, Cardiac Cannulation Set |
| Insulation | enum | Whether the instrument is electrically insulated for electrosurgery | Insulated, Non-Insulated |
| Compatible Power Systems | text | Power handpiece or generator compatibility for powered instruments | Stryker System 8, Synthes AO Power, Aesculap Acculan 4 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ISO 7153 (surgical instrument materials), ISO 13485 (quality management), and HCPCS coding standards | [B. Braun Aesculap](https://surgical-instruments.bbraun.com/en-01), [McKesson Medical-Surgical](https://mms.mckesson.com/catalog?node=5631124+8962), [KLS Martin](https://www.klsmartin.com/en/products/surgical-instruments/), [Millennium Surgical](https://www.surgicalinstruments.com/) |
