# SKU Schema: Refractory Products & Technical Ceramics

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.refractory_technical_ceramics`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | SG-HEX-SA80, ZRCI-RS100, AE-AL2O3-PLATE |
| Product Name | product_name | text | — | yes | Full product name including material, shape, and key specs | Hexoloy SA Silicon Carbide Beam 50x50x600mm, Alumina 99.5% Crucible 100ml |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/sic-beam-50x50x600 |
| Price | price | number | — | yes | Numeric price per unit excluding currency symbol | 245.00, 89.50, 1200.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Material Composition | material_composition | text | — | — | Primary ceramic or refractory material | Silicon Carbide (SiC), Alumina (Al2O3), Zirconia (ZrO2), Mullite, Boron Nitride (BN) |
| Product Form | product_form | enum | — | — | Physical shape category of the product | Brick, Tube, Plate, Crucible, Roller, Setter, Sagger, Beam, Castable, Mortar |
| Bond Type | bond_type | text | — | — | Bonding system used in the refractory product | Fired, Chemically Bonded, Resin Bonded, Phosphate Bonded, Cement Bonded |
| Grade | grade | text | — | — | Manufacturer quality or purity grade designation | Standard, Premium, High Purity, Technical, Industrial |
| Insulating Class | insulating_class | text | — | — | Classification of insulating refractory by temperature rating per ASTM C155 | IFB-20, IFB-23, IFB-26, IFB-28, IFB-30 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | Germany, USA, China, India, Japan |
| Alumina Content | alumina_content | number | % | — | Percentage of alumina in the product where applicable | 70, 85, 96, 99.5 |
| Maximum Service Temperature | maximum_service_temperature | number | C | — | Maximum continuous operating temperature in degrees Celsius | 1260, 1400, 1650, 1800, 2200 |
| Bulk Density | bulk_density | number | g/cm3 | — | Mass per unit volume of the product | 1.80, 2.50, 3.10, 3.85 |
| Apparent Porosity | apparent_porosity | number | % | — | Volume percentage of open pores in the material | 5, 15, 22, 30 |
| Thermal Conductivity | thermal_conductivity | number | W/mK | — | Rate of heat transfer through the material at specified temperature | 1.2, 3.5, 15.0, 120.0 |
| Cold Crushing Strength | cold_crushing_strength | number | MPa | — | Compressive strength measured at room temperature | 20, 55, 120, 350 |
| Modulus of Rupture | modulus_of_rupture | number | MPa | — | Flexural strength at room temperature | 5, 12, 35, 400 |
| Thermal Shock Resistance | thermal_shock_resistance | text | — | — | Resistance to damage from rapid temperature changes | Excellent, Good, Moderate, Poor |
| Dimensions | dimensions | text | mm | — | Physical dimensions as length x width x height or diameter x length | 230x114x65, 50x50x600, OD60xID40x300 |
| Application | application | text (list) | — | — | Primary intended industrial applications | Kiln Furniture, Furnace Lining, Blast Furnace, Glass Melting, Crucible, Filtration |
| Industry Sector | industry_sector | text | — | — | Target industry for the product | Steel, Aluminum, Glass, Ceramics, Petrochemical, Cement |
| Chemical Resistance | chemical_resistance | text | — | — | Resistance to specific chemical environments | Acid Resistant, Alkali Resistant, Slag Resistant, Metal Resistant |
| Standard Compliance | standard_compliance | text (list) | — | — | Relevant industry standards the product meets | ASTM C155, ASTM C401, ISO 10081, EN 993, DIN 51060 |
| Refractoriness Under Load | refractoriness_under_load | number | C | — | Temperature at which deformation begins under standard load | 1300, 1450, 1600, 1750 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (ASTM C155, ASTM C401, ISO 10081, EN 993) | [Saint-Gobain Performance Ceramics & Refractories](https://www.ceramicsrefractories.saint-gobain.com/products), [Edgetech Industries](https://www.eticeramics.com/refractory-ceramics/), [Vesuvius](https://www.vesuvius.com/en/our-solutions/en-us/foundry/non-ferrous-foundry/crucibles-refractories-and-ceramics.html), [American Elements](https://www.americanelements.com/refractory-ceramics) |
