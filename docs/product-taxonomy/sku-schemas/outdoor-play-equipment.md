# SKU Schema: Outdoor Play Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.outdoor_play`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 01-1104, KGC-12, RAINB-CASTLE, GP-SKYE-1 |
| Product Name | text | Full product name including brand, model, and key features | Gorilla Playsets Double Down II Wooden Swing Set, Rainbow Castle Playset, Trampolify KGC Series 14ft Trampoline Combo |
| URL | text | Direct link to the product page | https://example.com/product/gorilla-double-down-ii |
| Price | number | Numeric retail price excluding currency symbol | 299.99, 899.99, 2499.99, 5999.00 |
| Currency | text | ISO 4217 currency code | USD, CAD, GBP, EUR, AUD |
| Product Type | enum | Primary equipment category | Swing Set, Playset, Trampoline, Slide, Climbing Wall, Sandbox, Playhouse, Combo Set |
| Frame Material | text | Primary structural material used for the frame | Cedar, Pressure-Treated Pine, Powder-Coated Steel, Galvanized Steel, Redwood |
| Hardware Type | text | Fastener specification used in assembly | 1/2-inch Carriage Bolts, Recessed Safety-Capped, Acorn Nuts, Thru-Bolt |
| Platform Height | number (inches) | Height of the main deck or platform above ground | 36, 48, 54, 60 |
| Number of Platforms | number | Count of elevated deck areas in the playset | 1, 2, 3 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Swing Type | text (list) | Types of swing seats provided | Belt Swing, Bucket Swing, Tire Swing, Saucer Swing, Glider, Trapeze Bar |
| Slide Type | text (list) | Types of slides included with the set | Wave Slide, Spiral Slide, Tube Slide, Double Slide |
| Canopy/Roof Type | text | Type of overhead cover on the playset | Fabric Canopy, Wood Roof, Vinyl Canopy, None |
| Country of Origin | text | Country where the product is manufactured | USA, China, Taiwan |
| Assembled Dimensions (L x W x H) | text (inches) | Overall footprint and height of the assembled unit | 179 x 96 x 74, 228 x 234 x 156, 144 diameter x 96 |
| Footprint/Safety Zone | text (feet) | Recommended minimum clearance area around the equipment per ASTM guidelines | 24 x 18, 30 x 26, 20 diameter |
| Age Range | text | Recommended age group for the equipment | 3-8, 3-10, 6-15, 3-12 |
| Lumber Dimensions | text (inches) | Cross-section size of structural wood members | 4 x 4, 4 x 6, 2 x 4, 2 x 6 |
| Wood Treatment | text | Preservative or finish applied to wooden components | Natural Cedar, Stained, Pressure Treated, Sealed, Untreated |
| Additional Play Features | text (list) | Extra play elements beyond swings and slides | Climbing Wall, Rope Ladder, Monkey Bars, Sandbox, Picnic Table, Telescope, Steering Wheel, Punching Bag |
| Safety Enclosure | boolean | Whether a safety net enclosure is included | Yes, No |
| Assembly Time | text (hours) | Estimated time required for assembly | 4-6, 5-7, 8-12, 12-16 |
| Assembly Required | enum | Level of assembly needed after delivery | Full Assembly, Partial Pre-Assembly, Pre-Cut and Pre-Drilled, Professional Install Recommended |
| ASTM Compliance | text (list) | Applicable ASTM safety standards the product meets | ASTM F1148, ASTM F1487, ASTM F2373, ASTM F381, ASTM F2225 |
| Surfacing Recommendation | text | Recommended ground surface material beneath the equipment | Rubber Mulch, Wood Chips, Engineered Wood Fiber, Pea Gravel, Rubber Mat |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 sources plus ASTM F1148 and CPSC Public Playground Safety Handbook | [Gorilla Playsets](https://www.gorillaplaysets.com/), [Rainbow Play Systems](https://www.rainbowplay.com/), [Sportspower](https://sportspowerswingsets.com/), [Trampolify](https://trampolify.com/) |
