# Motion storyline

Read this module while shaping, integrating, or directing a new landing page, before the master is locked. Also read it when a new or changed carrier depends on time, scroll, continuity, or direct manipulation.

**Motion and composition are co-designed.** A new landing is not composed as a static page and animated afterward. Its reading route defines what remains still, what changes, what the visitor controls, and how one state hands evidence to the next.

This module owns narrative behavior. [interaction-motion.md](interaction-motion.md) owns the detailed implementation and verification of approved behavior.

## Translate the argument into change

Start with the page thesis and section argument. Give each decisive scene a **motion hypothesis** before choosing its final composition:

```text
Narrative beat:
Visitor belief — before / during / after:
Evidence visible at rest:
What changes and why:
Trigger — viewport / scroll / pointer / keyboard / explicit control / time:
Visitor control and interruption:
Entry / active / exit / reduced-motion states:
Incoming section handoff:
Outgoing section handoff:
Static equivalent:
```

Motion must answer a narrative question. Useful roles include:

- **Reveal causality:** an input becomes a retained result.
- **Preserve continuity:** one object, record, or idea remains identifiable across states.
- **Explain sequence:** ordered work becomes clearer through controlled progression.
- **Show a boundary:** information crosses, stops at, or remains inside a verified constraint.
- **Confirm agency:** the visitor's action visibly changes the answer or state.
- **Hand off attention:** the ending state of one section becomes the starting premise of the next.

If no role improves comprehension, keep the scene still and record that decision. Stillness is part of the motion rhythm.

## Compose the page rhythm

Classify every section as one of:

| Mode | Use |
|---|---|
| Static anchor | Reading, proof, comparison, or recovery after a dense scene |
| Functional interaction | Disclosure, calculator, selector, form, navigation, copy, modal, or stateful action |
| Explanatory motion | Time, continuity, procedure, causality, or spatial relationship carries evidence |

Build the reading route as alternating intensity, not repeated reveals. A viewport may contain one major explanatory motion and at most one supporting motion. Adjacent sections cannot both demand continuous attention unless the same evidence-bearing object visibly connects them.

Choose the trigger from the visitor's job:

- Use scroll when progression belongs to the reading argument and every stoppable frame remains valid.
- Use an explicit control when the visitor is comparing, inspecting, replaying, or choosing.
- Use pointer movement only for optional inspection; meaning and navigation must remain available to keyboard and touch.
- Use finite automatic time only for a short demonstration that settles on the most informative state and can be replayed or ignored.
- Do not use parallax, looping decoration, or entrance choreography as a substitute for a weak section transition.

## Design section handoffs with motion

For every adjacent pair, decide whether the handoff is:

- **Continuation:** the same carrier or state persists while the claim advances.
- **Transformation:** the outgoing state visibly becomes the incoming evidence.
- **Cut:** motion stops and whitespace or a surface change creates an intentional editorial break.
- **Control handoff:** an automatic explanation ends and the visitor receives a stable action or inspectable state.

Define both edges before implementing either section. The transition fails when the page must autoplay through empty or ambiguous frames, when movement hides a mismatched width or spacing decision, or when the incoming section makes sense only after the effect finishes.

## Approve an experience baseline

Do not approve a new direction from one screenshot. Lock an **experience baseline** containing:

```text
Resting / active / exit / reduced-motion frames:
Page and section narrative beats:
Trigger and visitor control:
Carrier identity across states:
Static meaning at every stoppable state:
Desktop / tablet / mobile reassembly:
Allowed implementation tolerance:
Locked copy / type / color / geometry / surface decisions:
```

This experience baseline becomes the source of truth for `craft`. Its resting frame is the later static baseline used to detect implementation drift; the static frame does not precede or constrain motion ideation.

When motion is material and unresolved, prototype only the smallest decisive scene at its real desktop and mobile size. Compare a static treatment and the strongest plausible motion treatment with copy, facts, carrier, geometry, and color fixed. Approve motion only when the time-based version produces a visible communication gain.

## Existing and fidelity work

For a bounded polish of an existing page, inventory current static and interactive behavior before proposing changes. Preserve unaffected behavior.

Under `fidelity-port`, the approved source already supplies the experience baseline. Capture its resting and meaningful interaction states and translate them mechanically; do not reopen its motion storyline or invent missing delight.

## Handoff to interaction craft

At `craft`, pass the approved experience baseline to [interaction-motion.md](interaction-motion.md). Implementation may tune durations or easing within the existing system when that does not change the narrative beat, spatial path, state order, or resting composition.

`jakubkrehel/make-interfaces-feel-better` may refine micro-interaction mechanics after this baseline is locked. It does not decide the landing's narrative beats, motion carrier, scroll storyline, or section handoffs.

## Common mistakes

| Mistake | Correction |
|---|---|
| Finish the static page, then ask where animation fits | Write the motion hypothesis while shaping the decisive scene |
| Make every section enter | Alternate explanatory motion with static anchors |
| Use scroll because the page is long | Use scroll only when position represents progress through the argument |
| Let motion repair a weak composition | Make every stoppable frame work as a composition first |
| Treat a micro-craft skill as the motion director | Let the landing argument own the storyline; use micro-craft for state quality |
