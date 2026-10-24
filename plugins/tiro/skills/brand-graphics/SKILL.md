---
name: brand-graphics
description: Create or reuse Tiro brand graphics and product-evidence compositions. Includes a standalone stepped-waveform reference; use for reusable marketing assets, not product UI implementation or whole landing pages.
---

# Tiro Brand Graphics

Keep product evidence, brand graphics, and channel composition separate. Use exact product captures and logos; never ask a generated image to redraw them. Compose final copy and channel layouts as separate editable layers.

## Finished content defaults

For final marketing images, read [marketing-composition.md](references/marketing-composition.md): all three color themes, current semantic-token sourcing, title-aligned or omitted logo, shared title calibration and default waveform background. Raw references remain separate from final composition.

## Product evidence

When product UI appears, use a newly verified capture of the latest production surface. Record its URL, capture time/timezone, platform, theme, available build/deploy identifier, and the design-system ref consulted. Check for relevant UI changes before reusing older captures; mark freshness unverified when production cannot be checked. A prototype or old HTML is not current-production evidence.

Consult the current authorized design-system contract, but preserve actual production pixels if they disagree: record the mismatch instead of recoloring or rebuilding the capture to match tokens. Keep brand graphics outside the product layer.

When a live production surface could expose user-identifying or customer content, capture a relevant privacy-safe fragment rather than editing text or the DOM to hide identity. A faithful crop of a safe region preserves product truth; blanking or rewriting pixels does not. Keep the original captured fragment read-only and disclose its crop; avoid collecting or retaining a sensitive full-screen capture when a safe fragment is sufficient.

## Intake — ask once before producing

Before producing anything, confirm the few facts that change the subject, evidence, or format. Ask them **once, grouped and concise** — not as a full checklist, and never re-ask anything the request already supplied. Present the choices you actually observed in the request; do not invent options. Group the ask into:

- **Destination / placement** — where this will appear (channel and placement). This decides whether the task is a raw graphic only, or an actual email/popup/surface implementation. Do not silently treat one request as two final channels.
- **Dimensions** — W×H or aspect ratio. If the destination is given but the dimensions are not, propose dimensions clearly marked as assumptions and get confirmation before the final export; do not state an assumed size as an established spec.
- **File / motion format** — only the formats relevant to the destination: PNG / JPG / SVG / HTML for static or editable; MP4 (with duration, fps, and audio) for motion. Ask motion fields only when motion is actually in scope.
- **Quantity and language** — how many assets and which language(s).

If a fact is already supplied, carry it forward silently. If the chosen channel is unknown, propose dimensions as explicit assumptions and confirm before finalizing. Treat any size, ratio, or format that is not independently verified as a proposal, not an existing production spec.

See [references/online-formats.md](references/online-formats.md) for the generic capability map: which online formats this skill can produce directly, which need an actual implementation surface, and how static, editable, and runtime outputs differ.

## Paired product-present and product-free versions

For finished marketing compositions, by default deliver **two versions of the same message in the same chosen format**: one that includes the product surface, and one brand-only version with no product UI. This is the default flow, not an add-on.

- **Explicit single-version override.** The requester may explicitly ask for only one version (product-present only, or brand-only only). Honor that; do not silently produce the pair.
- **No valid, latest production access = no fake product version.** If there is no verified latest-production capture or access, do not fabricate product UI and do not substitute an old prototype, mockup, or HTML as if it were current. In that case, deliver the brand-only version honestly, and report the product-present counterpart as blocked pending a real capture. Ask for the capture or the access required. A placeholder is never an acceptable final product version.
- **Brand-only is a recomposition, not the product version minus a screenshot.** Do not simply delete the screenshot and leave the hole. Recompose a purposeful graphic or title treatment so the brand-only version stands on its own composition.

Raw waveform references, source-only components, and research documents are not finished marketing compositions and do not require product variants.

Both versions share the confirmed message, format, dimensions, and language from intake. Record which version is product-present and which is brand-only, and the evidence/provenance for the product-present one.

## Brand direction and reference

Finished marketing content defaults to a waveform background under the composition guide; plain fields remain valid for raw layers and explicit waveform-free briefs. Other geometric/pattern styles are optional. Preserve older assets as references.

The current waveform working reference is **60 horizontal lines, medium weight, slow flow**. The2026-10-25 update makes waveform the finished-marketing background default; the exact preset remains a review baseline, not final brand approval or evidence of production adoption. Thin and thick profiles remain comparison alternatives.

- [Open the graphic-only reference](references/waveform-medium-60-horizontal/index.html).
- [Usage and settings](references/waveform-medium-60-horizontal/README.md).
- [Source and extraction provenance](references/waveform-medium-60-horizontal/provenance.json).

The reference contains a pen-nib shape expressed as numeric carrier geometry. It excludes the product simulation, authentication/onboarding UI, logos, fonts, customer content, and internal URLs. It is a brand graphic and does not prove product behavior. Exact weights, density, and slow-flow values for this review snapshot are recorded in its provenance; do not invent a separate preset.

For motion-capable surfaces, preserve the reference's slow drift; provide pause and a deterministic static frame for reduced motion. Suspend animation when hidden. Static exports should use a readable stable frame. Motion is decorative, not recording status or measured audio.

## Context-object waveform generation

For conversation, recording, and organization objects rendered with the original HTML waveform treatment, use [the context-object workflow](references/waveform-context-workflow.md). It covers meaningful object selection, 3D source prompts, native-renderer preservation, new input data, and full-size/thumbnail review. [Open the four-object animated reference](references/waveform-context-20261021/review.html) or [compare the contact sheet](references/waveform-context-20261021/contactsheet/contact-2x2-dark.png). This is a liked generation direction and review reference, not global brand adoption or production evidence. The bundled fields replay these four objects; new source conversion requires the separately documented build tools.

## Selecting the image before waveform conversion

Choose a subject whose silhouette and broad light/shadow masses remain recognizable at the intended output size and 60-line density. A clear isolated object with readable volume works better than flat texture or fine detail. Prefer uncluttered backgrounds and enough quiet space around text. Avoid lettering, UI, intricate grids, and dominant transparent reflections in the source. Verify grayscale, small-size, and stepped-tone previews before accepting it. Use authorized source assets and retain their provenance.

The supplied carrier set covers one object only. It does not implement arbitrary image conversion; source sampling needs its own verification when a new object is introduced.

## Validation

Run `node references/waveform-medium-60-horizontal/identity.test.cjs` for deterministic static output, active flow, profiles, and carrier count. An optional local source argument compares extracted geometry results against the original review implementation. This does not establish production adoption or independently prove the carrier preprocessing is identical.

Inspect light/dark output, full size and thumbnail, legibility, line density, and motion. Before public distribution verify the package contains no product/customer data, credentials, private links, or external runtime requests. Match source hashes in the provenance.

Authorized teams may consult their current ontology/design contracts for newer approved decisions. Do not expose private contract contents or require private access to use this public standalone reference.

For compact chat assets, inspect both the final full-size PNG and a 320px-wide chat preview. Fix clipped or shifted exports caused by artwork overflowing a fixed artboard. Use explicit semantic line breaks in Korean headlines when needed; prevent a final syllable or short ending from becoming an orphan line. Check rendered headline/subtitle bounds against the product fragment, and use the exact navigation labels observed in production for any setup instructions.
