# Catalog Detector Script Split — Design Spec

**Date:** 2026-03-17
**Goal:** Split `catalog_probe.py` (959 lines, four blended concerns) into four focused tactical scripts plus a thin orchestrator. Each script is independently runnable, self-documenting, and small enough to reason about in isolation. Per-slug output files are stored in a structured subdirectory rather than scattered in the root of `docs/catalog-detector/`.

## Problem

`catalog_probe.py` is 959 lines mixing transport/fetching, platform detection, anti-bot analysis, sitemap parsing, knowledgebase loading, and recipe verification into one file. This causes three problems:

1. **Comprehension:** it is not obvious which section of the script is responsible for which output field, or how to interpret a given result.
2. **Maintenance:** changing recipe verification risks breaking platform detection; a bug in XML parsing silently affects the recipe_match result.
3. **Model guidance:** the model has no clear signal for when to use the probe, what each output field means, or what `recipe_match == "poor"` actually implies — leading to misinterpretation (e.g., harlowbros false negative where category page URLs produced a spurious "poor" rating).

`validate_assessment.py` (338 lines) is a single concern and does not need splitting, but its gate functions have no docstrings — the model cannot determine what a gate failure means or how to fix it.

Script outputs are not persisted. Only stderr logs are saved. The probe JSON goes to stdout and is consumed once; individual probe sub-results are never inspectable after the run.

## Constraints (inherited from existing scripts design)

1. Scripts report evidence, not decisions. No pass/fail verdicts that hide reasoning.
2. Scripts are immutable during pipeline execution. Record bugs in Platform-Specific Notes; fix in a dedicated maintenance pass.
3. Exit codes are the contract: `0` = full result, `1` = partial (errors[] explains gaps), `2` = crash (fall back to manual reasoning).
4. Null means "not found." Errors array distinguishes "absent" from "couldn't check."

---

## Script Inventory

| Script | Lines (est.) | Single responsibility |
|---|---|---|
| `probe_access.py` | ~150 | Fetch homepage, detect blocking, measure transport health |
| `probe_platform.py` | ~120 | Detect CMS/platform from HTML signals and headers |
| `probe_discovery.py` | ~220 | Parse robots.txt, sitemap, homepage links — find product URLs |
| `probe_recipe.py` | ~280 | Load knowledgebase, verify extraction recipe on sampled product pages |
| `catalog_probe.py` | ~100 | Orchestrator: coordinate the four scripts, assemble final JSON |
| `validate_assessment.py` | ~360 | Receives documentation pass (gate docstrings) and `--output-json` flag |

All tactical scripts are **independently runnable**: `uv run probe_access.py --url https://example.com` works on its own, prints JSON to stdout, and has its own PEP 723 `# /// script` inline dependency block.

---

## Script Interfaces

### `probe_access.py`

**CLI:** `uv run probe_access.py --url <url>`

**Output JSON:**
```json
{
  "url": "https://...",
  "final_url": "https://...",
  "redirected": false,
  "cross_domain_redirect": false,
  "homepage_status": 200,
  "transport_health": "healthy|degraded|blocked",
  "anti_bot": {
    "challenge_page_detected": false,
    "cloudflare_ray": null,
    "cloudflare_challenge": false,
    "captcha_detected": false,
    "datadome_detected": false,
    "perimeterx_detected": false,
    "blocked_keywords_found": [],
    "homepage_content_length": 12345,
    "suspected_empty_shell": false
  },
  "errors": []
}
```

**Interpretation (must appear in script docstring):**
- `transport_health == "blocked"` → stop immediately; write `anti_bot_severe` assessment
- `transport_health == "degraded"` → proceed but note in Platform-Specific Notes
- `transport_health == "healthy"` → proceed normally
- `anti_bot.suspected_empty_shell == true` → site may be JS-rendered; confirm with probe_platform text_to_html_ratio

---

### `probe_platform.py`

**CLI:** `uv run probe_platform.py --url <url>`

**Output JSON:**
```json
{
  "platform_guess": "magento|prestashop|woocommerce|shopify|unknown|...",
  "platform_confidence": "definitive|likely|weak|none",
  "platform_signal_count": 2,
  "platform_conflict": false,
  "platform_version": null,
  "js_rendering_signals": {
    "body_text_length": 1234,
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
  "errors": []
}
```

**Interpretation (must appear in script docstring):**
- `platform_guess == "unknown"` → deep investigation path; no knowledgebase to load
- `platform_confidence == "definitive"` → signal from meta tag or powered-by header; trust it
- `platform_confidence == "weak"` or `"none"` → use LLM judgment; probe may be wrong
- `platform_conflict == true` → 2+ platforms detected; orchestrator will run `probe_recipe.py` for each candidate and pick best result by `recipe_match` rank (`full > partial > poor`)
- `text_to_html_ratio < 0.05` → likely SPA; check for `js_only` stop condition
- `framework_detected != null` → JS framework present; verify if structured data fallback is available

---

### `probe_discovery.py`

**CLI:** `uv run probe_discovery.py --url <url>`

**Output JSON:**
```json
{
  "robots_txt": {
    "found": true,
    "status": 200,
    "sitemaps": ["https://example.com/sitemap.xml"],
    "disallowed_paths": ["/checkout/", "/account/"],
    "crawl_delay": null
  },
  "sitemap": {
    "found": true,
    "urls_checked": ["https://example.com/sitemap.xml"],
    "product_url_count": 540,
    "product_url_count_truncated": false,
    "product_url_pattern_guess": "/products/{slug}",
    "sample_product_urls": ["https://example.com/products/oak-beam"],
    "sample_success_rate": "5/5"
  },
  "homepage_links": {
    "catalog_links": ["https://example.com/shop"],
    "nav_categories": ["Timber", "Decking", "Cladding"]
  },
  "json_ld_on_homepage": ["BreadcrumbList", "Organization"],
  "errors": []
}
```

**Interpretation (must appear in script docstring):**
- `sitemap.found == false` → use category traversal for product discovery; note in assessment
- `sitemap.sample_success_rate` below 80% → URLs may be stale or behind auth; verify manually
- `robots_txt.crawl_delay` → copy value into scraper config; respect it between requests
- `sitemap.product_url_count == 0` AND `homepage_links.catalog_links == []` → likely `no_public_catalog` stop
- `sample_product_urls` → pass directly to `probe_recipe.py` via `--product-urls`
- `json_ld_on_homepage` contains `"Product"` → structured data likely available on product pages; prioritise `structured_data` strategy

---

### `probe_recipe.py`

**CLI:** `uv run probe_recipe.py --url <url> --platform <platform> --knowledgebase-dir <dir> [--product-urls <url1,url2,...>]`

`--product-urls` is **optional**. When omitted, the script returns `recipe_match: "untested"` immediately with an `errors[]` entry noting no URLs were supplied. This preserves standalone usability — the caller can test a recipe by passing URLs directly without running `probe_discovery.py` first.

**Output JSON:**
```json
{
  "knowledgebase_file": "magento.md",
  "knowledgebase_found": true,
  "knowledgebase_selectors_parsed": 5,
  "knowledgebase_api_endpoints_parsed": 0,
  "recipe_match": "full|partial|poor|untested",
  "product_pages_tested": 3,
  "checks": [
    {
      "url": "https://...",
      "status": 200,
      "json_ld_found": true,
      "json_ld_type": "Product",
      "css_checks": [
        {"selector": "h1", "found": true, "sample_text": "Oak Beam 100x100mm"}
      ],
      "api_checks": []
    }
  ],
  "pagination_check": {
    "tested": true,
    "pattern_confirmed": "?p={n}",
    "next_page_found": true
  },
  "errors": []
}
```

**Interpretation (must appear in script docstring):**
- `recipe_match == "full"` → recipe verified on real product pages; use fast path
- `recipe_match == "partial"` → some checks passed; verify failing ones manually before trusting
- `recipe_match == "poor"` → **does NOT mean the site is broken.** The probe may have received category page URLs from the sitemap instead of product pages. Always inspect `checks[].url` — if URLs contain `/shop/`, `/category/`, or `/collection/` path segments, the match result is invalid. Treat as `"untested"` and proceed to manual investigation.
- `recipe_match == "untested"` → no product URLs supplied or available; proceed to Step 3a
- `knowledgebase_found == false` → no recipe to verify; proceed to deep investigation
- `checks[].status` non-200 → possible access restriction on product pages

---

### `catalog_probe.py` (orchestrator)

**CLI:** `uv run catalog_probe.py --url <url> --slug <slug> --knowledgebase-dir <dir> --output-dir docs/catalog-detector/<slug>`

**Behaviour:**
1. Creates `--output-dir` if it doesn't exist
2. Runs `probe_access.py` → saves result to `{output-dir}/probe_access.json`; if `transport_health == "blocked"`, exits early with assembled JSON
3. Runs `probe_platform.py` → saves result to `{output-dir}/probe_platform.json`
4. Runs `probe_discovery.py` → saves result to `{output-dir}/probe_discovery.json`
5. Runs `probe_recipe.py`, passing `sample_product_urls` from discovery output via `--product-urls`:
   - If `platform_conflict == false` AND knowledgebase exists for `platform_guess`: run once for `platform_guess`
   - If `platform_conflict == true`: run once per candidate platform **that has a knowledgebase**; keep result with best `recipe_match` rank (`full > partial > poor > untested`); save winning result to `{output-dir}/probe_recipe.json`. This rule overrides the skip condition below — even if `platform_guess == "unknown"`, a conflicting candidate with a knowledgebase is still tested.
   - If no candidate has a knowledgebase (including `platform_guess == "unknown"` with no conflict, or all conflict candidates lacking knowledgebases): skip; `probe_recipe.json` is not written
6. Assembles all sub-results into combined JSON → prints to stdout (see Assembled JSON Schema below)
7. Stderr from all sub-scripts is merged and saved to `{output-dir}/probe.log`

The orchestrator contains no analysis logic — only coordination, file I/O, and JSON assembly.

### Assembled JSON Schema

The orchestrator merges sub-script outputs into a flat dict. Fields from each sub-script are merged at the top level:

```json
{
  "url": "...", "final_url": "...", "redirected": false,
  "cross_domain_redirect": false, "homepage_status": 200,
  "transport_health": "healthy",
  "anti_bot": {
    "challenge_page_detected": false,
    "cloudflare_ray": null,
    "cloudflare_challenge": false,
    "captcha_detected": false,
    "datadome_detected": false,
    "perimeterx_detected": false,
    "blocked_keywords_found": [],
    "homepage_content_length": 12345,
    "suspected_empty_shell": false
  },
  "platform_guess": "magento", "platform_confidence": "likely",
  "platform_signal_count": 2, "platform_conflict": false,
  "platform_version": null,
  "js_rendering_signals": { ... },
  "geo_hints": { ... },
  "robots_txt": { ... },
  "sitemap": { ... },
  "homepage_links": { ... },
  "json_ld_on_homepage": [...],
  "recipe_verification": {
    "knowledgebase_file": "magento.md",
    "knowledgebase_found": true,
    "knowledgebase_selectors_parsed": 5,
    "knowledgebase_api_endpoints_parsed": 0,
    "recipe_match": "full",
    "product_pages_tested": 3,
    "checks": [...],
    "pagination_check": { ... }
  },
  "errors": []
}
```

---

## Output Directory Structure

**Per-slug subdirectory replaces the current flat layout:**

```
docs/catalog-detector/
  {slug}/
    probe_access.json       ← transport health and anti-bot results
    probe_platform.json     ← platform detection results
    probe_discovery.json    ← sitemap/robots/links results
    probe_recipe.json       ← recipe verification (only if knowledgebase exists)
    probe.log               ← merged stderr from all probe scripts
    assessment.md           ← catalog assessment document
    validate.json           ← validation gate results
    validate.log            ← validation stderr
```

**SKILL.md probe command:**
```bash
uv run .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url {site_url} --slug {slug} \
  --knowledgebase-dir docs/platform-knowledgebase \
  --output-dir docs/catalog-detector/{slug}
```

**SKILL.md validate command:**
```bash
uv run .claude/skills/catalog-detector/scripts/validate_assessment.py \
  docs/catalog-detector/{slug}/assessment.md \
  --knowledgebase-dir docs/platform-knowledgebase \
  --output-json docs/catalog-detector/{slug}/validate.json \
  2>docs/catalog-detector/{slug}/validate.log
```

`validate_assessment.py` gains an `--output-json` flag that writes gate results to a file in addition to stdout. Gate logic is unchanged.

---

## Documentation Requirements

### Layer 1: Script header docstring

Every tactical script (`probe_access.py`, `probe_platform.py`, `probe_discovery.py`, `probe_recipe.py`) opens with a module-level docstring covering:
- One-sentence description of what it does
- When to call it (which workflow step, what preconditions must be true)
- What arguments it requires
- Exit code contract
- Critical interpretation notes (especially failure modes and false positives)

### Layer 2: Output field inline comments

The assembled `result` dict in each script's `main()` function has inline comments on every field explaining its possible values and what each means to the caller. Example:

```python
result = {
    "recipe_match": recipe_match,
    # "full"     → recipe verified on product pages; use fast path
    # "partial"  → some checks passed; verify the failing ones manually
    # "poor"     → most checks failed; VERIFY checks[].url before concluding —
    #              category page URLs produce false "poor" results
    # "untested" → no product URLs supplied or available; proceed to Step 3a
}
```

### Layer 3: validate_assessment.py gate docstrings

Every `check_*` function in `validate_assessment.py` receives a docstring covering:
- What it verifies
- What failure means in plain language
- How to fix the failure

Example:
```python
def check_price_verified(content: str) -> dict:
    """
    Verifies that the Price section contains ≥2 URLs with observed price values.

    WHAT IT CHECKS: Looks for lines matching '- https?://...' or '- /path/...'
    in the #### Price section. Counts distinct verified URLs.

    FAILURE MEANS: The price selector was written without being tested on real pages.
    HOW TO FIX: Navigate to 2+ product pages, observe the actual price rendered,
    and record each URL with its observed price in the Verified on: block.
    """
```

---

## Migration

Existing flat files under `docs/catalog-detector/` are gitignored and can be cleaned up manually. New runs write to the subdirectory structure automatically. SKILL.md routing conditions are updated to match the new schema as part of implementation — no separate migration step needed.
