# SKU Schema Key Column Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an explicit `Key` column to all 237 SKU schema files so scrapers match attribute names against explicit snake_case keys, not inferred conversions.

**Architecture:** A Python migration script converts all schema files in-place, adding the Key column between Attribute and Data Type. A verification script then checks every file. Finally, the product-taxonomy skill template and scraper-generator agent are updated to reference the Key column.

**Tech Stack:** Python (standard library only), markdown table parsing via regex.

---

## Chunk 1: Migration Script + Run

### Task 1: Write the migration script

**Files:**
- Create: `scripts/add_schema_key_column.py`

The script does:
1. For each `.md` file in `docs/product-taxonomy/sku-schemas/`
2. Find markdown tables (Core Attributes and Extended Attributes)
3. For each attribute row, compute `key` from the Attribute column
4. Insert the Key column as the second column (after Attribute, before Data Type)
5. Update the header row and separator row accordingly
6. Write the file back

**Conversion rule:**
- Lowercase the display name
- Replace spaces with underscores
- Drop these characters: `/ ( ) , &`
- Collapse consecutive underscores to one
- Strip leading/trailing underscores

**Edge cases (verified against existing scrapers):**
- "GTIN / EAN" → `gtin_ean`
- "Charging Power (kW)" → `charging_power_kw`
- "Rated Current (A)" → `rated_current_a`
- "Dimensions (H x W x D)" → `dimensions_h_x_w_x_d`
- "IP Rating" → `ip_rating`
- "Wood Type" → `wood_type`
- "Country of Origin" → `country_of_origin`

- [ ] **Step 1: Write the migration script**

```python
"""Add explicit Key column to all SKU schema markdown files."""
import re
from pathlib import Path

SCHEMAS_DIR = Path("docs/product-taxonomy/sku-schemas")

def display_name_to_key(name: str) -> str:
    """Convert display name to snake_case key."""
    key = name.lower()
    key = re.sub(r'[/()&,]', '', key)  # drop special chars
    key = key.replace(' ', '_')
    key = re.sub(r'_+', '_', key)  # collapse multiple underscores
    key = key.strip('_')
    return key

def migrate_table(lines: list[str], start: int) -> list[str]:
    """Add Key column to a markdown table starting at line index `start`.
    Returns the modified lines for this table section."""
    # line[start] is the header: | Attribute | Data Type | Description | Example Values |
    # line[start+1] is the separator: |-----------|-----------|-------------|----------------|
    # line[start+2..] are data rows until empty line or non-table line

    header = lines[start]
    separator = lines[start + 1]

    # Check if Key column already exists
    if '| Key |' in header or '| Key |' in header.replace('  ', ' '):
        return lines  # already migrated

    # Insert Key column after Attribute
    # Header: | Attribute | Data Type | ... → | Attribute | Key | Data Type | ...
    header = header.replace('| Attribute | Data Type |', '| Attribute | Key | Data Type |')
    separator = separator.replace('|-----------|-----------|', '|-----------|-----|-----------|')

    result = [header, separator]

    i = start + 2
    while i < len(lines):
        line = lines[i]
        if not line.strip().startswith('|'):
            result.append(line)
            i += 1
            break

        # Parse: | {attribute} | {data_type} | {description} | {examples} |
        parts = line.split('|')
        # parts[0] is empty (before first |), parts[-1] is empty (after last |)
        if len(parts) >= 5:
            attribute = parts[1].strip()
            key = display_name_to_key(attribute)
            # Insert key after attribute
            new_parts = [parts[0], parts[1], f' {key} ', *parts[2:]]
            result.append('|'.join(new_parts))
        else:
            result.append(line)
        i += 1

    # Append remaining lines
    while i < len(lines):
        result.append(lines[i])
        i += 1

    return result

def migrate_file(path: Path) -> bool:
    """Migrate a single schema file. Returns True if modified."""
    text = path.read_text()
    lines = text.split('\n')

    modified = False
    i = 0
    new_lines = []
    while i < len(lines):
        line = lines[i]
        # Detect table header
        if '| Attribute | Data Type | Description | Example Values |' in line:
            if '| Key |' not in line:
                # This table needs migration
                table_lines = migrate_table(lines, i)
                new_lines = lines[:i]  # everything before this table
                new_lines.extend(table_lines)
                # migrate_table consumed rest of file, so rebuild
                text = '\n'.join(new_lines)
                lines = text.split('\n')
                modified = True
                i = 0  # restart scan for second table
                continue
        i += 1

    if modified:
        path.write_text('\n'.join(lines))
    return modified

def main():
    schema_files = sorted(SCHEMAS_DIR.glob('*.md'))
    print(f"Found {len(schema_files)} schema files")

    migrated = 0
    skipped = 0
    errors = []

    for path in schema_files:
        try:
            if migrate_file(path):
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
```

- [ ] **Step 2: Run the migration script**

Run: `uv run python scripts/add_schema_key_column.py`
Expected: "Found 237 schema files", "Migrated: 237, Already done: 0, Errors: 0"

- [ ] **Step 3: Spot-check 5 schema files across different domains**

Manually read these files and verify the Key column is correct:
1. `softwood-hardwood-lumber.md` — verify "Wood Type" → `wood_type`, "Structural Grade" → `structural_grade`
2. `electric-vehicle-charging-equipment.md` — verify "GTIN / EAN" → `gtin_ean`, "Charging Power (kW)" → `charging_power_kw`
3. `hand-tools-hammers-wrenches-screwdrivers.md` — verify "Tool Category" → `tool_category`, "Head Material" → `head_material`
4. `plywood-engineered-wood-panels-osb-particle-board.md` — verify "Panel Type" → `panel_type`, "Surface Grade Front" → `surface_grade_front`
5. `dairy-products.md` — verify keys for a completely different domain

### Task 2: Write the verification script

**Files:**
- Create: `scripts/verify_schema_keys.py`

This script reads ALL 237 schema files and checks:
1. Every table has 5 columns (Attribute, Key, Data Type, Description, Example Values)
2. Every Key value matches the conversion rule applied to its Attribute
3. No duplicate keys within a single table
4. No empty keys
5. Universal attributes (SKU, Product Name, URL, Price, Currency) have correct keys (`sku`, `product_name`, `url`, `price`, `currency`)

- [ ] **Step 4: Write the verification script**

```python
"""Verify all SKU schema files have correct Key columns."""
import re
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

        # Detect table header
        if line.strip().startswith('| Attribute'):
            table_count += 1
            table_name = "Core" if table_count == 1 else "Extended"

            # Check header has Key column
            if '| Key |' not in line:
                issues.append(f"{table_name}: Missing Key column in header")
                i += 1
                continue

            # Check header format
            expected_cols = ['Attribute', 'Key', 'Data Type', 'Description', 'Example Values']
            header_parts = [p.strip() for p in line.split('|') if p.strip()]
            if header_parts != expected_cols:
                issues.append(f"{table_name}: Wrong header columns: {header_parts}")

            # Skip separator
            i += 2

            # Check data rows
            keys_seen = set()
            while i < len(lines) and lines[i].strip().startswith('|'):
                row_parts = [p.strip() for p in lines[i].split('|') if p.strip()]
                if len(row_parts) < 5:
                    issues.append(f"{table_name}: Row has {len(row_parts)} columns, expected 5: {lines[i][:80]}")
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

def main():
    schema_files = sorted(SCHEMAS_DIR.glob('*.md'))
    print(f"Verifying {len(schema_files)} schema files...")

    total_issues = 0
    files_with_issues = 0

    for path in schema_files:
        issues = verify_file(path)
        if issues:
            files_with_issues += 1
            print(f"\n❌ {path.name}:")
            for issue in issues:
                print(f"  - {issue}")
                total_issues += 1

    clean = len(schema_files) - files_with_issues
    print(f"\n{'='*60}")
    print(f"Total: {len(schema_files)} files, {clean} clean, {files_with_issues} with issues, {total_issues} total issues")

    if total_issues == 0:
        print("✅ All schema files pass verification")
    else:
        print(f"❌ {total_issues} issues need fixing")

    return 1 if total_issues > 0 else 0

if __name__ == "__main__":
    exit(main())
```

- [ ] **Step 5: Run the verification script**

Run: `uv run python scripts/verify_schema_keys.py`
Expected: "All schema files pass verification" with 0 issues.

If there are issues, fix them (either in the migration script and re-run, or manually for edge cases), then re-verify until clean.

---

## Chunk 2: Update Agent and Skill Instructions

### Task 3: Update scraper-generator agent

**Files:**
- Modify: `agents/scraper-generator.md` — Step 2a (attribute mapping instructions)

The key change: replace "match it against schema attribute names (exact `snake_case` match)" with "match it against the `Key` column in the schema tables (exact match)".

- [ ] **Step 1: Update Step 2a in the agent**

In `agents/scraper-generator.md`, find Step 2a and update these instructions:

**Old (line ~85):**
```
2. For each attribute the scraper extracts, match it against schema attribute names (exact `snake_case` match).
```

**New:**
```
2. For each attribute the scraper extracts, match it against the Key column in the SKU schema tables (exact match).
```

**Old (line ~89):**
```
6. The scraper code must use the **EXACT attribute names** from the schema — no inventing names, no renaming.
```

**New:**
```
6. The scraper code must use the **EXACT key values** from the schema's Key column — no inventing names, no renaming, no inferring snake_case from display names.
```

Also update the data contract description (around line 184-186):

**Old:**
```
- `core_attributes` — attributes matching **core** names in the SKU schema (exact `snake_case` match)
- `extended_attributes` — attributes matching **extended** names in the SKU schema
```

**New:**
```
- `core_attributes` — attributes whose keys match the **Key** column in the SKU schema's Core Attributes table
- `extended_attributes` — attributes whose keys match the **Key** column in the SKU schema's Extended Attributes table
```

- [ ] **Step 2: Update self-verification gates 6 and 7**

**Old:**
```
| 6 | **`core_attributes` keys match schema** | Every key in `core_attributes` appears in the SKU schema's core attribute list |
| 7 | **`extended_attributes` keys match schema** | Every key in `extended_attributes` appears in the SKU schema's extended attribute list |
```

**New:**
```
| 6 | **`core_attributes` keys match schema** | Every key in `core_attributes` appears in the Key column of the SKU schema's Core Attributes table |
| 7 | **`extended_attributes` keys match schema** | Every key in `extended_attributes` appears in the Key column of the SKU schema's Extended Attributes table |
```

### Task 4: Update product-taxonomy skill

**Files:**
- Modify: `.claude/skills/product-taxonomy/SKILL.md` — canonical template, strict format rules, self-verification

- [ ] **Step 3: Update the canonical file structure template**

In the canonical template (around line 188), change from 4 columns to 5 columns:

**Old:**
```
| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | ... | ... |
```

**New:**
```
| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | ... | ... |
| Product Name | product_name | text | ... | ... |
| URL | url | text | ... | ... |
| Price | price | number | ... | ... |
| Currency | currency | text | ... | ... |
| {core attr} | {snake_case_key} | {type} | ... | ... |
```

Apply the same change to the Extended Attributes template.

- [ ] **Step 4: Update the mandatory attributes table**

The mandatory attributes table (around line 126) should also include Key values:

**New:**
```
| Attribute | Key | Data Type | Why mandatory |
|-----------|-----|-----------|---------------|
| SKU | sku | text | Every product needs a unique identifier |
| Product Name | product_name | text | Every product needs a human-readable name |
| URL | url | text | Link to the product page or listing |
| Price | price | number | Numeric price value, no currency symbol |
| Currency | currency | text | ISO 4217 currency code, always separate from Price |
```

- [ ] **Step 5: Update strict format rules table**

Change the column count rule:

**Old:**
```
| **Table has exactly 4 columns** | `| Attribute | Data Type | Description | Example Values |` | ...
```

**New:**
```
| **Table has exactly 5 columns** | `| Attribute | Key | Data Type | Description | Example Values |` | ...
```

Add a new rule:

```
| **Key column contains valid snake_case** | `wood_type`, `structural_grade`, `charging_power_kw` | camelCase, display names, empty keys |
| **Key derivation rule** | Lowercase, spaces→underscores, drop `/ ( ) , &`, collapse consecutive underscores, strip leading/trailing underscores | Invented keys not matching the display name |
```

- [ ] **Step 6: Update self-verification gates**

Gate 10 currently checks 4 columns. Update to 5:

**Old:**
```
| 10 | **Format compliance** | Table has exactly 4 columns (no `#` row-number column), ...
```

**New:**
```
| 10 | **Format compliance** | Table has exactly 5 columns (Attribute, Key, Data Type, Description, Example Values), no backticks in any table cell, ...
```

Add a new gate:

```
| 11 | **Key column correct** | Every Key value matches the conversion rule applied to its Attribute display name. Universal keys are: sku, product_name, url, price, currency |
```

- [ ] **Step 7: Update the schema evolution rules**

Add Key to the "What you cannot change" section:

```
- **Key** — changing a key breaks downstream scrapers and eval configs that reference it. If the key is wrong, deprecate the attribute and create a new one.
```

### Task 5: Update scraper-generator skill wrapper

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md` — Product record format section

- [ ] **Step 8: Update product record format description**

**Old (line ~68-70):**
```
- **`core_attributes`** — attributes matching core names in the SKU schema
- **`extended_attributes`** — attributes matching extended names in the SKU schema
```

**New:**
```
- **`core_attributes`** — attributes matching the Key column in the SKU schema's Core Attributes table
- **`extended_attributes`** — attributes matching the Key column in the SKU schema's Extended Attributes table
```

---

## Chunk 3: Test the Product Taxonomy Skill

### Task 6: Test the product-taxonomy skill generates Key column

- [ ] **Step 9: Run product-taxonomy in evolution mode on an existing subcategory**

Invoke: `/product-taxonomy Electric Vehicle Charging Equipment`

This is an evolution run (schema already exists). Verify that:
1. The skill preserves the existing Key column values
2. If it adds new attributes, they include correct Key values
3. The output file still passes `scripts/verify_schema_keys.py`

- [ ] **Step 10: Run verification again after the test**

Run: `uv run python scripts/verify_schema_keys.py`
Expected: Still 0 issues — the taxonomy skill preserved Key columns correctly.

---
