# Code Generator Reference

This reference defines the canonical product record format, library selection, required behavior, and code quality rules for generated scrapers. The orchestrator reads this inline during Step 2c — it is not dispatched as a sub-agent.

## Inputs

The orchestrator provides the following when generating scraper code:

| Input | What it contains |
|-------|-----------------|
| Scraping strategy | One of `static_html`, `structured_data`, `pdf_pricelist` — from the catalog assessment |
| Catalog structure | Categories, navigation paths, pagination patterns, entry points, anti-bot notes |
| Estimated product count | Used to validate discovery completeness |
| Platform | CMS/e-commerce platform (e.g., `woocommerce`, `shopify`, `unknown`, `custom`) |
| Platform knowledgebase | CSS selectors, JSON-LD patterns, pagination mechanisms, pitfalls from prior runs on the same platform (if available) |
| SKU schema(s) | Core and extended attribute tables for each subcategory the company covers |
| Attribute routing tables | Core/extended/extra routing per subcategory, built before this step |
| LABEL_MAP + CATEGORY_ALIASES | Non-English sites only — source-language labels mapped to English schema Keys |
| Category mapping | URL prefix → taxonomy ID mapping for multi-subcategory companies |
| Default category | The company's primary taxonomy ID, used as fallback |
| Persist hook implementations | `setup`, `persist`, `teardown` function bodies provided by the harness |

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

The generated scraper must:

1. **Extract universal top-level fields for every product:**
   - `sku` — the retailer or manufacturer identifier
   - `name` — full product name
   - `url` — direct link to the product page
   - `price` — numeric price (float, no currency symbols), or `null` if unavailable
   - `currency` — ISO 4217 currency code, or `null` if unavailable
   - `brand` — the product's brand name (promoted to top-level, not inside attribute buckets)
   - `product_category` — the taxonomy ID. For multi-subcategory companies, determine from the URL-based category mapping. For single-subcategory companies, use the company's primary taxonomy ID.
   - `scraped_at` — ISO 8601 timestamp of when this product was extracted

2. **Extract category-specific attributes** using the routing tables from the attribute mapping step. Route each attribute into the correct bucket per the Product Record Format above. For unit extraction: when the SKU schema's `Unit` column is not `—`, extract the unit from the source site and include it in `attribute_units`. Units are site-derived — no conversions. When the site does not explicitly state a unit, infer from context (e.g., regional conventions) and embed as a static value in the generated code. When units vary per product within the same site, use per-product extraction logic.

3. **Handle pagination completely** — follow all pages, not just the first. Support whichever pagination pattern the site uses (page numbers, next buttons, cursor-based, infinite scroll). Never stop at an arbitrary page limit.

4. **Build the `category_path`** for each product from the site's breadcrumb or navigation hierarchy (e.g., `"Tools > Saws > Plunge-Cut Saws"`).

5. **Produce structured product records** conforming to the Product Record Format section above. Universal top-level fields are always present. Attribute bucket keys use the exact Key values from the SKU schema — no inventing names, no renaming, no inferring snake_case from display names.

6. **Deliver product data in batches through a three-phase persist hook.** The scraper never accumulates more than one batch in memory. The hook has three functions — the scraper defines when they are called, the harness defines what they do:

   - `setup()` — called once before scraping begins. Returns a context object (e.g., file handle, DB connection) that `persist` and `teardown` receive.
   - `persist(records, context)` — called after each batch of up to 100 product records. Hands the batch to the harness for storage.
   - `teardown(context, summary)` — called once after scraping completes, even if the scraper exits early due to `--limit`. `summary` is a dict with: `total_products` (int), `batches_written` (int), `duration_seconds` (float), `errors_count` (int), `limited` (bool), `timestamp` (ISO 8601 string).

   Batch size is 100 records. The last batch may be smaller. The scraper must call `teardown()` in all cases — normal completion, `--limit` reached, or graceful error exit.

7. **Log structured output** using JSON lines to stderr. Each log line must include a `level` (`info`, `warning`, `error`), a `message`, and a `timestamp`. Key events to log:
   - Scraper start (with target URL and strategy)
   - Each page or section processed (with product count)
   - Errors and retries (with details)
   - Final summary (total products found, total time)

8. **Handle errors gracefully:**
   - Retry failed HTTP requests up to 3 times with exponential backoff
   - Skip individual products that fail to parse rather than aborting the entire run
   - Log warnings for missing optional attributes, errors for missing universal attributes
   - Respect rate limits — include reasonable delays between requests (1–2 seconds default)
   - Set request timeouts (30 seconds default)

9. **Include a `main()` entry point** that accepts an optional `--limit N` argument via `argparse`. When provided, the scraper stops after extracting N products total. Use a custom `argparse` type function (e.g., `positive_int`) that raises `ArgumentTypeError` for values `<= 0` — do not use post-hoc `if` checks. Scraping configuration (target URL, request headers, delays) is embedded in the script. Always use `with httpx.Client(...) as client:` as a context manager — never manual `create_client()` / `client.close()` pairs.

   When `--limit` is used, the scraper traverses categories normally and stops when the cumulative product count reaches N. The `limited` field in the teardown summary is `true` only when the limit was the binding constraint: `limited = (total_products >= limit)`. If the catalog is smaller than the limit, `limited` is `false`.

10. **Include a `--probe URL` argument** that accepts a single product-page URL, runs the extraction logic against it, and prints the result as formatted JSON to stdout. If extraction succeeds, the output is the full product record. If extraction fails, the output is a JSON object with `"error"` and `"details"` fields. `--probe` skips the persist hooks entirely (no `setup`/`persist`/`teardown` calls) and exits immediately after the single extraction. `--probe` and `--limit` are mutually exclusive — argparse enforces this.

---

## Product Discovery Strategy

The scraper must find every product in the catalog, not just the ones visible on the first page of the most obvious categories. The catalog assessment provides primary navigation paths, but the scraper should be robust against incomplete navigation — especially on custom or unknown platforms where catalog structure may be irregular.

**Discovery sources — use multiple when available:**

1. **Sitemap-based discovery.** When the catalog assessment identifies a product sitemap, parse it for all product URLs. Sitemaps are the most comprehensive source — they often include products not reachable through category navigation. Extract all `<loc>` entries matching the site's product URL pattern.

2. **JSON API endpoints.** Known platforms expose bulk product APIs (e.g., Shopify's `/products.json`). When available, these return complete product data without page-by-page crawling — use them as the primary source.

3. **Category tree traversal.** Walk every leaf category from the catalog assessment's category structure. Follow nested subcategories to their deepest level — do not stop at parent categories. A parent category page may show aggregated products, but child categories often contain additional products. Exhaust pagination within each leaf category.

4. **"All products" or "shop" pages.** When a single collection page lists every product (with pagination), prefer it over category-by-category traversal — it guarantees no products are missed due to navigation gaps.

**Deduplication.** Products may appear in multiple categories or across different discovery sources. Deduplicate by product URL or SKU — maintain a set of seen identifiers and skip duplicates. When the same product appears in multiple categories, use the first occurrence's `category_path`.

**Discovery validation.** Compare unique product URLs found against the catalog assessment's estimate. Log a warning if discovered count is <50% (missing categories or pagination) or >5x (following non-product links). Neither is an automatic stop.

**Custom and unknown platform guidance.** When the platform is `custom` or `unknown`:
- Use URL patterns from the catalog assessment for link discovery — do not depend on platform-specific CSS classes.
- Follow the navigation tree to any depth. Check all pagination mechanisms (page numbers, "next" links, AJAX endpoints, offset/cursor params).
- When both a sitemap and category navigation exist, use the sitemap as the authoritative product URL list. Use navigation only for `category_path`.
- Log products found per category and per discovery source. Flag 0-product categories (possible selector mismatch) and source count discrepancies.

---

## Python Code Quality

The generated scraper is production code that runs daily as a CronJob. Write it to the same standard as hand-written Python.

**File structure:** Start with PEP 723 inline script metadata, then `from __future__ import annotations`. This makes the script fully self-contained:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
```

List the exact libraries chosen in the Library Selection step.

**Style:**
- Target Python 3.10+.
- Use expressive names and small focused functions — favor readability over inline comments.
- Define constants at module level for magic values: URLs, delays, selectors, CSS class names.

**Imports:**
- Organize in standard order: standard library, third-party, local.
- No unused imports. Consolidate related imports (`from x import a, b`).

**Type hints:**
- Type all function signatures (parameters and return types).
- Use PEP 604 syntax: `str | None` not `Optional[str]`, `list[str]` not `List[str]`.

**Error handling:**
- Never use bare `except:` or broad `except Exception` — catch specific exception types.
- When catching exceptions, always log context (URL, product ID, what was being attempted).

**HTTP discipline:**
- Validate responses: check status codes before parsing.
- Reuse a single `httpx.Client` instance throughout the scraper rather than creating new connections per request.

**Data hygiene:**
- Use `pathlib.Path` for file paths, not strings.
- Filter None values from product attribute dicts before output: `{k: v for k, v in d.items() if v is not None}`. Use `is not None` rather than truthiness to preserve valid falsy values like `0` and `False`.

---

## What NOT to Include

- No imports from outside the script's declared dependencies
- No hardcoded credentials or API keys
- No interactive prompts
- No persistence logic beyond the harness-provided hook implementations — the scraper defines the hook call pattern (`setup`/`persist`/`teardown`), the harness defines what each hook does

---

## Expected Output

A single standalone Python file containing:
- PEP 723 inline script metadata with declared dependencies
- The scraper implementation following all Required Behavior rules above
- The persist hook implementations (`setup`, `persist`, `teardown`) as provided by the harness
- A `main()` entry point with `--limit` and `--probe` arguments
