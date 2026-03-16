---
name: product-classifier
description: >
  Research and classify a company's physical products into the project taxonomy.
  Produces a company profile report with classification, product lines, and preliminary catalog analysis.
  Use this skill whenever the user provides a company name or URL for investigation — "research this company",
  "what does X make", "classify this company", "look up [company name]", "what products does X sell",
  or any company name/URL given with intent to understand what physical goods a company offers.
  Also trigger when the user pastes a company URL without further context.
  If the user wants the full pipeline (classify + detect catalog + generate scraper + eval), use /product-discovery instead.
user-invocable: true
---

# Product Classifier

Research and classify a company's physical products into the project taxonomy, producing a company profile report.

## Input

`$ARGUMENTS` is a company URL or company name.

## File locations

| Resource | Path |
|----------|------|
| Product taxonomy | `docs/product-taxonomy/categories.md` |
| Company reports dir | `docs/product-classifier/` |
| Company report (output) | `docs/product-classifier/{slug}.md` |

## Workflow

Read and follow `references/workflow.md`.

- Provide the file paths from the table above when the workflow references logical resources (e.g., "the product taxonomy categories file", "the company reports directory", "write the company report").
- Use web search, web fetch, and Playwright browser tools to investigate company websites as the workflow directs.
- This skill may stop autonomously without escalation — if the company fails the tangible goods gate or is rejected as a general retailer/marketplace. In these cases the workflow produces no report. Report the outcome to the user.

## Escalation handling

When the workflow reaches an escalation point, present it to the user using this format and **wait for their response** before continuing:

```
**Escalation: `{decision_name}`**
**Stage:** Product Classifier
{One-sentence summary — from the decision's Context field.}
{Escalation payload — the specific evidence or candidates the workflow gathered.}
**Your options:**
1. {Action to resolve and continue}
2. {Alternative action, if applicable}
3. Stop — skip this company and end the pipeline
```

User options per escalation:

- `ambiguous_company` — 1) Pick a candidate by name or number, 2) Provide additional context to narrow the search, 3) Stop
- `tangible_ambiguous` — 1) Include the company and proceed with classification, 2) Exclude the company and stop the pipeline, 3) Stop
- `category_not_found` — 1) Suggest a new subcategory to add to the taxonomy, 2) Stop

## Notes

File-driven skill — no database or external services required.
