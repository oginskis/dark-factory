# Pipeline Skill Conventions

These conventions define the structure and rules for pipeline skills in this repository.

---

## Convention 1: Skill Structure

Every pipeline skill follows this structure. The SKILL.md is the single entry point.

```markdown
---
name: {skill-name}
description: >
  {What it does — first sentence.}
  {What it produces — second sentence.}
  {When to use — trigger phrases and contexts.}
  {Prerequisites — name the specific upstream skill, e.g., "Requires a company report from /product-classifier".}
  {Pipeline redirect — when to use /product-discovery instead, or note if independent.}
user-invocable: true
---

# {Skill Title}

{One-line summary — what value this skill provides to the downstream consumer.}

## Input

`$ARGUMENTS` is {description of expected input} (e.g., `{example}`).

## File locations

| Resource | Path |
|----------|------|
| {Upstream input} | `docs/{upstream-stage}/{slug}.md` |
| {Other inputs} | `docs/...` |
| {Output} | `docs/{this-stage}/{slug}.md` |

### {Optional: Slug derivation}

{When slug computation is non-trivial (multiple slug types like `{slug}`, `{category-slug}`, `{platform-slug}`), add a `### Slug derivation` subsection under File locations. Omit for simple skills where the slug is just the company slug from $ARGUMENTS.}

## {Optional: Domain context section}

{When a skill needs to explain its role relative to shared concepts, add a domain context section between File locations and Workflow. Omit when not needed.}

## Workflow

Read and follow `references/workflow.md`.

- Provide the file paths from the table above when the workflow references logical resources (e.g., "{logical name 1}", "{logical name 2}").
- {Tools to use — web search, web fetch, Playwright, etc. Or "No web search or Playwright needed."}
- {Autonomous stop behavior — describe if the skill stops without escalation.}

## Escalation handling

{Escalation format template — identical across all escalating skills.}
{User options per escalation decision.}

(Omit this section for skills that do not escalate — e.g., catalog-detector.)

## Notes

{Only include if there's something genuinely useful to say — skill ownership, unusual behaviors, operational constraints. Omit or keep minimal if there's nothing worth noting.}
```

### SKILL.md rules

| Rule | Why |
|------|-----|
| **Description includes trigger phrases** | Prevents undertriggering — Claude needs explicit cues |
| **Prerequisites name the specific upstream skill** | "Requires a company report from /product-classifier" not "requires upstream data" |
| **Description mentions pipeline redirect** | Prevents confusion between individual stages and full pipeline |
| **File locations table is exhaustive** | Every file the workflow reads or writes must have a row |
| **One-line summary describes value to downstream consumer** | Forces purpose-driven thinking |
| **Workflow section lists all escalation points with user options** | User must know what actions they can take on escalation |
| **Workflow explicitly describes stop behavior** | Harness needs to know the skill may terminate without output |
| **Workflow examples match logical resource names exactly** | Prevents mapping errors between SKILL.md and references/ |
| **SKILL.md stays under 500 lines** | Progressive disclosure — detail belongs in references/ |

### Escalation presentation format

When the workflow escalates, the harness presents the decision to the user. Every escalation presentation includes:
1. **Decision name** — which decision was triggered
2. **Stage** — which pipeline stage hit the issue
3. **Context** — what was encountered
4. **Payload** — the specific evidence or candidates gathered
5. **Numbered options** — clear actions the user can take to resolve or stop

The workflow section lists each escalation decision with its numbered options. Example:

```
- `ambiguous_company` — 1) Pick a candidate, 2) Provide additional context, 3) Stop
- `category_not_found` — 1) Suggest a new subcategory, 2) Pick the closest existing, 3) Stop
```

Every escalation must include a "Stop" option so the user can always halt cleanly.

---

## Convention 2: Workflow Reference Structure

The `references/workflow.md` file contains all reasoning, decision logic, and report templates. It describes *what to do and decide* — the SKILL.md handles *how to interact*.

### Workflow template

```markdown
# {Skill Name} Workflow

**Input:** {what the workflow receives}
**Output:** {what it produces — describe value to downstream consumer}

---

## Context

{What this workflow does, its role in the pipeline, what the downstream consumer needs.}

## Step 1: {First Action}
{Instructions}
{Decision references: "stop — see the `{decision_name}` decision"}

---

## Step N: Write {Output Name}
{Report template(s) — success and stop variants if applicable}

### Strict format rules
{Correct/Wrong table}

---

## Step N+1: Self-Verification
{Quality gates table}

---

## {Optional: Investigation Guidance}

## Boundaries

{What this workflow does NOT do.}

---

## Decisions
{All decision blocks, each following the escalation pattern below}
```

**Required sections:** `## Context`, `## Boundaries`, and `## Decisions` are mandatory in every workflow and orchestrator file. Only `## Investigation Guidance` is optional.

### Escalation pattern (every decision block)

```markdown
### Decision: {snake_case_name}

**Context:** {what situation triggers this decision}
**Autonomous resolution:** {rule for auto-deciding, or "Never"}
**Escalate when:** {conditions, or "Never" if autonomous stop}
**Escalation payload:** {what info to pass, or "N/A"}
```

### Workflow rules

| Rule | Why |
|------|-----|
| **Every step that can stop/escalate references the decision by name** | Prevents orphaned decisions |
| **Sub-steps use letter suffixes** (e.g., `## Step 1b:`) | Complex steps can split into logically distinct phases |
| **Report templates include both success and stop variants** | Stop cases must produce a minimal report |
| **Strict format rules table after each report template** | Correct/Wrong columns prevent formatting errors |
| **Self-verification step with numbered quality gates** | Workflow must check its own output before completing |
| **Decisions section is always last** | Consistent location for harness to find definitions |
| **No duplicated steps across branches** | If writing "Same as Step X", make it a shared step instead |
| **Output designed for downstream consumer** | Not a generic survey — every section should help the next stage |

### Branching workflows

When a workflow has variants (e.g., fast path vs. full investigation), structure it so that only the actual divergence is branched. Share everything before and after:

```
Step 1: Shared setup/detection
Step 2: Fast path (branch A)        ← only these differ
Step 3: Full investigation (branch B)
Step 4: Shared output building      ← uses results from whichever branch ran
Step 5: Shared report writing
Step 6: Shared verification
```

**Test:** If a step in one branch says "Same as Step X in the other branch", it should be a shared step after the branches merge. This typically cuts 30-40% of workflow length.

### Decomposition pattern

When a workflow exceeds ~3,000 words (~4,000 tokens), instruction-following degrades. Decompose into an orchestrator plus sub-workflows:

```
.claude/skills/{name}/
├── SKILL.md
└── references/
    ├── orchestrator.md        <- orchestrator (replaces workflow.md for decomposed skills)
    ├── {phase-1}.md           <- sub-workflow (focused task, own context window)
    ├── {phase-2}.md           <- sub-workflow
    └── {phase-3}.md           <- sub-workflow
```

For decomposed skills, SKILL.md says `Read and follow `references/orchestrator.md`.` instead of `references/workflow.md`.

**Decomposition criteria** — split along phases that:
- Have distinct cognitive tasks (discovery vs generation vs validation)
- Produce a defined output that the next phase consumes
- Can fail independently with their own circuit breakers

**The orchestrator keeps:** context loading, state machine logic, all Decision blocks, self-verification gates, short final steps.

**Sub-workflows receive:** their own instruction file (read at dispatch time) and structured input from the orchestrator.

**Sub-workflow rules:**
- Each sub-workflow stays under ~2,500 words
- Input/output contracts are defined in the orchestrator
- Sub-workflows don't reference other sub-workflows or the orchestrator by name
- Sub-workflows must have `**Input:**` and `**Output:**` one-line fields after the heading
- Sub-workflows must have `## Input Contract` and `## Output Contract` sections
- Heading must contain "Sub-Agent" (e.g., `# Label Discoverer Sub-Agent`)

### Soft boundary guideline

SKILL.md focuses on wiring (file paths, tools, escalation presentation). References/ focuses on reasoning (steps, decisions, templates, quality gates). This is a guideline for clarity, not a hard wall. Sub-workflow reference files dispatched via Agent tool should stay lean and tool-name-free so they can port to other harnesses.

---

## Convention 3: Reference Integrity

These rules prevent the most common bugs — broken references between SKILL.md and references/.

### Logical resource name mapping

Every logical resource name used in the workflow must appear in the SKILL.md workflow section's mapping, and must correspond to a row in the File locations table.

**Check:** grep the workflow file for phrases like "the company report", "the product taxonomy categories file". Each must appear as an example in the SKILL.md workflow bullet.

### Escalation/stop alignment

1. Every `Decision:` block in the workflow must be either:
   - Listed as an escalation point in SKILL.md's workflow section (if it escalates), or
   - Covered by the stop behavior description (if autonomous stop)
2. Every escalation point listed in SKILL.md must exist as a `Decision:` block in the workflow
3. Every stop condition must appear in the orchestrator's `**Stop the pipeline if:**` list for that stage

### Cross-skill references

When one skill references another skill's files, use full paths: `.claude/skills/{name}/references/{file}`. Never use relative paths across skill boundaries.

### Taxonomy references

When the workflow references the product taxonomy, use the full logical name "the product taxonomy categories file" — not shortened forms like "the taxonomy file." This prevents ambiguity with SKU schema files.

---

## Convention 4: Orchestrator Integration

The product-discovery orchestrator (`.claude/skills/product-discovery/SKILL.md`) chains all pipeline stages. When adding or modifying a stage:

1. Add/update the `## Stage N:` section with:
   - `Invoke /skill-name {slug}.`
   - One-line description of what the stage does
   - `**Stop the pipeline if:**` list matching ALL stop/escalation conditions from the workflow
2. Update the escalation instruction at the top if the new stage's escalation behavior differs
3. Update `## Pipeline Summary` if the stage produces additional output files

Every stage's stop conditions must appear in the orchestrator's stop list — this is the single source of truth for pipeline halting behavior.

---

## Convention 5: Script Infrastructure

Script everything mechanical. If a step is repeatable, doesn't need LLM judgment, and produces structured data — it belongs in a Python script, not in the workflow prose. Scripts reduce token cost (run once per company, not per-conversation), improve consistency (same logic every time), and make output inspectable (JSON files on disk).

### When to script

| Script it | Don't script it |
|-----------|-----------------|
| Data gathering (fetch pages, parse sitemaps, detect platforms) | Deciding what strategy to use |
| Validation gates (check report structure, verify required fields) | Writing the report itself |
| Evidence collection (test selectors, check anti-bot, verify recipes) | Interpreting ambiguous results |
| Any check that can be expressed as code | Anything requiring web browsing with judgment |

**Rule of thumb:** If you find yourself writing "check that X exists and Y matches pattern Z" in a workflow step, that's a script.

### Script directory structure

```
.claude/skills/{name}/
├── SKILL.md
├── references/
│   └── workflow.md
└── scripts/
    ├── _lib.py              ← shared infrastructure (HTTP, logging); NOT standalone
    ├── {action_1}.py        ← focused tactical script; standalone via uv run
    ├── {action_2}.py        ← focused tactical script
    ├── {orchestrator}.py    ← thin coordinator; runs tactical scripts as subprocesses
    └── {validator}.py       ← validates the skill's output report
```

### Script design rules

| Rule | Why |
|------|-----|
| **PEP 723 inline metadata** | Each script is standalone-runnable with `uv run script.py` — no setup, no virtualenv |
| **JSON to stdout, logs to stderr** | Output is structured data the LLM can parse; logs are for humans debugging |
| **Exit code contract: 0 = full, 1 = partial, 2 = crash** | LLM routes on exit code — 0/1 = use the output, 2 = fall back to manual |
| **Evidence not decisions** | Scripts report what they found. The LLM decides what to do with it. No pass/fail verdicts that hide reasoning |
| **Null = not found, errors[] = couldn't check** | Distinguishes "field is absent" from "script failed to check" — prevents false negatives |
| **Immutable during pipeline runs** | Never edit scripts mid-run. Record bugs in the report's Platform-Specific Notes; fix in a dedicated maintenance pass |
| **One responsibility per script, ~150-300 lines** | Small enough to reason about in isolation. If a script mixes concerns, split it |
| **No info-level fetch logging** | Don't log every HTTP request. Only log warnings (timeouts, rate limits) and errors (crashes, parse failures) |

### Shared library pattern

Extract shared infrastructure (HTTP client, logging, challenge detection) into a `_lib.py` file. Tactical scripts import from it:

```python
from _lib import fetch, log, make_client, TransportTracker
```

`_lib.py` is NOT a standalone script — no PEP 723 block, no `if __name__`. Python's `sys.path[0]` = script directory makes sibling imports work with `uv run`.

### Script documentation — three layers

Scripts must be self-documenting for the LLM. Three layers, each serving a different purpose:

**Layer 1: Module docstring** — when to call, what args, exit codes, interpretation guide:
```python
"""
Fetch a website's homepage and assess transport health.

WHEN TO CALL: First script in the probe pipeline. No preconditions.
ARGUMENTS: --url (required), --timeout (default: 15.0)
EXIT CODES: 0 = full result, 1 = partial, 2 = crash

INTERPRETATION:
    transport_health == "blocked" → stop immediately
    transport_health == "degraded" → proceed but note in report
"""
```

**Layer 2: Inline comments on output fields** — what each value means to the caller:
```python
result = {
    "recipe_match": recipe_match,
    # "full"     → recipe verified; use fast path
    # "partial"  → some checks passed; verify manually
    # "poor"     → most failed; check if URLs were category pages
    # "untested" → no product URLs supplied
}
```

**Layer 3: Validation gate docstrings** — what it checks, what failure means, how to fix:
```python
def check_price_verified(content: str) -> dict:
    """
    WHAT IT CHECKS: Price section has >=2 URLs with observed values.
    FAILURE MEANS: Price selector written without testing on real pages.
    HOW TO FIX: Navigate to 2+ product pages, record URLs with prices.
    """
```

### Orchestrator pattern

When a skill has multiple tactical scripts, add a thin orchestrator that:
1. Runs tactical scripts as subprocesses (via `subprocess.run(["uv", "run", ...])`)
2. Saves each script's JSON output to `{output-dir}/{script_name}.json`
3. Merges all stderr into `{output-dir}/{stage}.log`
4. Assembles a combined JSON to stdout
5. Handles early-exit conditions (e.g., skip remaining scripts if site is blocked)

The orchestrator contains NO analysis logic — only coordination, file I/O, and JSON assembly.

### Per-slug output directories

Script output goes to `docs/{stage}/{slug}/` with individual JSON files per script:

```
docs/{stage}/{slug}/
    {script_1}.json     ← individual script result
    {script_2}.json     ← individual script result
    {stage}.log         ← merged stderr from all scripts
    assessment.md       ← the skill's main output report
    validate.json       ← validation gate results
    validate.log        ← validation stderr
```

This makes every intermediate result inspectable — when something goes wrong, you can check the individual JSON file instead of re-running the entire pipeline.

### SKILL.md integration

When a skill has scripts, the SKILL.md Workflow section includes:
- The exact `uv run` command with argument placeholders
- Routing logic based on script output fields (e.g., "if recipe_match is 'full' AND transport_health is 'healthy' → skip Steps 1-3")
- The immutability rule: "DO NOT modify the script. If it produces unexpected results, fall back to manual reasoning."
