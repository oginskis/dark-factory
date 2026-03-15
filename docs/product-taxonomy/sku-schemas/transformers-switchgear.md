# SKU Schema: Transformers & Switchgear

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | NXAIR-24-1250, SM6-QM-24, VFI-3PH-2500 |
| Product Name | text | Full product name including type, voltage class, and rating | Siemens NXAIR M 24 kV Air-Insulated Switchgear, Schneider Electric SM6 24 kV Modular Switchgear, Eaton Cooper Power VFI 2500 kVA Pad-Mount Transformer |
| URL | text | Direct link to the product page | https://www.siemens.com/global/en/products/energy/medium-voltage/systems/nxair.html |
| Price | number | Numeric price per unit, excluding currency symbol | 25000, 85000, 350000, 2500000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, INR |
| Manufacturer | text | OEM or integrator name | ABB, Siemens, Schneider Electric, Eaton, Hitachi Energy, GE Vernova, Mitsubishi Electric |
| Equipment Type | enum | Primary product classification | Power transformer, Distribution transformer, Medium voltage switchgear, Low voltage switchgear, Ring main unit, Circuit breaker, Disconnect switch |
| Rated Power | number (kVA) | Nominal power rating for transformers | 500, 2500, 10000, 40000, 250000 |
| Primary Voltage | number (kV) | High-side or primary winding rated voltage | 6.6, 11, 24, 36, 72.5, 132, 400, 765 |
| Secondary Voltage | number (kV) | Low-side or secondary winding rated voltage | 0.4, 0.69, 6.6, 11, 33 |
| Rated Current | number (A) | Continuous current rating for switchgear busbars or feeders | 400, 630, 1250, 2000, 2500, 4000 |
| Short-Circuit Rating | number (kA) | Maximum short-time withstand or breaking current | 12, 16, 25, 31.5, 40, 50 |
| Frequency | text (Hz) | Nominal operating frequency | 50, 60, 50/60 |
| Number of Phases | number | Electrical phase count | 1, 3 |
| Insulation Type | text | Primary insulation medium | Mineral oil, Natural ester (FR3), Dry-type (cast resin), SF6, Air, Vacuum |
| Switching Medium | text | Arc interruption technology for switchgear | Vacuum, SF6, Air |
| BIL Rating | number (kV) | Basic impulse insulation level | 95, 125, 170, 200, 350, 650 |
| Cooling Type | text | Transformer cooling classification per IEC 60076 | ONAN, ONAF, OFAF, ODAF, AN, AF |
| Impedance | number (%) | Short-circuit impedance for transformers | 4.0, 6.0, 8.0, 10.0, 12.5 |
| Tap Changer Type | text | Voltage regulation mechanism | No-load tap changer, On-load tap changer (OLTC), None |
| Tap Range | text | Available voltage adjustment range | +/- 2x2.5%, +/- 5x2%, +/- 8x1.25% |
| Efficiency | number (%) | Full-load energy efficiency for transformers | 98.5, 99.0, 99.5, 99.7 |
| Temperature Rise | number (K) | Maximum winding temperature rise above ambient | 55, 65, 70, 80 |
| Enclosure Type | text | Housing or installation configuration | Indoor, Outdoor, Pad-mounted, Pole-mounted, Substation, Metal-enclosed, Metal-clad |
| IP Rating | text | Ingress protection rating of the enclosure | IP20, IP31, IP42, IP54, IP65 |
| Dimensions | text (mm) | Overall length x width x height of the unit | 550 x 1200 x 2250, 2500 x 3200 x 4500 |
| Weight | number (kg) | Total mass of the unit including oil or insulation | 850, 3500, 12000, 85000, 250000 |
| Noise Level | number (dB(A)) | Sound power level at rated load | 52, 60, 68, 75, 85 |
| Arc Fault Rating | text | Internal arc containment classification per IEC 62271-200 | IAC A FLR, IAC AFL, IAC B, None |
| Insulation Class | text | Thermal insulation class for dry-type transformers | B (130 C), F (155 C), H (180 C) |
| Standards Compliance | text (list) | Applicable design and test standards | IEC 60076, IEC 62271-200, IEEE C57, ANSI C37, IEC 61869, EN 50588 |
| Certifications | text (list) | Third-party certifications and markings | CE, UL, CSA, KEMA type-tested, CESI |
| Dielectric Fluid Volume | number (L) | Volume of insulating fluid for liquid-filled transformers | 120, 500, 2500, 15000 |
| Service Life | number (years) | Expected operational design life | 20, 25, 30, 40 |
| Corrosion Protection | text | Enclosure or tank corrosion resistance class | C3, C4, C5, Hot-dip galvanised |
| Country of Origin | text | Country where the unit is manufactured or assembled | Switzerland, Germany, France, Ireland, USA, India, China |
| Application | text (list) | Primary intended use cases or industries | Utility distribution, Industrial, Commercial building, Data centre, Renewable integration, Mining, Oil and gas |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus IEC 60076 and IEC 62271 standards | [Siemens NXAIR](https://www.siemens.com/global/en/products/energy/medium-voltage/systems/nxair.html), [Schneider Electric SM6](https://www.se.com/ww/en/work/products/product-launch/sm6/), [Eaton Cooper Power VFI](https://www.eaton.com/us/en-us/catalog/medium-voltage-power-distribution-control-systems/vfi-three-phase-pad-mounted-transformers.html), [Hitachi Energy Transformers](https://www.hitachienergy.com/products-and-solutions/transformers/power-transformers) |
