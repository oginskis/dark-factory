# Coder Sub-Agent

**Input:** Mode (generate/fix), catalog assessment, routing tables, category mapping, SKU schemas, platform knowledgebase; fix mode adds test_report.json + existing scraper.py
**Output:** A single standalone `scraper.py` written to the company's scraper-generator directory

---

## Input Contract

| Field | Type | Description |
|---|---|---|
| `mode` | enum | `"generate"` (no scraper exists) or `"fix"` (patch existing scraper per test report) |
| `catalog_assessment` | file | Extraction blueprint: CSS selectors, pagination patterns, anti-bot notes |
| `routing_tables_path` | path | `generator_input.json` — core/extended/extra attribute routing per subcategory. Contains pre-processed core/extended/extra attribute routing, types, and units per subcategory (replaces raw SKU schemas). |
| `category_mapping` | object | URL prefix to taxonomy ID mapping (multi-subcategory companies) |
| `platform_knowledgebase` | file | Platform-specific selectors, JSON-LD patterns, pagination mechanisms, pitfalls |
| `LABEL_MAP` + `CATEGORY_ALIASES` | dicts | Non-English sites only — source-language labels mapped to English schema Keys |
| `scraper_output_path` | path | Path where the coder writes `scraper.py` |
| `test_report_path` | path | (fix mode only) Path to `test_report.json` — issues list, rule results, sample URLs, sample values |
| `existing_scraper_path` | path | (fix mode only) Path to current `scraper.py` to patch |

Persist hooks are built into this reference (see Persist Hook Implementations section below) — not passed as input.

---

## Output Contract

Write a single standalone `scraper.py` to disk containing PEP 723 metadata, the scraper implementation, persist hook implementations, and a `main()` entry point with `--limit`, `--probe`, `--categories`, and `--append` arguments.

---

## Modes

### Generate mode

Write scraper.py from scratch using the full context package.

### Fix mode

Receives everything from generate mode plus test report and existing scraper.

**Fix mode rules:**
- **Never rewrite the entire scraper.** Apply targeted patches only to functions, selectors, or logic the test report identifies as broken.
- **Read `passing_categories` first.** Do not modify extraction logic that would affect passing categories — avoid regressions.
- **Address issues by severity** — errors before warnings.

---

## Product Record Format

This is the canonical definition of the product record. Every product the scraper emits must conform to this structure.

| Level | What it contains | Extraction effort | Source |
|-------|-----------------|-------------------|--------|
| **Universal top-level fields** | `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path` | Always extract — mandatory for every product regardless of category. Never change across taxonomy updates. | Hardcoded in scraper |
| **`core_attributes`** | Attributes matching the **Key** column in the SKU schema's Core Attributes table | **High effort** — actively work to extract these even if they require navigating tabs, parsing spec tables, or combining multiple page elements. Target: >80% fill rate. | SKU schema |
| **`extended_attributes`** | Attributes matching the **Key** column in the SKU schema's Extended Attributes table | **Moderate effort** — extract when available on the page, but do not invent complex parsing for marginal gains. Target: >50% fill rate. | SKU schema |
| **`extra_attributes`** | Everything else that doesn't match any Key in core or extended | **Low effort / opportunistic** — capture what is naturally available during extraction. Serves as a feedback signal for future schema evolution. Keys must be `snake_case`, values must be primitives. | Discovered at runtime |
| **`attribute_units`** | Maps attribute keys (from any bucket) to their unit of measure string as found on the source site. Only includes attributes with physical units. | Extract when the SKU schema's `Unit` column is not `—`. For `extra_attributes`, include when the site makes the unit unambiguous. | SKU schema `Unit` column + site content |

Additional rules:
- `brand` is a universal top-level field — never place it inside an attribute bucket
- `product_category` is the taxonomy ID (e.g., `machinery.power_tools`)
- `attribute_units` keys must exactly match keys in `core_attributes`, `extended_attributes`, or `extra_attributes`. Values are site-derived — pass through what the site shows, no unit conversions.

### Example record

```json
{
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
  "attribute_units": {
    "voltage": "V",
    "tool_weight": "lb",
    "chuck_size": "mm",
    "max_torque": "N m"
  },
  "category_path": "Products > Power Tools > Drilling > Hammer Drills"
}
```

This is the data contract — the scraper defines what it produces, not how or where it is persisted. The harness provides the persistence mechanism.

---

## Language Rules for Non-English Sites

| Level | Keys | Values |
|-------|------|--------|
| **Universal top-level** | English (fixed) | `name` may remain in the original language. Other values in English where a static mapping is feasible. |
| **`core_attributes`** | English only — must match SKU schema Key column exactly | Map to English via static translation dicts for known value sets (species, materials, grades). Values without a mapping pass through in original language. |
| **`extended_attributes`** | English only — must match SKU schema Key column exactly | Same as core — static mapping where feasible, pass-through otherwise. |
| **`extra_attributes`** | English `snake_case` — derived from non-English labels at code-generation time | Values may remain in the original language. No translation required. |

The scraper handles this via static `LABEL_MAP` and value translation dicts — not runtime AI translation. Include the `LABEL_MAP` and `CATEGORY_ALIASES` dicts built during label discovery. Include static translation dicts for known closed value sets (species names, material types, grade labels — e.g., `"Egle": "Spruce"`). Extra attribute keys must be English `snake_case` derived from non-English labels at code-generation time, not at runtime.

---

## Library Selection

Choose based on the scraping strategy from the catalog assessment:

| Strategy | Libraries | When |
|----------|-----------|------|
| `static_html` | `httpx` + `selectolax` | Server-rendered HTML, no JavaScript required |
| `structured_data` | `httpx` (+ `selectolax` if HTML parsing needed alongside JSON/API) | JSON-LD, public API endpoints, product feeds. Add `selectolax` when the scraper also parses HTML for specs, breadcrumbs, or embedded script data not available in the structured source. |
| `pdf_pricelist` | `pdfplumber` | PDF price lists or catalogs |

---

## Required Behavior

1. **Extract universal top-level fields** for every product: `sku`, `name`, `url`, `price` (float or null), `currency` (ISO 4217 or null), `brand` (top-level, never in attribute buckets), `product_category` (taxonomy ID — from URL-based category mapping for multi-subcategory, primary ID for single), `scraped_at` (ISO 8601).

2. **Extract category-specific attributes** per routing tables. Route into correct bucket per Product Record Format. For units: extract from site when SKU schema `Unit` column is not `—`, include in `attribute_units`. No unit conversions. Infer from regional context when site omits units; use per-product logic when units vary.

3. **Handle pagination completely** — follow all pages using whatever pattern the site uses. Never stop at an arbitrary limit.

4. **Build `category_path`** from the site's breadcrumb or navigation hierarchy.

5. **Produce structured records** conforming to Product Record Format. Attribute keys must exactly match SKU schema Key values — no inventing or renaming.

6. **Three-phase persist hook** — never accumulate more than one batch in memory:
   - `setup()` — once before scraping, returns context object.
   - `persist(records, context)` — after each batch of up to 100 records.
   - `teardown(context, summary)` — always called (normal exit, `--limit`, or error). Summary dict: `total_products`, `batches_written`, `duration_seconds`, `errors_count`, `limited` (bool), `timestamp`.

7. **Structured logging** via JSON lines to stderr. Every log line must have `level` (`info`, `warning`, `error`), `message`, and `timestamp`. Log these events:
   - Scraper start (target URL, strategy)
   - Each page/section processed (category, page number, product count)
   - **Every HTTP request:** URL, status code, latency in ms. Example: `{"level": "info", "message": "GET 200 in 342ms", "url": "https://...", "status": 200, "latency_ms": 342, "timestamp": "..."}`
   - **HTTP errors (4xx, 5xx):** log at `warning` level — URL, status code, response body snippet (first 200 chars), retry attempt. Example: `{"level": "warning", "message": "GET 429 in 89ms — retry 1/3", "url": "https://...", "status": 429, "latency_ms": 89, "retry": 1, "timestamp": "..."}`
   - Backoff events (delay applied, reason)
   - Parse errors (URL, what failed, why)
   - Final summary (total products, total time, total requests, error count)

8. **Error handling with adaptive backoff:**
   - **NEVER add fixed delays.** No `time.sleep()` in normal path, no `REQUEST_DELAY`, no `Crawl-delay`. Fire requests as fast as the server responds. Non-negotiable.
   - **Backoff on errors only:** HTTP 429/500/502/503/504 triggers exponential backoff (2s → 4s → 8s → 16s cap). Reset after 5 consecutive successes. Implement as a stateful throttle class.
   - Retry failed requests up to 3 times. Skip unparseable products instead of aborting. Log warnings for optional, errors for universal attributes. 30s request timeout.

9. **`main()` entry point** with `argparse`. Use custom type function (e.g., `positive_int`) raising `ArgumentTypeError` for values <= 0. Use `with httpx.Client(...) as client:` context manager.

   **CLI flags:**
   - `--limit N` — stop after N products. `limited = (total_products >= limit)`.
   - `--probe URL` — extract single product, print JSON to stdout. Skips persist hooks. Exclusive with all other flags (argparse-enforced).
   - `--categories LIST` — comma-separated URL prefixes. Filters discovered leaf categories to matching prefixes (e.g., `/tools/drills` matches `/tools/drills/hammer-drills`). Skipped categories get no requests. Log matched vs total count. Combines with `--limit`.
   - `--append` — skip `setup()` truncation, append to existing `products.jsonl`. Combines with `--categories` and/or `--limit`.

---

## Validation Checklist

The scraper output will be validated against these rules. Code must pass all of them.

### Structural rules

| Rule | Pass criteria |
|------|---------------|
| S01 | ≥ 30% of products have non-empty `core_attributes` (at least one non-null value). Per-category breakdown — every top-level category must meet the threshold. |
| S02 | ≥ 20% of products have non-empty `extended_attributes`. Warning only. |
| S03 | 100% of products have all top-level fields: `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path`. All non-null except `price`/`currency` (may be null if catalog has no prices). |
| S04 | 100% of products have a `product_category` value that exists in `categories.md`. |
| S05 | `brand` is a top-level field in every product. Never inside `core_attributes`, `extended_attributes`, or `extra_attributes`. |
| S06 | ≥ 2 distinct top-level `category_path` values across products (auto-passes for single-category catalogs). |
| S07 | `errors_count` in `summary.json` is 0. |
| S08 | Scraper exits with code 0 (no crash). |
| S09 | `products.jsonl` exists and is non-empty after the run. |

### Semantic rules

| Rule | Pass criteria |
|------|---------------|
| M01 | For attributes typed `number` in the routing tables AND listed in `units`: the value must be numeric (`int`/`float`), and `attribute_units` must contain the key. **Wrong:** `"nominal_width": "18mm"`. **Right:** `"nominal_width": 18` + `"attribute_units": {"nominal_width": "mm"}`. |
| M02 | All attributes typed `number` in routing tables must be `int`/`float`, not strings. Warning only. |
| M03 | When the routing table `units` dict has an entry for an attribute and the product has that attribute, `attribute_units` must contain the key. Warning only. |
| M04 | Regex `\d+\s*(mm|cm|m|kg|g|lb|oz|ml|l|V|W|A|Hz|kW|MPa)$` must NOT match any value in attributes typed `number` or listed in `units`. Catches embedded units like `"18mm"`. |

### Key takeaway

**Always separate values from units.** Parse `"18mm"` into `value=18` + `attribute_units={"attr": "mm"}`. This is the most common validation failure.

---

## Product Discovery Strategy

Find every product in the catalog, not just the first page of obvious categories. Use multiple discovery sources when available:

1. **Sitemap-based discovery.** Parse product sitemaps for all `<loc>` entries matching the site's product URL pattern. Most comprehensive source — includes products unreachable via navigation.
2. **JSON API endpoints.** Platform bulk APIs (e.g., Shopify `/products.json`) return complete data without page-by-page crawling — use as primary source when available.
3. **Category tree traversal.** Walk every leaf category to its deepest level. Exhaust pagination within each leaf.
4. **"All products" pages.** When a single paginated collection lists everything, prefer it over category-by-category traversal.

**Category page validation.** Before extracting URLs, verify the page is a real category listing, not a search results redirect (common on Magento). Check for `catalogsearch/result` in URL or "Search results for:" in HTML. Log a warning and skip search result pages.

**Product URL filtering.** Use the catalog assessment's verified URL patterns and platform-specific selectors to distinguish product links from navigation/banner/footer links. Exclude static pages and promoted links appearing across unrelated categories.

**Deduplication.** Deduplicate by URL or SKU. Use the first occurrence's `category_path`.

**Discovery validation.** Log a warning if discovered count is <50% or >5x the catalog assessment's estimate.

**Custom/unknown platforms:** Use catalog assessment URL patterns (not platform CSS classes). Follow navigation to any depth. When both sitemap and navigation exist, use sitemap as authoritative URL list, navigation only for `category_path`. Log per-category and per-source counts; flag 0-product categories.

---

## Python Code Quality

Production code running daily as a CronJob — same standard as hand-written Python.

**File structure:** PEP 723 inline script metadata first, then `from __future__ import annotations`:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
```

**Rules:**
- Python 3.10+. PEP 604 types (`str | None`, `list[str]`). Type all function signatures.
- Expressive names, small focused functions, module-level constants for magic values.
- Standard import order (stdlib, third-party, local). No unused imports.
- Never bare `except:` or broad `except Exception` — catch specific types, always log context.
- Reuse a single `httpx.Client` instance. Validate status codes before parsing.
- `pathlib.Path` for file paths. Filter None values with `is not None` (preserves `0`, `False`).

---

## Persist Hook Implementations (NDJSON on Disk)

Current backend: **NDJSON files on disk**.

Include these functions in the generated scraper:

```python
BATCH_SIZE = 100
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

def setup(*, append: bool = False) -> Path:
    """Prepare output destination. Clear previous run unless appending."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "products.jsonl"
    if not append:
        output_file.write_text("")  # Truncate previous run
    return output_file

def persist(records: list[dict], output_file: Path) -> None:
    """Append a batch of product records as NDJSON."""
    with open(output_file, "a") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

def teardown(output_file: Path, summary: dict) -> None:
    """Write run summary alongside the product data."""
    summary_path = output_file.parent / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
```

The `setup()` function accepts an `append` keyword argument. When `--append` is passed on the command line, `main()` calls `setup(append=True)`, which skips the `output_file.write_text("")` truncation and preserves the existing `products.jsonl` content. When `--append` is not passed, `setup()` truncates as usual to ensure a clean run.

**Output format:** NDJSON (one JSON object per line). Append-friendly, crash-safe (completed batches survive mid-run failures), and memory-efficient to read.

To switch to a different backend (PostgreSQL, MongoDB), replace the hook implementations in this section — the scraper's scraping logic and data contract remain unchanged.

---

## What NOT to Include

- No imports from outside the script's declared dependencies
- No hardcoded credentials or API keys
- No interactive prompts
- No persistence logic beyond the harness-provided hook implementations
