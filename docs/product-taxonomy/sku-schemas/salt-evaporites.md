# SKU Schema: Salt & Evaporites

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.salt_evaporites`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Supplier or manufacturer product identifier | CMP-DRX-50, CGS-EVAP-99, MWS-SOL-CRS |
| Product Name | product_name | text | Full product name including type, grade, and production method | Compass Minerals DriRox Kiln-Dried Solar Salt, Cargill Top-Flo Evaporated Salt 99.9%, Morton Extra Coarse Solar Salt for Water Softening |
| URL | url | text | Direct link to the product page | https://example.com/products/drirox-solar-salt |
| Price | price | number | Numeric price per unit (per tonne, per bag, or per pallet), excluding currency symbol | 45.00, 120.00, 350.00, 8.99 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Salt Form | salt_form | enum | Physical form of the salt product | Coarse Crystal, Fine Granular, Powder, Flake, Pellet, Block, Brine, Rock |
| Grade | grade | enum | Quality or application grade designation | Technical, Industrial, Food Grade, Pharmaceutical, USP, Water Softening, Deicing, Agricultural |
| Country of Origin | country_of_origin | text | Country where the salt was produced | USA, UK, Canada, Germany, Chile, India, Pakistan, Australia |
| Particle Size Range | particle_size_range | text (mm) | Sieve-defined particle size distribution range | 0.1-0.5, 0.3-1.0, 1.0-3.0, 3.0-8.0, 6.0-25.0 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| NaCl Purity | nacl_purity | number (%) | Sodium chloride assay on a dry basis | 95.0, 97.0, 99.0, 99.6, 99.9 |
| Production Method | production_method | enum | Primary method used to produce the salt | Rock Mining, Solar Evaporation, Vacuum Evaporation, Alberger Process, Solution Mining |
| Moisture Content | moisture_content | number (%) | Surface moisture content as shipped | 0.05, 0.1, 0.5, 2.0, 3.0 |
| Water Insolubles | water_insolubles | number (%) | Percentage of water-insoluble matter | 0.01, 0.05, 0.10, 0.50, 1.50 |
| Calcium (Ca) | calcium_ca | number (%) | Calcium impurity content | 0.01, 0.05, 0.10, 0.40 |
| Magnesium (Mg) | magnesium_mg | number (%) | Magnesium impurity content | 0.001, 0.01, 0.05, 0.20 |
| Sulfate (SO4) | sulfate_so4 | number (%) | Sulfate impurity content | 0.01, 0.05, 0.20, 0.50 |
| Iron (Fe) | iron_fe | number (ppm) | Iron impurity level | 1, 5, 10, 50, 200 |
| Anti-Caking Agent | anti-caking_agent | text | Type and concentration of anti-caking additive if present | None, Yellow Prussiate of Soda (YPS) 14 ppm max, Sodium Ferrocyanide, Calcium Stearate |
| Bulk Density | bulk_density | number (kg/m3) | Loose bulk density of the product | 960, 1050, 1200, 1350, 1450 |
| Crystal Appearance | crystal_appearance | text | Visual description of crystal shape and color | White cubic crystals, Off-white irregular lumps, Clear translucent flakes, Pink rock salt |
| Color | color | text | Product color | White, Off-White, Gray, Pink, Translucent |
| Application | application | text (list) | Primary intended uses | Deicing, Water Softening, Chemical Manufacturing, Food Processing, Animal Nutrition, Dust Control, Oil and Gas Drilling, Pharmaceutical |
| Packaging | packaging | text | Available packaging options | 25 kg bag, 50 lb bag, 1 MT bulk bag, Bulk loose, 40 lb pellet bag, Block |
| Regulatory Compliance | regulatory_compliance | text (list) | Food, safety, and quality standards met | FDA 21 CFR, NSF/ANSI 60, Codex Alimentarius, BS 3247:2011, Kosher, Halal |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (Codex Alimentarius salt standards, BS 3247, NSF/ANSI 60) | [Compass Minerals](https://www.compassminerals.com/what-we-do/salt/), [Cargill Salt](https://www.cargill.com/industrial/na/general-industrial-salts), [Midwest Salt](https://midwestsalt.com/product/coarse-industrial-salt/), [ICL Industrial Products](https://icl-industrialproducts.com/products/sodium-chloride-industrial/) |
