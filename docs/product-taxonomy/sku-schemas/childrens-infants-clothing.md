# SKU Schema: Children's & Infants' Clothing

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | CT-SLP-NB-001, TCP-5678, HA-PJ-80CM, 1088033002, A01TB00000 |
| Product Name | text | Full product name including brand, garment type, age indication, and key differentiators | Organic Cotton Zip-Up Sleep and Play Newborn, Girls Graphic T-Shirt 4T, 5-pack Cotton Bodysuits, Babies Long-Sleeved Bodysuit 3-Pack |
| URL | text | Direct link to the product page | https://example.com/product/organic-cotton-sleeper |
| Price | number | Numeric retail price per unit, excluding currency symbol | 4.99, 8.99, 14.50, 29.00, 36.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD, SEK |
| Brand | text | Name of the clothing brand | Carter's, Hanna Andersson, The Children's Place, Gerber, Primary, Cat & Jack |
| Garment Type | text | Type of clothing item | Bodysuit, Sleeper, Romper, T-Shirt, Pants, Dress, Jacket, Onesie, Overalls, Snowsuit, Jumpsuit, Raincoat, Pyjamas |
| Gender | enum | Target gender for the garment | Boys, Girls, Unisex |
| Age Group | enum | Broad developmental age classification | Preemie, Newborn, Infant, Toddler, Little Kid, Big Kid |
| Age Range | text | Specific age range the garment is designed for | 0-3 months, 3-6 months, 6-12 months, 12-18 months, 2T-3T, 4-5 years, 6-7 years |
| Size | text | Garment size designation | Preemie, NB, 0-3M, 3-6M, 6-9M, 12M, 18M, 24M, 2T, 3T, 4T, 5, 6, 7, 8 |
| Size System | text | Country or regional sizing standard used | US, EU, UK, CM (centimeter-based) |
| Height Range | text | Child height range the size corresponds to | 46-51 cm, 56-62 cm, 68-74 cm, 80-86 cm |
| Weight Range | text | Child weight range the size corresponds to | Up to 6 lbs, 6-9 lbs, 12-17 lbs, 17-21 lbs, 22-25 lbs |
| Fit | text | Garment fit descriptor indicating how the item is cut relative to the body | Regular, Slim, Relaxed, Snug-Fitting, Room to Grow |
| Color | text | Primary color of the garment | Pink, Blue, White, Yellow, Grey, Mint, Navy, Multi, Beige |
| Pattern | text | Visual pattern or print on the fabric | Solid, Striped, Floral, Animal Print, Dinosaur, Polka Dot, Plaid, Character, Heart, Color Block |
| Material | text | Primary fabric composition with percentages | 100% Organic Cotton, 100% Polyester, 60% Cotton 40% Polyester, 95% Cotton 5% Spandex, 93% Bamboo Viscose 7% Spandex |
| Fabric Technology | text | Named fabric type or weave used in the garment | PurelySoft, HannaSoft, French Terry, Fleece, Waffle Knit, 1x1 Rib Knit, Poplin, Velvet, Terry Cloth, Seersucker, Cotton Muslin |
| Closure Type | text | Primary fastening mechanism suited for easy dressing | Snap, Zipper, Pull-On, Button, Velcro, Elastic Waist, Envelope Neck, Poppers |
| Zipper Direction | enum | Direction the zipper opens on sleepwear for diaper access | Top-Down, Two-Way, Bottom-Up |
| Neckline | text | Style of the neckline | Crew, Envelope, Peter Pan, Round, Lap Shoulder, Wrapover |
| Sleeve Length | text | Length of the sleeve | Short, Long, Sleeveless, Three-Quarter |
| Foot Coverage | enum | Whether sleepwear or bottoms include built-in foot covers | Footed, Footless, Convertible |
| Pack Quantity | number | Number of garments included in a multi-pack | 1, 2, 3, 4, 5 |
| Licensed Character | text | Name of the licensed intellectual property or franchise featured on the garment | Disney Princess, Star Wars, Winnie the Pooh, Mickey and Friends, None |
| Sustainability Label | text | Retailer or third-party sustainability program designation beyond organic certification | Conscious Choice, Cradle to Cradle Certified, Better Cotton Initiative, Recycled Polyester, None |
| Flame Resistance | text | Sleepwear flammability compliance method | Flame Resistant Polyester, Tight-Fitting Cotton, Snug-Fitting, Not Sleepwear |
| Safety Certification | text (list) | Product safety certifications the garment meets | CPSIA, OEKO-TEX Standard 100, EN 14682 (drawstring safety), Cradle to Cradle Gold |
| Organic Certification | text | Organic textile certification if applicable | GOTS, OCS (Organic Content Standard), None |
| Seam Construction | text | Type of interior seam finish relevant to comfort on sensitive skin | Flatlock, Tagless, Smooth, Covered |
| Care Instructions | text | Cleaning and maintenance directions | Machine wash warm, Tumble dry medium, Do not bleach, Machine wash cold |
| Country of Origin | text | Country where the garment was manufactured | China, India, Cambodia, Bangladesh, Sri Lanka, Tunisia, Morocco, France, Turkey |
| Season | text (list) | Seasons or climate conditions the garment is designed for | Spring, Summer, Fall, Winter, All-Season |
| Features | text (list) | Functional design details and enhancements | Diaper-friendly snap bottom, Built-in scratch mittens, Expandable shoulders, Non-slip soles, UPF 50+, Fold-over mittens, Room to grow cuffs, Zipper chin guard |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Added: Fit, Licensed Character, Sustainability Label. Updated example values for SKU, Product Name, Price, Currency, Garment Type, Color, Pattern, Material, Fabric Technology, Closure Type, Neckline, Flame Resistance, Safety Certification, Care Instructions, Country of Origin, Features. Deprecated: none. | [H&M](https://www2.hm.com/en_us/baby/products/clothing.html), [Petit Bateau](https://www.petit-bateau.co.uk/baby/), [PatPat](https://www.patpat.com/collections/baby-clothes) |
| 2026-03-15 | Initial schema — 33 attributes from 3 retailers plus CPSIA and OEKO-TEX safety standards | [Carter's](https://www.carters.com/c/baby-clothes), [Hanna Andersson](https://www.hannaandersson.com/baby-clothes/), [The Children's Place](https://www.childrensplace.com/us/c/baby-clothes) |
