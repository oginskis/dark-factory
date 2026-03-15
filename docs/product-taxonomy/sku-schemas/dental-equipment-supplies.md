# SKU Schema: Dental Equipment & Supplies

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.dental_equipment_supplies`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor catalog number | 1002809, 073-4560, ADC-511-BLK |
| Product Name | text | Full product name including type, brand, and key specification | A-dec 511 Dental Chair, Henry Schein Blu-Mousse VPS Impression Material, Brasseler H48.11.016 Carbide Bur |
| URL | text | Direct link to the product page | https://example.com/product/a-dec-511-dental-chair |
| Price | number | Catalog or sale price per unit, pack, or kit | 8.50, 65.00, 4500.00, 18000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Primary dental product classification | Dental Chair, Delivery System, Handpiece, Bur/Diamond, Impression Material, Restorative Material, Imaging System, Sterilizer, Curing Light, Scaler, Anesthetic, Cement, Endodontic Instrument, Orthodontic Supply |
| Sub-Category | text | More specific product type within the category | High-Speed Handpiece, Carbide Bur, VPS Impression, Composite Resin, Panoramic X-Ray, Autoclave, LED Curing Light |
| Material Composition | text | Primary material or active ingredient of the product | Stainless Steel, Tungsten Carbide, Vinyl Polysiloxane, Bis-GMA Composite, Porcelain, Zirconia, Titanium |
| Speed Classification | enum | Rotational speed category for handpieces and burs | High-Speed (300000-450000 RPM), Low-Speed (5000-40000 RPM), Electric (up to 200000 RPM) |
| Shank Type | enum | Handpiece attachment fitting standard for rotary instruments | FG (Friction Grip), RA (Right Angle/Latch), HP (Handpiece/Straight), CA (Contra Angle) |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Connection Type | text | Coupling interface for handpieces and equipment | Midwest 4-Hole, Midwest 5-Hole, ISO 4-Hole, KaVo MULTIflex, E-Type |
| Grit/Coarseness | enum | Abrasive grade for burs, diamonds, and polishing products | Extra-Fine, Fine, Medium, Coarse, Super-Coarse |
| Shade/Color | text | Product color or dental shade designation | A1, A2, A3, B1, C2, Translucent, Universal |
| Imaging Technology | enum | Detection method for diagnostic imaging products | Digital Sensor (CMOS/CCD), Phosphor Plate (PSP), Panoramic, CBCT (Cone Beam CT), Intraoral Camera |
| Image Resolution | text | Sensor or detector resolution specification | 20 lp/mm, 33 lp/mm, 96 x 96 um pixel |
| FOV | text (mm) | Field of view for CBCT and panoramic imaging systems | 5 x 5 cm, 8 x 8 cm, 13 x 16 cm, 23 x 17 cm |
| Sterilization Method | enum | Compatible or recommended sterilization process | Steam Autoclave (134 C), Chemical Vapor, Ethylene Oxide, Cold Sterilant, Single-Use Disposable |
| Light Intensity | number (mW/cm2) | Irradiance output for curing lights | 1000, 1600, 2000, 3200 |
| Working Time | text | Open time or handling window before material sets | 60 seconds, 90 seconds, 2 minutes, 3.5 minutes |
| Setting Time | text | Total cure or hardening time | 3 minutes, 4.5 minutes, 20 seconds (light cure) |
| Units per Package | number | Quantity of items per sales unit | 1, 5, 10, 25, 50, 100, 500 |
| Shelf Life | text | Product shelf life from date of manufacture | 12 months, 24 months, 36 months |
| Latex Free | enum | Whether the product is free of natural rubber latex | Yes, No |
| Power Requirements | text | Electrical input specification for powered equipment | 100-240 V AC 50/60 Hz, Rechargeable Li-Ion Battery, Pneumatic (80 PSI) |
| Dimensions (L x W x H) | text (mm) | External dimensions of the product or packaging | 18 x 3.5 (bur), 600 x 450 x 1200 (chair base), 1500 x 900 x 1100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 sources plus ISO dental instrument standards (ISO 6360, ISO 7785) and ADA specifications | [Henry Schein Dental Catalog 2025-2026](https://www.henryschein.com/us-en/dental/default.aspx), [Patterson Dental A-dec Chairs](https://www.pattersondental.com/equipment-technology/operatory/dental-chairs), [Brasseler USA Catalogs](https://brasselerusadental.com/catalogs), [Benco Dental Catalogs](https://www.benco.com/catalogs/) |
