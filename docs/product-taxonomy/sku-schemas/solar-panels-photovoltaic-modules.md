# SKU Schema: Solar Panels & Photovoltaic Modules

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.solar_panels_pv`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | LR7-72HGD-615M, LR5-72HPH-555M, JAM72S30-545 |
| Product Name | product_name | text | Full product name including key specs such as brand, wattage, and technology | LONGi Hi-MO 7 615W Bifacial N-Type Module, JA Solar DeepBlue 3.0 545W Mono PERC |
| URL | url | text | Direct link to the product page | https://example.com/product/hi-mo-7-615w |
| Price | price | number | Numeric price per unit (per module) excluding currency symbol | 189.00, 245.50, 310.00, 0.18 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CNY |
| Model Number | model_number | text | Manufacturer model designation | LR7-72HGD-615M, TSM-DE20-600, Tiger Neo 72HL4-BDV |
| Cell Type | cell_type | text | Photovoltaic cell technology | Monocrystalline PERC, N-Type TOPCon, HJT (Heterojunction), Polycrystalline, Bifacial N-Type |
| Frame Material | frame_material | text | Module frame construction | Anodized Aluminum Alloy, Frameless |
| Connector Type | connector_type | text | Cable connector standard | MC4, MC4-EVO2, QC4 |
| Performance Warranty | performance_warranty | number (yr) | Linear performance guarantee duration | 25, 30 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the module is manufactured | China, Vietnam, Malaysia, India, Germany, USA |
| Cell Arrangement | cell_arrangement | text | Physical layout and cut type of cells | Half-Cut, Full-Cell, Shingled, Multi-Busbar, SmartWire |
| Rated Power (Pmax) | rated_power_pmax | number (W) | Maximum power output under Standard Test Conditions | 370, 545, 580, 615, 650 |
| Power Tolerance | power_tolerance | text (W) | Deviation range from rated power | 0/+5W, 0/+10W, -3/+3% |
| Module Efficiency | module_efficiency | number (%) | Conversion efficiency under STC | 20.5, 21.3, 22.5, 22.8, 24.5 |
| Short Circuit Current (Isc) | short_circuit_current_isc | number (A) | Maximum current when circuit is shorted under STC | 11.52, 13.85, 14.33, 16.05 |
| Current at Max Power (Imp) | current_at_max_power_imp | number (A) | Current at the maximum power point under STC | 10.81, 13.20, 13.85, 15.25 |
| NMOT | nmot | number (C) | Nominal Module Operating Temperature | 41, 43, 45 |
| Temperature Coefficient Pmax | temperature_coefficient_pmax | number (%/C) | Power output change per degree Celsius above STC | -0.28, -0.29, -0.34, -0.35 |
| Temperature Coefficient Voc | temperature_coefficient_voc | number (%/C) | Open circuit voltage change per degree Celsius | -0.25, -0.27, -0.30 |
| Maximum Series Fuse Rating | maximum_series_fuse_rating | number (A) | Overcurrent protection fuse rating | 15, 20, 25, 30 |
| Module Dimensions (L x W x H) | module_dimensions_l_x_w_x_h | text (mm) | Physical module length, width, and frame thickness | 2278 x 1134 x 30, 2382 x 1134 x 30, 1722 x 1134 x 30 |
| Front Cover | front_cover | text | Front glass type and thickness | 3.2 mm Tempered Glass, 2.0 mm AR Coated Glass |
| Back Cover | back_cover | text | Rear cover material | White Backsheet, Transparent Backsheet, 2.0 mm Glass (Dual Glass) |
| Junction Box | junction_box | text | Junction box IP rating and configuration | IP68, IP67, 3 bypass diodes, Split junction box |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus IEC/UL standards (IEC 61215, IEC 61730, UL 61730) and STC/NMOT test conditions | [LONGi Hi-MO 7](https://www.longi.com/en/products/modules/hi-mo-7/), [SunHub Spec Sheet Guide](https://www.sunhub.com/blog/the-ultimate-guide-to-reading-a-solar-panel-spec-sheet/), [A1 Solar Store Datasheet Guide](https://a1solarstore.com/blog/whats-in-the-datasheet-a-guide-to-reading-solar-panel-specs.html), [ENF Solar Panel Directory](https://www.enfsolar.com/pv/panel) |
