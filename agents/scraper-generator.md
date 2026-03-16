# Scraper Generator Agent

**Input:** Company report, catalog assessment, and SKU schema(s) for the company's subcategories
**Output:** Scraper code, config metadata, and product data contract

---

## Context

This agent generates a production-ready Python scraper that extracts structured product data from a company's catalog. The scraper must be a single self-contained file with no imports from the rest of the codebase. It reads upstream reports (company report, catalog assessment) and the SKU schema to understand what to scrape and what attributes to extract.

---

## Step 1: Load Context

Read the company report. Extract:

- **Site URL** — where to start
- **Subcategory taxonomy IDs** — what the company sells
- **Business model** — B2B, B2C, etc.

Read the catalog assessment. Extract:

- **Scraping strategy** — one of: `static_html`, `structured_data`, `pdf_pricelist`
- **Catalog structure** — categories, navigation paths, pagination patterns
- **Estimated product count** — used to verify the scraper finds a reasonable number of products
- **Catalog entry points** — where product listings begin
- **Anti-bot notes** — rate limits, headers, or request patterns to respect
- **Platform** — the CMS/e-commerce platform identified by the catalog-detector (e.g., `woocommerce`, `shopify`, `unknown`)

If no catalog assessment exists (meaning the catalog-detector has not run yet), escalate — see the `missing_catalog_assessment` decision.

---

## Step 1b: Build Category Mapping

When the company report lists multiple `Subcategories` and the catalog assessment includes URL path patterns (e.g., `/Head-Protection/` → head protection), build a mapping from URL prefixes to taxonomy IDs so the scraper can classify products at runtime without any LLM.

1. Read all `Subcategories` taxonomy IDs from the company report (e.g., `safety.head_protection`, `safety.respiratory_protection`, `electronics.sensors_instrumentation`).
2. Read URL path patterns from the catalog assessment (e.g., `/Head-Protection/`, `/Respiratory-Protection/`, `/Portable-Gas-Detection/`).
3. Map each URL path pattern to the matching taxonomy ID by matching the semantic meaning of the URL segment to the subcategory name. For example, `/Head-Protection/` maps to `safety.head_protection`, `/Respiratory-Protection/` maps to `safety.respiratory_protection`.
4. **Every discovered URL prefix MUST be mapped.** If a prefix cannot be mapped to any subcategory, escalate — see the `unmapped_url_prefix` decision. Do not silently skip unmapped prefixes.
5. Set `default_category` to the company's `Primary` taxonomy ID (used as fallback when no prefix matches).

For **single-subcategory companies**, the mapping is trivial — all products get the primary taxonomy ID. The `category_mapping` in config can be empty or contain one entry.

The generated scraper uses this mapping at runtime (no LLM involved):
- For each product, check the product URL against the category mapping prefixes.
- The first prefix found in the URL determines the product's `product_category` taxonomy ID.
- If no prefix matches, use `default_category`.

Store the mapping in `config.json` (see Step 7 for the full format):
```json
{
  "category_mapping": {
    "/Head-Protection/": "safety.head_protection",
    "/Respiratory-Protection/": "safety.respiratory_protection",
    "/Portable-Gas-Detection/": "electronics.sensors_instrumentation"
  },
  "default_category": "safety.respiratory_protection"
}
```

---

## Step 2: Load the SKU Schema

Read the SKU schema for each subcategory the company covers.

**Single-subcategory companies:** Load the one SKU schema for the company's primary subcategory.

**Multi-subcategory companies:** Load the SKU schema for EVERY subcategory listed in the company report's `Subcategories` field. Each schema defines different category-specific attributes — their names, data types, descriptions, and example values. These attributes are split into **core** and **extended** lists within each schema. The scraper uses the category mapping from Step 1b to determine which schema applies to each product, and routes attributes into the correct bucket accordingly (see Step 2a).

If no SKU schema exists for any of the company's subcategories, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision. Repeat for each missing schema before proceeding.

---

## Step 2a: Map Attributes to Schema

After loading the SKU schema(s), determine how each attribute the scraper extracts will be routed into the product record's attribute buckets.

The scraper-generator MUST:

1. Read the SKU schema for the company's subcategory (or each subcategory for multi-subcategory companies) — specifically the **core** and **extended** attribute tables.
2. For each attribute the scraper extracts, match it against the **Key** column in the schema tables (exact match).
3. Matched **core** Key → `core_attributes`
4. Matched **extended** Key → `extended_attributes`
5. No match → `extra_attributes`
6. The scraper code must use the **EXACT key values** from the schema's Key column — no inventing names, no renaming, no inferring snake_case from display names.

**Multi-subcategory attribute routing:** When a company spans multiple subcategories, each subcategory has its own SKU schema with potentially different core and extended attribute lists. The same attribute name (e.g., `weight`) might be core in one schema and extended in another, or present in one but absent from another. The scraper must:

1. Determine the product's subcategory from the URL-based category mapping (Step 1b).
2. Look up the correct SKU schema for that subcategory.
3. Route the product's attributes against THAT schema's core/extended lists — not a merged or generic list.
4. This means the attribute classification (core vs extended vs extra) may differ per product depending on which subcategory it belongs to.

**`extra_attributes` governance:**
- Keys must be `snake_case`
- Values must be primitives (`string`, `number`, `boolean`) or arrays of primitives
- No nested objects

---

## Step 3: Generate the Scraper

Before generating the scraper, read the platform knowledgebase for the platform identified in Step 1 (if it exists). The knowledgebase contains CSS selectors, JSON-LD patterns, pagination mechanisms, and common pitfalls discovered from previous scraper runs on the same platform. Use these known patterns to inform the generated code — this avoids rediscovering platform-specific quirks through trial and error.

If no knowledgebase exists for the platform (first time encountering it, or platform is `unknown` or `custom`), proceed without it.

Write a single Python file that does everything needed to scrape the company's full product catalog. The scraper must be standalone — one `.py` file using only standard library modules plus the appropriate scraping library.

### Library Selection

Choose based on the scraping strategy from the catalog assessment:

| Strategy | Libraries | When |
|----------|-----------|------|
| `static_html` | `httpx` + `selectolax` | Server-rendered HTML, no JavaScript required |
| `structured_data` | `httpx` (+ `selectolax` if HTML parsing needed alongside JSON/API) | JSON-LD, public API endpoints, product feeds. Add `selectolax` when the scraper also parses HTML for specs, breadcrumbs, or embedded script data not available in the structured source. |
| `pdf_pricelist` | `pdfplumber` | PDF price lists or catalogs |

### Required Behavior

The generated scraper must:

1. **Extract universal top-level fields for every product:**
   - `sku` — the retailer or manufacturer identifier
   - `name` — full product name
   - `url` — direct link to the product page
   - `price` — numeric price (float, no currency symbols), or `null` if unavailable
   - `currency` — ISO 4217 currency code, or `null` if unavailable
   - `brand` — the product's brand name (promoted to top-level, not inside attribute buckets)
   - `product_category` — the taxonomy ID for the product's subcategory (e.g., `machinery.power_tools`). For multi-subcategory companies, determine from the URL-based category mapping built in Step 1b. For single-subcategory companies, use the company's primary taxonomy ID.
   - `scraped_at` — ISO 8601 timestamp of when this product was extracted

2. **Extract category-specific attributes** as defined in the SKU schema and route them into the correct bucket per Step 2a. Extraction effort varies by bucket:
   - **`core_attributes`** — high effort. These define what makes a product identifiable and comparable. Actively work to find and parse these even if they require navigating tabs, parsing spec tables, or combining multiple page elements.
   - **`extended_attributes`** — moderate effort. Extract when available on the page, but do not invent complex parsing for marginal gains.
   - **`extra_attributes`** — low effort / opportunistic. Capture what is naturally available during extraction, but do not put significant effort into finding these. They serve as a feedback signal for future schema evolution.

   **Non-English sites:** When generating a scraper for a site in a non-English language, the generated Python script must map non-English attribute labels to English keys. Include a static `LABEL_MAP` dict that maps the site's attribute labels to the corresponding SKU schema Key values (e.g., `"Biezums": "thickness"`, `"Suga": "species"`). For known closed value sets (species names, material types, grade labels), include a static translation dict (e.g., `"Egle": "Spruce"`). Extra attribute keys must also be English `snake_case` — derive them from the non-English labels at code-generation time, not at runtime. Values that cannot be statically mapped pass through in the original language.

3. **Handle pagination completely** — follow all pages, not just the first. Support whichever pagination pattern the site uses (page numbers, next buttons, cursor-based, infinite scroll). Never stop at an arbitrary page limit.

4. **Build the `category_path`** for each product from the site's breadcrumb or navigation hierarchy (e.g., `"Tools > Saws > Plunge-Cut Saws"`).

5. **Produce structured product data** as a flat list of product records. Each record follows this schema:

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
     "category_path": "Products > Power Tools > Drilling > Hammer Drills"
   }
   ```

   Universal top-level fields (always present, never change): `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`.

   Category-specific attribute buckets:
   - `core_attributes` — attributes whose keys match the **Key** column in the SKU schema's Core Attributes table (high extraction effort)
   - `extended_attributes` — attributes whose keys match the **Key** column in the SKU schema's Extended Attributes table (moderate extraction effort)
   - `extra_attributes` — everything else that doesn't match any Key in either table (low effort / opportunistic)

   This is the data contract — the agent defines what the scraper produces, not how or where it is persisted. The harness provides the persistence mechanism (file format, storage destination).

6. **Deliver product data in batches through a three-phase persist hook.** The scraper never accumulates more than one batch in memory. The hook has three functions — the agent defines when they are called, the harness defines what they do:

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
   - Respect rate limits — include reasonable delays between requests (1-2 seconds default)
   - Set request timeouts (30 seconds default)

9. **Include a `main()` entry point** that accepts an optional `--limit N` argument via `argparse`. When provided, the scraper stops after extracting N products total. `--limit` must be a positive integer — argparse rejects zero or negative values. Use a custom `argparse` type function (e.g., `positive_int`) that raises `ArgumentTypeError` for values `<= 0`, rather than post-hoc `if` checks. Scraping configuration (target URL, request headers, delays) is embedded in the script. The output destination is provided by the harness. Always use `with httpx.Client(...) as client:` as a context manager — never manual `create_client()` / `client.close()` pairs, which leak connections on exceptions.

   When `--limit` is used, the scraper traverses categories normally and stops when the cumulative product count reaches N. The `limited` field in the teardown summary is `true` only when the limit was the binding constraint: `limited = (total_products >= limit)`. If the catalog is smaller than the limit, `limited` is `false`.

10. **Include a `--probe URL` argument** that accepts a single product-page URL, runs the extraction logic against it, and prints the result as formatted JSON to stdout. If extraction succeeds, the output is the full product record. If extraction fails, the output is a JSON object with `"error"` and `"details"` fields describing the failure. `--probe` skips the persist hooks entirely (no `setup`/`persist`/`teardown` calls) and exits immediately after the single extraction. `--probe` and `--limit` are mutually exclusive — argparse enforces this.

### Product Discovery Strategy

The scraper must find every product in the catalog, not just the ones visible on the first page of the most obvious categories. The catalog assessment provides primary navigation paths, but the scraper should be robust against incomplete navigation — especially on custom or unknown platforms where catalog structure may be irregular.

**Discovery sources — use multiple when available:**

1. **Sitemap-based discovery.** When the catalog assessment identifies a product sitemap, parse it for all product URLs. Sitemaps are the most comprehensive source — they often include products not reachable through category navigation (uncategorized items, recently added products, items in hidden or seasonal categories). Extract all `<loc>` entries matching the site's product URL pattern.

2. **JSON API endpoints.** Known platforms expose bulk product APIs (e.g., Shopify's `/products.json`). Custom sites may have internal APIs discovered during catalog detection. When available, these return complete product data without page-by-page crawling — use them as the primary source.

3. **Category tree traversal.** Walk every leaf category from the catalog assessment's category structure. Follow nested subcategories to their deepest level — do not stop at parent categories that also have child categories. A parent category page may show aggregated products, but child categories often contain additional products not visible on the parent. Exhaust pagination within each leaf category.

4. **"All products" or "shop" pages.** Some sites have a single collection page listing every product (with pagination). When this exists and the site is small enough, prefer it over category-by-category traversal — it guarantees no products are missed due to navigation gaps.

**Deduplication.** Products may appear in multiple categories or across different discovery sources. The scraper must never emit the same product twice. Deduplicate by product URL or SKU — maintain a set of seen identifiers and skip duplicates. When the same product appears in multiple categories, use the first occurrence's `category_path`.

**Discovery validation.** After the discovery phase completes (before or during extraction), track the total number of unique product URLs found. Compare against the catalog assessment's estimated product count:

- If discovered count is **less than 50%** of the estimate, log a warning — the discovery logic may be missing categories, failing to follow pagination, or using selectors that don't match the site.
- If discovered count is **more than 5x** the estimate, log a warning — the discovery logic may be following non-product links (blog posts, documentation pages, category index pages).

Neither case is an automatic stop — the scraper continues — but the warning provides a diagnostic signal during testing.

**Custom and unknown platform guidance.** When the platform is `custom` or `unknown`, the scraper cannot rely on platform-specific CSS classes, API conventions, or URL patterns. Apply these defensive measures:

| Concern | Approach |
|---------|----------|
| **Link discovery** | Look for product links using the URL pattern from the catalog assessment (e.g., any `<a>` whose `href` matches `/product/`, `/item/`, `/p/`). Do not depend on a specific CSS class like `.product-card` — custom sites use arbitrary class names. |
| **Navigation depth** | Follow every link in the navigation tree without assuming a fixed depth. Custom sites may nest categories 4–5 levels deep, or use flat structures with hundreds of categories at one level. |
| **Pagination variants** | Check for all common pagination mechanisms: numbered page links, "next" links, "load more" buttons (which may correspond to an AJAX endpoint discoverable in the HTML), offset/cursor parameters, and "showing X of Y" counters that reveal additional pages. |
| **Sitemap as ground truth** | When both a sitemap and category navigation are available, use the sitemap as the authoritative product URL list. Use category navigation only to build `category_path` values. This prevents missing products that exist in the sitemap but are unreachable through navigation (common on custom sites with inconsistent internal linking). |
| **Empty category detection** | Log the number of products found per category. A category yielding 0 products may indicate a selector mismatch rather than an empty category — verify by checking whether the page contains product-like content before concluding it is empty. |
| **Cross-source reconciliation** | When multiple discovery sources are used (sitemap + navigation + API), log the count from each source separately. Large discrepancies (e.g., sitemap has 200 URLs but navigation yields 50) indicate the scraper is not reaching all products through one of the sources. |

### What NOT to Include

- No imports from the rest of the codebase
- No hardcoded credentials or API keys
- No interactive prompts
- No persistence logic beyond the harness-provided hook implementations — the agent defines the hook call pattern (setup/persist/teardown), the harness defines what each hook does

### Python Code Quality

The generated scraper is production code that runs daily as a CronJob. Write it to the same standard as hand-written Python.

**Style:**
- Target Python 3.10+. Start the file with PEP 723 inline script metadata, then `from __future__ import annotations`. The metadata block declares the Python version and third-party dependencies so the script is fully self-contained — runnable with `uv run scraper.py` with no separate `pyproject.toml` or virtual environment setup:
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

## Step 4: Probe Extraction

Before running the full scraper, validate that the extraction logic works against the live site. This is a fast feedback loop — seconds per iteration, not minutes.

### Category-diverse sampling

The probe must cover the breadth of the catalog, not just one corner. Different product categories on the same site often have different page layouts, spec tables, or data availability — a selector that works for sprinklers may fail on robotic mowers.

Select probe pages from **at least 3 different top-level categories** in the catalog (as identified in the catalog assessment's category structure). Within each category, pick a product that looks representative — not the simplest or most populated one. If the catalog has fewer than 3 top-level categories, probe at least one product from every category.

### Extraction validation

For each probe page, run the scraper's `--probe` mode with that URL. Examine the JSON output to verify: universal top-level fields (`sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`) are populated (`price` and `currency` may be `null` when the catalog does not display prices), `core_attributes` and `extended_attributes` contain schema-matched keys, `extra_attributes` keys are `snake_case` with primitive values, and no extraction errors are reported. This executes the real extraction code path — do not manually simulate selectors or JSON parsing.

If extraction would fail for a given page:
1. Identify the specific issue (wrong selector, unexpected JSON-LD structure, missing field)
2. Fix the scraper code
3. Re-probe the same page to verify the fix
4. Repeat until the probe passes for all sampled products

If the same extraction issue persists after 5 probe-fix cycles, escalate — see the `probe_extraction_failed` decision.

Once the probe passes for all sampled pages (across all probed categories), proceed to the full test.

---

## Step 5: Smoke Test

Run the scraper with `--limit 20` and verify it works end-to-end. This is a fast structural check — the probe (Step 4) already validated extraction logic, so failures here are about pagination, batching, rate limiting, or persist hook issues. Keep this at 20 products for fast iteration during scraper development.

### Test timeout

The test run has a **hard time limit of 2 minutes**. A `--limit 20` scraper that takes longer than 2 minutes is broken — it is either failing silently on every product, stuck in a retry loop, or crawling categories without extracting data. If the test process exceeds 2 minutes:

1. **Kill the process immediately** — do not wait for it to finish.
2. **Read the scraper's stderr output** (the JSON log lines) to diagnose the failure. Common patterns:
   - Repeated "Failed to parse" warnings with 0 products extracted → extraction logic is broken (regex, selector, or JSON path does not match the live site)
   - Repeated HTTP errors or retries → authentication, rate limiting, or network issue
   - Processing many categories with 0 products → the scraper discovers products but fails to extract every one

   Additional failure patterns:

   | Symptom | Likely cause | Fix |
   |---------|-------------|-----|
   | HTTP 429 responses in retry logs | Rate limiting — requests too frequent | Increase `REQUEST_DELAY`, add random jitter |
   | 200 responses but empty or minimal HTML body | Geo-blocking or bot detection | Add realistic headers (Accept, Accept-Language), rotate User-Agent |
   | Redirect chains to different domain or language | Localized site redirect | Pin URL scheme, set Accept-Language, handle redirects manually |
   | Garbled product names or `json.dumps` failures | Encoding mismatch — non-UTF-8 content | Detect encoding from Content-Type or HTML meta, decode explicitly |

3. **Fix the root cause** in the scraper code, then re-run the test. The timed-out run does not count toward the retry budget — after fixing, you have one run and one retry (two attempts total) before escalating.

Do not assume the scraper is "just slow." A correctly working `--limit 20` test should complete in under 90 seconds for most sites. If it consistently exceeds 2 minutes after a fix attempt, escalate — see the `scraper_test_failed` decision.

### Test verification

The test must verify:

1. **Scraper completes without crashing** — no unhandled exceptions
2. **Summary is valid** — `total_products` is between 1 and 20, `errors_count` is 0
3. **Product records are correct** — `brand` is a top-level field (not inside attribute buckets) and `product_category` is a valid taxonomy ID. Every record must have `sku`, `name`, `url`, and `scraped_at` populated (non-null). Price and currency should be populated when the catalog displays prices — when the catalog assessment notes that prices are unavailable (e.g., international sites without pricing), null values are acceptable. At least some records should have attributes in `core_attributes` and/or `extended_attributes` matching Key values from the SKU schema.
4. **Persist hook worked** — the harness received batches and the output destination has product data
5. **Category diversity** — the extracted products span at least 2 distinct `category_path` top-level values. The probe (Step 4) validates extraction logic across at least 3 categories; this gate verifies that the scraper traverses multiple categories in a real run with pagination and batching. If all 20 products come from a single category, the test coverage is insufficient. If the catalog has only one category, this check passes automatically.

Print a few extracted products from different categories as formatted JSON for visual inspection.

If the test fails, attempt one retry — see the `scraper_test_failed` decision.

Once the smoke test passes, the scraper code is final. The harness persists it to the appropriate location. Proceed to taxonomy feedback (Step 5a) and final verification (Step 5b).

---

## Step 5a: Taxonomy Feedback

After the scraper passes the smoke test (Step 5), analyze the test output for potential schema improvements.

1. **Collect** all unique attribute keys from `extra_attributes` across all test products.
2. **Evaluate significance** — for each extra attribute, count how many products include it. If an attribute appears on >80% of test products, it is a candidate for schema addition.
3. **Check schema coverage** — verify the candidate is not already in the schema under a different name (synonym check).
4. **Trigger taxonomy update** — if there are significant candidates, request that the subcategory's SKU schema be updated to consider the candidate attributes. Pass the candidate attribute names and example values. The enrichment process evaluates whether they are genuinely significant for the subcategory (researches other companies, not just this one).
5. **Log** — report which attributes were proposed to the taxonomy. The feedback does NOT re-map the current scraper's output. Newly added attributes take effect when this or another company's scraper is regenerated in the future.

### File locking for concurrency

Before modifying any schema file, the feedback step must acquire a file lock:
- Lock file: `{schema-filename}.lock` next to the schema file in the SKU schemas directory
  - Example: `power-tools-drills-saws-sanders.md.lock`
- If the lock file exists and is less than 10 minutes old: skip the feedback step, log a warning ("Another agent is updating this schema, skipping feedback")
- If the lock file exists but is older than 10 minutes: consider it stale, delete it, and proceed (the holding agent likely crashed)
- Create the lock file before triggering schema enrichment
- Delete the lock file after the taxonomy update completes (or fails)

### When to skip

Skip this step entirely when:
- There are no attributes in `extra_attributes` across any test products
- No extra attribute appears on >80% of test products
- The scraper test failed (feedback only runs after a successful test)

---

## Step 5b: Final Verification Run

After the smoke test and taxonomy feedback, re-run the scraper with a larger, representative sample. This run produces the output that the eval-generator (Stage 4) validates against. The scraper code does not change — this is purely a re-run with a bigger limit.

### Sample size

Compute the verification sample size from the catalog assessment's estimated product count:

```
sample_size = min(ceil(expected_product_count * 0.2), 100)
```

This gives 20% of the catalog, capped at 100 products. Examples:

| Estimated products | Sample size |
|--------------------|-------------|
| 50 | 10 |
| 123 | 25 |
| 500 | 100 |
| 2,000 | 100 |

**When to skip:** If `sample_size <= 20`, the smoke test output is already sufficient — skip the final verification run entirely. The smoke test's `--limit 20` output becomes the eval input.

### Verification timeout

Scale the timeout proportionally: `max(120, sample_size * 6)` seconds. This allows ~6 seconds per product (matching the smoke test's 2-minute budget for 20 products).

### What to verify

The smoke test already validated correctness. The final verification only checks:

1. **Scraper completes without crashing** at the larger sample size
2. **`errors_count` is 0** — no new errors appear at higher volume
3. **`total_products`** is between 1 and `sample_size`

If the final verification fails, apply the same retry logic as the smoke test — one retry allowed, then escalate via the `scraper_test_failed` decision.

---

## Step 6: Write Back to Platform Knowledgebase

After a successful test, write discoveries back to the platform knowledgebase. This step only runs when the platform is an enumerated value (`woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`) — skip for `unknown` or `custom` platforms.

If the platform knowledgebase does not exist yet, create it. If it exists, append new discoveries without removing existing content.

Write to these sections:
- **JSON-LD Patterns** — the JSON-LD structure encountered on this site (e.g., `AggregateOffer` vs list of `Offer`, `priceSpecification` nesting)
- **CSS Selectors** — selectors that worked for product links, pagination, breadcrumbs, and any that differed from the knowledgebase's existing suggestions
- **Pagination** — URL patterns and mechanisms used on this site
- **Common Pitfalls** — any issues hit during the probe phase and how they were resolved
- **Sites Using This Platform** — add a row with the company name, slug, today's date, and a brief note about anything unusual

---

## Step 7: Prepare Config Metadata

Produce config metadata for the scraper:

```json
{
  "company_slug": "{slug}",
  "category": "{taxonomy_id}",
  "sku_schema": "{category-slug}",
  "scraping_strategy": "static_html",
  "expected_product_count": 1200,
  "subcategories": ["safety.head_protection", "safety.respiratory_protection", "electronics.sensors_instrumentation"],
  "category_mapping": {
    "/Head-Protection/": "safety.head_protection",
    "/Respiratory-Protection/": "safety.respiratory_protection",
    "/Portable-Gas-Detection/": "electronics.sensors_instrumentation"
  },
  "default_category": "safety.respiratory_protection",
  "generated_at": "2026-03-14T12:00:00Z"
}
```

- `category` — the primary taxonomy ID from the company report (e.g., `machinery.power_tools`)
- `sku_schema` — the slug of the SKU schema file that was used (for single-subcategory companies). For multi-subcategory companies, this is the primary subcategory's schema slug.
- `scraping_strategy` — the strategy the scraper implements
- `expected_product_count` — from the catalog assessment estimate, updated with the actual count found during testing if it is higher
- `subcategories` — list of all taxonomy IDs this scraper covers. For single-subcategory companies, this is a one-element list. Matches the `Subcategories` field from the company report.
- `category_mapping` — a dict mapping URL path prefixes to taxonomy IDs. Built in Step 1b from the catalog assessment's URL path patterns and the company report's subcategories. For single-subcategory companies, this can be empty (all products use `default_category`). For multi-subcategory companies, every URL prefix from the catalog assessment must have an entry.
- `default_category` — the company's primary taxonomy ID, used as the fallback `product_category` value when no URL prefix matches
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

## Step 8: Self-Verification

Before presenting results, verify the scraper and config against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Scraper is standalone** | Single .py file, no imports from the codebase, only allowed libraries |
| 2 | **Smoke test passed** | `--limit 20` test: products extracted successfully with all universal top-level fields populated |
| 3 | **Product data contract correct** | Flat list of product records with universal top-level fields plus three attribute buckets (`core_attributes`, `extended_attributes`, `extra_attributes`) |
| 4 | **`brand` is top-level** | `brand` appears as a top-level field in every product record, not inside any attribute bucket |
| 5 | **`product_category` is valid** | `product_category` is a valid taxonomy ID from `categories.md` |
| 6 | **`core_attributes` keys match schema** | Every key in `core_attributes` appears in the Key column of the SKU schema's Core Attributes table |
| 7 | **`extended_attributes` keys match schema** | Every key in `extended_attributes` appears in the Key column of the SKU schema's Extended Attributes table |
| 8 | **`extra_attributes` keys are governed** | Keys are `snake_case`, values are primitives (string, number, boolean) or arrays of primitives, no nested objects |
| 9 | **Pagination handled** | Scraper follows all pages, not hardcoded to first page |
| 10 | **Error handling present** | Retries, timeouts, and graceful skipping of failed products |
| 11 | **Config metadata complete** | All required fields present with correct values, including `subcategories`, `category_mapping`, and `default_category`. For multi-subcategory companies, every URL prefix from the catalog assessment appears in `category_mapping`. |
| 12 | **Logging implemented** | JSON lines to stderr with required events |
| 13 | **Code quality** | PEP 723 inline script metadata present at top of file, `from __future__ import annotations` follows, all functions typed, no bare `except:`, constants at module level, single `httpx.Client` reused |
| 14 | **Persist hook present** | setup/persist/teardown functions exist, persist is called after each batch of up to 100 records, teardown is always called |
| 15 | **Platform knowledgebase updated** | Platform knowledgebase was written or updated after a successful test (when platform is an enumerated value — not `unknown` or `custom`) |
| 16 | **Category diversity in test** | Smoke test produced products from at least 2 distinct top-level categories (or the catalog has only one category) |
| 17 | **Product discovery strategy is robust** | Scraper uses the most comprehensive discovery source available (sitemap, JSON API, or exhaustive category traversal). For `custom`/`unknown` platforms, scraper uses URL-pattern-based link discovery rather than platform-specific CSS selectors. Deduplication by URL or SKU is present. |
| 18 | **Multi-subcategory mapping correct** | For multi-subcategory companies: category mapping covers all URL prefixes from catalog assessment, scraper uses per-subcategory SKU schemas for attribute routing, and `product_category` varies correctly across products from different sections. For single-subcategory companies: all products use the primary taxonomy ID. |
| 19 | **Final verification passed** | Final verification run (Step 5b) completed with 0 errors, or was correctly skipped because `sample_size <= 20`. The output from the final verification (or the smoke test if skipped) is ready for eval. |

If all 19 pass, the scraper is complete.

---

## Boundaries

- This agent generates scrapers only — it does not assess catalog scrapability (catalog-detector) or generate quality validation (eval-generator).
- It does not define or modify the product taxonomy or SKU schemas.
- It does not run the scraper in production — it only performs a dry-run test during generation.

---

## Decisions

### Decision: missing_catalog_assessment

**Context:** No catalog assessment exists for this company — the catalog-detector stage has not run yet. The scraper cannot be generated without knowing the site structure and scraping strategy.
**Autonomous resolution:** Never. The catalog assessment is a required input.
**Escalate when:** Always. Report that the catalog assessment is missing and suggest running the catalog-detector first.
**Escalation payload:** Company slug, path where the catalog assessment was expected.

### Decision: unmapped_url_prefix

**Context:** A URL path pattern from the catalog assessment cannot be mapped to any subcategory in the company report's `Subcategories` list. This means the catalog contains a product section that does not correspond to any known classification for this company.
**Autonomous resolution:** Never. Every URL prefix must map to a taxonomy ID — silently skipping prefixes would cause products in that section to be misclassified under the default category.
**Escalate when:** Always. Report the unmapped prefix, the full list of subcategories from the company report, and all URL patterns from the catalog assessment.
**Escalation payload:** Company slug, the unmapped URL prefix, the list of subcategories, all URL patterns from the catalog assessment.

### Decision: no_sku_schema

**Context:** No SKU schema file exists for the company's product category.
**Autonomous resolution:** Verify that the subcategory from the company report exists in the product taxonomy categories file. If it does, the schema simply hasn't been created yet — trigger SKU schema generation for that subcategory. Once the schema is available, return to Step 2 and continue.
**Escalate when:** The subcategory from the company report does not appear in the product taxonomy categories file. This indicates a taxonomy integrity issue that must be resolved before the pipeline can continue.
**Escalation payload:** Company slug, the taxonomy ID from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: probe_extraction_failed

**Context:** The probe found that the scraper's extraction logic does not work against the actual product pages — selectors don't match, JSON-LD structure is unexpected, or universal attributes cannot be extracted.
**Autonomous resolution:** Fix the scraper code and re-probe. Repeat up to 5 times per issue.
**Escalate when:** The same extraction issue persists after 5 probe-fix cycles. The site structure may be incompatible with the agent's extraction capabilities.
**Escalation payload:** Company slug, the specific extraction failure, what was tried, sample HTML from the problematic page.

### Decision: scraper_test_failed

**Context:** The scraper failed during the smoke test (`--limit 20`) or the final verification run — it crashed, produced no output, found far fewer products than expected, or had widespread missing data. The probe passed, so this is a structural issue (pagination, rate limiting, batching), not an extraction issue.
**Autonomous resolution:** Retry once. Analyze the error, adjust the scraper, and test again.
**Escalate when:** The scraper fails a second time after adjustment.
**Escalation payload:** Company slug, error details or partial results, what was tried in the retry, the scraping strategy that was used.
