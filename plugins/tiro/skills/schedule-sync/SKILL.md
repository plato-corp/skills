---
name: schedule-sync
description: Use when the user wants Tiro notes to flow into their LLM Wiki automatically on a schedule — registers a recurring job (agent scheduled task or cron) that runs the sync workflow daily or at a chosen cadence.
---

# Schedule Sync — recurring Tiro → wiki sync

Register a recurring job so `/tiro:sync` runs without anyone remembering to run it. A wiki that stays current by itself is the difference between a knowledge base and a graveyard.

## Usage

```
/tiro:schedule-sync [optional: cadence, e.g. "daily 7am", "weekdays 9am"]
```

## Workflow

1. **Confirm prerequisites.** The Tiro CLI must be installed and authenticated (`tiro auth status`), and the wiki root must be known. If either is missing, fix that first (`/tiro:sync` prerequisites).
2. **Pick the cadence.** Default: daily at 07:00 local time. Honor whatever the user asks.
3. **Register the job**, preferring the most native mechanism available:
   - **Agent scheduler** — if your harness supports scheduled/recurring tasks (e.g. Claude Code scheduled tasks / cron-style jobs), register the sync prompt there: run the `/tiro:sync` workflow against `<wiki-root>`, non-interactively, ingesting everything new since the last run.
   - **System cron fallback** — otherwise, offer a crontab entry that invokes the agent CLI headlessly with the same prompt. Show the exact line before installing it; never edit crontab without showing the user first.
4. **Dry-run once.** Execute one sync immediately so the user sees it work before trusting the schedule.
5. **Report.** What was registered, when it runs, how to list/remove it.

## Notes

- Scheduled runs must be non-interactive: skip discussion steps, ingest everything new, log to `log.md` as usual so the user can audit what happened while they were away.
- If a scheduled run hits an auth failure, it should stop and leave a clear note in `log.md` rather than retrying in a loop.
