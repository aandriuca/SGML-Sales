# SGML Sales — working notes for Claude

SGML Sales is the operational sibling of the **SGML Marketing Pipeline**: marketing
generates demand, SGML Sales converts and books it. This is a Python / FastAPI / SQLModel
backend for the **Lead → Opportunity → Order → Invoice** pipeline.

## ⛔ Hard boundary: the marketing pipeline is READ-ONLY

The `aandriuca/SGML-Marketing-Pipeline` repository is **production** — it generates SGML's
social posts, AEO content, and web materials. From this project it is **read-only /
feed-only**:

- **DO** read from it (its brand voice, its lead-log CSV export) and build code *here* in
  SGML Sales that consumes that output.
- **DO NOT** edit, commit to, or push to `SGML-Marketing-Pipeline`. Never modify it as a
  side effect of work on SGML Sales.
- If a task seems to *require* changing the marketing pipeline (e.g. it doesn't yet emit
  the data we need), **stop and ask the owner** rather than touching that repo.

Concrete examples of the boundary in action:

- `docs/OUTREACH-VOICE.md` is aligned *to* the marketing brand (`pipeline/brand.py`) but
  lives here; `brand.py` is the source of truth and is never edited from this side.
- `src/sgml_sales/services/marketing_import.py` *reads* a CSV exported from the marketing
  lead log and creates leads here. It never writes back. See
  [`docs/MARKETING-LEAD-IMPORT.md`](docs/MARKETING-LEAD-IMPORT.md).

## Conventions

- Source under `src/sgml_sales/`; tests under `tests/` (pytest, in-memory SQLite fixtures).
- Lint/format with **ruff**; run `python -m pytest -q` and `ruff check .` before committing.
- Tables are SQLModel `table=True` models; request bodies are the non-table `*Create`
  schemas in `schemas/inputs.py` (a table model can't double as a FastAPI body).
- No migrations yet — `init_db()` calls `create_all`. Adding a column to an existing model
  won't ALTER an existing SQLite file, so prefer additive, nullable fields and note it.

## Branding placeholders

The repo was scaffolded before the marketing repo was in scope; real company data is still
stubbed as `[... — placeholder]` and tracked in [`docs/BRANDING.md`](docs/BRANDING.md).
