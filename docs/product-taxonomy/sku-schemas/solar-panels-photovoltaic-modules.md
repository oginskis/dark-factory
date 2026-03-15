# SKU Schema: Solar Panels & Photovoltaic Modules

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | LR7-72HGD-615M, LR5-72HPH-555M, JAM72S30-545 |
| Product Name | text | Full product name including key specs such as brand, wattage, and technology | LONGi Hi-MO 7 615W Bifacial N-Type Module, JA Solar DeepBlue 3.0 545W Mono PERC |
| URL | text | Direct link to the product page | https://example.com/product/hi-mo-7-615w |
| Price | number | Numeric price per unit (per module) excluding currency symbol | 189.00, 245.50, 310.00, 0.18 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CNY |
| Brand/Manufacturer | text | Module manufacturer name | LONGi, JA Solar, Trina Solar, Canadian Solar, Jinko Solar, REC, Panasonic, Q CELLS, Meyer Burger |
| Model Number | text | Manufacturer model designation | LR7-72HGD-615M, TSM-DE20-600, Tiger Neo 72HL4-BDV |
| Cell Type | text | Photovoltaic cell technology | Monocrystalline PERC, N-Type TOPCon, HJT (Heterojunction), Polycrystalline, Bifacial N-Type |
| Cell Count | number | Total number of cells in the module | 60, 66, 72, 78, 108, 120, 132, 144 |
| Cell Arrangement | text | Physical layout and cut type of cells | Half-Cut, Full-Cell, Shingled, Multi-Busbar, SmartWire |
| Rated Power (Pmax) | number (W) | Maximum power output under Standard Test Conditions | 370, 545, 580, 615, 650 |
| Power Tolerance | text (W) | Deviation range from rated power | 0/+5W, 0/+10W, -3/+3% |
| Module Efficiency | number (%) | Conversion efficiency under STC | 20.5, 21.3, 22.5, 22.8, 24.5 |
| Open Circuit Voltage (Voc) | number (V) | Maximum voltage when circuit is open under STC | 40.9, 49.5, 52.51, 48.8 |
| Short Circuit Current (Isc) | number (A) | Maximum current when circuit is shorted under STC | 11.52, 13.85, 14.33, 16.05 |
| Voltage at Max Power (Vmp) | number (V) | Voltage at the maximum power point under STC | 34.2, 41.65, 43.80, 41.0 |
| Current at Max Power (Imp) | number (A) | Current at the maximum power point under STC | 10.81, 13.20, 13.85, 15.25 |
| NMOT | number (C) | Nominal Module Operating Temperature | 41, 43, 45 |
| Temperature Coefficient Pmax | number (%/C) | Power output change per degree Celsius above STC | -0.28, -0.29, -0.34, -0.35 |
| Temperature Coefficient Voc | number (%/C) | Open circuit voltage change per degree Celsius | -0.25, -0.27, -0.30 |
| Maximum System Voltage | number (V) | Maximum allowable voltage in a string configuration | 1000, 1500 |
| Maximum Series Fuse Rating | number (A) | Overcurrent protection fuse rating | 15, 20, 25, 30 |
| Module Dimensions (L x W x H) | text (mm) | Physical module length, width, and frame thickness | 2278 x 1134 x 30, 2382 x 1134 x 30, 1722 x 1134 x 30 |
| Weight | number (kg) | Net weight of one module | 19.5, 20.8, 28.5, 33.5 |
| Front Cover | text | Front glass type and thickness | 3.2 mm Tempered Glass, 2.0 mm AR Coated Glass |
| Back Cover | text | Rear cover material | White Backsheet, Transparent Backsheet, 2.0 mm Glass (Dual Glass) |
| Frame Material | text | Module frame construction | Anodized Aluminum Alloy, Frameless |
| Junction Box | text | Junction box IP rating and configuration | IP68, IP67, 3 bypass diodes, Split junction box |
| Connector Type | text | Cable connector standard | MC4, MC4-EVO2, QC4 |
| Bifacial | boolean | Whether the module captures light from both sides | Yes, No |
| Bifaciality Factor | number (%) | Ratio of rear to front power generation | 70, 75, 80, 85 |
| Wind Load Rating | number (Pa) | Maximum front wind load the module can withstand | 2400, 3600, 5400 |
| Snow Load Rating | number (Pa) | Maximum snow load the module can withstand | 5400, 7200 |
| Operating Temperature Range | text (C) | Certified operating temperature limits | -40 to +85, -40 to +85 |
| Annual Degradation Rate | number (%/yr) | Guaranteed maximum annual power loss after first year | 0.40, 0.45, 0.50, 0.55 |
| Product Warranty | number (yr) | Manufacturer product/material warranty duration | 12, 15, 25, 30 |
| Performance Warranty | number (yr) | Linear performance guarantee duration | 25, 30 |
| Fire Rating | text | Fire resistance classification | Type 1/Class A, Type 2/Class B, Class C |
| Certifications | text (list) | Testing and compliance certifications | IEC 61215, IEC 61730, UL 61730, MCS, CE, TUV |
| Country of Origin | text | Country where the module is manufactured | China, Vietnam, Malaysia, India, Germany, USA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus IEC/UL standards (IEC 61215, IEC 61730, UL 61730) and STC/NMOT test conditions | [LONGi Hi-MO 7](https://www.longi.com/en/products/modules/hi-mo-7/), [SunHub Spec Sheet Guide](https://www.sunhub.com/blog/the-ultimate-guide-to-reading-a-solar-panel-spec-sheet/), [A1 Solar Store Datasheet Guide](https://a1solarstore.com/blog/whats-in-the-datasheet-a-guide-to-reading-solar-panel-specs.html), [ENF Solar Panel Directory](https://www.enfsolar.com/pv/panel) |
