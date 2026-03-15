# SKU Schema: Wood Flooring & Decking

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber
**Taxonomy ID:** `wood.flooring_decking`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | LLBWPRENWOS7, TRX-SEL-PG-16, ADV-IPE-5/4x6 |
| Product Name | product_name | text | Full product name including species or collection, size, and finish | Bellawood 5/8in Select White Oak Engineered Hardwood 7.4in Wide, Trex Select Pebble Grey 1x6 16ft |
| URL | url | text | Direct link to the product page | https://example.com/product/white-oak-engineered-7-4 |
| Price | price | number | Numeric price per unit (per sq ft, per linear ft, or per piece) excluding currency symbol | 7.64, 3.50, 42.99 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Category | product_category | enum | Whether the product is flooring or decking | Solid Hardwood Flooring, Engineered Hardwood Flooring, Composite Decking, Wood Decking, Deck Tile |
| Material Type | material_type | enum | Primary material composition | Solid Wood, Engineered Wood, Composite, PVC, Thermally Modified Wood |
| Finish Type | finish_type | text | Surface finish or coating applied | Prefinished Aluminum Oxide, UV Urethane, Unfinished, Factory Oiled, Wire Brushed |
| Grade | grade | text | Quality or appearance grade of the wood | Select, Character, Rustic, Utility, Clear, Natural, Premium |
| Installation Grade | installation_grade | text (list) | Suitable subfloor levels | Above Grade, On Grade, Below Grade |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the product was manufactured or harvested | USA, Brazil, Indonesia, Canada, Germany |
| Species | species | text | Wood species or composite material description | White Oak, Ipe, Cumaru, Teak, Western Red Cedar, Garapa, Thermally Modified Ash |
| Thickness | thickness | text (in) | Board thickness as nominal or actual measurement | 3/4, 5/8, 5/4, 0.94, 0.82 |
| Width | width | number (in) | Board face width | 2.25, 3.5, 5.4, 5.5, 7.4 |
| Profile | profile | enum | Board edge and face profile type | Standard, Pre-Grooved, Tongue and Groove, Square Edge, Eased Edge, Grooved |
| Finish Sheen | finish_sheen | enum | Level of gloss on the surface finish | Matte, Satin, Semi-Gloss, Gloss |
| Texture | texture | enum | Surface texture of the board | Smooth, Wire Brushed, Hand Scraped, Distressed, Embossed Wood Grain |
| Janka Hardness | janka_hardness | number (lbf) | Resistance to denting measured by the Janka test | 510, 1070, 1650, 2170, 3190, 3680 |
| Veneer Thickness | veneer_thickness | number (mm) | Thickness of the top wear layer for engineered products | 0.6, 2, 3, 4, 6 |
| Installation Method | installation_method | text (list) | Supported installation methods | Nail, Glue, Float, Click-Lock, Hidden Fastener, Screw |
| Radiant Heat Compatible | radiant_heat_compatible | boolean | Whether the product is compatible with radiant heating systems | true, false |
| Coverage per Box | coverage_per_box | number (sqft) | Square feet of flooring per box or bundle | 14.00, 20.04, 23.50 |
| Warranty Duration | warranty_duration | text | Length of product warranty | 25 years, 50 years, 100 years Residential, Lifetime |
| Certification | certification | text (list) | Environmental and chain-of-custody certifications | FSC, PEFC, FloorScore, GreenGuard Gold, CARB Phase 2 |
| Durability Rating | durability_rating | text | Natural decay or weather resistance rating | Class 1 (Very Durable), Class 2, Class 3, 75+ years, 30+ years |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ASTM D2394, EN 13501, CARB Phase 2) | [Advantage Lumber](https://www.advantagelumber.com/wood-decking.htm), [Lumber Liquidators](https://lumberliquidators.com/products/bwpr-eng-white-oak-5-8-x-7-4-sel), [Trex](https://www.trex.com/products/decking/), [Nova USA Wood](https://www.novausawood.com/) |
