---
name: bootstrap-wiki
description: Use when setting up a new personal LLM Wiki — an agent-maintained, interlinked markdown knowledge base. Interviews the user about their domain, scaffolds the raw/wiki/schema structure, writes a tailored schema file (CLAUDE.md / AGENTS.md), and seeds the index, log, and overview.
---

# Bootstrap Wiki — set up a personal LLM Wiki

Set up a **persistent, LLM-maintained wiki**: a structured, interlinked collection of markdown files that compounds as you feed it sources, instead of re-deriving knowledge on every question like RAG does.

This skill is an implementation of the **LLM Wiki pattern described by Andrej Karpathy** — an idea file meant to be handed to your agent and instantiated for your own domain. Credit for the pattern goes to him; this skill encodes how the Tiro team runs it in production, every day, for personal knowledge, research, and team memory.

## Usage

```
/tiro:bootstrap-wiki [optional: target directory or domain description]
```

## The core idea (tell the user this if they ask)

Three layers:

- **`raw/`** — immutable source documents the user curates (articles, papers, meeting notes, journal entries). The agent reads them, never modifies them.
- **`wiki/`** — markdown pages the agent owns entirely: source summaries, entity pages, concept pages, topic syntheses, analyses. Interlinked with `[[wikilinks]]`.
- **The schema** (`CLAUDE.md` / `AGENTS.md`) — the configuration document that turns a generic agent into a disciplined wiki maintainer: structure, conventions, and workflows for ingest / query / lint.

The human curates sources and asks questions. The agent does all the bookkeeping — summarizing, cross-referencing, contradiction-flagging, index maintenance. Wikis die when maintenance costs exceed value; an agent makes maintenance nearly free.

## Workflow

### 1. Interview — keep it short, 3 questions max at a time

Ask the user:

1. **Domain & purpose.** What is this wiki for? (personal knowledge / research topic / reading companion / team memory / competitive analysis / anything else.) The answer shapes the schema's page types and tone.
2. **Location.** Where should it live? Default: a new git repo directory they name. Recommend they open it in Obsidian as the reading UI (the agent is the writer; Obsidian is the browser).
3. **Language.** Which language should wiki pages be written in? Filenames should stay lowercase-english-with-hyphens regardless.

### 2. Scaffold

Create:

```
<wiki-root>/
├── raw/                # user-owned, immutable sources
│   ├── articles/
│   ├── books/
│   ├── papers/
│   ├── media/
│   └── journal/
├── wiki/
│   ├── sources/        # one summary page per raw source
│   ├── entities/       # people, orgs, places
│   ├── concepts/       # ideas, techniques
│   ├── topics/         # synthesis pages
│   ├── analyses/       # saved answers to good questions
│   └── journal/        # optional daily notes
├── index.md            # catalog of every page, by category
├── log.md              # append-only chronological record
├── overview.md         # dashboard: counts, recent activity
└── CLAUDE.md           # the schema (also symlink/copy AGENTS.md if the user uses other agents)
```

`git init` the directory unless it is already inside a repo.

### 3. Write the schema

Write `CLAUDE.md` tailored to the interview answers. It must define:

- **Ownership rules** — `raw/` is user-owned and read-only for the agent; `wiki/` is agent-owned; `index.md`/`log.md`/`overview.md` are agent-maintained.
- **Page formats** — YAML frontmatter per page type. Source pages must carry a `source_path` field pointing back to the raw original.
- **Cross-reference rules** — `[[wikilinks]]` everywhere, bidirectional links, contradictions recorded explicitly on both pages.
- **The three operations** — ingest (see `/tiro:ingest`), query (see `/tiro:query`), lint (see `/tiro:lint`), each as a short workflow section.
- **Log format** — entries like `## [YYYY-MM-DD] ingest | Title` so `grep "^## \[" log.md | tail -5` works.

Keep the schema under ~150 lines. It will co-evolve with the user; say so in a comment at the top.

### 4. Seed

- `index.md` with empty category sections.
- `log.md` with a bootstrap entry.
- `overview.md` with zero counts.

### 5. First ingest

Ask the user for one real source (a URL, a file, a note) and run the ingest workflow on it end-to-end, so they see the full loop working before the session ends. An empty wiki teaches nothing.

### 6. Optional integrations — detect, don't preach

- If the **Tiro CLI** (`tiro`) is installed and authenticated (`tiro auth status`), mention once: their Tiro meeting notes can flow into this wiki automatically via `/tiro:sync`, and `/tiro:schedule-sync` can make it a daily habit. If `tiro` is not installed, do not bring it up.
- If the user mentions Obsidian, suggest the graph view for spotting hubs/orphans and Obsidian Web Clipper for getting articles into `raw/`.

## Quality bar

- The schema must reflect the user's actual domain — a book-reading wiki needs character/theme pages, not "entities/concepts" boilerplate.
- Everything in the user's chosen language except filenames and frontmatter keys.
- End by summarizing: what was created, how to add the next source, and the one-line habit ("drop a file in raw/, say 'ingest it'").
