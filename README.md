# Excel File Host

This small project provides a simple web page for hosting and linking to Excel files.

## Adding Excel files

1. Place your `.xlsx` files in the `excel_files/` folder.
2. Run `python3 scripts/generate_list.py` to update `file_list.json`.
3. Open `index.html` in your browser. The page lists all Excel files and provides links to download or open them in a new tab.

The `generate_list.py` script scans the `excel_files` directory and creates `file_list.json`, which the web page uses to display the list.
