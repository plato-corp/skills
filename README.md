# ThePlato Skills

**The agent workflows we actually use, every day, at [ThePlato](https://tiro.ooo) — packaged so you can install them in one line.**

We build [Tiro](https://tiro.ooo), an AI meeting assistant, and we run our company on AI agents — engineering, operations, consulting, personal knowledge. This repo is the public slice of that practice: not demos, but the exact skills our team and our AX consulting clients run in production.

```
/plugin marketplace add plato-corp/skills
/plugin install tiro@plato-skills
```

Every skill installs under the `tiro:*` namespace.

---

## The LLM Wiki suite

The anchor of this repo is a complete toolchain for running a **personal LLM Wiki** — an agent-maintained, interlinked markdown knowledge base, as described in Andrej Karpathy's *LLM Wiki* pattern (all credit for the idea to him; this is our production implementation of it).

The pattern in one paragraph: instead of RAG re-deriving answers from raw documents on every question, the agent **incrementally builds and maintains a persistent wiki**. Every source you add gets compiled in — summary pages, entity pages, cross-references, flagged contradictions. Knowledge compounds instead of being rediscovered. You curate sources and ask questions; the agent does all the bookkeeping humans abandon wikis over. We run our team memory and personal knowledge bases this way — some of ours have 1,000+ interlinked pages.

The suite covers the full lifecycle:

| Skill | What it does |
|---|---|
| [`/tiro:bootstrap-wiki`](plugins/tiro/skills/bootstrap-wiki/SKILL.md) | Interview → scaffold `raw/` + `wiki/` + schema → seed index/log → first ingest. A working wiki in one session. |
| [`/tiro:ingest`](plugins/tiro/skills/ingest/SKILL.md) | Compile one source into the wiki: summary page, entity/concept updates, bidirectional links, contradiction flags. |
| [`/tiro:query`](plugins/tiro/skills/query/SKILL.md) | Ask the wiki. Cited answers; valuable syntheses get filed back as analysis pages so exploration compounds. |
| [`/tiro:lint`](plugins/tiro/skills/lint/SKILL.md) | Health check: contradictions, stale claims, orphans, broken links, missing pages. Prioritized report + fixes. |
| [`/tiro:socratic`](plugins/tiro/skills/socratic/SKILL.md) | Fact-grounded Socratic learning — 50:50 information and challenge, grounded in your wiki and the web. |
| [`/tiro:sync`](plugins/tiro/skills/sync/SKILL.md) | Pull your [Tiro](https://tiro.ooo) meeting notes into the wiki, idempotently. Your conversations become part of the knowledge base. |
| [`/tiro:schedule-sync`](plugins/tiro/skills/schedule-sync/SKILL.md) | Register a recurring daily sync so the wiki stays current by itself. |

Everything except `sync`/`schedule-sync` works with **zero dependencies** — plain markdown, any directory, any agent. If you use Tiro, your meetings flow in automatically; if you don't, the suite never mentions it.

## Getting started in 10 minutes

1. Install (two lines above).
2. Run `/tiro:bootstrap-wiki` and answer three questions — what the wiki is for, where it lives, what language.
3. Drop one article/paper/note into `raw/` and watch the first ingest touch a dozen pages.
4. Open the folder in [Obsidian](https://obsidian.md) — the agent is the writer, Obsidian is your reading UI. The graph view shows your knowledge taking shape.
5. Ask it something with `/tiro:query`. Learn something hard with `/tiro:socratic`.
6. (Tiro users) `/tiro:sync`, then `/tiro:schedule-sync` — and your wiki grows while you sleep.

## How we use this ourselves

- **Personal knowledge** — founders and engineers each run their own wiki: journals, bookmarks, papers, meeting notes, all compounding in one place.
- **AX consulting** — when we help companies adopt AI agents, an LLM Wiki + Socratic dialogue is how a team learns to *articulate its own domain* — the prerequisite for any agent actually working. This repo exists partly because we kept setting this up by hand for clients.
- **Team memory** — meeting notes from Tiro flow into wikis nightly; decisions stop living in people's heads.

## About ThePlato

We're a small team in Seoul building [Tiro](https://tiro.ooo) — an AI meeting assistant for Korean, Japanese, and English — and running AX (AI transformation) engagements where we set companies up to work the way we do. If this repo is useful to you, [Tiro](https://tiro.ooo) is where our conversations-to-knowledge loop starts, and the `tiro` CLI (`npm i -g @theplato/tiro-cli`) is agent-first by design.

**Contact**: hello@theplato.io

## License

[MIT](LICENSE). The LLM Wiki pattern is Andrej Karpathy's idea; the skills, docs, and implementation here are ours.

---

[![Tiro — Perfectly crafted meeting notes](assets/hero.jpg)](https://tiro.ax)
