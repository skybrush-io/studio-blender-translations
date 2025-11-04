#!/usr/bin/env python3
"""Sort .po and .pot files recursively.

- Active entries are sorted by full msgid.
- Obsolete entries (#~) are sorted by full msgid and appended at the end.
- Preserves internal line breaks.

"""

import sys
from pathlib import Path
import polib

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input-directory>")
    sys.exit(1)

input_dir = Path(sys.argv[1])
if not input_dir.is_dir():
    print(f"Error: {input_dir} is not a directory")
    sys.exit(1)


def sort_po_file(po_path: Path):
    print(f"Processing: {po_path}", end=" ")
    po = polib.pofile(str(po_path))

    # Separate active and obsolete entries
    active_entries = [e for e in po if not e.obsolete]
    obsolete_entries = [e for e in po if e.obsolete]

    # Sort both lists by exact (lowercase) msgid (preserves line breaks)
    active_entries.sort(key=lambda e: e.msgid.lower())
    obsolete_entries.sort(key=lambda e: e.msgid.lower())

    # Create new POFile object
    new_po = polib.POFile()
    new_po.metadata = po.metadata

    # Append sorted active entries
    for entry in active_entries:
        new_po.append(entry)

    # Append sorted obsolete entries at the end
    for entry in obsolete_entries:
        new_po.append(entry)

    # Save file safely
    new_po.save(str(po_path))
    print(f"✅")


# Recursively process .po and .pot files
for po_file in input_dir.rglob("*.po"):
    sort_po_file(po_file)
for pot_file in input_dir.rglob("*.pot"):
    sort_po_file(pot_file)

print("All files sorted successfully.")
