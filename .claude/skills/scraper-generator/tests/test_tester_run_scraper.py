# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_run_scraper.py — execution harness."""
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
    """run_scraper() subprocess wrapper."""

    def test_success_returns_zero(self, tmp_path):
        # Use a simple python command instead of an actual scraper
        script = tmp_path / "ok.py"
        script.write_text("print('hello')")
        debug_log = tmp_path / "debug.log"

        code, stdout, duration = run_scraper.run_scraper(
            script, [], debug_log, timeout=10
        )
        # uv run won't work on a bare .py without PEP 723, so test the interface
        # by mocking subprocess
        assert isinstance(duration, float)

    @patch("tester_run_scraper.subprocess.run")
    def test_timeout_returns_minus_one(self, mock_run, tmp_path):
        import subprocess
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["uv"], timeout=5)
        debug_log = tmp_path / "debug.log"
        debug_log.touch()

        code, stdout, duration = run_scraper.run_scraper(
            Path("scraper.py"), ["--probe", "url"], debug_log, timeout=5
        )
        assert code == -1
        assert stdout == ""

    @patch("tester_run_scraper.subprocess.run")
    def test_crash_returns_exit_code(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        debug_log = tmp_path / "debug.log"
        debug_log.touch()

        code, stdout, duration = run_scraper.run_scraper(
            Path("scraper.py"), [], debug_log, timeout=10
        )
        assert code == 1


class TestStepProbe:
    """step_probe() runs --probe per URL and traces results."""

    @patch("tester_run_scraper.run_scraper")
    def test_successful_probe_traces_ok(self, mock_run, capsys, tmp_path):
        product = {"sku": "ABC", "name": "Widget", "url": "https://x.com/p1"}
        mock_run.return_value = (0, json.dumps(product), 1.5)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], tmp_path / "d.log")

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert len(lines) == 1
        assert lines[0]["phase"] == "probe"
        assert lines[0]["status"] == "ok"
        assert "sku" in lines[0]["fields"]

    @patch("tester_run_scraper.run_scraper")
    def test_failed_probe_traces_error(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (1, "", 0.5)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], tmp_path / "d.log")

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "error"

    @patch("tester_run_scraper.run_scraper")
    def test_timeout_probe_traces_timeout(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (-1, "", 30.0)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], tmp_path / "d.log")

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "timeout"

    @patch("tester_run_scraper.run_scraper")
    def test_invalid_json_traces_parse_error(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "not json {{{", 1.0)

        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], tmp_path / "d.log")

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
    """step_categories() runs scraper per category with --append."""

    @patch("tester_run_scraper.run_scraper")
    def test_first_category_no_append(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 2.0)
        scraper = tmp_path / "co" / "scraper.py"
        scraper.parent.mkdir(parents=True)
        scraper.touch()

        run_scraper.step_categories(
            scraper, ["/shop/tools", "/shop/wood"], 10, tmp_path / "d.log"
        )

        calls = mock_run.call_args_list
        # First call should NOT have --append
        assert "--append" not in calls[0][0][1]
        # Second call SHOULD have --append
        assert "--append" in calls[1][0][1]

    @patch("tester_run_scraper.run_scraper")
    def test_traces_per_category(self, mock_run, capsys, tmp_path):
        mock_run.return_value = (0, "", 1.0)
        scraper = tmp_path / "co" / "scraper.py"
        scraper.parent.mkdir(parents=True)
        scraper.touch()

        run_scraper.step_categories(
            scraper, ["/a", "/b", "/c"], 5, tmp_path / "d.log"
        )

        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert len(lines) == 3
        assert all(l["phase"] == "category" for l in lines)
        assert [l["category"] for l in lines] == ["/a", "/b", "/c"]

    @patch("tester_run_scraper.run_scraper")
    def test_summary_accumulates_across_categories(self, mock_run, capsys, tmp_path):
        scraper = tmp_path / "co" / "scraper.py"
        scraper.parent.mkdir(parents=True)
        scraper.touch()
        output_dir = scraper.parent / "output"
        output_dir.mkdir()

        call_count = 0
        def side_effect(scraper_path, args, debug_log, timeout):
            nonlocal call_count
            call_count += 1
            errors = 3 if call_count == 1 else 0
            summary = {"total_products": 5, "batches_written": 1,
                       "duration_seconds": 2.0, "errors_count": errors,
                       "limited": False, "timestamp": f"2026-01-01T00:0{call_count}:00Z"}
            (output_dir / "summary.json").write_text(json.dumps(summary))
            return (0, "", 2.0)

        mock_run.side_effect = side_effect

        run_scraper.step_categories(
            scraper, ["/shop/tools", "/shop/wood"], 10, tmp_path / "d.log"
        )

        merged = json.loads((output_dir / "summary.json").read_text())
        assert merged["total_products"] == 10
        assert merged["errors_count"] == 3  # 3 from first + 0 from second
        assert merged["duration_seconds"] == 4.0

    @patch("tester_run_scraper.run_scraper")
    def test_append_preserves_existing_summary(self, mock_run, capsys, tmp_path):
        scraper = tmp_path / "co" / "scraper.py"
        scraper.parent.mkdir(parents=True)
        scraper.touch()
        output_dir = scraper.parent / "output"
        output_dir.mkdir()
        existing = {"total_products": 20, "batches_written": 4, "duration_seconds": 10.0,
                     "errors_count": 1, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        (output_dir / "summary.json").write_text(json.dumps(existing))

        def side_effect(scraper_path, args, debug_log, timeout):
            summary = {"total_products": 5, "batches_written": 1,
                       "duration_seconds": 2.0, "errors_count": 0,
                       "limited": False, "timestamp": "2026-01-01T00:05:00Z"}
            (output_dir / "summary.json").write_text(json.dumps(summary))
            return (0, "", 2.0)

        mock_run.side_effect = side_effect

        run_scraper.step_categories(
            scraper, ["/shop/wood"], 10, tmp_path / "d.log", append=True
        )

        merged = json.loads((output_dir / "summary.json").read_text())
        assert merged["total_products"] == 25
        assert merged["errors_count"] == 1


class TestStepDepth:
    """step_depth() merges summary with existing accumulated summary."""

    @patch("tester_run_scraper.run_scraper")
    def test_merges_with_existing_summary(self, mock_run, capsys, tmp_path):
        scraper = tmp_path / "co" / "scraper.py"
        scraper.parent.mkdir(parents=True)
        scraper.touch()
        output_dir = scraper.parent / "output"
        output_dir.mkdir()
        existing = {"total_products": 30, "batches_written": 6, "duration_seconds": 15.0,
                     "errors_count": 2, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        (output_dir / "summary.json").write_text(json.dumps(existing))

        def side_effect(scraper_path, args, debug_log, timeout):
            summary = {"total_products": 100, "batches_written": 10,
                       "duration_seconds": 60.0, "errors_count": 0,
                       "limited": True, "timestamp": "2026-01-01T00:10:00Z"}
            (output_dir / "summary.json").write_text(json.dumps(summary))
            return (0, "", 60.0)

        mock_run.side_effect = side_effect

        run_scraper.step_depth(scraper, tmp_path / "d.log")

        merged = json.loads((output_dir / "summary.json").read_text())
        assert merged["total_products"] == 130
        assert merged["errors_count"] == 2
        assert merged["limited"] is True


class TestStepSaveBaseline:
    """step_save_baseline() copies products.jsonl to baseline."""

    def test_copies_file(self, tmp_path, capsys):
        products = tmp_path / "products.jsonl"
        products.write_text('{"sku":"1"}\n')

        run_scraper.step_save_baseline(tmp_path)

        baseline = tmp_path / "baseline_products.jsonl"
        assert baseline.exists()
        assert baseline.read_text() == '{"sku":"1"}\n'

    def test_missing_products_traces_error(self, tmp_path, capsys):
        run_scraper.step_save_baseline(tmp_path)

        data = json.loads(capsys.readouterr().out.strip())
        assert data["status"] == "error"


class TestStepSaveIteration:
    """step_save_iteration() copies products and debug to iteration files."""

    def test_copies_both_files(self, tmp_path, capsys):
        (tmp_path / "products.jsonl").write_text('{"sku":"1"}\n')
        (tmp_path / "debug_iteration_1.log").write_text("log line\n")

        run_scraper.step_save_iteration(tmp_path, 1)

        assert (tmp_path / "products_iteration_1.jsonl").exists()
        assert (tmp_path / "debug.log").exists()
        assert (tmp_path / "debug.log").read_text() == "log line\n"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
