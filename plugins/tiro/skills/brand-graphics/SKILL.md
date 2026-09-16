---
name: brand-graphics
description: Use when Tiro external marketing work needs a reusable channel-agnostic photo, product-proof treatment, or graphic asset before copy, logo, and channel-specific layout are composed. For final OG images or covers, continue through the channel-composition handoff. Not for product GUI or whole landing pages.
---

# Tiro Brand Graphics

Create the visual evidence or brand layer that `marketing-visuals` can adapt across channels. A brand graphic is not a finished poster: it contains no final copy, logo lockup, CTA, factual label, or channel chrome.

## Current Tiro design contracts

Before changing Tiro color, logos, title typography, or brand graphics, discover the authorized design and ontology sources from the current workspace instructions, configured source registry, or verified project handoff. Read the affected contracts before making visual decisions. Keep private repository identities, document paths, review identifiers, values, and reference images in that authorized environment; do not embed them in this public skill.

Read the color usage and logo-mode contracts for color/logo work, the Korean/English/Japanese title-font contract for title work, and the approved graphic-style guide, implementation rules, and reference-asset manifest for graphic work. Follow the source registry's links rather than guessing filenames. Record the actual source, ref, commit, and governing files in the project's authorized record. Verify any designated review branch's state and SHA; a closed unmerged review is not adoption evidence. If lookup fails, preserve existing work and report the missing contract rather than inventing values.

- Tiro title fonts require the documented optical calibration in every environment. Mixed Latin and standalone English use their respective roles; body, controls, and wordmarks retain their separate contracts. Verify actual fonts and rendered calibration, not only font-family declarations.
- Use the current approved reference style. The current authorized flat or other style overrides historical material-depth treatment. Do not reopen style exploration or reapply historical constraints that conflict with the current decision. Layout research informs composition without overriding the canon.
- For an authorized graphic-generation task, read the source's reference-use permission. When already permitted, open and attach the actual approved reference images without requesting the same permission again. Preserve source assets, record derived outputs, and inspect the result against the canon. Exact logos, UI, and text use original assets or real typesetting. Production permission does not independently authorize publication or deployment.
- Keep rule authority separate from adoption: a document or review does not prove every Figma style, token consumer, or production surface has migrated. Apply explicit current decisions within their scope.

## Three routes

Pick one route first; it decides whether imagery, evidence, and references are even needed.

- **solid-field** — a plain authorized brand-color plane. It carries the message through exact logo, title typography, and whitespace. No imagegen, no reference attachment, no invented evidence. Valid families: `solid-brand-field`.
- **brand-graphic** — ambient atmosphere or brand-material structure supporting mood or identity. Needs no fictional evidence and no causal transition. An ambient field may be one calm dominant field rather than an event. Valid families: `ambient-atmosphere`, `brand-material-structure`.
- **product-proof** — a verified product fragment or real human moment leads and supports a verified claim; generated illustrative scenes never prove actual use. Requires a real evidence source and at least one reference. Valid families: `product-proof-field`, `conversation-moment`, `record-compression`.

Family/route validity is defined in [recipes.json](design-system/recipes.json). Do not invent a family or use one outside its route.

## Required input

Accept a compact upstream brief:

```text
Purpose: <intended viewer change>
One-second message: <one sentence>
Route: <solid-field / brand-graphic / product-proof>
Evidence: <verified product fragment / supplied photo / conversation moment / brand-origin structure / none>
Asset role: <hero / proof field / atmosphere / connector>
Target crops: <ratios and protected zones>
Must preserve: <source identity or product truth>
Must avoid: <artifact-specific failures>
```

If called directly, derive these fields from the request. Ask only when a missing fact would materially change the subject or evidence.

Latest explicit decisions in the authorized guide override conflicting traits visible in older reference images. Before generation, resolve palette direction, flat versus dimensional treatment, and permitted form variation from that guide. The current authorized flat/other style overrides historical material depth. Do not turn a reference image or recipe into a closed shape vocabulary. Keep historical examples separate from current production requirements.

## Persist a plan before production

Before any generation or non-generation reuse, persist a compact JSON plan (`plan.json`) recording: source/ref, route and a valid recipe family, each reference image path with a `preserve` / `change` / `free` decision, purpose, composition dimensions with proposed copy/logo zones, and palette roles with exclusions. The exact shape and rules are in [recipe-contract.md](references/recipe-contract.md).

Then run the validator's `prepare` step to snapshot the plan and existing references into a new receipt:

```sh
python3 tools/validate_plan.py prepare --plan plan.json --receipt receipt.json
```

`prepare` validates the plan against the routes/families, confirms every named reference file exists, and writes an immutable-by-convention SHA256 receipt. It refuses to overwrite an existing receipt.

## Workflow — when imagery is needed (brand-graphic / product-proof)

1. Read [recipe-contract.md](references/recipe-contract.md) and resolve every manifest field. Persist the plan and run `prepare`.
2. The plan must already select one recipe family valid for the route from [recipes.json](design-system/recipes.json). For product-proof the family follows the evidence. For ambient brand-graphic, no evidence or causal transition is required.
3. Read [graphic-language.md](references/graphic-language.md). For event-bearing routes define one focal event and one quieter release zone; for ambient/solid define one calm dominant field and a reserved release zone. Every dominant form needs a message, evidence-support, structural, or brand-material role — except ambient fields, which assert no transition.
4. Honor an explicit requested candidate count. Otherwise produce one master asset by default. Use 2–3 only when the unresolved choice changes the subject, evidence anatomy, or focal event — not merely color or crop.
5. Choose generation, direct composition, or reuse as appropriate. When generating, attach the actual planned reference images to the generation tool. Save the tool argument JSON so its native reference-path field (imagegen: `referenced_image_paths`) matches the planned reference paths. Keep generated raster art free of letters, numbers, logos, UI labels, seals, metrics, and watermarks. An approved exact vector motif such as [tiro-nib-motif.svg](assets/tiro-nib-motif.svg) may be supplied as a separate editable brand layer when the manifest names its semantic role; never ask an image model to imitate it. Preserve supplied people, products, and current UI truth. Never invent a substitute proof.
6. Record execution: an `execution.json` linking `receipt_sha256` to the receipt, the `tool_args_path`, and the `outputs`. Declare `method` as `generation`, `direct`, or `reuse`; direct composition names its editable `source_artifact`, and reuse names `reuse.source_artifact`. Reuse and direct composition need no generation-tool arguments.
7. Run the visual review (below) and record it as `review.json`, then run `check`.

## Solid-field path

When the current authorized brand guide permits a plain brand-color field, that field is a complete valid asset; the channel composition relies on exact logo, title typography, and whitespace. Do not add texture, geometry, halftone, connectors, or invented evidence to fill the frame or pass a genericity test.

Implement the field directly in CSS or vector using the governing background/foreground contract. Image generation and reference attachment are unnecessary; the plan's `references` list may be empty. Still persist the plan and run `prepare`/`check`; the execution record uses `method: direct`, names the editable `source_artifact`, and needs no `tool_args_path`. Judge the final channel composition by hierarchy, contrast, correct brand assets/type, whitespace, and crop fitness; absence of decorative objects is not a failure. Final typography remains the channel composer's responsibility.

## Visual review and validation gate

Compare the actual reference image(s) and the actual saved output side by side, at master size and at thumbnail, following [visual-review.md](references/visual-review.md). Record every required criterion with a disposition — `pass`, `fix`, or `unverified` — and concrete evidence, against the plan's preserved/changed traits plus hierarchy and craft. There is no numeric approval floor. `fix` and `unverified` block release; a raw graphic with any unresolved criterion is not finished.

Run the check:

```sh
python3 tools/validate_plan.py check --plan plan.json --receipt receipt.json \
  --execution execution.json --review review.json
```

`check` verifies structural records only: the plan and references are unchanged since the receipt, the execution record links to the receipt hash, the actual saved generation-tool argument JSON uses the planned reference paths, declared outputs exist, and every review criterion passes with evidence. It **cannot** prove the generation tool truly ran, cannot prove authorship order, and does not judge artistic quality. Receipt timestamps and SHA snapshots are integrity records, **not** cryptographic proof that planning preceded generation.

## Handoff contract

```text
Route: <solid-field / brand-graphic / product-proof>
Asset: <path>
Brand motif layer: <none or exact vector path and role>
Recipe: <family id + path or inline manifest>
Plan / receipt: <plan.json / receipt.json>
Focal event: <observable event, or calm dominant field for ambient/solid>
Release zone: <location and usable bounds>
Crop tolerance: <per ratio>
Evidence preserved: <what remains true, or "none — ambient/solid">
Review: <every criterion pass, with evidence>
Known limits: <what the channel adapter must not assume>
Proposed typography/logo placement: <copy and logo zones, before generation>
```

Hand off the proposed typography and logo placement **before** generation so the channel composer can plan; the raw graphic never carries final type.

## Final OG image / poster / channel composition

A raw brand graphic is not a final deliverable. To produce a final OG image, poster, or channel-specific composition:

- If `marketing-visuals` is installed, forward the handoff contract and the selected asset to it and let it own channel chrome, exact copy, logo lockup, and per-ratio layout.
- If `marketing-visuals` is not installed, compose the channel deliverable here with this explicit procedure, naming exact assets and types:
  1. Choose the channel and its exact output (e.g. OG image PNG 1200×630; poster PDF/PNG at named print size; social PNG at the channel ratio).
  2. Place the brand graphic or solid field as the background layer within the plan's protected content zone and release zone.
  3. Typeset final copy with the real title-font contract and calibration; do not rasterize placeholder text into the graphic.
  4. Add the exact logo lockup (vector) in the reserved logo zone; never use a generated logo-like mark.
  5. Verify contrast, safe margins, and per-ratio crops against the target crops; export the named file type.
  6. Record the final composition as a separate output from the raw graphic.

A revised plan gets a new receipt before the next production attempt; preserve old attempts. Never backfill a preflight claim. Judge the complete channel composition again using the same reference comparisons, actual font loading, hierarchy and crop checks; raw-asset approval does not approve the composed output.
