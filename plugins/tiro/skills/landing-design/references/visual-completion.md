# Visual completion

Read this reference after a master is assembled and before `craft`, `polish`, or `release`. Also read it when a rendered page feels unfinished, hard to scan, or mechanically correct but visually unclear.

Rendered does not mean finished. Automated tests, valid markup, a successful build, zero overflow, and an empty console are mechanical evidence. They do not prove that a visitor can orient, decide, or act.

## Verification scope

Choose scope from the changed contract before running the checks below:

| Change | Required scope |
|---|---|
| New master, structural integration, reading-route or hierarchy change, or `release` | Run the complete viewport attention contract and visual-completion gate on the full affected route. |
| Bounded `polish` or control correction | Reproduce the defect at its exact viewport, test the nearest pressure widths and interaction states, and capture one unaffected canonical viewport for regression. Run the 2-second, 5-second, headings-only, squint, and transition tests only when the correction can change their subject. |
| Changed breakpoint or responsive reassembly | Test the affected canonical widths, the first pressure width, and `-1px / +1px` at the changed breakpoint. Do not run every breakpoint boundary when breakpoint logic is unchanged. |
| `fidelity-port` | Compare against the approved source at matching provenance. Use these checks to find translation drift, never to improve a matching source-owned decision. |

Do not recertify locked, unaffected decisions during a bounded correction. The complete gate remains mandatory before releasing a new or structurally changed page, and any observed Blocker or Major still prevents release within the scope it affects.

## Viewport attention contract

For every screenful in the primary reading route, record:

```text
Dominant: the one thing that must be seen first
Supporting: at most two things needed to understand it
Next cue: the next thing to read or do
De-emphasized: information hidden, collapsed, delayed, or visually quiet here
```

A viewport fails when it has more than one dominant item, more than two supporting items, no next cue, or no deliberate de-emphasis decision. An item cannot be called dominant when equal-size headings, repeated cards, dividers, or competing color fields make another item equally loud.

## Progressive disclosure

The primary answer owns the strongest visual weight. Plan-detail comparisons, calculation assumptions, quote documents, implementation notes, and FAQ cannot precede the answer or look equally important. Place them after the answer and collapse, summarize, or quiet them until the visitor asks for detail.

Do not hide information needed to interpret the answer. A metric must identify its subject and state change at a glance: `회의 후 정리 · 기존 30분 → Tiro 2분`, not an isolated `2분` repaired only by nearby body copy.

Give each decision fact one visible owner. A progress strip, field number, completion counter, result label, helper line, or section heading fails when it repeats a relationship already obvious from the control or answer beneath it. Keep only the fragment that best supports interpretation or action; collapse constraints and secondary detail until they become relevant.

## Visual completion gate

Capture the integrated page at `1440px` and `390px` in the actual browser. Add changed breakpoints and pressure widths when applicable. Record CSS viewport, browser zoom, DPR when relevant, crop or full-page state, and responsive state.

Run these tests in order:

1. **2-second test:** Can a new visitor state what this page is for?
2. **5-second test:** Can they state what to do first and what answer it produces?
3. **Headings-only test:** Does the argument remain continuous without body copy?
4. **Squint test:** Does attention move in one intended direction with one dominant item per viewport?
5. **Transition crops:** When adjacent sections share a screen, do width, silhouette, spacing, and the next cue explain the handoff?
6. **Prototype-smell test:** Are there temporary controls, excessive empty regions, repeated equal-weight cards, redundant progress or field markers, always-visible helper copy, decorative numbers or lines, arbitrary dividers, sticky intermediate states, or a generic closing campaign surface?

## Severity and deterministic corrections

**Blocker**

- The visitor cannot identify the page job, first action, primary answer, or next step.
- Supporting explanation precedes or competes with the primary answer.
- A viewport has multiple dominant items or no next cue.
- A meaning-bearing intermediate or sticky state is unreadable.

**Major**

- Text measures and section axes shift without a narrative reason.
- Unowned whitespace, excessive dividers, or repeated equal-weight cards break the reading route.
- A metric omits its subject, before state, or after state.
- The closing action is visually generic or detached from the accumulated answer.
- Desktop or mobile preserves content but loses hierarchy.

Map each surviving problem to a correction:

| Symptom | Correction |
|---|---|
| Wrong information arrives first | Reorder the argument around the visitor's first action and answer |
| Supporting material competes | Collapse, summarize, delay, or reduce contrast and size |
| Ragged widths or drifting axes | Assign a shared reading measure, stage measure, and explicit transition between them |
| Divider-heavy page | Re-group with composition, density, silhouette, or whitespace before adding a boundary |
| Ambiguous metric | Put task name, before state, and after state in the same visual unit |
| Generic final CTA | Carry the current answer into a continuation or handoff; remove the unearned campaign field |
| Broken sticky or intermediate state | Author a valid static, stacked, or user-controlled state |

## Correction loop and receipt

Any Blocker or Major issue prevents release. Group related findings into one bounded pass, then run `critique → correction → recapture` on the same frames. Repeat until no Blocker or Major remains; do not submit the first rendered implementation as the finished result while known visual defects remain.

Record:

```text
Viewport / provenance:
Attention contract:
2-second / 5-second result:
Headings-only / squint result:
Transition crop result:
Prototype-smell findings:
Blocker / Major corrections:
Recapture result:
Mechanical evidence, kept separate:
Release verdict:
```
