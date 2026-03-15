# SKU Schema: Metal Cans & Closures

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | TRV-FD-307x409, TC-70G-CT, OBK-MT-16OZ |
| Product Name | text | Full product name including capacity, material, and format | 307x409 3-Piece Steel Food Can, 70G Tinplate Continuous Thread Closure, 16 oz Aluminum Beverage Can 202/211 |
| URL | text | Direct link to the product page | https://example.com/cans/307x409-food-can |
| Price | number | Numeric price per unit or per thousand, excluding currency symbol | 0.06, 0.12, 85.00, 250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CNY |
| Brand/Manufacturer | text | Company producing or distributing the metal can or closure | Trivium Packaging, Crown Holdings, Ball Corporation, Ardagh Metal Packaging, Tecnocap, Silgan |
| Product Category | enum | Broad classification of the metal packaging item | Food Can, Beverage Can, Aerosol Can, General Line Can, Closure/End, Metal Bottle, Paint Can, Drum |
| Can Construction | enum | Number of body pieces in the can | 2-Piece (Drawn and Ironed), 2-Piece (Draw-Redraw), 3-Piece (Welded Side Seam), 3-Piece (Soldered) |
| Body Material | enum | Primary metal used for the can body | Tinplate (ETP), Tin-Free Steel (TFS/ECCS), Aluminum Alloy, Chrome-Plated Steel |
| Body Material Thickness | number (mm) | Thickness of the body wall material | 0.15, 0.18, 0.20, 0.23, 0.28, 0.30 |
| End Material | enum | Metal used for the can top and bottom ends | Tinplate, Tin-Free Steel, Aluminum |
| End Diameter | number (mm) | Nominal diameter of the can end expressed in standard can-maker notation or millimetres | 52.3, 58, 65, 68.3, 73, 83, 99, 153 |
| Can Diameter | number (mm) | Nominal outside body diameter of the can | 52.3, 65.3, 73.0, 83.4, 99.0, 153.0, 211.0 |
| Can Height | number (mm) | Overall height of the filled and seamed can | 50, 70, 95, 113, 122, 133, 178 |
| Nominal Capacity | number (mL) | Stated volume capacity of the can | 150, 250, 330, 355, 400, 500, 750, 2840 |
| Can Size Code | text | Industry-standard numeric designation using diameter-by-height notation | 202x308, 211x400, 300x407, 307x409, 307x512, 401x411, 603x700 |
| Interior Coating/Lining | enum | Type of internal protective coating applied to the can body and ends | Epoxy, Polyester, BPA-NI (BPA Non-Intent), Oleoresin, Vinyl, Unlined |
| Exterior Coating | enum | Protective or decorative coating on the can exterior | Litho-Printed, White Coated, Clear Lacquer, Uncoated, Matte Finish |
| Printing | text | Description of decoration applied to the can exterior | Undecorated, 4-Color Litho, 6-Color Litho, Shrink Sleeve, Paper Label, Embossed |
| End/Closure Type | enum | Style of the can end or closure mechanism | Standard Double Seam, Easy-Open (EOE), Ring-Pull, Stay-On Tab (SOT), Peel-Off, Twist-Off (Lug), Continuous Thread (CT), Press-On Twist-Off (PT), Pilfer-Proof (ROPP) |
| Retort Capability | enum | Whether the can is designed to withstand thermal retort processing (121C+) | Yes, No |
| Vacuum Pack | enum | Whether the can is designed for vacuum-packed contents | Yes, No |
| Pressure Rating | number (bar) | Maximum internal pressure the can is rated to withstand for carbonated or aerosol products | 0, 3.5, 6.2, 10, 18 |
| Shelf Life Support | text | Typical shelf life the packaging is designed to provide | 1 year, 2 years, 3 years, 5 years |
| Stacking Strength | number (kg) | Maximum load the filled can withstands in a vertical stack | 50, 80, 120, 200 |
| Pallet Quantity | number | Number of cans per standard pallet layer or full pallet | 1680, 2400, 4032, 5040 |
| Food Contact Compliance | text (list) | Regulatory food-contact safety standards the product meets | FDA 21 CFR, EU 1935/2004, GB 4806, FSSC 22000 |
| Certification | text (list) | Quality and sustainability certifications held by the manufacturer | ISO 9001, ISO 14001, BRC Packaging, ASI (Aluminium Stewardship Initiative), Metal Recycles Forever |
| Recyclability | enum | Whether the metal packaging is recyclable in standard metal recycling streams | Infinitely Recyclable, Recyclable, Limited |
| Country of Origin | text | Country where the can or closure is manufactured | USA, UK, Germany, France, China, Brazil, Japan |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus industry standards (can-maker size codes, FDA 21 CFR, EU 1935/2004) | [Trivium Packaging Food Cans](https://www.triviumpackaging.com/products/industry/food), [Tecnocap Metal Closures](https://www.tecnocapclosures.com/metal-packaging-group/), [C.L. Smith Metal Cans](https://www.clsmith.com/packaging-solutions/metal-cans/), [Witop Tinplate Classification Guide](https://www.witoptinplate.com/metal-packaging-can-containers/) |
