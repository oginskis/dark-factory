# SKU Schema: Transformers & Switchgear

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.transformers_switchgear`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | NXAIR-24-1250, SM6-QM-24, VFI-3PH-2500 |
| Product Name | product_name | text | Full product name including type, voltage class, and rating | Siemens NXAIR M 24 kV Air-Insulated Switchgear, Schneider Electric SM6 24 kV Modular Switchgear, Eaton Cooper Power VFI 2500 kVA Pad-Mount Transformer |
| URL | url | text | Direct link to the product page | https://www.siemens.com/global/en/products/energy/medium-voltage/systems/nxair.html |
| Price | price | number | Numeric price per unit, excluding currency symbol | 25000, 85000, 350000, 2500000 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, INR |
| Equipment Type | equipment_type | enum | Primary product classification | Power transformer, Distribution transformer, Medium voltage switchgear, Low voltage switchgear, Ring main unit, Circuit breaker, Disconnect switch |
| Insulation Type | insulation_type | text | Primary insulation medium | Mineral oil, Natural ester (FR3), Dry-type (cast resin), SF6, Air, Vacuum |
| Cooling Type | cooling_type | text | Transformer cooling classification per IEC 60076 | ONAN, ONAF, OFAF, ODAF, AN, AF |
| Tap Changer Type | tap_changer_type | text | Voltage regulation mechanism | No-load tap changer, On-load tap changer (OLTC), None |
| Enclosure Type | enclosure_type | text | Housing or installation configuration | Indoor, Outdoor, Pad-mounted, Pole-mounted, Substation, Metal-enclosed, Metal-clad |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Insulation Class | insulation_class | text | Thermal insulation class for dry-type transformers | B (130 C), F (155 C), H (180 C) |
| Country of Origin | country_of_origin | text | Country where the unit is manufactured or assembled | Switzerland, Germany, France, Ireland, USA, India, China |
| Manufacturer | manufacturer | text | OEM or integrator name | ABB, Siemens, Schneider Electric, Eaton, Hitachi Energy, GE Vernova, Mitsubishi Electric |
| Rated Power | rated_power | number (kVA) | Nominal power rating for transformers | 500, 2500, 10000, 40000, 250000 |
| Rated Current | rated_current | number (A) | Continuous current rating for switchgear busbars or feeders | 400, 630, 1250, 2000, 2500, 4000 |
| Short-Circuit Rating | short-circuit_rating | number (kA) | Maximum short-time withstand or breaking current | 12, 16, 25, 31.5, 40, 50 |
| Frequency | frequency | text (Hz) | Nominal operating frequency | 50, 60, 50/60 |
| Number of Phases | number_of_phases | number | Electrical phase count | 1, 3 |
| Switching Medium | switching_medium | text | Arc interruption technology for switchgear | Vacuum, SF6, Air |
| BIL Rating | bil_rating | number (kV) | Basic impulse insulation level | 95, 125, 170, 200, 350, 650 |
| Impedance | impedance | number (%) | Short-circuit impedance for transformers | 4.0, 6.0, 8.0, 10.0, 12.5 |
| Tap Range | tap_range | text | Available voltage adjustment range | +/- 2x2.5%, +/- 5x2%, +/- 8x1.25% |
| Efficiency | efficiency | number (%) | Full-load energy efficiency for transformers | 98.5, 99.0, 99.5, 99.7 |
| Temperature Rise | temperature_rise | number (K) | Maximum winding temperature rise above ambient | 55, 65, 70, 80 |
| IP Rating | ip_rating | text | Ingress protection rating of the enclosure | IP20, IP31, IP42, IP54, IP65 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus IEC 60076 and IEC 62271 standards | [Siemens NXAIR](https://www.siemens.com/global/en/products/energy/medium-voltage/systems/nxair.html), [Schneider Electric SM6](https://www.se.com/ww/en/work/products/product-launch/sm6/), [Eaton Cooper Power VFI](https://www.eaton.com/us/en-us/catalog/medium-voltage-power-distribution-control-systems/vfi-three-phase-pad-mounted-transformers.html), [Hitachi Energy Transformers](https://www.hitachienergy.com/products-and-solutions/transformers/power-transformers) |
