---
name: brand-graphics
description: Use when Tiro external marketing work needs a reusable channel-agnostic photo, product-proof treatment, or graphic asset before copy, logo, and channel-specific layout are composed. Not for final YouTube thumbnails, Instagram posts, blog covers, landing pages, or product GUI.
---

# Tiro Brand Graphics

Create the visual evidence layer that `marketing-visuals` can adapt across channels. A brand graphic is not a finished poster: it contains no final copy, logo lockup, CTA, factual label, or channel chrome.

## Current Tiro design contracts

Before changing Tiro color, logos, title typography, or brand graphics, discover the authorized design and ontology sources from the current workspace instructions, configured source registry, or verified project handoff. Read the affected contracts before making visual decisions. Keep private repository identities, document paths, review identifiers, values, and reference images in that authorized environment; do not embed them in this public skill.

Read the color usage and logo-mode contracts for color/logo work, the Korean/English/Japanese title-font contract for title work, and the approved graphic-style guide, implementation rules, and reference-asset manifest for graphic work. Follow the source registry's links rather than guessing filenames. Record the actual source, ref, commit, and governing files in the project's authorized record. Verify any designated review branch's state and SHA; a closed unmerged review is not adoption evidence. If lookup fails, preserve existing work and report the missing contract rather than inventing values.

- Tiro title fonts require the documented optical calibration in every environment. Mixed Latin and standalone English use their respective roles; body, controls, and wordmarks retain their separate contracts. Verify actual fonts and rendered calibration, not only font-family declarations.
- Use the current approved reference style. Do not reopen style exploration or reapply historical constraints that conflict with the current decision. Layout research informs composition without overriding the canon.
- For an authorized graphic-generation task, read the source's reference-use permission. When already permitted, open and attach the actual approved reference images without requesting the same permission again. Preserve source assets, record derived outputs, and inspect the result against the canon. Exact logos, UI, and text use original assets or real typesetting. Production permission does not independently authorize publication or deployment.
- Keep rule authority separate from adoption: a document or review does not prove every Figma style, token consumer, or production surface has migrated. Apply explicit current decisions within their scope.

## Required input

Accept a compact upstream brief:

```text
Purpose: <intended viewer change>
One-second message: <one sentence>
Evidence: <verified product fragment / supplied photo / conversation moment / brand-origin structure / none>
Asset role: <hero / proof field / atmosphere / connector>
Target crops: <ratios and protected zones>
Must preserve: <source identity or product truth>
Must avoid: <artifact-specific failures>
```

If called directly, derive these fields from the request. Ask only when a missing fact would materially change the subject or evidence.

## Solid-field path

Before selecting a recipe, check whether the current authorized brand guide permits a plain brand-color field. When it does, that field is a complete valid asset; the channel composition can rely on exact logo, title typography, and whitespace. Do not add texture, geometry, halftone, connectors, or invented evidence just to fill the frame or pass a genericity test.

For this path, implement the field directly in CSS or vector using the governing background/foreground contract. Image generation and reference-image attachment are unnecessary. Record purpose, source, palette roles, protected content zone, and target crop in the handoff; mark imagery-only fields (evidence family, material event, generation seed) as not applicable with a reason. Skip the imagery workflow below. Judge the final channel composition by hierarchy, contrast, correct brand assets/type, whitespace, and crop fitness; absence of decorative objects is not a failure. Final typography remains the channel composer's responsibility.

## Workflow — when imagery is needed

1. Read [recipe-contract.md](references/recipe-contract.md) and resolve every manifest field before making imagery.
2. Select one evidence family from [recipes.json](design-system/recipes.json). The family follows the evidence; it is not a style menu.
3. Read [graphic-language.md](references/graphic-language.md). Define one focal event and one quieter release zone. Every dominant form needs a message, evidence-support, structural, or brand-material role.
4. Produce one master asset by default. Use 2–3 only when the unresolved choice changes the subject, evidence anatomy, or focal event—not merely color or crop.
5. Keep generated raster art free of letters, numbers, logos, UI labels, seals, metrics, and watermarks. An approved exact vector motif such as [tiro-nib-motif.svg](assets/tiro-nib-motif.svg) may be supplied as a separate editable brand layer when the manifest names its semantic role; never ask an image model to imitate it. Preserve supplied people, products, and current UI truth. Never invent a substitute proof.
6. Inspect the rendered asset at master size and all target crops. Reject it when it becomes generic SaaS decoration after removing the Tiro brief, lacks a thumbnail focal event, or cannot leave usable space for the channel composition.
7. Return the selected asset, manifest, crop guidance, and a short quality receipt. Do not add final typography or publish it.

## Handoff contract

```text
Asset: <path>
Brand motif layer: <none or exact vector path and role>
Recipe: <path or inline manifest>
Focal event: <observable event>
Release zone: <location and usable bounds>
Crop tolerance: <per ratio>
Evidence preserved: <what remains true>
Known limits: <what the channel adapter must not assume>
Scores: purpose causality / evidence support / Tiro specificity / crop fitness / craft
```

All five critical scores must be at least 9.0. Averages do not compensate.
