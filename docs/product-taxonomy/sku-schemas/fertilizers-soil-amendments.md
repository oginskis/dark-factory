# SKU Schema: Fertilizers & Soil Amendments

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DTE-ALFALFA-5LB, FDC-NUTRIVEG-25, BW-PAR4-50 |
| Product Name | text | Full product name including brand, formulation, and size | Down To Earth Alfalfa Meal 5 lb, Fedco NutriVeg 5-4-4 Organic Fertilizer 25 lb, Espoma Garden-tone 3-4-4 18 lb |
| URL | text | Direct link to the product page | https://example.com/products/alfalfa-meal-5lb |
| Price | number | Numeric price per unit excluding currency symbol | 8.99, 14.50, 32.95, 89.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Down To Earth, Espoma, Dr. Earth, Jobe's, Fedco, Bridgewell, Scotts, Miracle-Gro |
| Product Type | enum | Primary functional classification | Granular Fertilizer, Liquid Fertilizer, Wettable Powder, Soil Amendment, Compost, Potting Mix, Inoculant, Mineral Supplement |
| NPK Nitrogen | number (%) | Guaranteed minimum percentage of total nitrogen by weight | 0, 2, 4, 5, 10, 21, 46 |
| NPK Phosphorus | number (%) | Guaranteed minimum percentage of available phosphate (P2O5) by weight | 0, 2, 3, 6, 20, 46 |
| NPK Potassium | number (%) | Guaranteed minimum percentage of soluble potash (K2O) by weight | 0, 2, 3, 4, 9, 18, 60 |
| Secondary Nutrients | text (list) | Additional macro- and secondary nutrients guaranteed on the label | Calcium 5%, Magnesium 3%, Sulfur 4%, Iron 1% |
| Micronutrients | text (list) | Trace elements included in the guaranteed analysis | Boron, Copper, Iron, Manganese, Molybdenum, Zinc |
| Derived From | text (list) | Source materials the nutrients are derived from | Bone Meal, Blood Meal, Fish Meal, Kelp Meal, Feather Meal, Potassium Sulfate, Urea, Ammonium Nitrate |
| Organic Certification | text | Organic listing or certification standard the product meets | OMRI Listed, CDFA OIM, EU Organic, None |
| Product Form | enum | Physical form of the product | Granular, Pelletized, Powder, Liquid Concentrate, Ready-to-Use Liquid, Spike, Tablet |
| Slow Release | boolean | Whether the product contains slow-release or controlled-release nitrogen | true, false |
| Slow Release Percentage | number (%) | Percentage of nitrogen that is water-insoluble or slowly available | 25, 50, 70, 100 |
| Net Weight | number (kg) | Net weight of the package in kilograms | 0.9, 2.3, 4.5, 11.3, 22.7, 50 |
| Net Volume | number (L) | Net volume for liquid products in litres | 0.5, 0.95, 3.78, 9.46, 208 |
| Coverage Area | number (m2) | Area one package will cover at the recommended application rate | 46, 93, 232, 465, 743 |
| Application Rate | text | Recommended dosage per area or per plant as stated on the label | 2.5 kg per 93 m2, 30 mL per L water, 60 g per plant |
| Application Method | enum | Recommended way to apply the product | Broadcast, Side-Dress, Top-Dress, Foliar Spray, Drip Fertigation, Soil Drench, Incorporation |
| Application Season | text (list) | Recommended season or timing for application | Spring, Fall, Pre-Planting, Growing Season, Year-Round |
| Target Crop | text (list) | Crops or plant types the product is formulated for | Vegetables, Lawn, Trees, Roses, Blueberries, Cannabis, Citrus, General Purpose |
| Soil pH Effect | enum | Whether the product raises, lowers, or has no effect on soil pH | Acidifying, Alkalizing, Neutral |
| Contains Biologicals | boolean | Whether the product contains beneficial microorganisms such as mycorrhizae or bacteria | true, false |
| Particle Size | text (mm) | Granule or pellet diameter range for solid products | 1-2, 2-4, 1-4, 0.5-1.5 |
| Bulk Density | number (kg/L) | Packed bulk density of the product | 0.5, 0.7, 0.9, 1.1, 1.3 |
| Hazmat Classification | text | Hazardous material transport classification if applicable | Non-Hazardous, Class 5.1 Oxidizer, None |
| Country of Origin | text | Country where the product is manufactured or mined | USA, Canada, Peru, Morocco, Chile |
| Shelf Life | number (months) | Expected shelf life of the product when stored properly | 12, 24, 36, 60, Indefinite |
| GHS Signal Word | text | Globally Harmonized System signal word if classified as hazardous | None, Warning, Danger |
| Manufacturer | text | Parent company or manufacturer name | The Scotts Miracle-Gro Company, Espoma Company, Down To Earth Fertilizer, Bridgewell Agribusiness |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus AAPFCO labelling standards and OMRI listing requirements | [Down To Earth](https://downtoearthfertilizer.com/products/), [Fedco Seeds Amendments](https://fedcoseeds.com/supplies/amendments-and-fertilizers), [Espoma](https://www.espoma.com/plant-food-basics/reading-labels/), [Bridgewell Agribusiness](https://www.bridgewellab.com/agriculture/) |
