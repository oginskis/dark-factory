# Pure Skills Refactor Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate the `agents/` directory by moving all agent content into `references/` under each skill, rewriting SKILL.md files to the integrated pattern, and simplifying skill-creator-local conventions.

**Architecture:** Each pipeline skill becomes self-contained under `.claude/skills/{name}/` with SKILL.md (integrated wiring + workflow pointer) + `references/` (detailed reasoning). The product-discovery orchestrator invokes stage skills via the Skill tool. The `agents/` directory is deleted.

**Tech Stack:** Markdown, Python (verify_skill.py)

**Spec:** `docs/superpowers/specs/2026-03-16-pure-skills-refactor-design.md`

**Atomicity:** All tasks must be completed on a single branch and merged as one unit. The system is broken between file moves and SKILL.md rewrites.

---

## Chunk 1: Move files and rewrite pipeline SKILL.md files

### Task 1: Move all agent files to references/

**Files:**
- Move: `agents/product-classifier.md` → `.claude/skills/product-classifier/references/workflow.md`
- Move: `agents/catalog-detector.md` → `.claude/skills/catalog-detector/references/workflow.md`
- Move: `agents/eval-generator.md` → `.claude/skills/eval-generator/references/workflow.md`
- Move: `agents/scraper-generator.md` → `.claude/skills/scraper-generator/references/orchestrator.md`
- Move: `agents/scraper-generator/label-discoverer.md` → `.claude/skills/scraper-generator/references/label-discoverer.md`
- Move: `agents/scraper-generator/code-generator.md` → `.claude/skills/scraper-generator/references/code-generator.md`
- Move: `agents/scraper-generator/validator.md` → `.claude/skills/scraper-generator/references/validator.md`
- Delete: `agents/` directory

- [ ] **Step 1: Create references/ directories for skills that don't have them**

```bash
mkdir -p .claude/skills/product-classifier/references
mkdir -p .claude/skills/catalog-detector/references
mkdir -p .claude/skills/eval-generator/references
```

Note: `.claude/skills/scraper-generator/references/` already exists (has `persist-hooks.md`).

- [ ] **Step 2: Move the 3 simple pipeline agent files**

```bash
git mv agents/product-classifier.md .claude/skills/product-classifier/references/workflow.md
git mv agents/catalog-detector.md .claude/skills/catalog-detector/references/workflow.md
git mv agents/eval-generator.md .claude/skills/eval-generator/references/workflow.md
```

- [ ] **Step 3: Move scraper-generator orchestrator and sub-agents**

The orchestrator (`agents/scraper-generator.md`) is tracked and can use `git mv`. The 3 sub-agent files under `agents/scraper-generator/` may be untracked (created on this branch) — use `mv` for those and `git add` the destinations.

```bash
git mv agents/scraper-generator.md .claude/skills/scraper-generator/references/orchestrator.md
mv agents/scraper-generator/label-discoverer.md .claude/skills/scraper-generator/references/label-discoverer.md
mv agents/scraper-generator/code-generator.md .claude/skills/scraper-generator/references/code-generator.md
mv agents/scraper-generator/validator.md .claude/skills/scraper-generator/references/validator.md
git add .claude/skills/scraper-generator/references/label-discoverer.md
git add .claude/skills/scraper-generator/references/code-generator.md
git add .claude/skills/scraper-generator/references/validator.md
```

- [ ] **Step 4: Delete the agents/ directory**

```bash
rm -rf agents/
```

- [ ] **Step 5: Verify all files landed correctly**

```bash
ls -la .claude/skills/product-classifier/references/workflow.md
ls -la .claude/skills/catalog-detector/references/workflow.md
ls -la .claude/skills/eval-generator/references/workflow.md
ls -la .claude/skills/scraper-generator/references/orchestrator.md
ls -la .claude/skills/scraper-generator/references/label-discoverer.md
ls -la .claude/skills/scraper-generator/references/code-generator.md
ls -la .claude/skills/scraper-generator/references/validator.md
ls -la .claude/skills/scraper-generator/references/persist-hooks.md
test ! -d agents/ && echo "agents/ deleted successfully"
```

All 8 files must exist. `agents/` must not exist.

### Task 2: Rewrite product-classifier SKILL.md

**Files:**
- Modify: `.claude/skills/product-classifier/SKILL.md`
- Reference (read-only): `.claude/skills/product-classifier/references/workflow.md`

- [ ] **Step 1: Read the current SKILL.md and the workflow reference**

Read `.claude/skills/product-classifier/SKILL.md` (current thin wrapper, ~53 lines) and `.claude/skills/product-classifier/references/workflow.md` (the former agent file) to understand the current wiring and logical resource names.

- [ ] **Step 2: Rewrite SKILL.md to the integrated template**

The new SKILL.md must follow the integrated template from the spec (lines 94-137). Key elements:

- Keep: frontmatter (name, description, user-invocable) — unchanged
- Keep: `## Input` section — unchanged
- Keep: `## File locations` table — unchanged
- Replace: the one-line agent pointer (`Read and follow the agent instructions in agents/product-classifier.md`) with `## Workflow` section that says `Read and follow references/workflow.md` plus the harness-specific instructions
- Merge: the current `## Claude Code wiring` bullets into the `## Workflow` section
- Keep: escalation handling (format template + user options) — move to its own `## Escalation handling` section
- Keep: `## Notes` — unchanged

The `## Workflow` section should contain:
- "Read and follow `references/workflow.md`."
- File path mapping instruction: "Provide the file paths from the table above when the workflow references logical resources (e.g., 'the product taxonomy categories file', 'the company reports directory', 'write the company report')."
- Tool instructions: "Use web search, web fetch, and Playwright browser tools to investigate company websites as the workflow directs."
- Stop behavior: "This skill may stop autonomously without escalation — if the company fails the tangible goods gate or is rejected as a general retailer/marketplace. In these cases the workflow produces no report. Report the outcome to the user."

- [ ] **Step 3: Verify line count and structure**

```bash
wc -l .claude/skills/product-classifier/SKILL.md
grep -c "^## " .claude/skills/product-classifier/SKILL.md
```

Expected: under 80 lines. Must have sections: Input, File locations, Workflow, Escalation handling, Notes.

### Task 3: Rewrite catalog-detector SKILL.md

**Files:**
- Modify: `.claude/skills/catalog-detector/SKILL.md`
- Reference (read-only): `.claude/skills/catalog-detector/references/workflow.md`

- [ ] **Step 1: Read the current SKILL.md**

Read `.claude/skills/catalog-detector/SKILL.md` (~43 lines).

- [ ] **Step 2: Rewrite to integrated template**

Same pattern as Task 2. Key differences for catalog-detector:
- Tool instructions: "Use web search, web fetch, and Playwright browser tools to investigate catalog pages as the workflow directs."
- Stop behavior: "This skill does not escalate — all decisions are autonomous stops. If the workflow determines scraping is not viable, it writes a minimal catalog assessment and stops. Report the outcome to the user."
- The `## Role in the four-level product record` section: update its cross-reference from `agents/scraper-generator/code-generator.md` to `.claude/skills/scraper-generator/references/code-generator.md`. Keep this section — it provides useful context.
- Reading the platform knowledgebase is optional note: keep in `## Workflow`.

- [ ] **Step 3: Verify line count and structure**

```bash
wc -l .claude/skills/catalog-detector/SKILL.md
grep -c "^## " .claude/skills/catalog-detector/SKILL.md
```

Expected: under 60 lines. Must have sections: Input, File locations, Role in the four-level product record, Workflow, Notes.

### Task 4: Rewrite scraper-generator SKILL.md

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md`
- Reference (read-only): `.claude/skills/scraper-generator/references/orchestrator.md`

- [ ] **Step 1: Read the current SKILL.md**

Read `.claude/skills/scraper-generator/SKILL.md` (~85 lines). This was already rewritten during the decomposition — it's close to the target state.

- [ ] **Step 2: Rewrite to integrated template**

Key changes from the current version:
- Replace `Read and follow the orchestrator agent instructions in agents/scraper-generator.md` with `Read and follow references/orchestrator.md`
- Replace the current `## Claude Code wiring` heading with `## Workflow`
- Update sub-agent dispatch to reference `references/` paths:
  - `references/label-discoverer.md` — non-English label discovery
  - `references/code-generator.md` — scraper.py generation
  - `references/validator.md` — probe testing and smoke tests
- Move escalation format + user options to `## Escalation handling` section
- Update `### Product record format` pointer to: "The canonical definition lives in `references/code-generator.md`."
- Keep: slug derivation, file locations table, execution commands (uv run, timeouts, probe), tool restrictions, data persistence instructions

- [ ] **Step 3: Verify line count and structure**

```bash
wc -l .claude/skills/scraper-generator/SKILL.md
grep -c "^## " .claude/skills/scraper-generator/SKILL.md
```

Expected: under 100 lines. Must have: Input, File locations, Workflow, Escalation handling, Notes.

### Task 5: Rewrite eval-generator SKILL.md

**Files:**
- Modify: `.claude/skills/eval-generator/SKILL.md`
- Reference (read-only): `.claude/skills/eval-generator/references/workflow.md`

- [ ] **Step 1: Read the current SKILL.md**

Read `.claude/skills/eval-generator/SKILL.md` (~78 lines).

- [ ] **Step 2: Rewrite to integrated template**

Key changes:
- Replace agent pointer with `Read and follow references/workflow.md`
- Replace `## Claude Code wiring` with `## Workflow`
- Update cross-reference in `## Eval and the four-level product record` from `agents/scraper-generator/code-generator.md` to `.claude/skills/scraper-generator/references/code-generator.md`
- Move escalation handling to its own section
- Keep: file locations, slug derivation, eval script execution command, tool restrictions

- [ ] **Step 3: Verify line count and structure**

```bash
wc -l .claude/skills/eval-generator/SKILL.md
grep -c "^## " .claude/skills/eval-generator/SKILL.md
```

Expected: under 90 lines. Must have: Input, File locations, Eval and the four-level product record, Workflow, Escalation handling, Notes.

---

## Chunk 2: Rewrite orchestrator, conventions, and cross-references

### Task 6: Rewrite product-discovery orchestrator

**Files:**
- Modify: `.claude/skills/product-discovery/SKILL.md`

- [ ] **Step 1: Read the current product-discovery SKILL.md**

Read `.claude/skills/product-discovery/SKILL.md` (~191 lines). Note all references to `agents/` paths and to reading agent files.

- [ ] **Step 2: Replace stage dispatch instructions**

For each of the 4 stages, replace the current two-step pattern:

```
Read file locations from `.claude/skills/{name}/SKILL.md`,
then read and follow `agents/{name}.md` in full.
```

With:

```
Invoke `/product-classifier {slug}`.
```

(Replace `product-classifier` with the appropriate skill name for each stage.)

- [ ] **Step 3: Update the slug derivation reference**

Replace line 47's reference:
```
see the slug derivation algorithm in `agents/product-classifier.md` Step 1
```
With:
```
see the slug derivation algorithm in `.claude/skills/product-classifier/references/workflow.md` Step 1
```

- [ ] **Step 4: Update the product record format reference**

Replace the scraper-generator stage description's reference:
```
see scraper-generator skill for the canonical definition
```
With:
```
see `.claude/skills/scraper-generator/references/code-generator.md` for the canonical definition
```

- [ ] **Step 5: Remove agent file reading instructions**

Remove lines 39 and 47 that tell the orchestrator how to read agent files:
- "Each stage has a corresponding skill file... that defines the file locations for that stage. Use those paths when providing files to the agent — the agents themselves are harness-agnostic and use logical resource names."
- Replace with: "Each stage is a self-contained skill. Invoke it and follow its instructions."

- [ ] **Step 6: Verify no agents/ references remain**

```bash
grep -n "agents/" .claude/skills/product-discovery/SKILL.md
```

Expected: 0 matches.

### Task 7: Rewrite skill-creator-local SKILL.md and create conventions.md

**Files:**
- Modify: `.claude/skills/skill-creator-local/SKILL.md`
- Create: `.claude/skills/skill-creator-local/references/conventions.md`

This is the heaviest content task. The current 567-line SKILL.md splits into ~200-line SKILL.md + ~200-line conventions.md.

- [ ] **Step 1: Read the current skill-creator-local SKILL.md**

Read `.claude/skills/skill-creator-local/SKILL.md` (567 lines). Map which content stays in SKILL.md vs moves to conventions.md.

**Stays in SKILL.md:**
- Frontmatter
- Architecture section (simplified — one pattern: "SKILL.md + references/", plus standalone note)
- Skill Writing Best Practices (progressive disclosure, description, writing style, output format, domain organization) — these are general guidance, not conventions
- Change Routing → DELETED (no wrapper vs agent decision)
- Workflow: Creating a New Pipeline Stage (simplified checklist)
- Workflow: Reviewing an Existing Skill (simplified)
- Relationship to Skill-Creator Plugin
- Scripts section
- Reference Files section
- Pointer: "Read `references/conventions.md` for the full convention definitions."

**Moves to conventions.md:**
- Convention 1: Skill Structure (rewritten from old Convention 1 — integrated template, no wrapper/agent split)
- Convention 2: Workflow Reference Structure (rewritten from old Convention 2 — references/workflow.md template, decomposition pattern, soft boundary guideline)
- Convention 3: Reference Integrity (simplified from old Convention 3 — referenced files must exist, escalation alignment, cross-skill full paths)
- Convention 4: Orchestrator Integration (simplified from old Convention 5 — `/skill-name` invocation, stop conditions)

- [ ] **Step 2: Write references/conventions.md**

Create `.claude/skills/skill-creator-local/references/conventions.md` with the 4 new conventions. Each convention should be a `##` section.

**Convention 1: Skill Structure** — the integrated SKILL.md template from the spec (lines 94-137). Include: frontmatter requirements, required sections (Input, File locations, Workflow, Escalation handling, Notes), the 500-line limit guideline.

**Convention 2: Workflow Reference Structure** — the references/workflow.md template (spec lines 148-171). Include: step structure, decision blocks, self-verification, report templates, strict format rules. Add: decomposition pattern for >3,000-word workflows (orchestrator + sub-agent files in references/). Add: soft boundary guideline — "SKILL.md focuses on wiring, references/ focuses on reasoning. Guideline, not hard rule." Add: sub-agent reference files should stay lean and tool-name-free.

**Convention 3: Reference Integrity** — simplified rules:
- Every file referenced in SKILL.md's workflow section must exist in `references/`
- Escalation decisions listed in SKILL.md must match Decision blocks in workflow.md
- Cross-skill references use full paths: `.claude/skills/{name}/references/{file}`
- Logical resource names in workflow.md must be mapped in SKILL.md's file locations table or workflow instructions

**Convention 4: Orchestrator Integration** — product-discovery invokes `/skill-name`. Every stage stop condition must appear in the orchestrator's "Stop the pipeline if" list.

- [ ] **Step 3: Rewrite SKILL.md**

Rewrite the SKILL.md keeping the content listed in Step 1's "Stays in SKILL.md" section. Key changes:

- Architecture section: replace "Two Skill Patterns" (wrapper+agent vs standalone) with one pattern: "SKILL.md + references/" with a note that standalone skills (product-taxonomy, skill-creator-local) may skip references/ if content fits in SKILL.md.
- Remove entirely: "Change Routing: What Goes Where" section, "What belongs in Claude Code wiring" section, "Sub-agent dispatch (orchestrator pattern)" section, "Three rules of environment agnosticism", "Sub-agent reference integrity" (all moved to conventions.md or eliminated).
- Add pointer: "Read `references/conventions.md` for the full convention definitions."
- Update self-review checklist to reflect new pattern (no more "agent file uses no tool names" check, etc.)
- Update workflow sections (Creating/Reviewing) to reference new file locations.

- [ ] **Step 4: Verify line counts**

```bash
wc -l .claude/skills/skill-creator-local/SKILL.md
wc -l .claude/skills/skill-creator-local/references/conventions.md
```

Expected: SKILL.md ≤250 lines, conventions.md ≤250 lines.

- [ ] **Step 5: Verify no agents/ references remain**

```bash
grep -rn "agents/" .claude/skills/skill-creator-local/
```

Expected: 0 matches.

### Task 8: Rewrite verify_skill.py

**Files:**
- Modify: `.claude/skills/skill-creator-local/scripts/verify_skill.py`

- [ ] **Step 1: Read the current verify_skill.py**

Read `.claude/skills/skill-creator-local/scripts/verify_skill.py`. Map all `agents/`-dependent code.

- [ ] **Step 2: Fix find_repo_root()**

Replace the current check (line 30):
```python
if (path / "agents").is_dir() and (path / ".claude" / "skills").is_dir():
```
With:
```python
if (path / ".claude" / "skills").is_dir():
```

- [ ] **Step 3: Replace AGENTS_DIR with references helper**

Remove:
```python
AGENTS_DIR = REPO_ROOT / "agents"
```

Add a helper function:
```python
def references_dir(skill_name):
    """Return the references/ directory for a skill."""
    return SKILLS_DIR / skill_name / "references"
```

- [ ] **Step 4: Update check_skill_wrapper()**

Replace the agent reference check (line 221):
```python
if f"agents/{skill_name}.md" not in content:
```
With a check for references/workflow.md OR references/orchestrator.md:
```python
has_workflow_ref = "references/workflow.md" in content or "references/orchestrator.md" in content
if not has_workflow_ref:
    issues.append(Issue("critical", check, "Missing workflow reference (references/workflow.md or references/orchestrator.md)"))
```

- [ ] **Step 5: Rename check_agent_file() to check_workflow_reference()**

Rename the function. Update it to:
- Read from `references/workflow.md` or `references/orchestrator.md` (for decomposed skills)
- Keep: step structure checks, decision block format, self-verification, strict format rules, decision-step references
- Remove: the hard environment agnosticism checks (`tool_names` list, `path_pattern` regex). Replace with advisory-level notes:
```python
# Advisory: prefer capability-focused language in workflow references
for tool in ["WebSearch", "WebFetch", "Playwright", "Bash tool"]:
    if tool in content:
        issues.append(Issue("minor", check, f"Workflow reference mentions tool name '{tool}' — prefer capability-focused language"))
```
- Remove: the skill name reference check (line 321 — `/skill-name` references are now expected in orchestrator workflows)

- [ ] **Step 6: Update check_subagent_pattern()**

Repoint from `AGENTS_DIR / skill_name` to `references_dir(skill_name)`. The function should:
- Look for `.md` files in `references/` that are NOT `workflow.md`, `orchestrator.md`, or `persist-hooks.md` — those are sub-agent files
- Actually, better approach: check if `references/orchestrator.md` exists — if so, this is a decomposed skill. Sub-agent files are all other `.md` files in `references/` except `persist-hooks.md` and `orchestrator.md`.
- Keep: sub-agent files must not have Decision blocks, word count ≤2,500
- Soften: tool name and path checks to advisory level (minor severity)

- [ ] **Step 7: Update check_cross_references()**

Update to check `references/` paths instead of `agents/` paths. Add: validate that cross-skill references using full paths (`.claude/skills/{name}/references/{file}`) resolve to existing files.

- [ ] **Step 8: Update the verify_skill() main function**

Replace:
```python
agent_path = AGENTS_DIR / f"{skill_name}.md"
```
With logic to find the workflow reference:
```python
refs_dir = references_dir(skill_name)
workflow_path = refs_dir / "workflow.md"
orchestrator_path = refs_dir / "orchestrator.md"
workflow_content = read_file(workflow_path) or read_file(orchestrator_path)
```

Update the call from `check_agent_file` to `check_workflow_reference`.

- [ ] **Step 9: Run the script to verify it works**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
```

Expected: script runs without crashes. Issues may exist (cross-references being updated in Task 9), but no Python errors.

### Task 9: Update CLAUDE.md and remaining cross-references

**Files:**
- Modify: `CLAUDE.md`
- Modify: `.claude/skills/product-taxonomy/SKILL.md`

- [ ] **Step 1: Update CLAUDE.md Key Directories**

Remove:
```
- `agents/` — Harness-agnostic agent files (shared reasoning, no tool names or file paths)
```

Update the `.claude/skills/` description:
```
- `.claude/skills/` — Claude Code skill wrappers (file paths, tool wiring, escalation handling)
```
To:
```
- `.claude/skills/` — Pipeline skills (SKILL.md + references/ for each stage)
```

- [ ] **Step 2: Update CLAUDE.md Architecture**

Update the "Expensive tier" description:
```
**Expensive tier** — LLM agents classify companies, detect catalogs, generate scrapers and evals.
```
To:
```
**Expensive tier** — LLM skills classify companies, detect catalogs, generate scrapers and evals.
```

- [ ] **Step 3: Update CLAUDE.md Git section**

Replace:
```
`.claude/` (skills, settings) and `agents/` are always tracked — never gitignore them.
```
With:
```
`.claude/` (skills, settings) is always tracked — never gitignore it.
```

- [ ] **Step 4: Update CLAUDE.md Conventions**

Replace:
```
- **After every change to any skill or agent file**, run `/skill-creator-local deep review` to verify convention compliance. This is not optional.
- Skill wrappers and agent files are a paired two-file pattern. See `/skill-creator-local` for the full convention spec.
- Run `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all` to check convention compliance.
- Taxonomy IDs (e.g., `machinery.power_tools`) are the canonical identifiers — always from `docs/product-taxonomy/categories.md`.
- Agent files must be harness-agnostic: no tool names, no file paths, no user-facing language.
- The product taxonomy categories file is read-only for all skills except product-taxonomy.
```

With:
```
- **After every change to any skill file**, run `/skill-creator-local deep review` to verify convention compliance. This is not optional.
- Each pipeline skill is self-contained under `.claude/skills/{name}/` with SKILL.md + references/. See `/skill-creator-local` for conventions.
- Run `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all` to check convention compliance.
- Taxonomy IDs (e.g., `machinery.power_tools`) are the canonical identifiers — always from `docs/product-taxonomy/categories.md`.
- The product taxonomy categories file is read-only for all skills except product-taxonomy.
```

- [ ] **Step 5: Update product-taxonomy SKILL.md cross-reference**

In `.claude/skills/product-taxonomy/SKILL.md`, find:
```
see scraper-generator skill for the full four-level product record format
```
Replace with:
```
see `.claude/skills/scraper-generator/references/code-generator.md` for the full four-level product record format
```

- [ ] **Step 6: Final grep for any remaining agents/ references**

```bash
grep -rn "agents/" .claude/skills/ CLAUDE.md --include="*.md" --include="*.py" | grep -v "docs/superpowers/"
```

Expected: 0 matches. (The `grep -v "docs/superpowers/"` excludes historical spec/plan files which are left as-is.)

---

## Chunk 3: Verification and completion

### Task 10: Full verification

**Files:**
- None (verification only)

- [ ] **Step 1: Run verify_skill.py --all**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
```

Expected: 0 critical, 0 moderate issues for all skills. The catalog-detector word count warning (pre-existing, 3,193 words) is acceptable.

- [ ] **Step 2: Verify target directory structure**

```bash
# All workflow references exist
ls .claude/skills/product-classifier/references/workflow.md
ls .claude/skills/catalog-detector/references/workflow.md
ls .claude/skills/eval-generator/references/workflow.md
ls .claude/skills/scraper-generator/references/orchestrator.md
ls .claude/skills/scraper-generator/references/label-discoverer.md
ls .claude/skills/scraper-generator/references/code-generator.md
ls .claude/skills/scraper-generator/references/validator.md
ls .claude/skills/scraper-generator/references/persist-hooks.md
ls .claude/skills/skill-creator-local/references/conventions.md

# agents/ is gone
test ! -d agents/ && echo "OK: agents/ deleted"
```

- [ ] **Step 3: Verify no broken references**

```bash
# No agents/ references outside historical docs
grep -rn "agents/" .claude/skills/ CLAUDE.md --include="*.md" --include="*.py" | grep -v "docs/superpowers/"

# All cross-skill references resolve
for ref in $(grep -roh '\.claude/skills/[a-z-]*/references/[a-z-]*.md' .claude/skills/ CLAUDE.md); do
  test -f "$ref" || echo "BROKEN: $ref"
done
```

Expected: no agents/ references, no broken cross-skill references.

- [ ] **Step 4: Verify SKILL.md line counts**

```bash
wc -l .claude/skills/*/SKILL.md
```

Expected: all under 500 lines. Product-classifier ~70, catalog-detector ~55, scraper-generator ~95, eval-generator ~85, product-discovery ~190, product-taxonomy ~275, skill-creator-local ~250.

- [ ] **Step 5: Present diff for review**

Show the full `git diff --stat` and key changes for user review before any commit.
