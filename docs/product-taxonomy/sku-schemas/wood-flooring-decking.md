# SKU Schema: Wood Flooring & Decking

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | LLBWPRENWOS7, TRX-SEL-PG-16, ADV-IPE-5/4x6 |
| Product Name | text | Full product name including species or collection, size, and finish | Bellawood 5/8in Select White Oak Engineered Hardwood 7.4in Wide, Trex Select Pebble Grey 1x6 16ft |
| URL | text | Direct link to the product page | https://example.com/product/white-oak-engineered-7-4 |
| Price | number | Numeric price per unit (per sq ft, per linear ft, or per piece) excluding currency symbol | 7.64, 3.50, 42.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Flooring or decking manufacturer or brand name | Bellawood, Trex, TimberTech, Advantage Lumber, Nova USA Wood |
| Product Category | enum | Whether the product is flooring or decking | Solid Hardwood Flooring, Engineered Hardwood Flooring, Composite Decking, Wood Decking, Deck Tile |
| Species | text | Wood species or composite material description | White Oak, Ipe, Cumaru, Teak, Western Red Cedar, Garapa, Thermally Modified Ash |
| Material Type | enum | Primary material composition | Solid Wood, Engineered Wood, Composite, PVC, Thermally Modified Wood |
| Thickness | text (in) | Board thickness as nominal or actual measurement | 3/4, 5/8, 5/4, 0.94, 0.82 |
| Width | number (in) | Board face width | 2.25, 3.5, 5.4, 5.5, 7.4 |
| Length | text (ft) | Board length or range of lengths | 12, 16, 20, Random (1-7ft) |
| Profile | enum | Board edge and face profile type | Standard, Pre-Grooved, Tongue and Groove, Square Edge, Eased Edge, Grooved |
| Finish Type | text | Surface finish or coating applied | Prefinished Aluminum Oxide, UV Urethane, Unfinished, Factory Oiled, Wire Brushed |
| Finish Sheen | enum | Level of gloss on the surface finish | Matte, Satin, Semi-Gloss, Gloss |
| Texture | enum | Surface texture of the board | Smooth, Wire Brushed, Hand Scraped, Distressed, Embossed Wood Grain |
| Grade | text | Quality or appearance grade of the wood | Select, Character, Rustic, Utility, Clear, Natural, Premium |
| Janka Hardness | number (lbf) | Resistance to denting measured by the Janka test | 510, 1070, 1650, 2170, 3190, 3680 |
| Veneer Thickness | number (mm) | Thickness of the top wear layer for engineered products | 0.6, 2, 3, 4, 6 |
| Installation Method | text (list) | Supported installation methods | Nail, Glue, Float, Click-Lock, Hidden Fastener, Screw |
| Installation Grade | text (list) | Suitable subfloor levels | Above Grade, On Grade, Below Grade |
| Radiant Heat Compatible | boolean | Whether the product is compatible with radiant heating systems | true, false |
| Coverage per Box | number (sqft) | Square feet of flooring per box or bundle | 14.00, 20.04, 23.50 |
| Warranty Duration | text | Length of product warranty | 25 years, 50 years, 100 years Residential, Lifetime |
| Certification | text (list) | Environmental and chain-of-custody certifications | FSC, PEFC, FloorScore, GreenGuard Gold, CARB Phase 2 |
| Durability Rating | text | Natural decay or weather resistance rating | Class 1 (Very Durable), Class 2, Class 3, 75+ years, 30+ years |
| Recycled Content | number (%) | Percentage of recycled material in composite products | 0, 50, 95 |
| Color | text | Product color name or description | Pebble Grey, Saddle, Golden Teak, Natural, Havana Gold |
| Expected Lifespan | text | Estimated product service life | 25 years, 30+ years, 50+ years, 75+ years |
| Country of Origin | text | Country where the product was manufactured or harvested | USA, Brazil, Indonesia, Canada, Germany |
| Fire Rating | text | Fire performance classification where applicable | Class A, Class B, Class C, Bfl-s1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ASTM D2394, EN 13501, CARB Phase 2) | [Advantage Lumber](https://www.advantagelumber.com/wood-decking.htm), [Lumber Liquidators](https://lumberliquidators.com/products/bwpr-eng-white-oak-5-8-x-7-4-sel), [Trex](https://www.trex.com/products/decking/), [Nova USA Wood](https://www.novausawood.com/) |
