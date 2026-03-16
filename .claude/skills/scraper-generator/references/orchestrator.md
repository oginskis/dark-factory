# Scraper Generator Workflow

**Input:** Company report, catalog assessment, and SKU schema(s)
**Output:** Scraper code, config metadata, and product data contract

---

## Context

This workflow generates a production-ready Python scraper that extracts structured product data from a company's catalog. It orchestrates three sub-agents — label discoverer, code generator, and validator — and owns all retry and escalation decisions. The scraper must be a single self-contained file with no imports from the rest of the codebase.

### Step flow

```
Step 1: Load Context ──────────────────────────────────────────────────────────
  Read company report + catalog assessment
  │
  ├─ No catalog assessment? ──► ESCALATE: missing_catalog_assessment ──► STOP
  │
  ▼
Step 1b: Build Category Mapping ───────────────────────────────────────────────
  Map URL prefixes → taxonomy IDs
  │
  ├─ Unmapped URL prefix? ──► ESCALATE: unmapped_url_prefix ──► STOP
  │
  ▼
Step 2: Load SKU Schemas ──────────────────────────────────────────────────────
  Load schema for each subcategory
  │
  ├─ Schema missing, subcategory exists? ──► Auto-generate via /product-taxonomy
  │                                          (max 5 auto-generations per run)
  ├─ Schema missing, subcategory NOT in taxonomy? ──► ESCALATE: no_sku_schema ──► STOP
  │
  ▼
Step 2a: Map Attributes to Schema ─────────────────────────────────────────────
  Build core/extended/extra routing tables per subcategory
  │
  ▼
  ┌─ English site? ──────────────────────────────────────────────────────────┐
  │  skip label discovery                                                    │
  └──────────────────────────────────────────────────────────────────────────┘
  │
  ▼ non-English only
DISPATCH: Label Discoverer ────────────────────────────────────────────────────
  Sample site, build LABEL_MAP + CATEGORY_ALIASES
  │
  ├─ coverage_sufficient = true? ──► continue
  ├─ coverage_sufficient = false, attempts < 3? ──► re-dispatch (extended)
  ├─ coverage_sufficient = false, attempts = 3? ──► ESCALATE: label_coverage_insufficient ──► STOP
  │
  ▼
DISPATCH: Code Generator ──────────────────────────────────────────────────────
  Generate scraper.py
  │
  ▼
DISPATCH: Validator ───────────────────────────────────────────────────────────
  Probe → smoke test → taxonomy feedback → final verification
  │
  ├─ pass ──────────────────────────────────────────────────────────► continue
  │
  ├─ label_coverage_dropped (budget remains)
  │    ──► re-dispatch label discoverer
  │    ──► re-dispatch code generator
  │    ──► re-dispatch validator ─────────────────────────────────────────────┐
  │                                                                           │
  ├─ core_fill_rate_low                                                       │
  │    ──► fix routing tables / re-dispatch label discoverer if needed        │
  │    ──► re-dispatch code generator                                         │
  │    ──► re-dispatch validator ─────────────────────────────────────────────┤
  │                                                                           │
  ├─ probe_failed (after 5 internal fix cycles) ───────────────────────────► ESCALATE: probe_extraction_failed ──► STOP
  │                                                                           │
  ├─ test_failed / timeout (first failure)                                    │
  │    ──► re-dispatch code generator with diagnostics                        │
  │    ──► re-dispatch validator ─────────────────────────────────────────────┤
  │                                                                           │
  ├─ test_failed / timeout (second failure) ────────────────────────────────► ESCALATE: scraper_test_failed ──► STOP
  │                                                                           │
  ◄───────────────────────────────────────────────────────────────────────────┘
  │
  ▼
Step 3: Platform Knowledgebase ────────────────────────────────────────────────
  Write discoveries (skip for custom/unknown platforms)
  │
  ▼
Step 4: Config Metadata ───────────────────────────────────────────────────────
  Write config.json
  │
  ▼
Step 5: Self-Verification ─────────────────────────────────────────────────────
  Check orchestrator-level quality gates
  │
  ▼
  DONE ── scraper.py + config.json + output/products.jsonl ready for eval
```

---

## Step 1: Load Context

Read the company report and extract: site URL, subcategory taxonomy IDs, business model.

Read the catalog assessment and extract: scraping strategy (`static_html`, `structured_data`, `pdf_pricelist`), catalog structure (categories, navigation paths, pagination patterns), estimated product count, catalog entry points, anti-bot notes, and platform (e.g., `woocommerce`, `shopify`, `unknown`).

If no catalog assessment exists, escalate — see the `missing_catalog_assessment` decision.

---

## Step 1b: Build Category Mapping

Map each URL prefix from the catalog assessment to a taxonomy ID so the scraper classifies products at runtime without any LLM. **Every URL prefix MUST be mapped.** If a prefix cannot be matched to any subcategory in the company report, escalate — see the `unmapped_url_prefix` decision. Set `default_category` to the company's primary taxonomy ID (fallback when no prefix matches).

For single-subcategory companies, the mapping is trivial — `category_mapping` can be empty and all products use `default_category`.

Store the mapping in config (see Step 4):
```json
{
  "category_mapping": {
    "/Head-Protection/": "safety.head_protection",
    "/Respiratory-Protection/": "safety.respiratory_protection"
  },
  "default_category": "safety.respiratory_protection"
}
```

---

## Step 2: Load the SKU Schema

Load the SKU schema for each subcategory in the company report. For single-subcategory companies, load one schema. For multi-subcategory companies, load a schema per subcategory — the scraper uses the Step 1b category mapping to determine which schema applies per product.

If no SKU schema exists, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision. **Circuit breaker:** Auto-generate at most 5 missing schemas per run (starting with the primary, then by estimated product count). Log a warning for any remaining missing schemas.

---

## Step 2a: Map Attributes to Schema

Build attribute routing tables per subcategory to pass to the code generator.

- Matched **core** Key → `core_attributes`
- Matched **extended** Key → `extended_attributes`
- No match → `extra_attributes`

Use **EXACT key values** from the schema's Key column. For multi-subcategory companies, build a separate routing table per subcategory — the same attribute may be core in one schema and extended in another.

**`extra_attributes` governance:** `snake_case` keys; primitive values (`string`, `number`, `boolean`) or arrays of primitives; no nested objects.

---

## Dispatch: Label Discovery (non-English only)

Skip for English-language sites.

### Input contract

| Field | Description |
|---|---|
| `site_url` | Base URL of the site |
| `scraping_strategy` | From the catalog assessment |
| `catalog_structure` | Categories, subcategory URLs, navigation paths |
| `sku_schemas` | Map of taxonomy ID → loaded schema (core + extended attribute tables) |
| `subcategory_ids` | All taxonomy IDs the company covers |
| `site_language` | ISO 639-1 language code |

### Output contract

| Field | Description |
|---|---|
| `label_map` | `LABEL_MAP`: normalised site labels → English intermediate keys |
| `category_aliases` | `CATEGORY_ALIASES`: taxonomy ID → intermediate key → schema Key overrides |
| `coverage` | Overall label coverage (0.0–1.0) |
| `per_subcategory_coverage` | Taxonomy ID → coverage float |
| `unmapped_labels` | Labels present in inventory but not in `LABEL_MAP` |
| `extension_attempts` | Number of extension cycles performed (0–3) |
| `coverage_sufficient` | `true` if coverage ≥ 70% |

### Dispatch conditions

- `coverage_sufficient = true` → proceed to code generation.
- `coverage_sufficient = false`, `extension_attempts < 3` → re-dispatch, passing `extension_attempts` so the sub-agent continues from where it left off.
- `coverage_sufficient = false`, `extension_attempts = 3` → escalate — see the `label_coverage_insufficient` decision.

---

## Dispatch: Code Generation

### Input contract

| Field | Description |
|---|---|
| `scraping_strategy` | From the catalog assessment |
| `catalog_structure` | Categories, navigation paths, pagination patterns, entry points, anti-bot notes |
| `estimated_product_count` | From the catalog assessment |
| `platform` | CMS/e-commerce platform |
| `platform_knowledgebase` | Selectors, patterns, pitfalls from prior runs on this platform (if available) |
| `sku_schemas` | Core and extended attribute tables per subcategory |
| `attribute_routing_tables` | Core/extended/extra routing per subcategory, built in Step 2a |
| `label_map` | Non-English sites only — from label discoverer output |
| `category_aliases` | Non-English sites only — from label discoverer output |
| `category_mapping` | URL prefix → taxonomy ID mapping (from Step 1b) |
| `default_category` | The company's primary taxonomy ID |
| `persist_hook_implementations` | `setup`, `persist`, `teardown` function bodies from the harness |
| `fix_guidance` | On re-dispatch only — diagnostics from the validator's prior failure |

### Output contract

A single standalone Python file (scraper.py).

---

## Dispatch: Validation

### Input contract

| Field | Description |
|---|---|
| `scraper` | The generated scraper artifact |
| `catalog_structure` | Categories, navigation paths, top-level category list |
| `expected_product_count` | From the catalog assessment |
| `label_coverage` | Coverage float from label discoverer (non-English only) |
| `extension_attempts_used` | Label-discovery extension attempts already consumed (non-English only) |

### Output contract

| Field | Description |
|---|---|
| `status` | One of: `pass`, `label_coverage_dropped`, `core_fill_rate_low`, `probe_failed`, `test_failed`, `timeout` |
| `probe_results` | Per-URL probe outcomes |
| `smoke_test_summary` | Summary from smoke test teardown, or `null` |
| `final_verification_summary` | Summary from final verification, or `null` if skipped |
| `taxonomy_feedback` | Extra attributes proposed for schema addition, or `null` if skipped |
| `label_coverage_at_probe` | Recomputed label coverage after probing (non-English only) |
| `fix_cycles_used` | Map of gate name → fix-reprobe cycles consumed |

### Retry state machine

```
"pass"
  → Steps 3, 4, 5

"label_coverage_dropped" (extension_attempts_used < 3)
  → re-dispatch label discoverer (passing extension_attempts_used)
  → re-dispatch code generator with updated label_map + category_aliases
  → re-dispatch validator

"label_coverage_dropped" (extension_attempts_used = 3)
  → ESCALATE: label_coverage_insufficient

"core_fill_rate_low"
  → fix routing tables (Step 2a) or re-dispatch label discoverer if needed
  → re-dispatch code generator → re-dispatch validator

"probe_failed"
  → ESCALATE: probe_extraction_failed

"test_failed" / "timeout" (first failure)
  → re-dispatch code generator with fix_guidance = validator diagnostics
  → re-dispatch validator

"test_failed" / "timeout" (second failure)
  → ESCALATE: scraper_test_failed
```

---

## Step 3: Write Back to Platform Knowledgebase

After successful validation, write discoveries back to the platform knowledgebase. Skip for `unknown` or `custom` platforms — only run for enumerated values (`woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`). Create if it doesn't exist; append without removing existing content.

Write to: **JSON-LD Patterns**, **CSS Selectors**, **Pagination**, **Common Pitfalls**, **Sites Using This Platform** (company name, slug, date, any unusual notes).

---

## Step 4: Prepare Config Metadata

Produce config metadata for the scraper:

```json
{
  "company_slug": "{slug}",
  "category": "{taxonomy_id}",
  "sku_schema": "{category-slug}",
  "scraping_strategy": "static_html",
  "expected_product_count": 1200,
  "subcategories": ["safety.head_protection", "safety.respiratory_protection"],
  "category_mapping": {
    "/Head-Protection/": "safety.head_protection",
    "/Respiratory-Protection/": "safety.respiratory_protection"
  },
  "default_category": "safety.respiratory_protection",
  "generated_at": "2026-03-14T12:00:00Z"
}
```

- `category` — the primary taxonomy ID from the company report
- `sku_schema` — the slug of the SKU schema used (primary subcategory for multi-subcategory companies)
- `scraping_strategy` — the strategy the scraper implements
- `expected_product_count` — from the catalog assessment, updated with actual count if higher
- `subcategories` — list of all taxonomy IDs this scraper covers
- `category_mapping` — URL path prefixes → taxonomy IDs (empty for single-subcategory companies)
- `default_category` — the company's primary taxonomy ID, used as fallback `product_category`
- `generated_at` — ISO 8601 timestamp of when the scraper was generated

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Product data is a flat list of records** | One record per product, all at same level | Nested grouping by category, hierarchical structures |
| **`brand` is a top-level field** | `"brand": "Milwaukee Tool"` at root | `"brand"` inside `core_attributes` or any attribute bucket |
| **`product_category` is a valid taxonomy ID** | `"product_category": "machinery.power_tools"` | Display names like `"Machinery > Power Tools"`, missing field |
| **Price is a float, no currency symbols** | `224.99` | `"$224.99"`, `"224.99"`, `"USD 224.99"` |
| **Currency is ISO 4217** | `"USD"`, `"EUR"`, `"GBP"` | `"$"`, `"dollars"`, `"us"` |
| **SKU is a string** | `"871WAR1926F"` | `871` (numeric), `null` |
| **Core attributes match schema core list** | `"core_attributes": {"voltage": 18}` with `voltage` in schema core | Invented names, extended attrs in core bucket |
| **Extended attributes match schema extended list** | `"extended_attributes": {"chuck_size": 13}` with `chuck_size` in schema extended | Core attrs in extended bucket, invented names |
| **Extra attributes are governed** | `snake_case` keys, primitive values (string/number/boolean/array of primitives) | camelCase keys, nested objects |
| **`category_path` uses ` > ` separator** | `"Tools > Saws > Plunge-Cut Saws"` | `"Tools / Saws"`, `"Tools>Saws"` (no spaces) |
| **Config metadata matches schema** | All fields present with correct types | Missing fields, wrong types |

---

## Step 5: Self-Verification

Before presenting results, verify the scraper and config against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Scraper is standalone** | Single .py file, no imports from the codebase, only allowed libraries |
| 2 | **Validation passed** | Validator returned `pass` |
| 3 | **Product data contract correct** | Flat list of product records with universal top-level fields plus three attribute buckets |
| 4 | **`brand` is top-level** | `brand` appears as a top-level field in every product record, not inside any attribute bucket |
| 5 | **`product_category` is valid** | `product_category` is a valid taxonomy ID from the product taxonomy categories file |
| 6 | **`core_attributes` keys match schema** | Every key in `core_attributes` appears in the Key column of the SKU schema's Core Attributes table |
| 7 | **`extended_attributes` keys match schema** | Every key in `extended_attributes` appears in the Key column of the SKU schema's Extended Attributes table |
| 8 | **`extra_attributes` keys are governed** | Keys are `snake_case`, values are primitives (string, number, boolean) or arrays of primitives, no nested objects |
| 9 | **Config metadata complete** | All required fields present with correct values, including `subcategories`, `category_mapping`, and `default_category`. For multi-subcategory companies, every URL prefix from the catalog assessment appears in `category_mapping`. |
| 10 | **Platform knowledgebase updated** | Knowledgebase was written or updated after successful validation (when platform is an enumerated value — not `unknown` or `custom`) |
| 11 | **Multi-subcategory mapping correct** | For multi-subcategory companies: category mapping covers all URL prefixes, scraper uses per-subcategory SKU schemas for attribute routing, and `product_category` varies correctly across products from different sections. |
| 12 | **`attribute_units` correct** | `attribute_units` is a top-level dict. Every key appears in exactly one of `core_attributes`, `extended_attributes`, or `extra_attributes`. Values are strings. Attributes with schema Unit `—` do not appear. |
| 13 | **Label coverage sufficient (non-English sites)** | LABEL_MAP covers ≥70% of discovered attribute labels that map to schema keys. Context-dependent aliases (CATEGORY_ALIASES) exist when the same label maps to different schema keys per subcategory. Skip for English sites. |

If all 13 pass, the scraper is complete.

---

## Boundaries

- This workflow generates scrapers only — it does not assess catalog scrapability (catalog-detector) or generate quality validation (eval-generator).
- It does not define or modify the product taxonomy or SKU schemas.
- It does not run the scraper in production — validation sub-agent performs dry-run tests during generation.

---

## Decisions

### Decision: missing_catalog_assessment

**Context:** No catalog assessment exists — the catalog-detector has not run yet. The scraper cannot be generated without knowing the site structure and scraping strategy.
**Autonomous resolution:** Never.
**Escalate when:** Always. Report the missing assessment and suggest running the catalog-detector first.
**Escalation payload:** Company slug, location where the catalog assessment was expected.

### Decision: unmapped_url_prefix

**Context:** A URL path pattern from the catalog assessment cannot be mapped to any subcategory in the company report. Silently skipping would misclassify those products under the default category.
**Autonomous resolution:** Never.
**Escalate when:** Always. Report the unmapped prefix and the full list of subcategories and URL patterns.
**Escalation payload:** Company slug, the unmapped URL prefix, the list of subcategories, all URL patterns from the catalog assessment.

### Decision: no_sku_schema

**Context:** No SKU schema file exists for the company's product category.
**Autonomous resolution:** Verify that the subcategory from the company report exists in the product taxonomy categories file. If it does, the schema simply hasn't been created yet — trigger SKU schema generation for that subcategory. Once the schema is available, return to Step 2 and continue.
**Escalate when:** The subcategory from the company report does not appear in the product taxonomy categories file. This indicates a taxonomy integrity issue that must be resolved before the pipeline can continue.
**Escalation payload:** Company slug, the taxonomy ID from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: label_coverage_insufficient

**Context:** The site uses a non-English language and the LABEL_MAP cannot achieve ≥70% coverage of attribute labels that map to schema keys, even after 3 extension attempts. This means the site's attribute vocabulary is too different from the SKU schemas, or the schemas lack keys for attributes this site commonly provides.
**Autonomous resolution:** Never. This indicates a structural mismatch between the site's data model and the taxonomy schemas that cannot be solved by adding more label mappings.
**Escalate when:** Label coverage remains below 70% after 3 extension attempts.
**Escalation payload:** Company slug, current label coverage percentage, the label inventory (all discovered labels), which labels have no schema mapping, and which subcategories are most affected.

### Decision: probe_extraction_failed

**Context:** The probe found that the scraper's extraction logic does not work against the actual product pages — selectors don't match, JSON-LD structure is unexpected, or universal attributes cannot be extracted.
**Autonomous resolution:** Fix the scraper code and re-probe. The validator handles up to 5 probe-fix cycles internally.
**Escalate when:** The validator returns `probe_failed` — the 5-cycle internal circuit breaker was exhausted.
**Escalation payload:** Company slug, the specific extraction failure, what was tried, sample HTML from the problematic page.

### Decision: scraper_test_failed

**Context:** The scraper failed during the smoke test or final verification run — it crashed, produced no output, found far fewer products than expected, or had widespread missing data. The probe passed, so this is a structural issue (pagination, rate limiting, batching), not an extraction issue.
**Autonomous resolution:** Re-dispatch code generator with diagnostics and re-run validation once.
**Escalate when:** The validator returns `test_failed` or `timeout` a second time after the re-dispatch.
**Escalation payload:** Company slug, error details or partial results, what was tried in the retry, the scraping strategy that was used.
