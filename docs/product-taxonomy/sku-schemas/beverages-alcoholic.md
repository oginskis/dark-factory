# SKU Schema: Beverages (Alcoholic)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.beverages_alcoholic`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or distributor product identifier | BEV-70021, 080432400432, RNDC-55120 |
| Product Name | product_name | text | Full product name including brand, expression, vintage if applicable, and size | Maker's Mark Kentucky Straight Bourbon Whisky 750ml, Chateau Margaux 2015 750ml, Sierra Nevada Pale Ale 12oz 6-Pack |
| URL | url | text | Direct link to the product page | https://example.com/product/makers-mark-bourbon-750 |
| Price | price | number | Numeric price per selling unit (bottle, can, pack, case), excluding currency symbol | 29.99, 12.99, 189.00, 42.50 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD, JPY |
| Beverage Category | beverage_category | enum | Primary alcoholic beverage category | Wine, Spirits, Beer, Cider, Mead, Ready to Drink |
| Beverage Type | beverage_type | text | Specific type within the category | Bourbon, Scotch Whisky, Vodka, Gin, Tequila, Rum, Red Wine, White Wine, Sparkling Wine, IPA, Lager, Stout |
| Container Type | container_type | enum | Type of container the product is sold in | Glass Bottle, Can, Keg, Bag-in-Box, Tetra Pak, Ceramic Bottle |
| Country of Origin | country_of_origin | text | Country where the product was produced | USA, France, Scotland, Mexico, Japan, Italy, Ireland, Germany |
| Barrel Type | barrel_type | text | Type of barrel used for aging, applicable to spirits and some wines and beers | New American Oak, Ex-Bourbon, Sherry Cask, French Oak, Port Cask |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Producer/Distillery | producerdistillery | text | Company or estate that produces the product | Beam Suntory, Diageo, Sierra Nevada Brewing Co., Pernod Ricard |
| UPC/EAN | upcean | text | Universal Product Code or European Article Number barcode | 080432400432, 3262155000019 |
| ABV | abv | number (%) | Alcohol by volume percentage as stated on the label | 5.0, 12.5, 14.0, 40.0, 43.0, 46.0 |
| Proof | proof | number | Alcohol proof, equal to twice the ABV, used primarily for spirits | 80, 86, 90, 92, 100, 114 |
| Volume | volume | number (ml) | Net volume of the container | 187, 330, 355, 473, 500, 750, 1000, 1750 |
| Pack Configuration | pack_configuration | text | Description of the pack format | Single Bottle, 6-Pack Cans, 12-Pack Bottles, Case of 12, Half Barrel Keg |
| Grape Variety | grape_variety | text (list) | Primary grape varieties used, applicable to wine | Cabernet Sauvignon, Chardonnay, Pinot Noir, Sauvignon Blanc, Merlot, Riesling |
| Vintage | vintage | number | Year the grapes were harvested, applicable to wine | 2015, 2018, 2020, 2022 |
| Appellation/Region | appellationregion | text | Geographic origin or designated production region | Napa Valley, Bordeaux, Speyside, Champagne, Oaxaca, Tequila, Kentucky |
| Wine Style | wine_style | enum | Broad style classification for wines | Red, White, Rose, Sparkling, Dessert, Fortified, Orange |
| Wine Body | wine_body | enum | Body profile for wines | Light, Medium-Light, Medium, Medium-Full, Full |
| Wine Sweetness | wine_sweetness | enum | Sweetness level designation | Bone Dry, Dry, Off-Dry, Semi-Sweet, Sweet |
| Beer Style | beer_style | text | Specific beer style per brewing tradition | IPA, Pale Ale, Stout, Porter, Lager, Pilsner, Wheat Beer, Sour, Hazy IPA |
| IBU | ibu | number | International Bitterness Units for beer, measuring hop bitterness | 10, 25, 45, 65, 80, 100 |
| Age Statement | age_statement | text | Stated aging period, primarily for spirits | 4 Years, 12 Years, 18 Years, 25 Years, No Age Statement |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from beverage wholesale distributors, TTB labeling requirements, Brewers Association style guidelines, and wine classification standards | [Southern Glazer's](https://www.southernglazers.com/), [Provi](https://www.provi.com/), [TTB Wine Labeling](https://www.ttb.gov/labeling-wine/wine-labeling-alcohol-content), [Brewers Association Beer Style Guidelines](https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/) |
