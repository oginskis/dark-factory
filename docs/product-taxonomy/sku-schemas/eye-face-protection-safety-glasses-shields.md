# SKU Schema: Eye & Face Protection (Safety Glasses, Shields)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SF400G-WV-6, S3200HS, 11329-00000-20 |
| Product Name | text | Full product name including key specs such as type, lens tint, and model | 3M SecureFit 400 Series Anti-Fog Safety Glasses Clear Lens, Uvex Avatar Safety Glasses Gray Lens |
| URL | text | Direct link to the product page | https://example.com/product/securfit-400-clear |
| Price | number | Numeric unit price excluding currency symbol | 4.99, 12.50, 29.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the eye/face protection manufacturer | 3M, Honeywell, Uvex, Pyramex, Bollé, MCR Safety, Gateway Safety, Edge Eyewear |
| Product Type | enum | Primary type of eye or face protection | Safety Glasses, Safety Goggles, Face Shield, Welding Helmet, Over-the-Glass (OTG) Glasses |
| Lens Material | enum | Material the lens is made from | Polycarbonate, Trivex, Glass, Propionate |
| Lens Tint/Color | text | Lens color or tint for light and glare management | Clear, Gray, Amber, Indoor/Outdoor Mirror, Blue Mirror, Smoke, Yellow |
| Lens Coating | text (list) | Surface treatment applied to the lens | Anti-Fog, Anti-Scratch, Anti-Static, Hard Coat, Mirror, Scotchgard Protector |
| UV Protection | text | Ultraviolet light filtration level | 99.9% UVA/UVB, UV400 |
| Frame Material | text | Material of the spectacle frame or goggle body | Nylon, Polycarbonate, Rubber, TR-90, Metal |
| Frame Color | text | Color of the frame, temples, or goggle body | Black, Blue, Clear, Gray, Translucent |
| Lens Shape | text | Geometry and coverage style of the lens | Wraparound, Flat, Panoramic, Spherical |
| Base Curve | text | Lens curvature that determines peripheral coverage | 6 Base, 8 Base, 9 Base, 10 Base |
| Ventilation Type | text | Air flow design to reduce fogging (goggles) | Indirect Vent, Direct Vent, Sealed, Non-Vented |
| Impact Rating | text | Impact protection marking per ANSI Z87.1 | Z87+, Z87, Z87+ D3 (droplet), Z87+ D4 (dust), Z87+ D5 (fine dust) |
| Fit Type | text | How the eyewear adapts to different face shapes | Adjustable Temple, Pressure Diffusion Temple, Ratchet Temple, Elastic Strap |
| Prescription Compatible | boolean | Whether the eyewear accepts prescription inserts or is Rx-ready | true, false |
| Face Shield Visor Material | text | Material of the visor panel for face shields | Polycarbonate, PETG, Acetate, Mesh |
| Face Shield Window Size | text | Visible area dimensions of the face shield visor | 8 x 15.5 in, 9 x 14 in |
| Headgear Compatibility | text | Hard hat or headgear attachment system for face shields | Universal Slot, MSA V-Gard, Ratchet Headgear |
| Shade Number | text | Darkness level for welding or IR filtering lenses | Shade 3, Shade 5, Shade 10, Shade 12, Auto-Darkening 4-13 |
| Weight | number (g) | Total weight of the eyewear or face shield | 19, 23, 35, 170 |
| Nose Bridge Type | text | Nose pad style for comfort and fit | Soft Rubber, Adjustable Wire, Integrated, Foam Cushion |
| Temple Length | text | Length or adjustability of the earpieces | Fixed, Adjustable 4-Position, Telescoping |
| Color Options | text (list) | Available frame and lens combinations | Black/Clear, Blue/Gray, Red/Amber |
| Certifications | text (list) | Applicable safety standards met | ANSI/ISEA Z87.1-2020, CSA Z94.3, EN 166, AS/NZS 1337 |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, China, Taiwan |
| Pack Quantity | number | Number of pairs per box or case | 1, 12, 20 |
| Model Number | text | Manufacturer model or part number | SF401AF-WV, S3200HS, GG501SGAF |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ANSI Z87.1, CSA Z94.3, EN 166) | [3M Eye Protection](https://www.3m.com/3M/en_US/p/c/ppe/eye-protection/glasses/), [Honeywell Safety Eyewear](https://automation.honeywell.com/us/en/products/personal-protective-equipment/eye-protection/safety-eyewear/safety-glasses), [Pyramex Safety](https://www.pyramexsafety.com/), [Safety Glasses USA](https://safetyglassesusa.com/collections/3m) |
