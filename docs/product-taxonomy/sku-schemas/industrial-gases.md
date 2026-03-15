# SKU Schema: Industrial Gases

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products
**Taxonomy ID:** `chemicals.industrial_gases`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | AR UHP300, HE 300, NI 200, CO2-50L |
| Product Name | text | Full product name including gas type, grade, supply mode, and size | UHP Grade Argon Size 300 High Pressure Steel Cylinder CGA 580, Industrial Grade Oxygen Size 200 |
| URL | text | Direct link to the product page | https://example.com/product/ar-uhp300 |
| Price | number | Numeric price per unit (cylinder, dewar, or per volume), excluding currency symbol | 85.00, 250.00, 1200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Chemical Formula | text | Chemical formula of the primary gas species | Ar, O2, N2, CO2, He, C2H2, H2, SF6 |
| Gas Category | enum | Broad functional classification of the gas | Atmospheric, Noble/Rare, Fuel/Combustion, Specialty, Calibration, Medical, Shielding |
| Purity Grade | text | Named quality tier indicating minimum purity level | Industrial, High Purity, Ultra High Purity, Research, Zero, Medical |
| Valve Outlet Type | text | Thread or connection type where CGA is not used | DIN 477, BS 341, NF E29-650, DISS 718 |
| Hazard Class | text | DOT/ADR transport hazard classification | 2.2 Non-flammable Gas, 2.1 Flammable Gas, 5.1 Oxidizer |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the gas was produced or filled | USA, Canada, Germany, Australia, UK |
| Brand/Supplier | text | Gas manufacturer or distributor name | Linde, Air Liquide, Airgas, Matheson, Messer, Air Products, BOC, Praxair |
| Gas Name | text | Common name of the gas or mixture | Argon, Oxygen, Nitrogen, Carbon Dioxide, Helium, Acetylene, Hydrogen |
| CAS Number | text | Chemical Abstracts Service registry number for the gas | 7440-37-1, 7782-44-7, 7727-37-9, 124-38-9, 7440-59-7 |
| Purity | number (%) | Minimum purity expressed as a percentage by volume | 99.5, 99.995, 99.999, 99.9999 |
| Quality Code | text | Numeric grade code where digits encode nines of purity | 2.5, 4.5, 5.0, 5.7, 6.0 |
| Impurity Limits | text | Key impurity species and maximum concentrations in the product | O2 less than 1 ppm, H2O less than 1 ppm, N2 less than 5 ppm, THC less than 0.5 ppm |
| Physical State | enum | State of the gas as delivered in the container | Compressed Gas, Liquefied Gas, Dissolved Gas, Cryogenic Liquid |
| Supply Mode | enum | Type of delivery or containment system | Cylinder, Dewar, Bulk Tank, Tube Trailer, Microbulk, On-site Generation |
| Water Volume | number (L) | Internal water capacity of the cylinder in litres | 11, 20, 33, 40, 49, 50 |
| Gas Volume | text | Deliverable gas volume at standard temperature and pressure | 56 cu ft, 150 cu ft, 251 cu ft, 336 cu ft, 8.5 m3 |
| Fill Pressure | text | Maximum fill pressure of the cylinder | 2015 psi, 2265 psi, 2400 psi, 200 bar, 300 bar |
| CGA Valve Connection | text | Compressed Gas Association valve outlet fitting designation | CGA 580, CGA 540, CGA 320, CGA 350, CGA 510 |
| DOT/TC Specification | text | Cylinder construction specification per Department of Transportation or Transport Canada | 3AA-2015, 3AA-2400, 3AL-2216, 4BA-240 |
| Application | text (list) | Primary intended uses for the gas product | MIG Welding, TIG Welding, Laser Cutting, Inerting, Chromatography, Food Processing, Medical |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (CGA V-1, ISO 17025, DOT cylinder specifications) | [Airgas](https://www.airgas.com/product/Gases/Argon/p/AR%20UHP300), [Linde](https://www.lindedirect.com/solutions/specialty-gases-solutions/pure-gases), [Air Liquide](https://www.airliquide.ca/file/general/Cylinder_Chart_ENG.pdf), [Matheson](https://www.mathesongas.com/pdfs/litcenter/Industrial-Cylinder-Dimensions.pdf) |
