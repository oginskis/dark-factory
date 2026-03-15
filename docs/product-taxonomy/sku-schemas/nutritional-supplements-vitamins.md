# SKU Schema: Nutritional Supplements & Vitamins

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SWU252, NOW-0372, IHB-87432 |
| Product Name | text | Full product name including key active ingredient, strength, and form | Vitamin D3 5000 IU Softgels, Magnesium Glycinate 400 mg Capsules, Omega-3 Fish Oil 1000 mg |
| URL | text | Direct link to the product page | https://example.com/products/vitamin-d3-5000iu |
| Price | number | Numeric price per unit of sale, excluding currency symbol | 12.99, 24.50, 8.75 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Supplement brand or manufacturer name | NOW Foods, Swanson, Life Extension, Nature Made, Solgar |
| Supplement Type | text | Primary category of supplement | Vitamin, Mineral, Herbal, Amino Acid, Probiotic, Omega Fatty Acid, Enzyme |
| Primary Ingredient | text | Main active ingredient or blend name | Cholecalciferol, Magnesium Bisglycinate, EPA/DHA Fish Oil Concentrate, Lactobacillus acidophilus |
| Strength per Serving | text | Amount of primary active ingredient per serving with unit | 125 mcg (5000 IU), 400 mg, 1000 mg, 50 Billion CFU |
| Serving Size | text | Recommended serving expressed as count and form | 1 Softgel, 2 Capsules, 1 Tablespoon (15 mL), 1 Scoop (5 g) |
| Servings per Container | number | Total number of servings in the package | 250, 120, 60, 30 |
| Dosage Form | enum | Physical form of the supplement | Softgel, Capsule, Tablet, Gummy, Powder, Liquid, Lozenge, Chewable |
| Count | number | Total number of units (capsules, tablets, etc.) per container | 250, 120, 60, 90, 180 |
| Net Weight | text | Total net weight or volume of the product | 250 g, 16 fl oz, 500 mL, 8 oz |
| Supplement Facts | text (list) | All active nutrients with amounts and percent Daily Value per serving | Vitamin D3 125 mcg 625% DV, Calcium 200 mg 15% DV, Zinc 15 mg 136% DV |
| Other Ingredients | text (list) | Inactive ingredients including capsule material, fillers, binders, and coatings | Gelatin, Glycerin, Purified Water, Rice Flour, Magnesium Stearate, Cellulose |
| Allergen Declarations | text (list) | Allergens present or absent as declared on the label | Contains Fish (Anchovy, Sardine), Soy-Free, Gluten-Free, Dairy-Free |
| Dietary Certifications | text (list) | Dietary and lifestyle certifications | Non-GMO, Vegan, Vegetarian, Kosher, Halal, Organic, Paleo-Friendly |
| Third-Party Testing | text (list) | Independent quality verification seals or programs | USP Verified, NSF Certified for Sport, ConsumerLab Approved, iTested |
| GMP Certification | text | Good Manufacturing Practice certification status | cGMP Certified, NPA GMP Certified |
| Suggested Use | text | Recommended dosage instructions as stated on the label | Take 1 softgel daily with a fat-containing meal |
| Warnings | text | Caution and contraindication statements | Consult your healthcare practitioner if pregnant or nursing. Keep out of reach of children. |
| Storage Instructions | text | Recommended storage conditions | Store in a cool dry place. Refrigerate after opening. |
| Container Type | text | Packaging format | Bottle, Pouch, Blister Pack, Jar, Box with Packets |
| Container Material | enum | Primary material of the container | Plastic (HDPE), Glass, BPA-Free Plastic |
| Capsule Material | text | Shell material for encapsulated products | Bovine Gelatin, Fish Gelatin, Hydroxypropyl Methylcellulose (HPMC), Pullulan |
| Country of Origin | text | Country where the product is manufactured or bottled | USA, Canada, UK, Germany, Japan |
| UPC | text | Universal Product Code barcode number | 733739003720, 087614019048 |
| Product Weight | number (g) | Shipping or gross weight of the packaged product | 180, 340, 95, 520 |
| Product Dimensions | text (mm) | Package dimensions length x width x height | 65 x 65 x 120, 80 x 80 x 150 |
| Expiration Date Format | text | How expiration is expressed on the product | Best By date, Expiration date, MFG date + shelf life |
| Health Claim | text | Structure/function claim as printed on the label | Supports Bone Health, Promotes Immune Function, Supports Heart Health |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus FDA dietary supplement labeling regulations and USP verification standards | [Swanson Vitamins](https://www.swansonvitamins.com/p/swanson-premium-highest-potency-vitamin-d-3-5000-iu-5000-iu-250-sgels), [NOW Foods](https://www.nowfoods.com/products/supplements), [iHerb](https://www.iherb.com/c/supplements), [Fullscript](https://fullscript.com/wholesale-ordering) |
