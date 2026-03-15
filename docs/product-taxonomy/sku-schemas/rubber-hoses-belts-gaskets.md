# SKU Schema: Rubber Hoses, Belts & Gaskets

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.rubber_hoses_belts_gaskets`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | GT-20073217, GY-4060XL, PR-SRG-125 |
| Product Name | product_name | text | Full product name including type, material, and size | Gates MegaSys 4K Hydraulic Hose 3/8 in ID, Continental B42 V-Belt, Garlock 3000 Gasket 4 in |
| URL | url | text | Direct link to the product page | https://example.com/product/megasys-4k-hose-38 |
| Price | price | number | Numeric price per unit or per foot, excluding currency symbol | 8.50, 24.99, 3.75 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary product classification | Hydraulic Hose, Industrial Hose, V-Belt, Synchronous Belt, Timing Belt, Flat Gasket, Spiral Wound Gasket, O-Ring, Sheet Rubber |
| Material | material | text | Primary rubber or elastomer compound | Natural Rubber, SBR, NBR, EPDM, Neoprene, Silicone, Viton, Nitrile, FKM |
| Cover Material | cover_material | text | Outer cover compound for hoses and belts | Synthetic Rubber, Neoprene, Fiber Jacket, Polyurethane |
| Country of Origin | country_of_origin | text | Manufacturing country | USA, Germany, Japan, China, Mexico |
| Inside Diameter | inside_diameter | text (mm) | Internal bore diameter for hoses or ID for gaskets | 6.35, 9.5, 12.7, 19.0, 25.4, 50.8 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Width | width | number (mm) | Belt top width or gasket/sheet width | 10, 13, 17, 22, 610, 914 |
| Thickness | thickness | number (mm) | Wall thickness for hoses or sheet/gasket thickness | 1.6, 3.2, 4.8, 6.4, 9.5, 12.7 |
| Working Pressure | working_pressure | number (psi) | Maximum continuous operating pressure for hoses | 250, 1000, 3000, 5000, 6000 |
| Burst Pressure | burst_pressure | number (psi) | Minimum burst pressure for hoses | 1000, 4000, 12000, 20000 |
| Temperature Range | temperature_range | text | Continuous service temperature range | -40 F to 250 F, -67 F to 158 F, -20 F to 300 F |
| Reinforcement | reinforcement | text | Internal reinforcement structure for hoses and belts | Steel Wire Braid, Textile Braid, Steel Spiral, Polyester Cord, Aramid, Fiberglass |
| Durometer | durometer | text (Shore A) | Hardness measurement for gaskets, sheet rubber, and O-rings | 40A, 50A, 60A, 70A, 80A |
| Belt Cross Section | belt_cross_section | text | Standard belt profile designation | A, B, C, D, 3V, 5V, 8V, 3L, 4L, HTD |
| Flange/Coupling Standard | flangecoupling_standard | text | Connection standard or compatibility for hoses | SAE J517, DIN 20066, JIS B 8363, BSP |
| Application | application | text (list) | Primary intended uses | Hydraulic Systems, Power Transmission, Chemical Transfer, Food and Beverage, Steam, Air Compressor, Automotive Engine |
| Industry Standard | industry_standard | text (list) | Governing standards and specifications | SAE 100R1, SAE 100R2, EN 853, ISO 1307, DIN 2215, ISO 1813, ASTM D2000 |
| Oil Resistance | oil_resistance | enum | Resistance to petroleum-based fluids | Excellent, Good, Fair, Not Recommended |
| Chemical Resistance | chemical_resistance | enum | Resistance to chemicals and solvents | Excellent, Good, Fair, Not Recommended |
| Abrasion Resistance | abrasion_resistance | enum | Resistance to surface wear | High, Medium, Low |
| Certification | certification | text (list) | Safety and compliance certifications | FDA, MSHA, UL, 3-A Sanitary, ATEX, RoHS |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (SAE J517, DIN 2215, ISO 1307) | [Gates Corporation](https://www.gates.com/us/en/knowledge-center/resource-library/product-catalogs.html), [Goodyear Rubber Products](https://www.goodyearrubberproducts.com/catalog/index.asp), [Continental ContiTech](https://www.continental-industry.com/), [Metals USA / Pioneer Rubber](https://pioneerrubber.com) |
