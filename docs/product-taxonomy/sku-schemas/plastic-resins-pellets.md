# SKU Schema: Plastic Resins & Pellets

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or supplier product identifier (often the grade name) | DOW-DMDA-8904, CPChem-HHM-TR144, PPR-HDPE-VN-01 |
| Product Name | text | Full product name including resin type, grade, and key property descriptors | Dow DMDA-8904 NT7 HDPE Blow Molding Resin, Marlex HHM TR-144 High Molecular Weight HDPE, Tipelin BA 550-13 HDPE |
| URL | text | Direct link to the product page or technical data sheet | https://example.com/products/hdpe-blow-molding-8904 |
| Price | number | Numeric price per unit (per kg, per lb, or per MT), excluding currency symbol | 1.15, 1450.00, 2.30 |
| Currency | text | ISO 4217 currency code | USD, EUR, CNY, INR |
| Brand/Manufacturer | text | Resin producer or distributor name | Dow, Chevron Phillips Chemical, LyondellBasell, SABIC, ExxonMobil, INEOS, Borealis, KW Plastics |
| Polymer Type | enum | Base polymer classification | HDPE, LDPE, LLDPE, MDPE, PP Homopolymer, PP Copolymer, PS, GPPS, HIPS, PET, ABS, PC, PA (Nylon), POM (Acetal), PVC, TPE, TPU |
| Resin Grade Name | text | Manufacturer-assigned grade or trade name | DMDA-8904, Marlex HHM TR-144, Tipelin BA 550-13, SABIC HDPE B5429 |
| Resin Category | enum | Functional classification of the resin | Commodity, Engineering, High Performance, Recycled (PCR), Recycled (PIR), Bio-based |
| Virgin vs Recycled | enum | Whether the resin is virgin, post-consumer recycled, or post-industrial recycled | Virgin, PCR (Post-Consumer Recycled), PIR (Post-Industrial Recycled), Ocean-Bound, Regrind |
| Physical Form | enum | Form in which the resin is supplied | Pellets, Granules, Powder, Flakes, Bales |
| Melt Flow Rate | number (g/10min) | Melt flow index measured at standard conditions per ISO 1133 or ASTM D1238 | 0.3, 1.0, 4.0, 12.0, 25.0, 50.0 |
| MFR Test Conditions | text | Temperature and load used for MFR measurement | 190 degC / 2.16 kg, 190 degC / 5 kg, 230 degC / 2.16 kg, 190 degC / 21.6 kg |
| Density | number (g/cm3) | Resin density measured per ASTM D792 or ISO 1183 | 0.918, 0.935, 0.954, 0.960, 1.05, 1.20, 1.40 |
| Tensile Strength at Yield | number (MPa) | Tensile strength at yield per ASTM D638 or ISO 527 | 10, 21, 28, 38, 60, 80 |
| Flexural Modulus | number (MPa) | Stiffness measured per ASTM D790 or ISO 178 | 200, 800, 1200, 1500, 2500, 3000 |
| Impact Strength (Izod) | number (J/m) | Notched Izod impact strength per ASTM D256 | 20, 50, 100, 200, 800, NB (no break) |
| Heat Deflection Temperature | number (degC) | HDT at 0.45 MPa per ASTM D648 or ISO 75 | 40, 65, 80, 105, 130, 260 |
| Vicat Softening Point | number (degC) | Temperature at which a flat-ended needle penetrates the specimen | 80, 100, 125, 150 |
| ESCR | number (hours) | Environmental stress crack resistance per ASTM D1693 or ISO 22088 | 24, 100, 300, 1000, greater than 1000 |
| Processing Method | text (list) | Recommended processing technologies | Injection Molding, Blow Molding, Film Extrusion, Sheet Extrusion, Pipe Extrusion, Rotational Molding, Fiber Spinning, Thermoforming |
| Color | text | Color of the resin as supplied | Natural, White, Black, Custom |
| Pellet Size | number (mm) | Typical pellet diameter or granule size | 2.0, 3.0, 3.5, 4.0, 5.0 |
| Application | text (list) | Primary intended end-use applications | Bottles, Film, Pipe, Automotive Parts, Packaging, Containers, Caps and Closures, Wire and Cable, Geomembranes |
| Additive Content | text | Pre-compounded additives included in the resin | UV Stabilizer, Antioxidant, Slip Agent, Anti-Block, Nucleating Agent, Flame Retardant, Antistatic |
| FDA Compliance | enum | Whether the resin meets FDA food-contact regulations (21 CFR) | Yes, No, Specific grades only |
| Packaging | text | Packaging options for the resin product | 25 kg bags, 1000 kg bulk bags (FIBC), Railcar, Hopper truck, Gaylord box, Octabin |
| Country of Origin | text | Country where the resin was manufactured | USA, Germany, Saudi Arabia, South Korea, Belgium, China, India |
| Certification | text (list) | Quality, safety, or regulatory certifications | ISO 9001, ISO 14001, UL recognized, REACH, RoHS, FDA 21 CFR, EU 10/2011 |
| Minimum Order Quantity | text | Minimum purchase quantity | 25 kg, 500 kg, 1 MT, 20 MT, Truckload |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM D1238, ASTM D792, ISO 1133, ISO 1183) | [Dow HDPE](https://www.dow.com/en-us/product-technology/pt-polyethylene/pg-polyethylene-hdpe.html), [Chevron Phillips Polyethylene](https://www.cpchem.com/what-we-do/solutions/polyethylene/products), [Premier Plastic Resins](https://premierplasticresins.com/), [MOL Group HDPE Catalog](https://molgroupchemicals.com/userfiles/catalog/hdpe/HDPE_2024-EN.pdf) |
