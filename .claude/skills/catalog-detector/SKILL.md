---
name: catalog-detector
description: >
  Detect whether a company has a public product catalog and determine the best scraping strategy.
  Produces a catalog assessment report with site structure, pagination patterns, anti-bot measures, and recommended scraping approach.
  Use this skill when the user wants to check catalog availability or scrapability for a company that has already been classified —
  "check if X has a catalog", "detect pricelist for X", "what scraping strategy for X", "can we scrape X",
  "does X have a public product listing". Requires a company report from /product-classifier to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Catalog Detector

Read and follow the agent instructions in `agents/catalog-detector.md`.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment (output) | `docs/catalog-detector/{slug}.md` |
| Platform knowledgebase | `docs/platform-knowledgebase/{platform-slug}.md` |

## Role in the four-level product record

The catalog-detector determines whether a site can support the four-level product record format (see scraper-generator skill for the canonical definition). Specifically, Step 5 (Product Attribute Extractability Check) verifies that the catalog exposes enough structured data to support at least the universal top-level fields and core attributes. A site that only shows product names and images — without structured specs — cannot produce meaningful core_attributes and is stopped via `attributes_not_extractable`.

## Claude Code wiring

- Read the company report first for the company URL, categories, and business model context.
- Provide the file paths from the table above when the agent references logical resources (e.g., "the company report", "write the catalog assessment report", "the platform knowledgebase").
- Use web search, web fetch, and Playwright browser tools to investigate catalog pages as the agent directs.
- This agent does not escalate — all decisions are autonomous stops. If the agent determines scraping is not viable (`no_public_catalog`, `auth_required`, `anti_bot_severe`, `requires_headless_browser`, `spa_not_scrapable`, or `attributes_not_extractable`), it writes a minimal catalog assessment and stops. Report the outcome to the user.
- Reading the platform knowledgebase is optional — the file may not exist for platforms not yet encountered. If it does not exist, proceed without it.

## Notes

File-driven skill — no database or external services required.
