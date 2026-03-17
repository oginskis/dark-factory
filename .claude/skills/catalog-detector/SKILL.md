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
| Catalog assessment (output) | `docs/catalog-detector/{slug}.md` |
| Platform knowledgebase (read+write) | `docs/platform-knowledgebase/{platform-slug}.md` |

The platform knowledgebase is both read and written by this skill. For known platforms, it is loaded as the primary extraction recipe. After every successful run, the knowledgebase is updated with site-specific findings. For newly identified platforms on the deep investigation path, a new knowledgebase file is created.

## Workflow

Read and follow `references/workflow.md`.

- Read the company report first for the company URL, categories, and business model context.
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "write the catalog assessment report", "the platform knowledgebase").
- Use web search, web fetch, and Playwright browser tools to investigate catalog pages as the workflow directs.
- This skill does not escalate — all decisions are autonomous stops or track switches. If the workflow determines scraping is not viable (`no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, or `attributes_not_extractable`), it writes a minimal catalog assessment and stops. If the fast-path recipe verification fails (`platform_recipe_failed`), the workflow autonomously switches to the deep investigation path. Report the outcome to the user.
- The platform knowledgebase may not exist for platforms not yet encountered. On the fast path, a missing knowledgebase file means the platform is treated as unknown (deep investigation). On the deep investigation path, a new knowledgebase file is created if the platform is identifiable.

## Notes

Owns the platform knowledgebase — reads on every run, writes on every successful run.
