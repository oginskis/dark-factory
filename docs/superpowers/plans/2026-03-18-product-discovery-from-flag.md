# Product Discovery `--from` Flag Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `--from {stage}` flag to `/product-discovery` that skips earlier pipeline stages and validates prerequisites using a data-driven script that reads SKILL.md tables.

**Architecture:** A new Python script (`check_prerequisites.py`) parses the target stage's SKILL.md "File locations" table at runtime to determine which upstream files must exist. The product-discovery SKILL.md gets an "Arguments" section for `--from` parsing and stage skip guards. No hardcoded prerequisite map — SKILL.md files are the single source of truth.

**Tech Stack:** Python 3.10+ (stdlib only), pytest for tests, markdown table parsing via regex.

**Spec:** `docs/superpowers/specs/2026-03-18-product-discovery-from-flag-design.md`

---

### Task 1: Create the SKILL.md table parser module

**Files:**
- Create: `.claude/skills/product-discovery/scripts/check_prerequisites.py`

This task builds the core parsing function that reads a SKILL.md file, extracts its "File locations" table, and returns the list of prerequisite paths for a given slug.

- [ ] **Step 0: Create directories**

```bash
mkdir -p .claude/skills/product-discovery/scripts
mkdir -p .claude/skills/product-discovery/tests
```

- [ ] **Step 1: Create the script file with PEP 723 metadata and imports**

```python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Check that prerequisite files exist before running a pipeline stage with --from.

Parses each stage's SKILL.md "File locations" table at runtime to determine
which upstream files must exist. This makes SKILL.md the single source of truth —
no hardcoded prerequisite map.

Usage:
    python check_prerequisites.py --from scraper-generator --slug harlowbros
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
```

- [ ] **Step 2: Add repo root finder and constants**

```python
def find_repo_root() -> Path:
    """Walk up from script location to find repo root."""
    path = Path(__file__).resolve().parent
    for _ in range(10):
        if (path / ".claude" / "skills").is_dir():
            return path
        path = path.parent
    raise RuntimeError("Cannot find repo root")


REPO_ROOT = find_repo_root()

STAGE_ORDER = [
    "product-classifier",
    "catalog-detector",
    "scraper-generator",
    "eval-generator",
]

# Data files that must be non-empty (not just exist)
NON_EMPTY_SUFFIXES = (".jsonl", ".json")
```

- [ ] **Step 3: Add the SKILL.md table parser function**

```python
def parse_file_locations(skill_md_path: Path) -> list[dict[str, str]]:
    """Parse the 'File locations' table from a SKILL.md file.

    Returns a list of dicts with 'resource' and 'path' keys.
    """
    content = skill_md_path.read_text(encoding="utf-8")

    # Find the File locations table — look for header row with Resource | Path
    table_pattern = re.compile(
        r"^\| Resource \| Path \|\n\|[-| ]+\|\n((?:\|.*\|\n?)+)",
        re.MULTILINE,
    )
    match = table_pattern.search(content)
    if not match:
        return []

    rows = []
    for line in match.group(1).strip().split("\n"):
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) >= 2:
            rows.append({"resource": cells[0], "path": cells[1]})
    return rows
```

- [ ] **Step 4: Add the prerequisite extraction function**

```python
def get_required_files(stage: str, slug: str) -> list[dict[str, str]]:
    """Get the list of prerequisite files for a stage, resolved for the given slug.

    Reads the target stage's SKILL.md, filters to input files that contain {slug},
    substitutes the slug, and returns paths to check.

    Returns list of dicts: {"path": "resolved/path", "fix": "/skill-name slug"}
    """
    skill_md = REPO_ROOT / ".claude" / "skills" / stage / "SKILL.md"
    if not skill_md.exists():
        return []

    rows = parse_file_locations(skill_md)
    required = []

    for row in rows:
        resource = row["resource"]
        path_template = row["path"].strip("`")

        # Skip output files — convention: resource name ends with "(output)"
        if resource.rstrip().endswith("(output)"):
            continue

        # Skip paths that don't contain {slug} — these are shared repo files
        # (e.g., categories.md, eval.py) that always exist, not per-company prerequisites
        if "{slug}" not in path_template:
            continue

        # Skip directory paths
        if path_template.endswith("/"):
            continue

        # Substitute {slug}
        resolved = path_template.replace("{slug}", slug)

        # Skip if unresolvable placeholders remain (e.g., {category-slug}, {platform-slug})
        if "{" in resolved:
            continue

        # Determine which skill can produce this file
        fix = _suggest_fix(resolved, slug)
        required.append({"path": resolved, "fix": fix})

    return required


def _suggest_fix(path: str, slug: str) -> str:
    """Suggest which skill to run to produce a missing file."""
    if path.startswith("docs/product-classifier/"):
        return f"/product-classifier {slug}"
    if path.startswith("docs/catalog-detector/"):
        return f"/catalog-detector {slug}"
    if path.startswith("docs/scraper-generator/"):
        return f"/scraper-generator {slug}"
    if path.startswith("docs/eval-generator/"):
        return f"/eval-generator {slug}"
    return f"/product-discovery {slug}"
```

- [ ] **Step 5: Add the main check function and CLI entry point**

```python
def check_prerequisites(stage: str, slug: str) -> dict:
    """Check all prerequisites for a stage and return structured result."""
    if stage not in STAGE_ORDER:
        return {
            "stage": stage,
            "slug": slug,
            "status": "error",
            "message": f"Invalid stage '{stage}'. Valid stages: {', '.join(STAGE_ORDER)}",
            "missing": [],
        }

    # product-classifier is stage 1 — no prerequisites
    if stage == "product-classifier":
        return {"stage": stage, "slug": slug, "status": "pass", "missing": []}

    required = get_required_files(stage, slug)
    missing = []

    for req in required:
        full_path = REPO_ROOT / req["path"]
        if not full_path.exists():
            missing.append(req)
        elif req["path"].endswith(NON_EMPTY_SUFFIXES) and os.path.getsize(full_path) == 0:
            missing.append({"path": req["path"], "fix": req["fix"]})

    # Order missing files by pipeline stage (product-classifier first, then catalog-detector, etc.)
    stage_order_map = {prefix: i for i, prefix in enumerate([
        "docs/product-classifier/",
        "docs/catalog-detector/",
        "docs/scraper-generator/",
        "docs/eval-generator/",
    ])}

    def sort_key(item: dict) -> int:
        for prefix, order in stage_order_map.items():
            if item["path"].startswith(prefix):
                return order
        return 99

    missing.sort(key=sort_key)

    return {
        "stage": stage,
        "slug": slug,
        "status": "fail" if missing else "pass",
        "missing": missing,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Check pipeline prerequisites for --from")
    parser.add_argument("--from", dest="from_stage", required=True,
                        help="Stage to start from")
    parser.add_argument("--slug", required=True, help="Company slug")
    args = parser.parse_args()

    result = check_prerequisites(args.from_stage, args.slug)
    print(json.dumps(result, indent=2))

    if result["status"] == "error":
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Verify the script runs without errors**

Run: `uv run .claude/skills/product-discovery/scripts/check_prerequisites.py --from scraper-generator --slug harlowbros`

Expected: JSON output with `"status": "pass"` or `"status": "fail"` depending on whether harlowbros files exist.

---

### Task 2: Write tests for check_prerequisites.py

**Files:**
- Create: `.claude/skills/product-discovery/tests/test_check_prerequisites.py`

- [ ] **Step 1: Create the test file with PEP 723 metadata and imports**

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for check_prerequisites.py — SKILL.md table parsing and prerequisite validation."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from check_prerequisites import (
    check_prerequisites,
    get_required_files,
    parse_file_locations,
    STAGE_ORDER,
)
```

- [ ] **Step 2: Write tests for parse_file_locations**

```python
class TestParseFileLocations:
    def test_parses_standard_table(self, tmp_path):
        skill_md = tmp_path / "SKILL.md"
        skill_md.write_text(
            "# My Skill\n\n"
            "## File locations\n\n"
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Scraper (output) | `docs/scraper-generator/{slug}/scraper.py` |\n"
        )
        rows = parse_file_locations(skill_md)
        assert len(rows) == 2
        assert rows[0]["resource"] == "Company report"
        assert rows[0]["path"] == "`docs/product-classifier/{slug}.md`"
        assert rows[1]["resource"] == "Scraper (output)"

    def test_returns_empty_for_no_table(self, tmp_path):
        skill_md = tmp_path / "SKILL.md"
        skill_md.write_text("# My Skill\n\nNo table here.\n")
        rows = parse_file_locations(skill_md)
        assert rows == []
```

- [ ] **Step 3: Write tests for get_required_files**

```python
class TestGetRequiredFiles:
    def test_filters_output_files(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "test-stage" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Result (output) | `docs/test-stage/{slug}/result.json` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            files = get_required_files("test-stage", "acme")
        assert len(files) == 1
        assert files[0]["path"] == "docs/product-classifier/acme.md"

    def test_output_filter_uses_endswith_not_contains(self, tmp_path):
        """'Scrape output (products)' is NOT an output — only 'X (output)' is."""
        skill_md = tmp_path / ".claude" / "skills" / "test-stage" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Scrape output (products) | `docs/scraper-generator/{slug}/output/products.jsonl` |\n"
            "| Eval config (output) | `docs/eval-generator/{slug}/eval_config.json` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            files = get_required_files("test-stage", "acme")
        # "Scrape output (products)" should be included (not an output marker)
        # "Eval config (output)" should be excluded (ends with "(output)")
        assert len(files) == 1
        assert files[0]["path"] == "docs/scraper-generator/acme/output/products.jsonl"

    def test_skips_paths_without_slug_placeholder(self, tmp_path):
        """Shared repo files like categories.md are not per-company prerequisites."""
        skill_md = tmp_path / ".claude" / "skills" / "test-stage" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Taxonomy | `docs/product-taxonomy/categories.md` |\n"
            "| Eval script | `eval/eval.py` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            files = get_required_files("test-stage", "acme")
        assert len(files) == 1
        assert files[0]["path"] == "docs/product-classifier/acme.md"

    def test_skips_unresolvable_placeholders(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "test-stage" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| SKU schema | `docs/product-taxonomy/sku-schemas/{category-slug}.md` |\n"
            "| Platform KB | `docs/platform-knowledgebase/{platform-slug}.md` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            files = get_required_files("test-stage", "acme")
        assert len(files) == 1
        assert files[0]["path"] == "docs/product-classifier/acme.md"

    def test_fix_suggestion_matches_producing_stage(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "test-stage" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Assessment | `docs/catalog-detector/{slug}/assessment.md` |\n"
            "| Scraper | `docs/scraper-generator/{slug}/scraper.py` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            files = get_required_files("test-stage", "acme")
        assert files[0]["fix"] == "/product-classifier acme"
        assert files[1]["fix"] == "/catalog-detector acme"
        assert files[2]["fix"] == "/scraper-generator acme"
```

- [ ] **Step 4: Write tests for check_prerequisites**

```python
class TestCheckPrerequisites:
    def test_product_classifier_always_passes(self):
        result = check_prerequisites("product-classifier", "any-slug")
        assert result["status"] == "pass"
        assert result["missing"] == []

    def test_invalid_stage_returns_error(self):
        result = check_prerequisites("invalid-stage", "acme")
        assert result["status"] == "error"
        assert "Invalid stage" in result["message"]

    def test_missing_file_returns_fail(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "catalog-detector" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Assessment (output) | `docs/catalog-detector/{slug}/assessment.md` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            result = check_prerequisites("catalog-detector", "acme")
        assert result["status"] == "fail"
        assert len(result["missing"]) == 1
        assert result["missing"][0]["path"] == "docs/product-classifier/acme.md"

    def test_existing_file_returns_pass(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "catalog-detector" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Assessment (output) | `docs/catalog-detector/{slug}/assessment.md` |\n"
        )
        # Create the prerequisite file
        report = tmp_path / "docs" / "product-classifier" / "acme.md"
        report.parent.mkdir(parents=True)
        report.write_text("# Company Profile: Acme\n")
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            result = check_prerequisites("catalog-detector", "acme")
        assert result["status"] == "pass"
        assert result["missing"] == []

    def test_empty_data_file_returns_fail(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "eval-generator" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Scrape output (products) | `docs/scraper-generator/{slug}/output/products.jsonl` |\n"
        )
        # Create the file but leave it empty
        data_file = tmp_path / "docs" / "scraper-generator" / "acme" / "output" / "products.jsonl"
        data_file.parent.mkdir(parents=True)
        data_file.write_text("")
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            result = check_prerequisites("eval-generator", "acme")
        assert result["status"] == "fail"
        assert len(result["missing"]) == 1

    def test_missing_ordered_by_pipeline_stage(self, tmp_path):
        skill_md = tmp_path / ".claude" / "skills" / "eval-generator" / "SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            "| Resource | Path |\n"
            "|----------|------|\n"
            "| Scraper | `docs/scraper-generator/{slug}/scraper.py` |\n"
            "| Company report | `docs/product-classifier/{slug}.md` |\n"
            "| Assessment | `docs/catalog-detector/{slug}/assessment.md` |\n"
        )
        with patch("check_prerequisites.REPO_ROOT", tmp_path):
            result = check_prerequisites("eval-generator", "acme")
        # Should be sorted: product-classifier, catalog-detector, scraper-generator
        assert result["missing"][0]["path"].startswith("docs/product-classifier/")
        assert result["missing"][1]["path"].startswith("docs/catalog-detector/")
        assert result["missing"][2]["path"].startswith("docs/scraper-generator/")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
```

- [ ] **Step 5: Run all tests to verify they pass**

Run: `uv run --with pytest python -m pytest .claude/skills/product-discovery/tests/test_check_prerequisites.py -v`

Expected: All tests PASS.

- [ ] **Step 6: Run the script against the real repo to verify it works with actual SKILL.md files**

Run: `uv run .claude/skills/product-discovery/scripts/check_prerequisites.py --from eval-generator --slug harlowbros`

Expected: JSON output. Verify the `missing` list matches what you'd expect based on whether harlowbros files exist in `docs/`.

Run: `uv run .claude/skills/product-discovery/scripts/check_prerequisites.py --from product-classifier --slug anything`

Expected: `{"status": "pass", "missing": []}`.

Run: `uv run .claude/skills/product-discovery/scripts/check_prerequisites.py --from nonexistent --slug test`

Expected: `{"status": "error", ...}` with exit code 1.

- [ ] **Step 7: Commit**

```bash
git add .claude/skills/product-discovery/scripts/check_prerequisites.py \
       .claude/skills/product-discovery/tests/test_check_prerequisites.py
git commit -m "feat: add data-driven prerequisite checker for --from flag

Parses each stage's SKILL.md File locations table at runtime to determine
which upstream files must exist. No hardcoded prerequisite map — SKILL.md
is the single source of truth."
```

---

### Task 3: Update the product-discovery SKILL.md

**Files:**
- Modify: `.claude/skills/product-discovery/SKILL.md`

- [ ] **Step 1: Add the Arguments section after the existing `## Input` section**

Find the `## Input` section (ends before `## Stage 1: Product Classifier`). Insert after it:

```markdown
## Arguments

`$ARGUMENTS` may contain:
- A company slug, URL, or name (required)
- `--from {stage}` (optional) — skip stages before `{stage}` and run from there

Scan `$ARGUMENTS` for the `--from` token. If found, consume the next token as the stage name. Everything remaining is the company identifier.

**Valid `--from` values:** `product-classifier`, `catalog-detector`, `scraper-generator`, `eval-generator`. If the value doesn't match, reject with an error listing valid options.

`--from` can appear before or after the company identifier — both orderings are supported:
```
/product-discovery harlowbros --from scraper-generator
/product-discovery --from scraper-generator harlowbros
```

`--from product-classifier` runs the full pipeline. Log: "Note: `--from product-classifier` runs the full pipeline."

### Slug derivation when Stage 1 is skipped

When `--from` skips Stage 1, the slug must be derived before running the prerequisite check. If the input looks like a bare word with no dots or slashes, check whether `docs/product-classifier/{input}.md` exists and treat it as a slug directly. Otherwise, run `derive_slug.py` to get the slug from the URL.

### Prerequisite check

Before skipping to the target stage, run the prerequisite validation script:

```
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from {stage} --slug {slug}
```

If the script returns `"status": "fail"`, present each missing file as an escalation and **stop the pipeline**:

```
**Escalation: `missing_prerequisite`**

**Stage:** Product Discovery (--from {stage})

The prerequisite check found missing files required before {stage} can run.

Missing files:
{for each missing item: "- `{path}` — run `{fix}` to create it"}

**Your options:**
1. Run the suggested command(s) to create the missing files, then retry
2. Stop — cancel the pipeline run
```

If the script returns `"status": "pass"`, skip directly to the specified stage.
```

- [ ] **Step 2: Add skip guards to each stage section**

Add this line at the start of each stage section body — find each `## Stage N:` heading and insert right after it, before the first paragraph:

```markdown
**Skip this stage if `--from` specifies a later stage.**
```

Add to all four: `## Stage 1: Product Classifier`, `## Stage 2: Catalog Detector`, `## Stage 3: Scraper Generator`, `## Stage 4: Eval Generator`.

- [ ] **Step 3: Update the Pipeline Summary section to handle partial runs**

Find the `## Pipeline Summary` section and replace its opening paragraph:

```markdown
When all four stages complete successfully, present a structured summary to the user. Use this exact template — fill in values from the stage outputs, do not omit sections.
```

With:

```markdown
When all stages in the run complete successfully, present a structured summary to the user. Use this exact template — fill in values from the stage outputs, do not omit sections.

For `--from` runs where earlier stages were skipped, populate skipped sections by reading values from existing output files (e.g., read the company report for Company Profile, read the catalog assessment for Catalog). Annotate each skipped section heading with "(from prior run)" so the user knows which data is fresh vs cached. Example: `### Company Profile (from prior run)`.

If a `--from` run stops early (a downstream stage fails), follow the same early-stop summary behavior — shorter summary with a `### Stop Reason` section.
```

- [ ] **Step 4: Update the skill description in frontmatter to mention --from**

Update the `description:` field in the YAML frontmatter to mention `--from`:

```yaml
description: >
  End-to-end product discovery pipeline for a company.
  Takes a company URL or name and runs all four stages sequentially: classify, detect catalog, generate scraper, generate eval.
  Supports --from flag to start from a specific stage (e.g., --from scraper-generator) when upstream outputs already exist.
  Produces a company report, catalog assessment, scraper.py, config.json, and eval_config.json.
  Use this skill when the user wants the complete pipeline —
  "discover products for X", "run product discovery on X", "set up scraping for X",
  "I want to start tracking products from X", or any company URL/name with intent to build a full scraper pipeline.
  Also use when the user wants to re-run from a specific stage — "regenerate scraper for X", "re-run from scraper-generator for X".
  For individual stages only, use /product-classifier, /catalog-detector, /scraper-generator, or /eval-generator.
```

- [ ] **Step 5: Verify the SKILL.md is well-formed**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --skill product-discovery`

Expected: All checks pass (or only pre-existing warnings).

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/product-discovery/SKILL.md
git commit -m "feat: add --from flag to /product-discovery SKILL.md

Adds Arguments section with --from parsing, prerequisite check invocation,
stage skip guards, and partial-run summary guidance."
```

---

### Task 4: Integration test with real SKILL.md files

**Files:**
- No new files — this task validates the end-to-end flow

- [ ] **Step 1: Test against each stage with real SKILL.md files**

Run the script against each stage to verify the data-driven parser correctly extracts prerequisites from the actual SKILL.md tables in the repo:

```bash
# Should list: product-classifier report
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from catalog-detector --slug testcompany

# Should list: product-classifier report + catalog assessment
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from scraper-generator --slug testcompany

# Should list: product-classifier report + catalog assessment + scraper + config + products.jsonl + summary.json
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from eval-generator --slug testcompany
```

Expected: All return `"status": "fail"` with the correct missing files listed. The data-driven parser reads the actual SKILL.md tables, so verify the output matches what those tables contain (filtered to `{slug}`-bearing, non-output paths):

| Stage | Expected missing files |
|---|---|
| `catalog-detector` | `docs/product-classifier/testcompany.md` |
| `scraper-generator` | `docs/product-classifier/testcompany.md`, `docs/catalog-detector/testcompany/assessment.md` |
| `eval-generator` | `docs/product-classifier/testcompany.md`, `docs/catalog-detector/testcompany/assessment.md`, `docs/scraper-generator/testcompany/scraper.py`, `docs/scraper-generator/testcompany/output/products.jsonl`, `docs/scraper-generator/testcompany/output/summary.json` |

**Note:** The eval-generator SKILL.md does not list `config.json` in its File locations table, so it won't appear. If eval-generator actually needs `config.json` at runtime, add it to the eval-generator SKILL.md File locations table (as a non-output input) — the data-driven parser will then pick it up automatically.

If any expected file is missing from the output or any unexpected file appears, the SKILL.md table parser needs adjustment. Fix in Task 1 and re-run.

- [ ] **Step 2: Test with a slug that has all files present**

If harlowbros has files from prior runs, test:

```bash
uv run .claude/skills/product-discovery/scripts/check_prerequisites.py \
    --from scraper-generator --slug harlowbros
```

Expected: `"status": "pass"` if company report and catalog assessment exist, `"status": "fail"` otherwise.

- [ ] **Step 3: Run full test suite**

Run: `uv run --with pytest python -m pytest .claude/skills/product-discovery/tests/ -v`

Expected: All tests PASS.

- [ ] **Step 4: Run skill verification**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --skill product-discovery`

Expected: All checks pass.
