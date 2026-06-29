# SGML Sales — Architecture

## Purpose

Operational sales + accounting backbone for **[COMPANY NAME — placeholder]** (~$10M annual
sales, `[INDUSTRY — placeholder]`). Tracks the commercial pipeline and keeps revenue/AR in
sync with the sales motion.

## Pipeline

```
        ┌──────┐    qualify    ┌─────────────┐   propose   ┌───────┐
inbound │ Lead │ ────────────▶ │ Opportunity │ ──────────▶ │ Quote │
        └──────┘               └─────────────┘             └───┬───┘
                                                               │ accept
                                                               ▼
                                          book          ┌───────────┐
                                   ◀───────────────────  │   Order   │
                                                         └─────┬─────┘
                                                               │ fulfill / bill
                                                               ▼
                                                        ┌───────────┐    pay
                                                        │  Invoice  │ ───────▶ AR settled
                                                        └───────────┘
```

Every entity links back to a **Customer**. **Products** (goods/services) feed line items on
Quotes, Orders, and Invoices.

## Layers

| Layer       | Directory                  | Responsibility                                  |
| ----------- | -------------------------- | ----------------------------------------------- |
| API         | `src/sgml_sales/api`       | HTTP routing, request/response handling          |
| Schemas     | `src/sgml_sales/schemas`   | Pydantic request/response contracts              |
| Services    | `src/sgml_sales/services`  | Business logic: pipeline transitions, accounting |
| Models      | `src/sgml_sales/models`    | SQLModel tables (persistence)                    |
| Core        | `src/sgml_sales/core`      | Shared enums, constants                          |
| Infra       | `database.py`, `config.py` | Engine, sessions, settings                       |

## Accounting hooks

- **Invoice** carries `status` (draft → sent → paid → void) and amounts. The
  `accounting` service exposes `accounts_receivable()` (sum of unpaid invoices) and
  `recognized_revenue()` (sum of paid invoices) so the books can reconcile against the
  pipeline. Designed to later sync to an external ledger (e.g. SGL accounting system).

## Data store

- Dev: SQLite (zero-config, created on first run).
- Production: Postgres recommended (`DATABASE_URL=postgresql+psycopg://...`). SQLModel
  metadata is Alembic-ready for migrations.

## Extension points (future)

- Auth (sales reps / roles) — `models/user.py` stub-ready.
- Frontend SPA consuming this API.
- Webhook ingestion from **SGML Marketing Pipeline** to auto-create Leads.
