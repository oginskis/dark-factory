"""Verify all SKU schema files have correct Key columns."""
import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path("docs/product-taxonomy/sku-schemas")


def display_name_to_key(name: str) -> str:
    key = name.lower()
    key = re.sub(r'[/()&,]', '', key)
    key = key.replace(' ', '_')
    key = re.sub(r'_+', '_', key)
    key = key.strip('_')
    return key


def verify_file(path: Path) -> list[str]:
    """Return list of issues found."""
    issues = []
    text = path.read_text()
    lines = text.split('\n')

    table_count = 0
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('| Attribute'):
            table_count += 1
            table_name = "Core" if table_count == 1 else "Extended"

            if '| Key |' not in line:
                issues.append(f"{table_name}: Missing Key column in header")
                i += 1
                continue

            expected_header = ['Attribute', 'Key', 'Data Type', 'Description', 'Example Values']
            header_parts = [p.strip() for p in line.split('|') if p.strip()]
            if header_parts != expected_header:
                issues.append(f"{table_name}: Wrong header columns: {header_parts}")

            # Skip separator
            i += 2

            keys_seen: set[str] = set()
            while i < len(lines) and lines[i].strip().startswith('|'):
                row_parts = [p.strip() for p in lines[i].split('|') if p.strip()]
                if len(row_parts) < 5:
                    issues.append(f"{table_name}: Row has {len(row_parts)} cols, expected 5: {lines[i][:80]}")
                    i += 1
                    continue

                attr_name = row_parts[0]
                key = row_parts[1]
                expected_key = display_name_to_key(attr_name)

                if not key:
                    issues.append(f"{table_name}: Empty key for '{attr_name}'")
                elif key != expected_key:
                    issues.append(f"{table_name}: Key mismatch for '{attr_name}': got '{key}', expected '{expected_key}'")

                if key in keys_seen:
                    issues.append(f"{table_name}: Duplicate key '{key}'")
                keys_seen.add(key)

                i += 1
            continue
        i += 1

    if table_count < 2:
        issues.append(f"Found only {table_count} attribute tables (expected 2: Core + Extended)")

    return issues


def main() -> int:
    schema_files = sorted(SCHEMAS_DIR.glob('*.md'))
    print(f"Verifying {len(schema_files)} schema files...")

    total_issues = 0
    files_with_issues = 0

    for path in schema_files:
        file_issues = verify_file(path)
        if file_issues:
            files_with_issues += 1
            print(f"\n  {path.name}:")
            for issue in file_issues:
                print(f"    - {issue}")
                total_issues += 1

    clean = len(schema_files) - files_with_issues
    print(f"\n{'='*60}")
    print(f"Total: {len(schema_files)} files, {clean} clean, {files_with_issues} with issues, {total_issues} total issues")

    if total_issues == 0:
        print("All schema files pass verification")
    else:
        print(f"{total_issues} issues need fixing")

    return 1 if total_issues > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
