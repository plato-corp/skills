# Implementation and release

Read this module for `craft`, behavior-changing corrections, `audit`, `release`, and fidelity integration. Apply each check in proportion to the changed contract: full-page rules remain mandatory for a new master or release, while a bounded correction verifies the affected component, its nearest layout/interaction boundaries, and representative regressions.

Under `fidelity-port`, use perceptual rules only to detect source drift. Do not improve a matching approved source.

Scope the legacy full-route language below through the active route:

- New masters and structurally changed routes use the complete viewport matrix and comprehension checks.
- Bounded corrections use the exact defect, nearest pressure or interaction boundaries, and one unaffected regression viewport unless the fix changes more.
- Fidelity ports use the source's recorded desktop/mobile provenance plus changed integration boundaries. Generic comprehension, hierarchy, art-direction, and every-breakpoint checks do not become redesign gates when the destination matches the source.

For every new `craft` and `release`, **REQUIRED:** read [interaction-motion.md](interaction-motion.md). A new build implements the approved experience baseline produced with [motion-storyline.md](motion-storyline.md); its resting frame supplies the static parity baseline. Verify that baseline before interaction captures so micro-craft cannot conceal copy, typography, color, spacing, container, or section drift. A bounded correction that does not touch behavior may reuse previously verified interaction evidence; any behavior change reopens the affected state contract.

<!-- legacy:implementation:start -->
## 7. Implement and verify the rendered page

**REQUIRED for `craft`, `polish`, and `release`:** read [references/visual-completion.md](references/visual-completion.md). Its viewport attention contract, progressive-disclosure rule, severity model, and correction loop are release-blocking.

Implement the approved screen-specific medium inside the current stack, tokens, components, and shared chrome. The stack constrains integration; it does not retroactively choose DOM/CSS for every carrier. Keep a new dependency behind the active authorization boundary. Use real rendered product UI or verified captures when product evidence carries the message; do not redesign the product inside a marketing mockup. Preserve semantic heading order, visible focus, sufficient contrast, 44px targets, stable media geometry, keyboard behavior, and reduced motion. Advanced renderers own only their bounded carrier layer: reserve its layout before load, keep message and actions available without it, and verify the meaningful static, reduced-motion, unsupported-device, loading, and failure states.

At implementation and release time, route only named risks. Motion jank, React rendering, accessibility, metadata, Core Web Vitals, and browser-anchored review are separate specialist concerns; combine at most three only for a broad release review. General critique, Hallmark audit or study, and Impeccable critique or polish are second opinions, not permission to generate a new direction. Reconcile every surviving finding as `contract → rendered evidence → deterministic correction`.

Before replacing, merging, or promoting a page-section variant, inventory the behavior owned by the outgoing implementation: shared-header fixed and direction-aware states, dropdown and mobile navigation, section entry, scroll progress, screen or copy transitions, replay, hover/focus/pressed, and reduced motion. Map each behavior to the incoming implementation and verify it in the integrated route. A visually correct static replacement is a regression when an intentional interaction silently disappears.

Before using a screenshot to judge whitespace, density, type size, or section height, record its provenance: CSS viewport, browser zoom, device-pixel ratio when relevant, full-page or crop, and responsive state. If any value is unknown, spatial findings remain provisional and cannot block release until reproduced in an actual browser. Command-minus captures and distant boards may reveal relationships but do not prove absolute spacing.

Capture the actual integrated page at the agreed desktop, tablet, and mobile widths. Unless the active project defines a stricter matrix, verify `1440 / 1024 / 768 / 430 / 390 / 360px` plus one pixel immediately above and below every changed breakpoint. Compare neighboring widths for a quality valley: an intermediate width that is materially more cramped, accidental, or visually unfinished than both neighbors fails even when nothing overflows. Run the required visual-completion gate first, including the viewport attention contract and 2-second, 5-second, headings-only, squint, transition-crop, and prototype-smell tests. Then perform the mechanical pass below. A clean mechanical pass cannot prove hierarchy, rhythm, or message comprehension.

Verify:

- the first viewport communicates the approved message and action;
- headings alone reveal one accumulating page argument rather than a topic list;
- the intended belief and after-feeling are supported by visible evidence, and anti-feelings are absent;
- reference translations and the chosen carrier remain visible;
- each decisive screen uses its approved rendering medium for the recorded communication gain; DOM/CSS is not an unexamined default, and Canvas, video, WebGL, shaders, or 3D never leave an empty or meaning-poor fallback;
- every title alignment, visual deviation, and closing transition still has its stated job at each breakpoint;
- the same named bounds owner and coordinate frame survive from brief to DOM, CSS, and render; occupied anchors and intentional empty regions close the intended reading path;
- no orphan line, color, decoration, or motion-only explanation remains;
- Korean wrapping, image crops, overflow, layout shift, and every stoppable motion state;
- intrinsic, maximum, and collapsed widths for action groups; short controls are not stretched by a blanket mobile rule;
- every changed breakpoint at `-1px / +1px`, and no quality valley between the canonical widths;
- navigation, CTA destinations, forms, and success states;
- source-route parity: headings, body copy, lists, dates, links, counts, deep links, and public/restricted/locked/request states; every omission or merge has explicit approval;
- the design-system role map against rendered typography, color, spacing, radius, elevation, icon, action, and interaction states; at least one primary and one secondary action are checked in their applicable browser states;
- semantics, focus, contrast, reduced motion, metadata, performance risks, tests, build, and console output.

For every candidate finding, record `contract → rendered evidence → deterministic correction`, then try to falsify it with capture conditions, sibling counterevidence, responsive states, and documented exceptions. Delete an unsupported finding. Any visual-completion Blocker or Major prevents release. Group surviving defects into one bounded correction pass, then recapture the same reference frames. Source checks and distant board views do not prove visual completion. User approval is the final design gate unless the user explicitly activated Autonomous mode.

<!-- legacy:implementation:end -->

<!-- legacy:quick-reference:start -->
## Quick reference and red flags

| Decision | Pass condition |
|---|---|
| Approved-source port | `fidelity-port` is selected before edits; canonical source, ownership boundary, protected decisions, explicit deltas, mechanical translation, and pre-edit checks prevent visual reinterpretation |
| Family Hero | Shared grammar is visible across sibling pages; exceptions are page-job driven |
| Content migration | Every source route, tab, content item, link, count, and access state is preserved or has an explicitly approved omission; dense reviewer workflows are not silently flattened into one scroll |
| Decision route | Input precedes the primary answer, rationale follows it, `input → result → save` is visible, and supporting documents are progressively disclosed |
| Viewport attention | One dominant item, no more than two supporting items, one next cue, and an explicit de-emphasis decision |
| Design system | Every repeated primitive and visible action traces to an active Tiro component or token alias; typography and applicable interaction states are verified in the browser |
| Reference premise | 2–4 references have distinct jobs, visible extractions, Tiro translations, and named surfaces not to copy; an existing implementation is not implicit approval |
| Carrier and asset | One photo, product-state, or graphic carrier owns the message; its evidence, source or production method, and fallback are explicit |
| Section model | Facts are classified before layout; non-peer relationships remain inferable with heading and body hidden |
| Rendering medium | Each decisive screen compares plausible media and records one winner, observable gain, closest rejected alternative, stack and dependency fit, and meaningful fallback; advanced rendering is used only when it earns its runtime cost |
| Color climate | Dominant field and area distribution produce the intended after-feeling; inherited warmth or accent color does not drift into an unapproved chapter mood |
| Title rhythm | One home axis remains dominant; exceptions move the complete composition |
| Repeated macro | Same geometry contract, or one evidence-density reason for the difference |
| Bounded composition | Named bounds owner and stable coordinate frame; anchors, empty regions, reading path, and reassembly match the rendered box |
| Compound claim | Every important clause has visible, proportionate proof |
| Divider | Encodes a visible system or exact boundary after simpler separation was insufficient |
| Product depth | Current product source is named; chrome, functional overlays, product carriers, and marketing fields use distinct roles; values are aliases rather than local imitations |
| Hover geometry | Component bounds stay fixed; feedback is in-plane and focus-visible remains equally clear |
| Screenshot finding | Reproduced with known viewport and zoom before becoming release-blocking |
| Action width | Natural width, explicit cap, and a content-pressure collapse trigger; full-width only with local semantic cause |
| Responsive composition | No accidental wrap or quality valley; tablet/mobile reassemble the content instead of merely shrinking it |
| Closing CTA | Named anchor survives the relocation test; any new surface carries narrative or destination meaning |
| Visual completion | No Blocker or Major at 1440px or 390px after matching recapture; mechanical evidence remains separate |

Stop and re-open the relevant gate when any of these appear:

- “I will recreate the same feel in the destination stack” when an approved rendered source exists.
- A port begins by authoring a new page stylesheet, normalizing the Hero, changing card treatment, or remapping color area before a protected-decision ledger and source baselines exist.
- Shared site chrome, framework conversion, component extraction, or Autonomous mode is used as permission to change source-owned copy, type, color, layout, spacing, or responsive behavior.
- “Every exception has a local rationale” while the family or page still looks unstable.
- “The important parts are represented” used to replace exact migration, route parity, locked states, or the source visitor workflow.
- “The section already exists” used to skip reference, carrier, or color-climate approval.
- “The project is React” or “HTML is fastest” used as the rendering-medium decision without comparing the scene's communication ceiling.
- `Graphic` silently implemented as styled divs, or one renderer imposed across the page, without a screen-specific medium scan.
- WebGL, Three.js, a shader helper, Canvas, or video selected for novelty while its static, reduced-motion, loading, failure, or unsupported state loses the claim or action.
- “The new page concept must feel coherent” used to flatten gates, containment, hierarchy, sequence, or transformation into peer cards, records, or columns.
- Avoiding a category cliché by omitting image exploration instead of improving the evidence, casting, or transformation.
- Inheriting the site's dominant warm or chromatic field without checking the chapter's intended belief, after-feeling, and area distribution.
- “The widths are close enough” for repeated templates that should share an axis.
- “The tests pass” used as proof of message, hierarchy, or rhythm.
- A primary answer delayed by rationale, or plan details, assumptions, quote documents, and FAQ presented at equal weight.
- A viewport with multiple dominant items, no next cue, or no explicit de-emphasis decision.
- A section divider added because the next chapter is otherwise difficult to compose.
- A compound claim whose largest visual label names the tool or destination rather than the promised constraint.
- A spacing or density verdict inferred from a screenshot with unknown zoom.
- A short mobile action stretched to its container without block semantics or an explicit local stack.
- `nowrap`, smaller type, or tighter padding used before the parent layout is allowed to reflow.
- An intermediate width that looks worse than both a larger and a smaller checkpoint.
- `Top-left`, `center`, or `bottom-right` implemented inside a legacy column or nested cell without naming the governing outer box.
- A closing CTA whose surface supplies visual weight but no evidence, transition, or destination meaning.
- A decorative stage with a stronger shadow than its embedded product surface, or multiple local shadows attempting to imply one product family.
- An isolated metric whose task, before state, or after state is only discoverable in adjacent body copy.
- A card, button, CTA, row, image, or diagram panel that lifts, scales up, tilts, bounces, or gains a stronger shadow merely because the pointer entered it.

<!-- legacy:quick-reference:end -->
