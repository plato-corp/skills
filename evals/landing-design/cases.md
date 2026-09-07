# Tiro landing design behavioral cases

Run each case in a fresh context. For the RED control, do not expose the skill. For GREEN, instruct the evaluator to read and follow `plugins/tiro/skills/landing-design/SKILL.md`. Do not provide the expected answer to the acting agent.

Both RED observations below were captured from a real session on 2026-09-07 that ran with the skill loaded at `v0.5.0`. They are skill-loaded failures, not no-skill controls: the routing table did not surface the REQUIRED gate, so the agent answered it from recall.

## Case 1 — Carrier medium for a transformation claim

```text
IMPORTANT: This is real production work. Produce the actual implementation, not a plan.

Renew the hero of our AX landing page. The claim is that context created in a meeting does not disappear: many spoken fragments become one retained decision, which then arrives in the company's own systems (wiki, issue tracker, chat).

The current hero shows this as three stacked panels labelled 01 Capture / 02 Organize / 03 Activate. The project is a static site with no build step and no existing rendering dependencies.

Build the renewed hero.
```

### RED observation captured before authoring

The skill-loaded agent wrote `Rendering medium: semantic DOM + CSS transform. WebGL rejected — three nodes moving is fine in DOM and the fallback is better` into its own receipt **before opening `rendering-medium.md`**, then implemented styled `div`s. The rejection was pre-written rather than derived: no medium scan was run, no non-DOM candidate was considered, and the resulting carrier was the swapped-panel pattern the module names as the weak representation for a transformation content model.

Root cause in the routing table: the `direction` row did not list `rendering-medium.md`, the `carrier` row framed it as *only when the predicate is true*, and the actual REQUIRED marker lived inside `carrier-and-system.md` prose — one level below the decision it governs.

Pass requires: the medium scan is run per decisive screen with at least one non-DOM candidate; the selection contract records the observable gain and the closest rejected alternative; copy, controls and every fact stay in DOM; carrier geometry is reserved before load; static, reduced-motion and failure states exist. Selecting DOM/CSS is a valid outcome **only** when it follows the scan.

## Case 2 — A governing rule that is not in the code

```text
IMPORTANT: This is real production work.

Our landing page is Korean. Set the hero headline and section titles. The repository contains the design-system token files. Ship the CSS and a test that protects the typography decision.
```

### RED observation captured before authoring

The agent found colour tokens in `tds-foundations.css`, stopped searching, and never ran a filesystem sweep — so `02_타이포그래피/2026-08-22_Tiro_타이포그래피_의사결정_보고서.md`, which contains the governing role table, was never opened. It then invented `the brand serif appears in exactly one place on the page`, set the Korean hero in the UI sans, applied the serif to two Latin glyphs inside that same sentence, and **encoded the invented rule as a passing test**.

Every part of that contradicted the real document: Brand Display KR is the serif and the Korean hero is its primary allowed role; the UI sans is explicitly forbidden as the sole face of a brand-bearing hero; mixing faces inside one sentence is disallowed; and the real limit is one representative serif headline *per screen*, not per page. Hardening the guess as a test removed the means of noticing any of it.

Pass requires: a filesystem search for governing documents before the decision, not only an inspection of the expected file; conflicting sources surfaced with a chosen winner and reason rather than averaged; and no enforced rule without a cited source.
