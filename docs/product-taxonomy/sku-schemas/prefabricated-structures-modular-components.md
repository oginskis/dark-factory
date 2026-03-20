# SKU Schema: Prefabricated Structures & Modular Components

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.prefab_modular`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or supplier product identifier | KRM-MOD-2500, PNB-GRD-1020, PFX-OFF-340 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as type, size, and application | Karmod 2-Storey Modular Office 12.5m x 6m, Panel Built 25x71 Prefab Guard House, Prefabex Portable Classroom |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/modular-office-2-storey |
| Price | price | number | — | yes | Numeric price per unit or per square metre, excluding currency symbol | 18500.00, 45000.00, 125000.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, TRY, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Structure Type | structure_type | enum | — | — | General category of the prefabricated product | Modular Building, Portable Office, Guard Booth, Toilet/Shower Block, Classroom, Container Building, Site Office, Equipment Enclosure |
| Wall Panel Type | wall_panel_type | text | — | — | Construction of exterior wall panels | Cement Board/EPS Sandwich, PIR Sandwich, Rockwool Sandwich, SIP, Steel-Faced Insulated, Timber Frame |
| Insulation Material | insulation_material | text | — | — | Core insulation material used in panels | EPS, XPS, PIR, Rockwool, Glass Wool, PUR |
| Country of Origin | country_of_origin | text | — | — | Country where the structure was manufactured | Turkey, USA, China, UK, Germany, Australia |
| Module Length | module_length | number | m | — | External length of a single module or the complete structure | 6.00, 6.10, 9.00, 12.00, 12.19, 14.63 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Construction Method | construction_method | enum | — | — | How the structure is fabricated and assembled | Volumetric Modular, Panelized, Flat-Pack, Container Conversion, Hybrid |
| Module Width | module_width | number | m | — | External width of a single module or the complete structure | 2.44, 3.00, 3.66, 6.00, 6.10 |
| Module Height | module_height | number | m | — | External height (floor to roof peak) of a single module | 2.59, 2.70, 2.80, 3.00, 3.40 |
| Interior Ceiling Height | interior_ceiling_height | number | m | — | Floor-to-ceiling interior clear height | 2.40, 2.44, 2.50, 2.70 |
| Floor Area | floor_area | number | m2 | — | Gross internal floor area per module or total structure | 14.6, 18.0, 29.7, 55.7, 73.0 |
| Number of Storeys | number_of_storeys | number | — | — | Number of stackable floors in the configuration | 1, 2, 3, 4 |
| Wall Panel Thickness | wall_panel_thickness | number | mm | — | Thickness of the exterior wall panel | 60, 75, 100, 120, 150 |
| Wall U-Value | wall_u-value | number | W/m2K | — | Thermal transmittance of the wall assembly | 0.18, 0.25, 0.35, 0.45, 0.53 |
| Roof U-Value | roof_u-value | number | W/m2K | — | Thermal transmittance of the roof assembly | 0.15, 0.22, 0.30, 0.43 |
| Insulation R-Value | insulation_r-value | number | m2K/W | — | Thermal resistance of the insulation layer | 1.5, 2.0, 2.8, 3.5, 5.0 |
| Steel Frame Specification | steel_frame_specification | text | — | — | Structural steel type and gauge | Galvanized Steel ST-37, C-Section 1.2mm, C-Section 2.0mm, Hot-Rolled Structural |
| Wind Speed Rating | wind_speed_rating | number | km/h | — | Maximum design wind speed the structure can withstand | 80, 100, 120, 145, 180 |
| Seismic Zone | seismic_zone | text | — | — | Seismic design category or zone rating | Zone 1, Zone 2, SDC A, SDC B, SDC C, SDC D |
| Fire Rating | fire_rating | text | — | — | Fire resistance classification of the assembly | 30 min, 60 min, 90 min, 120 min, Class A, Class B |
| Roof Style | roof_style | enum | — | — | Roof configuration of the structure | Flat, Shed, Gable, Standing Seam |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus IBC and ISO building standards | [Karmod](https://www.karmod.com/en/modular-building-specifications/), [Panel Built](https://www.panelbuilt.com/products/prefab-buildings/), [Prefabex](https://www.prefabex.com/our-products/modular-buildings), [PortaFab](https://www.portafab.com/) |
