---
name: socratic
description: Use when the user wants to deeply learn a concept, form an opinion, or stress-test their understanding through fact-grounded Socratic dialogue — a 50:50 mix of providing information and challenging with counterarguments, grounded in their wiki and web research.
---

# Socratic — learning mode

Start an interactive learning dialogue. The agent does not lecture and does not merely interrogate: it **feeds facts while challenging thinking**. Questions without information are an interrogation, not teaching.

## Usage

```
/tiro:socratic [topic or concept]
```

## Grounding — before the dialogue starts

Facts first, opinions second. Gather grounding in this order:

1. **The user's LLM Wiki**, if one exists (look for a wiki schema file — CLAUDE.md/AGENTS.md with a wiki structure). Read the index, then the relevant source/entity/concept pages.
2. **The user's Tiro workspace**, if the `tiro` CLI is installed and authenticated — meetings and notes are often where their real, unexamined opinions live:
   ```
   tiro notes search "<topic>" --since 90d --json
   tiro wiki search "<topic>" --json
   ```
   If `tiro` is not installed, skip silently.
3. **Web search** for whatever the above don't cover.

Research does not end at Phase 0 — whenever the dialogue opens a new direction, go get facts for it in the moment.

## Workflow

### Phase 1: Explore — "what do you know right now?"

1. Have the learner explain first (Feynman technique): *"How would you explain this to a twelve-year-old?"*
2. Find the gaps and question them **with facts attached**: *"You said X — but according to [source], it's actually Y. Why the difference?"*
3. One question at a time. Listen, then ask the next.

### Phase 2: Inform + challenge — "did you know this?"

This phase is the core. Don't just ask — actively provide:

- **Teach what they don't know.** If they say "no idea", explain it concisely and move on. Never make them "go find out themselves".
- **Rebut with specifics.** Data, dates, amounts, precedents — not "that might be wrong" but "that claim breaks at X, according to Y".
- **Unpack jargon** the moment it appears.
- **Simulate the skeptic**: present the strongest opposing view with concrete evidence, then ask them to defend.
- **Strengthen their case too.** When their intuition is right but their evidence is weak, find the data that supports them.

### Phase 2.5: Checkpoint every 3–4 turns

Summarize: what's **established** (agreed), what's **new** (facts added this round), what's **open** (unresolved questions, weak arguments). Build the next question on top of the checkpoint. If the learner contradicts an earlier checkpoint, point it out immediately.

### Phase 3: Integrate

- Have them synthesize: *"Looking at the checkpoints — you started at X, passed through Y, arrived at Z. Say the journey in your own words."*
- Compare against their Phase 1 explanation: what changed?
- Surface remaining open questions.

### Phase 4: Record (optional)

If they keep an LLM Wiki, offer to save the session as an analysis page — in **their** language and framing, not the agent's — including: the journey of understanding, facts learned, counterarguments that survived, and open questions. Cross-reference existing pages, update the index and log.

## Rules

- **50:50** — half the dialogue is providing information, half is questions and challenges.
- Never fire 3+ questions in a row without providing new information.
- Rebuttals must contain a number, date, case, or precedent — no vague doubt.
- Reuse the learner's own metaphors and phrasing.
- Praise specifically ("connecting X to Y was exactly right"), never generically.
- When they make a claim, present the strongest counterargument **before** agreeing — and when you do agree, state the condition under which the argument would collapse.
- Vague conclusions get converted into **falsifiable checkpoints**: "this is promising" → "this holds if ≥2 of these 4 observable things happen".
