# Interface quality

Use for every visual candidate, implementation hardening, and final review.

## Frame the surface

Define one primary outcome. Within one second, the intended user should understand the primary object, its current state, and the next action. For expert workflows, reduce guidance only when vocabulary and control placement are already learned; for infrequent or consumer tasks, keep necessary text labels and recovery cues.

Calibrate three axes:

- **Change scope:** correction → recomposition → new pattern.
- **Density:** scanning speed versus detail needed at decision time.
- **Guidance:** expert shorthand versus explicit labels and help.

## Build hierarchy before decoration

1. Inventory information and actions.
2. Rank primary, secondary, metadata, and exceptional content.
3. Make the order readable with type role, weight, proportion, alignment, and space.
4. Add separation only as needed: layout/space → divider → background → elevation.
5. Use color and lines to support hierarchy, never to manufacture it.

Every visible element must reduce cognitive load, expose state, enable action, or create necessary structure. Remove it otherwise.

## Use the system, not remembered values

- Read only the active token/component/foundation files required by the surface.
- Use semantic tokens and existing primitives/composites. If a semantic role is absent, propose it; do not choose a nearby primitive by taste.
- Preserve Primitive → Composite → Screen ownership and verify active consumer paths.
- Do not assume theme support, font families, icon policy, radius, density, or motion from an old report.
- Treat shared UI as a component candidate before duplicating screen-local markup.

## Design the whole state model

Cover applicable states at layout time:

`default · hover · pressed · focus-visible · disabled · loading · empty · error · success · overflow`

Also verify:

- narrow and wide layouts, content growth, and locale expansion;
- stable loading geometry and recoverable errors;
- keyboard order, visible focus, touch target, contrast, and non-color cues;
- truncation, wrapping, long names, missing metadata, and permission differences.

## Anti-slop and final craft

- Avoid card-everything surfaces, pill overuse, scattered actions, decorative gradients, oversized headings, and needless dashboard framing.
- Use one alignment axis per region and keep related actions together.
- Check nested radii: inner radius should visually derive from outer radius and inset, not repeat it blindly.
- Optically align icons and labels; geometric centering is not always visual centering.
- Give images and light surfaces enough boundary contrast without decorative frames.
- Press feedback must read as a state change, not a layout jump.
- Keep metadata inline when scanning benefits and the content still survives narrow widths.
- Motion cannot rescue weak hierarchy or unclear state.

## Candidate release gate

Choose 4–6 criteria that are critical for this surface. Define 10/10 before scoring. Example for a Share-discoverability decision:

| Criterion | 10/10 means |
|---|---|
| Task clarity | A permitted user can locate the share entry and predict what it does without competing primary actions. |
| Causal fit | The intervention addresses the verified failure step, not merely the complaint wording. |
| System fit | Hierarchy, component, token, and state choices trace to current governing sources. |
| Completion | Permission, loading, success, failure, copy-link, and mobile/narrow behavior are specified. |
| Accessibility | Keyboard/touch operation, visible focus, labels, contrast, and non-color meaning are intact. |

For every criterion:

```text
Criterion: <screen-specific name>
10/10: <observable target>
Current: <0–10 with evidence>
Gap: <concrete correction, or none>
```

Do not share a candidate until every critical item is at least 9/10. Never pass on average. Self-scoring is a release gate, not user-validation evidence; keep research and outcome measurement separate.

## Final review contract

1. Confirmed primary outcome and preserved constraints.
2. Grounding receipt and component/token mapping.
3. Changed behavior and information hierarchy.
4. State, responsive, localization, and accessibility matrix.
5. Screen-specific scorecard with 10/10 definitions.
6. Rendered verification performed and remaining external validation.
