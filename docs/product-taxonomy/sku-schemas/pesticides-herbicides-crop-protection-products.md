# SKU Schema: Pesticides, Herbicides & Crop Protection Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SYN-ACURON-2.5GAL, BASF-PRIAXOR-2.5GAL, COR-DIM2EW |
| Product Name | text | Full product name including brand, formulation, and package size | Acuron Herbicide 2.5 gal, Priaxor Xemium Fungicide, Dimension 2EW Herbicide |
| URL | text | Direct link to the product page | https://example.com/products/acuron-herbicide |
| Price | number | Numeric price per unit excluding currency symbol | 42.95, 119.50, 289.00, 575.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Syngenta, Bayer, Corteva, BASF, FMC, ADAMA, Atticus, Nufarm |
| Product Category | enum | Primary crop protection classification | Herbicide, Insecticide, Fungicide, Rodenticide, Plant Growth Regulator, Adjuvant, Seed Treatment, Biopesticide |
| Active Ingredient | text (list) | Chemical common names of active ingredients in the formulation | Glyphosate, S-metolachlor, Atrazine, Mesotrione, Chlorantraniliprole, Azoxystrobin |
| Active Ingredient Concentration | text (list) | Percentage or weight per volume of each active ingredient | 41%, 28.6%, 9.5% w/w, 480 g/L |
| Mode of Action Group | text (list) | Resistance management group numbers assigned by IRAC, FRAC, or HRAC | Group 15, Group 5, Group 27, Group 4, Group 11 |
| Formulation Type | enum | Physical form and formulation classification | Emulsifiable Concentrate (EC), Suspension Concentrate (SC), Wettable Powder (WP), Soluble Liquid (SL), Water-Dispersible Granule (WDG), Flowable (F), Granular (G), Ready-to-Use (RTU) |
| Signal Word | enum | Acute toxicity signal word required on the label | CAUTION, WARNING, DANGER |
| Restricted Use | boolean | Whether the product is classified as a Restricted Use Pesticide requiring a licence to purchase | true, false |
| EPA Registration Number | text | Regulatory registration number issued by the environmental protection authority | 100-1623, 432-1312, 7969-472 |
| Target Pests | text (list) | Pests, weeds, or diseases the product is labelled to control | Palmer Amaranth, Waterhemp, Giant Ragweed, Corn Earworm, Brown Rust, Powdery Mildew |
| Target Crops | text (list) | Crops the product is registered for use on | Field Corn, Soybeans, Cotton, Wheat, Rice, Turf, Ornamentals |
| Application Timing | text (list) | Growth stage or timing window for application | Pre-Emergence, Post-Emergence, Pre-Plant, At Planting, Burndown, Early Season, Late Season |
| Application Rate | text | Labelled rate range per area or volume of water | 2.5-3 qt/A, 0.38-0.77 fl oz/1000 sq ft, 1-2 L/ha |
| Application Method | enum | Recommended application technique | Ground Spray, Aerial Spray, Chemigation, Soil Incorporation, Seed Treatment, Granular Broadcast, Bait Station |
| Spray Volume | text | Recommended carrier volume per treated area | 10-20 gal/A, 100-200 L/ha |
| Re-Entry Interval | text | Minimum time after application before workers may re-enter treated areas without protective equipment | 4 hours, 12 hours, 24 hours, 48 hours |
| Pre-Harvest Interval | number (days) | Minimum number of days between last application and crop harvest | 0, 7, 14, 21, 30, 60 |
| Rainfast Period | text | Time after application before rainfall will not reduce efficacy | 1 hour, 2 hours, 4 hours, 6 hours |
| Tank Mix Compatibility | text (list) | Products or product types approved for tank mixing | Glyphosate, AMS, Crop Oil Concentrate, Non-Ionic Surfactant |
| Net Volume | number (L) | Net volume of the container in litres | 0.95, 2.5, 9.46, 110, 208 |
| Net Weight | number (kg) | Net weight for dry formulations in kilograms | 0.34, 0.68, 2.27, 4.54, 11.34 |
| Selectivity | enum | Whether the product targets specific organism types or controls broadly | Selective, Non-Selective |
| Systemic Action | enum | Whether the active ingredient moves within the target organism | Systemic, Contact, Translaminar |
| Residual Activity | boolean | Whether the product provides extended control beyond the initial application | true, false |
| Shelf Life | number (months) | Expected shelf life when stored per label instructions | 12, 24, 36, 60 |
| Storage Temperature Range | text | Acceptable storage temperature range to maintain product integrity | 0-40 C, Above 0 C, 5-35 C |
| Hazmat Shipping Class | text | DOT or IMDG hazardous materials transport classification | Non-Regulated, Class 6.1, Class 9, Class 3 |
| Country of Origin | text | Country where the product is manufactured or formulated | USA, Germany, Switzerland, India, China, Israel |
| SDS Available | boolean | Whether a Safety Data Sheet is available for the product | true, false |
| Manufacturer | text | Parent company or registrant name | Syngenta Crop Protection, Bayer CropScience, Corteva Agriscience, BASF Corporation, FMC Corporation |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus EPA FIFRA labelling requirements and IRAC/FRAC/HRAC resistance management group classifications | [Bayer CropScience Catalog](https://www.cropscience.bayer.us/crop-protection/catalog), [Syngenta Acuron](https://www.syngenta-us.com/herbicides/acuron), [FBN Crop Protection](https://www.fbn.com/direct/crop-protection), [EPA Pesticide Labels](https://www.epa.gov/ingredients-used-pesticide-products/how-search-information-about-pesticide-ingredients-and-labels) |
