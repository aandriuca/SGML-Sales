# 📥 Prospect import inbox — drop your list here

This is the one place to put a prospect export (Store Leads, Apollo, Clay, or a
plain spreadsheet saved as **CSV**) so SGML Sales can load it as leads.

## Do this

1. **Export your list as a CSV** from Store Leads (or Apollo/Clay/Google Sheets →
   File → Download → CSV).
2. **Put the file in this folder** (`data/prospect-imports/`). Name it anything —
   e.g. `canada-shopify-batch1.csv`.
3. **Run the import** from the project root:

   ```bash
   python -m sgml_sales.services.prospect_import data/prospect-imports/canada-shopify-batch1.csv
   ```

   Add `--strict` to keep only Canada + $1M–$10M rows:

   ```bash
   python -m sgml_sales.services.prospect_import data/prospect-imports/canada-shopify-batch1.csv --strict
   ```

4. You'll see a summary like `imported=120 duplicate=4 invalid=1 filtered_icp=15`.
   Those rows are now leads in the pipeline (tagged `source = "store-leads"`).

## Even simpler

If you're in a session with me (Claude), just **drop the CSV here and tell me the
filename** — I'll run the import and show you the results. You don't have to touch
the command line.

## Notes

- The columns don't need to match anything exactly — the importer recognizes common
  names (`Store Name` / `Domain` / `Estimated Sales` / `Owner Email`, etc.).
- **CSVs you drop here are NOT committed to git** (they may hold contact data) — only
  this README is tracked. The files stay on your machine.
- The fields kept per lead: business name, domain (`website`), email, revenue
  estimate, platform, category.
