# SKU Schema: Fire Extinguishers & Suppression Equipment

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.fire_extinguishers_suppression`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | B417T, PRO-4MP-1, FE2A10GR, 466112 |
| Product Name | product_name | text | — | Full product name including key specs such as class, agent, and capacity | Amerex B417T 2.5 lb ABC Dry Chemical Fire Extinguisher, Kidde Pro 210 4 lb ABC Fire Extinguisher, Ansul Sentry 20 lb CO2 Extinguisher |
| URL | url | text | — | Direct link to the product page | https://example.com/product/amerex-b417t-abc-extinguisher |
| Price | price | number | — | Numeric unit price excluding currency symbol | 42.99, 64.95, 289.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary type of fire protection equipment | Portable Extinguisher, Wheeled Extinguisher, Kitchen Suppression System, Vehicle Suppression System, Clean Agent System, Fire Blanket, Aerosol Suppression Unit |
| Fire Class | fire_class | text (list) | — | Fire classifications the extinguisher is rated to combat | A, B, C, D, K, ABC, BC |
| Cylinder Material | cylinder_material | text | — | Material of the pressure vessel | Steel, Aluminum, Stainless Steel |
| Valve Material | valve_material | text | — | Material of the discharge valve assembly | Chrome-Plated Brass, Aluminum, Stainless Steel |
| Mounting Type | mounting_type | text | — | Type of bracket or mounting system | Wall Hook, Vehicle Bracket, Strap Bracket, Cabinet, Marine Bracket |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, China, Mexico, Italy |
| Model Number | model_number | text | — | Manufacturer model or part number | B417T, PRO-4MP-1, A02VB, 466112 |
| UL Rating | ul_rating | text | — | Underwriters Laboratories numerical effectiveness rating | 1A:10B:C, 2A:10B:C, 4A:80B:C, 10A:120B:C, 2A:40B:C |
| Extinguishing Agent | extinguishing_agent | text | — | Chemical or substance used to suppress fire | Monoammonium Phosphate (Dry Chemical), Sodium Bicarbonate, Carbon Dioxide (CO2), Water, Wet Chemical (Potassium Acetate), Halotron, Clean Agent (FE-36), Foam (AFFF), Sodium Chloride (Class D) |
| Discharge Time | discharge_time | text | — | Duration of continuous agent discharge | 8-12 seconds, 13-15 seconds, 18-20 seconds, 25-30 seconds |
| Discharge Range | discharge_range | text | — | Maximum effective throw distance of the agent stream | 10-15 ft, 15-21 ft, 20-35 ft |
| Operating Pressure | operating_pressure | number | psi | Internal pressure of the charged extinguisher at standard temperature | 100, 150, 195, 235 |
| Operating Temperature Range | operating_temperature_range | text | — | Ambient temperature range for reliable operation | -40 F to 120 F, -20 F to 120 F, 32 F to 120 F |
| Height | height | number | in | Overall height of the extinguisher including handle | 8.7, 15.7, 19.5, 24.5 |
| Width | width | number | in | Overall width including handle or hose bracket | 4.5, 6.0, 8.5, 10.0 |
| Rechargeable | rechargeable | boolean | — | Whether the extinguisher can be professionally refilled after use | true, false |
| Mounting Bracket Included | mounting_bracket_included | boolean | — | Whether a wall bracket or vehicle bracket is included | true, false |
| Corrosion Resistant | corrosion_resistant | boolean | — | Whether the cylinder or valve has corrosion-resistant coating for marine or industrial use | true, false |
| Inspection Gauge | inspection_gauge | boolean | — | Whether a pressure gauge is included for visual inspection | true, false |
| Safety Seal | safety_seal | text | — | Tamper indicator showing the extinguisher has not been discharged | Pull Pin with Tamper Seal, Break-Away Seal |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (UL 711, NFPA 10, EN 3) | [Amerex](https://www.amerex-fire.com/products/), [Kidde](https://www.kidde.com/products/commercial-fire-extinguishers/pro-210-fire-extinguisher), [National Fire Supply](https://nationalfiresupply.com/), [Fire Extinguisher Depot](https://fireextinguisherdepot.com/fire-extinguisher-underwriters-laboratory-ul-rating-guide/) |
