---
name: sync
description: Use when syncing Tiro meeting notes and transcripts into an LLM Wiki — discovers notes not yet ingested, downloads them into raw/ via the Tiro CLI, and runs the ingest workflow on each, idempotently and without ever modifying existing raw files.
---

# Sync — Tiro notes → wiki

Pull your Tiro meeting notes and transcripts into the wiki so your conversations become part of your compounding knowledge base. Tiro is the source of truth; `raw/` preserves originals; `wiki/sources/` gets one page per note.

## Prerequisites

- [Tiro](https://tiro.ooo) account with notes, and the Tiro CLI:
  ```
  npm install -g @theplato/tiro-cli
  tiro auth login
  ```
- An LLM Wiki (create one with `/tiro:bootstrap-wiki` if needed).

## Usage

```
/tiro:sync [optional: --since 7d | --all-history]
```

## Workflow

1. **Verify access.** `tiro auth status --json`. On auth failure, tell the user to run `tiro auth login` — do not retry automatically.
2. **Discover.** List candidate notes:
   ```
   tiro notes list --since 30d --json
   ```
   (default window 30d; honor the user's `--since` / full-history request). Compare against notes already in the wiki — source pages record the note GUID (first 8 characters in the filename and/or `source_path`), so a note already ingested is skipped. Same GUID is never ingested twice; **idempotent by GUID**, not by title — duplicate titles with different GUIDs are all kept.
3. **Download** each new note into `raw/tiro/`:
   ```
   tiro notes get <guid> --output raw/tiro/<date>-<slug>-<guid8>.md --include transcript
   ```
   One note's failure must not block the rest; collect failures and report them at the end.
4. **Ingest** each downloaded note with the ingest workflow (`/tiro:ingest`): source page with `source_path`, entity/concept/topic updates, cross-references, index/log/overview.
   - For large batches: source pages may be created in parallel, but shared files (`index.md`, `log.md`, `overview.md`, entity/concept/topic pages) are merged **sequentially at the end** — never concurrently.
5. **Report.** Notes found / already-synced / newly downloaded / ingested / failed. Offer to commit.

## Invariants

- Never modify, overwrite, or delete existing files in `raw/`.
- Every source page records `source_path` back to the raw file.
- Re-running the same sync is always safe (idempotence by GUID).

## Make it a habit

Run `/tiro:schedule-sync` once to register a recurring daily sync — the wiki stays current without anyone remembering to do it.
