# SGML Sales

> Sales infrastructure & accounting platform for **[COMPANY NAME — placeholder]**, a company with ~$10M in annual sales.

SGML Sales is a Python backend that powers the end-to-end commercial pipeline — from
inbound **leads**, through **opportunities** and **quotes**, to **orders**, **invoices**,
and the accounting hooks (accounts receivable, revenue recognition) needed to keep the
books in sync with the sales motion.

It is the operational sibling of the **SGML Marketing Pipeline** project: marketing
generates demand, SGML Sales converts and books it.

---

## ⚠️ Branding placeholders

This repository was scaffolded before the branding/company background from the
`SGML-Marketing-Pipeline` repository could be accessed (session repo-scope limitation).
Every spot that needs real company data is marked with `[... — placeholder]` and is
collected in [`docs/BRANDING.md`](docs/BRANDING.md). Fill those in (or re-run with the
marketing repo in scope) to finalize.

---

## Tech stack

| Concern        | Choice                          |
| -------------- | ------------------------------- |
| Language       | Python 3.11+                    |
| Web framework  | FastAPI                         |
| ORM / models   | SQLModel (SQLAlchemy + Pydantic)|
| Migrations     | Alembic-ready (SQLModel metadata)|
| Server         | Uvicorn                         |
| Testing        | pytest + httpx                  |
| Lint / format  | Ruff                            |

## Domain model

```
Lead ──▶ Opportunity ──▶ Quote ──▶ Order ──▶ Invoice
  │            │                       │          │
Customer ◀─────┴───────────────────────┴──────────┘
Product/Service catalog feeds Quotes, Orders, Invoices
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for detail.

## Sales strategy & playbooks

The business strategy driving this software is captured in:

- [`docs/SALES-STRATEGY.md`](docs/SALES-STRATEGY.md) — revenue model, ICP, pipeline
  stages, qualification scorecard, and the path from $1M to $10M recurring.
- [`docs/COLD-LEAD-PLAYBOOK.md`](docs/COLD-LEAD-PLAYBOOK.md) — the cold lead engine
  (source → engage → nurture) for reaching Canadian e-commerce owners.

> These are the working notes from the virtual-VP-of-Sales sessions. Read them first to
> pick up full context in a new session.

## Quick start

```bash
# 1. Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# 2. Install dependencies
pip install -e ".[dev]"

# 3. Copy environment template
cp .env.example .env

# 4. Run the API (creates a local SQLite DB on first run)
uvicorn sgml_sales.main:app --reload

# 5. Open the interactive docs
open http://localhost:8000/docs
```

## Running tests

```bash
pytest
```

## Project layout

```
src/sgml_sales/
├── main.py            # FastAPI app factory & startup
├── config.py          # Settings (env-driven)
├── database.py        # Engine, session, init
├── models/            # SQLModel tables (domain entities)
├── schemas/           # Request/response models
├── api/routes/        # HTTP endpoints
├── services/          # Business logic (pipeline, accounting)
└── core/              # Shared enums & constants
tests/                 # pytest suite
docs/                  # Architecture & branding notes
```

## License

See [LICENSE](LICENSE).
