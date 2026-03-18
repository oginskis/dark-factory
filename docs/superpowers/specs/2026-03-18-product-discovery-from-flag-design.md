# Product Discovery `--from` Flag

**Date:** 2026-03-18
**Status:** Approved

## Problem

`/product-discovery` always runs all four stages (classify, detect, scrape, eval) from the beginning. When the company report and catalog assessment already exist and only the scraper needs regeneration + re-evaluation, stages 1 and 2 are wasted time and tokens. Individual skills can be called separately, but there's no way to say "start from this stage and run everything downstream."

## Solution

Add an optional `--from {stage}` flag to `/product-discovery` that skips stages before the specified one and runs from that stage through to the end. A data-driven prerequisite validation script ensures all upstream outputs exist before allowing the skip.

## Usage

```
/product-discovery harlowbros                            # full pipeline (default)
/product-discovery harlowbros --from catalog-detector    # stages 2, 3, 4
/product-discovery harlowbros --from scraper-generator   # stages 3, 4
/product-discovery harlowbros --from eval-generator      # stage 4 only
```

`--from` can appear before or after the company name — both orderings are supported.

`--from product-classifier` is valid but equivalent to the full pipeline (no prerequisites to check). Log a note: "Note: `--from product-classifier` runs the full pipeline."

## Argument Parsing

Scan `$ARGUMENTS` for the `--from` token. If found, consume the next token as the stage name. Everything remaining (regardless of position) is the company slug or URL.

**Stage name validation:** The stage name must be one of: `product-classifier`, `catalog-detector`, `scraper-generator`, `eval-generator`. If it doesn't match, reject with a clear error listing valid options.

When `--from` skips Stage 1 (product-classifier), the slug must still be derived before anything else. If the input looks like a bare word with no dots or slashes, check whether `docs/product-classifier/{input}.md` exists and treat it as a slug directly. Otherwise, run `derive_slug.py` with the URL to get the slug. Pass the slug to the prerequisite check and all downstream stage invocations.

## Stage Order

```
1. product-classifier
2. catalog-detector
3. scraper-generator
4. eval-generator
```

`--from` skips all stages before the specified one. Downstream stages always run.

## Prerequisite Validation

### Data-driven approach

The validation script does **not** hardcode the prerequisite map. Instead, it reads each upstream stage's SKILL.md "File locations" table at runtime and checks that all non-output files exist for the target slug. This makes the SKILL.md files the single source of truth — when a stage adds a new input file, the prerequisite checker picks it up automatically.

**How it works:**
1. Determine which stages are upstream of `--from` (e.g., for `--from eval-generator`, upstream stages are product-classifier, catalog-detector, scraper-generator).
2. For the target stage, parse its SKILL.md "File locations" table.
3. Extract paths that are inputs (not marked as `(output)`) and that contain `{slug}`.
4. Substitute `{slug}` with the actual slug and check file existence.
5. For data files (`products.jsonl`, `summary.json`), additionally verify the file is non-empty (`os.path.getsize > 0`).

**Fallback prerequisite map** (for reference — the script derives this from SKILL.md, not from a hardcoded table):

| Starting from | Required files |
|---|---|
| `catalog-detector` | `docs/product-classifier/{slug}.md` |
| `scraper-generator` | `docs/product-classifier/{slug}.md`, `docs/catalog-detector/{slug}/assessment.md` |
| `eval-generator` | `docs/product-classifier/{slug}.md`, `docs/catalog-detector/{slug}/assessment.md`, `docs/scraper-generator/{slug}/scraper.py`, `docs/scraper-generator/{slug}/config.json`, `docs/scraper-generator/{slug}/output/products.jsonl`, `docs/scraper-generator/{slug}/output/summary.json` |

When any prerequisite is missing, the skill escalates immediately — shows the user what's missing and which stage to run first. Does not attempt to auto-run the missing stage. When multiple files are missing, the `missing` list is ordered by pipeline stage so the user knows which to fix first.

## Validation Script

**File:** `.claude/skills/product-discovery/scripts/check_prerequisites.py`

**Interface:**
```bash
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from scraper-generator --slug harlowbros
```

**Output:** JSON to stdout:
```json
{
  "stage": "scraper-generator",
  "slug": "harlowbros",
  "status": "pass",
  "missing": []
}
```

On failure:
```json
{
  "stage": "scraper-generator",
  "slug": "harlowbros",
  "status": "fail",
  "missing": [
    {
      "path": "docs/catalog-detector/harlowbros/assessment.md",
      "fix": "/catalog-detector harlowbros"
    }
  ]
}
```

The script parses SKILL.md "File locations" tables to determine required files, then checks existence (and non-emptiness for data files). Finds the repo root by walking up from the script location looking for `.claude/skills/`. For `--from product-classifier`, returns `{"status": "pass", "missing": []}` (no prerequisites).

**Conventions:**
- PEP 723 inline metadata at top (no external dependencies needed — only stdlib)
- Exit code 0 on success, non-zero on argument errors
- JSON output to stdout only

**Test file:** `.claude/skills/product-discovery/tests/test_check_prerequisites.py` (per repo conventions).

## SKILL.md Changes

### 1. New "Arguments" section (before Stage 1)

Describes `--from {stage}` parsing from `$ARGUMENTS`. Valid values match skill names: `product-classifier`, `catalog-detector`, `scraper-generator`, `eval-generator`. Invalid stage names are rejected with a clear error listing valid options.

When `--from` is provided, run the prerequisite check script. If status is `fail`, present each missing file as an escalation and stop. If status is `pass`, skip to the specified stage.

### 2. Stage skip guards

Each stage section (1-4) gets a one-line guard:

> **Skip this stage if `--from` specifies a later stage.**

### 3. Pipeline summary for partial runs

A `--from` run that completes successfully still shows the full pipeline summary, reading values from existing output files to populate sections for skipped stages. Annotate skipped sections with "(from prior run)" so the user knows which data is fresh vs cached.

If a `--from` run stops early (a downstream stage fails), it follows the same early-stop summary behavior as full pipeline runs — shorter summary covering only completed stages, with a `### Stop Reason` section.

### 4. Orthogonal to fix mode

`--from` does not interact with scraper-generator's fix mode (invoked by `/scraper-remediation`). They are independent features.

## Archive Behavior

Each downstream stage archives its own output directory before starting (e.g., scraper-generator moves `docs/scraper-generator/{slug}/` to `docs/scraper-generator/{slug}-archived-{timestamp}/`). This is existing behavior inherited from each stage's skill — `--from` does not change it.

**Known trade-off:** If a stage archives its previous output and then fails, the previous working artifacts are in the archived directory, not at the active path. The user can recover by renaming the archived directory back. This is the same behavior as running the stage individually — `--from` does not make it worse, but users should be aware that re-running a stage replaces previous output regardless of success.

## Limitations

- **No staleness detection.** The prerequisite check validates file existence and non-emptiness only. It does not verify file freshness, content validity, or consistency between upstream files (e.g., that the catalog assessment matches the current company report). Users who suspect upstream files are stale should run the full pipeline without `--from`.
- **No file locking.** If upstream files are modified during a `--from` run, the pipeline may read inconsistent data.
- **Overwrite on re-run.** Each stage that runs will archive and replace its previous output, same as a standalone invocation.

## Files Changed

| File | Change |
|---|---|
| `.claude/skills/product-discovery/SKILL.md` | Add Arguments section, stage skip guards, partial-run summary guidance |
| `.claude/skills/product-discovery/scripts/check_prerequisites.py` | New — data-driven prerequisite validation script |
| `.claude/skills/product-discovery/tests/test_check_prerequisites.py` | New — tests for the validation script |
