# SKU Schema: Skincare Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.skincare`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 0301871120, P455418, B00F97FHAW |
| Product Name | text | Full product name including brand, line, product type, and size | CeraVe AM Facial Moisturizing Lotion SPF 30 2 fl oz, The Ordinary Niacinamide 10% + Zinc 1% 30ml |
| URL | text | Direct link to the product page | https://www.cerave.com/skincare/moisturizers/am-facial-moisturizing-lotion-with-sunscreen |
| Price | number | Numeric unit price excluding currency symbol | 16.99, 7.90, 52.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Product Type | enum | Primary product classification | Moisturizer, Serum, Cleanser, Toner, Sunscreen, Eye Cream, Face Mask, Exfoliant, Face Oil, Essence, Ampoule, Lip Treatment, Retinol Treatment |
| UV Filter Type | enum | Type of UV protection system used | Chemical, Mineral, Hybrid, None |
| Skin Type | text (list) | Targeted skin type | Normal, Dry, Oily, Combination, Sensitive, All Skin Types |
| Key Active Ingredients | text (list) | Primary active or featured ingredients | Hyaluronic Acid, Niacinamide, Retinol, Vitamin C, Salicylic Acid, Ceramides, Peptides, AHA, BHA |
| Active Ingredient Concentration | text | Concentration of key actives when disclosed | 10% Niacinamide, 0.5% Retinol, 15% Vitamin C, 2% Salicylic Acid |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| INCI Ingredients | text | Full INCI ingredient list from packaging | Water, Homosalate, Niacinamide, Cetearyl Alcohol, Glycerin |
| Formulation | enum | Physical form of the product | Lotion, Cream, Gel, Gel-Cream, Serum, Oil, Foam, Balm, Mist, Essence, Emulsion, Stick |
| Packaging Material | text | Primary packaging material | Plastic Tube, Glass Bottle, Plastic Bottle, Airless Pump, Jar |
| Country of Origin | text | Country where the product is manufactured | USA, France, South Korea, Japan, Germany, Canada |
| Volume | number (ml) | Volume of the product | 30, 50, 60, 75, 100, 200 |
| SPF | number | Sun protection factor when present | 15, 30, 40, 50, 50+ |
| Skin Concern | text (list) | Skin concerns the product addresses | Acne, Aging, Dark Spots, Dullness, Dryness, Redness, Pores, Wrinkles, Uneven Tone |
| Fragrance Free | enum | Whether the product is fragrance-free | Yes, No |
| Non-Comedogenic | enum | Whether the product is non-comedogenic (will not clog pores) | Yes, No |
| Dermatologist Tested | enum | Whether the product has been tested by dermatologists | Yes, No |
| Allergy Tested | enum | Whether the product has undergone allergy testing | Yes, No |
| Oil Free | enum | Whether the product is oil-free | Yes, No |
| Paraben Free | enum | Whether the product is free of parabens | Yes, No |
| Cruelty Free | enum | Whether the product is certified cruelty-free | Yes, No |
| Vegan | enum | Whether the product contains no animal-derived ingredients | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus ISO 22716 and EU cosmetic regulations | [CeraVe AM Moisturizing Lotion SPF 30](https://www.cerave.com/skincare/moisturizers/am-facial-moisturizing-lotion-with-sunscreen), [The Ordinary](https://theordinary.com), [ILIA Super Serum Skin Tint](https://www.sephora.com/product/ilia-super-serum-skin-tint-spf-40-P455418), [EWG Skin Deep Database](http://www.ewg.org/skindeep/) |
