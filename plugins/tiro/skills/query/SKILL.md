---
name: query
description: Use when answering a question from an LLM Wiki — navigates the index, reads relevant pages, synthesizes a cited answer, and offers to file valuable answers back into the wiki as analysis pages so explorations compound.
---

# Query — ask the wiki

Answer a question using the wiki as the knowledge base, with citations, and file good answers back in.

## Usage

```
/tiro:query [question]
```

## Workflow

1. **Navigate via the index.** Read `index.md` (or search page names/content) to shortlist relevant pages. Don't bulk-read the whole wiki.
2. **Read and synthesize.** Read the shortlisted source/entity/concept/topic pages. If they cite `raw/` originals and the question needs depth, go to the originals.
3. **Answer with citations.** Every substantive claim should name the wiki page (and through it, the source) it came from. If the wiki doesn't know, say so — and offer a web search to fill the gap, clearly marked as non-wiki material.
4. **File it back.** If the answer involved real synthesis — a comparison, a contradiction found, a new connection — offer to save it as a page in `wiki/analyses/` with the original question in the frontmatter. Good answers should not evaporate into chat history; this is how exploration compounds.
5. **Strengthen the graph.** If answering revealed missing links between existing pages, add them.
6. **Log.** If an analysis was saved, append a log entry.

## Also grounded in Tiro (optional)

If the `tiro` CLI is installed and authenticated, the user's Tiro workspace is a second knowledge base you can search alongside the local wiki:

```
tiro notes search "<query>" --since 90d --json
tiro wiki search "<query>" --json
```

Use it when the question touches meetings, decisions, or conversations that haven't been ingested into the local wiki yet. If `tiro` is not installed, skip this silently.
