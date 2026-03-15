# SKU Schema: Dyes & Pigments

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | P11255, 546127, L4763, DX-0021 |
| Product Name | text | Full product name including brand, trade name, color index, or grade | Hostaperm Fast Yellow 180, Irgalite Maroon L4763, Dianix Red S-B, Indanthren Blue RSN |
| URL | text | Direct link to the product page | https://example.com/product/hostaperm-yellow-180 |
| Price | number | Numeric price per sales unit (kg, g, lb, or each), excluding currency symbol | 45.00, 285.00, 12.50, 3200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, INR |
| Brand/Manufacturer | text | Company that produces or markets the product | BASF, Sun Chemical, DyStar, Clariant, Huntsman, DIC, Lanxess, Sigma-Aldrich |
| Product Line | text | Named trade series within the brand | Hostaperm, Cromophtal, Lumogen, Dianix, Levafix, Remazol, Sunfast, Irgalite |
| Product Class | enum | Top-level classification as a dye or pigment | Organic Pigment, Inorganic Pigment, Reactive Dye, Disperse Dye, Vat Dye, Acid Dye, Metal Complex Dye, Direct Dye, Cationic Dye, Fluorescent Dye |
| Chemical Class | text | Chemical structural class of the colorant | Azo, Anthraquinone, Phthalocyanine, Quinacridone, Perylene, Diketopyrrolo-pyrrole, Iron Oxide, Titanium Dioxide, Carbon Black |
| Color Index Name | text | Standardized name assigned by the Colour Index International system | Pigment Red 52:2, Pigment Blue 15:3, Reactive Blue 19, Disperse Yellow 42, Pigment Black 7 |
| Color Index Number | text | Five-digit numeric Colour Index constitution number | 15865, 74160, 61200, 77891 |
| CAS Number | text | Chemical Abstracts Service registry number uniquely identifying the substance | 128-69-8, 81-88-9, 13463-67-7, 147-14-8 |
| Molecular Formula | text | Empirical formula of the active colorant | C24H8O6, C28H31ClN2O3, C32H16CuN8, C37H34N2Na2O9S3 |
| Molecular Weight | number (g/mol) | Molar mass of the colorant molecule | 392.32, 479.01, 576.07, 696.66 |
| Color/Shade | text | Visual color description or shade designation as sold | Yellow, Red, Blue, Green, Black, Maroon, Violet, Orange |
| Physical Form | enum | Form in which the product is sold | Powder, Granule, Liquid Dispersion, Paste, Presscake, Chip, Pellet, Solution |
| Lightfastness | text | Resistance to fading on exposure to light, typically Blue Wool Scale 1-8 or ASTM rating | 7, 8, Excellent, Good, ASTM 5 |
| Heat Stability | text | Maximum temperature the colorant can withstand without significant color shift | 180 C, 200 C, 280 C, 300 C |
| Weather Resistance | text | Resistance to outdoor weathering rated on a qualitative or standard scale | Excellent, Very Good, Good, Fair, 5 (ISO scale) |
| Tinting Strength | text | Relative strength of coloration compared to a standard, expressed as a percentage or qualitative grade | 100%, 105%, High, Standard |
| Specific Gravity | number | Density of the colorant relative to water | 1.30, 1.60, 2.20, 4.10 |
| Oil Absorption | number (g/100g) | Grams of oil required to wet 100 grams of pigment | 25, 40, 55, 80, 120 |
| Particle Size | text (microns) | Median or range of particle size in the supplied form | 0.1-0.5, 0.3, 1-5, less than 1 |
| pH Value | text | Acidity or alkalinity of the product in aqueous dispersion | 6.5-7.5, 7.0, 8.0-9.0, 5.0-6.0 |
| Fiber/Substrate Compatibility | text (list) | Materials the dye or pigment is designed to color | Cellulose, Polyester, Polyamide, Wool, Acrylic, Plastics, Coatings, Inks, Paper, Leather |
| Application Method | text (list) | How the dye or pigment is applied to the substrate | Exhaust Dyeing, Continuous Dyeing, Textile Printing, Dispersion Milling, Dry Blending, Spin Dyeing |
| Container Size | text | Volume or weight of the sales unit | 5 g, 25 g, 1 kg, 25 kg bag, 500 kg IBC |
| Dye Content | number (%) | Percentage of active colorant in the commercial product | 25, 40, 75, 99 |
| Regulatory Compliance | text (list) | Safety, environmental, and restricted-substance compliance | REACH, OEKO-TEX, bluesign, GOTS, RSL compliant, RoHS, FDA approved |
| Solubility | text | Solubility characteristics in common media | Insoluble in water, Soluble in water, Soluble in organic solvents, Dispersible |
| Country of Origin | text | Country where the product is manufactured | Germany, India, China, USA, Japan, Switzerland |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (Colour Index International, ISO pigment test methods, OEKO-TEX) | [BASF Pigments](https://aerospace.basf.com/high-performance-pigments.html), [DyStar](https://www.dystar.com/textile-dyes-pigments/), [Sun Chemical](https://www.sunchemical.com/color-materials/), [Sigma-Aldrich](https://www.sigmaaldrich.com/US/en/substance/ptcda39232128698) |
