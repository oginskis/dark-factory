# Scraper Generator Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split scraper-generator into 3 agents (orchestrator/coder/tester), add targeted re-testing, add semantic validation rules.

**Architecture:** Rewrite 3 reference files (orchestrator.md, coder.md, tester.md), update 1 Python script (prepare_generator_input.py), create 1 new Python script (compare_baseline.py), update SKILL.md. All work is on main branch.

**Tech Stack:** Python 3.10+ (stdlib only for scripts), pytest, markdown reference files.

**Spec:** `docs/superpowers/specs/2026-03-18-scraper-generator-agent-redesign.md`

---

### Task 1: Add units to prepare_generator_input.py

**Files:**
- Modify: `.claude/skills/scraper-generator/scripts/prepare_generator_input.py`
- Modify: `.claude/skills/scraper-generator/tests/test_prepare_generator_input.py`

The tester needs unit info to evaluate semantic rules M01/M03/M04. The routing table currently has `types` but no `units`.

- [ ] **Step 1: Write failing test for units extraction**

Add to `test_prepare_generator_input.py` in the `TestExtractRoutingTable` class:

```python
def test_units_extracted(self, tmp_path):
    schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
    result = extract_routing_table(schema_file)
    assert "units" in result
    assert result["units"]["weight"] == "kg"

def test_units_skips_dash(self, tmp_path):
    schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
    result = extract_routing_table(schema_file)
    assert "widget_type" not in result["units"]
    assert "color" not in result["units"]

def test_units_skips_universal_keys(self, tmp_path):
    schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
    result = extract_routing_table(schema_file)
    assert "price" not in result["units"]
```

And update `TestExtractRoutingTable.test_structure_has_three_keys`:

```python
def test_structure_has_four_keys(self, tmp_path):
    schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
    result = extract_routing_table(schema_file)
    assert set(result.keys()) == {"core", "extended", "types", "units"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/test_prepare_generator_input.py::TestExtractRoutingTable::test_units_extracted -v`

Expected: FAIL — `"units"` not in result.

- [ ] **Step 3: Add units extraction to extract_routing_table**

In `prepare_generator_input.py`, modify `extract_routing_table()`:

```python
def extract_routing_table(schema_path: Path) -> dict:
    """Extract core/extended attribute keys, types, and units from a schema file."""
    content = schema_path.read_text(encoding="utf-8")

    core_rows = parse_schema_table(content, "Core Attributes")
    extended_rows = parse_schema_table(content, "Extended Attributes")

    core_keys = []
    extended_keys = []
    types = {}
    units = {}

    for row in core_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        unit = row.get("Unit", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            core_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")
            if unit and unit != "—" and unit != "-":
                units[key] = unit

    for row in extended_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        unit = row.get("Unit", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            extended_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")
            if unit and unit != "—" and unit != "-":
                units[key] = unit

    return {
        "core": core_keys,
        "extended": extended_keys,
        "types": types,
        "units": units,
    }
```

- [ ] **Step 4: Run tests**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/test_prepare_generator_input.py -v`

Expected: All pass. Fix the renamed test (`test_structure_has_four_keys`).

- [ ] **Step 5: Add integration test for units with real schema**

Add to `TestExtractRoutingTableIntegration`:

```python
def test_softwood_hardwood_lumber_units(self):
    schema_path = SCHEMAS_DIR / "softwood-hardwood-lumber.md"
    if not schema_path.exists():
        pytest.skip("Schema file not present in working tree")
    result = extract_routing_table(schema_path)
    assert "units" in result
    # actual_thickness and actual_width should have mm units
    assert result["units"].get("actual_thickness") is not None
    assert result["units"].get("actual_width") is not None
    # enum/text fields like wood_type should not have units
    assert "wood_type" not in result["units"]
```

- [ ] **Step 6: Run full test suite**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/test_prepare_generator_input.py -v`

Expected: All pass.

---

### Task 2: Create compare_baseline.py

**Files:**
- Create: `.claude/skills/scraper-generator/scripts/compare_baseline.py`
- Create: `.claude/skills/scraper-generator/tests/test_compare_baseline.py`

JSONL diff script for regression detection. The tester calls it during `retest` mode.

- [ ] **Step 1: Create test file**

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for compare_baseline.py — JSONL regression detection."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from compare_baseline import compare_products, load_jsonl


class TestLoadJsonl:
    def test_loads_valid_jsonl(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text('{"sku": "A", "url": "https://x.com/a"}\n{"sku": "B", "url": "https://x.com/b"}\n')
        products = load_jsonl(f)
        assert len(products) == 2
        assert products[0]["sku"] == "A"

    def test_empty_file(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text("")
        products = load_jsonl(f)
        assert products == []

    def test_skips_blank_lines(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text('{"sku": "A"}\n\n{"sku": "B"}\n')
        products = load_jsonl(f)
        assert len(products) == 2


class TestCompareProducts:
    def test_no_regressions(self):
        baseline = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}},
        ]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}},
        ]
        result = compare_products(baseline, retest)
        assert result["regressions"] == []
        assert result["status"] == "pass"

    def test_price_changed(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [{"url": "https://x.com/a", "sku": "A", "price": None, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1
        assert result["regressions"][0]["field"] == "price"
        assert result["status"] == "fail"

    def test_core_attributes_disappeared(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}}]
        retest = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1
        assert result["regressions"][0]["field"] == "core_attributes"

    def test_sku_disappeared(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [{"url": "https://x.com/a", "sku": None, "price": 10.0, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1

    def test_product_missing_from_retest(self):
        baseline = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
            {"url": "https://x.com/b", "sku": "B", "price": 20.0, "core_attributes": {}},
        ]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
        ]
        # Product B not in retest — not a regression (retest is scoped)
        result = compare_products(baseline, retest)
        assert result["status"] == "pass"

    def test_unmatched_retest_product_ignored(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
            {"url": "https://x.com/new", "sku": "NEW", "price": 5.0, "core_attributes": {}},
        ]
        result = compare_products(baseline, retest)
        assert result["status"] == "pass"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/test_compare_baseline.py -v`

Expected: FAIL — `compare_baseline` module not found.

- [ ] **Step 3: Create compare_baseline.py**

```python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Compare scraper output against a baseline to detect regressions.

Used by the tester during retest mode. Matches products by URL,
compares key fields (sku, price, core_attributes population).

Usage:
    python compare_baseline.py --baseline output/baseline_products.jsonl --retest output/products.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REGRESSION_FIELDS = ["sku", "price", "brand", "product_category"]


def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    products = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            products.append(json.loads(line))
    return products


def compare_products(baseline: list[dict], retest: list[dict]) -> dict:
    """Compare retest products against baseline, report regressions.

    Only compares products present in BOTH sets (matched by URL).
    Products in baseline but not in retest are ignored (retest is scoped).
    """
    baseline_by_url = {p["url"]: p for p in baseline if "url" in p}
    regressions = []

    for product in retest:
        url = product.get("url")
        if not url or url not in baseline_by_url:
            continue

        base = baseline_by_url[url]

        # Check key fields
        for field in REGRESSION_FIELDS:
            base_val = base.get(field)
            new_val = product.get(field)
            if base_val is not None and new_val is None:
                regressions.append({
                    "url": url,
                    "field": field,
                    "baseline_value": base_val,
                    "retest_value": new_val,
                })

        # Check core_attributes population
        base_core = base.get("core_attributes", {})
        new_core = product.get("core_attributes", {})
        if len(base_core) > 0 and len(new_core) == 0:
            regressions.append({
                "url": url,
                "field": "core_attributes",
                "baseline_value": f"{len(base_core)} attributes",
                "retest_value": "empty",
            })

    return {
        "status": "fail" if regressions else "pass",
        "products_compared": len([p for p in retest if p.get("url") in baseline_by_url]),
        "regressions": regressions,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare scraper output against baseline")
    parser.add_argument("--baseline", required=True, help="Path to baseline JSONL")
    parser.add_argument("--retest", required=True, help="Path to retest JSONL")
    args = parser.parse_args()

    baseline = load_jsonl(Path(args.baseline))
    retest = load_jsonl(Path(args.retest))
    result = compare_products(baseline, retest)

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/test_compare_baseline.py -v`

Expected: All pass.

---

### Task 3: Write coder.md

**Files:**
- Create: `.claude/skills/scraper-generator/references/coder.md`

This file absorbs `code-generator.md` (260 lines) + `persist-hooks.md` (35 lines) and adds:
- `--categories` and `--append` CLI flag requirements
- Two modes: `generate` and `fix`
- Fix mode reads `test_report.json` for targeted patches

- [ ] **Step 1: Read current code-generator.md and persist-hooks.md in full**

Read: `.claude/skills/scraper-generator/references/code-generator.md` (all 260 lines)
Read: `.claude/skills/scraper-generator/references/persist-hooks.md` (all 35 lines)

- [ ] **Step 2: Write coder.md**

Create `.claude/skills/scraper-generator/references/coder.md` with this structure:

```markdown
# Coder Sub-Agent

**Input:** Catalog assessment, routing tables, category mapping, platform knowledgebase
**Output:** `scraper.py` written to disk

---

## Modes

### Mode: generate

[Input contract — what the orchestrator passes]

### Mode: fix

[Input contract — test_report.json + existing scraper.py + full context]
[Fix guidance — read issues, sample_values, affected_attributes]
[Rule: never rewrite the entire scraper, targeted patches only]
[Rule: read passing_categories to avoid regressions]

---

## Product Record Format

[COPY from code-generator.md lines 25-84 — the canonical record format, example JSON]

---

## Language Rules for Non-English Sites

[COPY from code-generator.md lines 88-98]

---

## Library Selection

[COPY from code-generator.md lines 101-109]

---

## Required Behavior

[COPY from code-generator.md lines 113-161 — all 10 rules]
[UPDATE rule 9 to add --categories and --append flags alongside --limit and --probe]
[ADD rule 11: --categories LIST flag — filter discovered leaf categories by prefix]
[ADD rule 12: --append flag — skip setup() truncation, append to existing products.jsonl]

---

## Product Discovery Strategy

[COPY from code-generator.md lines 165-195]

---

## Python Code Quality

[COPY from code-generator.md lines 199-241]

---

## Persist Hook Implementations

[COPY from persist-hooks.md — the setup/persist/teardown functions]
[UPDATE setup() to check for --append flag and skip truncation when set]

---

## What NOT to Include

[COPY from code-generator.md lines 244-249]

---

## Expected Output

[COPY from code-generator.md lines 253-259]
[UPDATE to mention --categories and --append in the CLI]
```

The key additions vs current `code-generator.md`:
1. **Modes section** at top — generate vs fix
2. **`--categories` flag** in Required Behavior rule 11
3. **`--append` flag** in Required Behavior rule 12 and persist hooks `setup()`
4. **Fix mode guidance** — how to read test_report.json, what to patch

- [ ] **Step 3: Verify coder.md is complete**

Check that coder.md contains:
- All 10 original Required Behavior rules from code-generator.md
- Product Record Format with example JSON
- Library Selection table
- Product Discovery Strategy
- Python Code Quality rules
- Persist hooks with `--append` support
- `--categories` and `--append` flag specs
- Generate mode input contract
- Fix mode input contract and guidance

---

### Task 4: Write tester.md

**Files:**
- Create: `.claude/skills/scraper-generator/references/tester.md`

Three modes, structural rules S01-S09, semantic rules M01-M04, structured test report.

- [ ] **Step 1: Read current validator.md in full**

Read: `.claude/skills/scraper-generator/references/validator.md` (all 220 lines)

- [ ] **Step 2: Write tester.md**

Create `.claude/skills/scraper-generator/references/tester.md` with this structure:

```markdown
# Tester Sub-Agent

**Input:** Scraper path, catalog structure, expected product count, routing tables
**Output:** `test_report.json` written to disk

**Key rule:** The tester NEVER edits scraper.py. It only runs the scraper and evaluates output.

---

## Input Contract

| Field | Type | Description |
|---|---|---|
| scraper_path | path | Path to scraper.py |
| catalog_structure | object | Verified category tree from catalog assessment |
| expected_product_count | int | From catalog assessment |
| routing_tables_path | path | Path to generator_input.json (for semantic rules) |
| mode | enum | "full", "retest", or "final" |
| fix_targets | list | (retest only) Rules and categories to re-verify |
| regression_sample_from | list | (retest only) Passing categories to sample for regression |

---

## Output Contract

Write `test_report.json` to the scraper's output directory. Overwrite on each dispatch.

[Full JSON schema from the spec — mode, timestamp, status, smoke_summary, final_summary, rule_results, issues, passing_categories]

[Retest additions: fix_results, regression_results, new_issues]

---

## Modes

### Full Mode

1. Probe: select 3-5 product URLs across different top-level categories. Run `--probe URL` for each. Evaluate all rules on probe output.
2. Per-category sampling: for each top-level category, run `--categories {cat} --limit N` (proportional to estimated size, min 5). Use `--append` after first run. Total sample = 20% of expected products, max 500.
3. Depth check: run `--limit 100` sequential (no --categories) to verify pagination and deduplication.
4. Evaluate all rules (S01-S09, M01-M04) on combined output.
5. Save baseline: copy products.jsonl to baseline_products.jsonl.
6. Write test_report.json.

### Retest Mode

1. Fix verification: for each fix_target, run `--categories {affected_categories} --limit 10`. Re-evaluate the specific failing rule.
2. Regression check: run `--categories {regression_sample_from} --limit 10 --append`. Run compare_baseline.py against baseline_products.jsonl.
3. Write test_report.json with fix_results, regression_results, new_issues.

### Final Mode

Same as full mode's per-category sampling + depth check (skip probe). Fresh run to confirm at scale. Write test_report.json.

---

## Validation Rules

### Structural Rules

[Table: S01-S09 with ID, rule, severity, threshold, check logic]

For each rule, describe:
- What to check
- How to compute the metric
- What to report in issues[] when it fails

### Semantic Rules

[Table: M01-M04 with ID, rule, severity, check logic]

For each rule, describe:
- What to check (using routing_tables types and units dicts)
- How to compute the metric
- Example pass/fail
- What to report in issues[] (include sample_values!)

### Rule Evaluation per Mode

| Rule | Full | Retest (fix) | Retest (regression) | Final |
|---|---|---|---|---|
| S01-S05 | All products | Affected categories | Compare baseline | All products |
| S06 | All products | Skip | Skip | All products |
| S07-S09 | All runs | All runs | All runs | All runs |
| M01-M04 | All products | Affected categories | Compare baseline | All products |

---

## Regression Detection

Use compare_baseline.py:
```
uv run .claude/skills/scraper-generator/scripts/compare_baseline.py \
    --baseline {output_dir}/baseline_products.jsonl \
    --retest {output_dir}/products.jsonl
```

If status is "fail", include regressions in test_report.json.

---

## Timeouts

| Mode | Timeout |
|---|---|
| Probe | 30 seconds per URL |
| Full (per-category run) | max(60, limit * 6) seconds |
| Full (depth check) | max(120, 100 * 6) = 600 seconds |
| Retest | 5 minutes total |
| Final | max(120, sample_size * 6) seconds |
```

- [ ] **Step 3: Verify tester.md is complete**

Check that tester.md contains:
- All three modes with step-by-step instructions
- All 13 rules (S01-S09, M01-M04) with check logic
- Test report JSON format
- Regression detection via compare_baseline.py
- Per-mode rule evaluation matrix
- Timeouts
- Input/output contracts
- "Never edits scraper.py" rule

---

### Task 5: Rewrite orchestrator.md

**Files:**
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md`

Pure coordination. Dispatches coder and tester. No code writing, no testing.

- [ ] **Step 1: Read current orchestrator.md in full**

Read: `.claude/skills/scraper-generator/references/orchestrator.md` (all 462 lines)

- [ ] **Step 2: Rewrite orchestrator.md**

The new orchestrator keeps:
- Step 1 (load context, category mapping, SKU schema loading, escalations) — same as today
- Step 1b (label map for non-English) — same as today
- Step 2a (attribute routing) — same as today
- Decisions section — same escalation definitions
- Fix mode section — updated for new agents

The new orchestrator changes:
- Step 2c (code generation) → **Dispatch Coder (mode: "generate")**
- Validator dispatch → **Dispatch Tester (mode: "full")**
- Retry loop → **Dispatch Coder (mode: "fix") + Dispatch Tester (mode: "retest")**
- Final verification → **Dispatch Tester (mode: "final")**
- Steps 3-5 (knowledgebase, config, self-verification) — same as today

Key sections to write:

```markdown
## Step 2: Dispatch Coder

Dispatch the coder sub-agent using the Agent tool.

**Generate mode input:**
- Read coder.md as the sub-agent reference
- Pass: catalog assessment path, routing tables path (generator_input.json), category mapping, platform knowledgebase path, label map (non-English)
- The coder reads these files and writes scraper.py

**Fix mode input:**
- Pass: all generate mode inputs + test_report.json path + existing scraper.py path
- The coder reads test_report.json, identifies failing rules, patches scraper.py

## Step 3: Dispatch Tester

Dispatch the tester sub-agent using the Agent tool.

**Full mode input:**
- Read tester.md as the sub-agent reference
- Pass: scraper path, catalog structure (from assessment), expected product count, routing tables path

**Retest mode input:**
- Pass: mode="retest", fix_targets (from test_report.json issues), regression_sample_from (from test_report.json passing_categories), scraper path, routing tables path

**Final mode input:**
- Pass: same as full mode but mode="final"

## Retry State Machine

[The flow from the spec: full -> fix loop (retest) -> final]
[Circuit breakers: max 3 cycles, max 2 per rule]
[Escalation when budget exhausted]
```

- [ ] **Step 3: Verify orchestrator.md completeness**

Check that orchestrator.md:
- Never mentions writing code (Step 2c is gone — replaced by coder dispatch)
- Never mentions running the scraper (validator dispatch is replaced by tester dispatch)
- Has correct dispatch instructions for both coder and tester
- Keeps all existing escalation paths
- Keeps non-English label mapping
- Keeps SKU schema auto-generation
- Keeps fix mode for /scraper-remediation (maps eval check names to rule IDs)
- Has the retry state machine with circuit breakers

---

### Task 6: Update SKILL.md and clean up

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md`
- Delete: `.claude/skills/scraper-generator/references/code-generator.md`
- Delete: `.claude/skills/scraper-generator/references/validator.md`
- Delete: `.claude/skills/scraper-generator/references/persist-hooks.md`

- [ ] **Step 1: Update SKILL.md file locations table**

Replace references to old files with new ones. Add new output files.

Changes to the file locations table:
- Remove: `Persist hook implementations` row (`.claude/skills/scraper-generator/references/persist-hooks.md`)
- Add: `Test report (output)` → `docs/scraper-generator/{slug}/output/test_report.json`
- Add: `Baseline products (output)` → `docs/scraper-generator/{slug}/output/baseline_products.jsonl`

- [ ] **Step 2: Update SKILL.md workflow section**

Update the dispatch instructions:
- Change "Sub-agent file: `.claude/skills/scraper-generator/references/validator.md`" to reference both `coder.md` and `tester.md`
- Update the dispatch description: "Dispatch the coder sub-agent for code generation/fixing and the tester sub-agent for validation, as directed by the orchestrator."
- Remove references to `code-generator.md` ("Reference file `references/code-generator.md` defines the canonical product record format...") — this is now in `coder.md`
- Remove "The orchestrator handles label mapping and code generation inline" — the orchestrator handles label mapping but dispatches the coder for code generation

- [ ] **Step 3: Delete old reference files**

```bash
rm .claude/skills/scraper-generator/references/code-generator.md
rm .claude/skills/scraper-generator/references/validator.md
rm .claude/skills/scraper-generator/references/persist-hooks.md
```

- [ ] **Step 4: Run skill verification**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --skill scraper-generator`

Expected: All checks pass.

- [ ] **Step 5: Run all tests**

Run: `uv run --with pytest python -m pytest .claude/skills/scraper-generator/tests/ -v`

Expected: All pass.

---

### Task 7: Verify with /skill-creator-local deep review

- [ ] **Step 1: Run deep review**

Invoke `/skill-creator-local deep review` for the scraper-generator skill to verify convention compliance after all changes.

- [ ] **Step 2: Fix any issues found**

Address any convention violations flagged by the review.
