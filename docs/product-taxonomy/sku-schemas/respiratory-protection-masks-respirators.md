# SKU Schema: Respiratory Protection (Masks, Respirators)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.respiratory_protection`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 8210, 8511, 6800, MOLDEX-2200 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, filter class, and model | 3M Particulate Respirator 8210 N95, Moldex 2200 N95 Disposable Respirator, 3M 6800 Full Facepiece Reusable Respirator |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/3m-8210-n95-respirator |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 1.25, 18.99, 149.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary type of respirator | Disposable Particulate Respirator, Reusable Half-Facepiece Respirator, Reusable Full-Facepiece Respirator, Powered Air-Purifying Respirator (PAPR), Supplied Air Respirator (SAR), Self-Contained Breathing Apparatus (SCBA) |
| Filter Class (NIOSH) | filter_class_niosh | text | — | — | NIOSH filtration classification for particulate and chemical protection | N95, N99, N100, R95, P95, P100, OV, AG, OV/AG/P100 |
| Filter Class (EN) | filter_class_en | text | — | — | European filtration classification | FFP1, FFP2, FFP3, A1, A2, B2, E2, K2, ABEK |
| Head Strap Type | head_strap_type | text | — | — | Mechanism to secure the respirator to the head | Two-Strap, Single Strap, Cradle, Head Harness, Behind-Ear Loops |
| Nose Clip Type | nose_clip_type | text | — | — | Method for achieving a seal around the nose | Adjustable Aluminum, M-Nose Clip, Cushioning Nose Foam, Molded Nose Bridge |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Material | material | text | — | — | Primary material of the facepiece or filter media | Electrostatically Charged Polypropylene, Silicone, Thermoplastic Elastomer, EPDM Rubber |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, Mexico, China, Germany |
| Model Number | model_number | text | — | — | Manufacturer model or part number | 8210, 8511, 6200, 2200N95 |
| Assigned Protection Factor | assigned_protection_factor | number | — | — | Workplace protection factor per OSHA | 10, 25, 50, 1000 |
| Filtration Efficiency | filtration_efficiency | text | — | — | Minimum percentage of particles filtered at test conditions | 95%, 99%, 99.97% |
| Facepiece Shape | facepiece_shape | enum | — | — | Physical form of the respirator facepiece | Cup, Flat Fold, Three-Panel, Half Mask, Full Face |
| Exhalation Valve | exhalation_valve | boolean | — | — | Whether the respirator includes an exhalation valve for reduced breathing resistance | true, false |
| Cartridge/Filter Interface | cartridgefilter_interface | text | — | — | Connection standard for replaceable filters and cartridges on reusable respirators | Bayonet, Threaded 40mm, Snap-In, Proprietary Click |
| Compatible Cartridges | compatible_cartridges | text (list) | — | — | Cartridge or filter model numbers compatible with the facepiece | 3M 6001, 3M 2091, 3M 7093, Moldex 7600 |
| Latex Free | latex_free | boolean | — | — | Whether the product is free of natural rubber latex | true, false |
| Fluid Resistance | fluid_resistance | boolean | — | — | Whether the respirator resists penetration by synthetic blood (surgical/medical use) | true, false |
| Inhalation Resistance | inhalation_resistance | text | — | — | Measured breathing resistance at standard test flow rate | Less than 35 mm H2O at 85 L/min |
| Application | application | text (list) | — | — | Intended use environments and hazards | Sanding, Welding, Painting, Chemical Handling, Mold Remediation, Asbestos, Healthcare |
| Shelf Life | shelf_life | text | — | — | Recommended product expiration or storage life | 3 years, 5 years, 10 years |
| Pack Quantity | pack_quantity | number | — | — | Number of respirators per box or case | 1, 10, 20, 160 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (NIOSH 42 CFR 84, EN 149, AS/NZS 1716) | [3M Respiratory Protection](https://www.3m.com/3M/en_US/respiratory-protection-us/), [Moldex](https://www.moldex.com/product-category/respiratory-protection/), [Honeywell Safety](https://automation.honeywell.com/us/en/products/personal-protective-equipment/), [Enviro Safety Products](https://www.envirosafetyproducts.com/collections/respiratory-protection) |
