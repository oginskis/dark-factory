# Scraper Acceptance Criteria

What the scraper output must satisfy. Single source of truth for all three agents:

- **Coder** — targets these criteria when writing or fixing the scraper.
- **Tester** — verifies each criterion, maps results to `pass`/`needs_fix`/`unfixable`.
- **Orchestrator** — reads criterion IDs from the tester's report to drive the fix loop and escalation decisions.

Every requirement is either **error** (blocks the scraper) or **warning** (logged, doesn't block).

### Attribute coverage (per subcategory)

| ID | Blocks? | Requirement |
|------|---------|-------------|
| S01 | yes | For each subcategory, the scraper must extract at least **75% of core attributes** defined in the SKU schema. An attribute counts as extracted if it appears with a non-null value in the sampled products. |
| S02 | yes | The scraper must extract at least **50% of extended attributes** defined in the SKU schema, for each subcategory. Same logic as S01. |

### Mandatory fields (every product)

| ID | Blocks? | Requirement |
|------|---------|-------------|
| S03 | yes | Every product must have all mandatory core attributes: `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path`. All must be non-null, except `price` and `currency` which may be null when the catalog doesn't show prices. |
| S04 | yes | Every product's `product_category` must be a valid taxonomy ID from `categories.md`. |
| S05 | yes | `brand` must be a top-level field. It must never appear inside `core_attributes`, `extended_attributes`, or `extra_attributes`. |

### Execution (does the scraper run without errors?)

| ID | Blocks? | Requirement |
|------|---------|-------------|
| S06 | no | Products should come from at least 2 different top-level categories (skipped during retests). |
| S07 | yes | The scraper must finish without HTTP or parsing errors (`errors_count` = 0 in the run summary). |
| S08 | yes | The scraper must exit with code 0 (no crash). Exit code -1 means timeout. |
| S09 | yes | The scraper must produce at least one non-empty output file. |

### Value formatting (are extracted values clean?)

| ID | Blocks? | Requirement |
|------|---------|-------------|
| M01 | yes | Numeric attributes that have a unit (e.g., weight in kg) must store the number as `int`/`float` and put the unit string in `attribute_units`. Wrong: `"weight": "5kg"`. Right: `"weight": 5` + `"attribute_units": {"weight": "kg"}`. |
| M02 | no | All number-typed attributes should be `int`/`float`, not strings like `"18"`. |
| M03 | no | When the SKU schema defines a unit for an attribute and the product has that attribute, `attribute_units` should include it. |
| M04 | yes | No embedded units anywhere — values like `"18mm"`, `"5kg"`, `"220V"` must not appear in any attribute bucket (core, extended, or extra). The `_parse_numeric()` function must split value from unit across all buckets. |

### Status determination

How the tester maps criterion results to scraper status. The orchestrator uses this status to drive the fix loop.

| Status | Condition |
|--------|-----------|
| `pass` | All error-severity criteria pass. Warning-only failures (S06, M02, M03) are logged but don't block. |
| `needs_fix` | One or more error-severity criteria failed, but the scraper ran and produced output. Enters the fix loop. |
| `unfixable` | S08 (crash) or S09 (no output) failed. The scraper is fundamentally broken — immediate escalation, no fix loop. |
