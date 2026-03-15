# Persist Hook Implementations (NDJSON on Disk)

Current backend: **NDJSON files on disk**.

The agent defines the data contract (product record schema, config metadata schema) and the persist hook call pattern (setup/persist/teardown). This file defines what those hooks do for the current disk backend.

Include these functions in the generated scraper:

```python
BATCH_SIZE = 100
OUTPUT_DIR = Path("output")

def setup() -> Path:
    """Prepare output destination. Clear previous run."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "products.jsonl"
    output_file.write_text("")  # Truncate previous run
    return output_file

def persist(records: list[dict], output_file: Path) -> None:
    """Append a batch of product records as NDJSON."""
    with open(output_file, "a") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

def teardown(output_file: Path, summary: dict) -> None:
    """Write run summary alongside the product data."""
    summary_path = output_file.parent / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
```

**Output format:** NDJSON (one JSON object per line). Append-friendly, crash-safe (completed batches survive mid-run failures), and memory-efficient to read.

To switch to a different backend (PostgreSQL, MongoDB), replace the hook implementations in this file — the agent's scraping logic and data contract remain unchanged.
