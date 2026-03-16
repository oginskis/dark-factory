# SKU Schema: Pesticides, Herbicides & Crop Protection Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.pesticides_herbicides_crop_protection`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | SYN-ACURON-2.5GAL, BASF-PRIAXOR-2.5GAL, COR-DIM2EW |
| Product Name | product_name | text | — | Full product name including brand, formulation, and package size | Acuron Herbicide 2.5 gal, Priaxor Xemium Fungicide, Dimension 2EW Herbicide |
| URL | url | text | — | Direct link to the product page | https://example.com/products/acuron-herbicide |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 42.95, 119.50, 289.00, 575.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Category | product_category | enum | — | Primary crop protection classification | Herbicide, Insecticide, Fungicide, Rodenticide, Plant Growth Regulator, Adjuvant, Seed Treatment, Biopesticide |
| Active Ingredient | active_ingredient | text (list) | — | Chemical common names of active ingredients in the formulation | Glyphosate, S-metolachlor, Atrazine, Mesotrione, Chlorantraniliprole, Azoxystrobin |
| Active Ingredient Concentration | active_ingredient_concentration | text (list) | — | Percentage or weight per volume of each active ingredient | 41%, 28.6%, 9.5% w/w, 480 g/L |
| Formulation Type | formulation_type | enum | — | Physical form and formulation classification | Emulsifiable Concentrate (EC), Suspension Concentrate (SC), Wettable Powder (WP), Soluble Liquid (SL), Water-Dispersible Granule (WDG), Flowable (F), Granular (G), Ready-to-Use (RTU) |
| Hazmat Shipping Class | hazmat_shipping_class | text | — | DOT or IMDG hazardous materials transport classification | Non-Regulated, Class 6.1, Class 9, Class 3 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured or formulated | USA, Germany, Switzerland, India, China, Israel |
| Mode of Action Group | mode_of_action_group | text (list) | — | Resistance management group numbers assigned by IRAC, FRAC, or HRAC | Group 15, Group 5, Group 27, Group 4, Group 11 |
| Signal Word | signal_word | enum | — | Acute toxicity signal word required on the label | CAUTION, WARNING, DANGER |
| Restricted Use | restricted_use | boolean | — | Whether the product is classified as a Restricted Use Pesticide requiring a licence to purchase | true, false |
| EPA Registration Number | epa_registration_number | text | — | Regulatory registration number issued by the environmental protection authority | 100-1623, 432-1312, 7969-472 |
| Target Pests | target_pests | text (list) | — | Pests, weeds, or diseases the product is labelled to control | Palmer Amaranth, Waterhemp, Giant Ragweed, Corn Earworm, Brown Rust, Powdery Mildew |
| Target Crops | target_crops | text (list) | — | Crops the product is registered for use on | Field Corn, Soybeans, Cotton, Wheat, Rice, Turf, Ornamentals |
| Application Timing | application_timing | text (list) | — | Growth stage or timing window for application | Pre-Emergence, Post-Emergence, Pre-Plant, At Planting, Burndown, Early Season, Late Season |
| Application Rate | application_rate | text | — | Labelled rate range per area or volume of water | 2.5-3 qt/A, 0.38-0.77 fl oz/1000 sq ft, 1-2 L/ha |
| Application Method | application_method | enum | — | Recommended application technique | Ground Spray, Aerial Spray, Chemigation, Soil Incorporation, Seed Treatment, Granular Broadcast, Bait Station |
| Spray Volume | spray_volume | text | — | Recommended carrier volume per treated area | 10-20 gal/A, 100-200 L/ha |
| Re-Entry Interval | re-entry_interval | text | — | Minimum time after application before workers may re-enter treated areas without protective equipment | 4 hours, 12 hours, 24 hours, 48 hours |
| Pre-Harvest Interval | pre-harvest_interval | number | days | Minimum number of days between last application and crop harvest | 0, 7, 14, 21, 30, 60 |
| Rainfast Period | rainfast_period | text | — | Time after application before rainfall will not reduce efficacy | 1 hour, 2 hours, 4 hours, 6 hours |
| Tank Mix Compatibility | tank_mix_compatibility | text (list) | — | Products or product types approved for tank mixing | Glyphosate, AMS, Crop Oil Concentrate, Non-Ionic Surfactant |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus EPA FIFRA labelling requirements and IRAC/FRAC/HRAC resistance management group classifications | [Bayer CropScience Catalog](https://www.cropscience.bayer.us/crop-protection/catalog), [Syngenta Acuron](https://www.syngenta-us.com/herbicides/acuron), [FBN Crop Protection](https://www.fbn.com/direct/crop-protection), [EPA Pesticide Labels](https://www.epa.gov/ingredients-used-pesticide-products/how-search-information-about-pesticide-ingredients-and-labels) |
