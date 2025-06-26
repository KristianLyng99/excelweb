# Excel File Host

This project provides a small static website for browsing Excel files. Files are placed in the `excel_files/` directory and listed on the web page with details and a built in search box.

## Adding Excel files

1. Copy your `.xlsx` files into the `excel_files/` folder.
2. Run `python3 scripts/generate_list.py` to refresh `file_list.json`.
   This script records each file's size and last modification time.
3. Open `index.html` in your browser. You can search, view file sizes and see
   when each file was last updated.

The site is completely static, so it can be hosted on any file server or even
opened directly from disk.
