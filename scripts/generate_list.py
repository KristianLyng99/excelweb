import os
import json

FILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'excel_files')
OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'file_list.json')

files = [f for f in os.listdir(FILES_DIR) if f.lower().endswith('.xlsx')]
with open(OUTPUT, 'w') as f:
    json.dump(files, f, indent=2)
print(f"Wrote {OUTPUT} with {len(files)} files.")
