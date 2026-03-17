# Catalog Detector Scripts — Design Spec

**Date:** 2026-03-17
**Goal:** Reduce LLM token cost in catalog-detector by scripting mechanical steps (platform detection, recipe verification, anti-bot check, report validation). Scripts report evidence; the LLM decides.

## Constraints

1. **Scripts report evidence, not decisions.** Raw extraction results, confidence levels, and symptoms — never pass/fail verdicts that hide reasoning.
2. **Scripts are immutable during pipeline execution.** The workflow MUST NOT modify, patch, or fix these scripts — even if the bug is obvious. Editing scripts mid-pipeline risks introducing regressions that affect other companies. If a script fails, the LLM falls back to manual reasoning and records the issue in Platform-Specific Notes for a dedicated maintenance pass.
3. **Structured logging to stderr.** Every HTTP request, selector test, and decision point is logged as a JSON line. If the script crashes, the LLM reads the log to understand what happened and proceeds manually.
4. **Exit codes are the contract.** `0` = full result on stdout. `1` = partial result (some checks couldn't run — JSON still on stdout with `errors` array explaining gaps). `2` = script error (fall back to manual reasoning entirely).
5. **Null means "not found." Errors are explicit.** A null field means the check ran and found nothing. When a check couldn't run (network error, timeout), the field is null AND the `errors` array contains an entry explaining why. The LLM checks the `errors` array to distinguish "absent" from "unknown."

## Prerequisite: Knowledgebase Format Normalization

Before implementation, migrate the `## CSS Selectors` sections in `woocommerce.md` and `shopify.md` from bullet-list format to the markdown table format used in `prestashop.md` and `magento.md`:

```markdown
## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on listing | `ul.products li.product a` | Filter for href containing `/product/` |
| ...     | ...      | ...   |
```

The workflow's Step 5 template already defines this table format for new knowledgebase files. Existing files predate the template and need alignment. The script's table parser depends on this format — without it, CSS verification silently finds zero selectors for the two most common e-commerce platforms.

Also normalize the `## Pagination` section in `shopify.md` to use `URL pattern:` and `Products per page:` bullet items (the format all other files use), adding entries for each discovery method (JSON API, HTML collections, sitemap).

---

## Script 1: `catalog_probe.py`

**Location:** `.claude/skills/catalog-detector/scripts/catalog_probe.py`

**Replaces:** Workflow Steps 1 (platform detection), 2 (fast-path recipe verification), 3a (anti-bot check)

### CLI

```bash
uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url https://www.example.com \
  --knowledgebase-dir docs/platform-knowledgebase \
  --timeout 15 \
  --delay 0.5 \
  2>probe_stderr.log
```

| Arg | Required | Default | Description |
|-----|----------|---------|-------------|
| `--url` | yes | — | Company website URL (homepage) |
| `--knowledgebase-dir` | yes | — | Path to platform knowledgebase directory |
| `--timeout` | no | 15 | Per-request timeout in seconds |
| `--delay` | no | 0.5 | Seconds to wait between HTTP requests (rate-limit safety) |
| `--max-product-samples` | no | 5 | Number of product URLs to sample for recipe verification |
| `--max-response-size` | no | 2000000 | Max response body size in bytes (truncate beyond this) |

### Output (stdout, JSON)

```json
{
  "url": "https://www.example.com",
  "final_url": "https://www.example.com/en/",
  "redirected": true,
  "cross_domain_redirect": false,
  "homepage_status": 200,
  "errors": [],
  "rate_limited": false,
  "platform_signals": {
    "meta_generator": "PrestaShop 9.0.2",
    "powered_by_header": null,
    "shopify_cdn": false,
    "wp_content_path": false,
    "prestashop_modules_path": true,
    "magento_static_version": false,
    "woocommerce_body_class": false,
    "bigcommerce_cdn": false,
    "squarespace_static": false,
    "wix_static": false,
    "drupal_settings": false
  },
  "platform_guess": "prestashop",
  "platform_confidence": "definitive",
  "platform_signal_count": 2,
  "platform_conflict": false,
  "platform_version": "PrestaShop 9.0.2",
  "anti_bot": {
    "homepage_content_length": 45230,
    "challenge_page_detected": false,
    "suspected_empty_shell": false,
    "cloudflare_ray": null,
    "cloudflare_challenge": false,
    "captcha_detected": false,
    "datadome_detected": false,
    "perimeterx_detected": false,
    "blocked_keywords_found": [],
    "product_page_status": 200,
    "product_page_accessible": true
  },
  "js_rendering_signals": {
    "body_text_length": 12450,
    "noscript_tag_found": false,
    "framework_detected": null,
    "empty_product_container": false,
    "text_to_html_ratio": 0.28
  },
  "geo_hints": {
    "vary_accept_language": false,
    "html_lang": "en-GB",
    "geo_redirect_detected": false,
    "country_path_segment": null
  },
  "robots_txt": {
    "found": true,
    "status": 200,
    "sitemaps": ["https://example.com/sitemap.xml"],
    "disallowed_paths": ["/cart", "/checkout", "/my-account"],
    "crawl_delay": null
  },
  "sitemap": {
    "found": true,
    "urls_checked": ["https://example.com/sitemap.xml"],
    "product_url_count": 540,
    "product_url_count_truncated": false,
    "product_url_pattern_guess": "/{category}/{id}-{slug}.html",
    "sample_product_urls": [
      "https://example.com/beams/55-green-oak-150.html",
      "https://example.com/flooring/323-oak-architrave.html",
      "https://example.com/cladding/126-shiplap.html"
    ],
    "sample_success_rate": "5/5"
  },
  "homepage_links": {
    "catalog_links": ["/products", "/shop", "/collections"],
    "nav_categories": ["Structural Timber", "Cladding", "Outdoor"]
  },
  "json_ld_on_homepage": ["Organization", "WebSite"],
  "recipe_verification": {
    "knowledgebase_file": "prestashop.md",
    "knowledgebase_found": true,
    "knowledgebase_selectors_parsed": 6,
    "knowledgebase_api_endpoints_parsed": 0,
    "recipe_match": "full",
    "product_pages_tested": 3,
    "checks": [
      {
        "url": "https://example.com/beams/55-green-oak-150.html",
        "status": 200,
        "page_truncated": false,
        "body_text_length": 8500,
        "json_ld_product_found": true,
        "json_ld_extracted": {
          "name": "Green Oak Beams 150mm x 150mm",
          "sku": "GOB150150",
          "price": "66.99",
          "currency": "GBP",
          "brand": "UK Timber"
        },
        "css_checks": [
          {"selector": "h1", "extracted": "Green Oak Beams 150mm x 150mm", "non_empty": true},
          {"selector": ".price", "extracted": "From £66.99 + VAT", "non_empty": true},
          {"selector": "nav.breadcrumb", "extracted": "Home > Structural Timber > ...", "non_empty": true}
        ],
        "api_checks": [],
        "attribute_selectors_tested": [
          {"selector": ".product-variants .form-group", "count": 3}
        ]
      }
    ],
    "pagination_check": {
      "tested": true,
      "category_url": "https://example.com/58-green-oak-beams",
      "page1_product_count": 10,
      "page2_url": "https://example.com/58-green-oak-beams?page=2",
      "page2_status": 200,
      "page2_product_count": 10,
      "products_differ": true
    }
  },
  "transport_health": {
    "total_requests": 12,
    "status_200_count": 11,
    "status_429_count": 0,
    "status_403_count": 0,
    "status_other_count": 1,
    "timeouts": 0,
    "suspected_challenge_pages": 0,
    "inter_request_delay_used": 0.5,
    "overall": "healthy"
  }
}
```

### Key design rules

**Platform detection:**
- Check ALL platform signals, not just the first match. Report every signal found.
- `platform_guess` is the best match. `platform_confidence` uses a distinct scale from recipe verification: `definitive` (explicit meta tag or header), `likely` (path patterns only), `weak` (heuristic/inconclusive), `none` (no signals → `unknown`).
- `platform_signal_count`: how many signals were positive. The LLM can assess if confidence is based on 1 weak signal or 5 strong ones.
- `platform_conflict`: true when 2+ different platforms have positive signals (e.g., wp_content_path + shopify_cdn). When true, the LLM should not trust `platform_guess` without manual verification.
- `platform_version`: the full version string from meta_generator or equivalent (e.g., "PrestaShop 9.0.2", "Shopify"). Null if no version info found. Helps the LLM assess knowledgebase staleness.
- Never return `custom` — that's an LLM judgment. Return `unknown` with the raw signals. The LLM decides whether `unknown` + recognizable signals warrants `custom` classification.
- When `platform_conflict` is true AND knowledgebase files exist for multiple detected platforms, run recipe verification against each matching platform and report all results under `recipe_verification.checks`.

**Anti-bot detection:**
- Report symptoms only: HTTP status codes, challenge page markers, known bot-detection headers.
- `challenge_page_detected`: true if the response body matches any of these patterns (case-insensitive):
  - `"you have been blocked"`, `"access denied"`, `"challenge-platform"`, `"cf-browser-verification"`
  - `"just a moment"` (Cloudflare Turnstile title)
  - `"cf-turnstile"`, `"_cf_chl_opt"` (Turnstile widget markers)
  - `"checking if the site connection is secure"` (Cloudflare managed challenge)
  - `<iframe src="https://challenges.cloudflare.com"` (Cloudflare challenge iframe)
  - CAPTCHA markers: `"g-recaptcha"`, `"h-captcha"`, `"captcha"` in form action
- `suspected_empty_shell`: true if `homepage_content_length > 1000` but `body_text_length < 500` and no `<nav>`, `<article>`, or `<main>` elements with substantial text. This catches JS-rendered shells that return HTTP 200 but have no server-rendered content.
- `blocked_keywords_found`: deduplicated list of matched keywords from the patterns above.
- Also fetch one product page (from sitemap or homepage links) to check if product pages are blocked even when homepage isn't.

**JS rendering signals:**
- `body_text_length`: length of text content inside `<body>`, stripped of `<script>` and `<style>` tags. Short body text relative to `homepage_content_length` suggests JS rendering.
- `noscript_tag_found`: true if `<noscript>` tag exists (common in SPA frameworks).
- `framework_detected`: check for known framework markers — `__NEXT_DATA__` (Next.js), `window.__NUXT__` (Nuxt), `ng-app` or `ng-version` (Angular), `data-reactroot` (React), `data-v-` attributes (Vue). Null if none found.
- `empty_product_container`: true if the homepage has a container element (`.products`, `#product-list`, `[data-products]`) that is empty or contains only loading placeholders.
- `text_to_html_ratio`: `body_text_length / homepage_content_length`. Below 0.05 strongly suggests JS rendering.

**Geo hints:**
- `vary_accept_language`: true if response has `Vary: Accept-Language` header.
- `html_lang`: value of `<html lang="...">` attribute.
- `geo_redirect_detected`: true if `final_url` contains a country/language path segment (e.g., `/en-gb/`, `/us/`, `/de/`, `/fr/`).
- `country_path_segment`: the detected segment (e.g., `"en-gb"`) or null.

**Sitemap parsing:**
- Follow sitemap index files (sitemaps containing other sitemaps). Max recursion depth: 3 levels.
- Count URLs matching common product patterns: `/product/`, `/p/`, `.html`, `/shop/`, `/collections/`.
- `product_url_pattern_guess` is a URL template with named placeholders (e.g., `/{category}/{id}-{slug}.html`) — NOT a regex. The LLM validates it.
- If sitemap is huge (>10K URLs), stop counting at 10K, set `product_url_count` to 10000 and `product_url_count_truncated` to true.
- Sample product URLs from diverse positions in the sitemap (beginning, middle, end) to avoid clustering of stale URLs. Default 5 samples.
- `sample_success_rate`: `"{ok}/{total}"` — how many sampled URLs returned HTTP 200. Alerts the LLM to sitemap staleness if ratio is low.

**Knowledgebase parsing:**
- The script parses the `## CSS Selectors` section as a markdown table — extracts the `Selector` column from each row. Requires the table format from the workflow template (pipe-delimited, header row with `Element | Selector | Notes`).
- The script parses `## JSON-LD Patterns` as free text — looks for mentions of specific `@type` values (Product, BreadcrumbList, etc.).
- The script parses `## Pagination` section for `URL pattern:` and `Products per page:` values from bullet items.
- If a platform has documented API endpoints (e.g., Shopify's `/products.json`), the script parses those from the `## Shopify JSON API` or equivalent section and tests them under `api_checks`.
- `knowledgebase_selectors_parsed`: count of CSS selectors extracted from the table. If 0, the LLM knows CSS verification was skipped.
- `knowledgebase_api_endpoints_parsed`: count of API endpoints found. If 0 for a platform that should have APIs (Shopify), the LLM can manually verify.
- Other knowledgebase sections (Common Pitfalls, Sites Using This Platform) are not parsed by the script — they're for LLM consumption only.

**Recipe verification:**
- Only runs if `knowledgebase_found` is true.
- For each sample product URL: fetch the page, try JSON-LD extraction, try each CSS selector from the knowledgebase table, try each API endpoint.
- Report raw extracted text — never interpret or validate content. The LLM judges if "£66.99 + VAT" is a usable price.
- `non_empty`: true/false — the only judgment the script makes is empty vs non-empty.
- `recipe_match` uses a distinct scale from platform confidence: `full` (all checks pass on all URLs and pagination verified), `partial` (>50% pass but gaps exist), `poor` (<50% pass), `untested` (couldn't test — no selectors parsed, all URLs failed, etc.).
- **If `pagination_check.tested` is false, `recipe_match` cannot be `full` — downgrade to `partial` at best.** Pagination is a core verification step.
- `body_text_length` per check: text length of `<body>` stripped of scripts/styles. If very short (< 500) on a page with `status: 200`, the page may be JS-rendered — the LLM should investigate even if JSON-LD was found.
- `json_ld_extracted` is limited to: `name`, `sku`, `price`, `currency`, `brand`, `@type`. All other JSON-LD fields (description, images, reviews) are dropped to control output size.
- `css_checks` capped at 10 selectors per URL (most important first per knowledgebase order).
- Extracted text truncated to 200 characters per field.

**Pagination check:**
- Attempts to find a category page from the sitemap or knowledgebase and verify that page 2 exists and contains different products than page 1.
- When tested, reports full schema: category URL, page 1 product count, page 2 URL and status, page 2 product count, and whether products differ.
- When not tested (no category URL found), reports `tested: false` with reason.

**Transport health:**
- Synthesizes signals across ALL HTTP requests made during the probe.
- `rate_limited` (top-level): true if any request received HTTP 429.
- `overall`: `healthy` (all 200s), `degraded` (some non-200s or timeouts), `blocked` (majority 403/429/challenge pages).
- This gives the LLM a single place to check "did the probe itself have connectivity issues?" before trusting detailed findings.

**Rate limiting:**
- Wait `--delay` seconds between every HTTP request (default 0.5s).
- On HTTP 429: check `Retry-After` header, wait that duration (or 5s default), retry once. If still 429, record and move on.

**Redirect handling:**
- Follow redirects (httpx default) up to 10 hops. Record `final_url`, `redirected`, and `cross_domain_redirect`.
- `cross_domain_redirect`: true when the final URL's registrable domain differs from the input URL's domain. The LLM decides whether to use the original or redirected URL.
- Use the `final_url` for resolving relative paths (robots.txt, sitemap, product URLs).

**Response size and encoding:**
- Truncate response bodies at `--max-response-size` (default 2MB). Set `page_truncated: true` on affected checks. For HTML parsing, the first 2MB almost always contains all product data (JSON-LD is in `<head>`, main content is early in `<body>`).
- Always use `response.text` (decoded Unicode) when passing HTML to selectolax, never `response.content` (raw bytes). If `response.encoding` is None (charset detection failed), decode with `utf-8` errors=`replace` as fallback.

**Error handling:**
- Every HTTP request is wrapped in try/except. Failures are logged to stderr and the corresponding field is set to null.
- **The `errors` array captures every check that couldn't run**, with `section` (which output field is affected) and `error` (what went wrong). This lets the LLM distinguish "checked and not found" (null, no error) from "couldn't check" (null, error entry present).
- If the homepage itself is unreachable, exit with code 1 and a partial result.
- If a product page 404s, try the next sample URL. If all sample URLs fail, set `recipe_match` to `untested`.
- Never raise unhandled exceptions — catch everything, log it, degrade gracefully.

### Logging (stderr, JSON lines)

```json
{"level": "info", "message": "Fetching homepage", "url": "https://...", "timestamp": "..."}
{"level": "info", "message": "Homepage fetched", "status": 200, "content_length": 45230, "timestamp": "..."}
{"level": "info", "message": "Platform signal found", "signal": "meta_generator", "value": "PrestaShop 9.0.2", "timestamp": "..."}
{"level": "info", "message": "Waiting between requests", "delay_seconds": 0.5, "timestamp": "..."}
{"level": "warning", "message": "Rate limited", "url": "https://...", "status": 429, "retry_after": 5, "timestamp": "..."}
{"level": "warning", "message": "Response truncated", "url": "https://...", "original_size": 5200000, "truncated_to": 2000000, "timestamp": "..."}
{"level": "warning", "message": "Sitemap fetch failed", "url": "https://.../sitemap.xml", "error": "Timeout", "timestamp": "..."}
{"level": "error", "message": "Homepage unreachable", "url": "https://...", "error": "ConnectionError", "timestamp": "..."}
```

### Exit codes

| Code | Meaning | LLM action |
|------|---------|------------|
| 0 | Full result — all sections populated, `errors` array empty | Read JSON, use for routing |
| 1 | Partial result — some sections null, `errors` array explains gaps | Read JSON + `errors` array, supplement with manual fetches for affected sections |
| 2 | Script crashed — no usable JSON on stdout | Read stderr log, fall back to manual Steps 1-3 entirely |

### Invocation guidance

Always redirect stderr to a file to prevent log lines from mixing with the JSON result:

```bash
uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url {site_url} --knowledgebase-dir docs/platform-knowledgebase \
  2>docs/catalog-detector/{slug}_probe_stderr.log
```

Parse stdout as a single JSON object. Read the stderr log file separately for diagnostics.

---

## Script 2: `validate_assessment.py`

**Location:** `.claude/skills/catalog-detector/scripts/validate_assessment.py`

**Replaces:** Workflow Step 6 (self-verification gates)

### CLI

```bash
uv run python .claude/skills/catalog-detector/scripts/validate_assessment.py \
  docs/catalog-detector/uk-timber.md \
  --knowledgebase-dir docs/platform-knowledgebase \
  2>validate_stderr.log
```

| Arg | Required | Default | Description |
|-----|----------|---------|-------------|
| positional | yes | — | Path to the catalog assessment markdown file |
| `--knowledgebase-dir` | no | `docs/platform-knowledgebase` | Path to check for knowledgebase updates |

### Output (stdout, JSON)

```json
{
  "file": "docs/catalog-detector/uk-timber.md",
  "detected_template": "success",
  "gates": {
    "correct_template": {
      "pass": true,
      "details": "Success template detected: has Extraction Blueprint section"
    },
    "heading_and_slug": {
      "pass": true,
      "details": "H1: 'Catalog Assessment: UK Timber Ltd', Slug: 'uk-timber'"
    },
    "strategy_valid": {
      "pass": true,
      "details": "Strategy: structured_data"
    },
    "platform_valid": {
      "pass": true,
      "details": "Platform: prestashop"
    },
    "data_source_concrete": {
      "pass": true,
      "details": "Primary method: json_ld, has endpoint/URL pattern"
    },
    "discovery_actionable": {
      "pass": true,
      "details": "Discovery method: productlist_module, pagination pattern present, products per page: ~50"
    },
    "category_tree_complete": {
      "pass": false,
      "details": "2 of 12 leaf categories have dash instead of a product count"
    },
    "price_verified": {
      "pass": true,
      "details": "4 product URLs found with price values in Verified on section"
    },
    "spec_table_verified": {
      "pass": true,
      "details": "3 product URLs found with attribute counts in Verified on section"
    },
    "product_count": {
      "pass": true,
      "details": "250 (productlist module)"
    },
    "knowledgebase_updated": {
      "pass": true,
      "details": "Found 'uk-timber' in prestashop.md Sites table"
    },
    "anti_bot_value": {
      "pass": true,
      "details": "Anti-bot: none"
    }
  },
  "passed": 11,
  "failed": 1,
  "issues": [
    "Gate 7 (category_tree_complete): 2 of 12 leaf categories have dash instead of a product count"
  ]
}
```

### Key design rules

**Template detection:**
- If `Scraping strategy: none` and `Stop reason:` present → stop template. Check stop gates (3 gates).
- If `## Extraction Blueprint` present → success template. Check success gates (12 gates).
- If neither → report `"detected_template": "unknown"` and fail all gates.

**Gate checks (pure string/regex matching):**

| Gate | How the script checks it |
|------|------------------------|
| correct_template | Presence of `## Extraction Blueprint` (success) or `Stop reason:` (stop) |
| heading_and_slug | H1 starts with `# Catalog Assessment:`, `**Slug:**` line present with non-empty value |
| strategy_valid | `**Scraping strategy:**` value is one of: `static_html`, `structured_data`, `pdf_pricelist`, `none` |
| platform_valid | `**Platform:**` value is one of the enumerated platforms |
| data_source_concrete | `### Data Source` section exists with `**Primary method:**` and `**Endpoint/URL pattern:**` that aren't placeholder text |
| discovery_actionable | `### Product Discovery` section has `**Discovery method:**`, `**Pagination mechanism:**`, `**Products per page:**` |
| category_tree_complete | Parse the `#### Verified Category Tree` table. Every row with Depth > 1 and no "(landing)" note must have a numeric product count |
| price_verified | `#### Price` section has `**Verified on:**` with at least 2 URLs containing price values |
| spec_table_verified | `#### Spec Table / Attributes` section has `**Verified on:**` with at least 2 URLs |
| product_count | `**Estimated product count:**` has a number (not just text) |
| knowledgebase_updated | Check if the slug appears in `{knowledgebase-dir}/{platform}.md` Sites table |
| anti_bot_value | `**Anti-bot:**` value starts with one of: `none`, `light`, `moderate` |

**Stop template gates:**

| Gate | How checked |
|------|------------|
| stop_template | `**Scraping strategy:** none` and `**Stop reason:**` present |
| valid_stop_reason | Value is one of: `no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, `attributes_not_extractable` |
| findings_explain | `## Findings` section exists with at least one bullet point |

**Error handling:**
- If the file doesn't exist or is empty, exit 2 with error on stderr.
- If the file can't be parsed as markdown (no H1), exit 1 with a partial result noting the parse failure.
- Each gate check is independent — one gate crashing doesn't prevent other gates from running.

### Logging, exit codes, invocation

Same patterns as `catalog_probe.py`. Redirect stderr to a file. Parse stdout as JSON.

---

## Workflow Integration

### Changes to SKILL.md

Add to the `## Workflow` section:

```
- Before starting the workflow, run the catalog probe script:
  `uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py --url {site_url} --knowledgebase-dir docs/platform-knowledgebase 2>docs/catalog-detector/{slug}_probe_stderr.log`
  Parse stdout as JSON. Read the stderr log file for diagnostics if needed.
  - Exit code 0 or 1: use the probe results to inform Steps 1-3. Routing logic:
    - If recipe_match is "full" AND transport_health.overall is "healthy" AND anti_bot shows no blocking AND js_rendering_signals show no SPA framework:
      → Skip Steps 1-3, proceed to Step 4 using the probe data.
    - If recipe_match is "full" BUT anti_bot shows issues OR js_rendering_signals.text_to_html_ratio < 0.05:
      → Skip Steps 1-2, proceed to Step 3 for deeper investigation of the flagged concern.
    - If recipe_match is "partial" or "poor":
      → Use probe data as a starting point, proceed to Step 3 (starting at 3b, the probe already covers 3a).
    - If recipe_match is "untested" (no knowledgebase or all URLs failed):
      → Proceed to Step 3 from 3a, using probe's anti_bot and platform signals as context.
    - If platform_guess is "unknown" but signals suggest a recognizable CMS, classify as "custom" — the script never returns "custom" because that requires LLM judgment.
    - Check the errors array: any entry means the corresponding section's data is incomplete. Supplement with manual investigation for those sections.
  - Exit code 2: ignore the script output, fall back to manual Steps 1-3 entirely.
  - DO NOT modify the probe script. If it produces unexpected results, use manual reasoning to verify or override — the script output is evidence, not a verdict.

- After writing the catalog assessment, run the validation script:
  `uv run python .claude/skills/catalog-detector/scripts/validate_assessment.py docs/catalog-detector/{slug}.md --knowledgebase-dir docs/platform-knowledgebase 2>docs/catalog-detector/{slug}_validate_stderr.log`
  Fix any failing gates. DO NOT modify the validation script.
```

### Immutability rule

Both scripts are treated as read-only infrastructure during pipeline execution. The workflow MUST include this instruction:

> **These scripts are infrastructure, not generated code. Never edit, patch, or fix them during a pipeline run — even if you can identify the bug. If a script fails (exit code 2) or produces unexpected results, fall back to manual reasoning for those steps. Record the issue in the catalog assessment's Platform-Specific Notes so it can be fixed in a dedicated maintenance pass. Editing scripts mid-pipeline risks introducing regressions that affect other companies.**

---

## Dependencies

Both scripts use only:
- `httpx` — HTTP client
- `selectolax` — HTML parsing (for CSS selector verification)
- Standard library: `json`, `re`, `argparse`, `sys`, `pathlib`, `datetime`, `time`, `xml.etree.ElementTree`

PEP 723 inline metadata:
```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
```

---

## Token savings estimate

| Scenario | Before (tokens) | After (tokens) | Savings |
|----------|-----------------|----------------|---------|
| Known platform, recipe passes (fast path) | ~40K | ~25K | ~15K (38%) |
| Known platform, recipe fails → deep investigation | ~50K | ~40K | ~10K (20%) |
| Unknown platform → deep investigation | ~50K | ~45K | ~5K (10%) |
| Anti-bot stop (early exit) | ~20K | ~5K | ~15K (75%) |
| Report validation (all runs) | ~3K | ~500 | ~2.5K (83%) |

Weighted average across pipeline runs: **~25-30% token reduction** for catalog-detector stage.
