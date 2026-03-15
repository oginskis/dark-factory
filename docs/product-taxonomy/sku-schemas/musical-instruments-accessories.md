# SKU Schema: Musical Instruments & Accessories

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.musical_instruments`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 0113012706, P45B, YDP-165R, SECU24FCCB |
| Product Name | text | Full product name including brand, model, and key variant details | Fender American Professional II Stratocaster Sunburst, Yamaha P-225 88-Key Digital Piano, PRS SE Custom 24 Floyd |
| URL | text | Direct link to the product page | https://example.com/product/fender-strat-am-pro-ii |
| Price | number | Numeric retail price excluding currency symbol | 149.99, 699.99, 1499.99, 3999.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Instrument Type | enum | Primary instrument classification | Electric Guitar, Acoustic Guitar, Bass Guitar, Digital Piano, Acoustic Piano, Keyboard, Drums, Violin, Trumpet, Ukulele |
| Body Material | text | Primary material of the instrument body or shell | Alder, Ash, Mahogany, Maple, Spruce, Nyatoh, Basswood, Rosewood |
| Top Material | text | Material used for the instrument top or soundboard on acoustic/semi-hollow instruments | Sitka Spruce, Cedar, Maple, Poplar Burl, Quilted Maple |
| Neck Material | text | Material used for the neck | Maple, Mahogany, Roasted Maple, Maple/Bubinga |
| Fingerboard Material | text | Material used for the fretboard or fingerboard | Rosewood, Maple, Ebony, Pau Ferro, Richlite |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Bridge Type | text | Type of bridge or tailpiece | Synchronized Tremolo, Tune-O-Matic, Floyd Rose, Hardtail, Fixed |
| Country of Origin | text | Country where the instrument is manufactured | USA, Japan, Mexico, Indonesia, China, South Korea, Germany |
| Instrument Family | enum | Broad family the instrument belongs to | String, Keyboard, Percussion, Brass, Woodwind |
| Model/Series | text | Named product line or series | American Professional II, Player Series, P-Series, Clavinova, Les Paul Standard |
| Body Shape/Style | text | Shape classification for stringed instruments or form factor for others | Stratocaster, Les Paul, Dreadnought, Concert, Jumbo, Grand Auditorium, Upright |
| Number of Frets | number | Total fret count on the fingerboard | 20, 21, 22, 24 |
| Neck Radius | text (inches) | Curvature of the fingerboard surface | 7.25, 9.5, 10-16 Compound, 12 |
| Nut Width | number (mm) | Width of the fingerboard at the nut | 42, 43, 44.5, 48 |
| Number of Strings | number | Total string count on the instrument | 4, 5, 6, 7, 12 |
| Pickup Configuration | text | Type and arrangement of pickups for electric instruments | SSS, HSS, HH, P90, Single Coil, Humbucker |
| Pickup Models | text (list) | Specific pickup model names installed | V-Mod II Single-Coil, 57 Classic, Fishman Sonitone, Suhr Woodshed |
| Tuning Machines | text | Type or brand of tuning pegs | Fender Standard Cast/Sealed, Grover Rotomatics, Locking, Open-Gear |
| Number of Keys | number | Number of keys on a keyboard or piano instrument | 25, 49, 61, 76, 88 |
| Key Action | text | Type of key mechanism on keyboard instruments | Weighted (GHS), Graded Hammer, Semi-Weighted, Synth Action, Natural Wood |
| Polyphony | number | Maximum number of simultaneous notes a digital instrument can produce | 48, 64, 128, 192, 256 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 sources plus industry classification standards | [Sweetwater](https://www.sweetwater.com/), [Yamaha](https://usa.yamaha.com/products/musical_instruments/), [Fender](https://www.fender.com/), [Musicians Friend](https://www.musiciansfriend.com/) |
