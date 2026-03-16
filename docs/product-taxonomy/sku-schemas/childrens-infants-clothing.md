# SKU Schema: Children's & Infants' Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.childrens_infants_clothing`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | CT-SLP-NB-001, TCP-5678, HA-PJ-80CM, 1088033002, A01TB00000 |
| Product Name | product_name | text | — | Full product name including brand, garment type, age indication, and key differentiators | Organic Cotton Zip-Up Sleep and Play Newborn, Girls Graphic T-Shirt 4T, 5-pack Cotton Bodysuits, Babies Long-Sleeved Bodysuit 3-Pack |
| URL | url | text | — | Direct link to the product page | https://example.com/product/organic-cotton-sleeper |
| Price | price | number | — | Numeric retail price per unit, excluding currency symbol | 4.99, 8.99, 14.50, 29.00, 36.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD, SEK |
| Garment Type | garment_type | text | — | Type of clothing item | Bodysuit, Sleeper, Romper, T-Shirt, Pants, Dress, Jacket, Onesie, Overalls, Snowsuit, Jumpsuit, Raincoat, Pyjamas |
| Material | material | text | — | Primary fabric composition with percentages | 100% Organic Cotton, 100% Polyester, 60% Cotton 40% Polyester, 95% Cotton 5% Spandex, 93% Bamboo Viscose 7% Spandex |
| Closure Type | closure_type | text | — | Primary fastening mechanism suited for easy dressing | Snap, Zipper, Pull-On, Button, Velcro, Elastic Waist, Envelope Neck, Poppers |
| Country of Origin | country_of_origin | text | — | Country where the garment was manufactured | China, India, Cambodia, Bangladesh, Sri Lanka, Tunisia, Morocco, France, Turkey |
| Size | size | text | — | Garment size designation | Preemie, NB, 0-3M, 3-6M, 6-9M, 12M, 18M, 24M, 2T, 3T, 4T, 5, 6, 7, 8 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Gender | gender | enum | — | Target gender for the garment | Boys, Girls, Unisex |
| Age Group | age_group | enum | — | Broad developmental age classification | Preemie, Newborn, Infant, Toddler, Little Kid, Big Kid |
| Age Range | age_range | text | — | Specific age range the garment is designed for | 0-3 months, 3-6 months, 6-12 months, 12-18 months, 2T-3T, 4-5 years, 6-7 years |
| Height Range | height_range | text | — | Child height range the size corresponds to | 46-51 cm, 56-62 cm, 68-74 cm, 80-86 cm |
| Fit | fit | text | — | Garment fit descriptor indicating how the item is cut relative to the body | Regular, Slim, Relaxed, Snug-Fitting, Room to Grow |
| Color | color | text | — | Primary color of the garment | Pink, Blue, White, Yellow, Grey, Mint, Navy, Multi, Beige |
| Pattern | pattern | text | — | Visual pattern or print on the fabric | Solid, Striped, Floral, Animal Print, Dinosaur, Polka Dot, Plaid, Character, Heart, Color Block |
| Fabric Technology | fabric_technology | text | — | Named fabric type or weave used in the garment | PurelySoft, HannaSoft, French Terry, Fleece, Waffle Knit, 1x1 Rib Knit, Poplin, Velvet, Terry Cloth, Seersucker, Cotton Muslin |
| Zipper Direction | zipper_direction | enum | — | Direction the zipper opens on sleepwear for diaper access | Top-Down, Two-Way, Bottom-Up |
| Neckline | neckline | text | — | Style of the neckline | Crew, Envelope, Peter Pan, Round, Lap Shoulder, Wrapover |
| Foot Coverage | foot_coverage | enum | — | Whether sleepwear or bottoms include built-in foot covers | Footed, Footless, Convertible |
| Pack Quantity | pack_quantity | number | — | Number of garments included in a multi-pack | 1, 2, 3, 4, 5 |
| Licensed Character | licensed_character | text | — | Name of the licensed intellectual property or franchise featured on the garment | Disney Princess, Star Wars, Winnie the Pooh, Mickey and Friends, None |
| Sustainability Label | sustainability_label | text | — | Retailer or third-party sustainability program designation beyond organic certification | Conscious Choice, Cradle to Cradle Certified, Better Cotton Initiative, Recycled Polyester, None |
| Flame Resistance | flame_resistance | text | — | Sleepwear flammability compliance method | Flame Resistant Polyester, Tight-Fitting Cotton, Snug-Fitting, Not Sleepwear |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Added: Fit, Licensed Character, Sustainability Label. Updated example values for SKU, Product Name, Price, Currency, Garment Type, Color, Pattern, Material, Fabric Technology, Closure Type, Neckline, Flame Resistance, Safety Certification, Care Instructions, Country of Origin, Features. Deprecated: none. | [H&M](https://www2.hm.com/en_us/baby/products/clothing.html), [Petit Bateau](https://www.petit-bateau.co.uk/baby/), [PatPat](https://www.patpat.com/collections/baby-clothes) |
| 2026-03-15 | Initial schema — 33 attributes from 3 retailers plus CPSIA and OEKO-TEX safety standards | [Carter's](https://www.carters.com/c/baby-clothes), [Hanna Andersson](https://www.hannaandersson.com/baby-clothes/), [The Children's Place](https://www.childrensplace.com/us/c/baby-clothes) |
