"""Add explicit Key column to all SKU schema markdown files."""
import re
from pathlib import Path

SCHEMAS_DIR = Path("docs/product-taxonomy/sku-schemas")


def display_name_to_key(name: str) -> str:
    """Convert display name to snake_case key."""
    key = name.lower()
    key = re.sub(r'[/()&,]', '', key)
    key = key.replace(' ', '_')
    key = re.sub(r'_+', '_', key)
    key = key.strip('_')
    return key


def process_file(path: Path) -> bool:
    """Add Key column to a schema file. Returns True if modified."""
    text = path.read_text()

    # Skip if already migrated
    if '| Attribute | Key |' in text:
        return False

    lines = text.split('\n')
    new_lines = []
    modified = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect attribute table header
        if '| Attribute | Data Type | Description | Example Values |' in line:
            # Replace header
            new_lines.append(line.replace(
                '| Attribute | Data Type | Description | Example Values |',
                '| Attribute | Key | Data Type | Description | Example Values |'
            ))
            i += 1

            # Replace separator
            if i < len(lines):
                new_lines.append(lines[i].replace(
                    '|-----------|-----------|-------------|----------------|',
                    '|-----------|-----|-----------|-------------|----------------|'
                ))
                i += 1

            # Process data rows
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = lines[i]
                # Split on | keeping structure
                parts = row.split('|')
                # parts: ['', ' Attribute ', ' Data Type ', ' Description ', ' Examples ', '']
                if len(parts) >= 6:
                    attr_name = parts[1].strip()
                    key = display_name_to_key(attr_name)
                    # Insert key column after attribute
                    new_parts = [parts[0], parts[1], f' {key} ', *parts[2:]]
                    new_lines.append('|'.join(new_parts))
                else:
                    new_lines.append(row)
                i += 1

            modified = True
            continue

        new_lines.append(line)
        i += 1

    if modified:
        path.write_text('\n'.join(new_lines))
    return modified


def main() -> None:
    schema_files = sorted(SCHEMAS_DIR.glob('*.md'))
    print(f"Found {len(schema_files)} schema files")

    migrated = 0
    skipped = 0
    errors = []

    for path in schema_files:
        try:
            if process_file(path):
                migrated += 1
            else:
                skipped += 1
        except Exception as e:
            errors.append((path.name, str(e)))
            print(f"ERROR: {path.name}: {e}")

    print(f"Migrated: {migrated}, Already done: {skipped}, Errors: {len(errors)}")
    for name, err in errors:
        print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
