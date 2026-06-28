# Branding & company background — TO BE FILLED IN

This project was scaffolded **without access** to the `SGML-Marketing-Pipeline`
repository, which holds the canonical branding and company background. This session's
GitHub access was scoped to `aandriuca/SGML-Sales` only.

To complete branding, do one of:

1. **Re-scope and re-run** — add `aandriuca/SGML-Marketing-Pipeline` to the environment's
   allowed repositories (Claude Code on the web settings), start a **new** session, and ask
   to "pull branding from the marketing pipeline repo into SGML Sales."
2. **Paste the details** — provide the items below and they'll be baked in.

## Items to source from SGML-Marketing-Pipeline (placeholders)

| Field                  | Placeholder value                | Used in                          |
| ---------------------- | -------------------------------- | -------------------------------- |
| Company legal name     | `[COMPANY NAME — placeholder]`   | README, LICENSE, .env.example    |
| Company short/brand    | `[BRAND — placeholder]`          | README, API title                |
| Tagline / mission      | `[TAGLINE — placeholder]`        | README, API description          |
| Primary brand color    | `[#HEX — placeholder]`           | (future) frontend / docs theme   |
| Secondary brand color  | `[#HEX — placeholder]`           | (future) frontend / docs theme   |
| Logo asset             | `[path/url — placeholder]`       | (future) frontend / docs         |
| Industry / vertical    | `[INDUSTRY — placeholder]`       | docs/ARCHITECTURE.md             |
| Reporting currency     | `USD` (assumed)                  | config / accounting              |
| Annual sales (context) | ~$10M (per project brief)        | sizing assumptions               |

## Notes / assumptions made in absence of data

- **Currency** assumed `USD`.
- **Scale**: ~$10M annual sales implies thousands of orders/invoices per year, not
  millions — SQLite is fine for dev; Postgres recommended for production.
- Domain modeled as a standard B2B sales pipeline (lead → opportunity → quote → order →
  invoice) with accounts-receivable accounting hooks. Adjust if the company is B2C or
  subscription-based.
