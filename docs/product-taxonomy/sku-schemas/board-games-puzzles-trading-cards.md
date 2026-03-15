# SKU Schema: Board Games, Puzzles & Trading Cards

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.board_games_puzzles`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 6603938, 15271, C1009, POK85346 |
| Product Name | text | Full product name including title, edition, and product type | Catan Board Game 5th Edition, Ravensburger Grandiose Greece 1000-Piece Puzzle, Pokemon Scarlet and Violet Booster Box |
| URL | text | Direct link to the product page | https://example.com/product/catan-5th-edition |
| Price | number | Numeric retail price excluding currency symbol | 9.99, 14.99, 44.99, 139.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Product Type | enum | Primary product category | Board Game, Jigsaw Puzzle, Trading Card Game, Card Game, Party Game, Strategy Game, Dice Game, Expansion |
| Game Category | text (list) | Thematic or genre classification of the game | Strategy, Family, Party, Cooperative, Economic, Fantasy, Sci-Fi, Educational |
| Puzzle Material | text | Material the puzzle is made from | Cardboard, Wood, Foam, Acrylic |
| Country of Origin | text | Country where the product is manufactured | USA, Germany, China, Poland, Japan |
| Player Count Minimum | number | Minimum number of players required | 1, 2, 3 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Brand/Publisher | text | Company that produces or publishes the product | Hasbro, Ravensburger, Wizards of the Coast, The Pokemon Company, Asmodee, Fantasy Flight Games |
| Age Recommendation | text | Recommended minimum age printed on packaging | 3+, 6+, 8+, 10+, 13+, 14+ |
| Playing Time | text (minutes) | Estimated time to complete one game session. May be a range | 15, 30-45, 60-120, 90-180 |
| Game Mechanic | text (list) | Core gameplay mechanisms used in the game | Dice Rolling, Tile Placement, Deck Building, Worker Placement, Area Control, Trading, Drafting |
| Puzzle Piece Thickness | number (mm) | Thickness of individual puzzle pieces | 1.8, 2.0, 2.2 |
| Card Dimensions | text (mm) | Physical size of individual trading or game cards | 63 x 88, 63.5 x 88, 57 x 87 |
| TCG Set Name | text | Named set or expansion within a trading card game | Scarlet and Violet, Modern Horizons 3, Prismatic Evolutions |
| TCG Rarity Levels | text (list) | Rarity tiers present in the product | Common, Uncommon, Rare, Ultra Rare, Secret Rare, Holo Rare |
| Pack Configuration | text | How trading card products are packaged and sold | Booster Pack, Elite Trainer Box, Booster Box (36 packs), Theme Deck, Bundle |
| Game Designer | text | Name of the board game designer or design team | Klaus Teuber, Reiner Knizia, Uwe Rosenberg, Elizabeth Hargrave |
| Components Included | text (list) | Physical components packaged with a board game | Game Board, Dice, Cards, Tokens, Meeples, Miniatures, Rulebook, Sand Timer |
| Language | text (list) | Languages supported by the rulebook and game components | English, German, French, Spanish, Japanese, Multi-Language |
| Edition/Version | text | Specific edition or version of the product | 5th Edition, Revised, Anniversary Edition, Collector Edition, Travel Edition |
| Package Dimensions (L x W x H) | text (inches) | Outer box dimensions | 10.75 x 10.75 x 3, 15.5 x 10 x 2.5, 6 x 4 x 3 |
| Expansion/Standalone | enum | Whether the product requires a base game or is playable alone | Standalone, Expansion, Standalone Expansion |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 sources plus BoardGameGeek data model and EN 71 toy safety standards | [Best Buy Games](https://www.bestbuy.com/site/toys-games-collectibles/board-games-puzzles-cards/pcmcat274200050008.c), [Ravensburger](https://www.ravensburger.us/), [BoardGameGeek](https://boardgamegeek.com/), [TCGplayer](https://www.tcgplayer.com/) |
