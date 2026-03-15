# Taxonomy Enforcement & Schema Tiering Design

**Date:** 2026-03-15
**Status:** Approved

## Problem

SKU schemas contain 30-40 attributes per subcategory, but real scrapers extract only 7-13. Scraper-generated attribute names don't match schema names, making cross-company search impossible. There's no feedback loop from real catalog data back to schemas.

## Goals

1. Enable cross-company product search by enforcing consistent attribute names
2. Reduce schema bloat to match what real catalogs actually publish
3. Create a feedback loop where scraping real catalogs improves schemas over time
4. Keep daily scraper runs LLM-free (cheap tier)

## Design

### 1. Three-Tier Attribute Hierarchy

**Universal fields** (8, same across all subcategories, top-level on every product record):
- `sku` — product identifier (was: `sku`)
- `name` — human-readable name (unchanged — keeping `name` not `product_name` for backward compatibility)
- `url` — link to product page (was: `url`)
- `price` — numeric price (was: `price`)
- `currency` — ISO 4217 code (was: `currency`)
- `brand` — manufacturer/brand name (promoted from `attributes.brand` to top-level)
- `product_category` — canonical taxonomy ID, dot-notation (NEW)
- `scraped_at` — ISO 8601 timestamp (was: `scraped_at`)

**Core attributes** (5-10 per subcategory): Attributes meaningful for cross-company comparison within the subcategory. Commonly appear on real product catalogs. These are the searchable/filterable fields.

Core selection criteria:
- **Identity**: what kind of product (`tool_type`, `fastener_type`, `dosage_form`)
- **Material/composition**: what it's made of (`material`, `primary_ingredient`)
- **Primary dimension**: the key size/capacity metric (`voltage`, `thread_size`, `capacity_oz`)
- **Identification/provenance**: model number, country of origin — key for procurement and trade compliance

**Extended attributes** (10-15 per subcategory): Real but either product-type-specific (e.g., `chuck_size` only for drills) or rarely published. Scrapers extract when available but not expected for every product.

### 2. Product Record Format

#### Before (current format)

```json
{
  "sku": "2904-20",
  "name": "M18 FUEL 1/2\" Hammer Drill/Driver",
  "url": "https://www.milwaukeetool.com/...",
  "price": null,
  "currency": null,
  "scraped_at": "2026-03-15T14:43:46+00:00",
  "attributes": {
    "brand": "Milwaukee Tool",
    "tool_type": "Hammer Drill",
    "power_source": "Cordless",
    "badge_branding": "FUEL",
    "warranty": "5 Year Limited Warranty"
  },
  "category_path": "Products > Power Tools > Drilling > Hammer Drills"
}
```

#### After (new format)

```json
{
  "_format": 2,
  "sku": "2904-20",
  "name": "M18 FUEL 1/2\" Hammer Drill/Driver",
  "url": "https://www.milwaukeetool.com/...",
  "price": null,
  "currency": null,
  "brand": "Milwaukee Tool",
  "product_category": "machinery.power_tools",
  "scraped_at": "2026-03-15T14:43:46+00:00",
  "core_attributes": {
    "tool_type": "Hammer Drill",
    "power_source": "Cordless",
    "voltage": 18,
    "motor_type": "Brushless",
    "tool_weight": 3.3,
    "model_number": "2904-20",
    "country_of_origin": "USA"
  },
  "extended_attributes": {
    "chuck_size": 13,
    "chuck_type": "All Metal Ratcheting",
    "number_of_speed_settings": 2,
    "max_torque": 158
  },
  "extra_attributes": {
    "badge_branding": "FUEL",
    "warranty": "5 Year Limited Warranty",
    "image_url": "https://..."
  },
  "category_path": "Products > Power Tools > Drilling > Hammer Drills"
}
```

#### Field mapping (before → after)

| Old field | New field | Change |
|-----------|-----------|--------|
| `sku` | `sku` | unchanged |
| `name` | `name` | unchanged (NOT renamed to `product_name`) |
| `url` | `url` | unchanged |
| `price` | `price` | unchanged |
| `currency` | `currency` | unchanged |
| `scraped_at` | `scraped_at` | unchanged |
| `attributes.brand` | `brand` | promoted to top-level |
| `attributes.{core_field}` | `core_attributes.{core_field}` | moved, name from schema |
| `attributes.{extended_field}` | `extended_attributes.{extended_field}` | moved, name from schema |
| `attributes.{unmapped_field}` | `extra_attributes.{unmapped_field}` | moved |
| `category_path` | `category_path` | unchanged — non-governed provenance field, raw site breadcrumb for debugging. NOT a universal field. |
| (new) | `product_category` | NEW — canonical taxonomy ID (universal field) |
| (new) | `_format` | NEW — version discriminator (2 for new format, absent for v1) |

#### Backward compatibility

- `_format` field: new records have `_format: 2`, old records have no `_format` field (implicitly v1)
- The eval script reads `_format` and handles both formats:
  - v1: reads `attributes` as a flat dict (existing behavior)
  - v2: reads `core_attributes`, `extended_attributes`, `extra_attributes` separately
- During transition, existing scrapers continue running with v1 output. They are regenerated one-by-one as companies go through the pipeline again. No forced mass regeneration of scrapers.
- The migration of schemas (Section 8) is independent of scraper regeneration — schemas change format first, scrapers adopt the new format when regenerated.

#### `extra_attributes` governance

- Keys must be `snake_case`
- Values must be primitives (`string`, `number`, `boolean`) or arrays of primitives
- The eval flags companies where `len(extra_attributes) > len(core_attributes) + len(extended_attributes)` as a warning — suggests the schema is inadequate for this company
- `extra_attributes` are included in the JSONL output and preserved, but not used for cross-company search

### 3. Taxonomy IDs

Each subcategory in `categories.md` gets a stable dot-notation ID appended to the line in backticks:

#### Format

```markdown
## Machinery & Industrial Equipment
- Power Tools (Drills, Saws, Sanders) `machinery.power_tools`
- Hand Tools (Hammers, Wrenches, Screwdrivers) `machinery.hand_tools`
- HVAC Equipment `machinery.hvac`

## Energy Equipment & Storage
- Electric Vehicle Charging Equipment `energy.ev_charging`
- Solar Panels & Photovoltaic Modules `energy.solar_panels`
```

#### Parsing logic

All skills parse taxonomy IDs using this regex on each subcategory line:

```python
match = re.match(r'^- (.+?) `([a-z][a-z0-9_.]+)`$', line.strip())
# match.group(1) = display name, match.group(2) = taxonomy ID
```

Lines without a backtick-enclosed ID are treated as having no ID (error during validation). The migration must ensure every subcategory line has an ID.

#### Rules

- IDs are immutable once assigned — never rename
- Format: `{category_short}.{subcategory_short}` — lowercase, underscores, dots
- IDs must be unique across the entire taxonomy (enforced by a verification script)
- Human-readable display names remain alongside for UI rendering
- Every skill that writes `product_category` MUST look up the ID from `categories.md` — never construct or guess IDs

#### ID uniqueness verification

A verification script (run as part of the migration and as a pre-commit check) validates:
- Every subcategory line has exactly one backtick-enclosed ID
- No duplicate IDs across all subcategories
- IDs match the `[a-z][a-z0-9_.]+` pattern

### 4. Product-Level Category Classification

Companies spanning multiple subcategories get per-product classification via URL-based mapping.

#### Company report format change

The product-classifier (Stage 1) currently allows "one primary, at most one secondary" subcategory. This changes to:

```markdown
## Business Classification

| Attribute | Value |
|-----------|-------|
| Subcategories | `safety.head_protection` (Head Protection), `safety.respiratory_protection` (Respiratory Protection), `safety.fall_protection` (Fall Protection), `electronics.sensors` (Sensors & Instrumentation) |
| Primary | `safety.respiratory_protection` (Respiratory Protection) |
| Business model | B2B |
| Target market | Industrial workers, firefighters, military |
| Geographic focus | Global (US site scraped) |
```

- **`Subcategories`**: ALL taxonomy IDs that apply to this company's products (unlimited)
- **`Primary`**: the single most representative subcategory (used as fallback)
- Display names kept alongside IDs in parentheses for readability

#### URL-prefix mapping

**At scraper generation time (expensive tier, LLM):**
1. Discover all unique URL path segments from sitemap/discovery
2. Map each to a taxonomy ID from the company's `Subcategories` list
3. Store exhaustive mapping in scraper config — every discovered prefix must be mapped
4. If a prefix cannot be mapped to any subcategory, the scraper-generator must escalate (not silently skip)

```json
{
  "category_mapping": {
    "/Head-Protection/": "safety.head_protection",
    "/Respiratory-Protection/": "safety.respiratory_protection",
    "/Portable-Gas-Detection/": "electronics.sensors",
    "/Fall-Protection/": "safety.fall_protection"
  },
  "default_category": "safety.respiratory_protection"
}
```

Matching supports both URL path segments and query parameters:
- Path: `"/Head-Protection/" in url` (substring match)
- Query: `"category=head-protection" in url` (substring match on full URL)

The scraper-generator chooses the appropriate pattern per site during generation.

**At scraper runtime (cheap tier, no LLM):**
- Substring match product URL against mapping keys
- Match found → use mapped taxonomy ID
- No match → tag as `_unclassified`

**Eval catches degradation:**
- New check: `category_classification` — % of products with valid `product_category` (not `_unclassified`)
- Threshold: 0.95 (95% must be classified)
- Weight: 10

No silent misclassification. No LLM at runtime.

#### Multi-subcategory scraper generation

When a company spans multiple subcategories, the scraper-generator must:
1. Load the SKU schema for EACH subcategory in the company's `Subcategories` list
2. For each product, determine its subcategory from the URL mapping
3. Map the product's attributes against the correct subcategory's schema
4. A product's `core_attributes` and `extended_attributes` are governed by the schema matching its `product_category`

### 5. Schema File Format

New two-table format replacing the current single flat table:

```markdown
# SKU Schema: Power Tools (Drills, Saws, Sanders)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.power_tools`

## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Tool Type | text | Specific type of power tool | Hammer Drill, Circular Saw, Sander |
| Power Source | enum | How the tool is powered | Corded, Cordless, Pneumatic |
| Voltage | number (V) | Battery platform or supply voltage | 18, 20, 36, 110 |
| Motor Type | enum | Type of electric motor | Brushed, Brushless |
| Tool Weight | number (kg) | Weight of the bare tool | 1.5, 3.3, 4.7 |
| Model Number | text | Manufacturer model designation | 2904-20, DCD999B |
| Country of Origin | text | Manufacturing country | Germany, China, USA |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Battery Capacity | number (Ah) | Amp-hour capacity | 2.0, 5.0, 8.0 |
| Chuck Size | number (mm) | Drill chuck diameter | 10, 13, 16 |
| Blade Diameter | number (mm) | Saw blade diameter | 168, 210, 254 |
| Max Torque | number (Nm) | Maximum torque output | 54, 135, 158 |
| No-Load Speed | text | Max speed under no load | 0-2100 rpm |
| Number of Speed Settings | number | Discrete speed ranges | 1, 2, 3 |
| Certifications | text (list) | Safety certifications | CE, UL, CSA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
```

Target sizes: 5-10 core, 10-15 extended, total under 30.

The `product-taxonomy` skill's self-verification checks update to:
- Core: 5-10 attributes (was: n/a)
- Extended: 10-15 attributes (was: n/a)
- Total: 15-30 attributes (was: 20-40)
- Two table sections required: `## Core Attributes` and `## Extended Attributes` (was: single `## Attributes`)

### 6. Taxonomy Feedback Loop

Triggered during scraper generation (Stage 3), as a **post-generation step** after the scraper passes its `--limit 20` test. This ensures the feedback does not affect the current scraper generation — it prepares improvements for the next run.

1. **Collect** all unique attribute keys from the test output (20 products across categories)
2. **Compare** against schema — identify mapped vs unmapped attributes
3. **Evaluate significance** — did the unmapped attribute appear on >80% of test products?
4. **Trigger taxonomy update** — invoke `/product-taxonomy` in evolution mode (add-only) for significant unmapped attributes. The taxonomy skill researches whether the attribute is genuinely significant for the subcategory (not just company-specific).
5. **Log** what was added — the scraper-generator reports which attributes were proposed to the taxonomy

The feedback does NOT re-map the current scraper's output. The newly added extended attributes will be used when this company's scraper is regenerated in the future, or when other companies in the same subcategory are scraped.

#### Evolution rules (add-only)

- Can add new extended attributes
- Can promote extended → core when an attribute appears in scraper output from 3+ different companies for that subcategory. Promotion is triggered by a verification script that scans all scraper configs for the subcategory and counts attribute frequency.
- Never delete or rename existing attributes (exception: one-time migration, see Section 8)
- The one-time migration (Section 8) is explicitly exempted from this rule — it may restructure, trim, and split existing schemas

#### Concurrency

If two scraper-generators for companies in the same subcategory run concurrently and both trigger taxonomy evolution:
- The taxonomy skill uses file-level writes — the second write overwrites the first
- To prevent this: the feedback step acquires a simple file lock (`{schema-file}.lock` next to the schema file). If locked, skip the feedback step (the other agent is handling it). Log a warning.
- Lock staleness: locks older than 10 minutes are considered stale and can be broken (the holding agent likely crashed).

### 7. Skill Changes

**`categories.md`:**
- Add dot-notation ID to every subcategory (237 IDs)
- Add ID uniqueness verification script

**`product-taxonomy` skill:**
- New schema format with Core/Extended split
- Core: 5-10, Extended: 10-15, total 15-30
- Self-verification checks updated for new format and targets
- Evolution mode: add-only to extended, promote to core by frequency

**`product-classifier` skill (Stage 1):**
- Uses taxonomy IDs instead of display names
- Company report has `Subcategories` field listing ALL relevant taxonomy IDs (unlimited)
- Company report has `Primary` field for the single most representative subcategory
- The "hard limit: one primary, at most one secondary" rule is replaced by "unlimited subcategories, one primary"

**`catalog-detector` skill (Stage 2):**
- No structural changes
- The catalog assessment should note URL path patterns observed per product category (useful for scraper-generator's URL mapping)

**`scraper-generator` skill (Stage 3):**
- Reads schema core/extended attribute names for all company subcategories
- Maps extracted fields to schema names (exact match required for core/extended)
- Unmapped → `extra_attributes`
- Builds URL-prefix → taxonomy ID mapping for `product_category`
- Multi-subcategory: loads multiple schemas, maps each product to correct one
- Outputs new three-bucket record format with `_format: 2`
- Post-test: runs taxonomy feedback loop for significant unmapped attributes

**`eval-generator` skill (Stage 4):**

Updated check definitions (weights sum to 100):

| Check | Weight | Threshold | Change |
|-------|--------|-----------|--------|
| `core_attribute_coverage` | 20 | 0.90 | was: `attribute_coverage` (20). Now checks only core attributes. |
| `extended_attribute_coverage` | 5 | 0.50 | NEW. Lighter check for extended attributes. |
| `pagination_completeness` | 10 | 0.70 | was: 15. Reduced to make room. |
| `category_diversity` | 5 | 0.50 | was: 10. Reduced to make room. |
| `category_classification` | 10 | 0.95 | NEW. % of products with valid taxonomy ID. |
| `price_sanity` | 10 | 1.00 | unchanged from current. |
| `data_freshness` | 5 | 1.00 | was: 10. Reduced to make room. |
| `schema_conformance` | 5 | 1.00 | was: 10. Now checks core + extended types. |
| `row_count_trend` | 5 | 0.80 | was: 10. Reduced to make room. |
| `duplicate_detection` | 10 | 0.99 | KEPT from current. Detects duplicate products by SKU. |
| `field_level_regression` | 10 | 0.50 | KEPT from current. Detects per-field fill rate drops vs previous run. |
| `extra_attributes_ratio` | 5 | 0.50 | NEW. Value = 1 - (extra_count / (core+extended count)). Higher is better. Flags inadequate schemas. |

Weights sum to 100. The `extra_attributes_ratio` is defined as `1 - (extra / (core + extended))` so that a higher value is better (fewer extras relative to schema-aligned attributes), consistent with all other checks where higher = better.

The eval script handles both v1 and v2 format records:
- v1 (no `_format` field): treats `attributes` as a flat dict, applies old-style checks
- v2 (`_format: 2`): uses `core_attributes`, `extended_attributes`, `extra_attributes`

### 8. Migration Plan (Big Bang)

One-time migration of all 237 schemas. This migration is explicitly exempted from the append-only evolution rule — it may restructure, trim, and drop attributes.

#### Step 1: Assign taxonomy IDs

Add dot-notation IDs to every subcategory line in `categories.md`. Run the uniqueness verification script. Commit.

#### Step 2: Migrate schemas

Run 237 parallel agents, each one:
1. Reads the existing flat schema
2. Applies core selection heuristics:
   - Identity attributes (type, form, kind) → core
   - Material/composition → core
   - Primary dimension/size → core
   - Performance metrics → extended
   - Product-type-specific → extended
   - Certifications, accessories, packaging → extended
   - Deep spec sheet only (sound power level, vibration level) → drop
3. Writes the updated schema in the new two-table format with `**Taxonomy ID:**` header
4. Self-verifies: core has 5-10, extended has 10-15, total 15-30

#### Step 3: Verify

Run verification across all schemas:
- Every schema has `## Core Attributes` and `## Extended Attributes` sections
- Every schema has a `**Taxonomy ID:**` that matches an ID in `categories.md`
- Core count: 5-10
- Extended count: 10-15
- Total: 15-30
- No backticks in table cells
- No duplicate attribute names across core and extended

#### Rollback

The entire migration is a single git commit. Rollback: `git revert <commit>`. All schemas return to their previous flat format. No data is lost — the migration only changes file format, it does not delete files.

#### Existing scrapers

Existing generated scrapers continue to run with v1 format output. They are NOT regenerated as part of this migration. When a company next goes through the pipeline (either for maintenance or new discovery), its scraper is regenerated with the new format. This avoids a risky mass regeneration of scraper code.

## Non-Goals

- Real-time product search UI (this spec is about data structure, not search infrastructure)
- Changing the scraper execution model (daily CronJobs remain unchanged)
- Cross-subcategory attribute standardization (each subcategory schema is independent)
- Mass regeneration of existing scrapers (they adopt new format when regenerated individually)
