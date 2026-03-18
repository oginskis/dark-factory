# SKU Schema: Building Hardware & Ironmongery (Handles, Hinges, Locks)

**Last updated:** 2026-03-18
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.building_hardware_ironmongery`

## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product code for the hardware item | 14854, HH-LR-SN-102, YAL-PBS2-CH |
| Product Name | product_name | text | Full product name including type, range, finish and size | Grade 13 Ball Bearing Fire Door Hinge Satin Finish, Sintra Lever on Rose Door Handle Pair Polished Chrome |
| URL | url | text | Direct link to the product page | https://www.example.com/grade-13-ball-bearing-hinge |
| Price | price | number | Numeric price value without currency symbol, typically per unit or per pack | 8.49, 24.99, 112.00 |
| Currency | currency | text | ISO 4217 currency code | GBP, EUR, USD |
| Hardware Type | hardware_type | text | Primary classification of the hardware item | Door Handle, Hinge, Lock, Latch, Letterbox, Door Knocker, Door Closer, Cabin Hook, Shelf Bracket |
| Material | material | text | Primary material the hardware is manufactured from | Stainless Steel, Brass, Zinc Alloy, Aluminium, Steel, Iron, Polyamide |
| Finish | finish | text | Surface treatment or coating applied to the hardware | Polished Chrome, Satin Nickel, Antique Brass, Matt Black, Dark Bronze, Brushed Stainless Steel |
| Fire Rated | fire_rated | boolean | Whether the product is certified for use on fire doors | true, false |
| Country of Origin | country_of_origin | text | Country where the hardware was manufactured | United Kingdom, China, Italy, Germany |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Hardware Subtype | hardware_subtype | text | Specific subcategory within the hardware type | Lever on Rose, Lever on Backplate, Pull Handle, Butt Hinge, Ball Bearing Hinge, Mortice Lock, Rim Lock, Cylinder Lock, Tubular Latch |
| Length | length | number (mm) | Primary dimension of the hardware item, typically the height for hinges or plate length for handles | 76, 102, 152, 200 |
| Width | width | number (mm) | Secondary dimension, typically the leaf width for hinges or plate width for handles | 38, 51, 76, 102 |
| Depth | depth | number (mm) | Thickness or projection of the hardware item from the mounting surface | 2.5, 3, 13, 25 |
| Colour | colour | text | Visible colour of the finished product, distinct from the finish process | Black, Chrome, Brass, Bronze, Nickel, Pewter, Gold, White, Stainless Steel |
| Interior Exterior | interior_exterior | text | Whether the hardware is suitable for interior use, exterior use, or both | Interior, Exterior, Interior and Exterior |
| Max Door Weight | max_door_weight | number (kg) | Maximum door weight the hardware can support, primarily for hinges and closers | 40, 60, 80, 120 |
| Security Rating | security_rating | text | Security standard or grade the product is certified to, primarily for locks | BS 3621, Sold Secure Silver, Sold Secure Gold, PAS 24 |
| Hinge Grade | hinge_grade | text | Performance grade classification per BS EN 1935 or equivalent, for hinges | Grade 7, Grade 11, Grade 13, Grade 14 |
| Pack Size | pack_size | number | Number of individual items included in the pack | 1, 2, 3, 5, 10 |
| Fixings Supplied | fixings_supplied | boolean | Whether installation screws or fixings are included with the product | true, false |
| Certification | certification | text (list) | International standards and certifications the product meets | BS EN 1935, BS EN 1634, Certifire, CE, BS 3621, EN 1906 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-18 | Initial schema — 10 core + 12 extended attributes from 4 companies | [IronmongeryDirect](https://www.ironmongerydirect.co.uk), [Screwfix](https://www.screwfix.com/c/security-ironmongery/door-handles/cat6760002), [Toolstation](https://www.toolstation.com/grade-13-ball-bearing-fire-door-hinge/p73733), [RS Components](https://uk.rs-online.com/web/c/security-ironmongery/latches-hinges-handles/) |
