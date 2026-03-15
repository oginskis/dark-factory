# SKU Schema: Packaging Tape, Strapping & Cushioning

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | S-423, 372, IPG-HM-2x110 |
| Product Name | text | Full product name including key specs such as type, width, and adhesive | 3M Scotch 372 Performance Box Sealing Tape 48mm x 50m, Polyester Strapping 1/2 in x 3250 ft, Bubble Cushioning Roll 12 in x 175 ft |
| URL | text | Direct link to the product page | https://example.com/product/box-sealing-tape-372 |
| Price | number | Numeric price per unit or per roll/case excluding currency symbol | 4.29, 58.50, 124.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that manufactures the product | 3M, Shurtape, IPG, Signode, Samuel Strapping, Sealed Air |
| Product Type | enum | High-level product category | Carton Sealing Tape, Strapping, Bubble Cushioning, Foam Wrap, Stretch Film, Dunnage Bag, Edge Protector, Masking Tape, Filament Tape |
| Material | text | Primary backing or body material | Polypropylene (BOPP), Polyester (PET), Steel, Polyethylene Foam, Polyethylene Bubble, Vinyl, Paper |
| Adhesive Type | text | Type of adhesive applied to the tape | Hot Melt, Acrylic, Natural Rubber, Solvent-Based, Water-Activated, None |
| Width | number (mm) | Width of the tape, strapping, or cushioning roll | 12, 19, 48, 72, 300 |
| Length | number (m) | Length per roll or sheet | 50, 66, 100, 914, 1000 |
| Thickness | number (mil) | Total thickness of backing plus adhesive layer, measured in mils (thousandths of an inch) | 1.6, 2.0, 2.6, 3.1 |
| Tensile Strength | number (N/mm) | Force per unit width required to break the tape or strapping | 80, 140, 250, 530 |
| Elongation at Break | number (%) | Percentage the material stretches before breaking | 120, 160, 25, 6 |
| Adhesion to Steel | number (N/25mm) | Peel adhesion strength measured on a steel surface | 4.5, 8.0, 12.0 |
| Break Strength | number (kg) | Maximum load the strapping can bear before breaking | 135, 270, 580, 900 |
| Core Size | number (mm) | Inner diameter of the roll core | 38, 76, 406 |
| Color | text | Product color | Clear, Tan, Brown, White, Black, Red |
| Noise Level | enum | Sound level produced during dispensing (primarily for packaging tape) | Standard, Low Noise, Silent |
| Temperature Range | text | Operating or application temperature range | -20C to 60C, 5C to 40C |
| Rolls per Case | number | Number of rolls or units per case or carton | 6, 12, 24, 36 |
| Bubble Size | text | Diameter of bubbles in cushioning material | Small (3/16 in), Medium (5/16 in), Large (1/2 in) |
| Density | number (kg/m3) | Foam density for cushioning products | 25, 33, 45 |
| Cushioning Thickness | number (mm) | Thickness of foam or bubble layer | 3, 5, 10, 25, 50 |
| Dispensing Method | text | How the product is applied | Hand Dispenser, Machine Applied, Self-Dispensing, Manual Tensioner |
| Water Resistance | boolean | Whether the product resists moisture penetration | true, false |
| Certification | text (list) | Regulatory or industry certifications | RoHS, REACH, UL, ISTA Certified |
| Country of Origin | text | Country where the product is manufactured | USA, Germany, China, Italy, India |
| Recyclable | boolean | Whether the material is recyclable | true, false |
| MOQ | number | Minimum order quantity (rolls or cases) | 1, 6, 36, 100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 28 attributes from 4 companies plus industry standards (ASTM D5330, ASTM D3950) | [US Packaging and Wrapping](https://uspackagingandwrapping.com/packing-tape-101.html), [IPG (Intertape Polymer Group)](https://www.itape.com/), [Shorr Packaging](https://www.shorr.com/packaging-products/tapes-adhesives/), [Shurtape](https://www.shurtape.com/markets/specialty-tapes/made-in-usa/) |
