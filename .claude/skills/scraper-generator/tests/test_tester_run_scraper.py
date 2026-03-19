# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_run_scraper.py — execution harness with versioned output paths."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# Add scripts dir to path so we can import
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_run_scraper as run_scraper


class TestTrace:
    """trace() emits structured JSON to stdout."""

    def test_trace_outputs_json_line(self, capsys):
        run_scraper.trace("test_phase", key="value")
        out = capsys.readouterr().out.strip()
        data = json.loads(out)
        assert data["phase"] == "test_phase"
        assert data["key"] == "value"
        assert "timestamp" in data

    def test_trace_extra_fields(self, capsys):
        run_scraper.trace("probe", url="https://x.com", status="ok", exit_code=0)
        data = json.loads(capsys.readouterr().out.strip())
        assert data["url"] == "https://x.com"
        assert data["exit_code"] == 0


class TestRunScraper:
    """run_scraper() subprocess wrapper with stderr capture."""

    @patch("tester_run_scraper.subprocess.run")
    def test_success_returns_zero(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0, stdout="hello", stderr="")
        code, stdout, duration = run_scraper.run_scraper(
            Path("scraper.py"), ["--probe", "url"], None, timeout=10
        )
        assert code == 0
        assert stdout == "hello"
        assert isinstance(duration, float)

    @patch("tester_run_scraper.subprocess.run")
    def test_timeout_returns_minus_one(self, mock_run, tmp_path):
        import subprocess
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["uv"], timeout=5)

        code, stdout, duration = run_scraper.run_scraper(
            Path("scraper.py"), ["--probe", "url"], None, timeout=5
        )
        assert code == -1
        assert stdout == ""

    @patch("tester_run_scraper.subprocess.run")
    def test_crash_returns_exit_code(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="")

        code, stdout, duration = run_scraper.run_scraper(
            Path("scraper.py"), [], None, timeout=10
        )
        assert code == 1

    @patch("tester_run_scraper.subprocess.run")
    def test_stderr_appended_to_log_file(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="crash trace\n")
        log_file = tmp_path / "debug.log"

        run_scraper.run_scraper(Path("scraper.py"), [], log_file, timeout=10)

        assert log_file.exists()
        assert "crash trace" in log_file.read_text()

    @patch("tester_run_scraper.subprocess.run")
    def test_empty_stderr_no_log_file_created(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        log_file = tmp_path / "debug.log"

        run_scraper.run_scraper(Path("scraper.py"), [], log_file, timeout=10)

        assert not log_file.exists()


class TestStepProbe:
    """step_probe() runs --probe per URL and traces results."""

    @patch("tester_run_scraper.run_scraper")
    def test_successful_probe_traces_ok(self, mock_run, capsys):
        product = {"sku": "ABC", "name": "Widget", "url": "https://x.com/p1"}
        mock_run.return_value = (0, json.dumps(product), 1.5)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert len(lines) == 1
        assert lines[0]["phase"] == "probe"
        assert lines[0]["status"] == "ok"
        assert "sku" in lines[0]["fields"]

    @patch("tester_run_scraper.run_scraper")
    def test_failed_probe_traces_error(self, mock_run, capsys):
        mock_run.return_value = (1, "", 0.5)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "error"

    @patch("tester_run_scraper.run_scraper")
    def test_timeout_probe_traces_timeout(self, mock_run, capsys):
        mock_run.return_value = (-1, "", 30.0)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "timeout"

    @patch("tester_run_scraper.run_scraper")
    def test_invalid_json_traces_parse_error(self, mock_run, capsys):
        mock_run.return_value = (0, "not json {{{", 1.0)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "parse_error"


class TestMergeSummaries:
    """_merge_summaries() accumulates summary stats across scraper runs."""

    def test_merge_two_summaries(self):
        a = {"total_products": 10, "batches_written": 2, "duration_seconds": 5.0,
             "errors_count": 1, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        b = {"total_products": 8, "batches_written": 1, "duration_seconds": 3.0,
             "errors_count": 2, "limited": True, "timestamp": "2026-01-01T00:01:00Z"}
        merged = run_scraper._merge_summaries(a, b)
        assert merged["total_products"] == 18
        assert merged["errors_count"] == 3
        assert merged["duration_seconds"] == 8.0
        assert merged["limited"] is True
        assert merged["timestamp"] == "2026-01-01T00:01:00Z"

    def test_merge_with_empty_accumulated(self):
        b = {"total_products": 5, "errors_count": 0, "limited": False, "timestamp": "t"}
        assert run_scraper._merge_summaries({}, b) == b

    def test_merge_with_empty_run(self):
        a = {"total_products": 5, "errors_count": 1, "limited": False, "timestamp": "t"}
        assert run_scraper._merge_summaries(a, {}) == a

    def test_errors_accumulate(self):
        a = {"total_products": 0, "batches_written": 0, "duration_seconds": 0,
             "errors_count": 3, "limited": False, "timestamp": "t1"}
        b = {"total_products": 0, "batches_written": 0, "duration_seconds": 0,
             "errors_count": 5, "limited": False, "timestamp": "t2"}
        assert run_scraper._merge_summaries(a, b)["errors_count"] == 8


class TestStepCategories:
    """step_categories() runs scraper per category with versioned output paths."""

    @patch("tester_run_scraper.run_scraper")
    def test_passes_output_file_and_summary_file(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 2.0)
        output_file = tmp_path / "products_1_a3f2.jsonl"
        summary_file = tmp_path / "summary_1_a3f2.json"

        run_scraper.step_categories(
            Path("scraper.py"), ["/shop/tools"], 10,
            output_file, summary_file, None
        )

        call_args = mock_run.call_args_list[0][0][1]
        assert "--output-file" in call_args
        assert str(output_file) in call_args
        assert "--summary-file" in call_args
        assert str(summary_file) in call_args

    @patch("tester_run_scraper.run_scraper")
    def test_passes_log_file_when_provided(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 2.0)
        log_file = tmp_path / "debug_1_a3f2.log"

        run_scraper.step_categories(
            Path("scraper.py"), ["/shop/tools"], 10,
            tmp_path / "p.jsonl", tmp_path / "s.json", log_file
        )

        call_args = mock_run.call_args_list[0][0][1]
        assert "--log-file" in call_args
        assert str(log_file) in call_args

    @patch("tester_run_scraper.run_scraper")
    def test_first_category_no_append(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 2.0)

        run_scraper.step_categories(
            Path("scraper.py"), ["/shop/tools", "/shop/wood"], 10,
            tmp_path / "p.jsonl", tmp_path / "s.json", None
        )

        calls = mock_run.call_args_list
        assert "--append" not in calls[0][0][1]
        assert "--append" in calls[1][0][1]

    @patch("tester_run_scraper.run_scraper")
    def test_traces_per_category(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 1.0)

        run_scraper.step_categories(
            Path("scraper.py"), ["/a", "/b", "/c"], 5,
            tmp_path / "p.jsonl", tmp_path / "s.json", None
        )

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert len(lines) == 3
        assert all(l["phase"] == "category" for l in lines)
        assert [l["category"] for l in lines] == ["/a", "/b", "/c"]

    @patch("tester_run_scraper.run_scraper")
    def test_summary_accumulates_across_categories(self, mock_run, capsys, tmp_path):
        summary_file = tmp_path / "summary_1_a3f2.json"
        call_count = 0

        def side_effect(scraper_path, args, log_file, timeout):
            nonlocal call_count
            call_count += 1
            errors = 3 if call_count == 1 else 0
            summary = {"total_products": 5, "batches_written": 1,
                       "duration_seconds": 2.0, "errors_count": errors,
                       "limited": False, "timestamp": f"2026-01-01T00:0{call_count}:00Z"}
            summary_file.write_text(json.dumps(summary))
            return (0, "", 2.0)

        mock_run.side_effect = side_effect

        run_scraper.step_categories(
            Path("scraper.py"), ["/shop/tools", "/shop/wood"], 10,
            tmp_path / "products_1_a3f2.jsonl", summary_file, None
        )

        merged = json.loads(summary_file.read_text())
        assert merged["total_products"] == 10
        assert merged["errors_count"] == 3
        assert merged["duration_seconds"] == 4.0

    @patch("tester_run_scraper.run_scraper")
    def test_append_preserves_existing_summary(self, mock_run, capsys, tmp_path):
        summary_file = tmp_path / "summary_1_a3f2.json"
        existing = {"total_products": 20, "batches_written": 4, "duration_seconds": 10.0,
                     "errors_count": 1, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        summary_file.write_text(json.dumps(existing))

        def side_effect(scraper_path, args, log_file, timeout):
            summary = {"total_products": 5, "batches_written": 1,
                       "duration_seconds": 2.0, "errors_count": 0,
                       "limited": False, "timestamp": "2026-01-01T00:05:00Z"}
            summary_file.write_text(json.dumps(summary))
            return (0, "", 2.0)

        mock_run.side_effect = side_effect

        run_scraper.step_categories(
            Path("scraper.py"), ["/shop/wood"], 10,
            tmp_path / "products_1_a3f2.jsonl", summary_file, None,
            append=True
        )

        merged = json.loads(summary_file.read_text())
        assert merged["total_products"] == 25
        assert merged["errors_count"] == 1


class TestStepDepth:
    """step_depth() merges summary with existing accumulated summary."""

    @patch("tester_run_scraper.run_scraper")
    def test_merges_with_existing_summary(self, mock_run, capsys, tmp_path):
        summary_file = tmp_path / "summary_1_a3f2.json"
        existing = {"total_products": 30, "batches_written": 6, "duration_seconds": 15.0,
                     "errors_count": 2, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        summary_file.write_text(json.dumps(existing))

        def side_effect(scraper_path, args, log_file, timeout):
            summary = {"total_products": 100, "batches_written": 10,
                       "duration_seconds": 60.0, "errors_count": 0,
                       "limited": True, "timestamp": "2026-01-01T00:10:00Z"}
            summary_file.write_text(json.dumps(summary))
            return (0, "", 60.0)

        mock_run.side_effect = side_effect
        output_file = tmp_path / "products_1_a3f2.jsonl"

        run_scraper.step_depth(Path("scraper.py"), output_file, summary_file, None)

        merged = json.loads(summary_file.read_text())
        assert merged["total_products"] == 130
        assert merged["errors_count"] == 2
        assert merged["limited"] is True

    @patch("tester_run_scraper.run_scraper")
    def test_passes_versioned_paths_to_scraper(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 5.0)
        output_file = tmp_path / "products_1_a3f2.jsonl"
        summary_file = tmp_path / "summary_1_a3f2.json"
        log_file = tmp_path / "debug_1_a3f2.log"

        run_scraper.step_depth(Path("scraper.py"), output_file, summary_file, log_file)

        call_args = mock_run.call_args_list[0][0][1]
        assert "--output-file" in call_args
        assert "--summary-file" in call_args
        assert "--log-file" in call_args
        assert "--append" in call_args


class TestStepSaveBaseline:
    """step_save_baseline() copies versioned products file to baseline."""

    def test_copies_file(self, tmp_path, capsys):
        products = tmp_path / "products_1_a3f2.jsonl"
        products.write_text('{"sku":"1"}\n')

        run_scraper.step_save_baseline(products)

        baseline = tmp_path / "baseline_products.jsonl"
        assert baseline.exists()
        assert baseline.read_text() == '{"sku":"1"}\n'

    def test_missing_products_traces_error(self, tmp_path, capsys):
        missing = tmp_path / "products_1_a3f2.jsonl"
        run_scraper.step_save_baseline(missing)

        data = json.loads(capsys.readouterr().out.strip())
        assert data["status"] == "error"


class TestSummaryHelpers:
    """_read_summary, _write_summary, _clear_summary work with file paths."""

    def test_read_existing_summary(self, tmp_path):
        sf = tmp_path / "summary_1_a3f2.json"
        sf.write_text(json.dumps({"errors_count": 3}))
        assert run_scraper._read_summary(sf) == {"errors_count": 3}

    def test_read_missing_summary(self, tmp_path):
        sf = tmp_path / "nonexistent.json"
        assert run_scraper._read_summary(sf) == {}

    def test_read_none_summary(self):
        assert run_scraper._read_summary(None) == {}

    def test_write_summary(self, tmp_path):
        sf = tmp_path / "summary_1_a3f2.json"
        run_scraper._write_summary(sf, {"errors_count": 0})
        assert json.loads(sf.read_text()) == {"errors_count": 0}

    def test_clear_summary(self, tmp_path):
        sf = tmp_path / "summary_1_a3f2.json"
        sf.write_text("{}")
        run_scraper._clear_summary(sf)
        assert not sf.exists()

    def test_clear_missing_summary_no_error(self, tmp_path):
        sf = tmp_path / "nonexistent.json"
        run_scraper._clear_summary(sf)  # should not raise


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
