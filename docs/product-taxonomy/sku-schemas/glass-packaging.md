# SKU Schema: Glass Packaging

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.glass`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | ARD-8018855, SKS-GB-16BRF, OBK-GJ-8OZ |
| Product Name | product_name | text | Full product name including capacity, color, shape, and neck finish | 750ml Claret Inspiration Eco Series Flint, 16 oz Amber Boston Round 28-400, 8 oz Clear Wide Mouth Jar 70-450 |
| URL | url | text | Direct link to the product page | https://example.com/glass/750ml-claret-flint |
| Price | price | number | Numeric price per unit or per case, excluding currency symbol | 0.65, 1.20, 12.25, 48.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Container Type | container_type | enum | Broad format classification of the glass package | Bottle, Jar, Jug, Vial, Carafe, Growler, Demijohn |
| Glass Type | glass_type | enum | Composition category of the glass | Flint (Clear), Amber, Green, Cobalt Blue, Opal (Frosted), Champagne Green, Antique Green, Dead Leaf Green |
| Glass Composition | glass_composition | enum | Chemical composition of the glass formulation | Soda-Lime, Borosilicate, Type I (Neutral), Type II (Treated Soda-Lime), Type III (Soda-Lime) |
| Neck Finish Type | neck_finish_type | enum | Thread or engagement style of the closure opening | Continuous Thread (CT), Lug (Twist-Off), Crown, Cork, BVS (Bague Vin Standard), ROPP (Roll-On Pilfer-Proof), Snap, Bar Top |
| Country of Origin | country_of_origin | text | Country where the glass container is manufactured | USA, France, Germany, Italy, Czech Republic, India, Mexico |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Neck Finish Code | neck_finish_code | text | GPI or industry standard neck finish specification code | 18-400, 28-400, 28-405, 30A-3115-F-140, 33-400, 38-2000 Lug, 63-2030 Lug, 70-450, BVS 30x60 |
| Body Shape | body_shape | enum | Primary profile of the container body | Boston Round, French Square, Cylinder, Bordeaux/Claret, Burgundy, Flint Flask, Oval, Wide Mouth Round, Economy Round, Custom |
| Overall Height | overall_height | number (mm) | Total height from base to top of the finish | 80, 127, 165, 210, 270, 302, 350 |
| Wall Thickness | wall_thickness | number (mm) | Nominal glass wall thickness | 2.0, 2.5, 3.0, 3.5, 4.0, 5.0 |
| Mould Number | mould_number | text | Manufacturer mould identification number for the specific container design | 5511026, 2389A, 7720B |
| Closure Compatibility | closure_compatibility | text (list) | Types of closures recommended for use with this container | Screw Cap, Lug Cap, Crown Cap, Cork Stopper, ROPP Aluminum Cap, Snap Cap, Pump Dispenser |
| UV Protection | uv_protection | enum | Whether the glass color provides ultraviolet light filtering | High (Amber), Moderate (Green), Low (Flint/Clear) |
| Returnable/Refillable | returnablerefillable | enum | Whether the container is designed for multi-trip refill systems | Returnable, One-Way (Non-Returnable) |
| Application Sector | application_sector | text (list) | Primary end-use industry for the container | Wine, Beer, Spirits, Food, Beverage, Pharmaceutical, Cosmetics, Candle |
| Decoration | decoration | text (list) | Applied surface decoration methods available or present | ACL (Applied Ceramic Label), Screen Print, Organic Ink, Pressure-Sensitive Label, Embossing/Debossing, Frosting, Sleeve |
| Pallet Configuration | pallet_configuration | text | Number of containers per pallet layer and total per pallet | 2340 per pallet (18 layers x 130), 1200 per pallet |
| Food Contact Compliance | food_contact_compliance | text (list) | Regulatory food-contact safety standards the product meets | FDA 21 CFR, EU 1935/2004, EC 10/2011, USP Type III |
| Certification | certification | text (list) | Environmental and quality certifications | ISO 9001, ISO 14001, ISO 22000, Cradle to Cradle, 100% Recyclable |
| Recyclability | recyclability | enum | Whether the glass container is recyclable | Infinitely Recyclable, Recyclable with Color Sorting |
| Capacity | capacity | number (mL) | Nominal fill-point volume of the container | 30, 60, 100, 250, 375, 500, 750, 1000, 1500, 3785 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus industry standards (GPI neck finish standards, ASTM C148/C149, USP glass types) | [Ardagh Glass North America Catalog](https://northamerica.ardaghproducts.com/products/750-ml-inspiration-429), [O.Berk Glass Containers](https://www.oberk.com/containers/glass), [Bottlestore 16oz Boston Round](https://www.bottlestore.com/16oz-flint-boston-round-glass-bottle-28-400-neck.html), [SKS Bottle and Packaging](https://www.sks-bottle.com/) |
