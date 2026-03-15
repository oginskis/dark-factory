# SKU Schema: Newspapers & Periodicals

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.newspapers_periodicals`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Publisher, distributor, or retailer product identifier | NYT-DAILY-2026, MAG-NAT-GEO-0326, WSJ-WEEKEND |
| Product Name | text | Full publication title including edition descriptor if applicable | The New York Times Daily Edition, National Geographic March 2026, The Economist Weekly |
| URL | text | Direct link to the product or subscription page | https://example.com/subscribe/nyt-daily |
| Price | number | Numeric cover price or subscription price per issue/period, excluding currency symbol | 3.00, 6.99, 12.50, 299.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, AUD |
| Publication Type | enum | Broad classification of the serial publication | Newspaper, Magazine, Journal, Newsletter, Trade Publication |
| Format | enum | Page format classification of the publication | Broadsheet, Berliner/Midi, Tabloid/Compact, US Broadsheet, Digest, Letter, Custom |
| Paper Type | enum | Stock used for the interior pages | Newsprint, Coated Glossy, Coated Matte, Uncoated, Supercalendered |
| Edition Type | enum | Edition variant classification | National, Regional, International, City, Weekend, Special |
| Ink Type | enum | Classification of ink used in printing | Soy-Based, Vegetable-Based, Petroleum-Based |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Subscription Type | enum | How the publication reaches the reader | Print Only, Digital Only, Print and Digital Bundle, Single Copy |
| ISSN | text | International Standard Serial Number identifying the serial publication | 0362-4331, 0027-9358, 0013-0613 |
| Publisher | text | Publishing company or media group name | The New York Times Company, Conde Nast, News Corp, Axel Springer |
| Frequency | enum | How often the publication is issued | Daily, Weekly, Biweekly, Monthly, Bimonthly, Quarterly, Annual |
| Page Width | number (mm) | Trimmed page width | 280, 305, 315, 375, 381, 210 |
| Page Height | number (mm) | Trimmed page height | 430, 559, 470, 597, 578, 276 |
| Printing Method | enum | Primary press technology used for production | Offset Lithography, Web Offset, Coldset Web, Heatset Web, Digital, Gravure, Flexography |
| Color Mode | enum | Color capability of the interior pages | Full Color (CMYK), Spot Color, Black and White, Mixed (Color and B/W sections) |
| Binding/Finishing | enum | Method used to hold pages together | Saddle-Stitch, Perfect Binding, Folded (no binding), Wire-O, Case Bound |
| Circulation | number | Average number of copies distributed per issue | 350000, 1200000, 55000, 8500000 |
| Distribution Region | text | Primary geographic market for the publication | United States, United Kingdom, Global, Germany, India |
| Language | text | Primary language of the publication content | English, German, French, Spanish, Japanese, Mandarin |
| Advertising Ratio | number (%) | Approximate percentage of total page area occupied by advertising | 30, 45, 60 |
| Shelf Life | text | Typical relevance duration of the publication content | 1 day, 1 week, 1 month, 3 months |
| Recyclability | enum | Whether the product is recyclable in standard paper recycling streams | Yes, No, Partially (remove inserts) |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from industry standards and publisher specifications (ISSN, ISO 8601 frequency codes, newspaper format dimensions) | [PaperSizes.io Newspaper Formats](https://papersizes.io/newspaper), [MakeMyNewspaper Specifications](https://makemynewspaper.com/specifications), [Thomas Group Newspaper Sizes](https://thomasgroupprinting.com/newspaper-sizes-guide/), [Mixam Magazine Printing](https://mixam.com/magazines) |
