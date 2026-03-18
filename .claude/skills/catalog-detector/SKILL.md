---
name: catalog-detector
description: >
  Detect whether a company has a public product catalog and produce a concrete extraction blueprint for the scraper-generator.
  Produces a catalog assessment with verified selectors, API endpoints, category tree, and platform-specific extraction recipe.
  Use this skill when the user wants to check catalog availability or scrapability for a company that already has a company report from /product-classifier —
  "check if X has a catalog", "detect pricelist for X", "what scraping strategy for X", "can we scrape X",
  "does X have a public product listing". Requires a company report from /product-classifier to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Catalog Detector

Produce a concrete extraction blueprint that the scraper-generator can translate directly into code, leveraging platform-specific knowledge to minimize downstream investigation.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment (output) | `docs/catalog-detector/{slug}/assessment.md` |
| Platform knowledgebase (read+write) | `docs/platform-knowledgebase/{platform-slug}.md` |

The platform knowledgebase is both read and written by this skill. For known platforms, it is loaded as the primary extraction recipe. After every successful run, the knowledgebase is updated with site-specific findings. For newly identified platforms on the deep investigation path, a new knowledgebase file is created.

## Workflow

Read and follow `references/workflow.md`.

- **Archive previous run:** Before starting, check if `docs/catalog-detector/{slug}/` exists. If it does, archive it: `mv docs/catalog-detector/{slug} docs/catalog-detector/{slug}-archived-$(date -u +%Y%m%dT%H%M%S)`. Then create the fresh directory: `mkdir -p docs/catalog-detector/{slug}`. Every invocation generates from scratch — never read from or make decisions based on archived directories (`{slug}-archived-*`).
- Before starting the workflow, run the catalog probe script:
  `uv run .claude/skills/catalog-detector/scripts/catalog_probe.py --url {site_url} --slug {slug} --knowledgebase-dir docs/platform-knowledgebase --output-dir docs/catalog-detector/{slug}`
  Parse stdout as JSON. Individual probe results are saved as JSON files in the output directory. Read `docs/catalog-detector/{slug}/probe.log` for diagnostics if needed.
  - Exit code 0 or 1: use the probe results to inform Steps 1-3. Routing logic:
    - If recipe_match is "full" AND transport_health is "healthy" AND anti_bot shows no blocking AND js_rendering_signals show no SPA framework:
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
  `uv run .claude/skills/catalog-detector/scripts/validate_assessment.py docs/catalog-detector/{slug}/assessment.md --knowledgebase-dir docs/platform-knowledgebase --output-json docs/catalog-detector/{slug}/validate.json 2>docs/catalog-detector/{slug}/validate.log`
  Fix any failing gates. DO NOT modify the validation script.
- **These scripts are infrastructure, not generated code. Never edit, patch, or fix them during a pipeline run — even if you can identify the bug. If a script fails (exit code 2) or produces unexpected results, fall back to manual reasoning for those steps. Record the issue in the catalog assessment's Platform-Specific Notes so it can be fixed in a dedicated maintenance pass. Editing scripts mid-pipeline risks introducing regressions that affect other companies.**
- Read the company report first for the company URL, categories, and business model context.
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "write the catalog assessment report", "the platform knowledgebase").
- Use web search, web fetch, and Playwright browser tools to investigate catalog pages as the workflow directs.
- This skill does not escalate — all decisions are autonomous stops or track switches. If the workflow determines scraping is not viable (`no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, or `attributes_not_extractable`), it writes a minimal catalog assessment and stops. If the fast-path recipe verification fails (`platform_recipe_failed`), the workflow autonomously switches to the deep investigation path. Report the outcome to the user.
- The platform knowledgebase may not exist for platforms not yet encountered. On the fast path, a missing knowledgebase file means the platform is treated as unknown (deep investigation). On the deep investigation path, a new knowledgebase file is created if the platform is identifiable.

## Notes

Owns the platform knowledgebase — reads on every run, writes on every successful run.
