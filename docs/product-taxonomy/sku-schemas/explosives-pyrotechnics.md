# SKU Schema: Explosives & Pyrotechnics

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DYNAP-75, APB-400, TROJAN-RP, NP2028 |
| Product Name | text | Full product name including brand, product line, and key specification | Dyno AP 75mm Cartridge, Austin Powder Hydromite 1100, TROJAN RINGPRIME Cast Booster, Protocol 2028 Barrage |
| URL | text | Direct link to the product page | https://example.com/product/dyno-ap-75 |
| Price | number | Numeric price per sales unit (case, cartridge, each, or kg), excluding currency symbol | 150.00, 2400.00, 45.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD, ZAR |
| Brand/Manufacturer | text | Company that produces or markets the product | Dyno Nobel, Orica, Austin Powder, Maxam, EPC Groupe, AECI, Estes, Celtic Fireworks |
| Product Line | text | Named series or range within the brand | DYNOMIX, Hydromite, TROJAN, Fortis, Emulex, FRAGMAX |
| Product Category | enum | Primary functional classification | Bulk Explosive, Packaged Explosive, Detonator, Booster, Detonating Cord, Initiating System, Consumer Firework, Display Firework, Signal Flare, Propellant |
| Explosive Type | text | Chemical or compositional type of the energetic material | ANFO, Emulsion, Watergel, Dynamite, Cast Pentolite, Black Powder, Flash Powder, Composite Propellant |
| Active Compound | text | Primary energetic chemical compound | Ammonium Nitrate/Fuel Oil, RDX, PETN, HMX, TNT, Nitroglycerine, Potassium Nitrate |
| UN Number | text | United Nations number for transport classification of the product | UN0082, UN0081, UN0331, UN0336, UN0335, UN0337 |
| UN Hazard Class/Division | text | UN explosives classification division | 1.1D, 1.1B, 1.3G, 1.4G, 1.4S, 1.5D |
| Compatibility Group | text | Letter designating mixing and storage compatibility per UN regulations | B, D, G, S |
| Packaging Group | text | UN packaging group indicating degree of danger | I, II, III |
| Density | number (g/cc) | Bulk or packed density of the product | 0.82, 1.10, 1.16, 1.30, 1.40, 1.55 |
| Velocity of Detonation | text (m/s) | Speed at which the detonation wave travels through the explosive at a stated diameter | 3960, 4400-5000, 4725, 7300 |
| Relative Weight Strength | number (%) | Energy output per unit mass relative to ANFO at 100% | 80, 100, 115, 130, 160 |
| Relative Bulk Strength | number (%) | Energy output per unit volume relative to ANFO at 100% | 100, 120, 148, 178, 210 |
| Energy | number (MJ/kg) | Detonation energy per unit mass | 2.8, 3.3, 3.7, 4.2, 5.0 |
| Water Resistance | enum | Ability of the product to perform in the presence of water | None, Limited, Good, Excellent |
| Detonator Sensitivity | enum | Whether the product can be initiated directly by a standard detonator | Cap Sensitive, Booster Required |
| Cartridge/Package Diameter | text (mm) | Outside diameter of the cartridge, package, or charge | 25, 32, 50, 65, 75, 100, 150 |
| Cartridge/Package Length | text (mm) | Length of the individual cartridge or unit | 200, 400, 600, 800 |
| Net Explosive Content | text (kg) | Mass of explosive substance per unit excluding non-explosive components | 0.05, 0.5, 1.0, 5.0, 25.0 |
| Fume Class | text | Classification of toxic fumes produced on detonation per applicable standard | Class 1, Class 2, Class 3 |
| Shelf Life | text | Maximum storage duration under recommended conditions from date of manufacture | 12 months, 24 months, 36 months |
| Storage Temperature Range | text | Ambient temperature limits for safe storage | -20 to 50 C, 0 to 40 C, 10 to 30 C |
| Minimum Order Quantity | text | Smallest purchasable quantity | 1 case, 1 pallet, 25 kg, 100 units |
| Certifications | text (list) | Regulatory approvals and compliance marks applicable to the product | CE, ISO 17025, BAM, MSHA, IME, BATFE |
| Application | text (list) | Primary intended commercial or industrial uses | Surface Mining, Underground Mining, Quarrying, Demolition, Seismic, Construction, Fireworks Display, Road Building |
| Country of Origin | text | Country where the product is manufactured | USA, Australia, Norway, Sweden, Spain, South Africa, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (UN Recommendations on Transport of Dangerous Goods, IME, OSHA 1910.109) | [Dyno Nobel](https://www.dynonobel.com/products-services/products/bulk-technology/anfo/), [Austin Powder](https://austinpowder.com/bulk-explosives/), [Orica](https://www.orica.com/products-services/initiating-systems/electrics/electrics), [PacSci EMC](https://psemc.com/resources/pyrotechnic-white-papers/properties-of-selected-high-explosives-rev/) |
