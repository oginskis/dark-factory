# Catalog Detector Script Split — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the monolithic `catalog_probe.py` (959 lines) into 4 focused tactical scripts + thin orchestrator, add gate docstrings to `validate_assessment.py`, update SKILL.md.

**Architecture:** Extract shared HTTP/logging infrastructure into `_probe_lib.py`. Each tactical script imports from it and is independently runnable via `uv run`. The orchestrator runs tactical scripts as subprocesses and assembles their JSON outputs. Per-slug output directories replace the current flat layout.

**Tech Stack:** Python 3.10+, httpx, selectolax, PEP 723 inline script metadata, `uv run`

**Spec:** `docs/superpowers/specs/2026-03-17-catalog-detector-script-split-design.md`

---

## File Structure

All files under `.claude/skills/catalog-detector/scripts/`:

| File | Action | Responsibility |
|------|--------|---------------|
| `_probe_lib.py` | Create | Shared HTTP client, logging, transport tracking, challenge detection |
| `probe_access.py` | Create | Fetch homepage, detect blocking, measure transport health |
| `probe_platform.py` | Create | Detect CMS/platform from HTML signals and headers |
| `probe_discovery.py` | Create | Parse robots.txt, sitemap, homepage links — find product URLs |
| `probe_recipe.py` | Create | Load knowledgebase, verify extraction recipe on sampled product pages |
| `catalog_probe.py` | Rewrite | Thin orchestrator: run 4 scripts as subprocesses, assemble JSON, save per-slug output files |
| `validate_assessment.py` | Modify | Add gate docstrings + `--output-json` flag |

Also modify:
| File | Action | Change |
|------|--------|--------|
| `.claude/skills/catalog-detector/SKILL.md` | Modify | New probe/validate commands, updated routing conditions |

### Shared library design

`_probe_lib.py` is NOT a standalone script — no PEP 723 block, no `if __name__`. It's imported by sibling scripts (Python's `sys.path[0]` = script directory makes this work with `uv run`).

Contains functions extracted verbatim from current `catalog_probe.py`:
- `log()` (lines 30-33)
- `CHALLENGE_PATTERNS` (lines 36-49)
- `detect_challenge_page()` (lines 52-54)
- `find_blocked_keywords()` (lines 57-59)
- `TransportTracker` class (lines 62-109) — **modified:** `summary()` returns just the `overall` string, not the full dict
- `fetch()` (lines 112-158)
- `get_body_text_length()` (lines 336-341)
- `make_client()` — new helper that returns a configured `httpx.Client` with browser-like headers

Each tactical script declares `httpx` and `selectolax` in its PEP 723 block (so `uv run` installs them), then does `from _probe_lib import ...`.

---

## Task 1: Create `_probe_lib.py`

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/_probe_lib.py`

- [ ] **Step 1: Create the shared library**

Extract from current `catalog_probe.py` lines 14-158 and 336-341:
- Imports: `json`, `sys`, `time`, `re` from stdlib; `httpx` from third-party; `HTMLParser` from selectolax
- `log()` — verbatim from lines 30-33
- `CHALLENGE_PATTERNS` — verbatim from lines 36-49
- `detect_challenge_page()` — verbatim from lines 52-54
- `find_blocked_keywords()` — verbatim from lines 57-59
- `TransportTracker` class — from lines 62-109, but change `summary()` to return just the `overall` string:
  ```python
  def summary(self) -> str:
      """Return transport health as a string: 'healthy', 'degraded', or 'blocked'."""
      if self.status_403 + self.status_429 + self.challenge_pages > self.total / 2:
          return "blocked"
      total_non_ok = self.total - self.status_200
      if total_non_ok > 0 or self.timeouts > 0:
          return "degraded"
      return "healthy"
  ```
- `fetch()` — verbatim from lines 112-158
- `get_body_text_length()` — verbatim from lines 336-341
- New `make_client()`:
  ```python
  def make_client() -> httpx.Client:
      return httpx.Client(
          headers={
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          },
          follow_redirects=True,
          max_redirects=10,
      )
  ```

- [ ] **Step 2: Verify import works**

Run: `cd .claude/skills/catalog-detector/scripts && uv run python -c "from _probe_lib import log, fetch, TransportTracker, make_client; print('OK')"`

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/_probe_lib.py
```

---

## Task 2: Create `probe_access.py`

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/probe_access.py`
- Source: `catalog_probe.py` lines 248-270 (`analyze_anti_bot`), 760-820 (homepage fetch + redirect detection + anti-bot assembly)

- [ ] **Step 1: Create the script**

Structure:
1. PEP 723 block: `httpx`, `selectolax`
2. Module docstring with interpretation notes from spec (transport_health meanings, anti_bot.suspected_empty_shell)
3. `from _probe_lib import log, fetch, find_blocked_keywords, detect_challenge_page, TransportTracker, get_body_text_length, make_client`
4. `analyze_anti_bot()` — extracted from lines 248-270, **without** `product_page_status` and `product_page_accessible` fields
5. `parse_args()` — `--url` (required), `--timeout` (default 15.0), `--delay` (default 0.5), `--max-response-size` (default 2_000_000)
6. `main()`:
   - Fetch homepage via `fetch()`
   - Detect redirects (lines 794-802)
   - Run `analyze_anti_bot()` on homepage HTML
   - Set `cloudflare_ray` from response headers
   - Compute `transport_health` string from `tracker.summary()`
   - Assemble result dict with inline comments per spec Layer 2
   - Print JSON to stdout
   - Exit 0/1/2 per contract

- [ ] **Step 2: Smoke test**

Run: `uv run .claude/skills/catalog-detector/scripts/probe_access.py --url https://www.harlowbros.co.uk`

Verify: JSON output has all fields from spec (`url`, `final_url`, `redirected`, `cross_domain_redirect`, `homepage_status`, `transport_health` as string, `anti_bot` object without `product_page_status`/`product_page_accessible`, `errors` array).

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/probe_access.py
```

---

## Task 3: Create `probe_platform.py`

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/probe_platform.py`
- Source: `catalog_probe.py` lines 161-245 (platform signals + guess), 273-333 (JS rendering + geo hints)

- [ ] **Step 1: Create the script**

Structure:
1. PEP 723 block: `httpx`, `selectolax`
2. Module docstring with interpretation notes from spec (platform_guess meanings, text_to_html_ratio thresholds, platform_conflict handling)
3. Import from `_probe_lib`
4. `PLATFORM_SIGNALS` dict — verbatim from lines 161-173
5. `SIGNAL_TO_PLATFORM` dict — verbatim from lines 176-186
6. `detect_platform_signals()` — verbatim from lines 189-213
7. `guess_platform()` — verbatim from lines 216-245
8. `analyze_js_rendering()` — verbatim from lines 273-311
9. `extract_geo_hints()` — verbatim from lines 314-333
10. `parse_args()` — `--url`, `--timeout`, `--delay`, `--max-response-size`
11. `main()`:
    - Fetch homepage
    - Run `detect_platform_signals()` + `guess_platform()`
    - Run `analyze_js_rendering()` + `extract_geo_hints()`
    - Assemble result dict with inline comments
    - Print JSON, exit 0/1/2

- [ ] **Step 2: Smoke test**

Run: `uv run .claude/skills/catalog-detector/scripts/probe_platform.py --url https://www.harlowbros.co.uk`

Verify: JSON has `platform_guess`, `platform_confidence`, `platform_signal_count`, `platform_conflict`, `platform_version`, `js_rendering_signals`, `geo_hints`, `errors`.

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/probe_platform.py
```

---

## Task 4: Create `probe_discovery.py`

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/probe_discovery.py`
- Source: `catalog_probe.py` lines 344-449 (robots, sitemap, homepage links, sampling), 822-885 (main flow for robots/sitemap/links/json-ld)

- [ ] **Step 1: Create the script**

Structure:
1. PEP 723 block: `httpx`, `selectolax`
2. Module docstring with interpretation notes from spec (sitemap.found meanings, crawl_delay, no_public_catalog detection, json_ld_on_homepage)
3. Import from `_probe_lib` + stdlib `xml.etree.ElementTree`, `urllib.parse`
4. `parse_robots_txt()` — verbatim from lines 344-361
5. `PRODUCT_URL_PATTERNS`, `MAX_SITEMAP_DEPTH`, `MAX_PRODUCT_URLS` — from lines 364-366
6. `parse_sitemap()` — verbatim from lines 369-409
7. `sample_diverse()` — verbatim from lines 412-417
8. `extract_homepage_links()` — verbatim from lines 420-449
9. `guess_url_pattern()` — verbatim from lines 728-742
10. `parse_args()` — `--url`, `--timeout`, `--delay`, `--max-response-size`, `--max-product-samples`
11. `main()`:
    - Fetch homepage (for homepage links + JSON-LD extraction)
    - Fetch robots.txt, parse it
    - Parse sitemaps (from robots.txt or default `/sitemap.xml`)
    - Sample product URLs, check accessibility
    - Extract homepage links
    - Extract JSON-LD types from homepage
    - Assemble result dict with inline comments
    - Print JSON, exit 0/1/2

- [ ] **Step 2: Smoke test**

Run: `uv run .claude/skills/catalog-detector/scripts/probe_discovery.py --url https://www.harlowbros.co.uk`

Verify: JSON has `robots_txt`, `sitemap`, `homepage_links`, `json_ld_on_homepage`, `errors`.

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/probe_discovery.py
```

---

## Task 5: Create `probe_recipe.py`

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/probe_recipe.py`
- Source: `catalog_probe.py` lines 452-742 (knowledgebase parsing, recipe verification, pagination, recipe match computation)

- [ ] **Step 1: Create the script**

Structure:
1. PEP 723 block: `httpx`, `selectolax`
2. Module docstring with interpretation notes from spec (recipe_match meanings — especially the `"poor"` false-negative warning about category page URLs, `"untested"` when no product URLs)
3. Import from `_probe_lib` + `pathlib`, `urllib.parse`
4. `extract_md_section()` — verbatim from lines 452-456
5. `parse_knowledgebase()` — verbatim from lines 459-514
6. `verify_recipe()` — from lines 517-615, **with field renames:**
   - `json_ld_product_found` → `json_ld_found`
   - Add `json_ld_type` field (record actual `@type` value, e.g. `"Product"`)
   - `css_checks[].extracted` → `css_checks[].sample_text`
   - `css_checks[].non_empty` → `css_checks[].found`
   - Drop: `page_truncated`, `body_text_length`, `json_ld_extracted`, `attribute_selectors_tested`
7. `check_pagination()` — from lines 618-694, **simplified output:**
   ```python
   {"tested": bool, "pattern_confirmed": str|null, "next_page_found": bool}
   ```
   Drop: `category_url`, `page1_product_count`, `page2_url`, `page2_status`, `page2_product_count`, `products_differ`
8. `compute_recipe_match()` — from lines 697-725, updated to use new field names (`json_ld_found` instead of `json_ld_product_found`, `css["found"]` instead of `css["non_empty"]`)
9. `parse_args()` — `--url`, `--platform`, `--knowledgebase-dir`, `--product-urls` (optional, comma-separated), `--timeout`, `--delay`, `--max-response-size`
10. `main()`:
    - If `--product-urls` omitted → return `recipe_match: "untested"` with errors entry
    - Load knowledgebase for `--platform`
    - If knowledgebase not found → return `knowledgebase_found: false`, `recipe_match: "untested"`
    - Run `verify_recipe()` on product URLs
    - Run `check_pagination()`
    - Compute `recipe_match`
    - Assemble result dict with inline comments
    - Print JSON, exit 0/1/2

- [ ] **Step 2: Smoke test**

Run: `uv run .claude/skills/catalog-detector/scripts/probe_recipe.py --url https://www.harlowbros.co.uk --platform magento --knowledgebase-dir docs/platform-knowledgebase --product-urls "https://www.harlowbros.co.uk/treated-softwood-railway-sleepers-200mm-x-100mm-2-4m"`

Verify: JSON has `knowledgebase_file`, `knowledgebase_found`, `knowledgebase_selectors_parsed`, `knowledgebase_api_endpoints_parsed`, `recipe_match`, `product_pages_tested`, `checks` (with `json_ld_found`, `json_ld_type`, `css_checks[].found`, `css_checks[].sample_text`), `pagination_check`, `errors`.

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/probe_recipe.py
```

---

## Task 6: Rewrite `catalog_probe.py` as orchestrator

**Files:**
- Rewrite: `.claude/skills/catalog-detector/scripts/catalog_probe.py`

- [ ] **Step 1: Rewrite the script**

The new orchestrator is ~100 lines. It contains NO analysis logic — only subprocess coordination, file I/O, and JSON assembly.

Structure:
1. PEP 723 block: no external dependencies (stdlib only — uses `subprocess`, `json`, `pathlib`, `argparse`)
2. Module docstring explaining orchestrator role
3. `parse_args()` — `--url`, `--slug`, `--knowledgebase-dir`, `--output-dir`
4. `run_script()` helper:
   ```python
   def run_script(script_name: str, args: list[str], output_dir: Path, log_parts: list[str]) -> dict | None:
       """Run a sibling script, save JSON to output_dir, collect stderr. Returns parsed JSON or None."""
       script_path = Path(__file__).parent / script_name
       result = subprocess.run(
           ["uv", "run", str(script_path)] + args,
           capture_output=True, text=True
       )
       log_parts.append(result.stderr)
       if result.returncode == 2:
           return None
       try:
           data = json.loads(result.stdout)
       except json.JSONDecodeError:
           return None
       # Save individual result
       json_name = script_name.replace(".py", ".json")
       (output_dir / json_name).write_text(json.dumps(data, indent=2))
       return data
   ```
5. `RECIPE_RANK` dict — from line 745
6. `main()`:
   - Create `--output-dir`
   - Run `probe_access.py --url {url}` → if `transport_health == "blocked"`, early exit
   - Run `probe_platform.py --url {url}`
   - Run `probe_discovery.py --url {url}`
   - Run `probe_recipe.py` with logic from spec:
     - Extract `sample_product_urls` from discovery result
     - If `platform_conflict == false` and knowledgebase exists → run once for `platform_guess`
     - If `platform_conflict == true` → run per candidate with knowledgebase, keep best
     - If no knowledgebase → skip
   - Assemble flat JSON from all sub-results (top-level merge, recipe under `recipe_verification`)
   - Merge all stderr into `{output-dir}/probe.log`
   - Print assembled JSON to stdout
   - Exit 0/1/2

- [ ] **Step 2: Smoke test end-to-end**

Run:
```bash
uv run .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url https://www.harlowbros.co.uk --slug harlowbros-test \
  --knowledgebase-dir docs/platform-knowledgebase \
  --output-dir docs/catalog-detector/harlowbros-test
```

Verify:
- `docs/catalog-detector/harlowbros-test/probe_access.json` exists
- `docs/catalog-detector/harlowbros-test/probe_platform.json` exists
- `docs/catalog-detector/harlowbros-test/probe_discovery.json` exists
- `docs/catalog-detector/harlowbros-test/probe_recipe.json` exists (magento KB exists)
- `docs/catalog-detector/harlowbros-test/probe.log` exists
- stdout is assembled JSON with all fields

Clean up: `rm -rf docs/catalog-detector/harlowbros-test`

- [ ] **Step 3: Commit**

```
git add .claude/skills/catalog-detector/scripts/catalog_probe.py
```

---

## Task 7: Update `validate_assessment.py`

**Files:**
- Modify: `.claude/skills/catalog-detector/scripts/validate_assessment.py`

- [ ] **Step 1: Add gate docstrings**

Add a docstring to every `check_*` function following the Layer 3 format from the spec:
```python
"""
WHAT IT CHECKS: ...
FAILURE MEANS: ...
HOW TO FIX: ...
"""
```

All 15 gate functions need docstrings (12 success + 3 stop).

- [ ] **Step 2: Add `--output-json` flag**

Modify `main()`:
1. Add `parser.add_argument("--output-json", type=Path, default=None)`
2. After computing result, if `args.output_json`:
   ```python
   args.output_json.parent.mkdir(parents=True, exist_ok=True)
   args.output_json.write_text(json.dumps(result, indent=2))
   ```
3. Still print to stdout as before

- [ ] **Step 3: Smoke test**

Run:
```bash
uv run .claude/skills/catalog-detector/scripts/validate_assessment.py \
  docs/catalog-detector/harlowbros.md \
  --knowledgebase-dir docs/platform-knowledgebase \
  --output-json /tmp/test_validate.json
```

Verify: `/tmp/test_validate.json` exists and matches stdout. Clean up: `rm /tmp/test_validate.json`

- [ ] **Step 4: Commit**

```
git add .claude/skills/catalog-detector/scripts/validate_assessment.py
```

---

## Task 8: Update SKILL.md

**Files:**
- Modify: `.claude/skills/catalog-detector/SKILL.md`

- [ ] **Step 1: Update probe command**

Replace the current probe command (line 36) with:
```
uv run .claude/skills/catalog-detector/scripts/catalog_probe.py --url {site_url} --slug {slug} --knowledgebase-dir docs/platform-knowledgebase --output-dir docs/catalog-detector/{slug}
```

- [ ] **Step 2: Update validate command**

Replace the current validate command (line 52) with:
```
uv run .claude/skills/catalog-detector/scripts/validate_assessment.py docs/catalog-detector/{slug}/assessment.md --knowledgebase-dir docs/platform-knowledgebase --output-json docs/catalog-detector/{slug}/validate.json 2>docs/catalog-detector/{slug}/validate.log
```

- [ ] **Step 3: Update routing conditions**

In the routing logic (lines 38-48):
- `transport_health.overall is "healthy"` → `transport_health is "healthy"`
- `docs/catalog-detector/{slug}.md` → `docs/catalog-detector/{slug}/assessment.md`
- Remove references to `{slug}_probe_stderr.log` and `{slug}_validate_stderr.log`

- [ ] **Step 4: Update file locations table**

```
| Catalog assessment (output) | `docs/catalog-detector/{slug}/assessment.md` |
```

- [ ] **Step 5: Commit**

```
git add .claude/skills/catalog-detector/SKILL.md
```

---

## Verification

After all tasks, run a full end-to-end test:

```bash
uv run .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url https://www.harlowbros.co.uk --slug harlowbros-verify \
  --knowledgebase-dir docs/platform-knowledgebase \
  --output-dir docs/catalog-detector/harlowbros-verify
```

Check:
1. All 4 probe JSON files written to `docs/catalog-detector/harlowbros-verify/`
2. `probe.log` written
3. Assembled JSON on stdout has correct structure
4. `transport_health` is a string, not a dict
5. No `product_page_status` or `product_page_accessible` in `anti_bot`
6. `recipe_verification.checks[].json_ld_found` (not `json_ld_product_found`)
7. `recipe_verification.checks[].css_checks[].found` and `.sample_text` (not `.non_empty` and `.extracted`)

Clean up: `rm -rf docs/catalog-detector/harlowbros-verify`
