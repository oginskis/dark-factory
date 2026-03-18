# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for util_show_test_status.py — human-readable test report formatting."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from util_show_test_status import format_report


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


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
