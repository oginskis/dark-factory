# SKU Schema: Respiratory Protection (Masks, Respirators)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 8210, 8511, 6800, MOLDEX-2200 |
| Product Name | text | Full product name including key specs such as type, filter class, and model | 3M Particulate Respirator 8210 N95, Moldex 2200 N95 Disposable Respirator, 3M 6800 Full Facepiece Reusable Respirator |
| URL | text | Direct link to the product page | https://example.com/product/3m-8210-n95-respirator |
| Price | number | Numeric unit price excluding currency symbol | 1.25, 18.99, 149.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the respiratory protection manufacturer | 3M, Moldex, Honeywell, MSA, GVS, Draeger |
| Product Type | enum | Primary type of respirator | Disposable Particulate Respirator, Reusable Half-Facepiece Respirator, Reusable Full-Facepiece Respirator, Powered Air-Purifying Respirator (PAPR), Supplied Air Respirator (SAR), Self-Contained Breathing Apparatus (SCBA) |
| Filter Class (NIOSH) | text | NIOSH filtration classification for particulate and chemical protection | N95, N99, N100, R95, P95, P100, OV, AG, OV/AG/P100 |
| Filter Class (EN) | text | European filtration classification | FFP1, FFP2, FFP3, A1, A2, B2, E2, K2, ABEK |
| Assigned Protection Factor | number | Workplace protection factor per OSHA | 10, 25, 50, 1000 |
| Filtration Efficiency | text | Minimum percentage of particles filtered at test conditions | 95%, 99%, 99.97% |
| Facepiece Shape | enum | Physical form of the respirator facepiece | Cup, Flat Fold, Three-Panel, Half Mask, Full Face |
| Exhalation Valve | boolean | Whether the respirator includes an exhalation valve for reduced breathing resistance | true, false |
| Head Strap Type | text | Mechanism to secure the respirator to the head | Two-Strap, Single Strap, Cradle, Head Harness, Behind-Ear Loops |
| Nose Clip Type | text | Method for achieving a seal around the nose | Adjustable Aluminum, M-Nose Clip, Cushioning Nose Foam, Molded Nose Bridge |
| Size | text | Available sizing options | Small, Medium, Large, Universal, S/M, M/L |
| Cartridge/Filter Interface | text | Connection standard for replaceable filters and cartridges on reusable respirators | Bayonet, Threaded 40mm, Snap-In, Proprietary Click |
| Compatible Cartridges | text (list) | Cartridge or filter model numbers compatible with the facepiece | 3M 6001, 3M 2091, 3M 7093, Moldex 7600 |
| Material | text | Primary material of the facepiece or filter media | Electrostatically Charged Polypropylene, Silicone, Thermoplastic Elastomer, EPDM Rubber |
| Weight | number (g) | Weight of the respirator without cartridges or with standard filters | 8, 12, 170, 420 |
| Latex Free | boolean | Whether the product is free of natural rubber latex | true, false |
| Fluid Resistance | boolean | Whether the respirator resists penetration by synthetic blood (surgical/medical use) | true, false |
| Inhalation Resistance | text | Measured breathing resistance at standard test flow rate | Less than 35 mm H2O at 85 L/min |
| Application | text (list) | Intended use environments and hazards | Sanding, Welding, Painting, Chemical Handling, Mold Remediation, Asbestos, Healthcare |
| Shelf Life | text | Recommended product expiration or storage life | 3 years, 5 years, 10 years |
| Pack Quantity | number | Number of respirators per box or case | 1, 10, 20, 160 |
| Certifications | text (list) | Applicable safety and regulatory standards met | NIOSH 42 CFR 84, EN 149:2001+A1:2009, AS/NZS 1716, GB 2626-2019 |
| NIOSH Approval Number | text | NIOSH test and certification approval identifier | TC-84A-0007, TC-84A-9226 |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, China, Germany |
| Model Number | text | Manufacturer model or part number | 8210, 8511, 6200, 2200N95 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (NIOSH 42 CFR 84, EN 149, AS/NZS 1716) | [3M Respiratory Protection](https://www.3m.com/3M/en_US/respiratory-protection-us/), [Moldex](https://www.moldex.com/product-category/respiratory-protection/), [Honeywell Safety](https://automation.honeywell.com/us/en/products/personal-protective-equipment/), [Enviro Safety Products](https://www.envirosafetyproducts.com/collections/respiratory-protection) |
