# Prototype and reports

Use only when alternatives are materially different or the user requests an HTML comparison/report.

## Material-alternative gate

Create variants when two or more of these could legitimately change:

- information architecture or grouping;
- primary interaction model;
- density and disclosure strategy;
- placement/ownership of a primary action;
- guidance level for materially different user sophistication.

Do not create variants for color, radius, card treatment, minor spacing, or decorative novelty. If one direction is already confirmed, finish it instead.

## Comparison contract

Create **2–3** candidates. Each must:

- use the same realistic fixture data, copy, permissions, and edge cases;
- name the decision axes it changes and the tradeoff it accepts;
- be recognizable without relying on labels such as “A/B/C”;
- cover relevant responsive layouts and states;
- pass its own all-critical-items-at-least-9 quality gate;
- live in an isolated HTML report/prototype and never overwrite production UI.

When evidence is incomplete, preserve uncertainty in the fixture rather than inventing product concepts. A candidate can test an assumption only if the report labels it as an assumption and defines how to validate it.

## Shared HTML shell

Copy `../assets/report-shell.html` into the isolated output location and adapt it. Populate its semantic CSS variables from the verified current design-system sources; do not preserve its fallback values as product truth.

Keep report chrome quieter than the candidate UI:

- one compact header and one primary reading column;
- one consistent alignment axis;
- actions grouped once, not repeated on every card;
- navigation only for genuinely long reports;
- no nested card stacks, competing sticky regions, decorative controls, or button clutter;
- each candidate has the same viewport and data controls.

## Three report modes

### Decision Brief

Use while the cause or intervention type is uncertain. Include verdict, grounding, facts/assumptions/open decisions, primary outcome, smallest intervention, risks, and validation.

### Comparison Lab

Use for material alternatives. Include:

1. Decision being made and fixed constraints.
2. Shared fixture and edge cases.
3. Candidate previews at equivalent viewports.
4. Named axes and tradeoffs.
5. Per-candidate scorecards with observable 10/10 definitions.
6. Comparison summary and recommended next validation.

### Final Review / Handoff

Use after direction confirmation or an explicit final request. Include confirmed behavior, hierarchy, component/token mapping, state/responsive/localization/accessibility matrix, scorecard, rendered verification, and remaining external checks.

## Feedback synthesis

When the user likes parts of multiple candidates:

1. Record the favored property and the user need it serves, not only “take the header from A.”
2. Check that the properties share a coherent hierarchy and interaction model.
3. State the synthesis rule and the tradeoff it introduces.
4. Create the combined direction.
5. Retain one or two closest originals for comparison until the synthesis is confirmed.

Do not create a feature buffet. If favored parts conflict, expose the conflict and ask the user to choose the governing priority.

## Recover from “이게 아닌데”

First determine whether the user rejects the design direction, evidence, or report shape. When the format is the problem, name the other two modes and recommend one switch. Do not advertise the menu after a successful report.
