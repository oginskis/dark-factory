# SKU Schema: Prefabricated Structures & Modular Components

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or supplier product identifier | KRM-MOD-2500, PNB-GRD-1020, PFX-OFF-340 |
| Product Name | text | Full product name including key specs such as type, size, and application | Karmod 2-Storey Modular Office 12.5m x 6m, Panel Built 25x71 Prefab Guard House, Prefabex Portable Classroom |
| URL | text | Direct link to the product page | https://example.com/product/modular-office-2-storey |
| Price | number | Numeric price per unit or per square metre, excluding currency symbol | 18500.00, 45000.00, 125000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, TRY, AUD |
| Brand | text | Manufacturer or supplier name | Karmod, Panel Built, Prefabex, PortaFab, Modular Genius, ATCO, Algeco, Wernick |
| Structure Type | enum | General category of the prefabricated product | Modular Building, Portable Office, Guard Booth, Toilet/Shower Block, Classroom, Container Building, Site Office, Equipment Enclosure |
| Construction Method | enum | How the structure is fabricated and assembled | Volumetric Modular, Panelized, Flat-Pack, Container Conversion, Hybrid |
| Module Width | number (m) | External width of a single module or the complete structure | 2.44, 3.00, 3.66, 6.00, 6.10 |
| Module Length | number (m) | External length of a single module or the complete structure | 6.00, 6.10, 9.00, 12.00, 12.19, 14.63 |
| Module Height | number (m) | External height (floor to roof peak) of a single module | 2.59, 2.70, 2.80, 3.00, 3.40 |
| Interior Ceiling Height | number (m) | Floor-to-ceiling interior clear height | 2.40, 2.44, 2.50, 2.70 |
| Floor Area | number (m2) | Gross internal floor area per module or total structure | 14.6, 18.0, 29.7, 55.7, 73.0 |
| Number of Storeys | number | Number of stackable floors in the configuration | 1, 2, 3, 4 |
| Wall Panel Type | text | Construction of exterior wall panels | Cement Board/EPS Sandwich, PIR Sandwich, Rockwool Sandwich, SIP, Steel-Faced Insulated, Timber Frame |
| Wall Panel Thickness | number (mm) | Thickness of the exterior wall panel | 60, 75, 100, 120, 150 |
| Wall U-Value | number (W/m2K) | Thermal transmittance of the wall assembly | 0.18, 0.25, 0.35, 0.45, 0.53 |
| Roof U-Value | number (W/m2K) | Thermal transmittance of the roof assembly | 0.15, 0.22, 0.30, 0.43 |
| Insulation Material | text | Core insulation material used in panels | EPS, XPS, PIR, Rockwool, Glass Wool, PUR |
| Insulation R-Value | number (m2K/W) | Thermal resistance of the insulation layer | 1.5, 2.0, 2.8, 3.5, 5.0 |
| Steel Frame Specification | text | Structural steel type and gauge | Galvanized Steel ST-37, C-Section 1.2mm, C-Section 2.0mm, Hot-Rolled Structural |
| Floor Load Capacity | number (kg/m2) | Maximum uniformly distributed floor live load | 150, 200, 250, 350, 500 |
| Snow Load Capacity | number (kg/m2) | Maximum design snow load on the roof | 50, 75, 100, 150, 200 |
| Wind Speed Rating | number (km/h) | Maximum design wind speed the structure can withstand | 80, 100, 120, 145, 180 |
| Seismic Zone | text | Seismic design category or zone rating | Zone 1, Zone 2, SDC A, SDC B, SDC C, SDC D |
| Fire Rating | text | Fire resistance classification of the assembly | 30 min, 60 min, 90 min, 120 min, Class A, Class B |
| Roof Style | enum | Roof configuration of the structure | Flat, Shed, Gable, Standing Seam |
| Relocatable | boolean | Whether the structure can be disassembled and moved | true, false |
| Application | text (list) | Primary intended uses for the structure | Office, Classroom, Healthcare, Guard Booth, Bathroom, Storage, Retail, Laboratory |
| Certification | text (list) | Building code and quality certifications | IBC, ISO 9001, CE, AS/NZS 3837, CSA |
| Country of Origin | text | Country where the structure was manufactured | Turkey, USA, China, UK, Germany, Australia |
| Heaviest Component Weight | number (kg) | Weight of the heaviest individual panel or module for transport planning | 114, 250, 500, 2500, 15000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus IBC and ISO building standards | [Karmod](https://www.karmod.com/en/modular-building-specifications/), [Panel Built](https://www.panelbuilt.com/products/prefab-buildings/), [Prefabex](https://www.prefabex.com/our-products/modular-buildings), [PortaFab](https://www.portafab.com/) |
