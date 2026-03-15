# SKU Schema: Specialty Papers (Filter, Thermal, Coated)

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | KOE-KT48PF, WHT-1001-090, DOM-TP55, AHL-613 |
| Product Name | text | Full product name including paper type, grade, and key specs | Koehler KT48-PF Phenol-Free Thermal Paper 48gsm, Whatman Grade 1 Qualitative Filter Paper 90mm |
| URL | text | Direct link to the product page | https://example.com/product/koehler-kt48-pf-thermal |
| Price | number | Numeric price per roll, per pack, or per ream excluding currency symbol | 12.50, 45.00, 285.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Specialty paper manufacturer or brand | Koehler Paper, Jujo Thermal, Whatman/Cytiva, Ahlstrom, Domtar, Sappi, Mitsubishi HiTec Paper |
| Specialty Type | enum | Primary specialty paper classification | Thermal POS, Thermal Label, Qualitative Filter, Quantitative Filter, Coated Glossy, Coated Matte, Carbonless, Security, Transfer |
| Basis Weight | number (gsm) | Weight in grams per square metre | 44, 48, 55, 65, 70, 80, 90, 115, 150 |
| Caliper | number (um) | Thickness per sheet in micrometres | 48, 55, 62, 75, 95, 120, 180 |
| Coating Type | text | Functional coating applied to the paper surface | Thermal Sensitive, Clay Coated, Silicone Release, Polyethylene, Wax, None |
| Topcoat | boolean | Whether an additional protective topcoat is applied over the functional coating | true, false |
| Thermal Sensitivity | enum | Speed of image development for thermal papers (higher = faster printing) | Standard (x), Medium (xx), High (xxx), Maximum (xxxx) |
| Image Durability | text | Expected readable life of the thermal image under normal storage | 5 years, 7 years, 10 years, 25 years |
| Phenol Free | boolean | Whether the thermal coating is free of BPA, BPS, and all phenol developers | true, false |
| Pore Size | number (um) | Particle retention rating for filter papers | 2.5, 5, 8, 11, 20, 25 |
| Filtration Speed | enum | Relative flow rate through the filter paper | Slow, Medium, Medium-Fast, Fast, Very Fast |
| Wet Strength | text | Whether the paper retains integrity when wet, important for filter papers | High, Medium, Low |
| Ash Content | number (%) | Residual ash after ignition, critical for quantitative filter papers | 0.007, 0.01, 0.06, 0.1 |
| Filter Paper Type | enum | Classification of filter paper by application | Qualitative, Quantitative (Ashless), Hardened, Technical/Industrial |
| Gloss Level | number (%) | Surface gloss measured at 75 degrees for coated papers | 10, 30, 50, 70, 85 |
| Smoothness | number (Bekk s) | Surface smoothness for coated papers measured in Bekk seconds | 30, 100, 300, 600, 1200 |
| Sheet/Roll Size | text | Product dimensions — diameter for filter circles, width for rolls, sheet size for cut paper | 45mm, 90mm, 110mm, 57mmx50m, 80mmx80m, A4, 8.5x11 |
| Supply Form | enum | How the product is packaged and supplied | Sheets, Rolls, Circles, Jumbo Rolls, Reams, Packs |
| Sheets/Units per Pack | number | Number of sheets, circles, or rolls in a standard retail pack | 50, 100, 200, 500, 6, 50 |
| Opacity | number (%) | Percentage of light blocked, indicating show-through resistance | 85, 90, 94, 97 |
| Brightness | number (%) | ISO or GE brightness of the paper surface | 80, 88, 92, 96 |
| Print Method Compatibility | text (list) | Printing or imaging processes the paper is designed for | Direct Thermal, Thermal Transfer, Offset, Gravure, Flexography, Digital |
| Chemical Compatibility | text | Resistance to specific chemicals, important for filter and industrial papers | Acid Resistant, Alkali Resistant, Solvent Resistant |
| Certification | text (list) | Environmental and quality certifications | FSC, PEFC, BPA-Free, EU Ecolabel, Nordic Swan, FDA Food Contact |
| Country of Origin | text | Country where the paper was manufactured | Germany, Finland, Japan, USA, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISO 536, ISO 2470, TAPPI, Whatman grade system) | [Koehler Paper](https://www.koehlerpaper.com/en/products/Thermal-paper/), [Jujo Thermal](https://www.jujothermal.com/products/thermal-papers/), [Whatman/Cytiva](https://www.cytivalifesciences.com/en/us/insights/a-guide-to-whatman-filter-paper-grades), [Domtar](https://www.domtar.com/our-product/thermal-coated-pos-papers/) |
