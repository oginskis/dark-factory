# SKU Schema: Glass Containers (Bottles, Jars)

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.glass_containers`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | 4225B11-B, ARD-12HRT-AG, OI-750BG-FL |
| Product Name | product_name | text | — | Full product name including key specs such as container type, capacity, and color | 16oz Clear Glass French Square Bottle, Ardagh 12oz Heritage Amber Beer Bottle, O-I 750ml Flint Bordeaux Wine Bottle |
| URL | url | text | — | Direct link to the product page | https://example.com/product/16oz-french-square |
| Price | price | number | — | Numeric price per unit or per case, excluding currency symbol | 0.35, 0.72, 1.50, 52.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Container Type | container_type | enum | — | General shape category of the glass container | Bottle, Jar, Vial, Jug, Carboy, Growler, Flask, Ampoule |
| Glass Type | glass_type | text | — | Glass material classification | Type I Borosilicate, Type II Treated Soda-Lime, Type III Soda-Lime |
| Closure Type | closure_type | text | — | Type of cap or closure compatible with the container | Screw Cap, Lug Cap, Crown Cap, Cork, ROPP (Roll-On Pilfer-Proof), Swing Top, Snap-On, Pump, Sprayer |
| Country of Origin | country_of_origin | text | — | Country where the container was manufactured | USA, Mexico, France, Germany, Italy, China, India |
| Capacity | capacity | number | ml | Nominal liquid volume capacity | 5, 15, 30, 60, 120, 250, 375, 500, 750, 1000, 1500, 4000 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Shape | shape | text | — | Specific shape or silhouette of the container | Boston Round, French Square, Packer, Bordeaux, Burgundy, Long Neck, Flagon, Mason, Wide Mouth, Cylinder |
| Color | color | enum | — | Glass color or tint | Flint (Clear), Amber, Green, Cobalt Blue, Dead Leaf Green, Antique Green, Frosted, Opaque White |
| Neck Finish | neck_finish | text | — | Standardized neck thread specification (GPI/SPI standard) | 28-400, 33-400, 38-400, 43-400, 48-400, 53-400, 70-400, 63-2030 Lug, 26mm Crown |
| Height | height | number | mm | Overall height of the container from base to top of finish | 42, 68, 102, 148, 168, 225, 292, 338 |
| Body Width | body_width | number | mm | External width for non-round containers (square, oval) | 40, 52, 60, 69, 86, 95 |
| Wall Thickness | wall_thickness | number | mm | Nominal wall thickness of the container | 1.5, 2.0, 2.5, 3.0, 4.0, 5.0 |
| Label Panel Height | label_panel_height | number | mm | Height of the label-friendly panel area | 25, 38, 50, 75, 95, 110 |
| Label Panel Width | label_panel_width | number | mm | Width or circumference of the label panel area | 30, 46, 55, 80, 100, 150, 200 |
| Case Pack Quantity | case_pack_quantity | number | — | Number of containers per case or carton | 6, 12, 24, 36, 40, 48, 72 |
| Pallet Quantity | pallet_quantity | number | — | Number of containers per full pallet | 600, 1200, 1800, 2200, 3600 |
| FDA Food Contact | fda_food_contact | boolean | — | Whether the container is FDA compliant for food/beverage contact | true, false |
| Recyclable | recyclable | boolean | — | Whether the container is recyclable in standard glass streams | true, false |
| Market Segment | market_segment | text (list) | — | Primary end-use markets for the container | Food, Beverage, Beer, Wine, Spirits, Pharmaceutical, Cosmetic, Essential Oil, Candle |
| Minimum Order Quantity | minimum_order_quantity | number | — | Minimum purchase quantity from the manufacturer | 1, 12, 144, 1000, 5000, 100000 |
| Decoration Options | decoration_options | text (list) | — | Available decoration or branding methods | Screen Print, Decal, Embossing, Debossing, Sleeve Label, Spray Coating, Acid Etch, Organic Coating |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus GPI finish standards and ASTM E438 | [Berlin Packaging](https://www.berlinpackaging.com/4225b11-b-16-oz-clear-glass-french-square-bottles-cap-not-included/), [Ardagh Group](https://northamerica.ardaghproducts.com/), [O-I Glass](https://glass-catalog.com/eu-en/catalog), [Container and Packaging](https://www.containerandpackaging.com/catalog/glass-containers) |
