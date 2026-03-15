# SKU Schema: Beverages (Alcoholic)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor product identifier | BEV-70021, 080432400432, RNDC-55120 |
| Product Name | text | Full product name including brand, expression, vintage if applicable, and size | Maker's Mark Kentucky Straight Bourbon Whisky 750ml, Chateau Margaux 2015 750ml, Sierra Nevada Pale Ale 12oz 6-Pack |
| URL | text | Direct link to the product page | https://example.com/product/makers-mark-bourbon-750 |
| Price | number | Numeric price per selling unit (bottle, can, pack, case), excluding currency symbol | 29.99, 12.99, 189.00, 42.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD, JPY |
| Brand | text | Consumer-facing brand name | Maker's Mark, Chateau Margaux, Sierra Nevada, Hendrick's, Moet & Chandon |
| Producer/Distillery | text | Company or estate that produces the product | Beam Suntory, Diageo, Sierra Nevada Brewing Co., Pernod Ricard |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 080432400432, 3262155000019 |
| Beverage Category | enum | Primary alcoholic beverage category | Wine, Spirits, Beer, Cider, Mead, Ready to Drink |
| Beverage Type | text | Specific type within the category | Bourbon, Scotch Whisky, Vodka, Gin, Tequila, Rum, Red Wine, White Wine, Sparkling Wine, IPA, Lager, Stout |
| ABV | number (%) | Alcohol by volume percentage as stated on the label | 5.0, 12.5, 14.0, 40.0, 43.0, 46.0 |
| Proof | number | Alcohol proof, equal to twice the ABV, used primarily for spirits | 80, 86, 90, 92, 100, 114 |
| Volume | number (ml) | Net volume of the container | 187, 330, 355, 473, 500, 750, 1000, 1750 |
| Container Type | enum | Type of container the product is sold in | Glass Bottle, Can, Keg, Bag-in-Box, Tetra Pak, Ceramic Bottle |
| Pack Size | number | Number of individual containers per selling unit | 1, 4, 6, 12, 15, 24, 30 |
| Pack Configuration | text | Description of the pack format | Single Bottle, 6-Pack Cans, 12-Pack Bottles, Case of 12, Half Barrel Keg |
| Grape Variety | text (list) | Primary grape varieties used, applicable to wine | Cabernet Sauvignon, Chardonnay, Pinot Noir, Sauvignon Blanc, Merlot, Riesling |
| Vintage | number | Year the grapes were harvested, applicable to wine | 2015, 2018, 2020, 2022 |
| Appellation/Region | text | Geographic origin or designated production region | Napa Valley, Bordeaux, Speyside, Champagne, Oaxaca, Tequila, Kentucky |
| Country of Origin | text | Country where the product was produced | USA, France, Scotland, Mexico, Japan, Italy, Ireland, Germany |
| Wine Style | enum | Broad style classification for wines | Red, White, Rose, Sparkling, Dessert, Fortified, Orange |
| Wine Body | enum | Body profile for wines | Light, Medium-Light, Medium, Medium-Full, Full |
| Wine Sweetness | enum | Sweetness level designation | Bone Dry, Dry, Off-Dry, Semi-Sweet, Sweet |
| Beer Style | text | Specific beer style per brewing tradition | IPA, Pale Ale, Stout, Porter, Lager, Pilsner, Wheat Beer, Sour, Hazy IPA |
| IBU | number | International Bitterness Units for beer, measuring hop bitterness | 10, 25, 45, 65, 80, 100 |
| Age Statement | text | Stated aging period, primarily for spirits | 4 Years, 12 Years, 18 Years, 25 Years, No Age Statement |
| Barrel Type | text | Type of barrel used for aging, applicable to spirits and some wines and beers | New American Oak, Ex-Bourbon, Sherry Cask, French Oak, Port Cask |
| Organic | boolean | Whether the product is certified organic | true, false |
| Dietary Certifications | text (list) | Dietary or production certifications | Organic, Biodynamic, Vegan, Gluten Free, Non-GMO, Natural Wine, Sustainable |
| Sulfite Declaration | boolean | Whether the label declares the presence of sulfites | true, false |
| Case Pack | number | Number of selling units per wholesale case | 6, 12, 24, 48 |
| Tasting Notes | text | Brief flavor description from the producer or distributor | Vanilla, caramel, and toasted oak with a smooth finish |
| Food Pairing | text (list) | Recommended food pairings as suggested by the producer | Red Meat, Grilled Fish, Cheese, Chocolate, Spicy Cuisine |
| Awards | text (list) | Competition medals or ratings received | Gold Medal, 92 Points, Double Gold, Best in Show |
| Seasonal/Limited Edition | boolean | Whether the product is a seasonal release or limited edition | true, false |
| Serving Temperature | text | Recommended serving temperature | Chilled (4-8C), Room Temperature, On Ice, 16-18C |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from beverage wholesale distributors, TTB labeling requirements, Brewers Association style guidelines, and wine classification standards | [Southern Glazer's](https://www.southernglazers.com/), [Provi](https://www.provi.com/), [TTB Wine Labeling](https://www.ttb.gov/labeling-wine/wine-labeling-alcohol-content), [Brewers Association Beer Style Guidelines](https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/) |
