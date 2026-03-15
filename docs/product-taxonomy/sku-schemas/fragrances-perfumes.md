# SKU Schema: Fragrances & Perfumes

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | Y0785220, 2525854, 3348901368254 |
| Product Name | text | Full product name including brand, fragrance name, concentration, and size | Dior Sauvage Eau de Parfum 100ml, Chanel No. 5 Parfum 50ml |
| URL | text | Direct link to the product page | https://www.dior.com/en_us/beauty/products/sauvage-eau-de-parfum-Y0785220.html |
| Price | number | Numeric unit price excluding currency symbol | 105.00, 165.00, 38.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer, brand, or fashion house name | Dior, Chanel, Tom Ford, Jo Malone, Guerlain, Versace, Calvin Klein |
| Fragrance Name | text | The named fragrance within the brand | Sauvage, No. 5, Black Orchid, Bleu de Chanel, Light Blue |
| Concentration | enum | Fragrance concentration type indicating oil percentage | Eau de Cologne, Eau de Toilette, Eau de Parfum, Parfum, Extrait de Parfum, Elixir |
| Volume | number (ml) | Volume of the bottle | 30, 50, 75, 100, 150, 200 |
| Volume (oz) | number (oz) | Volume in fluid ounces as commonly displayed in US retail | 1.0, 1.7, 2.5, 3.4, 5.0, 6.8 |
| Target Gender | enum | Intended consumer gender | Men, Women, Unisex |
| Fragrance Family | enum | Primary olfactory classification | Woody, Oriental, Floral, Fresh, Citrus, Aromatic, Gourmand, Chypre, Fougere, Aquatic |
| Top Notes | text (list) | Initial scent notes perceived in the first minutes | Bergamot, Pepper, Lemon, Grapefruit, Pink Pepper, Mandarin |
| Heart Notes | text (list) | Middle notes that emerge after the top notes fade | Lavender, Geranium, Rose, Jasmine, Iris, Cinnamon, Star Anise |
| Base Notes | text (list) | Long-lasting notes that form the foundation of the fragrance | Ambroxan, Vanilla, Sandalwood, Musk, Cedarwood, Tonka Bean, Patchouli, Vetiver |
| Perfumer | text | Name of the perfumer or nose who created the fragrance | Francois Demachy, Jacques Polge, Alberto Morillas |
| Launch Year | number | Year the fragrance was first released | 2015, 1921, 2006, 2018 |
| Bottle Type | enum | Form factor of the fragrance container | Spray, Splash, Rollerball, Travel Spray, Decant |
| Refillable | enum | Whether the bottle supports refilling | Yes, No |
| Limited Edition | enum | Whether the product is a limited edition release | Yes, No |
| Gift Set | enum | Whether the product is sold as part of a gift set | Yes, No |
| Set Contents | text (list) | Items included in a gift set | EDP 100ml, Shower Gel 50ml, Travel Spray 10ml, Body Lotion 75ml |
| INCI Ingredients | text | Full INCI ingredient list from packaging | Alcohol, Parfum, Aqua, Limonene, Linalool, Coumarin, Citronellol |
| Alcohol Free | enum | Whether the fragrance is alcohol-free | Yes, No |
| Packaging Material | text | Primary packaging material for the bottle | Glass, Glass with Metal Cap, Crystal |
| Box Included | enum | Whether the product comes in a presentation box | Yes, No |
| Country of Origin | text | Country where the fragrance is manufactured | France, Italy, USA, Spain, UK |
| Batch Code | text | Manufacturer batch or lot code for traceability | 3G01, 4C02, 9X14 |
| Shelf Life | number (months) | Expected shelf life from date of manufacture | 36, 48, 60 |
| Certifications | text (list) | Product regulatory or quality certifications | IFRA Compliant, EU Cosmetics Regulation, ISO 22716 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus IFRA and fragrance classification standards | [Dior Sauvage EDP](https://www.dior.com/en_us/beauty/products/sauvage-eau-de-parfum-Y0785220.html), [Fragrantica Dior Sauvage](https://www.fragrantica.com/perfume/Dior/Sauvage-31861.html), [Ulta Beauty Dior Sauvage](https://www.ulta.com/p/sauvage-eau-de-parfum-xlsImpprod17941005), [The Perfume Shop Concentration Guide](https://www.theperfumeshop.com/blog/expertise/whats-the-difference-between-parfum-and-eau-de-parfum/) |
