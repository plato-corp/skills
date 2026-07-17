---
name: lint
description: Use when health-checking an LLM Wiki — finds contradictions, stale claims, orphan pages, broken links, missing cross-references, and schema violations, then produces a prioritized report and offers fixes.
---

# Lint — wiki health check

Periodic maintenance pass. Wikis rot in predictable ways; this catches them early.

## Usage

```
/tiro:lint
```

## Checks

1. **Contradictions** — pages making conflicting claims about the same entity/concept; mismatched dates or numbers; analyses with opposing conclusions.
2. **Staleness** — claims that newer sources have superseded; pages resting entirely on old sources.
3. **Orphans** — pages with no inbound `[[wikilinks]]` (excluding links from `index.md`).
4. **Broken links** — `[[wikilinks]]` pointing to pages that don't exist. Frequently-referenced missing pages are creation candidates.
5. **Missing cross-references** — pages sharing tags or topics with no links between them.
6. **Missing concept pages** — ideas mentioned across several sources that never got their own page.
7. **Index integrity** — pages missing from `index.md`.
8. **Frontmatter validity** — every page follows the schema; source pages carry `source_path` and the raw file still exists.
9. **Exploration gaps** — questions the wiki raises but can't answer; sources worth hunting for next.

## Report

Save to `wiki/analyses/lint-report-YYYY-MM-DD.md`, sectioned by severity:

- 🔴 **Critical** — contradictions, wrong information (fix now)
- 🟡 **Recommended** — orphans, broken links, gaps
- 🟢 **Suggestions** — new questions, sources to find, structural improvements
- 📊 **Stats** — page counts, source counts, average links per page, top hub pages

For each issue propose a concrete fix; apply fixes the user approves. Append a log entry with counts and a link to the report.
