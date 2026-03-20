# SKU Schema: Dental Equipment & Supplies

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.dental_equipment_supplies`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor catalog number | 1002809, 073-4560, ADC-511-BLK |
| Product Name | product_name | text | — | yes | Full product name including type, brand, and key specification | A-dec 511 Dental Chair, Henry Schein Blu-Mousse VPS Impression Material, Brasseler H48.11.016 Carbide Bur |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/a-dec-511-dental-chair |
| Price | price | number | — | yes | Catalog or sale price per unit, pack, or kit | 8.50, 65.00, 4500.00, 18000.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Category | product_category | enum | — | — | Primary dental product classification | Dental Chair, Delivery System, Handpiece, Bur/Diamond, Impression Material, Restorative Material, Imaging System, Sterilizer, Curing Light, Scaler, Anesthetic, Cement, Endodontic Instrument, Orthodontic Supply |
| Sub-Category | sub-category | text | — | — | More specific product type within the category | High-Speed Handpiece, Carbide Bur, VPS Impression, Composite Resin, Panoramic X-Ray, Autoclave, LED Curing Light |
| Material Composition | material_composition | text | — | — | Primary material or active ingredient of the product | Stainless Steel, Tungsten Carbide, Vinyl Polysiloxane, Bis-GMA Composite, Porcelain, Zirconia, Titanium |
| Speed Classification | speed_classification | enum | — | — | Rotational speed category for handpieces and burs | High-Speed (300000-450000 RPM), Low-Speed (5000-40000 RPM), Electric (up to 200000 RPM) |
| Shank Type | shank_type | enum | — | — | Handpiece attachment fitting standard for rotary instruments | FG (Friction Grip), RA (Right Angle/Latch), HP (Handpiece/Straight), CA (Contra Angle) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Connection Type | connection_type | text | — | — | Coupling interface for handpieces and equipment | Midwest 4-Hole, Midwest 5-Hole, ISO 4-Hole, KaVo MULTIflex, E-Type |
| Grit/Coarseness | gritcoarseness | enum | — | — | Abrasive grade for burs, diamonds, and polishing products | Extra-Fine, Fine, Medium, Coarse, Super-Coarse |
| Shade/Color | shadecolor | text | — | — | Product color or dental shade designation | A1, A2, A3, B1, C2, Translucent, Universal |
| Imaging Technology | imaging_technology | enum | — | — | Detection method for diagnostic imaging products | Digital Sensor (CMOS/CCD), Phosphor Plate (PSP), Panoramic, CBCT (Cone Beam CT), Intraoral Camera |
| Image Resolution | image_resolution | text | — | — | Sensor or detector resolution specification | 20 lp/mm, 33 lp/mm, 96 x 96 um pixel |
| FOV | fov | text | cm | — | Field of view for CBCT and panoramic imaging systems | 5 x 5 cm, 8 x 8 cm, 13 x 16 cm, 23 x 17 cm |
| Sterilization Method | sterilization_method | enum | — | — | Compatible or recommended sterilization process | Steam Autoclave (134 C), Chemical Vapor, Ethylene Oxide, Cold Sterilant, Single-Use Disposable |
| Light Intensity | light_intensity | number | mW/cm2 | — | Irradiance output for curing lights | 1000, 1600, 2000, 3200 |
| Working Time | working_time | text | — | — | Open time or handling window before material sets | 60 seconds, 90 seconds, 2 minutes, 3.5 minutes |
| Setting Time | setting_time | text | — | — | Total cure or hardening time | 3 minutes, 4.5 minutes, 20 seconds (light cure) |
| Units per Package | units_per_package | number | — | — | Quantity of items per sales unit | 1, 5, 10, 25, 50, 100, 500 |
| Shelf Life | shelf_life | text | — | — | Product shelf life from date of manufacture | 12 months, 24 months, 36 months |
| Latex Free | latex_free | enum | — | — | Whether the product is free of natural rubber latex | Yes, No |
| Power Requirements | power_requirements | text | — | — | Electrical input specification for powered equipment | 100-240 V AC 50/60 Hz, Rechargeable Li-Ion Battery, Pneumatic (80 PSI) |
| Dimensions (L x W x H) | dimensions_l_x_w_x_h | text | mm | — | External dimensions of the product or packaging | 18 x 3.5 (bur), 600 x 450 x 1200 (chair base), 1500 x 900 x 1100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 sources plus ISO dental instrument standards (ISO 6360, ISO 7785) and ADA specifications | [Henry Schein Dental Catalog 2025-2026](https://www.henryschein.com/us-en/dental/default.aspx), [Patterson Dental A-dec Chairs](https://www.pattersondental.com/equipment-technology/operatory/dental-chairs), [Brasseler USA Catalogs](https://brasselerusadental.com/catalogs), [Benco Dental Catalogs](https://www.benco.com/catalogs/) |
