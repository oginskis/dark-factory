# SKU Schema: Specialty Papers (Filter, Thermal, Coated)

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.specialty_papers`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | KOE-KT48PF, WHT-1001-090, DOM-TP55, AHL-613 |
| Product Name | product_name | text | — | yes | Full product name including paper type, grade, and key specs | Koehler KT48-PF Phenol-Free Thermal Paper 48gsm, Whatman Grade 1 Qualitative Filter Paper 90mm |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/koehler-kt48-pf-thermal |
| Price | price | number | — | yes | Numeric price per roll, per pack, or per ream excluding currency symbol | 12.50, 45.00, 285.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Specialty Type | specialty_type | enum | — | — | Primary specialty paper classification | Thermal POS, Thermal Label, Qualitative Filter, Quantitative Filter, Coated Glossy, Coated Matte, Carbonless, Security, Transfer |
| Coating Type | coating_type | text | — | — | Functional coating applied to the paper surface | Thermal Sensitive, Clay Coated, Silicone Release, Polyethylene, Wax, None |
| Filter Paper Type | filter_paper_type | enum | — | — | Classification of filter paper by application | Qualitative, Quantitative (Ashless), Hardened, Technical/Industrial |
| Supply Form | supply_form | enum | — | — | How the product is packaged and supplied | Sheets, Rolls, Circles, Jumbo Rolls, Reams, Packs |
| Country of Origin | country_of_origin | text | — | — | Country where the paper was manufactured | Germany, Finland, Japan, USA, China |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Caliper | caliper | number | um | — | Thickness per sheet in micrometres | 48, 55, 62, 75, 95, 120, 180 |
| Topcoat | topcoat | boolean | — | — | Whether an additional protective topcoat is applied over the functional coating | true, false |
| Thermal Sensitivity | thermal_sensitivity | enum | — | — | Speed of image development for thermal papers (higher = faster printing) | Standard (x), Medium (xx), High (xxx), Maximum (xxxx) |
| Image Durability | image_durability | text | — | — | Expected readable life of the thermal image under normal storage | 5 years, 7 years, 10 years, 25 years |
| Phenol Free | phenol_free | boolean | — | — | Whether the thermal coating is free of BPA, BPS, and all phenol developers | true, false |
| Filtration Speed | filtration_speed | enum | — | — | Relative flow rate through the filter paper | Slow, Medium, Medium-Fast, Fast, Very Fast |
| Wet Strength | wet_strength | text | — | — | Whether the paper retains integrity when wet, important for filter papers | High, Medium, Low |
| Ash Content | ash_content | number | % | — | Residual ash after ignition, critical for quantitative filter papers | 0.007, 0.01, 0.06, 0.1 |
| Gloss Level | gloss_level | number | % | — | Surface gloss measured at 75 degrees for coated papers | 10, 30, 50, 70, 85 |
| Smoothness | smoothness | number | Bekk s | — | Surface smoothness for coated papers measured in Bekk seconds | 30, 100, 300, 600, 1200 |
| Sheets/Units per Pack | sheetsunits_per_pack | number | — | — | Number of sheets, circles, or rolls in a standard retail pack | 50, 100, 200, 500, 6, 50 |
| Opacity | opacity | number | % | — | Percentage of light blocked, indicating show-through resistance | 85, 90, 94, 97 |
| Brightness | brightness | number | % | — | ISO or GE brightness of the paper surface | 80, 88, 92, 96 |
| Print Method Compatibility | print_method_compatibility | text (list) | — | — | Printing or imaging processes the paper is designed for | Direct Thermal, Thermal Transfer, Offset, Gravure, Flexography, Digital |
| Chemical Compatibility | chemical_compatibility | text | — | — | Resistance to specific chemicals, important for filter and industrial papers | Acid Resistant, Alkali Resistant, Solvent Resistant |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISO 536, ISO 2470, TAPPI, Whatman grade system) | [Koehler Paper](https://www.koehlerpaper.com/en/products/Thermal-paper/), [Jujo Thermal](https://www.jujothermal.com/products/thermal-papers/), [Whatman/Cytiva](https://www.cytivalifesciences.com/en/us/insights/a-guide-to-whatman-filter-paper-grades), [Domtar](https://www.domtar.com/our-product/thermal-coated-pos-papers/) |
