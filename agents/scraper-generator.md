# Scraper Generator Agent

**Input:** Company report, catalog assessment, and SKU schema for the company's category
**Output:** Scraper code, config metadata, and product data contract

---

## Context

This agent generates a production-ready Python scraper that extracts structured product data from a company's catalog. The scraper must be a single self-contained file with no imports from the rest of the codebase. It reads upstream reports (company report, catalog assessment) and the SKU schema to understand what to scrape and what attributes to extract.

---

## Step 1: Load Context

Read the company report. Extract:

- **Site URL** — where to start
- **Primary and secondary classifications** — what the company sells
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

## Step 2: Load the SKU Schema

Read the SKU schema for the company's product category.

The schema defines category-specific attributes — their names, data types, descriptions, and example values. These attributes go into the `attributes` object of each product record, alongside the six universal attributes that every scraper must extract.

If no SKU schema exists for the company's category, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision.

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
| `structured_data` | `httpx` | JSON-LD, public API endpoints, product feeds |
| `pdf_pricelist` | `pdfplumber` | PDF price lists or catalogs |

### Required Behavior

The generated scraper must:

1. **Extract universal attributes for every product:**
   - `sku` — the retailer or manufacturer identifier
   - `name` — full product name
   - `url` — direct link to the product page
   - `price` — numeric price (float, no currency symbols)
   - `currency` — ISO 4217 currency code
   - `scraped_at` — ISO 8601 timestamp of when this product was extracted

2. **Extract category-specific attributes** as defined in the SKU schema. Map site elements to schema attributes using the descriptions and example values in the schema as guidance. Not every attribute will be present on every site — extract what is available, skip what is not.

3. **Handle pagination completely** — follow all pages, not just the first. Support whichever pagination pattern the site uses (page numbers, next buttons, cursor-based, infinite scroll). Never stop at an arbitrary page limit.

4. **Build the `category_path`** for each product from the site's breadcrumb or navigation hierarchy (e.g., `"Tools > Saws > Plunge-Cut Saws"`).

5. **Produce structured product data** as a flat list of product records. Each record follows this schema:

   ```json
   {
     "sku": "871WAR1926F",
     "name": "8 oz. Frozen Coulotte Steak - 20/Case",
     "url": "https://example.com/product/871WAR1926F",
     "price": 224.99,
     "currency": "USD",
     "scraped_at": "2026-03-15T12:34:56Z",
     "attributes": {
       "brand": "Warrington Farm Meats",
       "protein_type": "Beef",
       "cut_form": "Steak",
       "storage_type": "Frozen",
       "net_weight": 8,
       "net_weight_uom": "oz",
       "case_pack_size": 20
     },
     "category_path": "Meat & Seafood > Beef > Steaks"
   }
   ```

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

9. **Include a `main()` entry point** that accepts an optional `--limit N` argument via `argparse`. When provided, the scraper stops after extracting N products total. `--limit` must be a positive integer — argparse rejects zero or negative values. Scraping configuration (target URL, request headers, delays) is embedded in the script. The output destination is provided by the harness.

   When `--limit` is used, the scraper traverses categories normally and stops when the cumulative product count reaches N. The `limited` field in the teardown summary is `true` only when the limit was the binding constraint: `limited = (total_products >= limit)`. If the catalog is smaller than the limit, `limited` is `false`.

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
- Filter empty/None values from product attribute dicts before output: `{k: v for k, v in d.items() if v}`.

---

## Step 4: Probe Extraction

Before running the full scraper, validate that the extraction logic works against the live site. This is a fast feedback loop — seconds per iteration, not minutes.

### Category-diverse sampling

The probe must cover the breadth of the catalog, not just one corner. Different product categories on the same site often have different page layouts, spec tables, or data availability — a selector that works for sprinklers may fail on robotic mowers.

Select probe pages from **at least 3 different top-level categories** in the catalog (as identified in the catalog assessment's category structure). Within each category, pick a product that looks representative — not the simplest or most populated one. If the catalog has fewer than 3 top-level categories, probe at least one product from every category.

### Extraction validation

For each probe page, fetch it using web fetch capabilities (not by running the scraper script) and apply the extraction logic from the generated scraper: check whether the CSS selectors match, whether JSON-LD parses correctly, whether universal attributes (sku, name, url, price, currency) can be extracted, and whether category-specific attributes are found.

If extraction would fail for a given page:
1. Identify the specific issue (wrong selector, unexpected JSON-LD structure, missing field)
2. Fix the scraper code
3. Re-probe the same page to verify the fix
4. Repeat until the probe passes for all sampled products

If the same extraction issue persists after 5 probe-fix cycles, escalate — see the `probe_extraction_failed` decision.

Once the probe passes for all sampled pages (across all probed categories), proceed to the full test.

---

## Step 5: Test the Scraper (Full Verification)

Run the scraper with `--limit 20` and verify it works end-to-end. The probe (Step 4) already validated extraction logic, so failures at this stage are structural — pagination, batching, rate limiting, or persist hook issues.

The test must verify:

1. **Scraper completes without crashing** — no unhandled exceptions
2. **Summary is valid** — `total_products` is between 1 and 20, `errors_count` is 0
3. **Product records are correct** — at least some records have all 6 universal attributes populated (sku, name, url, price, currency, scraped_at) and at least some category-specific attributes in the `attributes` object
4. **Persist hook worked** — the harness received batches and the output destination has product data
5. **Category diversity** — the extracted products span at least 2 distinct `category_path` top-level values. The probe (Step 4) validates extraction logic across at least 3 categories; this gate verifies that the scraper traverses multiple categories in a real run with pagination and batching. If all 20 products come from a single category, the test coverage is insufficient. If the catalog has only one category, this check passes automatically.

Print a few extracted products from different categories as formatted JSON for visual inspection.

If the test fails, attempt one retry — see the `scraper_test_failed` decision.

Once the test passes, the scraper code is final. The harness persists it to the appropriate location.

---

## Step 6: Write Back to Platform Knowledgebase

After a successful test, write discoveries back to the platform knowledgebase. This step only runs when the platform is an enumerated value (`woocommerce`, `shopify`, `magento`, `prestashop`) — skip for `unknown` or `custom` platforms.

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
  "category": "{Category > Subcategory}",
  "sku_schema": "{category-slug}",
  "scraping_strategy": "static_html",
  "expected_product_count": 1200,
  "generated_at": "2026-03-14T12:00:00Z"
}
```

- `category` — the exact classification from the company report
- `sku_schema` — the slug of the SKU schema file that was used
- `scraping_strategy` — the strategy the scraper implements
- `expected_product_count` — from the catalog assessment estimate, updated with the actual count found during testing if it is higher
- `generated_at` — ISO 8601 timestamp of when the scraper was generated

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Product data is a flat list of records** | One record per product, all at same level | Nested grouping by category, hierarchical structures |
| **Price is a float, no currency symbols** | `224.99` | `"$224.99"`, `"224.99"`, `"USD 224.99"` |
| **Currency is ISO 4217** | `"USD"`, `"EUR"`, `"GBP"` | `"$"`, `"dollars"`, `"us"` |
| **SKU is a string** | `"871WAR1926F"` | `871` (numeric), `null` |
| **Category-specific attributes go in `attributes` object** | `"attributes": {"brand": "..."}` | Flat at product root level |
| **`category_path` uses ` > ` separator** | `"Tools > Saws > Plunge-Cut Saws"` | `"Tools / Saws"`, `"Tools>Saws"` (no spaces) |
| **Config metadata matches schema** | All fields present with correct types | Missing fields, wrong types |

---

## Step 8: Self-Verification

Before presenting results, verify the scraper and config against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Scraper is standalone** | Single .py file, no imports from the codebase, only allowed libraries |
| 2 | **Dry-run test passed** | Products extracted successfully with all 6 universal attributes populated |
| 3 | **Product data contract correct** | Flat list of product records with all required fields per the schema |
| 4 | **Pagination handled** | Scraper follows all pages, not hardcoded to first page |
| 5 | **Error handling present** | Retries, timeouts, and graceful skipping of failed products |
| 6 | **Config metadata complete** | All required fields present with correct values |
| 7 | **Logging implemented** | JSON lines to stderr with required events |
| 8 | **Code quality** | PEP 723 inline script metadata present at top of file, `from __future__ import annotations` follows, all functions typed, no bare `except:`, constants at module level, single `httpx.Client` reused |
| 9 | **Persist hook present** | setup/persist/teardown functions exist, persist is called after each batch of up to 100 records, teardown is always called |
| 10 | **Platform knowledgebase updated** | Platform knowledgebase was written or updated after a successful test (when platform is an enumerated value — not `unknown` or `custom`) |
| 11 | **Category diversity in test** | Dry-run test produced products from at least 2 distinct top-level categories (or the catalog has only one category) |

If all 11 pass, the scraper is complete.

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

### Decision: no_sku_schema

**Context:** No SKU schema file exists for the company's product category.
**Autonomous resolution:** Verify that the subcategory from the company report exists in the product taxonomy categories file. If it does, the schema simply hasn't been created yet — trigger SKU schema generation for that subcategory. Once the schema is available, return to Step 2 and continue.
**Escalate when:** The subcategory from the company report does not appear in the product taxonomy categories file. This indicates a taxonomy integrity issue that must be resolved before the pipeline can continue.
**Escalation payload:** Company slug, the full `Category > Subcategory` value from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: probe_extraction_failed

**Context:** The probe found that the scraper's extraction logic does not work against the actual product pages — selectors don't match, JSON-LD structure is unexpected, or universal attributes cannot be extracted.
**Autonomous resolution:** Fix the scraper code and re-probe. Repeat up to 5 times per issue.
**Escalate when:** The same extraction issue persists after 5 probe-fix cycles. The site structure may be incompatible with the agent's extraction capabilities.
**Escalation payload:** Company slug, the specific extraction failure, what was tried, sample HTML from the problematic page.

### Decision: scraper_test_failed

**Context:** The scraper failed during the full `--limit 20` test — it crashed, produced no output, found far fewer products than expected, or had widespread missing data. The probe passed, so this is a structural issue (pagination, rate limiting, batching), not an extraction issue.
**Autonomous resolution:** Retry once. Analyze the error, adjust the scraper, and test again.
**Escalate when:** The scraper fails a second time after adjustment.
**Escalation payload:** Company slug, error details or partial results, what was tried in the retry, the scraping strategy that was used.
