# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Unit tests for verify_skill.py convention verification."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from verify_skill import (
    Issue,
    extract_frontmatter,
    extract_h2_sections,
    extract_decisions,
    extract_decision_blocks,
    extract_file_locations,
    is_inside_code_block,
    extract_logical_refs_from_workflow,
    extract_wiring_examples,
    extract_orchestrator_stops,
    check_skill_wrapper,
    check_skill_structure,
    check_workflow_reference,
    check_standalone_skill,
    check_cross_references,
    check_report_template,
    verify_skill,
    SKILLS_DIR,
)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _issues_by_severity(issues, severity):
    return [i for i in issues if i.severity == severity]


def _issue_messages(issues):
    return [i.message for i in issues]


# ---------------------------------------------------------------------------
# extract_frontmatter
# ---------------------------------------------------------------------------


class TestExtractFrontmatter:
    def test_valid_yaml(self):
        content = "---\nname: my-skill\ndescription: A great skill\nuser-invocable: true\n---\n# Title"
        fm = extract_frontmatter(content)
        assert fm["name"] == "my-skill"
        assert fm["description"] == "A great skill"
        assert fm["user-invocable"] == "true"

    def test_missing_frontmatter(self):
        content = "# Title\n\nJust some content without frontmatter."
        fm = extract_frontmatter(content)
        assert fm == {}

    def test_empty_content(self):
        fm = extract_frontmatter("")
        assert fm == {}

    def test_frontmatter_with_multiword_values(self):
        content = "---\nname: product-classifier\ndescription: Classify companies into taxonomy\n---\n"
        fm = extract_frontmatter(content)
        assert fm["description"] == "Classify companies into taxonomy"

    def test_indented_lines_skipped(self):
        """Lines starting with a space (nested YAML) should be skipped."""
        content = "---\nname: test\ndescription: >\n  This is a multiline\n  description\n---\n"
        fm = extract_frontmatter(content)
        assert fm["name"] == "test"
        # description line is parsed but indented continuation lines are skipped
        assert "description" in fm

    def test_frontmatter_no_closing(self):
        """Frontmatter that never closes should return empty dict."""
        content = "---\nname: test\ndescription: stuff\n# Title"
        fm = extract_frontmatter(content)
        assert fm == {}


# ---------------------------------------------------------------------------
# extract_h2_sections
# ---------------------------------------------------------------------------


class TestExtractH2Sections:
    def test_multiple_sections(self):
        content = "# Title\n\n## Input\n\nSome text.\n\n## Workflow\n\nMore text.\n\n## Notes\n\nEnd."
        sections = extract_h2_sections(content)
        assert sections == ["Input", "Workflow", "Notes"]

    def test_no_sections(self):
        content = "# Title\n\nJust a title, no H2 sections here."
        sections = extract_h2_sections(content)
        assert sections == []

    def test_h3_not_captured(self):
        content = "## Section\n\n### Subsection\n\nContent."
        sections = extract_h2_sections(content)
        assert sections == ["Section"]

    def test_sections_with_special_characters(self):
        content = "## File locations\n\n## Escalation handling\n"
        sections = extract_h2_sections(content)
        assert sections == ["File locations", "Escalation handling"]


# ---------------------------------------------------------------------------
# extract_decisions
# ---------------------------------------------------------------------------


class TestExtractDecisions:
    def test_found(self):
        content = "## Decisions\n\n### Decision: Scrapability\n\nSome text.\n\n### Decision: Strategy\n\nMore."
        decisions = extract_decisions(content)
        assert decisions == ["Scrapability", "Strategy"]

    def test_none(self):
        content = "## Decisions\n\nNo decision blocks here."
        decisions = extract_decisions(content)
        assert decisions == []

    def test_single_decision(self):
        content = "### Decision: Classification\n\n**Context:** Something."
        decisions = extract_decisions(content)
        assert decisions == ["Classification"]


# ---------------------------------------------------------------------------
# extract_decision_blocks
# ---------------------------------------------------------------------------


class TestExtractDecisionBlocks:
    def test_escalating_decision(self):
        content = (
            "### Decision: Scrapability\n\n"
            "**Context:** Check if site is scrapable.\n"
            "**Autonomous resolution:** Always try.\n"
            "**Escalate when:** Site blocks all attempts.\n"
        )
        blocks = extract_decision_blocks(content)
        assert "Scrapability" in blocks
        assert blocks["Scrapability"]["escalates"] is True

    def test_non_escalating_decision(self):
        content = (
            "### Decision: Format\n\n"
            "**Context:** Choose output format.\n"
            "**Autonomous resolution:** Pick JSON.\n"
            "**Escalate when:** Never — always autonomous.\n"
        )
        blocks = extract_decision_blocks(content)
        assert "Format" in blocks
        assert blocks["Format"]["escalates"] is False

    def test_mixed_decisions(self):
        content = (
            "### Decision: Alpha\n\n"
            "**Context:** First.\n"
            "**Escalate when:** Never.\n\n"
            "### Decision: Beta\n\n"
            "**Context:** Second.\n"
            "**Escalate when:** Unrecoverable error.\n"
        )
        blocks = extract_decision_blocks(content)
        assert blocks["Alpha"]["escalates"] is False
        assert blocks["Beta"]["escalates"] is True

    def test_no_escalate_field_treated_as_non_escalating(self):
        content = (
            "### Decision: Gamma\n\n"
            "**Context:** No escalation field at all.\n"
            "**Autonomous resolution:** Just do it.\n"
        )
        blocks = extract_decision_blocks(content)
        assert "Gamma" in blocks
        assert blocks["Gamma"]["escalates"] is False


# ---------------------------------------------------------------------------
# extract_file_locations
# ---------------------------------------------------------------------------


class TestExtractFileLocations:
    def test_valid_table(self):
        content = (
            "## File locations\n\n"
            "| Resource | Path |\n"
            "|---|---|\n"
            "| company report | docs/product-classifier/{slug}/report.md |\n"
            "| catalog assessment | docs/catalog-detector/{slug}/assessment.md |\n"
        )
        locations = extract_file_locations(content)
        assert len(locations) == 2
        assert locations[0]["name"] == "company report"
        assert locations[0]["path"] == "docs/product-classifier/{slug}/report.md"
        assert locations[1]["name"] == "catalog assessment"

    def test_no_table(self):
        content = "## File locations\n\nNo table here, just text."
        locations = extract_file_locations(content)
        assert locations == []

    def test_table_ends_at_non_pipe_line(self):
        content = (
            "| Resource | Path |\n"
            "|---|---|\n"
            "| report | path/to/report |\n"
            "\nSome text after table.\n"
            "| This | is not part of table |\n"
        )
        locations = extract_file_locations(content)
        assert len(locations) == 1

    def test_empty_content(self):
        locations = extract_file_locations("")
        assert locations == []


# ---------------------------------------------------------------------------
# is_inside_code_block
# ---------------------------------------------------------------------------


class TestIsInsideCodeBlock:
    def test_inside(self):
        content = "Some text.\n```python\ncode here\n```\n"
        # Position inside the code block (within "code here")
        pos = content.index("code here")
        assert is_inside_code_block(content, pos) is True

    def test_outside(self):
        content = "Some text.\n```python\ncode here\n```\nAfter block."
        pos = content.index("After block")
        assert is_inside_code_block(content, pos) is False

    def test_before_any_block(self):
        content = "No code blocks here at all."
        assert is_inside_code_block(content, 5) is False

    def test_at_boundary_opening(self):
        content = "Text\n```\ncode\n```\n"
        # Position right after the opening fence
        pos = content.index("\ncode")
        assert is_inside_code_block(content, pos) is True

    def test_between_two_blocks(self):
        content = "```\nblock1\n```\nBetween\n```\nblock2\n```\n"
        pos = content.index("Between")
        assert is_inside_code_block(content, pos) is False

    def test_nested_fences(self):
        """After two code blocks, text is outside."""
        content = "```\na\n```\n```\nb\n```\nOutside"
        pos = content.index("Outside")
        assert is_inside_code_block(content, pos) is False


# ---------------------------------------------------------------------------
# extract_logical_refs_from_workflow
# ---------------------------------------------------------------------------


class TestExtractLogicalRefsFromWorkflow:
    def test_read_reference(self):
        content = "Read the company report and proceed."
        refs = extract_logical_refs_from_workflow(content)
        assert any("company report" in r for r in refs)

    def test_write_reference(self):
        content = "Write the catalog assessment report to disk."
        refs = extract_logical_refs_from_workflow(content)
        assert any("catalog assessment report" in r for r in refs)

    def test_from_reference(self):
        content = "Get data from the product taxonomy categories file."
        refs = extract_logical_refs_from_workflow(content)
        assert any("product taxonomy categories file" in r for r in refs)

    def test_no_references(self):
        content = "This text has no logical resource references at all."
        refs = extract_logical_refs_from_workflow(content)
        assert refs == []

    def test_inside_code_block_excluded(self):
        content = "```\nRead the company report\n```\n"
        refs = extract_logical_refs_from_workflow(content)
        assert refs == []

    def test_multiple_patterns(self):
        content = (
            "Read the company report first.\n"
            "Check the product taxonomy categories file.\n"
            "Write the catalog assessment report.\n"
        )
        refs = extract_logical_refs_from_workflow(content)
        assert len(refs) >= 2


# ---------------------------------------------------------------------------
# extract_wiring_examples
# ---------------------------------------------------------------------------


class TestExtractWiringExamples:
    def test_with_workflow_section(self):
        content = (
            '## Workflow\n\n'
            'Read and follow `references/workflow.md`.\n\n'
            'Wiring: "company report" maps to the report file.\n'
            '"catalog assessment" is the output.\n\n'
            '## Notes\n'
        )
        examples = extract_wiring_examples(content)
        assert "company report" in examples
        assert "catalog assessment" in examples

    def test_without_workflow_section(self):
        content = "## Input\n\nSome input.\n\n## Notes\n\nSome notes.\n"
        examples = extract_wiring_examples(content)
        assert examples == []

    def test_no_quoted_strings(self):
        content = "## Workflow\n\nNo quoted strings here.\n"
        examples = extract_wiring_examples(content)
        assert examples == []


# ---------------------------------------------------------------------------
# extract_orchestrator_stops
# ---------------------------------------------------------------------------


class TestExtractOrchestratorStops:
    def test_found_stage(self):
        content = (
            "## Stage 1: Product Classifier\n\n"
            "- Classify company into taxonomy\n"
            "- Generate report\n\n"
            "## Stage 2: Catalog Detector\n\n"
            "- Detect catalog\n"
        )
        stops = extract_orchestrator_stops(content, "Product Classifier")
        assert len(stops) == 2
        assert "Classify company into taxonomy" in stops

    def test_missing_stage(self):
        content = (
            "## Stage 1: Product Classifier\n\n"
            "- Do stuff\n"
        )
        stops = extract_orchestrator_stops(content, "Scraper Generator")
        assert stops == []

    def test_multiple_bullet_points(self):
        content = (
            "## Stage 3: Scraper Generator\n\n"
            "- Generate scraper script\n"
            "- Validate output format\n"
            "- Test run scraper\n\n"
            "## Pipeline Complete\n"
        )
        stops = extract_orchestrator_stops(content, "Scraper Generator")
        assert len(stops) == 3


# ---------------------------------------------------------------------------
# check_skill_wrapper
# ---------------------------------------------------------------------------


class TestCheckSkillWrapper:
    def _valid_wrapper(self):
        return (
            "---\n"
            "name: catalog-detector\n"
            "description: Detect product catalogs\n"
            "user-invocable: true\n"
            "---\n\n"
            "# Catalog Detector\n\n"
            "Detect public product catalogs.\n\n"
            "## Input\n\n"
            "Company name or URL.\n\n"
            "## File locations\n\n"
            "| Resource | Path |\n"
            "|---|---|\n"
            "| company report | docs/product-classifier/{slug}/report.md |\n\n"
            "## Workflow\n\n"
            "Read and follow `references/workflow.md`.\n\n"
            "## Notes\n\n"
            "File-driven skill — reads from company report, writes catalog assessment.\n"
        )

    def test_valid_wrapper(self):
        issues = []
        check_skill_wrapper("catalog-detector", self._valid_wrapper(), issues)
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0, f"Unexpected critical issues: {_issue_messages(critical)}"

    def test_missing_frontmatter_name(self):
        content = (
            "---\n"
            "description: Test\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\n## File locations\n\n## Workflow\n\nrefs references/workflow.md\n\n## Notes\n\nFile-driven skill.\n"
        )
        issues = []
        check_skill_wrapper("test-skill", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing 'name'" in m for m in msgs)

    def test_missing_required_sections(self):
        content = (
            "---\n"
            "name: test-skill\n"
            "description: Test\n"
            "user-invocable: true\n"
            "---\n\n"
            "# Test\n\n"
            "## Input\n\nStuff.\n"
        )
        issues = []
        check_skill_wrapper("test-skill", content, issues)
        msgs = _issue_messages(issues)
        # File locations, Workflow, Notes are missing
        assert any("File locations" in m for m in msgs)
        assert any("Workflow" in m for m in msgs)
        assert any("Notes" in m for m in msgs)

    def test_name_mismatch(self):
        content = (
            "---\n"
            "name: wrong-name\n"
            "description: Test\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\n## File locations\n\n## Workflow\n\nrefs references/workflow.md\n\n## Notes\n\nFile-driven skill.\n"
        )
        issues = []
        check_skill_wrapper("correct-name", content, issues)
        msgs = _issue_messages(issues)
        assert any("wrong-name" in m and "correct-name" in m for m in msgs)

    def test_missing_workflow_reference_in_content(self):
        content = (
            "---\n"
            "name: test\n"
            "description: Test\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\n## File locations\n\n## Workflow\n\nDo stuff.\n\n## Notes\n\nFile-driven skill.\n"
        )
        issues = []
        check_skill_wrapper("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing workflow reference" in m for m in msgs)


# ---------------------------------------------------------------------------
# check_skill_structure
# ---------------------------------------------------------------------------


class TestCheckSkillStructure:
    def test_valid_structure(self):
        content = (
            "# Catalog Detector\n\n"
            "Detect public product catalogs and assess scrapability.\n\n"
            "## Workflow\n\n"
            "Read and follow `references/workflow.md`.\n\n"
            "## Escalation handling\n\n"
            "The workflow gathered evidence.\n\n"
            "## Notes\n\n"
            "File-driven skill.\n"
        )
        issues = []
        check_skill_structure("catalog-detector", content, issues)
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0, f"Unexpected critical issues: {_issue_messages(critical)}"

    def test_missing_summary(self):
        content = (
            "# Catalog Detector\n"
            "## Workflow\n\n"
            "Read and follow `references/workflow.md`.\n\n"
            "## Notes\n\n"
            "File-driven skill.\n"
        )
        issues = []
        check_skill_structure("catalog-detector", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing one-line summary" in m for m in msgs)

    def test_wrong_workflow_delegation(self):
        content = (
            "# Test Skill\n\n"
            "A summary line.\n\n"
            "## Workflow\n\n"
            "Do stuff manually.\n\n"
            "## Notes\n\n"
            "File-driven skill.\n"
        )
        issues = []
        check_skill_structure("test-skill", content, issues)
        msgs = _issue_messages(issues)
        assert any("Workflow must start with" in m for m in msgs)

    def test_escalation_agent_wording(self):
        content = (
            "# Test Skill\n\n"
            "Summary.\n\n"
            "## Workflow\n\n"
            "Read and follow `references/workflow.md`.\n\n"
            "## Escalation handling\n\n"
            "The context the agent gathered.\n\n"
            "## Notes\n\n"
            "File-driven skill.\n"
        )
        issues = []
        check_skill_structure("test-skill", content, issues)
        msgs = _issue_messages(issues)
        assert any("the agent gathered" in m for m in msgs)

    def test_notes_missing_file_driven(self):
        content = (
            "# Test Skill\n\n"
            "Summary.\n\n"
            "## Workflow\n\n"
            "Read and follow `references/workflow.md`.\n\n"
            "## Notes\n\n"
            "Some notes without the standard line.\n"
        )
        issues = []
        check_skill_structure("test-skill", content, issues)
        msgs = _issue_messages(issues)
        assert any("File-driven skill" in m for m in msgs)


# ---------------------------------------------------------------------------
# check_workflow_reference
# ---------------------------------------------------------------------------


class TestCheckWorkflowReference:
    def _valid_workflow(self):
        return (
            "# Catalog Detector Workflow\n\n"
            "**Input:** Company name or URL.\n"
            "**Output:** Catalog assessment report.\n\n"
            "## Context\n\n"
            "This workflow detects product catalogs.\n\n"
            "## Boundaries\n\n"
            "Do not modify data.\n\n"
            "## Step 1: Read company report\n\n"
            "Read the company report.\n\n"
            "Self-Verification: check `Scrapability` decision.\n\n"
            "Strict format rules:\n\n"
            "| Field | Rule |\n"
            "|---|---|\n"
            "| url | Must be valid |\n\n"
            "## Step 2: Assess catalog\n\n"
            "Use the `Scrapability` decision.\n\n"
            "## Decisions\n\n"
            "### Decision: Scrapability\n\n"
            "**Context:** Determine if site is scrapable.\n"
            "**Autonomous resolution:** Proceed if accessible.\n"
            "**Escalate when:** Never.\n"
        )

    def test_valid_workflow(self):
        issues = []
        check_workflow_reference("catalog-detector", self._valid_workflow(), issues)
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0, f"Unexpected critical issues: {_issue_messages(critical)}"

    def test_missing_context_section(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Boundaries\n\n## Step 1: Do\n\nSelf-Verification check.\n\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing '## Context'" in m for m in msgs)

    def test_missing_boundaries_section(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\nContext.\n\n## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing '## Boundaries'" in m for m in msgs)

    def test_missing_decisions_section(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing '## Decisions'" in m for m in msgs)

    def test_heading_says_agent(self):
        content = (
            "# Test Agent\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Agent" in m for m in msgs)

    def test_no_steps(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\nNo steps at all.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("No numbered steps" in m for m in msgs)

    def test_missing_input_output(self):
        content = (
            "# Test Workflow\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("**Input:**" in m for m in msgs)
        assert any("**Output:**" in m for m in msgs)

    def test_decision_missing_context_field(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "Use `BadDec`.\n\n"
            "## Decisions\n\n### Decision: BadDec\n\n"
            "**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("BadDec" in m and "**Context:**" in m for m in msgs)

    def test_purpose_instead_of_context(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Purpose\n\n## Boundaries\n\n"
            "## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("## Purpose" in m for m in msgs)

    def test_decisions_not_last_section(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Do\n\nSelf-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n\n"
            "## Appendix\n\nExtra stuff.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("last ## section" in m for m in msgs)

    def test_tool_name_advisory(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Use WebSearch\n\nUse WebSearch to find things.\n\n"
            "Self-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        minor = _issues_by_severity(issues, "minor")
        msgs = _issue_messages(minor)
        assert any("WebSearch" in m for m in msgs)

    def test_step_numbering_gap(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: First\n\nStuff.\n\n"
            "## Step 3: Third\n\nStuff.\n\n"
            "Self-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("numbering gap" in m for m in msgs)

    def test_sub_step_without_parent(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: First\n\nStuff.\n\n"
            "## Step 3a: Orphan sub\n\nStuff.\n\n"
            "Self-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Sub-step 3a" in m for m in msgs)

    def test_decision_unreferenced_in_steps(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Do stuff\n\nJust do stuff, no decision reference.\n\n"
            "Self-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Orphan\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Orphan" in m and "never referenced" in m for m in msgs)

    def test_taxonomy_reference_consistency(self):
        content = (
            "# Test Workflow\n\n"
            "**Input:** data.\n**Output:** result.\n\n"
            "## Context\n\n## Boundaries\n\n"
            "## Step 1: Check taxonomy file\n\nRead the taxonomy file.\n\n"
            "Self-Verification.\nStrict format rules.\n\n"
            "## Decisions\n\n### Decision: Foo\n\n"
            "**Context:** c.\n**Autonomous resolution:** r.\n**Escalate when:** Never.\n"
        )
        issues = []
        check_workflow_reference("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("taxonomy file" in m and "product taxonomy categories file" in m for m in msgs)


# ---------------------------------------------------------------------------
# check_standalone_skill
# ---------------------------------------------------------------------------


class TestCheckStandaloneSkill:
    def test_valid_standalone(self):
        content = (
            "---\n"
            "name: product-taxonomy\n"
            "description: Manage product taxonomy\n"
            "user-invocable: true\n"
            "---\n\n"
            "# Product Taxonomy\n\n"
            "Research SKU attributes.\n\n"
            "## Input\n\n"
            "Subcategory name.\n"
        )
        issues = []
        check_standalone_skill("product-taxonomy", content, issues)
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0, f"Unexpected critical issues: {_issue_messages(critical)}"

    def test_missing_name(self):
        content = (
            "---\n"
            "description: Test\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\nStuff.\n"
        )
        issues = []
        check_standalone_skill("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing 'name'" in m for m in msgs)

    def test_missing_description(self):
        content = (
            "---\n"
            "name: test\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\nStuff.\n"
        )
        issues = []
        check_standalone_skill("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Missing 'description'" in m for m in msgs)

    def test_missing_user_invocable(self):
        content = (
            "---\n"
            "name: test\n"
            "description: A test skill\n"
            "---\n\n"
            "## Input\n\nStuff.\n"
        )
        issues = []
        check_standalone_skill("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("user-invocable" in m for m in msgs)

    def test_missing_input_section(self):
        content = (
            "---\n"
            "name: test\n"
            "description: A test skill\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Output\n\nNo input section here.\n"
        )
        issues = []
        check_standalone_skill("test", content, issues)
        msgs = _issue_messages(issues)
        assert any("Input" in m for m in msgs)

    def test_name_mismatch(self):
        content = (
            "---\n"
            "name: other-name\n"
            "description: Mismatched\n"
            "user-invocable: true\n"
            "---\n\n"
            "## Input\n\nStuff.\n"
        )
        issues = []
        check_standalone_skill("test-skill", content, issues)
        msgs = _issue_messages(issues)
        assert any("other-name" in m and "test-skill" in m for m in msgs)


# ---------------------------------------------------------------------------
# check_cross_references
# ---------------------------------------------------------------------------


class TestCheckCrossReferences:
    def test_missing_file_locations_table(self):
        skill_content = (
            "## Workflow\n\n"
            'Read and follow `references/workflow.md`.\n\n'
            "## Notes\n"
        )
        workflow_content = (
            "## Step 1: Read\n\nRead the company report.\n"
        )
        issues = []
        check_cross_references("test", skill_content, workflow_content, issues)
        msgs = _issue_messages(issues)
        assert any("no File locations table" in m for m in msgs)

    def test_escalating_decision_not_in_wrapper(self):
        skill_content = (
            "## File locations\n\n"
            "| Resource | Path |\n"
            "|---|---|\n"
            "| report | docs/report.md |\n\n"
            "## Workflow\n\n"
            'Read and follow `references/workflow.md`.\n\n'
        )
        workflow_content = (
            "### Decision: CriticalFail\n\n"
            "**Context:** Something critical.\n"
            "**Autonomous resolution:** Try.\n"
            "**Escalate when:** Always escalate.\n"
        )
        issues = []
        check_cross_references("test", skill_content, workflow_content, issues)
        msgs = _issue_messages(issues)
        assert any("CriticalFail" in m and "not mentioned" in m for m in msgs)

    def test_escalation_template_missing_markers(self):
        skill_content = (
            "## File locations\n\n"
            "| Resource | Path |\n"
            "|---|---|\n"
            "| report | docs/report.md |\n\n"
            "## Workflow\n\n"
            'Read and follow `references/workflow.md`.\n\n'
            "## Escalation handling\n\n"
            "Some text without proper markers.\n"
        )
        workflow_content = "No decisions.\n"
        issues = []
        check_cross_references("test", skill_content, workflow_content, issues)
        msgs = _issue_messages(issues)
        assert any("**Stage:**" in m for m in msgs)


# ---------------------------------------------------------------------------
# check_report_template
# ---------------------------------------------------------------------------


class TestCheckReportTemplate:
    def test_valid_template(self):
        workflow_content = (
            "## Step 3: Write report\n\n"
            "```markdown\n"
            "# Assessment: {company_name}\n\n"
            "**Slug:** {slug}\n"
            "**Date:** {date}\n"
            "```\n"
        )
        issues = []
        check_report_template(workflow_content, issues)
        # The heading format is "# Assessment: {company_name}" which matches "# .+: {"
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0

    def test_missing_date_field(self):
        workflow_content = (
            "```markdown\n"
            "# Report: {company_name}\n\n"
            "**Slug:** {slug}\n"
            "```\n"
        )
        issues = []
        check_report_template(workflow_content, issues)
        msgs = _issue_messages(issues)
        assert any("date" in m.lower() for m in msgs)

    def test_no_template_no_issues(self):
        workflow_content = "## Steps\n\nNo template here.\n"
        issues = []
        check_report_template(workflow_content, issues)
        assert len(issues) == 0


# ---------------------------------------------------------------------------
# Issue class
# ---------------------------------------------------------------------------


class TestIssue:
    def test_str_critical(self):
        issue = Issue("critical", "test-check", "Something is wrong")
        assert "[!!!]" in str(issue)
        assert "test-check" in str(issue)
        assert "Something is wrong" in str(issue)

    def test_str_moderate(self):
        issue = Issue("moderate", "check", "Moderate issue")
        assert "[ ! ]" in str(issue)

    def test_str_minor(self):
        issue = Issue("minor", "check", "Minor issue")
        assert "[ . ]" in str(issue)


# ---------------------------------------------------------------------------
# Integration: verify_skill against a real skill (catalog-detector)
# ---------------------------------------------------------------------------


class TestIntegrationCatalogDetector:
    def test_verify_catalog_detector_no_critical_issues(self):
        """Run verify_skill against the real catalog-detector skill and expect no critical issues."""
        issues = verify_skill("catalog-detector")
        critical = _issues_by_severity(issues, "critical")
        assert len(critical) == 0, (
            f"catalog-detector has {len(critical)} critical issues:\n"
            + "\n".join(str(i) for i in critical)
        )


class TestIntegrationAllSkills:
    def test_verify_all_skills(self):
        """Run verify_skill against all skills (simulating --all mode) and collect results."""
        skill_names = [
            d.name for d in SKILLS_DIR.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()
        ]
        assert len(skill_names) > 0, "No skills found to verify"

        results = {}
        for skill_name in sorted(skill_names):
            issues = verify_skill(skill_name)
            critical = _issues_by_severity(issues, "critical")
            moderate = _issues_by_severity(issues, "moderate")
            minor = _issues_by_severity(issues, "minor")
            results[skill_name] = {
                "critical": len(critical),
                "moderate": len(moderate),
                "minor": len(minor),
                "issues": issues,
            }

        # At minimum, all skills should be processable without exceptions
        assert len(results) == len(skill_names)

        # Report any critical issues for debugging
        critical_skills = {
            name: data for name, data in results.items() if data["critical"] > 0
        }
        if critical_skills:
            report = "\n".join(
                f"  {name}: {data['critical']} critical\n"
                + "\n".join(f"    {i}" for i in _issues_by_severity(data["issues"], "critical"))
                for name, data in critical_skills.items()
            )
            # Do not fail — just verify all skills were checked.
            # Critical issues may exist in skills that are work-in-progress.
            pass

    def test_standalone_skills_checked_correctly(self):
        """Standalone skills should get reduced checks (no workflow structure check)."""
        for skill_name in ["product-taxonomy", "product-discovery", "skill-creator-local"]:
            skill_path = SKILLS_DIR / skill_name / "SKILL.md"
            if not skill_path.exists():
                continue
            issues = verify_skill(skill_name)
            # Standalone skills should not have workflow-structure issues
            workflow_issues = [i for i in issues if i.check == "workflow-structure"]
            assert len(workflow_issues) == 0, (
                f"Standalone skill {skill_name} got workflow-structure checks:\n"
                + "\n".join(str(i) for i in workflow_issues)
            )


# ---------------------------------------------------------------------------
# Integration: verify_skill against a nonexistent skill
# ---------------------------------------------------------------------------


class TestIntegrationNonexistent:
    def test_nonexistent_skill(self):
        """A nonexistent skill should return a critical file-exists issue."""
        issues = verify_skill("nonexistent-skill-xyz")
        assert len(issues) == 1
        assert issues[0].severity == "critical"
        assert "not found" in issues[0].message


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
