# SKU Schema: Diapers & Incontinence Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 54282-BG28, B07DC8BR3B, H01ODPV2S7 |
| Product Name | text | Full product name including brand, line, type, and size | Pampers Swaddlers Diapers Size 4, TENA ProSkin Super Briefs Large, NorthShore MegaMax Tab-Style Briefs |
| URL | text | Direct link to the product page | https://example.com/product/adult-briefs-large |
| Price | number | Numeric price per package or case, excluding currency symbol | 12.99, 34.50, 89.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or product brand name | Pampers, Huggies, TENA, Depend, NorthShore, Tranquility, Prevail |
| Product Type | enum | Primary product form | Baby Diaper, Adult Brief, Pull-On Underwear, Pad, Liner, Booster Pad, Underpad |
| Target User | enum | Intended wearer demographic | Baby, Toddler, Youth, Adult Male, Adult Female, Adult Unisex |
| Size | text | Labeled size designation | Newborn, Size 1, Size 6, Small, Medium, Large, XL, XXL |
| Weight Range | text (lbs) | Body weight range the product is designed for | 8-14, 22-37, 34-47 in (hip), 120-175 lbs |
| Waist/Hip Range | text (in) | Waist or hip circumference range for adult products | 34-47, 48-59, 60-64 |
| Absorbency Level | text | Manufacturer-stated absorbency tier or capacity | Light, Moderate, Heavy, Maximum, Overnight, Super |
| Absorbency Capacity | number (mL) | Measured fluid capacity in millilitres where published | 500, 1200, 2500, 4000 |
| Closure Type | enum | Fastening mechanism | Tabs (Refastenable), Pull-On, Velcro, Hook-and-Loop |
| Pack Quantity | number | Number of individual items per pack or bag | 20, 28, 72, 150, 198 |
| Case Quantity | number | Number of individual items per case or total count in bulk packaging | 96, 150, 252 |
| Material Composition | text (list) | Key materials in the product | Polypropylene, Cellulose Fluff Pulp, Sodium Polyacrylate, Polyethylene |
| Wetness Indicator | boolean | Whether the product includes a color-changing wetness indicator | true, false |
| Leak Guard Feature | text | Leak prevention technology or barrier description | All-Around LeakGuard, Dual Barrier Leg Cuffs, Standing Leak Guards |
| Fragrance | enum | Whether the product is scented or unscented | Fragrance-Free, Scented |
| Latex Free | boolean | Whether the product is free of natural rubber latex | true, false |
| Chlorine Free | boolean | Whether the product is free of elemental chlorine bleaching | true, false |
| Hypoallergenic | boolean | Whether the product is dermatologist-tested and hypoallergenic | true, false |
| Overnight Rated | boolean | Whether the product is specifically designed for extended overnight wear | true, false |
| Product Line | text | Sub-brand or product line within the brand | Swaddlers, Baby-Dry, Pure Protection, ProSkin, MegaMax |
| Skin Care Feature | text | Built-in skin care ingredients or treatments | Aloe, Vitamin E, Shea Butter, Moisture Barrier Cream |
| Reusable | boolean | Whether the product is washable and reusable versus disposable | true, false |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, Poland, Japan |
| Certifications | text (list) | Relevant safety or environmental certifications | Dermatologist Tested, OEKO-TEX, FSC, Cradle to Cradle |
| UPC | text | Universal Product Code barcode number | 037000862161, 768702534284 |
| Package Dimensions | text (cm) | Packaged dimensions length x width x height | 40.6 x 30.5 x 17.8 |
| Package Weight | number (kg) | Total weight of the package or case | 2.3, 4.8, 9.1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISO 15621, ASTM D7619) | [Pampers](https://www.pampers.com/en-us/baby/diapering/article/diaper-size-and-weight-chart), [NorthShore Care](https://www.northshorecare.com/adult-diapers), [TENA](https://www.tena.us/professionals/products/), [The Honest Company](https://www.honest.com/baby-products/view-all-baby) |
