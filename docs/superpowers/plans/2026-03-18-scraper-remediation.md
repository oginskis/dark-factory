# Scraper Remediation Feedback Loop — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an autonomous eval↔scraper-generator feedback loop that detects scraper degradation, triages config drift vs scraper regression, and applies up to 3 fix cycles before escalating to a human.

**Architecture:** A new `/scraper-remediation` skill orchestrates the loop. It reads eval results, triages the failure, invokes scraper-generator in fix mode (new), re-runs eval with history isolation (`--no-history` flag, new), and tracks everything in a remediation log. Scraper-generator gets a documented fix mode that patches existing scrapers instead of regenerating from scratch.

**Tech Stack:** Python (eval.py changes), Markdown (skill files following repo conventions)

**Spec:** `docs/superpowers/specs/2026-03-18-scraper-remediation-design.md`

---

## File Map

| Action | File | Responsibility |
|--------|------|---------------|
| Modify | `eval/eval.py` | Add `--no-history` flag |
| Modify | `eval/test_eval.py` | Test `--no-history` behavior |
| Create | `.claude/skills/scraper-remediation/SKILL.md` | Skill wrapper — input, file locations, workflow delegation |
| Create | `.claude/skills/scraper-remediation/references/workflow.md` | Full remediation workflow — entry conditions, triage, cycle flow, escalation |
| Modify | `.claude/skills/scraper-generator/SKILL.md` | Document fix mode invocation, backup step, skip archive |
| Modify | `.claude/skills/scraper-generator/references/orchestrator.md` | Add fix mode step flow, fix_summary output, fix_outcome: "unfixable" |
| Modify | `.claude/skills/scraper-generator/references/validator.md` | Document fix_summary field in validation.json output |

---

### Task 1: Add `--no-history` flag to eval.py

**Files:**
- Modify: `eval/eval.py:869-944` (argument parsing + history/baseline write sections)
- Modify: `eval/test_eval.py` (add test class)

- [ ] **Step 1: Write the failing test**

Add to `eval/test_eval.py`:

```python
class TestNoHistoryFlag:
    """Verify --no-history skips eval_history.json append and baseline creation."""

    def _setup_eval_tree(self, tmp_path):
        """Build the directory structure that eval.py's main() expects.

        eval.py uses find_project_root() which walks up from the config file
        looking for an eval/ directory. Then it resolves:
        - scraper output: {root}/docs/scraper-generator/{slug}/output/
        - eval output: {config_parent}/output/
        """
        # Project root marker — find_project_root needs eval/ dir
        (tmp_path / "eval").mkdir()

        # Config at docs/eval-generator/testco/eval_config.json
        config_dir = tmp_path / "docs" / "eval-generator" / "testco"
        config_dir.mkdir(parents=True)
        config = {
            "company_slug": "testco",
            "expected_product_count": 10,
            "expected_top_level_categories": ["Cat A"],
            "subcategories": {
                "wood.softwood_hardwood_lumber": {
                    "core_attributes": ["wood_type"],
                    "extended_attributes": [],
                    "expected_count": 10,
                }
            },
            "type_map": {"wood_type": "str"},
            "enum_attributes": {},
            "has_prices": True,
        }
        config_path = config_dir / "eval_config.json"
        config_path.write_text(json.dumps(config))

        # Scraper output at docs/scraper-generator/testco/output/
        scraper_dir = tmp_path / "docs" / "scraper-generator" / "testco" / "output"
        scraper_dir.mkdir(parents=True)
        product = {
            "sku": "SKU1", "name": "Test", "url": "https://example.com/p1",
            "price": 10.0, "currency": "GBP", "brand": "Test",
            "product_category": "wood.softwood_hardwood_lumber",
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "category_path": "Cat A",
            "core_attributes": {"wood_type": "Softwood"},
            "extended_attributes": {}, "extra_attributes": {},
        }
        (scraper_dir / "products.jsonl").write_text(json.dumps(product) + "\n")
        (scraper_dir / "summary.json").write_text(json.dumps({
            "total_products": 1, "limited": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }))

        return config_path

    def test_no_history_skips_history_and_baseline(self, tmp_path):
        """With --no-history: eval_result.json written, history and baseline skipped."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval.py", str(config_path), "--no-history"]):
            from eval import main as eval_main
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert not (eval_output / "eval_history.json").exists()
        assert not (eval_output / "baseline.json").exists()

    def test_without_no_history_writes_history(self, tmp_path):
        """Without --no-history: eval_history.json IS created."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval.py", str(config_path)]):
            from eval import main as eval_main
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert (eval_output / "eval_history.json").exists()

    def test_no_history_still_reads_existing_baseline(self, tmp_path):
        """--no-history reads existing baseline for scoring but does not create one."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"
        eval_output.mkdir(parents=True, exist_ok=True)

        # Pre-create a baseline
        baseline = {"attribute_fill_rates": {"wood_type": 1.0}, "products_found": 1}
        (eval_output / "baseline.json").write_text(json.dumps(baseline))

        with patch("sys.argv", ["eval.py", str(config_path), "--no-history"]):
            from eval import main as eval_main
            eval_main()

        # Baseline should still exist and be unchanged
        result_baseline = json.loads((eval_output / "baseline.json").read_text())
        assert result_baseline == baseline
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
uv run --with pytest --with httpx --with selectolax python -m pytest eval/test_eval.py::TestNoHistoryFlag -v
```

Expected: FAIL — `--no-history` flag not recognized.

- [ ] **Step 3: Add `--no-history` argument to eval.py**

In `eval/eval.py`, modify the `main()` function argument parsing (around line 872):

```python
parser.add_argument("--no-history", action="store_true",
                    help="Write eval_result.json but skip eval_history.json and baseline updates (for remediation re-runs)")
```

- [ ] **Step 4: Guard history append with the flag**

In `eval/eval.py`, wrap the history append block (around lines 935-944):

```python
if not args.no_history:
    history.append(history_entry)
    eval_history_path.write_text(json.dumps(history, indent=2))
```

- [ ] **Step 5: Guard baseline creation with the flag**

In `eval/eval.py`, wrap the baseline call (around line 927):

```python
if args.no_history:
    baseline = load_json(baseline_path) if baseline_path.exists() else None
else:
    baseline = maybe_create_baseline(products, config, is_limited, baseline_path)
```

This way: `--no-history` still reads the existing baseline (for field_level_regression scoring) but never creates or updates it.

- [ ] **Step 6: Run tests to verify they pass**

```bash
uv run --with pytest --with httpx --with selectolax python -m pytest eval/test_eval.py::TestNoHistoryFlag -v
```

Expected: PASS

- [ ] **Step 7: Run all eval tests to check for regressions**

```bash
uv run --with pytest --with httpx --with selectolax python -m pytest eval/test_eval.py -v
```

Expected: All tests pass.

- [ ] **Step 8: Commit**

```bash
git add eval/eval.py eval/test_eval.py
git commit -m "Add --no-history flag to eval.py for remediation re-runs"
```

---

### Task 2: Create `/scraper-remediation` skill

**Files:**
- Create: `.claude/skills/scraper-remediation/SKILL.md`
- Create: `.claude/skills/scraper-remediation/references/workflow.md`

- [ ] **Step 1: Create SKILL.md**

Follow the skill wrapper convention (Convention 1 from `conventions.md`). Must include: frontmatter, 4-sentence description, Input, File locations table, Workflow delegation, Escalation handling, Notes.

Key content:
- `name: scraper-remediation`
- `description:` 4 sentences: what it does, what it produces, trigger phrases, prerequisites
- Input: company slug
- File locations table: eval_result.json (read), validation.json (read), scraper.py (read, backup), eval_config.json (read), remediation_log.json (write)
- Workflow: "Read and follow `references/workflow.md`."
- Escalation: `unfixable_scraper` (fix_outcome: "unfixable"), `cycles_exhausted` (3 cycles done, still failing)
- Notes: "File-driven skill — reads eval and scraper artifacts, writes only to `docs/scraper-remediation/{slug}/`."

Refer to the spec for all details: `docs/superpowers/specs/2026-03-18-scraper-remediation-design.md`

- [ ] **Step 2: Create references/workflow.md**

Follow the workflow reference convention (Convention 2). Must include: Input/Output one-liners, Context section, numbered Steps, Boundaries, Decisions with full structure.

**Steps to include:**

1. **Entry Conditions** — check eval_result.json exists, check status, check concurrency guard (4h TTL)
2. **Triage** — config drift detection (pagination_completeness/category_diversity failing in isolation) vs scraper regression. If config drift: re-run `/eval-generator`, re-run eval, exit if resolved
3. **Backup** — copy scraper.py to scraper.py.pre-remediation
4. **Build Fix Request** — construct JSON from eval_result.json check_details (format per spec)
5. **Invoke Scraper-Generator Fix Mode** — pass fix request, wait for completion
6. **Re-Run Eval** — `uv run eval/eval.py {eval_config_path} --no-history`
7. **Assess Result** — if passing: delete baseline.json, log resolved. If fix_outcome "unfixable": escalate immediately. If still failing and cycle < 3: loop to step 4. If cycle == 3: escalate.
8. **Write Remediation Log** — persist to `docs/scraper-remediation/{slug}/remediation_log.json`

**Self-Verification step** (required by verify_skill.py): One of the numbered steps must be named "Self-Verification" — verify remediation_log.json was written with correct structure and outcome.

**Decisions:**
- `unfixable_scraper`: Context — scraper-generator returned fix_outcome: "unfixable". Autonomous: none. Escalate: always. Payload: slug, cycle history, fix_summary.
- `cycles_exhausted`: Context — 3 fix cycles completed, eval still failing. Autonomous: none. Escalate: always. Payload: slug, 3-cycle history, current eval score.

**Boundaries:**
- Does not modify scraper.py (scraper-generator does that)
- Does not modify eval_config.json (eval-generator does that, during triage only)
- Does not modify eval_history.json or baseline.json (uses --no-history)
- Only writes to `docs/scraper-remediation/{slug}/`
- Exception: creates `scraper.py.pre-remediation` backup in scraper-generator's directory

**Strict format rules for remediation_log.json** — table per spec.

- [ ] **Step 3: Verify directory structure**

```bash
ls -la .claude/skills/scraper-remediation/
ls -la .claude/skills/scraper-remediation/references/
```

Expected: SKILL.md and references/workflow.md exist.

- [ ] **Step 4: Run convention verification**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py scraper-remediation
```

Expected: No critical or moderate issues. Fix any that appear.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/scraper-remediation/
git commit -m "Add /scraper-remediation skill with workflow reference"
```

---

### Task 3: Update scraper-generator for fix mode

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md`
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md`
- Modify: `.claude/skills/scraper-generator/references/validator.md`

- [ ] **Step 1: Add fix mode to SKILL.md**

Add a section after the existing workflow delegation that documents fix mode invocation. Key additions:
- When invoked with a fix request (`mode: "fix"`), skip the archive step
- Read existing scraper.py instead of generating from scratch
- The remediation skill creates `scraper.py.pre-remediation` backup before invoking fix mode
- Workflow reference handles the fix mode step flow divergence

- [ ] **Step 2: Add fix mode step flow to orchestrator.md**

Add a new section "## Fix Mode" to orchestrator.md. Document:
- **Entry:** Receives fix request JSON with `mode`, `cycle`, `slug`, `failing_checks`, `passing_checks`, `scraper_path`, `eval_config_path`
- **Step 1 (load context):** Same as normal — reads catalog assessment, company report, SKU schemas, config.json
- **Step 2a-2c (code patching):** REPLACED — reads existing scraper.py, analyzes failing_checks to determine what to patch. If fundamental approach change needed (site changed strategy, added bot protection), set `fix_outcome: "unfixable"` and return immediately.
- **Step 3 (validation dispatch):** Same as normal — probe, smoke test, final verification. Validator internal retry counters reset fresh each cycle.
- **Step 4 (diagnostic persistence):** Same, plus writes `fix_summary` to validation.json.
- **fix_outcome values:** `"fixed"`, `"partial"`, `"unfixable"`

- [ ] **Step 3: Add fix_summary to validator.md**

Add to the validator's output contract section:

```json
{
  "fix_summary": {
    "summary": "Free-text description of changes made.",
    "fix_outcome": "fixed",
    "fix_targets": ["core_attribute_coverage"],
    "changes": [
      { "type": "enrichment_pattern", "attribute": "wood_type" }
    ]
  }
}
```

Document: this field is only present in fix mode. `changes[].type` is free-form text. `fix_outcome` is one of `"fixed"`, `"partial"`, `"unfixable"`.

- [ ] **Step 4: Run convention verification on scraper-generator**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py scraper-generator
```

Expected: No new critical or moderate issues. Fix any that appear.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/scraper-generator/
git commit -m "Add fix mode to scraper-generator for remediation feedback loop"
```

---

### Task 4: Full verification

- [ ] **Step 1: Run convention verification on all modified skills**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py scraper-remediation scraper-generator eval-generator
```

Expected: No critical or moderate issues.

- [ ] **Step 2: Run all tests**

```bash
uv run --with pytest --with httpx --with selectolax python -m pytest -v
```

Expected: All tests pass.

- [ ] **Step 3: Verify cross-references**

Check that:
- scraper-remediation SKILL.md references all file paths from the spec's file locations table
- scraper-remediation workflow.md references the fix request format from the spec
- scraper-generator orchestrator.md fix mode section is consistent with the spec
- validator.md fix_summary format matches the spec

- [ ] **Step 4: Final commit if any fixes were needed**

```bash
git add -A
git commit -m "Fix convention compliance issues from full verification"
```
