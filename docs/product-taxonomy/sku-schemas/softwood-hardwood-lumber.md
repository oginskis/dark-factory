# SKU Schema: Softwood & Hardwood Lumber

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber
**Taxonomy ID:** `wood.softwood_hardwood_lumber`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | PAJT4720, 1464, 1000029181 |
| Product Name | product_name | text | Full product name including key specs such as species, grade, and dimensions | PEFC C24 Regularised Joist Premium Treated Kiln Dried 47 x 200mm, Red Oak 4/4 Lumber S2S |
| URL | url | text | Direct link to the product page | https://example.com/product/c24-carcassing-47x200 |
| Price | price | number | Numeric price per unit (piece, board foot, or cubic metre depending on seller), excluding currency symbol | 11.58, 6.99, 224.50 |
| Currency | currency | text | ISO 4217 currency code | GBP, USD, EUR, CAD, AUD |
| Wood Type | wood_type | enum | Whether the species is a softwood or hardwood | Softwood, Hardwood |
| Structural Grade | structural_grade | text | Strength grade for load-bearing use. European: C16, C24, C30. North American: No. 1, No. 2, Select Structural, MSR grades | C16, C24, Select Structural, No. 2 |
| Appearance Grade | appearance_grade | text | Visual or appearance grade for non-structural or hardwood use. NHLA grades for hardwood, visual grades for softwood | FAS, FAS/1F, Select, No. 1 Common, No. 2 Common, Clear |
| Treatment Type | treatment_type | text | Preservative treatment applied to the timber | Tanalised, Pressure Treated, CCA, ACQ, Untreated, Heat Treated |
| Use Class | use_class | text | Durability classification per EN 335 indicating the intended exposure conditions | UC1, UC2, UC3, UC4, UC5 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country or region where the timber was sourced | Sweden, Latvia, Brazil, USA, Canada |
| Durability Class | durability_class | text | Natural durability rating of the species per EN 350 (Class 1 = very durable, Class 5 = not durable) | Class 1, Class 2, Class 3, Class 4, Class 5 |
| Species | species | text | Wood species common name | Spruce, Pine, Oak, Western Red Cedar, Douglas Fir, Southern Yellow Pine, Ipe |
| Nominal Thickness | nominal_thickness | text (mm) | Nominal (pre-dressing) thickness as stated by the seller. UK/EU in mm, US in inches or quarter notation | 47, 100, 2, 4/4, 8/4 |
| Nominal Width | nominal_width | text (mm) | Nominal (pre-dressing) width. May be a fixed value or random for hardwood boards | 200, 150, 4, 6, Random |
| Actual Thickness | actual_thickness | number (mm) | Finished thickness after dressing or planing. Always less than nominal | 45, 95, 19, 38 |
| Actual Width | actual_width | number (mm) | Finished width after dressing or planing | 195, 145, 119, 89 |
| Moisture Content | moisture_content | text | Drying state of the timber at point of sale | Kiln Dried, Green, Air Dried, KD-HT |
| Surfacing | surfacing | text | Extent of surface finishing applied to the board | Rough Sawn, S2S, S4S, PAR, Planed Eased Edges, Regularised |
| Application | application | text (list) | Primary intended uses for the product | Structural Framing, Landscaping, Fencing, Decking, Joinery, Cladding, Flooring |
| Certification | certification | text (list) | Chain-of-custody and sustainability certifications | FSC, PEFC, SFI, FSC Mix |
| Pack Quantity | pack_quantity | number | Number of pieces per pack or bundle. 1 if sold individually | 1, 6, 10, 168 |
| Specific Gravity | specific_gravity | number | Density ratio relative to water (dimensionless). Key indicator of hardness and strength | 0.35, 0.55, 0.72, 0.95 |
| Janka Hardness | janka_hardness | number (N) | Resistance to denting measured by the Janka test. Higher values indicate harder wood | 1560, 2700, 5400, 16370 |
| Color | color | text | Typical heartwood and sapwood color description | Pale yellow, Reddish brown, Honey gold, Chocolate brown |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (BS 4978, EN 14081, NHLA grading) | [Jewson](https://www.jewson.co.uk/timber/sawn-carcassing-timber/carcassing-timber), [Rex Lumber](https://www.rexlumber.com/lumber/), [Topwood Timber](https://topwoodtimber.co.uk/), [Lowes](https://www.lowes.com/pl/lumber-composites/framing-lumber/dimensional-lumber/4294402500) |
