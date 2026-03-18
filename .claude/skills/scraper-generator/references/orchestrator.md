# Scraper Generator Workflow

**Input:** Company report, catalog assessment, and SKU schema(s)
**Output:** Scraper code, config metadata, and product data contract

---

## Context

This workflow generates a production-ready Python scraper that extracts structured product data from a company's catalog. The orchestrator is **pure coordination** — it never writes code and never runs the scraper. It dispatches two sub-agents: the **coder** (writes and patches `scraper.py`) and the **tester** (runs the scraper, evaluates output, writes `test_report.json`). The orchestrator owns all retry logic, escalation decisions, and state transitions. The scraper must be a single self-contained file with no imports from the rest of the codebase.

### Step flow

```
Step 1: Load Context ──────────────────────────────────────────────────────────
  Read company report + catalog assessment + generator_input.json
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
  │  skip Step 2b                                                            │
  └──────────────────────────────────────────────────────────────────────────┘
  │
  ▼ non-English only
Step 2b: Build Label Map ──────────────────────────────────────────────────────
  Build LABEL_MAP + CATEGORY_ALIASES from language seed + blueprint labels
  │
  ├─ coverage ≥ 70%? ──► continue
  ├─ coverage 30–70%? ──► log warning, continue
  ├─ coverage < 30%? ──► ESCALATE: label_coverage_insufficient ──► STOP
  │
  ▼
DISPATCH: Coder (mode: "generate") ────────────────────────────────────────────
  Writes scraper.py
  │
  ▼
DISPATCH: Tester (mode: "full") ───────────────────────────────────────────────
  Runs scraper, evaluates output, writes test_report.json
  │
  ├─ "pass" ──────────────────────────────────────────────────────► Step 3
  │
  ├─ "needs_fix" ──► Fix→Retest Loop (max 3 cycles) ─────────────────────┐
  │                                                                       │
  │   DISPATCH: Coder (mode: "fix")                                       │
  │     ← scraper.py patched                                              │
  │   DISPATCH: Tester (mode: "retest")                                   │
  │     ← test_report.json overwritten                                    │
  │     ├─ "pass" ──► DISPATCH: Tester (mode: "final")                    │
  │     │               ├─ "pass" ──────────────────────────────► Step 3   │
  │     │               ├─ "needs_fix" / "unfixable" ──► ESCALATE         │
  │     ├─ "needs_fix" ──► next fix cycle ────────────────────────────────┤
  │     ├─ "unfixable" ──► ESCALATE: scraper_test_failed ──► STOP         │
  │                                                                       │
  │   Budget exhausted (3 cycles) ──► ESCALATE: scraper_test_failed ──► STOP
  │                                                                       │
  ├─ "unfixable" ──► ESCALATE: scraper_test_failed ──► STOP               │
  │                                                                       │
  ◄───────────────────────────────────────────────────────────────────────┘
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

Read the catalog assessment and extract: scraping strategy (`static_html`, `structured_data`, `pdf_pricelist`), platform, estimated product count, anti-bot severity, and currency from the header metadata. Read the `## Extraction Blueprint` section for the data source (API endpoints, selectors), product discovery (pagination, verified category tree), product data extraction (price, name, SKU, spec table, breadcrumb selectors with verified examples), and platform-specific notes.

If no catalog assessment exists, escalate — see the `missing_catalog_assessment` decision.

Read the pre-processed generator input file. This JSON contains attribute routing tables (core/extended key lists and types per subcategory) built from the SKU schemas by the pre-processing script. Use these tables directly in Steps 2a and the coder dispatch — do not re-read raw SKU schema files.

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

Build attribute routing tables per subcategory to pass to the coder.

- Matched **core** Key → `core_attributes`
- Matched **extended** Key → `extended_attributes`
- No match → `extra_attributes`

Use **EXACT key values** from the schema's Key column. For multi-subcategory companies, build a separate routing table per subcategory — the same attribute may be core in one schema and extended in another.

**`extra_attributes` governance:** `snake_case` keys; primitive values (`string`, `number`, `boolean`) or arrays of primitives; no nested objects.

This step is handled by `prepare_generator_input.py`, which produces the `generator_input.json` file with routing tables and units per subcategory. The orchestrator uses this file for coder dispatch context.

---

## Step 2b: Build Label Map (non-English only)

Skip for English-language sites.

Build the `LABEL_MAP` and `CATEGORY_ALIASES` dicts that the scraper will use to translate source-language attribute labels to English schema keys.

**Sources (in priority order):**
1. **Language seed file** — check the platform knowledgebase for a language seed (e.g., `labels-lv.json` for Latvian). Load common translations as the starting point.
2. **Extraction blueprint sample labels** — the catalog assessment's `## Extraction Blueprint > ### Product Data Extraction > #### Sample Attribute Labels` table contains sample attribute labels from 3-5 product pages. Map each label to a schema key using the attribute routing tables from Step 2a.
3. **Unmapped labels** — labels that don't match any schema key go to `extra_attributes` with `snake_case` keys.

**Build CATEGORY_ALIASES** for labels that map to different schema keys per subcategory (e.g., "thickness" → `nominal_thickness` for lumber, `thickness` for flooring). The language seed may already contain aliases — use those, add new ones from blueprint labels.

**Label coverage:** Count mapped labels vs total. Below 70%: log warning, proceed. Below 30%: escalate — see the `label_coverage_insufficient` decision.

**After successful scraper generation:** Save the merged LABEL_MAP back to the language seed file to enrich it for future sites.

---

## Dispatch: Coder (mode: "generate")

Dispatch the coder sub-agent to write the initial `scraper.py`. The coder reads `references/coder.md` for the complete product record format, library selection, required behavior, product discovery strategy, CLI flags, persist hooks, and Python code quality rules.

### Input to coder

| Field | Description |
|---|---|
| `mode` | `"generate"` |
| `catalog_assessment_path` | Path to the catalog assessment file |
| `routing_tables_path` | Path to `generator_input.json` |
| `category_mapping` | URL prefix → taxonomy ID mapping from Step 1b |
| `platform_knowledgebase_path` | Path to the platform knowledgebase file (if applicable) |
| `label_map` | `LABEL_MAP` dict from Step 2b (non-English only, omit for English) |
| `category_aliases` | `CATEGORY_ALIASES` dict from Step 2b (non-English only, omit for English) |
| `scraper_output_path` | Path where the coder writes `scraper.py` |

### Output from coder

The coder writes `scraper.py` to the specified path. No structured return — the file on disk is the output.

---

## Dispatch: Tester

Dispatch the tester sub-agent to run the scraper and evaluate its output. The tester reads `references/tester.md` for validation rules, run strategies, and report format.

### Input to tester

| Field | Description |
|---|---|
| `mode` | One of: `"full"`, `"retest"`, `"final"` |
| `scraper_path` | Path to `scraper.py` |
| `catalog_structure` | Categories, navigation paths, top-level category list from catalog assessment |
| `expected_product_count` | From the catalog assessment |
| `routing_tables_path` | Path to `generator_input.json` (for schema-aware validation rules) |
| `test_report_path` | Path where the tester writes `test_report.json` |
| `fix_targets` | (retest only) Rule IDs that the coder fixed — tester focuses verification on these |
| `regression_sample_from` | (retest only) Categories that were passing before the fix — tester checks for regressions |

### Output from tester

The tester writes `test_report.json` to the specified path. Format:

```json
{
  "mode": "full",
  "timestamp": "2026-03-18T15:00:00Z",
  "status": "pass | needs_fix | unfixable",
  "smoke_summary": {
    "total_products": 20,
    "errors_count": 0,
    "duration_seconds": 45.2,
    "scraper_crashed": false,
    "persist_hook_verified": true
  },
  "final_summary": { "...": "same fields" },
  "rule_results": [
    {"id": "S01", "status": "pass", "value": 0.72, "threshold": 0.30, "per_category": {}},
    {"id": "M01", "status": "fail", "value": 0.95, "detail": "95% of products have units embedded"}
  ],
  "issues": [
    {
      "rule_id": "M01",
      "detail": "units embedded in values",
      "affected_categories": ["/shop/timber-joinery/joinery-timber/decorative-mouldings"],
      "affected_attributes": ["nominal_width", "nominal_thickness"],
      "sample_urls": ["https://example.com/p1", "https://example.com/p2"],
      "sample_values": {"nominal_width": ["18mm", "9mm", "12mm"]}
    }
  ],
  "passing_categories": ["/shop/sheet-materials/plywood/marine-plywood"]
}
```

Retest mode adds: `fix_results`, `regression_results`, `new_issues`.

---

## Fix→Retest Loop

The orchestrator manages a state machine that iterates between the coder and tester until the scraper passes or budget is exhausted.

### State machine

```
Read test_report.json
  │
  ├─ status: "pass" ──► continue to Step 3
  │
  ├─ status: "needs_fix" ──► enter fix loop
  │     │
  │     ▼
  │   [cycle = 1..3]
  │     │
  │     ├─ DISPATCH: Coder (mode: "fix")
  │     │    Pass: test_report.json path + full context (catalog assessment,
  │     │          routing tables, category mapping, platform knowledgebase,
  │     │          LABEL_MAP + CATEGORY_ALIASES if non-English)
  │     │    ← scraper.py patched
  │     │
  │     ├─ DISPATCH: Tester (mode: "retest")
  │     │    Pass: fix_targets (rule IDs from issues), regression_sample_from
  │     │          (passing_categories from previous test_report)
  │     │    ← test_report.json overwritten
  │     │
  │     ├─ Read test_report.json
  │     │    ├─ "pass" ──► DISPATCH: Tester (mode: "final")
  │     │    │               ├─ "pass" ──► continue to Step 3
  │     │    │               ├─ "needs_fix" or "unfixable" ──► ESCALATE: scraper_test_failed
  │     │    ├─ "needs_fix" ──► next cycle (if budget remains)
  │     │    ├─ "unfixable" ──► ESCALATE: scraper_test_failed
  │     │
  │     ├─ Budget exhausted (cycle > 3) ──► ESCALATE: scraper_test_failed
  │
  ├─ status: "unfixable" ──► ESCALATE: scraper_test_failed
```

### Coder fix dispatch input

Same fields as generate mode, plus:

| Field | Description |
|---|---|
| `mode` | `"fix"` |
| `test_report_path` | Path to the latest `test_report.json` |
| `existing_scraper_path` | Path to the current `scraper.py` to patch |

The coder receives the full context on every dispatch — it always has the complete picture.

### Circuit breakers

| Breaker | Limit |
|---|---|
| Fix → retest cycles | Max 3 |
| Same rule failing after fix | Max 2 attempts per rule. If a rule fails twice after targeted fixes, treat as unfixable. |
| Retest timeout | 5 minutes |
| Full/final timeout | max(120, sample_size * 6) seconds |

**Per-rule tracking:** The orchestrator tracks how many times each rule ID has been targeted for a fix. After 2 failed attempts for the same rule, the orchestrator stops retrying that rule and escalates.

---

## Label Extension Retry

For non-English sites, the tester may discover new attribute labels that were not in the initial LABEL_MAP. When `test_report.json` reveals unmapped labels (through low coverage in rule results or issues referencing unknown labels), the orchestrator extends the workflow:

1. Read the unmapped labels from the test report.
2. Extend LABEL_MAP with new mappings for the discovered labels.
3. Re-dispatch the coder (mode: "fix") with the updated LABEL_MAP.
4. Re-dispatch the tester to verify the fix.

**Circuit breaker:** Max 3 label extension attempts. If label coverage remains insufficient after 3 extensions, escalate — see the `label_coverage_insufficient` decision.

Label extension attempts are separate from the fix→retest cycle count. A label extension triggers a coder fix dispatch and tester retest, but uses its own counter.

---

## Diagnostic Persistence

### test_report.json

Written by the tester after every dispatch. Overwritten on each re-dispatch. The file always reflects the last tester run. Path: `docs/scraper-generator/{slug}/output/test_report.json`.

### validation.json

After successful validation (tester returns "pass" in final or full mode), the orchestrator writes `validation.json` for eval-generator compatibility. This file is derived from `test_report.json` and uses the same format as the current validation diagnostics:

- All test report fields are mapped to the validation.json schema.
- `generated_at` — ISO 8601 timestamp added by the orchestrator.
- In fix mode, `fix_summary` is included (see Fix Mode section).

Path: `docs/scraper-generator/{slug}/output/validation.json`.

On re-dispatch (after a fix cycle), overwrite the file with the new attempt's results. Write this file for both English and non-English sites.

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
| 2 | **Validation passed** | Tester returned `pass` (test_report.json status is "pass") |
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

## Fix Mode

When invoked by `/scraper-remediation` with a fix request JSON (`mode: "fix"`), the workflow operates differently from fresh generation.

### Fix Request Input

```json
{
  "mode": "fix",
  "cycle": 1,
  "slug": "harlowbros",
  "failing_checks": [
    {
      "check": "core_attribute_coverage",
      "value": 0.0,
      "threshold": 0.9,
      "subcategory_details": { "..." : "..." }
    }
  ],
  "passing_checks": [
    { "check": "price_sanity", "value": 1.0, "threshold": 1.0 }
  ],
  "scraper_path": "docs/scraper-generator/harlowbros/scraper.py",
  "eval_config_path": "docs/eval-generator/harlowbros/eval_config.json"
}
```

### Eval Check → Rule ID Mapping

When `/scraper-remediation` sends eval check names, the orchestrator maps them to tester rule IDs for targeted fix dispatch:

| Eval Check Name | Rule ID | Description |
|---|---|---|
| `core_attribute_coverage` | S01 | Core attribute fill rate |
| `extended_attribute_coverage` | S02 | Extended attribute fill rate |
| `schema_conformance` | M02 | Type conformance |
| `price_sanity` | S03 | Required top-level fields (includes price) |
| `pagination_completeness` | S06 | Category diversity / pagination |
| `duplicate_detection` | S07 | Zero errors in run (includes duplicates) |
| `category_diversity` | S06 | Category diversity |

The orchestrator uses these mapped rule IDs when dispatching the coder in fix mode, so the coder can reference the same rule definitions from `references/tester.md`.

### Fix Mode Step Flow

1. **Step 1 (load context):** Same as normal — read catalog assessment, company report, SKU schemas, config.json, generator_input.json. This provides the reference data needed to understand what the scraper should extract.

2. **Dispatch Coder (mode: "fix"):** Map the `failing_checks` from the fix request to rule IDs using the table above. Dispatch the coder with:
   - The existing `scraper.py` path
   - `test_report.json` (if available from a previous run) or a synthesized report from the eval check details
   - Full context: catalog assessment, routing tables, category mapping, platform knowledgebase, LABEL_MAP + CATEGORY_ALIASES (non-English)
   - The mapped rule IDs as fix targets
   - `passing_checks` values so the coder avoids regressions

   The coder reads and patches the existing scraper. Fix guidance per eval check:
   - `core_attribute_coverage` / `extended_attribute_coverage` → add or fix enrichment patterns, alias mappings, description parsing for missing attributes. Use `subcategory_details.top_missing` for specifics.
   - `schema_conformance` → fix type conversions, ensure spec table values match expected types.
   - `price_sanity` → fix price extraction logic.
   - `pagination_completeness` / `category_diversity` → fix category traversal, pagination, URL patterns.
   - `duplicate_detection` → fix SKU extraction or deduplication logic.

   If the problem requires a fundamental approach change (site switched from HTML to SPA, added bot protection, restructured all URLs), the coder sets `fix_outcome: "unfixable"` and the orchestrator returns immediately without further dispatch.

3. **Dispatch Tester (mode: "full"):** Same as normal — the tester runs the patched scraper with full validation. Tester internal retry counters reset fresh for each fix mode invocation. If the tester returns "needs_fix", enter the normal fix→retest loop (max 3 cycles).

4. **Diagnostic persistence:** Same as normal, plus write the `fix_summary` field to `validation.json`.

### fix_summary Format

Added to `validation.json` only in fix mode:

```json
{
  "fix_summary": {
    "summary": "Added name-enrichment patterns for wood_type, appearance_grade.",
    "fix_outcome": "fixed",
    "fix_targets": ["core_attribute_coverage", "schema_conformance"],
    "changes": [
      { "type": "enrichment_pattern", "attribute": "wood_type" },
      { "type": "type_conversion", "scope": "spec_table_numeric" }
    ]
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `summary` | string | Free-text description of changes made |
| `fix_outcome` | string | `"fixed"` (patches applied, validation passed), `"partial"` (some fixes applied but validation has issues), `"unfixable"` (fundamental change needed) |
| `fix_targets` | array of strings | Eval check names that the fix targeted |
| `changes` | array of objects | Structured change records. `type` is free-form text describing the kind of change. Additional fields vary by type. |

### Fix Mode Constraints

- **Do not archive** the existing scraper directory — the remediation skill handles backup.
- **Do not regenerate from scratch** — dispatch the coder to read and patch the existing scraper.py.
- **Do not modify** eval_config.json or any eval-generator artifacts.
- **Tester counters reset** each fix mode invocation — a new fix cycle gets the full retry budget.
- Fix mode does not create config.json or generator_input.json — these already exist from the original generation.

---

## Boundaries

- This workflow generates scrapers only — it does not assess catalog scrapability (catalog-detector) or generate quality validation (eval-generator).
- It does not define or modify the product taxonomy or SKU schemas.
- It does not run the scraper in production — the tester sub-agent performs dry-run tests during generation.
- The orchestrator never writes scraper code — the coder sub-agent handles all code generation and patching.
- The orchestrator never runs the scraper — the tester sub-agent handles all execution and evaluation.

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

**Context:** The site uses a non-English language and label coverage is too low for a viable scraper. Two paths trigger this decision: (1) the initial LABEL_MAP at Step 2b cannot reach 30% coverage, indicating a fundamental mismatch between the site's attribute vocabulary and the SKU schemas; (2) after 3 label extension attempts, label coverage still stays below 70%, indicating the gap cannot be closed incrementally.
**Autonomous resolution:** Never. Both trigger paths indicate a structural mismatch that cannot be solved by adding more label mappings.
**Escalate when:** Label coverage is below 30% at Step 2b (immediate), or label coverage remains below 70% after 3 label extension attempts (retry budget exhausted).
**Escalation payload:** Company slug, current label coverage percentage, the label inventory (all discovered labels), which labels have no schema mapping, and which subcategories are most affected.

### Decision: probe_extraction_failed

**Context:** The tester found that the scraper's extraction logic does not work against the actual product pages — selectors don't match, JSON-LD structure is unexpected, or universal attributes cannot be extracted.
**Autonomous resolution:** The orchestrator dispatches the coder in fix mode with the tester's diagnostics. The fix→retest loop handles up to 3 cycles.
**Escalate when:** The fix→retest loop budget is exhausted (3 cycles with no resolution, or a rule fails after 2 targeted fix attempts).
**Escalation payload:** Company slug, the specific extraction failure, what was tried across fix cycles, sample data from the problematic pages.

### Decision: scraper_test_failed

**Context:** The scraper failed during the full test or final verification run — it crashed, produced no output, found far fewer products than expected, or had widespread missing data.
**Autonomous resolution:** The orchestrator enters the fix→retest loop (max 3 cycles).
**Escalate when:** The fix→retest loop budget is exhausted, or the tester returns "unfixable", or the final run after all retests pass still fails.
**Escalation payload:** Company slug, error details or partial results, what was tried across fix cycles, the scraping strategy that was used.
