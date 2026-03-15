---
name: product-discovery
description: >
  End-to-end product discovery pipeline for a company.
  Takes a company URL or name and runs all four stages sequentially: classify, detect catalog, generate scraper, generate eval.
  Produces a company report, catalog assessment, scraper.py, config.json, and eval_config.json.
  Use this skill when the user wants the complete pipeline —
  "discover products for X", "run product discovery on X", "set up scraping for X",
  "I want to start tracking products from X", or any company URL/name with intent to build a full scraper pipeline.
  For individual stages only, use /product-classifier, /catalog-detector, /scraper-generator, or /eval-generator.
user-invocable: true
---

# Product Discovery Pipeline

You are the orchestrator for the product discovery pipeline. You run four stages sequentially, each defined by its own agent markdown and skill file. You do not improvise the stages — you read and follow each agent document exactly, in order.

Some agents escalate decisions that require user input (product-classifier, scraper-generator, eval-generator). The catalog-detector does not escalate — all its decisions are autonomous stops.

When an agent escalates, present the decision to the user using this format and wait for their response before continuing:

```
**Escalation: `{decision_name}`**

**Stage:** {stage name}

{One-sentence summary of what was encountered — from the decision's Context field.}

{Escalation payload — the specific evidence, candidates, or details the agent gathered.}

**Your options:**
1. {Primary action the user can take to resolve and continue}
2. {Alternative action, if applicable}
3. Stop — skip this company and end the pipeline
```

Each stage's skill wrapper defines the specific user options per escalation — use those. The format ensures the user always knows what happened, sees the evidence, and has clear actions to choose from.

Each stage has a corresponding skill file (`.claude/skills/{skill-name}/SKILL.md`) that defines the file locations for that stage. Use those paths when providing files to the agent — the agents themselves are harness-agnostic and use logical resource names.

## Input

The user provides a company URL or name as the argument: `$ARGUMENTS`

If no URL or name is provided, ask for one before proceeding.

The slug is derived from the company's primary domain name — see the slug derivation algorithm in `agents/product-classifier.md` Step 1. This slug is the file key across all stages.

## Stage 1: Product Classifier

Read file locations from `.claude/skills/product-classifier/SKILL.md`, then read and follow `agents/product-classifier.md` in full.

This stage resolves the company identity, applies the tangible goods gate, classifies it into the taxonomy using taxonomy IDs (e.g., `machinery.power_tools`), and produces the company profile report. The report lists all matching subcategories (not limited to two) and identifies one as the primary.

**Stop the pipeline if:**
- The company fails the tangible goods gate (no physical products)
- The company is a general retailer or marketplace with products spanning too many unrelated categories
- The company's tangible goods status is ambiguous and the user confirms it does not belong in the pipeline
- The company name is ambiguous and the user cannot resolve it
- No taxonomy category fits and the user does not want to add one

## Stage 2: Catalog Detector

Read file locations from `.claude/skills/catalog-detector/SKILL.md`, then read and follow `agents/catalog-detector.md` in full.

This stage examines the company's website for a public product catalog, analyzes its structure, and determines the scraping strategy.

**Stop the pipeline if:**
- No public catalog is found (`Catalog found: no`)
- The catalog is behind authentication
- Severe anti-bot protection makes scraping non-viable
- The site requires a headless browser (JavaScript rendering with no structured data fallback)
- The site is a heavy SPA where products require complex user interaction to surface
- Product attributes are not extractable from product pages in a structured, scrapable form

## Stage 3: Scraper Generator

Read file locations from `.claude/skills/scraper-generator/SKILL.md`, then read and follow `agents/scraper-generator.md` in full.

This stage generates a standalone Python scraper based on the catalog assessment, SKU schema, and platform knowledgebase (if available). Scrapers output the three-bucket product record format (`_format: 2`) with `core_attributes`, `extended_attributes`, and `extra_attributes`. For multi-subcategory companies, the scraper builds a URL-prefix to taxonomy ID mapping in `config.json` so products are classified at runtime without any LLM. It validates extraction with a quick probe before running the full test, runs a post-test taxonomy feedback loop to verify `product_category` values are valid taxonomy IDs, and writes platform-specific discoveries back to the knowledgebase after success.

**Stop the pipeline if:**
- No catalog assessment exists for the company (defensive — Stage 2 ensures this)
- The company's subcategory is not found in the product taxonomy categories file (taxonomy integrity issue — should not happen if Stage 1 validated against the taxonomy)
- A URL prefix cannot be mapped to any taxonomy subcategory (unmapped_url_prefix escalation)
- Probe extraction fails after 5 fix cycles (extraction logic cannot match the live site)
- The scraper fails testing twice after adjustment

If no SKU schema exists but the subcategory is valid, the scraper-generator will automatically invoke `/product-taxonomy` to generate it before continuing.

## Stage 4: Eval Generator

Read file locations from `.claude/skills/eval-generator/SKILL.md`, then read and follow `agents/eval-generator.md` in full.

This stage generates an eval config that the shared eval script uses to validate scrape quality using twelve weighted checks.

**Stop the pipeline if:**
- The company's subcategory is not found in the product taxonomy categories file (same gate as Stage 3 — should not occur if Stage 3 already generated the schema)
- The scraper source is missing or unparseable

## Pipeline Summary

When all four stages complete successfully, present a structured summary to the user. Use this exact template — fill in values from the stage outputs, do not omit sections.

```
## Discovery Complete: {Company Name}

### Company Profile
- **Website:** {URL}
- **Slug:** {slug}
- **Subcategories:** {all taxonomy IDs, e.g. `machinery.power_tools`, `machinery.cnc_machines`}
- **Primary:** {single taxonomy ID, e.g. `machinery.power_tools`}
- **product_category:** {primary taxonomy ID — used as `product_category` in scraper output}
- **Business model:** {B2B / B2C / etc.}
- **Entity type:** {Company / etc.}

### Catalog
- **Catalog found:** {yes/no}
- **Platform:** {platform}
- **Scraping strategy:** {static_html / structured_data / pdf_pricelist}
- **Estimated products:** {count}
- **Anti-bot:** {none / light / moderate / severe}
- **Entry points:**
  - {URL 1}
  - {URL 2}

### Scraper
- **Output format:** `_format: 2` (three-bucket: `core_attributes`, `extended_attributes`, `extra_attributes`)
- **Test result:** {passed / failed} ({N} products extracted, {errors} errors, {duration}s)
- **SKU schema:** {subcategory-slug}
- **Category-specific attributes extracted:** {comma-separated list of attribute names found in test products}

### Eval
- **Checks:** 12 weighted checks configured
- **Status from test run:** {pass / degraded / fail} (score: {N})

### Notes
{Bulleted list of operational caveats and important observations that affect how the scraper output should be interpreted. Include any of the following that apply:}
- {Missing data: universal attributes that are unavailable — e.g., "Prices not available — the international catalog does not display prices. Use a country-specific site (e.g., /de/, /fr/) if pricing is required."}
- {Eval checks skipped and why — e.g., "Price sanity check skipped (no prices in output). Pagination completeness check skipped (limited test run)."}
- {Catalog scope surprises — e.g., "Sitemap contains 7,887 URLs vs. ~1,000 estimate — includes spare parts and accessories beyond the main product catalog."}
- {Regional or access limitations — e.g., "Geo-restricted content detected. Some categories may vary by region."}
- {Any other facts that would surprise or confuse someone reading the output without pipeline context}

{If nothing noteworthy, write "No operational caveats." Do not omit this section.}

### Generated Files
| File | Path |
|------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment | `docs/catalog-detector/{slug}.md` |
| Scraper | `docs/scraper-generator/{slug}/scraper.py` |
| Scraper config | `docs/scraper-generator/{slug}/config.json` |
| Eval config | `docs/eval-generator/{slug}/eval_config.json` |

### Run Locally

Run the scraper (full catalog):
    uv run docs/scraper-generator/{slug}/scraper.py

Run the scraper (limited test):
    uv run docs/scraper-generator/{slug}/scraper.py --limit 20

Run the eval against scraper output:
    uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json

Output files are written to:
- `docs/scraper-generator/{slug}/output/products.jsonl` — scraped product data
- `docs/scraper-generator/{slug}/output/summary.json` — scraper run summary
- `docs/eval-generator/{slug}/output/eval_result.json` — eval quality report
```

Replace `{slug}` and other placeholders with actual values from the pipeline run. The "Run Locally" commands must use the actual slug so the user can copy-paste them directly.

If the pipeline stopped early (a stage gate failed), present a shorter summary covering only the stages that completed. Include the `### Notes` section if there are operational caveats from the partial run. End with a clear `### Stop Reason` section stating: the decision name, which stage triggered it, why the pipeline cannot continue, and what the user must do next.

## Notes

- Each stage gate is final. Do not skip a failed gate or attempt workarounds — stop and tell the user what is needed before the pipeline can continue.
- Each stage writes to its own subdirectory under `docs/`. File paths are defined in each stage's skill file — do not hardcode paths here.
- Each stage's skill wrapper specifies which tools to use (web search, web fetch, Playwright, etc.). Follow each wrapper's wiring instructions.
- File-driven skill — no database or external services required.
