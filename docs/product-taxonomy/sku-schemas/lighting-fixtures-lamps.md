# SKU Schema: Lighting Fixtures & Lamps

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 6573200, CAP-4925, WL-8810-BK |
| Product Name | text | Full product name including key specs such as fixture type, finish, and size | Westinghouse 3-Light Drum Chandelier Oil Rubbed Bronze, Capital Lighting Flush Mount 13 in Matte Black, Hinkley Pendant 1-Light Aged Zinc 12 in |
| URL | text | Direct link to the product page | https://example.com/product/3-light-drum-chandelier |
| Price | number | Numeric price per unit excluding currency symbol | 29.99, 149.00, 875.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Brand/Manufacturer | text | Lighting brand or manufacturer | Westinghouse, Capital Lighting, Hinkley, Progress Lighting, Kichler, Visual Comfort, Currey and Company |
| Fixture Type | enum | Specific type of lighting fixture | Chandelier, Pendant, Flush Mount, Semi-Flush Mount, Wall Sconce, Table Lamp, Floor Lamp, Vanity Light, Track Light, Recessed Light, Ceiling Fan Light Kit, Outdoor Wall Lantern, Landscape Light |
| Number of Lights | number | Count of bulb sockets or integrated LED modules | 1, 2, 3, 4, 5, 6, 8, 12 |
| Bulb Base Type | text | Socket base standard | E26 (Medium), E12 (Candelabra), GU10, E27, Bi-Pin G9, Integrated LED |
| Bulb Type Compatible | text | Types of bulbs the fixture accepts | LED, Incandescent, CFL, Halogen, Edison, Integrated LED (Non-Replaceable) |
| Max Wattage per Bulb | number (W) | Maximum recommended wattage per socket | 40, 60, 75, 100, 150 |
| Total Wattage | number (W) | Combined wattage of all bulbs or integrated LED | 9, 36, 60, 120, 300 |
| Lumens | number (lm) | Total light output of the fixture (primarily for integrated LED) | 500, 800, 1600, 3000, 5000 |
| Color Temperature | number (K) | Correlated color temperature of included or recommended bulbs | 2200, 2700, 3000, 4000, 5000 |
| CRI | number | Color Rendering Index indicating color accuracy (0-100 scale) | 80, 82, 90, 95 |
| Dimmable | boolean | Whether the fixture supports dimming via compatible dimmer switch | true, false |
| Voltage | text | Input voltage range | 120V, 120-277V, 12V, 240V |
| Fixture Height | number (mm) | Overall height of the fixture body excluding hanging chain or rod | 150, 250, 400, 600 |
| Fixture Width/Diameter | number (mm) | Width or diameter of the fixture body | 130, 300, 450, 600, 800 |
| Fixture Depth/Extension | number (mm) | How far the fixture extends from the ceiling or wall | 100, 150, 200, 300 |
| Adjustable Hanging Length | number (mm) | Maximum chain, cord, or rod length for pendant and chandelier mounting | 900, 1200, 1800, 3000 |
| Shade Material | text | Material of the lampshade or diffuser | Fabric (Linen), Glass (Frosted), Glass (Seeded), Metal, Rattan, Acrylic, Mica |
| Housing Material | text | Material of the fixture body and canopy | Steel, Aluminum, Brass, Cast Iron, Wood, Resin, Ceramic |
| Finish | text | Surface finish or color of the fixture | Matte Black, Brushed Nickel, Oil Rubbed Bronze, Polished Chrome, Antique Brass, Aged Zinc, Satin Gold, Painted White |
| Mounting Type | text | How the fixture attaches to the structure | Ceiling Mount, Hardwired Wall Mount, Plug-In, Pendant (Stem/Cord/Chain), Recessed, Surface, Track |
| Bulbs Included | boolean | Whether bulbs are included in the box | true, false |
| Damp/Wet Rated | enum | Moisture exposure rating | Dry Rated, Damp Rated, Wet Rated |
| IP Rating | text | Ingress Protection rating for dust and water | IP20, IP44, IP65 |
| LED Lifespan | number (hours) | Rated lifespan of integrated LED modules | 25000, 50000, 75000, 100000 |
| Energy Star Certified | boolean | Whether the fixture meets Energy Star efficiency requirements | true, false |
| Product Weight | number (kg) | Total weight of the fixture | 0.9, 2.5, 5.0, 12.0 |
| Style | text | Design or aesthetic style | Modern, Farmhouse, Industrial, Transitional, Art Deco, Coastal, Mid-Century |
| Certification | text (list) | Safety and regulatory certifications | UL Listed, ETL Listed, CE, RoHS, Energy Star, Title 24 |
| Country of Origin | text | Country where the fixture is manufactured | China, USA, Italy, India, Mexico, Turkey |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (UL 1598, IEC 60598, Energy Star) | [Westinghouse Lighting](https://www.westinghouselighting.com/), [Capital Lighting](https://www.capitallightingfixture.com/catalogs), [Currey and Company](https://www.curreyandcompany.com/categories/lighting/), [LED Lighting Supply](https://www.ledlightingsupply.com/blog/led-product-specifications-important-points-to-watch) |
