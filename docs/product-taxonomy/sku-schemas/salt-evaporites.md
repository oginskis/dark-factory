# SKU Schema: Salt & Evaporites

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or manufacturer product identifier | CMP-DRX-50, CGS-EVAP-99, MWS-SOL-CRS |
| Product Name | text | Full product name including type, grade, and production method | Compass Minerals DriRox Kiln-Dried Solar Salt, Cargill Top-Flo Evaporated Salt 99.9%, Morton Extra Coarse Solar Salt for Water Softening |
| URL | text | Direct link to the product page | https://example.com/products/drirox-solar-salt |
| Price | number | Numeric price per unit (per tonne, per bag, or per pallet), excluding currency symbol | 45.00, 120.00, 350.00, 8.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Salt producer or supplier name | Compass Minerals, Cargill, Morton Salt, K+S, Midwest Salt, Gunther Salt, ICL |
| NaCl Purity | number (%) | Sodium chloride assay on a dry basis | 95.0, 97.0, 99.0, 99.6, 99.9 |
| Production Method | enum | Primary method used to produce the salt | Rock Mining, Solar Evaporation, Vacuum Evaporation, Alberger Process, Solution Mining |
| Salt Form | enum | Physical form of the salt product | Coarse Crystal, Fine Granular, Powder, Flake, Pellet, Block, Brine, Rock |
| Grade | enum | Quality or application grade designation | Technical, Industrial, Food Grade, Pharmaceutical, USP, Water Softening, Deicing, Agricultural |
| Moisture Content | number (%) | Surface moisture content as shipped | 0.05, 0.1, 0.5, 2.0, 3.0 |
| Particle Size Range | text (mm) | Sieve-defined particle size distribution range | 0.1-0.5, 0.3-1.0, 1.0-3.0, 3.0-8.0, 6.0-25.0 |
| Median Particle Size | number (mm) | D50 median crystal or particle size | 0.3, 0.6, 1.5, 3.0, 6.0 |
| Water Insolubles | number (%) | Percentage of water-insoluble matter | 0.01, 0.05, 0.10, 0.50, 1.50 |
| Calcium (Ca) | number (%) | Calcium impurity content | 0.01, 0.05, 0.10, 0.40 |
| Magnesium (Mg) | number (%) | Magnesium impurity content | 0.001, 0.01, 0.05, 0.20 |
| Sulfate (SO4) | number (%) | Sulfate impurity content | 0.01, 0.05, 0.20, 0.50 |
| Iron (Fe) | number (ppm) | Iron impurity level | 1, 5, 10, 50, 200 |
| Anti-Caking Agent | text | Type and concentration of anti-caking additive if present | None, Yellow Prussiate of Soda (YPS) 14 ppm max, Sodium Ferrocyanide, Calcium Stearate |
| Bulk Density | number (kg/m3) | Loose bulk density of the product | 960, 1050, 1200, 1350, 1450 |
| Crystal Appearance | text | Visual description of crystal shape and color | White cubic crystals, Off-white irregular lumps, Clear translucent flakes, Pink rock salt |
| Color | text | Product color | White, Off-White, Gray, Pink, Translucent |
| Application | text (list) | Primary intended uses | Deicing, Water Softening, Chemical Manufacturing, Food Processing, Animal Nutrition, Dust Control, Oil and Gas Drilling, Pharmaceutical |
| Packaging | text | Available packaging options | 25 kg bag, 50 lb bag, 1 MT bulk bag, Bulk loose, 40 lb pellet bag, Block |
| Regulatory Compliance | text (list) | Food, safety, and quality standards met | FDA 21 CFR, NSF/ANSI 60, Codex Alimentarius, BS 3247:2011, Kosher, Halal |
| Country of Origin | text | Country where the salt was produced | USA, UK, Canada, Germany, Chile, India, Pakistan, Australia |
| Certification | text (list) | Quality or management system certifications | ISO 9001, ISO 22000, FSSC 22000, GMP, BRC |
| Shelf Life | text | Recommended storage duration | 12 months, 24 months, 36 months, Indefinite if dry |
| Minimum Order Quantity | text | Minimum purchase size | 1 pallet, 1 truckload, 20 MT, Bulk tanker |
| CAS Number | text | Chemical Abstracts Service registry number for NaCl | 7647-14-5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (Codex Alimentarius salt standards, BS 3247, NSF/ANSI 60) | [Compass Minerals](https://www.compassminerals.com/what-we-do/salt/), [Cargill Salt](https://www.cargill.com/industrial/na/general-industrial-salts), [Midwest Salt](https://midwestsalt.com/product/coarse-industrial-salt/), [ICL Industrial Products](https://icl-industrialproducts.com/products/sodium-chloride-industrial/) |
