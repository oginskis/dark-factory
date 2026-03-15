# SKU Schema: Specialty Chemicals & Catalysts

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products
**Taxonomy ID:** `chemicals.specialty_catalysts`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Supplier catalog number or product identifier | 908126, 330108, KATALCO-51-102, Noblyst-P1159 |
| Product Name | product_name | text | Full product name including active component, support, and loading | Evonik Noblyst P1159 5% Pd on Alumina powder, BASF KATALCO 51-102 Methanol Synthesis Catalyst, Johnson Matthey 5% Palladium on Carbon |
| URL | url | text | Direct link to the product page | https://example.com/catalysts/noblyst-p1159 |
| Price | price | number | Numeric price per package unit excluding currency symbol | 85.00, 350.00, 1250.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Category | product_category | enum | Broad classification of the specialty chemical or catalyst | Heterogeneous Catalyst, Homogeneous Catalyst, Biocatalyst/Enzyme, Metal Scavenger, Adsorbent, Specialty Intermediate, Custom Compound |
| Support Material | support_material | text | Carrier or support material on which the active component is dispersed | Activated Carbon, Alumina (Al2O3), Silica (SiO2), Calcium Carbonate, Titania (TiO2), Zirconia (ZrO2), Zeolite |
| Form | form | enum | Physical form of the catalyst as supplied | Powder, Pellet, Extrudate, Ring, Tablet, Star Extrudate, Sphere, Paste, Gauze, Solution |
| Molecular Formula | molecular_formula | text | Molecular formula for single-compound specialty chemicals or the active phase | Pd, Pt, Ru, NiO, CoO, V2O5/TiO2 |
| Packaging Type | packaging_type | text | Container type used for shipping and storage | Glass bottle, HDPE bottle, Fibre drum, Steel drum, UN-approved container |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the catalyst or specialty chemical was manufactured | Germany, UK, USA, Japan, Belgium, Netherlands |
| CAS Number | cas_number | text | Chemical Abstracts Service registry number for the primary substance or formulation | 7440-05-3 (Pd), 7440-06-4 (Pt), 7440-18-8 (Ru), 7440-16-6 (Rh) |
| Active Metal | active_metal | text (list) | Catalytically active metal or metals in the product | Palladium (Pd), Platinum (Pt), Ruthenium (Ru), Rhodium (Rh), Nickel (Ni), Cobalt (Co), Copper (Cu), Gold (Au), Iron (Fe) |
| Metal Loading | metal_loading | text | Weight percentage of active metal on the support material | 1%, 5%, 10%, 20%, 0.5% Pd + 0.5% Pt |
| Shape Dimensions | shape_dimensions | text (mm) | Characteristic dimensions of formed catalyst shapes | 3x3 mm pellet, 10x4x13 mm ring, 1.5 mm extrudate, 5x5 mm tablet |
| BET Surface Area | bet_surface_area | number (m2/g) | Specific surface area measured by BET nitrogen adsorption method | 50, 150, 250, 800, 1200 |
| Pore Volume | pore_volume | number (mL/g) | Total pore volume of the catalyst or support | 0.20, 0.40, 0.65, 0.90, 1.10 |
| Bulk Density | bulk_density | number (kg/L) | Bulk density of the catalyst in its packed or loose form | 0.35, 0.55, 0.75, 1.10, 1.45 |
| Crush Strength | crush_strength | number (N) | Minimum radial or axial crush strength per individual particle | 20, 40, 60, 100, 150 |
| Moisture Content | moisture_content | text | Residual moisture in the catalyst as delivered, as weight percentage | Less than 3%, 50% water wet (for Pd/C), Less than 5% |
| Water Content State | water_content_state | enum | Whether the catalyst is shipped dry or water-wet for safety | Dry, Water Wet (approximately 50%), Solvent Wet |
| Minimum Operating Temperature | minimum_operating_temperature | number (degC) | Lowest temperature at which the catalyst achieves meaningful activity (ignition temperature) | 150, 200, 340, 380, 410 |
| Maximum Operating Temperature | maximum_operating_temperature | number (degC) | Highest temperature the catalyst can tolerate without permanent deactivation | 250, 400, 500, 630, 900 |
| Application | application | text (list) | Primary catalytic reactions or industrial processes the product is designed for | Hydrogenation, Oxidation, Cross-coupling, Methanol synthesis, Fischer-Tropsch, Ammonia synthesis, Selective catalytic reduction, Ester hydrogenation |
| Selectivity | selectivity | text | Qualitative or quantitative selectivity descriptor for the target reaction | High selectivity to methanol, Greater than 99% ee (enantioselective), Greater than 95% to target product |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (GHS Rev.9, CAS Registry, BET method ISO 9277) | [Evonik](https://catalysts.evonik.com/en/products/brands), [BASF](https://chemical-catalysts-and-adsorbents.basf.com/), [Johnson Matthey](https://matthey.com/products-and-markets/pgms-and-circularity/pgm-chemicals-and-catalysts/catalysts), [Parchem](https://parchem.com/product-specialty-chemicals-catalog/catalysts/catalyst-supplier/rare-metal-catalysts) |
