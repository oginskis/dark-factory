#!/usr/bin/env python3
"""
Verify a skill follows the dark-factory pipeline conventions (pure-skills pattern).

Usage:
    python verify_skill.py <skill-name>
    python verify_skill.py product-classifier
    python verify_skill.py --all

Checks:
  1. Skill wrapper structure (required sections, frontmatter)
  2. Skill structure (summary line, workflow delegation, escalation template, notes)
  3. Workflow reference structure (heading, Context/Boundaries/Decisions sections, steps, ordering)
  4. Cross-file reference integrity (logical names, decisions, file locations, escalation template markers)
  5. Orchestrator alignment (stop conditions)
  6. Report template compliance (heading, date, sections)
  7. Decision-step references (steps must point to decisions by name)

Exit code 0 = all checks pass, 1 = failures found.
"""

import sys
import re
from pathlib import Path


def find_repo_root():
    """Walk up from script location to find the repo root (directory containing .claude/skills/)."""
    path = Path(__file__).resolve().parent
    for _ in range(10):
        if (path / ".claude" / "skills").is_dir():
            return path
        path = path.parent
    raise RuntimeError("Cannot find repo root (directory with .claude/skills/)")


REPO_ROOT = find_repo_root()
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
ORCHESTRATOR = SKILLS_DIR / "product-discovery" / "SKILL.md"


def references_dir(skill_name):
    """Return the references/ directory for a skill."""
    return SKILLS_DIR / skill_name / "references"


# Skills that follow the standalone pattern (no workflow reference, reduced checks)
STANDALONE_SKILLS = {"product-taxonomy", "product-discovery", "skill-creator-local"}


class Issue:
    def __init__(self, severity, check, message):
        self.severity = severity  # "critical", "moderate", "minor"
        self.check = check
        self.message = message

    def __str__(self):
        icon = {"critical": "!!!", "moderate": " ! ", "minor": " . "}[self.severity]
        return f"  [{icon}] {self.check}: {self.message}"


def read_file(path):
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def extract_h2_sections(content):
    """Extract ## section headings in order."""
    return re.findall(r"^## (.+)$", content, re.MULTILINE)


def extract_decisions(content):
    """Extract Decision: names from workflow reference."""
    return re.findall(r"^### Decision: (\w+)", content, re.MULTILINE)


def extract_decision_blocks(content):
    """Extract full decision blocks with their escalation behavior."""
    blocks = {}
    pattern = r"### Decision: (\w+)\n\n(.*?)(?=\n### Decision:|\n---|\Z)"
    for match in re.finditer(pattern, content, re.DOTALL):
        name = match.group(1)
        body = match.group(2)
        # Check if "Escalate when:" contains "Never"
        esc_match = re.search(r"\*\*Escalate when:\*\*(.+?)$", body, re.MULTILINE)
        if esc_match:
            escalates = "Never" not in esc_match.group(1)
        else:
            escalates = False  # No "Escalate when" field — treat as non-escalating
        blocks[name] = {"body": body, "escalates": escalates}
    return blocks


def extract_file_locations(content):
    """Extract resource names from File locations table."""
    resources = []
    in_table = False
    for line in content.split("\n"):
        if "| Resource" in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2:
                resources.append({"name": parts[0], "path": parts[1]})
        elif in_table:
            in_table = False
    return resources


def extract_wiring_examples(content):
    """Extract logical resource name examples from wiring section."""
    examples = []
    wiring_match = re.search(r"## Workflow\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if wiring_match:
        wiring = wiring_match.group(1)
        examples = re.findall(r'"([^"]+)"', wiring)
    return examples


def extract_orchestrator_stops(content, stage_name):
    """Extract stop conditions for a given stage from the orchestrator."""
    pattern = rf"## Stage \d+: .*?{stage_name}.*?\n(.*?)(?=\n## Stage|\n## Pipeline|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    section = match.group(1)
    stops = re.findall(r"^- (.+)$", section, re.MULTILINE)
    return [s for s in stops if s.strip()]


def is_inside_code_block(content, position):
    """Check if a position in the content is inside a fenced code block."""
    # Count ``` fences before this position
    fences_before = content[:position].count("```")
    # Odd count means we're inside a code block
    return fences_before % 2 == 1


def extract_logical_refs_from_workflow(content):
    """Extract logical resource name references from workflow reference.

    Looks for patterns like:
    - "Read the company report"
    - "from the product taxonomy categories file"
    - "in the company reports directory"
    - "write the catalog assessment report"
    """
    patterns = [
        r'(?:Read|Write|Check|read|write|check|from|in|into)\s+the\s+([a-z][a-z ]+(?:file|report|directory|assessment|schema))',
        r'(?:Read|Write|Check|read|write|check|from|in|into)\s+the\s+(company report)',
        r'the\s+(product taxonomy categories file)',
        r'the\s+(catalog assessment(?:\s+report)?)',
        r'the\s+(company reports? directory)',
    ]
    refs = set()
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            if not is_inside_code_block(content, match.start()):
                refs.add(match.group(1).strip())
    return list(refs)


# ── Check functions ──────────────────────────────────────────────────────────


def check_standalone_skill(skill_name, content, issues):
    """Check standalone skill structure (no workflow reference, single-file pattern)."""
    check = "standalone-structure"

    # Frontmatter
    fm = extract_frontmatter(content)
    if "name" not in fm:
        issues.append(Issue("critical", check, "Missing 'name' in frontmatter"))
    elif fm["name"] != skill_name:
        issues.append(Issue("moderate", check, f"Frontmatter name '{fm['name']}' != directory name '{skill_name}'"))
    if "description" not in fm and "description:" not in content[:500]:
        issues.append(Issue("critical", check, "Missing 'description' in frontmatter"))
    if "user-invocable" not in fm:
        issues.append(Issue("moderate", check, "Missing 'user-invocable: true' in frontmatter"))

    # Input section (expected for all skills)
    sections = extract_h2_sections(content)
    if not any("input" in s.lower() for s in sections):
        issues.append(Issue("moderate", check, "Missing ## Input section"))


def check_skill_wrapper(skill_name, content, issues):
    """Check skill wrapper structure."""
    check = "wrapper-structure"

    # Frontmatter
    fm = extract_frontmatter(content)
    if "name" not in fm:
        issues.append(Issue("critical", check, "Missing 'name' in frontmatter"))
    elif fm["name"] != skill_name:
        issues.append(Issue("moderate", check, f"Frontmatter name '{fm['name']}' != directory name '{skill_name}'"))
    if "description" not in fm and "description:" not in content[:500]:
        issues.append(Issue("critical", check, "Missing 'description' in frontmatter"))
    if "user-invocable" not in fm:
        issues.append(Issue("moderate", check, "Missing 'user-invocable: true' in frontmatter"))

    # Required sections
    sections = extract_h2_sections(content)
    required = ["Input", "File locations", "Workflow", "Notes"]
    for req in required:
        if not any(req.lower() in s.lower() for s in sections):
            issues.append(Issue("critical", check, f"Missing required section: ## {req}"))

    # Workflow reference (references/workflow.md or references/orchestrator.md)
    has_workflow_ref = "references/workflow.md" in content or "references/orchestrator.md" in content
    if not has_workflow_ref:
        issues.append(Issue("critical", check, "Missing workflow reference (references/workflow.md or references/orchestrator.md)"))

    # Notes line
    if "File-driven skill" not in content:
        issues.append(Issue("minor", check, "Notes section missing standard 'File-driven skill' line"))

    # Description content checks
    desc_match = re.search(r"description:\s*>\s*\n((?:\s+.+\n)+)", content)
    if desc_match:
        desc = desc_match.group(1)
        if "/product-discovery" not in desc and "pipeline" not in desc.lower():
            issues.append(Issue("moderate", check, "Description should mention pipeline redirect or independence"))


def check_skill_structure(skill_name, content, issues):
    """Check SKILL.md section order and content consistency."""
    check = "skill-structure"

    # (a) One-line summary after # Title
    # After the first # heading, the next non-empty line should NOT be ## (meaning there's a summary)
    lines = content.split("\n")
    found_title = False
    for i, line in enumerate(lines):
        if not found_title and re.match(r"^# ", line) and not line.startswith("# ---"):
            found_title = True
            # Find next non-empty line after the title
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    if lines[j].startswith("## "):
                        issues.append(Issue("moderate", check,
                            "Missing one-line summary between # Title and first ## section"))
                    break
            break

    # (b) Workflow delegation line
    # The ## Workflow section must start with "Read and follow `references/workflow.md`."
    # or "Read and follow `references/orchestrator.md`." as its first content line
    workflow_match = re.search(r"^## Workflow\n(.*?)(?=\n## |\Z)", content, re.MULTILINE | re.DOTALL)
    if workflow_match:
        workflow_body = workflow_match.group(1)
        # Find first non-empty line in the workflow section
        first_content_line = ""
        for line in workflow_body.split("\n"):
            if line.strip():
                first_content_line = line.strip()
                break
        expected_lines = [
            "Read and follow `references/workflow.md`.",
            "Read and follow `references/orchestrator.md`.",
        ]
        if first_content_line not in expected_lines:
            issues.append(Issue("critical", check,
                "## Workflow must start with 'Read and follow `references/workflow.md`.' or 'Read and follow `references/orchestrator.md`.'"))

    # (c) Escalation template consistency
    # If ## Escalation handling exists, the template should say "the workflow gathered" not "the agent gathered"
    esc_match = re.search(r"^## Escalation handling\n(.*?)(?=\n## |\Z)", content, re.MULTILINE | re.DOTALL)
    if esc_match:
        esc_body = esc_match.group(1)
        if "the agent gathered" in esc_body:
            issues.append(Issue("moderate", check,
                "Escalation template says 'the agent gathered' — should say 'the workflow gathered'"))

    # (d) Standard Notes line — "File-driven skill"
    notes_match = re.search(r"^## Notes\n(.*?)(?=\n## |\Z)", content, re.MULTILINE | re.DOTALL)
    if notes_match:
        if "File-driven skill" not in notes_match.group(1):
            issues.append(Issue("minor", check, "## Notes section missing 'File-driven skill' line"))
    else:
        # No Notes section at all — already caught by check_skill_wrapper
        pass


def check_workflow_reference(skill_name, content, issues):
    """Check workflow reference file structure."""
    check = "workflow-structure"

    # Header — must say "Workflow" not "Agent"
    heading_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1)
        if heading.endswith(" Agent"):
            issues.append(Issue("moderate", check,
                f"Heading says '# {heading}' — should end with 'Workflow' not 'Agent'"))
        elif not heading.endswith(" Workflow"):
            issues.append(Issue("moderate", check,
                f"Heading '# {heading}' does not end with 'Workflow'"))
    else:
        issues.append(Issue("moderate", check, "Missing # heading"))

    # Must have ## Context section (not ## Purpose)
    h2_sections = extract_h2_sections(content)
    if "Purpose" in h2_sections:
        issues.append(Issue("moderate", check,
            "Has '## Purpose' — workflow/orchestrator files should use '## Context' instead"))
    if "Context" not in h2_sections:
        issues.append(Issue("moderate", check, "Missing '## Context' section"))

    # Must have ## Boundaries section
    if "Boundaries" not in h2_sections:
        issues.append(Issue("moderate", check, "Missing '## Boundaries' section"))

    # Must have ## Decisions section as last ## section
    if "Decisions" not in h2_sections:
        issues.append(Issue("critical", check, "Missing '## Decisions' section"))
    elif h2_sections[-1] != "Decisions":
        issues.append(Issue("moderate", check,
            f"'## Decisions' should be the last ## section, but '## {h2_sections[-1]}' comes after it"))

    if "**Input:**" not in content:
        issues.append(Issue("moderate", check, "Missing **Input:** field"))
    if "**Output:**" not in content:
        issues.append(Issue("moderate", check, "Missing **Output:** field"))

    # Steps (main + sub-steps like 1b, 2a)
    all_steps = re.findall(r"^## Step (\d+[a-z]?):", content, re.MULTILINE)
    main_steps = [s for s in all_steps if s.isdigit()]
    if not all_steps:
        issues.append(Issue("critical", check, "No numbered steps found"))
    elif len(all_steps) < 2:
        issues.append(Issue("moderate", check, f"Only {len(all_steps)} step(s) found — expected at least 2"))

    # Main step numbering is sequential
    for i, step_num in enumerate(main_steps):
        if int(step_num) != i + 1:
            issues.append(Issue("moderate", check, f"Step numbering gap: expected Step {i+1}, found Step {step_num}"))
            break

    # Sub-steps must have a parent main step
    for step in all_steps:
        if not step.isdigit():
            parent = re.match(r"(\d+)", step).group(1)
            if parent not in main_steps:
                issues.append(Issue("moderate", check, f"Sub-step {step} has no parent Step {parent}"))

    # Self-verification
    if "Self-Verification" not in content and "Self-verification" not in content:
        issues.append(Issue("moderate", check, "Missing Self-Verification step"))

    # Strict format rules
    if "Strict format rules" not in content and "format rules" not in content.lower():
        issues.append(Issue("moderate", check, "Missing Strict format rules table"))

    # Decisions section
    decisions = extract_decisions(content)
    if not decisions:
        issues.append(Issue("moderate", check, "No Decision: blocks found"))

    # Decision block format
    for dec in decisions:
        dec_pattern = rf"### Decision: {dec}\n\n.*?\*\*Context:\*\*"
        if not re.search(dec_pattern, content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Context:** field"))
        if not re.search(rf"### Decision: {dec}.*?\*\*Autonomous resolution:\*\*", content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Autonomous resolution:** field"))
        if not re.search(rf"### Decision: {dec}.*?\*\*Escalate when:\*\*", content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Escalate when:** field"))

    # Decision-step references: every decision should be referenced by name in a step
    for dec in decisions:
        # Look for the decision name referenced outside the Decisions section
        decisions_section_start = content.find("## Decisions")
        if decisions_section_start == -1:
            decisions_section_start = len(content)
        steps_content = content[:decisions_section_start]
        if f"`{dec}`" not in steps_content and dec not in steps_content.split("## Decisions")[0]:
            issues.append(Issue("moderate", check, f"Decision '{dec}' is defined but never referenced in any step"))

    # Advisory: prefer capability-focused language over tool names
    tool_names_advisory = ["WebSearch", "WebFetch", "Playwright", "Bash tool"]
    for tool in tool_names_advisory:
        if tool in content:
            issues.append(Issue("minor", check, f"Workflow reference mentions tool name '{tool}' — prefer capability-focused language"))

    # Taxonomy reference consistency
    if "taxonomy file" in content.lower() and "product taxonomy categories file" not in content:
        issues.append(Issue("moderate", check, "Uses shortened 'taxonomy file' — should use full name 'product taxonomy categories file'"))


def check_cross_references(skill_name, skill_content, workflow_content, issues):
    """Check cross-file reference integrity."""
    check = "cross-references"

    # Extract data from both files
    file_locations = extract_file_locations(skill_content)
    wiring_examples = extract_wiring_examples(skill_content)
    decision_blocks = extract_decision_blocks(workflow_content)

    # Check: every workflow logical resource name should appear in wiring examples
    logical_refs = extract_logical_refs_from_workflow(workflow_content)
    for ref in logical_refs:
        ref_lower = ref.lower().strip()
        # Normalize: strip leading adjectives like "full" and trailing qualifiers like "for an existing report"
        ref_core = re.sub(r'^(full|the)\s+', '', ref_lower)
        ref_core = re.sub(r'\s+(for|from|in|to|of)\s+.*$', '', ref_core)
        # Check if any wiring example contains the core reference
        matched = False
        for ex in wiring_examples:
            ex_lower = ex.lower()
            if ref_core in ex_lower or ex_lower in ref_core or ref_lower in ex_lower or ex_lower in ref_lower:
                matched = True
                break
        if not matched:
            issues.append(Issue("moderate", check, f"Workflow references '{ref}' but it's not in wrapper wiring examples"))

    # Check: every decision should be reflected in wrapper wiring
    escalating = [name for name, block in decision_blocks.items() if block["escalates"]]
    non_escalating = [name for name, block in decision_blocks.items() if not block["escalates"]]

    # Escalating decisions should be listed in wiring
    for dec in escalating:
        if dec not in skill_content:
            issues.append(Issue("critical", check, f"Escalating decision '{dec}' not mentioned in wrapper wiring"))

    # Non-escalating decisions should be covered by stop behavior description
    if non_escalating:
        # Check for explicit stop/autonomous language in the wiring section
        wiring_match = re.search(r"## Workflow\n(.*?)(?=\n## |\Z)", skill_content, re.DOTALL)
        wiring_text = wiring_match.group(1) if wiring_match else ""
        has_stop_description = any(phrase in wiring_text.lower() for phrase in [
            "does not escalate",
            "autonomous stop",
            "stop autonomously",
            "stops autonomously",
            "writes a minimal",
            "no report",
            "graceful degradation",
            "handled autonomously",
            "without escalation",
        ])
        if not has_stop_description:
            issues.append(Issue("moderate", check,
                f"Workflow has autonomous stops ({', '.join(non_escalating)}) but wrapper wiring doesn't describe stop behavior"))

    # Check: file locations cover workflow's read/write needs
    if not file_locations:
        issues.append(Issue("critical", check, "Wrapper has no File locations table"))

    # Check: escalation template cross-consistency
    # If SKILL.md has ## Escalation handling, verify the template has the key structural markers
    esc_match = re.search(r"^## Escalation handling\n(.*?)(?=\n## |\Z)", skill_content, re.MULTILINE | re.DOTALL)
    if esc_match:
        esc_body = esc_match.group(1)
        required_markers = [
            ("**Stage:**", "Missing '**Stage:**' marker in escalation template"),
            ("**Escalation:", "Missing '**Escalation:**' marker in escalation template"),
            ("**Your options:**", "Missing '**Your options:**' marker in escalation template"),
        ]
        for marker, msg in required_markers:
            if marker not in esc_body:
                issues.append(Issue("moderate", check, msg))


def check_orchestrator_alignment(skill_name, workflow_content, orchestrator_content, issues):
    """Check that orchestrator stop conditions match workflow decisions."""
    check = "orchestrator-alignment"

    if not orchestrator_content:
        issues.append(Issue("minor", check, "Cannot read orchestrator file"))
        return

    # Map skill names to stage names in orchestrator
    stage_map = {
        "product-classifier": "Product Classifier",
        "catalog-detector": "Catalog Detector",
        "scraper-generator": "Scraper Generator",
        "eval-generator": "Eval Generator",
    }

    stage_name = stage_map.get(skill_name)
    if not stage_name:
        return  # Not a pipeline stage

    # Check the stage exists in orchestrator
    if stage_name not in orchestrator_content:
        issues.append(Issue("critical", check, f"Stage '{stage_name}' not found in orchestrator"))
        return

    # Extract stop conditions
    stops = extract_orchestrator_stops(orchestrator_content, stage_name)
    decisions = extract_decisions(workflow_content)

    if not stops and decisions:
        issues.append(Issue("critical", check, f"Orchestrator has no stop conditions for '{stage_name}' but workflow has {len(decisions)} decisions"))


def check_subagent_pattern(skill_name, skill_content, issues):
    """Check sub-agent decomposition pattern when references/ contains an orchestrator."""
    check = "subagent-pattern"

    refs = references_dir(skill_name)
    if not refs.is_dir():
        return

    orchestrator_path = refs / "orchestrator.md"
    if not orchestrator_path.exists():
        return  # Not a decomposed skill

    # Sub-agent files are .md files in references/ that are NOT workflow.md, orchestrator.md, or persist-hooks.md
    excluded = {"workflow.md", "orchestrator.md", "persist-hooks.md", "code-generator.md"}
    subagent_files = sorted(
        f for f in refs.glob("*.md")
        if f.name not in excluded
    )

    if not subagent_files:
        return

    # Every sub-agent file should be referenced in the wrapper
    for subagent_file in subagent_files:
        ref = f"references/{subagent_file.name}"
        if subagent_file.name not in skill_content and ref not in skill_content:
            issues.append(Issue("critical", check,
                f"Sub-agent file '{subagent_file.name}' exists but is not referenced in wrapper"))

    # Sub-agent files: check contents
    tool_names_advisory = ["WebSearch", "WebFetch", "Playwright", "Bash tool", "Read tool", "Edit tool", "Agent tool"]

    for subagent_file in subagent_files:
        sa_content = read_file(subagent_file)
        if not sa_content:
            continue

        # Tool names (advisory/minor)
        for tool in tool_names_advisory:
            if tool in sa_content:
                issues.append(Issue("minor", check,
                    f"Sub-agent '{subagent_file.name}' references tool name '{tool}' — prefer capability-focused language"))

        # Input/Output one-liners
        if "**Input:**" not in sa_content:
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' missing **Input:** field"))
        if "**Output:**" not in sa_content:
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' missing **Output:** field"))

        # Input/Output contract tables
        sa_sections = extract_h2_sections(sa_content)
        if "Input Contract" not in sa_sections:
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' missing '## Input Contract' section"))
        if "Output Contract" not in sa_sections:
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' missing '## Output Contract' section"))

        # Heading should say "Sub-Agent"
        heading_match = re.search(r"^# (.+)$", sa_content, re.MULTILINE)
        if heading_match and "Sub-Agent" not in heading_match.group(1):
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' heading should contain 'Sub-Agent'"))

        # Decision blocks (critical — decisions belong in the orchestrator)
        decisions = extract_decisions(sa_content)
        if decisions:
            issues.append(Issue("critical", check,
                f"Sub-agent '{subagent_file.name}' has Decision blocks ({', '.join(decisions)}) — decisions belong in the orchestrator"))

        # Word count
        word_count = len(sa_content.split())
        if word_count > 2500:
            issues.append(Issue("moderate", check,
                f"Sub-agent '{subagent_file.name}' is {word_count} words (target: ≤2,500)"))


def check_script_test_coverage(skill_name, issues):
    """Check that all Python scripts have corresponding test files."""
    check = "test-coverage"
    scripts_dir = SKILLS_DIR / skill_name / "scripts"
    tests_dir = SKILLS_DIR / skill_name / "tests"

    if not scripts_dir.is_dir():
        return  # No scripts to test

    script_files = [
        f.stem for f in sorted(scripts_dir.glob("*.py"))
        if not f.name.startswith("_")  # Library files tested indirectly
    ]

    if not script_files:
        return

    if not tests_dir.is_dir():
        issues.append(Issue("critical", check,
            f"Scripts directory exists with {len(script_files)} script(s) but no tests/ directory"))
        return

    test_files = {f.stem for f in tests_dir.glob("test_*.py")}

    for script in script_files:
        expected_test = f"test_{script}"
        if expected_test not in test_files:
            issues.append(Issue("critical", check,
                f"Script '{script}.py' has no test file 'tests/{expected_test}.py'"))


def check_word_count(skill_name, workflow_content, issues):
    """Check workflow reference word count and warn about decomposition needs."""
    check = "word-count"

    word_count = len(workflow_content.split())
    refs = references_dir(skill_name)
    has_subagents = refs.is_dir() and (refs / "orchestrator.md").exists()

    if word_count > 3000 and not has_subagents:
        issues.append(Issue("minor", check,
            f"Workflow is {word_count} words (>3,000) with no sub-agent decomposition — consider splitting"))
    elif word_count > 3000:
        # Has sub-agents but orchestrator is still large
        issues.append(Issue("minor", check,
            f"Orchestrator is {word_count} words (>3,000) despite having sub-agents — consider trimming"))
    else:
        # Info-level — print but don't count as issue
        pass  # Word count OK


def check_report_template(workflow_content, issues):
    """Check report template compliance."""
    check = "report-template"

    # Check for H1 heading in template — only inside code blocks
    templates = re.findall(r"```markdown\n(.*?)```", workflow_content, re.DOTALL)
    if not templates:
        templates = re.findall(r"```\n(.*?)```", workflow_content, re.DOTALL)

    for template in templates:
        if "# " in template and "**Slug:**" in template:
            # This looks like a report template
            if not re.search(r"^# .+: \{", template, re.MULTILINE):
                issues.append(Issue("moderate", check, "Report template heading should be '# {Type}: {Company Name}'"))
            if "date" not in template.lower():
                issues.append(Issue("moderate", check, "Report template missing date field"))


# ── Main ─────────────────────────────────────────────────────────────────────


def verify_skill(skill_name):
    """Run all checks for a skill."""
    issues = []

    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    orchestrator_content = read_file(ORCHESTRATOR)

    skill_content = read_file(skill_path)

    if not skill_content:
        issues.append(Issue("critical", "file-exists", f"Skill file not found: {skill_path}"))
        return issues

    # Standalone skills get reduced checks (no workflow reference, no wrapper+workflow conventions)
    if skill_name in STANDALONE_SKILLS:
        check_standalone_skill(skill_name, skill_content, issues)
        check_script_test_coverage(skill_name, issues)
        return issues

    refs = references_dir(skill_name)
    workflow_path = refs / "workflow.md"
    orchestrator_path = refs / "orchestrator.md"

    workflow_content = read_file(workflow_path) or read_file(orchestrator_path)
    if not workflow_content:
        issues.append(Issue("critical", "file-exists", f"Workflow reference not found: checked {workflow_path} and {orchestrator_path}"))
        # Still check skill wrapper
        check_skill_wrapper(skill_name, skill_content, issues)
        return issues

    check_skill_wrapper(skill_name, skill_content, issues)
    check_skill_structure(skill_name, skill_content, issues)
    check_workflow_reference(skill_name, workflow_content, issues)
    check_cross_references(skill_name, skill_content, workflow_content, issues)
    check_orchestrator_alignment(skill_name, workflow_content, orchestrator_content, issues)
    check_report_template(workflow_content, issues)
    check_subagent_pattern(skill_name, skill_content, issues)
    check_word_count(skill_name, workflow_content, issues)
    check_script_test_coverage(skill_name, issues)

    return issues


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <skill-name> | --all")
        sys.exit(1)

    if sys.argv[1] == "--all":
        skill_names = [
            d.name for d in SKILLS_DIR.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()
        ]
    else:
        skill_names = [sys.argv[1]]

    total_issues = 0
    for skill_name in sorted(skill_names):
        issues = verify_skill(skill_name)
        critical = [i for i in issues if i.severity == "critical"]
        moderate = [i for i in issues if i.severity == "moderate"]
        minor = [i for i in issues if i.severity == "minor"]

        status = "PASS" if not critical and not moderate else "FAIL" if critical else "WARN"
        icon = {"PASS": "+", "FAIL": "x", "WARN": "~"}[status]

        print(f"\n[{icon}] {skill_name} — {status} ({len(critical)} critical, {len(moderate)} moderate, {len(minor)} minor)")

        for issue in critical + moderate + minor:
            print(issue)

        total_issues += len(critical) + len(moderate)

    print(f"\n{'='*60}")
    print(f"Total: {len(skill_names)} skills checked, {total_issues} issues found")
    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
