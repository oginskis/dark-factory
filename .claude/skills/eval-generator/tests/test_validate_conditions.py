# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for validate_conditions.py — conditions.md ↔ eval_run.py consistency."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_conditions import (
    parse_checks_table,
    parse_collection_strategy,
    validate_checks,
    validate_collection,
)


CONDITIONS_PATH = Path(__file__).resolve().parent.parent / "references" / "conditions.md"


class TestParseChecksTable:
    def test_parses_all_13_checks(self):
        text = CONDITIONS_PATH.read_text()
        checks = parse_checks_table(text)
        assert len(checks) == 13

    def test_weights_sum_to_100(self):
        text = CONDITIONS_PATH.read_text()
        checks = parse_checks_table(text)
        assert sum(c["weight"] for c in checks.values()) == 100

    def test_all_thresholds_between_0_and_1(self):
        text = CONDITIONS_PATH.read_text()
        checks = parse_checks_table(text)
        for name, c in checks.items():
            assert 0 <= c["threshold"] <= 1, f"{name} threshold {c['threshold']} out of range"


class TestParseCollectionStrategy:
    def test_parses_strategy(self):
        text = CONDITIONS_PATH.read_text()
        strategy = parse_collection_strategy(text)
        assert strategy["per_sub_percent"] == 20
        assert strategy["per_sub_min"] == 10
        assert strategy["per_sub_max"] == 100


class TestValidateChecks:
    def test_no_errors_when_matched(self):
        from eval_run import CHECKS
        text = CONDITIONS_PATH.read_text()
        doc_checks = parse_checks_table(text)
        errors = validate_checks(doc_checks, CHECKS)
        assert errors == []


class TestValidateCollection:
    def test_no_errors(self):
        text = CONDITIONS_PATH.read_text()
        strategy = parse_collection_strategy(text)
        errors = validate_collection(strategy)
        assert errors == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
