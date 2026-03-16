# SKU Schema: Pets & Companion Animals

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.pets_companion_animals`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or breeder product identifier | GP-FEM-01, HAM-SYR-M, CHIN-GRY |
| Product Name | product_name | text | — | Full product name including species, breed or variety, and sex | Fancy Guinea Pig Female, Winter White Dwarf Hamster, Standard Grey Chinchilla Male |
| URL | url | text | — | Direct link to the product or listing page | https://example.com/product/fancy-guinea-pig |
| Price | price | number | — | Numeric price per animal, excluding currency symbol | 7.79, 22.99, 199.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Coat Type | coat_type | text | — | Fur or hair texture and length | Short Hair, Long Hair, Satin, Rex, Wire, Smooth |
| Diet Type | diet_type | text | — | Primary feeding classification and staple food | Herbivore, Omnivore, Pelleted food with hay and vegetables |
| Habitat Type | habitat_type | text | — | Type of enclosure required | Wire cage, Glass aquarium, Multi-level cage, Hutch |
| Breeder Type | breeder_type | enum | — | Type of seller or operation | Pet Store, Licensed Breeder, Rescue, Hobby Breeder |
| Country of Origin | country_of_origin | text | — | Country or region where the animal was bred | USA, Netherlands, United Kingdom |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Species | species | text | — | Common species name of the animal | Guinea Pig, Hamster, Chinchilla, Rabbit, Gerbil, Mouse, Rat, Ferret |
| Breed | breed | text | — | Specific breed, variety, or morph within the species | Fancy Bear Syrian, Winter White Dwarf, Roborovski Dwarf, Holland Lop, Rex |
| Sex | sex | enum | — | Biological sex of the animal | Male, Female, Unsexed |
| Age | age | text | — | Age or age range of the animal at time of sale | 8 weeks, 3 months, Juvenile, Young Adult |
| Color | color | text | — | Primary coat, feather, scale, or fur color | White, Grey, Brown, Golden, Albino, Agouti, Calico |
| Pattern | pattern | text | — | Coat or marking pattern | Solid, Banded, Spotted, Tortoiseshell, Siamese, Dalmatian |
| Lifespan | lifespan | text | — | Typical expected lifespan under proper care | 1-2 years, 2-3 years, 5-8 years, 10-15 years |
| Experience Level | experience_level | enum | — | Recommended owner experience for this species or breed | Beginner, Intermediate, Advanced |
| Temperament | temperament | text | — | General behavioral disposition | Docile, Active, Social, Nocturnal, Diurnal, Territorial |
| Social Needs | social_needs | text | — | Whether the animal thrives alone or in groups | Solitary, Pairs recommended, Colony, Same-sex pairs |
| Activity Pattern | activity_pattern | enum | — | Time of day the animal is most active | Diurnal, Nocturnal, Crepuscular |
| Temperature Range | temperature_range | text | — | Ambient temperature range the animal requires | 65-75 F, 60-80 F, Below 75 F |
| Health Screening | health_screening | boolean | — | Whether the animal has been veterinary screened before sale | true, false |
| Vaccination Status | vaccination_status | text | — | Vaccines administered before sale, if applicable | Up to date, Not applicable, Spayed/Neutered |
| Guarantee Period | guarantee_period | text | — | Duration of health or satisfaction guarantee from seller | 14 days, 30 days, None |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 3 retailers plus industry classification standards | [PetSmart](https://www.petsmart.com/small-pet/live-small-pets/hamsters-guinea-pigs-and-more), [Petco](https://www.petco.com/shop/en/petcostore/category/small-animal/pet-small-animals), [J&A Exotics](https://www.jandaexotics.com/animals-for-sale) |
