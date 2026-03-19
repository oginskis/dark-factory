# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_run_scraper.py — execution harness with unique hash per invocation."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_run_scraper as run_scraper


class TestMakeHash:
    """_make_hash() generates unique 4-char hex strings."""

    def test_returns_4_hex_chars(self):
        h = run_scraper._make_hash()
        assert len(h) == 4
        assert all(c in "0123456789abcdef" for c in h)

    def test_two_calls_differ(self):
        hashes = {run_scraper._make_hash() for _ in range(100)}
        assert len(hashes) > 90  # statistically all unique


class TestTrace:
    def test_trace_outputs_json_line(self, capsys):
        run_scraper.trace("test_phase", key="value")
        data = json.loads(capsys.readouterr().out.strip())
        assert data["phase"] == "test_phase"
        assert data["key"] == "value"


class TestRunScraper:
    @patch("tester_run_scraper.subprocess.run")
    def test_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="hello", stderr="")
        code, stdout, duration = run_scraper.run_scraper(Path("s.py"), [], None, 10)
        assert code == 0
        assert stdout == "hello"

    @patch("tester_run_scraper.subprocess.run")
    def test_timeout(self, mock_run):
        import subprocess
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["uv"], timeout=5)
        code, stdout, duration = run_scraper.run_scraper(Path("s.py"), [], None, 5)
        assert code == -1

    @patch("tester_run_scraper.subprocess.run")
    def test_stderr_appended_to_log(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="trace\n")
        log = tmp_path / "d.log"
        run_scraper.run_scraper(Path("s.py"), [], log, 10)
        assert "trace" in log.read_text()


class TestStepProbe:
    @patch("tester_run_scraper.run_scraper")
    def test_ok(self, mock_run, capsys):
        mock_run.return_value = (0, json.dumps({"sku": "A"}), 1.0)
        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)
        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "ok"

    @patch("tester_run_scraper.run_scraper")
    def test_error(self, mock_run, capsys):
        mock_run.return_value = (1, "", 0.5)
        run_scraper.step_probe(Path("s.py"), ["https://x.com/p1"], None)
        lines = [json.loads(l) for l in capsys.readouterr().out.strip().splitlines()]
        assert lines[0]["status"] == "error"


class TestMergeSummaries:
    def test_merge(self):
        a = {"total_products": 10, "batches_written": 2, "duration_seconds": 5.0,
             "errors_count": 1, "limited": False, "timestamp": "2026-01-01T00:00:00Z"}
        b = {"total_products": 8, "batches_written": 1, "duration_seconds": 3.0,
             "errors_count": 2, "limited": True, "timestamp": "2026-01-01T00:01:00Z"}
        merged = run_scraper._merge_summaries(a, b)
        assert merged["total_products"] == 18
        assert merged["errors_count"] == 3
        assert merged["limited"] is True

    def test_merge_empty(self):
        b = {"total_products": 5, "errors_count": 0, "limited": False, "timestamp": "t"}
        assert run_scraper._merge_summaries({}, b) == b


class TestStepCategories:
    @patch("tester_run_scraper.run_scraper")
    def test_passes_output_paths_to_scraper(self, mock_run, tmp_path):
        mock_run.return_value = (0, "", 2.0)
        pf = tmp_path / "products_1_aaaa.jsonl"
        sf = tmp_path / "summary_1_aaaa.json"
        lf = tmp_path / "debug_1_aaaa.log"

        run_scraper.step_categories(Path("s.py"), ["/shop/tools"], 10, pf, sf, lf)

        call_args = mock_run.call_args_list[0][0][1]
        assert "--output-file" in call_args
        assert str(pf) in call_args

    @patch("tester_run_scraper.run_scraper")
    def test_first_cat_no_append(self, mock_run, tmp_path):
        mock_run.return_value = (0, "", 2.0)
        pf = tmp_path / "p.jsonl"
        sf = tmp_path / "s.json"
        lf = tmp_path / "d.log"

        run_scraper.step_categories(Path("s.py"), ["/a", "/b"], 10, pf, sf, lf)

        assert "--append" not in mock_run.call_args_list[0][0][1]
        assert "--append" in mock_run.call_args_list[1][0][1]

    @patch("tester_run_scraper.run_scraper")
    def test_summary_accumulates(self, mock_run, capsys, tmp_path):
        sf = tmp_path / "summary_1_aaaa.json"
        call_count = 0

        def side_effect(scraper_path, args, log_file, timeout):
            nonlocal call_count
            call_count += 1
            # Write to the temp summary path (extracted from args)
            for i, a in enumerate(args):
                if a == "--summary-file":
                    Path(args[i + 1]).write_text(json.dumps({
                        "total_products": 5, "batches_written": 1,
                        "duration_seconds": 2.0, "errors_count": 0,
                        "limited": False, "timestamp": f"t{call_count}"
                    }))
                    break
            return (0, "", 2.0)

        mock_run.side_effect = side_effect
        pf = tmp_path / "products_1_aaaa.jsonl"
        lf = tmp_path / "debug_1_aaaa.log"

        run_scraper.step_categories(Path("s.py"), ["/a", "/b"], 10, pf, sf, lf)

        merged = json.loads(sf.read_text())
        assert merged["total_products"] == 10


class TestStepDepth:
    @patch("tester_run_scraper.run_scraper")
    def test_passes_paths(self, mock_run, tmp_path):
        mock_run.return_value = (0, "", 5.0)
        pf = tmp_path / "products_1_bbbb.jsonl"
        sf = tmp_path / "summary_1_bbbb.json"
        lf = tmp_path / "debug_1_bbbb.log"

        run_scraper.step_depth(Path("s.py"), pf, sf, lf)

        call_args = mock_run.call_args_list[0][0][1]
        assert "--output-file" in call_args
        assert str(pf) in call_args
        # No --append — depth creates its own file
        assert "--append" not in call_args


class TestStepSaveBaseline:
    def test_concatenates_products(self, tmp_path, capsys):
        (tmp_path / "products_1_aaaa.jsonl").write_text('{"sku":"1"}\n')
        (tmp_path / "products_1_bbbb.jsonl").write_text('{"sku":"2"}\n')

        run_scraper.step_save_baseline(tmp_path, 1)

        baseline = tmp_path / "baseline_products.jsonl"
        assert baseline.exists()
        lines = baseline.read_text().strip().splitlines()
        assert len(lines) == 2

    def test_no_files_traces_error(self, tmp_path, capsys):
        run_scraper.step_save_baseline(tmp_path, 99)
        data = json.loads(capsys.readouterr().out.strip())
        assert data["status"] == "error"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
