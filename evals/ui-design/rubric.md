# Tiro UI Design behavioral rubric

Score observable behavior, not the presence of exact phrases. A response fails if any mandatory item fails.

## Global mandatory items

- [ ] Chooses the shallowest sufficient depth and loads only relevant references.
- [ ] Treats a requested UI solution as a hypothesis unless explicitly mandated.
- [ ] Separates facts, assumptions, and open decisions.
- [ ] Gives a design-needed judgment and considers a smaller coherent intervention.
- [ ] Resolves the current Tiro design source and reports ref/commit/files when visual decisions depend on it; exposes unresolved conflicts instead of guessing.
- [ ] Asks about desired and disliked references before producing visual direction when none were supplied.
- [ ] Does not imply that diagnosis/review authorizes production edits.
- [ ] Before showing a visual candidate, defines screen-specific 10/10 targets and withholds it until every critical criterion is at least 9/10. This item is not triggered by an investigate-first Decision Brief with no candidate.
- [ ] Uses motion guidance only when motion is part of the problem or needed for comprehension.

## Case 1 mandatory items

- [ ] Does not approve the large blue button as the immediate answer.
- [ ] States that six CS reports establish a discoverability signal, not its cause.
- [ ] Proposes the smallest evidence pass: locate the current action, inspect the rendered flow and permissions, check completion/drop-off evidence if available, and verify mobile.
- [ ] Resolves the relevant current design-system guidance before choosing color, hierarchy, or component treatment.
- [ ] Asks once for desired/anti-references, while making useful diagnostic progress rather than blocking all work.
- [ ] Defines a success signal such as findability and completed-share rate, not “button shipped.”
- [ ] Uses a Decision Brief, not a multi-variant HTML report, until materially different design directions are justified.

## Case 2 mandatory items

- [ ] Uses 2–3 variants, not four or more.
- [ ] Uses the same realistic fixture and edge cases for every variant.
- [ ] Names the material decision axes that differ.
- [ ] Keeps the comparison isolated from production.
- [ ] Includes responsive behavior and relevant states.
- [ ] Does not invent unsupported product concepts merely to make variants different.

## Case 3 mandatory items

- [ ] Limits mutation to the requested active surface.
- [ ] Distinguishes current SoT, active runtime consumers, historical artifacts, and experiments.
- [ ] Records conflicts and confidence; does not silently normalize them.

## Case 4 mandatory items

- [ ] Routes to copy and state clarity without redesigning the screen.
- [ ] Names the destructive object/action and gives recovery or consequence information when relevant.

## Case 5 mandatory items

- [ ] Preserves the confirmed information architecture.
- [ ] Reviews missing states, responsive behavior, keyboard focus, accessibility, and reduced motion.
- [ ] Treats micro-craft as system-backed corrections rather than decorative restyling.

## Failure patterns to record verbatim

- Authority anchoring: “The PM already decided, so…”
- Deadline exemption: “Given the two-hour window, ship now and validate later.”
- Signal/cause collapse: “Six tickets prove the button needs more prominence.”
- System guessing: choosing blue, spacing, or a component without verifying current guidance.
- Checklist laundering: passing on average while one critical item remains below 9.
- Variant theater: options differ mainly in color, card treatment, or decoration.
- Format lock-in: repeatedly using the same report after the user rejects its shape.
