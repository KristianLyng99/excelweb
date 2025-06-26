import os
import json
from datetime import datetime

FILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'excel_files')
OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'file_list.json')

entries = []
for name in sorted(os.listdir(FILES_DIR)):
    if not name.lower().endswith('.xlsx'):
        continue
    path = os.path.join(FILES_DIR, name)
    size = os.path.getsize(path)
    mtime = datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
    entries.append({'name': name, 'size': size, 'mtime': mtime})

with open(OUTPUT, 'w') as f:
    json.dump(entries, f, indent=2)
print(f"Wrote {OUTPUT} with {len(entries)} files.")
