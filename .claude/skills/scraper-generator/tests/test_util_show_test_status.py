# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for util_show_test_status.py — human-readable test report formatting."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from util_show_test_status import format_report, _load_reports_from_dir


class TestFormatReport:
    def test_full_mode_pass(self):
        report = {
            "mode": "full",
            "timestamp": "2026-03-18T15:00:00Z",
            "status": "pass",
            "rule_results": [
                {"id": "S01", "status": "pass", "value": 0.72, "threshold": 0.30},
                {"id": "S02", "status": "pass", "value": 0.45, "threshold": 0.20},
            ],
            "issues": [],
            "passing_categories": ["/shop/timber"],
        }
        output = format_report(report)
        assert "FULL mode" in output
        assert "PASS" in output
        assert "S01, S02" in output

    def test_full_mode_with_failure(self):
        report = {
            "mode": "full",
            "timestamp": "2026-03-18T15:00:00Z",
            "status": "needs_fix",
            "rule_results": [
                {"id": "M04", "status": "fail", "value": 43, "detail": "43 violations found"},
                {"id": "S01", "status": "pass", "value": 0.72, "threshold": 0.30},
            ],
            "issues": [
                {
                    "rule_id": "M04",
                    "detail": "units embedded in values",
                    "affected_attributes": ["nominal_width"],
                    "sample_values": {"nominal_width": ["18mm", "9mm"]},
                }
            ],
            "passing_categories": [],
        }
        output = format_report(report)
        assert "NEEDS_FIX" in output
        assert "FAILED:" in output
        assert "M04" in output
        assert "ISSUES:" in output
        assert "nominal_width" in output

    def test_retest_mode_with_fix_results(self):
        report = {
            "mode": "retest",
            "timestamp": "2026-03-18T15:05:00Z",
            "status": "pass",
            "rule_results": [
                {"id": "S01", "status": "pass", "value": 0.88, "threshold": 0.30},
            ],
            "issues": [],
            "fix_results": {
                "M04": {"status": "pass", "detail": "0 violations after fix"},
            },
            "regression_results": {
                "status": "pass",
                "products_compared": 49,
                "regressions": [],
            },
            "new_issues": [],
            "passing_categories": ["/shop/timber"],
        }
        output = format_report(report)
        assert "RETEST mode" in output
        assert "FIX RESULTS:" in output
        assert "M04: PASS" in output
        assert "REGRESSIONS: PASS" in output

    def test_retest_mode_with_regressions(self):
        report = {
            "mode": "retest",
            "timestamp": "2026-03-18T15:05:00Z",
            "status": "needs_fix",
            "rule_results": [],
            "issues": [],
            "fix_results": {},
            "regression_results": {
                "status": "fail",
                "products_compared": 20,
                "regressions": [
                    {"url": "https://x.com/a", "field": "price", "baseline_value": 10.0, "retest_value": None},
                ],
            },
            "new_issues": [],
            "passing_categories": [],
        }
        output = format_report(report)
        assert "REGRESSIONS: FAIL" in output
        assert "price" in output

    def test_warnings_displayed(self):
        report = {
            "mode": "full",
            "timestamp": "2026-03-18T15:00:00Z",
            "status": "pass",
            "rule_results": [
                {"id": "M03", "status": "warn", "value": 36, "detail": "36 attributes missing"},
            ],
            "issues": [],
            "passing_categories": [],
        }
        output = format_report(report)
        assert "WARNINGS:" in output
        assert "M03" in output

    def test_skipped_rules(self):
        report = {
            "mode": "retest",
            "timestamp": "2026-03-18T15:05:00Z",
            "status": "pass",
            "rule_results": [
                {"id": "S06", "status": "skip", "value": None, "detail": "Skipped in retest mode"},
            ],
            "issues": [],
            "passing_categories": [],
        }
        output = format_report(report)
        assert "SKIPPED: S06" in output

    def test_index_prefix(self):
        report = {
            "mode": "full",
            "timestamp": "2026-03-18T15:00:00Z",
            "status": "pass",
            "rule_results": [],
            "issues": [],
            "passing_categories": [],
        }
        output = format_report(report, index=3)
        assert "[3]" in output

    def test_new_issues_displayed(self):
        report = {
            "mode": "retest",
            "timestamp": "2026-03-18T15:05:00Z",
            "status": "pass",
            "rule_results": [],
            "issues": [],
            "new_issues": [
                {"rule_id": "M03", "detail": "M04 fix broke attribute_units"},
            ],
            "passing_categories": [],
        }
        output = format_report(report)
        assert "NEW ISSUES:" in output
        assert "M03" in output

    def test_passing_categories_count(self):
        report = {
            "mode": "full",
            "timestamp": "2026-03-18T15:00:00Z",
            "status": "pass",
            "rule_results": [],
            "issues": [],
            "passing_categories": ["/shop/a", "/shop/b", "/shop/c", "/shop/d", "/shop/e", "/shop/f"],
        }
        output = format_report(report)
        assert "PASSING CATEGORIES: 6" in output


class TestLoadReportsFromDir:
    """_load_reports_from_dir() scans for versioned report files."""

    def test_finds_versioned_reports(self, tmp_path):
        (tmp_path / "report_1_a3f2.json").write_text(json.dumps({"mode": "test", "status": "pass"}))
        (tmp_path / "report_2_b4d1.json").write_text(json.dumps({"mode": "retest", "status": "needs_fix"}))
        (tmp_path / "other_file.json").write_text("{}")

        reports = _load_reports_from_dir(tmp_path)
        assert len(reports) == 2
        assert reports[0][0] == 1  # iteration 1 first
        assert reports[1][0] == 2
        assert reports[0][1]["mode"] == "test"
        assert reports[1][1]["mode"] == "retest"

    def test_empty_dir_returns_empty(self, tmp_path):
        reports = _load_reports_from_dir(tmp_path)
        assert reports == []

    def test_ignores_malformed_files(self, tmp_path):
        (tmp_path / "report_1_a3f2.json").write_text("not json")
        (tmp_path / "report_2_b4d1.json").write_text(json.dumps({"mode": "test"}))

        reports = _load_reports_from_dir(tmp_path)
        assert len(reports) == 1
        assert reports[0][0] == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
