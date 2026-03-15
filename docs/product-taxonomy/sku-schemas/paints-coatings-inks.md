# SKU Schema: Paints, Coatings & Inks

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | B30W12650, 9794, AR-EP-100 |
| Product Name | text | Full product name including key identifiers such as brand, product line, and type | ProMar 200 Zero VOC Interior Latex Flat, Jotamastic 90 Aluminium, PPG Envirocron Powder Coating |
| URL | text | Direct link to the product page | https://example.com/product/promar-200-flat |
| Price | number | Numeric price per unit (gallon, litre, kg, or each depending on seller), excluding currency symbol | 42.99, 185.00, 12.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Brand | text | Manufacturer or brand name | Sherwin-Williams, PPG, Jotun, AkzoNobel, BASF, Hempel |
| Product Line | text | Named product series or collection within the brand | ProMar 200, Penguard, Interchar, Sigma, Jotashield |
| Product Type | enum | Primary classification of the coating product | Paint, Primer, Topcoat, Undercoat, Varnish, Lacquer, Stain, Ink, Powder Coating, Sealer |
| Coating Function | text (list) | Intended protective or decorative purpose | Anticorrosion, Antifouling, Fire Protection, Decorative, Abrasion Resistant, Chemical Resistant |
| Resin/Binder Type | text | Chemistry of the primary binder system | Epoxy, Alkyd, Polyurethane, Acrylic, Silicone, PVDF, Polyester, Vinyl, Chlorinated Rubber |
| Pigment Type | text | Type or class of pigment used | Titanium Dioxide, Zinc Phosphate, Iron Oxide, Aluminium, Carbon Black, Phthalocyanine |
| Finish/Sheen | enum | Gloss or sheen level of the dried film | Flat, Matte, Eggshell, Satin, Semi-Gloss, Gloss, High Gloss |
| Color | text | Color name or code as stated by the manufacturer | Extra White, Deep Base, RAL 7035, Safety Yellow, Custom Tint |
| Color System | text | Tinting or color matching system used | Tintable Base, Factory Mixed, RAL, NCS, Pantone, Custom Match |
| Volume Solids | number (%) | Percentage of film-forming material by volume remaining after drying | 45, 62, 78, 98 |
| VOC Content | number (g/L) | Volatile organic compound content in grams per litre | 0, 50, 100, 250, 340 |
| Specific Gravity | number | Density of the liquid product relative to water | 1.15, 1.35, 1.62, 2.10 |
| Recommended DFT | text (microns) | Recommended dry film thickness per coat in micrometres | 50-80, 75-125, 150-200, 60-80 |
| Spreading Rate | text | Theoretical coverage area per unit volume at recommended thickness | 6-8 m2/L, 200-400 sq ft/gal, 4.5 m2/L |
| Number of Components | enum | Number of parts that must be mixed before application | 1, 2, 3 |
| Dry Time Touch | text | Time to touch dry under standard conditions | 30 min, 2 h, 4 h, 6 h |
| Dry Time Hard | text | Time to hard dry or full cure under standard conditions | 24 h, 7 days, 30 days |
| Recoat Interval | text | Minimum and maximum time between coats | 4-48 h, 16 h min, 8-24 h |
| Application Method | text (list) | Recommended methods for applying the coating | Airless Spray, Brush, Roller, Conventional Spray, Dip, Electrostatic, Curtain Coating |
| Application Temperature Range | text | Ambient temperature range for proper application | 10-35 C, 50-95 F, 5-40 C |
| Substrate Compatibility | text (list) | Surfaces the product is designed to coat | Steel, Concrete, Wood, Aluminium, Galvanised Steel, Plaster, Drywall |
| Interior/Exterior Use | enum | Whether the product is rated for indoor, outdoor, or both | Interior, Exterior, Interior/Exterior |
| Container Size | text | Volume or weight of the sales unit | 1 gal, 5 gal, 1 L, 20 L, 200 L, 25 kg |
| Flash Point | text | Lowest temperature at which vapors ignite in the presence of an ignition source | 23 C, 38 C, 61 C, Non-flammable |
| Shelf Life | text | Maximum storage duration under recommended conditions from date of manufacture | 12 months, 24 months, 36 months |
| Pot Life | text | Usable working time after mixing for multi-component products | 2 h, 4 h, 8 h, Not applicable |
| Certifications | text (list) | Regulatory and industry certifications or compliance marks | ISO 12944, NORSOK M-501, IMO PSPC, CE, MPI, USDA |
| Hazard Class | text | Transport or storage hazard classification | Flammable Liquid Class 3, Non-hazardous, PG II |
| Country of Origin | text | Country where the product is manufactured | USA, UK, Norway, Germany, Netherlands |
| Manufacturer Part Number | text | Manufacturer-assigned product code distinct from retailer SKU | A80W08251, 17634, INP-399ABR |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (ISO 12944, ASTM paint standards, PPG PDS format) | [Sherwin-Williams](https://www.sherwin-williams.com/painting-contractors/products/promar-200-zero-voc-interior-latex), [PPG](https://www.ppgpaints.com/architects-and-specifiers/specifications), [Jotun](https://www.jotun.com/us/en/b2b/technical-info/), [AkzoNobel International Paint](https://aerospace.akzonobel.com/en/products) |
