# Core landing contract

Read this module for every landing-design action. It keeps global gates, autonomous behavior, and state continuity available while detailed action rules remain progressively disclosed.

## Gate applicability

The gate table below is a complete inventory, not an instruction to execute every gate on every edit. A gate is applicable when the current action or a named risk can change its protected outcome. Locked upstream gates remain satisfied until inputs or rendered evidence change. For a bounded correction, verify the affected contract and regressions at its boundaries; do not reopen message, reference, carrier, or site-family decisions without contrary evidence.

<!-- legacy:autonomous:start -->
### Autonomous mode

When the user explicitly requests work without intermediate confirmation, record each gate decision and its evidence internally and keep moving. Convert approval stops into internal direction locks, then run `critique → correction → recapture` until the visual-completion gate passes. Pause only for missing verified facts, insufficient permission, or an irreversible decision. Autonomous mode does not broaden the requested scope or authorization.

<!-- legacy:autonomous:end -->

<!-- legacy:gates:start -->
## Blocking gates

Do not compose or implement until every applicable gate has evidence. Missing evidence is not permission to invent a local answer; preserve the current family or stop at the smallest unresolved decision.

Search for the governing source before concluding it does not exist. Inspecting the one file you expected and stopping is not a search: token, type, brand, and diagram rules frequently live in a decision record or report rather than in code. Record each governing document you found and what it governs, so a later reader can tell a rule that was read from a rule that was assumed.

Never harden an unsourced rule. A rule you inferred may guide a draft, but it must not become a test, a lint, a locked token, or any other mechanism that will later be cited as compliance. Doing so converts a guess into a constraint and removes the means of noticing it was wrong. Every enforced rule cites the document or the observed defect it came from.

| Gate | Required evidence |
|---|---|
| Approved source, when porting or integrating | Active `fidelity-port`; canonical path or URL and capture provenance; source-owned and destination-owned boundary; protected-decision ledger; explicit deltas; mechanical translation method; pre-edit source or rendered checks |
| Site family | Current route plus the two closest sibling public pages; shared Hero axis, type scale, container, copy stack, action hierarchy, and responsive rule; named exceptions |
| Design system | Verified repository or path, ref and commit when applicable, governing token and component files, and a mapping for typography, color, spacing, radius, elevation, icon, action, and interaction-state roles; named gaps and approved exceptions |
| Message | Page thesis, claim clauses, proof for each clause, one-second message, and next action |
| Content migration, when redesigning an existing surface | Complete route, tab, section, copy, list, count, date, link, access-state, and interaction inventory; explicit permission for every omission or structural merge |
| Reading route | Visitor's initial question; first thing to read; first action; answer produced by that action; why each next section is needed; information kept supporting, delayed, or collapsed; redundancy map assigning each decision fact one visible owner |
| Reference | Supplied screenshots or one focused search; 2–4 selected references with distinct jobs, visible extractions, Tiro translations, surfaces not to copy, and approval state |
| Carrier | One primary carrier from photo, product state, or graphic; the verified evidence it carries, asset source or production method, fallback, and approval state |
| Section model | For every section: content model, entities, relationships, protected or changed state, semantic invariant, selected diagram grammar when applicable, and label-hidden inference |
| Rendering medium | For every decisive screen: plausible media considered, selected medium, observable communication gain, closest rejected alternative, current-stack fit, dependency boundary, static and reduced-motion fallback, unsupported/loading/failure states, performance and accessibility risks, and approval state |
| Color climate | Dominant field, supporting surfaces, neutral or chromatic bias, area distribution, accent budget, source, intended after-feeling, and prohibited drift |
| Layout | Page home axis, alignment exceptions, repeated pattern families, bounded-composition spatial frames, target widths, component pressure points, action width contracts, and tablet/mobile reassembly |
| Separation | The job of whitespace, surface, line, shadow, and gradient; divider escalation decision; line topology |
| Visual completion | Viewport attention contracts; 1440px and 390px 2-second, 5-second, headings-only, squint, transition-crop, and prototype-smell results; Blocker or Major corrections and matching recaptures |
| Specialist, when used | Active action, observed gap, selected source, locked decisions, allowed scope, side effects, expected output, and Tiro translation |
| Review | Capture provenance, perceptual assessment, mechanical assessment, falsification pass, and selected correction |

Treat these as a hierarchy: `site family → page → repeated pattern → section → element`. A locally defensible section cannot override a higher-level contract without an explicit exception.

<!-- legacy:gates:end -->

## Motion completion gate

For a new landing, read [motion-storyline.md](motion-storyline.md) during `shape`, `integrate`, and `direction`. Co-design the argument, composition, carrier, responsive route, and movement, then approve one experience baseline containing resting, active, exit, and reduced-motion frames.

For every new landing `craft` and `release`, read [interaction-motion.md](interaction-motion.md). The page is not complete when it only renders correctly at rest: every applicable control state needs a defined response, and every meaning-bearing carrier motion needs valid start, active, exit, interruption, responsive, and reduced-motion states.

At implementation time, the approved experience baseline becomes the source of truth. Its resting frame is recorded as the static parity baseline so interaction polish cannot change locked copy, typography, color, max width, spacing, section structure, carrier, or default hierarchy. For `fidelity-port` or bounded polish, capture the existing static and motion baseline before edits. If motion is deliberately absent, record the narrative or four-gate reason; silence is not a motion decision.

## Compact state

Use the existing evaluation or project record when the work spans actions or turns. Keep only `page / job / active action / locked / open / passed / evidence paths / explicit deltas`. Do not create a new project artifact for a one-turn bounded review when internal state is sufficient.

<!-- legacy:state:start -->
## 8. Preserve only current context

Record the latest brief, selected references, master, frozen decisions, screen-specific rendering-medium map, unresolved decisions, and approval or rejection reasons in the existing evaluation or project record. On a new round, load that compact state and only the sources needed for the active decision. Do not replay the full exploration history or treat old generated assets as approved work.
<!-- legacy:state:end -->
