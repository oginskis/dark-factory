# SKU Schema: Musical Instruments & Accessories

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 0113012706, P45B, YDP-165R, SECU24FCCB |
| Product Name | text | Full product name including brand, model, and key variant details | Fender American Professional II Stratocaster Sunburst, Yamaha P-225 88-Key Digital Piano, PRS SE Custom 24 Floyd |
| URL | text | Direct link to the product page | https://example.com/product/fender-strat-am-pro-ii |
| Price | number | Numeric retail price excluding currency symbol | 149.99, 699.99, 1499.99, 3999.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand/Manufacturer | text | Company that produces the instrument or accessory | Fender, Gibson, Yamaha, PRS, Ibanez, Taylor, Martin, Roland, Casio |
| Instrument Type | enum | Primary instrument classification | Electric Guitar, Acoustic Guitar, Bass Guitar, Digital Piano, Acoustic Piano, Keyboard, Drums, Violin, Trumpet, Ukulele |
| Instrument Family | enum | Broad family the instrument belongs to | String, Keyboard, Percussion, Brass, Woodwind |
| Model/Series | text | Named product line or series | American Professional II, Player Series, P-Series, Clavinova, Les Paul Standard |
| Body Material | text | Primary material of the instrument body or shell | Alder, Ash, Mahogany, Maple, Spruce, Nyatoh, Basswood, Rosewood |
| Body Shape/Style | text | Shape classification for stringed instruments or form factor for others | Stratocaster, Les Paul, Dreadnought, Concert, Jumbo, Grand Auditorium, Upright |
| Top Material | text | Material used for the instrument top or soundboard on acoustic/semi-hollow instruments | Sitka Spruce, Cedar, Maple, Poplar Burl, Quilted Maple |
| Neck Material | text | Material used for the neck | Maple, Mahogany, Roasted Maple, Maple/Bubinga |
| Fingerboard Material | text | Material used for the fretboard or fingerboard | Rosewood, Maple, Ebony, Pau Ferro, Richlite |
| Number of Frets | number | Total fret count on the fingerboard | 20, 21, 22, 24 |
| Scale Length | number (inches) | Vibrating string length from nut to bridge saddle | 24.75, 25, 25.5, 30, 34 |
| Neck Radius | text (inches) | Curvature of the fingerboard surface | 7.25, 9.5, 10-16 Compound, 12 |
| Nut Width | number (mm) | Width of the fingerboard at the nut | 42, 43, 44.5, 48 |
| Number of Strings | number | Total string count on the instrument | 4, 5, 6, 7, 12 |
| Pickup Configuration | text | Type and arrangement of pickups for electric instruments | SSS, HSS, HH, P90, Single Coil, Humbucker |
| Pickup Models | text (list) | Specific pickup model names installed | V-Mod II Single-Coil, 57 Classic, Fishman Sonitone, Suhr Woodshed |
| Bridge Type | text | Type of bridge or tailpiece | Synchronized Tremolo, Tune-O-Matic, Floyd Rose, Hardtail, Fixed |
| Tuning Machines | text | Type or brand of tuning pegs | Fender Standard Cast/Sealed, Grover Rotomatics, Locking, Open-Gear |
| Number of Keys | number | Number of keys on a keyboard or piano instrument | 25, 49, 61, 76, 88 |
| Key Action | text | Type of key mechanism on keyboard instruments | Weighted (GHS), Graded Hammer, Semi-Weighted, Synth Action, Natural Wood |
| Polyphony | number | Maximum number of simultaneous notes a digital instrument can produce | 48, 64, 128, 192, 256 |
| Voice/Tone Count | number | Number of built-in instrument voices or tones | 10, 24, 200, 400, 700 |
| Finish | text | Surface finish or color of the instrument | Sunburst, Black, Natural, Cherry, Vintage White, Satin, Gloss, Metallic |
| Dimensions (L x W x H) | text (inches) | Overall product dimensions | 52.25 x 11.5 x 6, 38.25 x 14.75 x 4.75 |
| Product Weight | number (lbs) | Weight of the instrument without case or packaging | 7.5, 8.2, 11.5, 25, 55 |
| Connectivity | text (list) | Audio and data connection ports | 1/4-inch Jack, XLR, USB-to-Host, MIDI, Bluetooth Audio, Aux In, Headphone Out |
| Power Source | text | How the instrument is powered for electronic instruments | AC Adapter, Battery (AA), Rechargeable Li-ion, USB-C, AC Mains |
| Included Accessories | text (list) | Items packaged with the instrument | Gig Bag, Hard Case, Strings, Cable, Sustain Pedal, Music Rest, Power Adapter, Allen Wrenches |
| Country of Origin | text | Country where the instrument is manufactured | USA, Japan, Mexico, Indonesia, China, South Korea, Germany |
| Warranty | text | Manufacturer warranty duration | Lifetime Limited, 2 Year, 5 Year, 10 Year |
| UPC/EAN | text | Universal Product Code or European Article Number | 885978579501, 0889025103589 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 sources plus industry classification standards | [Sweetwater](https://www.sweetwater.com/), [Yamaha](https://usa.yamaha.com/products/musical_instruments/), [Fender](https://www.fender.com/), [Musicians Friend](https://www.musiciansfriend.com/) |
