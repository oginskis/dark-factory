# SKU Schema: Nonwoven Fabrics & Felts

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.nonwoven_fabrics_felts`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | PE-15-60, F3-1/4, NW-PP-200 |
| Product Name | product_name | text | Full product name including key specs such as material, weight, and thickness | SAE F-3 Wool Felt 1/4in Grey, Polyester Needlepunch 400 GSM Black |
| URL | url | text | Direct link to the product page | https://example.com/product/sae-f3-wool-felt |
| Price | price | number | Numeric price per unit (per square yard, linear yard, or sheet), excluding currency symbol | 12.50, 28.00, 85.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Fabric Type | fabric_type | enum | Primary nonwoven classification | Needlepunch Felt, Pressed Wool Felt, Spunbond, Spunlace, Meltblown, Wet-Laid, Thermal Bond, Stitch Bond |
| Fiber Type | fiber_type | text | Primary fiber material used | Wool, Polyester, Polypropylene, Nylon, Aramid, Fiberglass, Viscose, Acrylic |
| SAE Grade | sae_grade | text | SAE International felt grade designation for industrial wool felts | F-1, F-3, F-5, F-7, F-10, F-13, F-15, F-26 |
| Country of Origin | country_of_origin | text | Country where the material was manufactured | USA, Germany, China, India |
| Weight | weight | number (GSM) | Mass per unit area in grams per square metre | 68, 200, 500, 1000, 1628 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Fiber Blend | fiber_blend | text | Full fiber composition with percentages where applicable | 95% Wool 5% Polyester, 100% Polyester, 80% Wool 20% Synthetic |
| Thickness | thickness | number (mm) | Material thickness in millimetres | 0.35, 0.5, 1.0, 3.0, 6.35, 12.7, 25.4 |
| Density | density | number (g/cm3) | Bulk density of the material | 0.20, 0.28, 0.32, 0.36, 0.45 |
| Width | width | number (in) | Roll width in inches | 36, 48, 60, 72, 96 |
| Color | color | text | Material color | White, Grey, Black, Natural, Brown, Pink |
| Tensile Strength | tensile_strength | number (psi) | Breaking strength under tension per ASTM D5035 or equivalent | 75, 200, 400, 500 |
| Elongation at Break | elongation_at_break | number (%) | Percentage stretch at the point of failure | 10, 25, 50, 100 |
| Compression Resistance | compression_resistance | number (psi) | Resistance to compression at 10% deflection | 1, 3, 6, 13, 21 |
| Abrasion Resistance | abrasion_resistance | enum | Qualitative rating of resistance to surface wear | Excellent, Good, Fair, Poor |
| Shore A Hardness | shore_a_hardness | text | Hardness measurement on the Shore A scale | 5-15, 15-25, 20-30, 30-40 |
| Air Permeability | air_permeability | number (CFM/ft2) | Airflow rate through the material per unit area | 5, 20, 50, 150, 400 |
| Max Operating Temperature | max_operating_temperature | number (F) | Maximum continuous-use temperature in degrees Fahrenheit | 200, 300, 400, 500, 800 |
| Vibration Damping | vibration_damping | enum | Effectiveness at absorbing vibration | Very Low, Low, Medium, High |
| Adhesive Backing | adhesive_backing | boolean | Whether the material has a pressure-sensitive adhesive layer | true, false |
| Application | application | text (list) | Intended industrial or commercial uses | Filtration, Gaskets, Polishing, Insulation, Packaging, Automotive, Acoustics |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus SAE felt standards | [US Felt](https://www.usfelt.com/sae_felt_specs.html), [Superior Felt & Filtration](https://www.superiorfelt.com/products/), [Sutherland Felt](https://sutherlandfelt.com/materials/polyester-felt/), [Monarch Textiles](https://www.monarchtextiles.com/) |
