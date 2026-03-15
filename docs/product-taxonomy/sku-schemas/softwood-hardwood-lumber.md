# SKU Schema: Softwood & Hardwood Lumber

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | PAJT4720, 1464, 1000029181 |
| Product Name | text | Full product name including key specs such as species, grade, and dimensions | PEFC C24 Regularised Joist Premium Treated Kiln Dried 47 x 200mm, Red Oak 4/4 Lumber S2S |
| URL | text | Direct link to the product page | https://example.com/product/c24-carcassing-47x200 |
| Price | number | Numeric price per unit (piece, board foot, or cubic metre depending on seller), excluding currency symbol | 11.58, 6.99, 224.50 |
| Currency | text | ISO 4217 currency code | GBP, USD, EUR, CAD, AUD |
| Brand/Manufacturer | text | Timber brand, mill, or supplier name | International Timber, West Fraser, Weyerhaeuser, Accoya |
| Species | text | Wood species common name | Spruce, Pine, Oak, Western Red Cedar, Douglas Fir, Southern Yellow Pine, Ipe |
| Wood Type | enum | Whether the species is a softwood or hardwood | Softwood, Hardwood |
| Nominal Thickness | text (mm) | Nominal (pre-dressing) thickness as stated by the seller. UK/EU in mm, US in inches or quarter notation | 47, 100, 2, 4/4, 8/4 |
| Nominal Width | text (mm) | Nominal (pre-dressing) width. May be a fixed value or random for hardwood boards | 200, 150, 4, 6, Random |
| Length | number (mm) | Board length in millimetres. US lengths often in feet (convert as needed) | 2400, 3600, 4800, 6000 |
| Actual Thickness | number (mm) | Finished thickness after dressing or planing. Always less than nominal | 45, 95, 19, 38 |
| Actual Width | number (mm) | Finished width after dressing or planing | 195, 145, 119, 89 |
| Structural Grade | text | Strength grade for load-bearing use. European: C16, C24, C30. North American: No. 1, No. 2, Select Structural, MSR grades | C16, C24, Select Structural, No. 2 |
| Appearance Grade | text | Visual or appearance grade for non-structural or hardwood use. NHLA grades for hardwood, visual grades for softwood | FAS, FAS/1F, Select, No. 1 Common, No. 2 Common, Clear |
| Treatment Type | text | Preservative treatment applied to the timber | Tanalised, Pressure Treated, CCA, ACQ, Untreated, Heat Treated |
| Use Class | text | Durability classification per EN 335 indicating the intended exposure conditions | UC1, UC2, UC3, UC4, UC5 |
| Moisture Content | text | Drying state of the timber at point of sale | Kiln Dried, Green, Air Dried, KD-HT |
| Surfacing | text | Extent of surface finishing applied to the board | Rough Sawn, S2S, S4S, PAR, Planed Eased Edges, Regularised |
| Application | text (list) | Primary intended uses for the product | Structural Framing, Landscaping, Fencing, Decking, Joinery, Cladding, Flooring |
| Certification | text (list) | Chain-of-custody and sustainability certifications | FSC, PEFC, SFI, FSC Mix |
| Country of Origin | text | Country or region where the timber was sourced | Sweden, Latvia, Brazil, USA, Canada |
| Durability Class | text | Natural durability rating of the species per EN 350 (Class 1 = very durable, Class 5 = not durable) | Class 1, Class 2, Class 3, Class 4, Class 5 |
| Pack Quantity | number | Number of pieces per pack or bundle. 1 if sold individually | 1, 6, 10, 168 |
| Weight per Unit | number (kg) | Weight of a single piece or per board foot/cubic metre | 2.35, 5.20, 12.50 |
| Specific Gravity | number | Density ratio relative to water (dimensionless). Key indicator of hardness and strength | 0.35, 0.55, 0.72, 0.95 |
| Janka Hardness | number (N) | Resistance to denting measured by the Janka test. Higher values indicate harder wood | 1560, 2700, 5400, 16370 |
| Color | text | Typical heartwood and sapwood color description | Pale yellow, Reddish brown, Honey gold, Chocolate brown |
| Grain Pattern | text | Characteristic grain and texture of the species | Straight, Interlocked, Wavy, Fine, Coarse |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (BS 4978, EN 14081, NHLA grading) | [Jewson](https://www.jewson.co.uk/timber/sawn-carcassing-timber/carcassing-timber), [Rex Lumber](https://www.rexlumber.com/lumber/), [Topwood Timber](https://topwoodtimber.co.uk/), [Lowes](https://www.lowes.com/pl/lumber-composites/framing-lumber/dimensional-lumber/4294402500) |
