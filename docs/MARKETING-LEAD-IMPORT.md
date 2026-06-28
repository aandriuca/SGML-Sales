# Marketing → Sales lead import (feed-only)

How marketing-generated leads flow into SGML Sales — **without ever modifying the
SGML Marketing Pipeline.** This is the data half of the integration; the voice half lives
in [`OUTREACH-VOICE.md`](OUTREACH-VOICE.md).

## The boundary (read this first)

`aandriuca/SGML-Marketing-Pipeline` is **read-only** to this project (see the repo root
[`CLAUDE.md`](../CLAUDE.md)). The importer below only ever *reads* a CSV that the marketing
world already produces. It does not write to, run, or change anything in the marketing
pipeline. If the marketing side ever needs a new export to make this work, that's a
decision for the owner — we don't reach into that repo.

## What feeds what

The marketing pipeline's lead output is the **lead log** — a sheet shaped like the
marketing repo's `docs/lead-log-template.csv`:

```
Date, Name / Business, Source, Magnet, Stage, Est $/mo, Notes
```

Owners maintain it (one row per opt-in / booked Margin Leak Review) and export it as CSV.
SGML Sales reads that CSV and creates `Lead` rows.

## How to import

```bash
python -m sgml_sales.services.marketing_import path/to/lead-log-export.csv
```

It prints a summary, e.g. `imported=12 skipped_duplicate=3 skipped_invalid=1`.

Programmatic use (e.g. from a scheduled job or another service):

```python
from sqlmodel import Session
from sgml_sales.database import engine
from sgml_sales.services.marketing_import import import_leads_from_csv

with Session(engine) as session:
    result = import_leads_from_csv(session, "lead-log-export.csv")
```

## Behaviour

- **Tagging.** Every created lead gets `source = "marketing-pipeline"`, so marketing-sourced
  demand is attributable in the funnel.
- **Stage → status.** The log's free-text `Stage` maps onto `LeadStatus`:

  | Marketing `Stage`            | `Lead.status`            |
  | ---------------------------- | ------------------------ |
  | `client`                     | `CONVERTED`              |
  | `lost`                       | `UNQUALIFIED`            |
  | `call-done`, `proposal`      | `QUALIFIED`              |
  | `lead`, `call-booked`, other | `NEW`                    |

- **Idempotent.** Re-importing an updated export won't create duplicates — a row is skipped
  if a `marketing-pipeline` lead with the same name already exists (deduped by name).
- **Skips noise.** Blank-name rows and the template's shipped sample row
  (`Example Co (delete this row)`) are skipped as invalid.

## Known limitation / deliberate follow-up

The marketing log's `Source` column is the **channel** (instagram, linkedin…), which is
distinct from SGML Sales' `Lead.source` (the *system* of origin, always
`marketing-pipeline` here). Per-channel attribution — knowing *which channel* booked the
call — would need a dedicated `channel` column on `Lead`. That's intentionally **not** done
yet (it's an additive schema change); capture it when channel-level reporting is needed.
