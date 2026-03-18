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
  │     ├─ "unfixable" ──► ESCALATE: probe_extraction_failed               │
  │     │                             or scraper_test_failed ──► STOP      │
  │                                                                       │
  │   Budget exhausted (3 cycles) ──► ESCALATE: probe_extraction_failed   │
  │                                   or scraper_test_failed ──► STOP
  │                                                                       │
  ├─ "unfixable" ──► ESCALATE: probe_extraction_failed or                 │
  │                             scraper_test_failed ──► STOP               │
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

Read the pre-processed generator input file. This JSON contains subcategory schemas (`core_attribute_keys`/`extended_attribute_keys` lists, `attribute_types` dict, and `units` dict per subcategory) built from the SKU schemas by the pre-processing script. Use these tables directly in Steps 2a and the coder dispatch — do not re-read raw SKU schema files.

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

## Step 2: Verify SKU Schemas

Check `generator_input.json` for each subcategory taxonomy ID from the company report. Each subcategory must have an entry in the `subcategory_schemas` dict. For single-subcategory companies, one entry. For multi-subcategory companies, one entry per subcategory — the scraper uses the Step 1b category mapping to determine which schema applies per product.

If a subcategory key is missing from `subcategory_schemas`, the pre-processing script could not find its schema file — see the `no_sku_schema` decision. **Circuit breaker:** Auto-generate at most 5 missing schemas per run (starting with the primary, then by estimated product count). Log a warning for any remaining missing schemas.

**After auto-generating any missing schemas:** Re-run `orchestrator_prepare_generator_input.py` with all taxonomy IDs to rebuild `generator_input.json` with the newly generated schemas included. Verify the regenerated file contains all expected subcategory keys before proceeding to Step 2a.

---

## Step 2a: Map Attributes to Schema

Build attribute routing tables per subcategory to pass to the coder.

- Matched **core** Key → `core_attributes`
- Matched **extended** Key → `extended_attributes`
- No match → `extra_attributes`

Use **EXACT key values** from the schema's Key column. For multi-subcategory companies, build a separate routing table per subcategory — the same attribute may be core in one schema and extended in another.

**`extra_attributes` governance:** `snake_case` keys; primitive values (`string`, `number`, `boolean`) or arrays of primitives; no nested objects.

This step is handled by `orchestrator_prepare_generator_input.py`, which produces the `generator_input.json` file with routing tables and units per subcategory. The orchestrator uses this file for coder dispatch context.

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
| `catalog_assessment` | Path to the catalog assessment file |
| `routing_tables_path` | Path to `generator_input.json` |
| `category_mapping` | URL prefix → taxonomy ID mapping from Step 1b |
| `platform_knowledgebase` | Path to the platform knowledgebase file (if applicable) |
| `LABEL_MAP` | Label map dict from Step 2b (non-English only, omit for English) |
| `CATEGORY_ALIASES` | Category aliases dict from Step 2b (non-English only, omit for English) |
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
| `iteration` | Iteration number (1 for first full run, increments for each retest/final) |
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
    "scraper_crashed": false,
    "persist_hook_verified": true,
    "duration_seconds": 45.2
  },
  "final_summary": {
    "total_products": 150,
    "errors_count": 0,
    "duration_seconds": 320.5,
    "scraper_crashed": false,
    "persist_hook_verified": true
  },
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
  │     │    │               ├─ "needs_fix" or "unfixable" ──► ESCALATE (see below)
  │     │    ├─ "needs_fix" ──► next cycle (if budget remains)
  │     │    ├─ "unfixable" ──► ESCALATE (see below)
  │     │
  │     ├─ Budget exhausted (cycle > 3) ──► ESCALATE (see below)
  │
  ├─ status: "unfixable" ──► ESCALATE (see below)

  ESCALATE decision routing:
    - Extraction failures (selectors don't match, probes return empty,
      universal attributes missing) ──► probe_extraction_failed
    - All other failures (crash, no output, low product count,
      widespread missing data) ──► scraper_test_failed
```

### "unfixable" status — context-dependent behavior

The tester returns `"unfixable"` when S08 (crash) or S09 (no output) fails. The orchestrator's response depends on the context:

| Context | Tester returns "unfixable" | Orchestrator action |
|---------|---------------------------|---------------------|
| **Full mode** (first run) | Scraper fundamentally broken | ESCALATE immediately. No fix loop — a crash or empty output on the first run means the extraction approach is wrong. |
| **Retest mode** (after a fix) | Fix introduced a crash or broke output | ESCALATE immediately. A coder patch that causes a crash is not recoverable by another patch — escalate with the debug log showing what broke. |
| **Final mode** (after retest passed) | Regression under full load | ESCALATE immediately. The scraper passed on a sample but fails at scale — likely a resource or pagination issue that needs investigation. |

In all three cases, the orchestrator does NOT retry. "Unfixable" always means immediate escalation. The distinction is which escalation decision to use: if the crash is related to extraction (selectors, parsing) → `probe_extraction_failed`; if it's a runtime issue (timeout, memory, HTTP) → `scraper_test_failed`.

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
| Same rule failing after fix | Max 2 targeted attempts per rule |
| Retest timeout | 5 minutes |
| Full/final timeout | max(120, sample_size * 6) seconds |

**Per-rule tracking:** The orchestrator maintains a dict `rule_fix_attempts: {rule_id: int}` counting how many times each rule has been explicitly listed in `fix_targets` for a coder dispatch. Only explicit targets increment the counter — a rule that fails as collateral damage from a fix aimed at a different rule does NOT count.

**Decision logic after each retest:**

```
for each failing rule in test_report:
    if rule_fix_attempts[rule] >= 2:
        mark rule as exhausted
    else:
        add to next fix_targets

if all failing rules are exhausted:
    ESCALATE (no fixable rules remain)
else if fix cycle > 3:
    ESCALATE (budget exhausted)
else:
    dispatch coder with remaining fix_targets
    increment rule_fix_attempts for each target
```

**Worked example:**

| Cycle | fix_targets sent | Tester result | rule_fix_attempts after |
|-------|-----------------|---------------|------------------------|
| 1 | `[S01, M01]` | S01 pass, M01 fail | `{S01: 1, M01: 1}` |
| 2 | `[M01]` | M01 fail, S03 fail (collateral) | `{S01: 1, M01: 2, S03: 0}` |
| 3 | `[S03]` | S03 fail | `{S01: 1, M01: 2, S03: 1}` |

At this point M01 is exhausted (2 attempts) but still failing → ESCALATE. S03 only has 1 attempt but the overall budget (3 cycles) is also exhausted. Note: M01 failing in cycle 2 counts as attempt 2 because it was in `fix_targets`. S03 failing in cycle 2 does NOT count because it was collateral — it only gets counted when explicitly targeted in cycle 3.

---

## Label Extension Retry

For non-English sites, the tester may discover new attribute labels that were not in the initial LABEL_MAP. When `test_report.json` reveals unmapped labels (through low coverage in rule results or issues referencing unknown labels), the orchestrator extends the workflow.

Label extension and fix→retest use **separate counters**. Each has a max of 3.

### State machine pseudocode

```
label_counter = 0
fix_counter = 0
phase = "label_extension"  # or "fix_retest"

after each tester dispatch:
    report = read test_report.json
    label_ok = (label_coverage >= 70%)
    has_label_issues = (label_coverage < 70% OR issues reference unknown labels)
    has_non_label_issues = any error-severity rule failed (S01, S03, S04, S05, S07, M01, M04)
    is_unfixable = (report.status == "unfixable")

    if is_unfixable:
        ESCALATE  # S08/S09 — fundamental failure

    if report.status == "pass":
        proceed to final mode (or Step 3 if already in final)

    # --- Phase: label_extension ---
    if phase == "label_extension":
        if has_label_issues AND label_counter < 3:
            extend LABEL_MAP with newly discovered labels
            dispatch coder (fix) with updated LABEL_MAP
            dispatch tester (retest)
            label_counter += 1
            # After retest, return to top of this decision block

        else if label_ok OR label_counter >= 3:
            # Label phase is done — either coverage met or budget exhausted
            if NOT label_ok AND label_counter >= 3:
                ESCALATE: label_coverage_insufficient

            if has_non_label_issues:
                phase = "fix_retest"
                fix_counter = 0  # fresh counter
                # Fall through to fix_retest phase below
            else:
                proceed to final mode

    # --- Phase: fix_retest ---
    if phase == "fix_retest":
        if has_non_label_issues AND fix_counter < 3:
            apply per-rule tracking (see Circuit Breakers)
            dispatch coder (fix) with fix_targets
            dispatch tester (retest)
            fix_counter += 1
        else:
            ESCALATE: probe_extraction_failed or scraper_test_failed
```

### Key rules

1. **Label issues are assessed by label coverage percentage**, not by which rule IDs fail. A low S01 score caused by unmapped labels is a label issue; a low S01 score with full label coverage is a non-label issue.
2. **The orchestrator never mixes phases.** It stays in label_extension until labels are resolved (≥70% or budget exhausted), then transitions to fix_retest if non-label issues remain. It never returns to label_extension after entering fix_retest.
3. **Transition resets the fix counter.** The fix_retest phase always starts at cycle=0, regardless of how many label extensions happened.
4. **Re-evaluate after each cycle.** After each tester retest, re-evaluate both `has_label_issues` and `has_non_label_issues` from the latest `test_report.json`. A label extension fix may resolve non-label issues as a side effect, potentially eliminating the need for a fix_retest phase.

### Budget

Worst-case dispatches: 3 label extensions (3 coder + 3 tester) + 3 fix-retest cycles (3 coder + 3 tester) + 1 final (tester only) = **6 coder dispatches + 7 tester dispatches**.

---

## Diagnostic Persistence

### test_report.json

Written by the tester after every dispatch. Overwritten on each re-dispatch. The file always reflects the last tester run. Path: `docs/scraper-generator/{slug}/output/test_report.json`.

### validation.json

After successful validation (tester returns "pass" in final or full mode), the orchestrator writes `validation.json` for diagnostic persistence and remediation tracking. The `/scraper-remediation` skill reads this file to diagnose degradation. The `/eval-generator` skill does NOT read it — it reads `products.jsonl` and `summary.json` directly.

Path: `docs/scraper-generator/{slug}/output/validation.json`.

**Schema — field mapping from test_report.json:**

```json
{
  "status": "pass",
  "probe_results": [],
  "smoke_test_summary": {},
  "final_verification_summary": {},
  "rule_results": [],
  "issues": [],
  "label_coverage_at_probe": null,
  "fix_cycles_used": 0,
  "generated_at": "2026-03-18T15:00:00Z",
  "fix_summary": null
}
```

| validation.json field | Source | Description |
|---|---|---|
| `status` | `test_report.status` | Overall pass/needs_fix/unfixable (always "pass" when written) |
| `probe_results` | Collected during full mode Step 1 | Array of probe trace objects from `tester_run_scraper.py --step probe` |
| `smoke_test_summary` | `test_report.smoke_summary` | Crash status, persist hook check, duration |
| `final_verification_summary` | `test_report.final_summary` | Total products, errors, duration |
| `rule_results` | `test_report.rule_results` | Array of per-rule pass/fail objects (S01-S09, M01-M04) |
| `issues` | `test_report.issues` | Array of issue details (empty when status is "pass") |
| `label_coverage_at_probe` | Orchestrator state | Float (0.0-1.0) for non-English sites, `null` for English |
| `fix_cycles_used` | Orchestrator state | Number of fix→retest cycles used (0 if passed on first try) |
| `generated_at` | Orchestrator | ISO 8601 timestamp when the orchestrator wrote this file |
| `fix_summary` | Fix mode only | Fix summary object (see Fix Mode section), `null` in normal mode |

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

### Output on success

| File | Description |
|------|-------------|
| `scraper.py` | Standalone scraper script |
| `config.json` | Config metadata (Step 4) |
| `output/products.jsonl` | Product data from final test run |
| `output/summary.json` | Run summary from scraper's teardown hook |
| `output/validation.json` | Validation diagnostics for eval-generator |
| `output/test_report.json` | Last tester report |
| `output/baseline_products.jsonl` | Baseline for future regression checks |

### Output on escalation (partial)

When the orchestrator escalates, these files may exist depending on how far the workflow progressed:

| File | Present when |
|------|-------------|
| `generator_input.json` | Step 1 completed (always, if pre-processing ran) |
| `scraper.py` | Coder dispatched at least once |
| `output/test_report.json` | Tester dispatched at least once |
| `output/debug_iteration_*.log` | Tester dispatched at least once |

No `config.json` or `validation.json` is written on escalation.

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

| Eval Check Name | Rule ID | Description | Scraper fixable? |
|---|---|---|---|
| `core_attribute_coverage` | S01 | Core attribute fill rate | Yes — fix extraction selectors |
| `extended_attribute_coverage` | S02 | Extended attribute fill rate | Yes — fix extraction selectors |
| `schema_conformance` | M02 | Type conformance (number attrs must be int/float) | Yes — fix type conversions |
| `price_sanity` | S03 | Required top-level fields present | Yes — fix field extraction |
| `pagination_completeness` | S06 | Category diversity / pagination | Yes — fix category traversal |
| `duplicate_detection` | S07 | Zero errors in run (includes duplicates) | Yes — fix deduplication |
| `category_diversity` | S06 | Category diversity | Yes — fix category traversal |
| `category_classification` | S04 | product_category is valid taxonomy ID | Yes — fix category_mapping |
| `data_freshness` | — | Checks scraped_at recency | No — rerun the scraper, not a code fix |
| `row_count_trend` | — | Product count vs historical baseline | No — site change or pagination issue, investigate first |
| `field_level_regression` | — | Field fill rates vs previous run | No — compare runs, not a code fix |
| `extra_attributes_ratio` | — | Extra attrs discovery rate | No — informational, no code fix |
| `semantic_validation` | M01, M04 (numeric format sub-checks only) | Domain-specific value checks | Partially — numeric format violations (e.g., `"18mm"` instead of `18`) map to M01/M04 and are fixable. Other semantic checks (non-product detection, domain value validation) are eval config issues, not scraper code. If `subcategory_details` references numeric format, set `fix_outcome: "fixed"` targets; otherwise `"unfixable"`. |

Checks marked "No" cannot be fixed by patching the scraper. If scraper-remediation sends one of these, the orchestrator should set `fix_outcome: "unfixable"` with a note explaining the check is outside scraper scope.

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
- **Baseline overwrite expected:** The tester in full mode saves a new baseline reflecting the patched scraper's output — the updated baseline becomes the regression reference for future retests.

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
