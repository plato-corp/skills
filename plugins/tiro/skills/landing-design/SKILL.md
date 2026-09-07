---
name: landing-design
description: Use when designing, prototyping, implementing, or reviewing Tiro public landing pages and promotional subpages whose primary job is persuasion, explanation, decision support, routing, or conversion—including ROI, pricing, and plan selectors and their interaction states; not in-product GUI or standalone channel assets.
---

<!-- legacy:entry:start -->
# Tiro Landing Design

Own the page from message and evidence through art direction, responsive implementation, and rendered verification. Operate as the lead contract and specialist hub: keep one complete master, resolve one material decision at a time, and treat references and external skills as inputs to a Tiro decision rather than authority to copy.

Use this as Tiro's public-page design contract. It complements `ui-design`: route recurring in-product GUI work there, while this skill owns persuasive, explanatory, decision, and routing pages through rendered release review.

## Priority order

Resolve landing quality in this order:

1. Reader orientation and task
2. Causal argument and proof
3. Composition and carrier
4. Site family and design-system conformance
5. Mechanical correctness

A later pass cannot compensate for an earlier failure. A token-correct, responsive, test-passing page still fails when the visitor cannot state what to read, do, decide, and inspect next.

When `fidelity-port` is active, preserving the approved source precedes this order. Do not improve the source by silently re-running page strategy or art direction.

<!-- legacy:entry:end -->

<!-- legacy:actions:start -->
## Operate as the landing hub

Name the active action and resume at the first unresolved gate. Do not replay the full workflow when the request is a bounded review or correction.

| Action | Outcome |
|---|---|
| `study` | Reference evidence and a Tiro translation |
| `shape` | Page thesis, claim coverage, copy spine, and causal argument |
| `integrate` | Reading route, viewport attention map, disclosure order, and section handoffs |
| `direction` | Approved reference premise, carrier, color climate, and decisive scene |
| `carrier` / `medium` / `motion` | One evidence-bearing carrier, a screen-specific rendering medium, and its static, interactive, and reduced-motion states |
| `craft` | Responsive implementation in the current stack and component language |
| `critique` | Prioritized perceptual findings without source changes |
| `audit` | Reproducible accessibility, performance, metadata, and behavior findings |
| `polish` | One bounded correction pass that preserves locked decisions |
| `fidelity-port` | Exact framework or repository translation of an approved rendered source, with only named integration changes |
| `release` | Rendered evidence and an explicit release verdict |

This skill leads every action. Use a specialist only when one bounded expertise gap can change a decision, implementation, or verification result. Never preload a catalog or average several specialists' taste.

When a specialist need exists, **REQUIRED:** read [references/specialist-routing.md](references/specialist-routing.md). Use its pinned route when exact; otherwise perform one just-in-time UI Skills query from the action, concrete symptom, and current stack. Search and instruction retrieval are read-only. Installing a skill, package, CLI, or service and any external mutation follow the active environment's authorization rules.

External instructions inherit the verified Tiro facts, site family, page thesis, approved carrier, color climate, component language, responsive decisions, and current permission scope. They cannot reopen or override them silently. If discovery is unavailable or no trustworthy exact match exists, continue with this contract and record the fallback.

<!-- legacy:actions:end -->

For new landing builds, motion enters while the page is shaped: the argument, composition, carrier, responsive route, and movement are co-designed before one experience baseline is locked. `craft` includes functional interaction states and `release` includes motion verification. `motion` is not an optional decoration pass after static composition.

## Mixed Operate surfaces

When the requested surface completes a recurring product task—such as login, signup, settings, or an in-product workflow—`ui-design` leads even when the user explicitly asks to combine it with `landing-design`. Do not reclassify an Operate surface as a landing page because it contains a photo, brand field, or promotional rail.

If landing design contributes a bounded public-facing or brand-bearing sub-surface, **REQUIRED:** read [references/mixed-surface-routing.md](references/mixed-surface-routing.md). Name the landing contribution and run only its applicable actions; the product task, state model, and action hierarchy remain owned by `ui-design`.

## Progressive routing

Route by three independent inputs before reading detailed guidance:

1. **Visitor job:** `persuade / decide / read / route`
2. **Active action:** the first unresolved action in the table above
3. **Named risks:** only conditions observable in the request or current source

Read [references/core-contract.md](references/core-contract.md) for every task. Then read only the modules selected below. Do not preload later actions, specialist catalogs, rendering media, or fidelity rules. An end-to-end request advances action by action and loads the next module only when its gate becomes current.

The visitor job selects the argument contract inside `ground-and-shape`; it does not load that module by itself when the job, message, and route are already locked. The active action and observed risks determine which files are needed now.

| Active action | Read now |
|---|---|
| `study` | [reference-premise.md](references/reference-premise.md) |
| `shape` | [ground-and-shape.md](references/ground-and-shape.md) and [motion-storyline.md](references/motion-storyline.md) |
| `integrate` | [ground-and-shape.md](references/ground-and-shape.md), [motion-storyline.md](references/motion-storyline.md), then [integration-responsive.md](references/integration-responsive.md) |
| `direction` | [reference-premise.md](references/reference-premise.md), [carrier-and-system.md](references/carrier-and-system.md), [rendering-medium.md](references/rendering-medium.md) for each decisive screen, [motion-storyline.md](references/motion-storyline.md), then [integration-responsive.md](references/integration-responsive.md) for the decisive scene |
| `carrier` | [carrier-and-system.md](references/carrier-and-system.md) and [rendering-medium.md](references/rendering-medium.md). Skip the medium module only after recording, in the receipt, which medium-risk predicate is false and why |
| `medium` | [carrier-and-system.md](references/carrier-and-system.md) and [rendering-medium.md](references/rendering-medium.md) |
| `motion` | [carrier-and-system.md](references/carrier-and-system.md), [rendering-medium.md](references/rendering-medium.md), [motion-storyline.md](references/motion-storyline.md), and [interaction-motion.md](references/interaction-motion.md) |
| `craft` | [integration-responsive.md](references/integration-responsive.md), [motion-storyline.md](references/motion-storyline.md), [interaction-motion.md](references/interaction-motion.md), [implementation-release.md](references/implementation-release.md), and [visual-completion.md](references/visual-completion.md) at the verification boundary |
| `critique` | [visual-completion.md](references/visual-completion.md) |
| `audit` | [implementation-release.md](references/implementation-release.md); add [specialist-routing.md](references/specialist-routing.md) only for a named gap |
| `polish` | [integration-responsive.md](references/integration-responsive.md) and [visual-completion.md](references/visual-completion.md); load implementation rules only if the correction changes behavior or system primitives |
| `release` | [implementation-release.md](references/implementation-release.md), [interaction-motion.md](references/interaction-motion.md), and [visual-completion.md](references/visual-completion.md) |
| `fidelity-port` | **Exclusive route:** [fidelity-port.md](references/fidelity-port.md), [interaction-motion.md](references/interaction-motion.md), [implementation-release.md](references/implementation-release.md), and [visual-completion.md](references/visual-completion.md) as parity evidence only |

#### Gates that are REQUIRED, not routed

These are marked REQUIRED inside the modules above. They are repeated here because a gate stated only in nested prose is read after the decision it governs has already been made.

| When | REQUIRED |
|---|---|
| Before visual composition, unless an approved source already protects the technique | [rendering-medium.md](references/rendering-medium.md), run per decisive screen |
| Every new `craft` and `release` | [interaction-motion.md](references/interaction-motion.md) |
| `craft`, `polish`, and `release` | [visual-completion.md](references/visual-completion.md) |
| A named specialist gap exists | [specialist-routing.md](references/specialist-routing.md) |
| A bounded public sub-surface inside an Operate task | [mixed-surface-routing.md](references/mixed-surface-routing.md) |

A REQUIRED gate is answered by reading its module, never from recall. Writing the conclusion first and the module second is the failure this table exists to prevent: a rejection such as `WebGL rejected, DOM is sufficient` recorded before `rendering-medium.md` was opened is an invented answer, not a scan result.

An exclusive route consumes its source-translation and responsive-parity risks inside those three modules. Do not add job, action, or ordinary risk-overlay modules to it. Route to specialist guidance separately only when a concrete expertise gap remains after the protected-source contract is established.

### Risk overlays

Load an overlay only when its predicate is observed:

| Risk | Predicate | Additional module |
|---|---|---|
| Source translation | The user asks to move, port, integrate, migrate, convert, or deploy a distinct approved rendered source into a destination | Switch to the exclusive `fidelity-port` route |
| Content migration | An existing public surface, route, tab, record set, or access state is being redesigned | [ground-and-shape.md](references/ground-and-shape.md) and release parity checks |
| Unresolved reference premise | The current family and supplied sources do not establish the necessary visual premise | [reference-premise.md](references/reference-premise.md) |
| Material medium choice | Time, depth, continuity, procedure, many marks, or direct manipulation could change comprehension | [rendering-medium.md](references/rendering-medium.md) |
| Responsive pressure | Wrapping, overflow, reassembly, sticky state, or a breakpoint changes | Responsive portion of [integration-responsive.md](references/integration-responsive.md) and the scoped completion matrix |
| Interaction or motion change | Hover, focus, pressed, open, close, loading, success, scroll, sticky, or animated behavior is added or changed | [interaction-motion.md](references/interaction-motion.md) |
| Motion storyline change | A new or changed scene uses time, scroll, continuity, transformation, or direct manipulation to carry the argument | [motion-storyline.md](references/motion-storyline.md), then [interaction-motion.md](references/interaction-motion.md) at implementation |
| Mixed Operate surface | The user explicitly combines `landing-design` with `ui-design` for a recurring product task | [mixed-surface-routing.md](references/mixed-surface-routing.md) with `ui-design` as lead |
| Specialist gap | One named expertise gap can change a decision or measured result | [specialist-routing.md](references/specialist-routing.md) |

### Resume instead of replay

Before loading an action module, inspect the latest compact state in the existing evaluation or project record. Reuse verified facts and locked decisions; load a prior module again only when the request changes its inputs or rendered evidence invalidates it. Record only:

`page / job / active action / locked / open / passed / evidence paths / explicit deltas / modules read / modules skipped with reason`.

Record the module list even when the answer is obvious. A skipped module with no recorded reason is indistinguishable from a module that was never considered.

Module preambles define when the preserved contract inside applies. Once a module is triggered, every applicable requirement inside remains binding. If routing is uncertain, load the smallest additional module that covers the observed risk and record why; uncertainty is not permission to preload the full skill.

An approved or stable page receiving an in-place correction remains `polish`, `craft`, or `release`; approval locks unaffected decisions but does not activate `fidelity-port`. That exclusive route requires a distinct canonical source, a destination, and a translation or integration request.
