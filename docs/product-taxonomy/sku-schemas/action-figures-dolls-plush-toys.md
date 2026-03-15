# SKU Schema: Action Figures, Dolls & Plush Toys

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | F4793, 209068, HLC87, 87-2204 |
| Product Name | text | Full product name including character, line, and scale | Marvel Legends Series 6-Inch Venom Action Figure, Star Wars Black Series Darth Vader, Barbie Dreamhouse Adventures Doll |
| URL | text | Direct link to the product page | https://example.com/product/marvel-legends-venom |
| Price | number | Numeric retail price excluding currency symbol | 24.99, 49.99, 129.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand/Manufacturer | text | Company that produces the toy | Hasbro, Mattel, NECA, McFarlane Toys, Bandai, Hot Toys, Funko |
| Product Type | enum | Primary toy category | Action Figure, Fashion Doll, Baby Doll, Plush Toy, Statue, Collectible Figure, Vinyl Figure |
| Franchise/License | text | Intellectual property or brand the product is based on | Marvel, Star Wars, Transformers, Barbie, Disney Princess, Pokemon, DC Comics |
| Character Name | text | Specific character represented by the figure or doll | Spider-Man, Darth Vader, Optimus Prime, Barbie, Pikachu |
| Scale | text | Proportional scale of the figure relative to real-world size | 1/12, 1/6, 1/18, 1/4, 1/10 |
| Figure Height | number (inches) | Height of the figure measured standing upright | 3.75, 5.5, 6, 7, 12 |
| Articulation Points | number | Number of movable joints on the figure | 5, 14, 20, 30, 36 |
| Material | text (list) | Primary materials used in construction | ABS Plastic, PVC, Die-Cast Metal, Fabric, Polyester Plush, Vinyl, Silicone |
| Accessories Included | text (list) | Items packaged with the figure or doll | Alternate Hands, Weapon, Shield, Stand, Clothing Set, Hairbrush, Pet |
| Series/Wave | text | Product line, wave number, or collection name | Wave 3, Black Series, Legends Series, Signature Collection, Build-A-Figure |
| Build-A-Figure Part | text | Component included for building a larger figure across a wave | Left Arm, Right Leg, Torso, Head, Wings |
| Age Recommendation | text | Recommended minimum age for the product | 3+, 4+, 8+, 14+, 15+ |
| Collector Grade | enum | Whether the item is positioned as a mass-market toy or collector piece | Standard, Premium, Deluxe, Ultimate, Collector Edition |
| Doll Body Type | text | Body style or articulation type for fashion dolls | Standard, Curvy, Petite, Tall, Made to Move |
| Plush Fill Material | text | Internal stuffing material for plush toys | Polyester Fiber, Bean Pellets, Memory Foam |
| Plush Size Category | text | Size classification for plush toys | Mini, Small, Medium, Large, Jumbo |
| Paint Application | text | Type of paint finish or decoration method | Hand-Painted, Tampo Print, Metallic, Wash, Dry Brush |
| Packaging Type | enum | How the product is packaged for sale | Window Box, Blister Card, Collector Box, Polybag, Tin |
| Product Dimensions (L x W x H) | text (inches) | Overall package or product dimensions | 8.5 x 2.5 x 12, 4 x 3 x 6.5 |
| Product Weight | number (oz) | Weight of the item including packaging | 4.8, 8.2, 14.5, 24 |
| Edition Size | number | Number of units produced for limited edition releases | 500, 1000, 3000, 5000 |
| Interactivity | text (list) | Electronic or interactive features built into the toy | Sound Effects, Light-Up, Voice, Motion Sensor, App-Enabled |
| Safety Certification | text (list) | Applicable toy safety standards and markings | ASTM F963, EN 71, CE, CPSIA, CPSC |
| Country of Origin | text | Country where the product is manufactured | China, Vietnam, Indonesia, Japan |
| UPC/EAN | text | Universal Product Code or European Article Number | 5010993954377, 4573102660213 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus ASTM F963 and EN 71 toy safety standards | [BigBadToyStore](https://www.bigbadtoystore.com/), [Hasbro](https://shop.hasbro.com/), [Amazon Toys](https://www.amazon.com/Action-Toy-Figures/b?node=2514571011), [Walmart Toys](https://www.walmart.com/cp/action-figures-playsets/4172) |
