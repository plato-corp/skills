# Interaction and motion craft

Read this module for every new landing `craft` and `release`, for the `motion` action, and whenever a correction changes hover, focus, pressed, open, close, loading, success, scroll, sticky, or animated behavior.

The default landing deliverable includes complete interaction behavior. Motion is designed with the component and carrier; it is not decoration added after the resting page is approved.

This contract adapts the interaction guidance from [`jakubkrehel/make-interfaces-feel-better`](https://github.com/jakubkrehel/make-interfaces-feel-better) to Tiro. Tiro's verified design system, site family, approved source, and this landing contract remain authoritative.

## Start from the approved experience

For a new landing, motion ideation happens during `shape`, `integrate`, and `direction`; read [motion-storyline.md](motion-storyline.md). `Craft` begins only after the composition and its narrative movement are approved together as an experience baseline.

At implementation, record the approved resting frame as a **static baseline** for each affected viewport and state:

```text
Route / viewport / zoom / DPR:
Locked copy and heading breaks:
Locked font family / computed size / line height:
Locked colors and area distribution:
Locked container / spacing / section order:
Locked surfaces / borders / radii / shadows:
Default carrier frame and visible evidence:
Explicitly permitted resting-state deltas:
```

The rendered **resting state** after interaction work must match this baseline. This is an implementation parity check, not a static-first design method. A motion pass cannot reinterpret copy, typography, color, max width, spacing, section structure, carrier, or default visual hierarchy after the experience baseline is locked. Change one of those only through its owning landing action and record the new lock first.

Under `fidelity-port`, preserve only source-owned interaction and motion. Do not add micro-craft because the destination feels less lively than the approved source.

## Build two motion lanes

### Functional interaction — required

Every interactive component must define the applicable states together with its initial implementation:

`default / hover / focus-visible / pressed / disabled / loading / open / closed / success / failure / exit / reduced motion`.

Also record pointer, keyboard, and touch behavior. A state that does not apply is marked `N/A`; it is not silently omitted.

### Explanatory motion — earned

Animate a carrier only when time, continuity, procedure, causality, spatial change, or direct manipulation makes the evidence easier to understand. Define:

```text
Purpose:
Trigger:
Start / active / exit:
User-stoppable states:
What becomes clearer than in the static frame:
Static and reduced-motion equivalent:
Responsive reassembly:
Runtime and offscreen behavior:
```

The first static frame must already communicate the claim and next action. Motion may clarify meaning; it cannot supply missing meaning.

## Four-gate filter

Before creating a custom motion sequence, pass all four gates:

| Gate | Pass condition |
|---|---|
| Frequency | Repetition will not become tiring at its expected session frequency |
| Purpose | It provides Feedback, Spatial consistency, State indication, Preventing a jarring change, Explanation, or rare bounded Delight |
| Speed | The duration matches the interaction and never delays the next action |
| Function | The same result is not already communicated clearly without motion |

Reject the sequence when any gate fails. Shared control-state primitives do not count as custom sequences; limit a page to the few evidence-bearing motions that survive the filter.

## Tiro motion grammar

Use the current repository's easing tokens and motion primitives before adding values or dependencies. Keep page chrome and outer component geometry in plane.

| Interaction | Starting range |
|---|---|
| Press feedback | `100–160ms`; default `120ms`, `scale(.96)`, never below `.95` |
| Hover or compact state change | `125–180ms` |
| Popover or dropdown | `150–220ms` |
| Accordion or disclosure | `180–240ms` |
| Dialog or drawer entry | `180–300ms` |
| Dialog or drawer exit | `120–200ms`, usually faster than entry |
| Rare staged group entrance | `30–80ms` between items; one bounded sequence only |

- Use CSS transitions for interruptible state changes and keyframes only for a staged, finite event.
- Prefer **transform and opacity**. Animate layout only when real content expands or collapses and the motion prevents a jarring reflow.
- Never use `transition: all`. Name every transitioned property.
- Use `will-change` only for a measured, bounded performance need; do not spread it across the page.
- Do not scale up, lift, tilt, bounce, spring, or deepen the shadow of an outer landing control on hover. Press feedback may scale down within the range above.
- Gate hover behavior with `(hover: hover) and (pointer: fine)`. Touch cannot depend on hover.
- For a contextual icon state, keep both states in one stable box and crossfade with `opacity`; a newly confirmed icon may enter from `scale(.25)` and `blur(4px)` to rest without bounce.
- Keep changing numbers stable with tabular numerals and a fixed measure.
- In React presence transitions, suppress first-render theatrics with `initial={false}` unless the approved carrier explicitly requires an entrance.
- Preserve a minimum `44px × 44px` touch target even when the visible glyph or control is smaller.

## Reduced motion and interruption

Under `prefers-reduced-motion`, settle immediately on a complete, meaningful state. Remove nonessential translation, scale, parallax, smooth scrolling, stagger, and continuous loops; retain only the smallest state indication needed to understand the interaction.

Every motion must tolerate interruption. Rapid open/close, route change, repeated clicks, reversed scroll, focus movement, background-tab suspension, and component unmount cannot leave hidden content focusable, lose focus return, duplicate actions, or strand an intermediate frame.

Continuous carrier motion must pause when offscreen or hidden. Do not start an unbounded animation loop for decoration.

## Build sequence

1. For a new landing, receive the approved experience baseline from `motion-storyline`; if it is missing, return to storyline and composition instead of decorating a finished static page. For fidelity or bounded polish, capture the existing static and interactive baseline before changes.
2. Inventory all interactive states and existing behavior before replacing a component.
3. Reuse one shared state primitive for repeated actions; shortlist only custom motion that passes the four gates.
4. Implement `entry / active / exit` together. Do not ship an entrance without the matching exit when the surface closes in place.
5. Implement touch, keyboard, and reduced-motion behavior in the same pass.
6. Capture resting-state parity first, then the meaningful interaction states at their actual viewport.

When the external `make-interfaces-feel-better` skill is available, use it after the experience baseline is locked as a bounded micro-craft specialist. Its allowed scope is interaction mechanics, icon-state continuity, optical alignment inside the locked box, target size, and motion restraint. It does not author the page's motion storyline. Discard or separately route any advice that changes Tiro typography, colors, spacing, radii, shadows, copy, page structure, carrier, or default hierarchy. Do not install or fetch a new capability without the authorization required by the active environment; this internal contract remains the fallback.

## Release evidence

Record:

```text
Static baseline comparison:
State inventory and N/A decisions:
Entry / active / exit capture:
Keyboard focus and focus return:
Touch and hover-capability result:
Reduced-motion result:
Rapid reversal or repeated-action result:
Layout shift and runtime result:
Continuous motion offscreen result:
Console result:
Release verdict:
```

Release fails when the resting design drifts, an applicable interaction state is missing, an entrance has no usable exit, meaningful content exists only after motion completes, touch or keyboard behavior loses the action, reduced motion loses the claim, or continuous decorative rendering remains active offscreen.

## Common mistakes

| Mistake | Correction |
|---|---|
| Motion is postponed until the visual page is “finished” | Define functional states while building each component and explanatory motion with its carrier |
| Every section receives a reveal | Keep only sequences that pass all four gates |
| A polish specialist changes the static design | Restore the static baseline and route the proposed visual change through its owning landing action |
| Entry feels polished but close snaps away | Keep the surface mounted through its exit, then remove or close it |
| Desktop motion is disabled wholesale on tablet | Author the pressured-width state or an equivalent user-controlled/static carrier |
| Reduced motion means removing the result | Remove the effect while preserving the final meaning and action |
