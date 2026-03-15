# SKU Schema: Nutritional Supplements & Vitamins

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.nutritional_supplements_vitamins`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SWU252, NOW-0372, IHB-87432 |
| Product Name | text | Full product name including key active ingredient, strength, and form | Vitamin D3 5000 IU Softgels, Magnesium Glycinate 400 mg Capsules, Omega-3 Fish Oil 1000 mg |
| URL | text | Direct link to the product page | https://example.com/products/vitamin-d3-5000iu |
| Price | number | Numeric price per unit of sale, excluding currency symbol | 12.99, 24.50, 8.75 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Supplement Type | text | Primary category of supplement | Vitamin, Mineral, Herbal, Amino Acid, Probiotic, Omega Fatty Acid, Enzyme |
| Primary Ingredient | text | Main active ingredient or blend name | Cholecalciferol, Magnesium Bisglycinate, EPA/DHA Fish Oil Concentrate, Lactobacillus acidophilus |
| Dosage Form | enum | Physical form of the supplement | Softgel, Capsule, Tablet, Gummy, Powder, Liquid, Lozenge, Chewable |
| Other Ingredients | text (list) | Inactive ingredients including capsule material, fillers, binders, and coatings | Gelatin, Glycerin, Purified Water, Rice Flour, Magnesium Stearate, Cellulose |
| Container Type | text | Packaging format | Bottle, Pouch, Blister Pack, Jar, Box with Packets |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the product is manufactured or bottled | USA, Canada, UK, Germany, Japan |
| Supplement Facts | text (list) | All active nutrients with amounts and percent Daily Value per serving | Vitamin D3 125 mcg 625% DV, Calcium 200 mg 15% DV, Zinc 15 mg 136% DV |
| Allergen Declarations | text (list) | Allergens present or absent as declared on the label | Contains Fish (Anchovy, Sardine), Soy-Free, Gluten-Free, Dairy-Free |
| Dietary Certifications | text (list) | Dietary and lifestyle certifications | Non-GMO, Vegan, Vegetarian, Kosher, Halal, Organic, Paleo-Friendly |
| Third-Party Testing | text (list) | Independent quality verification seals or programs | USP Verified, NSF Certified for Sport, ConsumerLab Approved, iTested |
| GMP Certification | text | Good Manufacturing Practice certification status | cGMP Certified, NPA GMP Certified |
| Suggested Use | text | Recommended dosage instructions as stated on the label | Take 1 softgel daily with a fat-containing meal |
| Warnings | text | Caution and contraindication statements | Consult your healthcare practitioner if pregnant or nursing. Keep out of reach of children. |
| Storage Instructions | text | Recommended storage conditions | Store in a cool dry place. Refrigerate after opening. |
| UPC | text | Universal Product Code barcode number | 733739003720, 087614019048 |
| Health Claim | text | Structure/function claim as printed on the label | Supports Bone Health, Promotes Immune Function, Supports Heart Health |
| Strength per Serving | text | Amount of primary active ingredient per serving with unit | 125 mcg (5000 IU), 400 mg, 1000 mg, 50 Billion CFU |
| Serving Size | text | Recommended serving expressed as count and form | 1 Softgel, 2 Capsules, 1 Tablespoon (15 mL), 1 Scoop (5 g) |
| Servings per Container | number | Total number of servings in the package | 250, 120, 60, 30 |
| Count | number | Total number of units (capsules, tablets, etc.) per container | 250, 120, 60, 90, 180 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus FDA dietary supplement labeling regulations and USP verification standards | [Swanson Vitamins](https://www.swansonvitamins.com/p/swanson-premium-highest-potency-vitamin-d-3-5000-iu-5000-iu-250-sgels), [NOW Foods](https://www.nowfoods.com/products/supplements), [iHerb](https://www.iherb.com/c/supplements), [Fullscript](https://fullscript.com/wholesale-ordering) |
