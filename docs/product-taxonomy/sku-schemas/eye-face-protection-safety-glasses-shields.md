# SKU Schema: Eye & Face Protection (Safety Glasses, Shields)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.eye_face_protection`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | SF400G-WV-6, S3200HS, 11329-00000-20 |
| Product Name | product_name | text | — | Full product name including key specs such as type, lens tint, and model | 3M SecureFit 400 Series Anti-Fog Safety Glasses Clear Lens, Uvex Avatar Safety Glasses Gray Lens |
| URL | url | text | — | Direct link to the product page | https://example.com/product/securfit-400-clear |
| Price | price | number | — | Numeric unit price excluding currency symbol | 4.99, 12.50, 29.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary type of eye or face protection | Safety Glasses, Safety Goggles, Face Shield, Welding Helmet, Over-the-Glass (OTG) Glasses |
| Lens Material | lens_material | enum | — | Material the lens is made from | Polycarbonate, Trivex, Glass, Propionate |
| Frame Material | frame_material | text | — | Material of the spectacle frame or goggle body | Nylon, Polycarbonate, Rubber, TR-90, Metal |
| Ventilation Type | ventilation_type | text | — | Air flow design to reduce fogging (goggles) | Indirect Vent, Direct Vent, Sealed, Non-Vented |
| Fit Type | fit_type | text | — | How the eyewear adapts to different face shapes | Adjustable Temple, Pressure Diffusion Temple, Ratchet Temple, Elastic Strap |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Face Shield Visor Material | face_shield_visor_material | text | — | Material of the visor panel for face shields | Polycarbonate, PETG, Acetate, Mesh |
| Nose Bridge Type | nose_bridge_type | text | — | Nose pad style for comfort and fit | Soft Rubber, Adjustable Wire, Integrated, Foam Cushion |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, Mexico, China, Taiwan |
| Model Number | model_number | text | — | Manufacturer model or part number | SF401AF-WV, S3200HS, GG501SGAF |
| Lens Tint/Color | lens_tintcolor | text | — | Lens color or tint for light and glare management | Clear, Gray, Amber, Indoor/Outdoor Mirror, Blue Mirror, Smoke, Yellow |
| Lens Coating | lens_coating | text (list) | — | Surface treatment applied to the lens | Anti-Fog, Anti-Scratch, Anti-Static, Hard Coat, Mirror, Scotchgard Protector |
| UV Protection | uv_protection | text | — | Ultraviolet light filtration level | 99.9% UVA/UVB, UV400 |
| Frame Color | frame_color | text | — | Color of the frame, temples, or goggle body | Black, Blue, Clear, Gray, Translucent |
| Lens Shape | lens_shape | text | — | Geometry and coverage style of the lens | Wraparound, Flat, Panoramic, Spherical |
| Base Curve | base_curve | text | — | Lens curvature that determines peripheral coverage | 6 Base, 8 Base, 9 Base, 10 Base |
| Impact Rating | impact_rating | text | — | Impact protection marking per ANSI Z87.1 | Z87+, Z87, Z87+ D3 (droplet), Z87+ D4 (dust), Z87+ D5 (fine dust) |
| Prescription Compatible | prescription_compatible | boolean | — | Whether the eyewear accepts prescription inserts or is Rx-ready | true, false |
| Headgear Compatibility | headgear_compatibility | text | — | Hard hat or headgear attachment system for face shields | Universal Slot, MSA V-Gard, Ratchet Headgear |
| Shade Number | shade_number | text | — | Darkness level for welding or IR filtering lenses | Shade 3, Shade 5, Shade 10, Shade 12, Auto-Darkening 4-13 |
| Color Options | color_options | text (list) | — | Available frame and lens combinations | Black/Clear, Blue/Gray, Red/Amber |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ANSI Z87.1, CSA Z94.3, EN 166) | [3M Eye Protection](https://www.3m.com/3M/en_US/p/c/ppe/eye-protection/glasses/), [Honeywell Safety Eyewear](https://automation.honeywell.com/us/en/products/personal-protective-equipment/eye-protection/safety-eyewear/safety-glasses), [Pyramex Safety](https://www.pyramexsafety.com/), [Safety Glasses USA](https://safetyglassesusa.com/collections/3m) |
