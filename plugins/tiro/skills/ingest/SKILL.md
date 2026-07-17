---
name: ingest
description: Use when integrating a new source (article, paper, note, meeting transcript, book chapter) into an LLM Wiki — reads the source, writes a summary page, updates entity/concept/topic pages, maintains cross-references, and records the work in the index and log.
---

# Ingest — integrate a source into the wiki

Take one source from `raw/` and compile it into the wiki: summary page, entity/concept updates, cross-references, index, log.

## Usage

```
/tiro:ingest [file path, URL, or description]
```

If no argument is given, look for files added to `raw/` in the last 24 hours and let the user pick.

## Workflow

1. **Locate the source.** If it's a URL, fetch it and save a markdown copy into the right `raw/` subfolder first — `raw/` is the source of truth, the wiki never links to content that could disappear.
2. **Read it fully.** PDFs: extract text. Images: view them separately after the text pass.
3. **Discuss briefly.** Show the user a 3–5 line summary and ask what matters most to them about it. Their angle belongs in the wiki; a summary without their context is just compression.
4. **Write the source page** in `wiki/sources/`:
   - Filename: lowercase-english-with-hyphens.
   - Frontmatter must include `source_path` (back-reference to the raw file), plus title, type, date, tags per the wiki's schema.
   - Sections: core summary, key points, connections, notable quotes (short, attributed).
5. **Update the graph.** Read `index.md` to see what exists, then:
   - Update or create entity pages for people/orgs the source discusses.
   - Update or create concept pages for ideas it introduces.
   - Update topic pages it bears on.
   - A single source typically touches 5–15 pages. That's the point — this is where compounding happens.
6. **Cross-reference both ways.** New page links to existing pages; existing pages get back-links. If the source **contradicts** something already in the wiki, record the contradiction explicitly on both pages — do not silently overwrite.
7. **Index, log, overview.** Add new pages to `index.md`, append a log entry (`## [YYYY-MM-DD] ingest | Title` with created/modified page lists), refresh `overview.md` counts.
8. **Report.** List every file touched. Offer to commit if the wiki is a git repo.

## Quality bar

- At least 2 cross-connections per source — actively hunt for them.
- Contradictions and surprises are the most valuable things to record; never smooth them over.
- Follow the wiki's schema file (CLAUDE.md / AGENTS.md) for language and formatting rules; it wins over this skill on any conflict.

## Batch mode

For many sources at once: create source pages in parallel if you use subagents, but **never let two writers touch shared files** (`index.md`, `log.md`, entity/concept/topic pages). Merge those sequentially at the end.
