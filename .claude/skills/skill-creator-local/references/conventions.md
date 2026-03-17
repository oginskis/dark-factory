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
