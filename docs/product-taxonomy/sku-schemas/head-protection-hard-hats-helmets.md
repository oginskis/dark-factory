# SKU Schema: Head Protection (Hard Hats, Helmets)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.head_protection`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 475362, 10034018, MSA-10204776 |
| Product Name | text | Full product name including key specs such as type, class, and brim style | MSA V-Gard Full Brim Hard Hat Class E, 3M SecureFit X5000 Series Safety Helmet Type 2 |
| URL | text | Direct link to the product page | https://example.com/product/v-gard-full-brim-hard-hat |
| Price | number | Numeric unit price excluding currency symbol | 12.50, 34.99, 89.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary type of head protection | Hard Hat, Safety Helmet, Bump Cap |
| ANSI/ISEA Type | enum | Impact protection classification per ANSI Z89.1 | Type I, Type II |
| Electrical Class | enum | Level of electrical insulation per ANSI Z89.1 | Class E, Class G, Class C |
| Shell Material | text | Material used for the outer shell | High-Density Polyethylene (HDPE), ABS, Polycarbonate, Fiberglass, Phenolic |
| Suspension Type | text | Internal suspension system that distributes impact force | 4-Point Ratchet, 6-Point Ratchet, 4-Point Pinlock, 6-Point Suspension, 8-Point Ratchet |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Suspension Material | text | Material of the suspension webbing and cradle | Polyester, Nylon, Polypropylene |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, China, Germany |
| Model Number | text | Manufacturer model or part number | 475362, H-700, A79R020000 |
| Brim Style | enum | Shape and coverage of the hat brim | Cap Style (Front Brim), Full Brim, No Brim |
| Venting | enum | Whether the shell includes ventilation openings | Vented, Non-Vented |
| Color | text | Shell color | White, Yellow, Orange, Red, Blue, Green, Gray, Hi-Viz Lime |
| Chinstrap Included | boolean | Whether an integrated or included chinstrap is provided | true, false |
| Accessory Slots | boolean | Whether the hat has integrated slots for face shields, earmuffs, or other attachments | true, false |
| Slot Configuration | text | Accessory mounting slot standard | MSA V-Gard, Universal Accessory Slot, Cap-Mounted |
| UV Indicator | boolean | Whether the shell includes a UV degradation indicator | true, false |
| Impact Protection Technology | text | Additional impact mitigation technology beyond standard shell | Mips Brain Protection, Koroyd, EPS Foam Liner, None |
| Reflective Trim | boolean | Whether the hat includes high-visibility reflective striping | true, false |
| Temperature Range | text | Rated operating temperature range | -30 C to 50 C, -20 F to 120 F |
| Dielectric Rating | text | Maximum voltage protection for electrical class | 20000V (Class E), 2200V (Class G) |
| Certifications | text (list) | Applicable safety standards met | ANSI/ISEA Z89.1-2014, CSA Z94.1-2015, EN 397, EN 12492, AS/NZS 1801 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (ANSI Z89.1, CSA Z94.1, EN 397) | [MSA Safety](https://us.msasafety.com/Head-Protection/Hard-Hats/c/11204), [Grainger](https://www.grainger.com/category/safety/head-protection/hard-hats-and-helmets), [3M](https://www.3m.com/3M/en_US/p/c/ppe/head-protection/), [Pyramex Safety](https://www.pyramexsafety.com/) |
