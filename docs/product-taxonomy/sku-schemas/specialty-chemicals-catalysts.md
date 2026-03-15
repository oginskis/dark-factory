# SKU Schema: Specialty Chemicals & Catalysts

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier catalog number or product identifier | 908126, 330108, KATALCO-51-102, Noblyst-P1159 |
| Product Name | text | Full product name including active component, support, and loading | Evonik Noblyst P1159 5% Pd on Alumina powder, BASF KATALCO 51-102 Methanol Synthesis Catalyst, Johnson Matthey 5% Palladium on Carbon |
| URL | text | Direct link to the product page | https://example.com/catalysts/noblyst-p1159 |
| Price | number | Numeric price per package unit excluding currency symbol | 85.00, 350.00, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Manufacturer or brand name of the catalyst product | Evonik, BASF, Johnson Matthey, Clariant, Haldor Topsoe, Alfa Aesar, Sigma-Aldrich |
| Product Category | enum | Broad classification of the specialty chemical or catalyst | Heterogeneous Catalyst, Homogeneous Catalyst, Biocatalyst/Enzyme, Metal Scavenger, Adsorbent, Specialty Intermediate, Custom Compound |
| CAS Number | text | Chemical Abstracts Service registry number for the primary substance or formulation | 7440-05-3 (Pd), 7440-06-4 (Pt), 7440-18-8 (Ru), 7440-16-6 (Rh) |
| Active Metal | text (list) | Catalytically active metal or metals in the product | Palladium (Pd), Platinum (Pt), Ruthenium (Ru), Rhodium (Rh), Nickel (Ni), Cobalt (Co), Copper (Cu), Gold (Au), Iron (Fe) |
| Metal Loading | text | Weight percentage of active metal on the support material | 1%, 5%, 10%, 20%, 0.5% Pd + 0.5% Pt |
| Support Material | text | Carrier or support material on which the active component is dispersed | Activated Carbon, Alumina (Al2O3), Silica (SiO2), Calcium Carbonate, Titania (TiO2), Zirconia (ZrO2), Zeolite |
| Form | enum | Physical form of the catalyst as supplied | Powder, Pellet, Extrudate, Ring, Tablet, Star Extrudate, Sphere, Paste, Gauze, Solution |
| Shape Dimensions | text (mm) | Characteristic dimensions of formed catalyst shapes | 3x3 mm pellet, 10x4x13 mm ring, 1.5 mm extrudate, 5x5 mm tablet |
| Particle Size/Mesh | text | Particle size range for powders or mesh specification | Less than 50 um, 50-100 um, 100-200 mesh, 3-5 mm, 0.8-1.2 mm |
| BET Surface Area | number (m2/g) | Specific surface area measured by BET nitrogen adsorption method | 50, 150, 250, 800, 1200 |
| Pore Volume | number (mL/g) | Total pore volume of the catalyst or support | 0.20, 0.40, 0.65, 0.90, 1.10 |
| Pore Size | text (nm) | Average or median pore diameter | 5, 10, 20, 50, Microporous (less than 2 nm), Mesoporous (2-50 nm) |
| Bulk Density | number (kg/L) | Bulk density of the catalyst in its packed or loose form | 0.35, 0.55, 0.75, 1.10, 1.45 |
| Crush Strength | number (N) | Minimum radial or axial crush strength per individual particle | 20, 40, 60, 100, 150 |
| Moisture Content | text | Residual moisture in the catalyst as delivered, as weight percentage | Less than 3%, 50% water wet (for Pd/C), Less than 5% |
| Water Content State | enum | Whether the catalyst is shipped dry or water-wet for safety | Dry, Water Wet (approximately 50%), Solvent Wet |
| Minimum Operating Temperature | number (degC) | Lowest temperature at which the catalyst achieves meaningful activity (ignition temperature) | 150, 200, 340, 380, 410 |
| Maximum Operating Temperature | number (degC) | Highest temperature the catalyst can tolerate without permanent deactivation | 250, 400, 500, 630, 900 |
| Application | text (list) | Primary catalytic reactions or industrial processes the product is designed for | Hydrogenation, Oxidation, Cross-coupling, Methanol synthesis, Fischer-Tropsch, Ammonia synthesis, Selective catalytic reduction, Ester hydrogenation |
| Selectivity | text | Qualitative or quantitative selectivity descriptor for the target reaction | High selectivity to methanol, Greater than 99% ee (enantioselective), Greater than 95% to target product |
| Molecular Formula | text | Molecular formula for single-compound specialty chemicals or the active phase | Pd, Pt, Ru, NiO, CoO, V2O5/TiO2 |
| Molecular Weight | number (g/mol) | Molar mass for single-compound specialty chemicals | 106.42, 195.08, 101.07, 74.93 |
| Purity | text | Minimum purity of the active metal or compound expressed as a percentage | 99.9% (metals basis), 99.95%, 99.99%, 97% |
| GHS Hazard Pictograms | text (list) | Globally Harmonized System hazard pictogram codes | GHS02 Flame, GHS07 Exclamation Mark, GHS08 Health Hazard, GHS09 Environment |
| Signal Word | enum | GHS signal word indicating severity of hazard | Danger, Warning |
| Hazard Statements | text (list) | GHS H-code hazard statements applicable to the product | H228 Flammable solid, H315 Causes skin irritation, H317 May cause allergic skin reaction, H412 Harmful to aquatic life |
| Packaging Size | text | Available package quantities | 5 g, 25 g, 100 g, 500 g, 1 kg, 5 kg, 25 kg, Drum, Bulk |
| Packaging Type | text | Container type used for shipping and storage | Glass bottle, HDPE bottle, Fibre drum, Steel drum, UN-approved container |
| Storage Conditions | text | Recommended storage environment | Store under inert gas, Store in dry location below 25 degC, Keep water-wet catalyst sealed to prevent drying |
| Shelf Life | text | Recommended maximum storage period from date of manufacture | 12 months, 24 months, 36 months |
| Country of Origin | text | Country where the catalyst or specialty chemical was manufactured | Germany, UK, USA, Japan, Belgium, Netherlands |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (GHS Rev.9, CAS Registry, BET method ISO 9277) | [Evonik](https://catalysts.evonik.com/en/products/brands), [BASF](https://chemical-catalysts-and-adsorbents.basf.com/), [Johnson Matthey](https://matthey.com/products-and-markets/pgms-and-circularity/pgm-chemicals-and-catalysts/catalysts), [Parchem](https://parchem.com/product-specialty-chemicals-catalog/catalysts/catalyst-supplier/rare-metal-catalysts) |
