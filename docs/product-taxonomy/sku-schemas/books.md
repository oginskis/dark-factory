# SKU Schema: Books

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.books`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer, distributor, or publisher product identifier | 978-0-13-468599-1, BB-HC-20456, ING-9780134685991 |
| Product Name | product_name | text | Full book title including subtitle if present | Clean Code: A Handbook of Agile Software Craftsmanship, The Great Gatsby |
| URL | url | text | Direct link to the product page | https://example.com/books/clean-code |
| Price | price | number | Numeric retail or wholesale price per copy, excluding currency symbol | 49.99, 12.95, 8.99 |
| Currency | currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Binding Type | binding_type | enum | Physical binding method of the book | Hardcover, Paperback, Mass Market Paperback, Spiral, Saddle-Stitch, Board Book, Library Binding |
| Paper Type | paper_type | enum | Interior paper stock classification | Uncoated White, Cream/Natural, Coated Glossy, Coated Matte, Newsprint |
| Ink/Color Type | inkcolor_type | enum | Interior printing color mode | Black and White, Full Color, Spot Color, Duotone |
| BISAC Category | bisac_category | text | Book Industry Standards and Communications subject classification code | FIC004000, COM051280, JUV000000 |
| Barcode Format | barcode_format | enum | Type of scannable barcode on the cover | EAN-13, UPC-A, None |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| ISBN-13 | isbn-13 | text | 13-digit International Standard Book Number | 978-0-13-468599-1, 978-0-14-028329-7 |
| ISBN-10 | isbn-10 | text | Legacy 10-digit ISBN for editions assigned before 2007 | 0-13-468599-8, 0-14-028329-4 |
| Author | author | text (list) | Author or authors of the work | Robert C. Martin, F. Scott Fitzgerald |
| Publisher | publisher | text | Publishing house or imprint name | Pearson, Penguin Books, HarperCollins, Oxford University Press |
| Publication Date | publication_date | text | Date of this edition's publication | 2008-08-01, 2004-09-30 |
| Edition | edition | text | Edition number or description | 1st, 2nd Revised, Anniversary |
| Language | language | text | Primary language of the text content | English, Spanish, French, German, Japanese |
| Spine Width | spine_width | number (mm) | Thickness of the book spine | 12, 25, 3, 45 |
| Cover Finish | cover_finish | enum | Surface treatment of the cover | Glossy, Matte, Soft-Touch Laminate, Spot UV, Uncoated |
| Dust Jacket | dust_jacket | enum | Whether a removable dust jacket is included (hardcover only) | Yes, No |
| Illustrations | illustrations | enum | Whether the book contains illustrations or photographs | None, Black and White, Full Color |
| Subject/Genre | subjectgenre | text (list) | Descriptive genre or subject tags | Literary Fiction, Computer Science, Cooking, Biography, Childrens Picture Book |
| Carton Quantity | carton_quantity | number | Number of copies packed per shipping carton | 12, 24, 36, 48 |
| Trim Size | trim_size | text (mm) | Finished page dimensions as width x height | 152 x 229, 108 x 175, 216 x 280 |
| Page Count | page_count | number | Total number of printed pages | 464, 180, 32, 1200 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 sources plus industry standards (ISBN.org, BISAC, ONIX metadata) | [B&N Press Trim Sizes](https://help-press.barnesandnoble.com/hc/en-us/articles/5358034341275-Trim-Sizes-and-Paper-Stock), [Blurb Book Dimensions](https://www.blurb.com/book-dimensions), [IngramSpark Print Options](https://www.ingramspark.com/plan-your-book/print/trim-sizes), [BookBaby Binding Options](https://www.bookbaby.com/book-printing/book-trim-sizes-and-binding-options) |
