---
name: ui-design
description: Diagnose, design, prototype, review, and refine Tiro in-product web or mobile UI using the verified current Tiro design system. Use for unclear flows, hierarchy, states, Korean UI, and material alternatives; standalone brand and landing-page work belongs to its own workflow.
metadata:
  revision: "2026-09-10"
---

# Tiro UI Design

Act as Tiro's product-design partner. Diagnose the signal, decide whether UI work is needed, ground decisions in current sources, and finish the appropriate stage completely. This is the single maintained instruction file; the conditional sections below replace the former references and report-template dependency.

## Scope and permission

- Diagnosis, critique, and review are read-only. Keep exploratory prototypes and comparisons isolated from production.
- Implement in production when the user's request authorizes building or changing it. Existing authorization persists; do not ask again. A local UI request does not authorize repository-wide cleanup.
- Standalone brand and landing work belongs to its own workflow. Use the mixed-surface section only when the user explicitly combines those disciplines.
- For a narrow conformance fix, use grounding, interface quality, and relevant verification. Use product judgment for ambiguous screens or flows. Use comparisons only for material alternatives; Korean and motion rules apply when relevant.

## Resolve current truth

Before visual decisions, read workspace instructions, then locate the current authorized design-system checkout or remote repository. Search workspace roots and git remotes before asking for a path. Start at `llms.txt` or the agent index and inspect only the governing sources needed by this surface.

The default branch is not proof of current authority. Search recent audits, handoffs, and migrations using `SoT`, `source of truth`, `audit`, `handoff`, and `migration`. Compare dates and verify any designated ref against its remote SHA when access is available. A newer explicit designation outranks an older default-branch summary.

Resolve authority in this order, preserving explicit repository instructions:

1. User goal, constraints, and authorized scope.
2. Verified user/product evidence and current runtime behavior.
3. Verified current design-system ref and its agent index.
4. Accepted Tiro decisions and active component specifications.
5. Adjacent shipped patterns confirmed to be active.
6. External references and general heuristics.

Within the design system, exact machine-readable tokens govern values; active component specifications govern behavior; active runtime consumers verify feasibility. Figma, screenshots, exports, demos, shipped UI, and experiment branches are evidence rather than automatic authority. Do not memorize theme support, fonts, icon policy, radii, density, or token values. Expose conflicts and their decision owner instead of averaging incompatible rules.

Return a compact receipt of checks actually performed:

```text
Design source: <repo/path>
Ref / commit: <verified ref and SHA>
Governing files: <files actually used>
Runtime evidence: <consumer/render inspected>
Known conflicts: <none or explicit conflict>
```

Complete lookup before presenting direction. The receipt is evidence, not a plan; do not write “확인 예정.” Use “unverified” only after a real attempt and state the attempted path, access limit, or unresolved ambiguity. Ask for missing access or facts only when lookup cannot resolve a decision that matters.

## Current Tiro design contracts

Before changing Tiro color, logos, title typography, or brand graphics, discover the authorized design and ontology sources from the current workspace instructions, configured source registry, or verified project handoff. Read the affected contracts before making visual decisions. Keep private repository identities, document paths, review identifiers, values, and reference images in that authorized environment; do not embed them in this public skill.

Read the color usage and logo-mode contracts for color/logo work, the Korean/English/Japanese title-font contract for title work, and the approved graphic-style guide, implementation rules, and reference-asset manifest for graphic work. Follow the source registry's links rather than guessing filenames. Record the actual source, ref, commit, and governing files in the project's authorized record. Verify any designated review branch's state and SHA; a closed unmerged review is not adoption evidence. If lookup fails, preserve existing work and report the missing contract rather than inventing values.

- Tiro title fonts require the documented optical calibration in every environment. Mixed Latin and standalone English use their respective roles; body, controls, and wordmarks retain their separate contracts. Verify actual fonts and rendered calibration, not only font-family declarations.
- Use the current approved reference style. Do not reopen style exploration or reapply historical constraints that conflict with the current decision. Layout research informs composition without overriding the canon.
- For an authorized graphic-generation task, read the source's reference-use permission. When already permitted, open and attach the actual approved reference images without requesting the same permission again. Preserve source assets, record derived outputs, and inspect the result against the canon. Exact logos, UI, and text use original assets or real typesetting. Production permission does not independently authorize publication or deployment.
- Keep rule authority separate from adoption: a document or review does not prove every Figma style, token consumer, or production surface has migrated. Apply explicit current decisions within their scope.

## Product judgment

For diagnosis and shaping, establish:

```text
Signal: observed friction
Facts: verified evidence
Assumptions: plausible but unverified
Open decisions: choices that can change the direction
Primary user: who, in what context
Primary outcome: one job for this surface
Success signal: observable behavior or measure
```

CS reports demonstrate friction, not its cause. Treat a suggested button, color, modal, or layout as a hypothesis unless the user explicitly fixes it as a constraint. Deadlines reduce investigation scope, not the need to distinguish evidence from solution.

Test interventions in order: better evidence or no change → existing behavior/default/permission correction → discoverability → copy or feedback → recomposition of existing components → new UI. Choose the smallest intervention that can produce the success signal.

```text
Because <evidence and causal hypothesis>, we will <intervention>,
so that <primary user outcome>.
This holds if <observable validation>; it fails if <falsifier>.
```

### References and Autonomous mode

Use supplied references and anti-references, identifying what to preserve or avoid. When an unknown preference would materially change a new direction, ask once and continue independent diagnosis while waiting. Do not make optional preference questions a prerequisite for an established component composition or narrow correction.

In Autonomous mode, perform focused reference research when category convention can change hierarchy, interaction, density, or language; record the direction and continue through critique, correction, and recapture. Use available Lazyweb screen/flow research tools or current web research; do not depend on obsolete skill names. Extract the specific pattern that changes a decision, rather than imitating an entire aesthetic. Skip research when it cannot affect a bounded conformance fix.

Autonomy removes intermediate approval pauses within authorized scope. Pause for genuinely required product facts, permissions, or an irreversible decision outside that scope; it does not expand production authorization.

## Interface quality

### Frame and hierarchy

Within one second, the intended user should understand the primary object, current state, and next action. Calibrate change scope (correction → recomposition → new pattern), density (scanning versus needed detail), and guidance (learned expert shorthand versus explicit labels and recovery cues).

Inventory information and actions; rank primary, secondary, metadata, and exceptions. Make hierarchy readable through type role, weight, proportion, alignment, and space. Escalate separation only as needed: layout/space → divider → background → elevation. Color and lines support hierarchy. Each element must expose state, enable action, reduce cognitive load, or create necessary structure.

### System and craft

- Use semantic tokens and existing primitives/composites. Propose a missing semantic role rather than choosing a nearby primitive by taste.
- Preserve Primitive → Composite → Screen ownership and inspect active consumers. Consider a shared component before duplicating screen-local markup.
- Avoid card-everything layouts, pill overuse, scattered actions, decorative gradients, oversized headings, and needless dashboard framing.
- Keep one alignment axis per region and related actions together. Keep metadata inline where scanning and narrow layouts permit it.
- Derive nested radii from the outer radius and inset. Optically align icons and labels. Give images and light surfaces adequate boundary contrast.
- Press feedback communicates state without layout jumps. Motion cannot compensate for weak hierarchy or unclear state.

### Whole state model

At layout time, cover applicable `default`, `hover`, `pressed`, `focus-visible`, `disabled`, `loading`, `empty`, `error`, `success`, and `overflow` states. Verify:

- narrow/wide layouts, content growth, and locale expansion;
- stable loading geometry, recoverable errors, and permission differences;
- keyboard order, visible focus, touch targets, contrast, and non-color cues;
- truncation, wrapping, long names, missing metadata, and realistic edge cases.

## Korean product UI

Use current semantic typography tokens. When no role-specific token defines these properties, use:

```css
.ko {
  word-break: keep-all;
  overflow-wrap: break-word;
  letter-spacing: 0;
  word-spacing: 0;
  line-height: 1.5;
}
```

Korean tracking is zero or negative, never positive for emphasis. A fallback of `-0.01em` to `-0.02em` may suit polished Korean text; multiline copy generally needs `1.5–1.65` line-height when the active token does not specify it. English-only heading tracking must not leak into Korean text.

Use the current Tiro glossary and UX-writing guidance for nouns, actions, formality, and English-across-locales exceptions. Keep labels distinct from placeholders. Do not concatenate translated sentence fragments or fix widths to English length. Verify KO/JA expansion, long titles, timestamps, badges, errors, and mixed Korean/Latin strings at narrow widths.

Inspect actual localized wrapping, isolated particles, awkward one-syllable last lines, and positive-tracking inheritance. Recheck hierarchy and density after replacing placeholders with real strings.

## Material alternatives and reports

Compare alternatives only when materially different information architecture, grouping, interaction, density/disclosure, action ownership, or guidance deserves a decision. Do not multiply candidates for color, radius, spacing, or decorative novelty. Finish a confirmed direction directly.

Follow an explicit workspace/user variant count; the current general design rule requests four finished candidates during exploration. Where no count is prescribed, 2–3 material alternatives are sufficient. Each uses the same realistic data, copy, permissions, edge cases, and equivalent viewports, with named decision axes and tradeoffs. Label uncertain product concepts as assumptions with validation conditions. Each candidate must independently pass the release gate.

Build an isolated HTML report when a visual comparison/report is useful or requested. A separate template file is not required. Derive semantic CSS variables from verified sources, not remembered or historical report values. Keep report chrome quieter than the UI: one compact header, a primary reading column, consistent alignment, actions grouped once, and navigation only for genuinely long reports. Avoid nested cards, competing sticky regions, and decorative controls.

Choose the report mode for the actual decision:

- **Decision Brief:** verdict (design, investigate, or solve without new UI), grounding, facts/assumptions/open decisions, primary outcome, smallest intervention, risks, falsifier, and next verification.
- **Comparison Lab:** decision and fixed constraints, shared fixtures, equivalent previews, axes/tradeoffs, per-candidate scorecards, comparison, and recommended next validation.
- **Final Review / Handoff:** confirmed outcome and constraints, grounding and token/component mapping, changed behavior/hierarchy, state/responsive/localization/accessibility matrix, scorecard, rendered verification, and remaining external checks.

When combining favored parts, identify the need each serves, verify a coherent hierarchy/interaction model, and state the synthesis rule and tradeoff. Keep one or two closest originals for comparison until confirmation. If favored properties conflict, expose the governing priority that needs a decision.

For “이게 아닌데,” distinguish rejection of direction, evidence, and report shape. If shape is the issue, name the other report modes and recommend one switch. Do not advertise all formats after a successful result.

## Motion, only when relevant

Use motion when it explains state, continuity, spatial change, or feedback, or when requested. For each transition, identify the trigger, the user question answered, minimum animated properties, and an equivalent reduced-motion transition. Omit purposeless motion.

Read current Tiro motion guidance and component source before choosing timing, easing, or properties. Prefer opacity, position, and subtle press feedback when the system permits. Avoid layout jank, attention loops, decorative bounce, blur, glow, particles, and parallax unless explicitly justified by the current product direction. Preserve interruption and rapid-repeat behavior. Honor `prefers-reduced-motion` or the platform equivalent. Verify loading, success, error, panel, overlay, and focus transitions together.

## Mixed landing + UI requests

On an Operate surface, `ui-design` leads. Preserve the recurring task, action hierarchy, content inventory, consent, inputs, states, and recovery. If the user explicitly pairs landing design, give it only a named bounded contribution such as a brand carrier or public handoff.

Before craft, record the surface/task, primary outcome, preserved content/states, each discipline's named decision, inspected sources/references, what each reference changed, rejected competing additions, attention ceiling, and evidence paths.

For the landing contribution, follow study → shape → direction → craft → release. Inspect 2–4 real category references for a new visual direction; reuse valid evidence and skip only a bounded conformance fix. Explain its necessity and set a measurable maximum area/pixel extent, permitted copy/contrast, and breakpoint removal condition. Verify the task still reads within one second, the carrier cannot be mistaken for the primary action, and capture the removal breakpoint at `-1px / +1px` with the wider-side measurement.

Remove contributions without an evidence-bearing or brand-bearing job. Reject promotional copy that delays an Operate task or repeats known context. Typography, imagery, color, or spacing alone does not prove both skills were applied: each claimed skill must inspect its sources, change a named decision within its scope, and provide release evidence.

## Release verification

Before presenting a candidate, define 4–6 screen-specific critical criteria with observable 10/10 targets. Include causal fit, task clarity, system fit, completion, and accessibility when relevant. Record each target, current score with evidence, and remaining correction.

Iterate until every critical criterion is at least 9/10; averages cannot hide a weak item. Apply stricter explicit project gates when relevant. Self-scoring is an internal quality check, not user-validation evidence. Inspect actual renders and relevant interactions, recapture after corrections, and report the checks performed and remaining external validation honestly. Do not claim an untested candidate passed.

Lead delivery with the judgment and next action, followed by the appropriate completed report or artifact.
