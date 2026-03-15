# SKU Schema: Pets & Companion Animals

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or breeder product identifier | GP-FEM-01, HAM-SYR-M, CHIN-GRY |
| Product Name | text | Full product name including species, breed or variety, and sex | Fancy Guinea Pig Female, Winter White Dwarf Hamster, Standard Grey Chinchilla Male |
| URL | text | Direct link to the product or listing page | https://example.com/product/fancy-guinea-pig |
| Price | number | Numeric price per animal, excluding currency symbol | 7.79, 22.99, 199.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Species | text | Common species name of the animal | Guinea Pig, Hamster, Chinchilla, Rabbit, Gerbil, Mouse, Rat, Ferret |
| Breed | text | Specific breed, variety, or morph within the species | Fancy Bear Syrian, Winter White Dwarf, Roborovski Dwarf, Holland Lop, Rex |
| Sex | enum | Biological sex of the animal | Male, Female, Unsexed |
| Age | text | Age or age range of the animal at time of sale | 8 weeks, 3 months, Juvenile, Young Adult |
| Adult Size | text | Expected full-grown body length or weight | 3-4 inches, 5-7 inches, 10-12 inches, Up to 12 inches |
| Weight | number (g) | Current or typical weight of the animal at time of sale | 30, 250, 500, 1200 |
| Color | text | Primary coat, feather, scale, or fur color | White, Grey, Brown, Golden, Albino, Agouti, Calico |
| Pattern | text | Coat or marking pattern | Solid, Banded, Spotted, Tortoiseshell, Siamese, Dalmatian |
| Coat Type | text | Fur or hair texture and length | Short Hair, Long Hair, Satin, Rex, Wire, Smooth |
| Lifespan | text | Typical expected lifespan under proper care | 1-2 years, 2-3 years, 5-8 years, 10-15 years |
| Experience Level | enum | Recommended owner experience for this species or breed | Beginner, Intermediate, Advanced |
| Temperament | text | General behavioral disposition | Docile, Active, Social, Nocturnal, Diurnal, Territorial |
| Social Needs | text | Whether the animal thrives alone or in groups | Solitary, Pairs recommended, Colony, Same-sex pairs |
| Activity Pattern | enum | Time of day the animal is most active | Diurnal, Nocturnal, Crepuscular |
| Diet Type | text | Primary feeding classification and staple food | Herbivore, Omnivore, Pelleted food with hay and vegetables |
| Minimum Habitat Size | text | Smallest recommended enclosure dimensions | 12 x 12 x 12 inches, 24 x 36 x 24 inches, 30 x 18 x 18 inches |
| Habitat Type | text | Type of enclosure required | Wire cage, Glass aquarium, Multi-level cage, Hutch |
| Temperature Range | text | Ambient temperature range the animal requires | 65-75 F, 60-80 F, Below 75 F |
| Health Screening | boolean | Whether the animal has been veterinary screened before sale | true, false |
| Vaccination Status | text | Vaccines administered before sale, if applicable | Up to date, Not applicable, Spayed/Neutered |
| Guarantee Period | text | Duration of health or satisfaction guarantee from seller | 14 days, 30 days, None |
| Restricted Regions | text (list) | States or jurisdictions where sale or ownership is prohibited | California, Hawaii, Alaska, Montana, New York |
| Availability | enum | Whether the animal can be purchased online or in-store only | In-store only, Online with delivery, Both |
| Breeder Type | enum | Type of seller or operation | Pet Store, Licensed Breeder, Rescue, Hobby Breeder |
| Microchipped | boolean | Whether the animal has been implanted with a microchip for identification | true, false |
| Pedigree | boolean | Whether the animal comes with documented lineage or registration papers | true, false |
| Country of Origin | text | Country or region where the animal was bred | USA, Netherlands, United Kingdom |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 3 retailers plus industry classification standards | [PetSmart](https://www.petsmart.com/small-pet/live-small-pets/hamsters-guinea-pigs-and-more), [Petco](https://www.petco.com/shop/en/petcostore/category/small-animal/pet-small-animals), [J&A Exotics](https://www.jandaexotics.com/animals-for-sale) |
