# SKU Schema: Diapers & Incontinence Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.diapers_incontinence`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 54282-BG28, B07DC8BR3B, H01ODPV2S7 |
| Product Name | product_name | text | — | Full product name including brand, line, type, and size | Pampers Swaddlers Diapers Size 4, TENA ProSkin Super Briefs Large, NorthShore MegaMax Tab-Style Briefs |
| URL | url | text | — | Direct link to the product page | https://example.com/product/adult-briefs-large |
| Price | price | number | — | Numeric price per package or case, excluding currency symbol | 12.99, 34.50, 89.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary product form | Baby Diaper, Adult Brief, Pull-On Underwear, Pad, Liner, Booster Pad, Underpad |
| Closure Type | closure_type | enum | — | Fastening mechanism | Tabs (Refastenable), Pull-On, Velcro, Hook-and-Loop |
| Material Composition | material_composition | text (list) | — | Key materials in the product | Polypropylene, Cellulose Fluff Pulp, Sodium Polyacrylate, Polyethylene |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, Mexico, Poland, Japan |
| Size | size | text | — | Labeled size designation | Newborn, Size 1, Size 6, Small, Medium, Large, XL, XXL |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Target User | target_user | enum | — | Intended wearer demographic | Baby, Toddler, Youth, Adult Male, Adult Female, Adult Unisex |
| Waist/Hip Range | waisthip_range | text | in | Waist or hip circumference range for adult products | 34-47, 48-59, 60-64 |
| Absorbency Level | absorbency_level | text | — | Manufacturer-stated absorbency tier or capacity | Light, Moderate, Heavy, Maximum, Overnight, Super |
| Pack Quantity | pack_quantity | number | — | Number of individual items per pack or bag | 20, 28, 72, 150, 198 |
| Case Quantity | case_quantity | number | — | Number of individual items per case or total count in bulk packaging | 96, 150, 252 |
| Wetness Indicator | wetness_indicator | boolean | — | Whether the product includes a color-changing wetness indicator | true, false |
| Leak Guard Feature | leak_guard_feature | text | — | Leak prevention technology or barrier description | All-Around LeakGuard, Dual Barrier Leg Cuffs, Standing Leak Guards |
| Fragrance | fragrance | enum | — | Whether the product is scented or unscented | Fragrance-Free, Scented |
| Latex Free | latex_free | boolean | — | Whether the product is free of natural rubber latex | true, false |
| Chlorine Free | chlorine_free | boolean | — | Whether the product is free of elemental chlorine bleaching | true, false |
| Hypoallergenic | hypoallergenic | boolean | — | Whether the product is dermatologist-tested and hypoallergenic | true, false |
| Overnight Rated | overnight_rated | boolean | — | Whether the product is specifically designed for extended overnight wear | true, false |
| Product Line | product_line | text | — | Sub-brand or product line within the brand | Swaddlers, Baby-Dry, Pure Protection, ProSkin, MegaMax |
| Skin Care Feature | skin_care_feature | text | — | Built-in skin care ingredients or treatments | Aloe, Vitamin E, Shea Butter, Moisture Barrier Cream |
| Reusable | reusable | boolean | — | Whether the product is washable and reusable versus disposable | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISO 15621, ASTM D7619) | [Pampers](https://www.pampers.com/en-us/baby/diapering/article/diaper-size-and-weight-chart), [NorthShore Care](https://www.northshorecare.com/adult-diapers), [TENA](https://www.tena.us/professionals/products/), [The Honest Company](https://www.honest.com/baby-products/view-all-baby) |
