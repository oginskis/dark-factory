# SKU Schema: Lighting Fixtures & Lamps

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.lighting_fixtures_lamps`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 6573200, CAP-4925, WL-8810-BK |
| Product Name | product_name | text | Full product name including key specs such as fixture type, finish, and size | Westinghouse 3-Light Drum Chandelier Oil Rubbed Bronze, Capital Lighting Flush Mount 13 in Matte Black, Hinkley Pendant 1-Light Aged Zinc 12 in |
| URL | url | text | Direct link to the product page | https://example.com/product/3-light-drum-chandelier |
| Price | price | number | Numeric price per unit excluding currency symbol | 29.99, 149.00, 875.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Fixture Type | fixture_type | enum | Specific type of lighting fixture | Chandelier, Pendant, Flush Mount, Semi-Flush Mount, Wall Sconce, Table Lamp, Floor Lamp, Vanity Light, Track Light, Recessed Light, Ceiling Fan Light Kit, Outdoor Wall Lantern, Landscape Light |
| Bulb Base Type | bulb_base_type | text | Socket base standard | E26 (Medium), E12 (Candelabra), GU10, E27, Bi-Pin G9, Integrated LED |
| Bulb Type Compatible | bulb_type_compatible | text | Types of bulbs the fixture accepts | LED, Incandescent, CFL, Halogen, Edison, Integrated LED (Non-Replaceable) |
| Shade Material | shade_material | text | Material of the lampshade or diffuser | Fabric (Linen), Glass (Frosted), Glass (Seeded), Metal, Rattan, Acrylic, Mica |
| Housing Material | housing_material | text | Material of the fixture body and canopy | Steel, Aluminum, Brass, Cast Iron, Wood, Resin, Ceramic |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Mounting Type | mounting_type | text | How the fixture attaches to the structure | Ceiling Mount, Hardwired Wall Mount, Plug-In, Pendant (Stem/Cord/Chain), Recessed, Surface, Track |
| Country of Origin | country_of_origin | text | Country where the fixture is manufactured | China, USA, Italy, India, Mexico, Turkey |
| Number of Lights | number_of_lights | number | Count of bulb sockets or integrated LED modules | 1, 2, 3, 4, 5, 6, 8, 12 |
| Max Wattage per Bulb | max_wattage_per_bulb | number (W) | Maximum recommended wattage per socket | 40, 60, 75, 100, 150 |
| Total Wattage | total_wattage | number (W) | Combined wattage of all bulbs or integrated LED | 9, 36, 60, 120, 300 |
| Lumens | lumens | number (lm) | Total light output of the fixture (primarily for integrated LED) | 500, 800, 1600, 3000, 5000 |
| Color Temperature | color_temperature | number (K) | Correlated color temperature of included or recommended bulbs | 2200, 2700, 3000, 4000, 5000 |
| CRI | cri | number | Color Rendering Index indicating color accuracy (0-100 scale) | 80, 82, 90, 95 |
| Dimmable | dimmable | boolean | Whether the fixture supports dimming via compatible dimmer switch | true, false |
| Fixture Height | fixture_height | number (mm) | Overall height of the fixture body excluding hanging chain or rod | 150, 250, 400, 600 |
| Fixture Depth/Extension | fixture_depthextension | number (mm) | How far the fixture extends from the ceiling or wall | 100, 150, 200, 300 |
| Finish | finish | text | Surface finish or color of the fixture | Matte Black, Brushed Nickel, Oil Rubbed Bronze, Polished Chrome, Antique Brass, Aged Zinc, Satin Gold, Painted White |
| Bulbs Included | bulbs_included | boolean | Whether bulbs are included in the box | true, false |
| Damp/Wet Rated | dampwet_rated | enum | Moisture exposure rating | Dry Rated, Damp Rated, Wet Rated |
| IP Rating | ip_rating | text | Ingress Protection rating for dust and water | IP20, IP44, IP65 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (UL 1598, IEC 60598, Energy Star) | [Westinghouse Lighting](https://www.westinghouselighting.com/), [Capital Lighting](https://www.capitallightingfixture.com/catalogs), [Currey and Company](https://www.curreyandcompany.com/categories/lighting/), [LED Lighting Supply](https://www.ledlightingsupply.com/blog/led-product-specifications-important-points-to-watch) |
