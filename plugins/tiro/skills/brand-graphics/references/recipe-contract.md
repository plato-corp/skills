# Recipe contract

Resolve this manifest before generating or composing the raw asset. Keep exact identifiers in the saved recipe so later channel adaptations can reproduce the decision.

Use the JSON plan below as the single pre-production record. Additional handoff notes may remain prose; do not fill a second ceremonial manifest.

## Field rules

- `route` selects the workflow. `solid-field` is a plain authorized brand-color plane and needs no imagegen or reference attachment. `brand-graphic` covers ambient atmosphere and brand-material structure; it needs no fictional evidence and no invented causal transition. `product-proof` leads with a verified product fragment or a real human moment.
- `recipe_family` must be one of the families listed for the chosen route in [recipes.json](../design-system/recipes.json). Any other id is invalid.
- `purpose` describes one intended viewer change; it is not a mood or asset type.
- `evidence_source` is a real path, URL, verified description, or `none`. Do not write a plausible substitute. Solid-field and ambient brand-graphic families set this to `none` legitimately; they must not invent evidence to look proven.
- `representation` states what may change: faithful crop, material abstraction, product framing, generated conversation moment, or flat brand plane.
- `brand_motif_layer` is `none` or an exact approved vector plus its message role. Keep it separate from generated raster art.
- `focal_event` is one visible event, not a list of objects. Ambient fields may present one calm dominant field rather than an event, and need no causal transition.
- The current authorized flat/other style overrides historical material-depth treatment. Do not reapply poised material depth when the current guide is flat.
- `release_zone` is a bounded quiet region reserved for later copy or channel metadata.
- `target_crops` are authored compositions. Never promise that one finished poster can simply be stretched into every ratio.
- `must_not` records artifact-specific risks. Do not replace this with a universal aesthetic blacklist.
- `seed_note` records enough of the selected generative direction to reproduce the material treatment; it does not need to expose hidden model reasoning.

## Plan file (persist before production)

Before any generation or non-generation reuse, persist a compact JSON plan next to the work (default `plan.json`). It is the single record the validator checks against. Required shape:

```json
{
  "plan_version": 1,
  "source": {"source": "<registry/handoff id>", "ref": "<ref/commit>"},
  "route": "solid-field | brand-graphic | product-proof",
  "recipe_family": "<family id valid for route>",
  "references": [
    {
      "path": "<reference image path within this work>",
      "decision": "preserve | change | free",
      "role": "<what this reference contributes>"
    }
  ],
  "purpose": "<intended viewer change>",
  "evidence_source": "none",
  "composition": {
    "width": 1200,
    "height": 630,
    "copy_zones": [{"name": "<id>", "x": 0, "y": 0, "w": 200, "h": 100}],
    "logo_zones": [{"name": "<id>", "x": 0, "y": 0, "w": 200, "h": 100}]
  },
  "palette": {
    "roles": {"<role>": "<value or token name>"},
    "exclusions": ["<disallowed color/role>"]
  }
}
```

Rules:

- `route` and `recipe_family` must be consistent with [recipes.json](../design-system/recipes.json).
- `solid-field` needs no `references` (an empty list is valid) and never needs an imagegen call or reference attachment.
- `product-proof` families require at least one reference and a real (non-`none`) evidence source.
- Ambient `brand-graphic` families require no fictional evidence and no causal-transition claim.
- Each reference trait carries an explicit `preserve` / `change` / `free` decision: `role` names the concrete trait and, for change, the intended replacement. Repeat the same image path in separate entries to preserve one trait, change another, and free the layout. At least one preserved trait should identify what makes the approved graphic language recognizable; do not reduce a structural reference to texture-only without an explicit user decision. Copy these decisions into the generation prompt and compare them in review. Non-generation reuse still lists the exact source artifact it reuses.
- `palette.exclusions` records colors or roles the composition must not use.

## Retry boundary

Retry once with one targeted correction when the subject, crop, or focal event is wrong. If the second render still fails a critical gate, stop and return the manifest plus failure receipt instead of presenting it as finished.

## Execution and review records

Save the actual tool arguments without renaming fields. For imagegen use its native `referenced_image_paths`; relative plan paths and absolute tool paths are resolved to the same files. Private prompts and references stay in the authorized project, never the public plugin.

`execution.json` has `receipt_sha256` (SHA256 of the receipt file), `method` (`generation`, `direct`, `reuse`), and nonempty `outputs` (file paths). Generation adds `tool_args_path`; direct composition adds editable `source_artifact`; reuse adds `reuse: {"source_artifact": "source.png"}`. Direct/reuse work does not require an imagegen call. Authorized design source/ref remain mandatory even when functional evidence is `none`.

`review.json` has `criteria`, a list of `{ "name": "hierarchy", "disposition": "pass", "evidence": "observable finding and actual file/size" }`. Required names are `hierarchy`, `craft`, and each planned preserved/changed trait as `<decision>:<role>`. Free traits do not create required checks. Record reference and output filenames, master/thumbnail inspection and concrete discrepancies in evidence. No numeric score substitutes for an observation. See visual-review.md.
