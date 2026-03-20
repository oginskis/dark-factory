# SKU Schema: Head Protection (Hard Hats, Helmets)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.head_protection`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 475362, 10034018, MSA-10204776 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, class, and brim style | MSA V-Gard Full Brim Hard Hat Class E, 3M SecureFit X5000 Series Safety Helmet Type 2 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/v-gard-full-brim-hard-hat |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 12.50, 34.99, 89.95 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary type of head protection | Hard Hat, Safety Helmet, Bump Cap |
| ANSI/ISEA Type | ansiisea_type | enum | — | — | Impact protection classification per ANSI Z89.1 | Type I, Type II |
| Electrical Class | electrical_class | enum | — | — | Level of electrical insulation per ANSI Z89.1 | Class E, Class G, Class C |
| Shell Material | shell_material | text | — | — | Material used for the outer shell | High-Density Polyethylene (HDPE), ABS, Polycarbonate, Fiberglass, Phenolic |
| Suspension Type | suspension_type | text | — | — | Internal suspension system that distributes impact force | 4-Point Ratchet, 6-Point Ratchet, 4-Point Pinlock, 6-Point Suspension, 8-Point Ratchet |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Suspension Material | suspension_material | text | — | — | Material of the suspension webbing and cradle | Polyester, Nylon, Polypropylene |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, Mexico, China, Germany |
| Model Number | model_number | text | — | — | Manufacturer model or part number | 475362, H-700, A79R020000 |
| Brim Style | brim_style | enum | — | — | Shape and coverage of the hat brim | Cap Style (Front Brim), Full Brim, No Brim |
| Venting | venting | enum | — | — | Whether the shell includes ventilation openings | Vented, Non-Vented |
| Color | color | text | — | — | Shell color | White, Yellow, Orange, Red, Blue, Green, Gray, Hi-Viz Lime |
| Chinstrap Included | chinstrap_included | boolean | — | — | Whether an integrated or included chinstrap is provided | true, false |
| Accessory Slots | accessory_slots | boolean | — | — | Whether the hat has integrated slots for face shields, earmuffs, or other attachments | true, false |
| Slot Configuration | slot_configuration | text | — | — | Accessory mounting slot standard | MSA V-Gard, Universal Accessory Slot, Cap-Mounted |
| UV Indicator | uv_indicator | boolean | — | — | Whether the shell includes a UV degradation indicator | true, false |
| Impact Protection Technology | impact_protection_technology | text | — | — | Additional impact mitigation technology beyond standard shell | Mips Brain Protection, Koroyd, EPS Foam Liner, None |
| Reflective Trim | reflective_trim | boolean | — | — | Whether the hat includes high-visibility reflective striping | true, false |
| Temperature Range | temperature_range | text | — | — | Rated operating temperature range | -30 C to 50 C, -20 F to 120 F |
| Dielectric Rating | dielectric_rating | text | — | — | Maximum voltage protection for electrical class | 20000V (Class E), 2200V (Class G) |
| Certifications | certifications | text (list) | — | — | Applicable safety standards met | ANSI/ISEA Z89.1-2014, CSA Z94.1-2015, EN 397, EN 12492, AS/NZS 1801 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (ANSI Z89.1, CSA Z94.1, EN 397) | [MSA Safety](https://us.msasafety.com/Head-Protection/Hard-Hats/c/11204), [Grainger](https://www.grainger.com/category/safety/head-protection/hard-hats-and-helmets), [3M](https://www.3m.com/3M/en_US/p/c/ppe/head-protection/), [Pyramex Safety](https://www.pyramexsafety.com/) |
