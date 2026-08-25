# Product judgment

Use this reference for diagnosis, shaping, new screens/flows, ambiguous requests, and any request that arrives with a prescribed UI solution.

## Orient before drawing

Produce a compact decision frame:

```text
Signal: what was observed
Facts: verified evidence only
Assumptions: plausible but unverified
Open decisions: choices that can change the direction
Primary user: who, in what context
Primary outcome: one job for this surface
Success signal: observable behavior or measure
```

CS reports prove that friction exists; they do not prove its cause. A stakeholder's button, color, modal, or layout request is one hypothesis. Deadlines reduce investigation scope, not the need to distinguish evidence from solution.

## Reference gate

Before producing a visual direction, ask once:

> 원하는 레퍼런스와 “이건 싫다”는 안티레퍼런스가 있나요? 없다면 제가 제품 카테고리 관행을 짧게 조사해 방향 가설을 잡겠습니다.

Do not ask again when references were already supplied. Inspect what the user wants preserved or avoided; ask a follow-up only when that intent is materially ambiguous.

If they have none:

- Research when category convention affects hierarchy, interaction, density, or expected language.
- Prefer `lazyweb-design-research` for category patterns and `lazyweb-quick-references` for concrete examples when those skills exist; otherwise use current web research.
- Record which pattern informed which decision. Do not imitate an entire product aesthetic.
- Skip research for a local token correction or established component composition where external examples cannot change the answer.

## Resolve authority

Use this order while preserving explicit repository instructions:

1. User goal, constraints, and permission scope.
2. Verified user/product evidence and current runtime behavior.
3. A verified current ref of `plato-corp/design`, beginning at its agent index.
4. Accepted Tiro decisions and active component specifications.
5. Adjacent shipped patterns, only after confirming they are still active.
6. External references and general heuristics.

For values, machine-readable tokens win. For behavior, active component specs win. For feasibility, active consumers matter. If an audit/handoff designates a non-default ref as SoT, verify its remote SHA and record it. If sources conflict, list the conflict and identify the decision owner; do not silently normalize.

The default branch is not proof of the current SoT. Before accepting it, search the workspace and design repository for recent files containing `SoT`, `source of truth`, `audit`, `handoff`, or `migration`; compare their dates and verify any named remote ref/commit. A newer explicit designation outranks an older default-branch summary, while its exact token files still govern values within that ref.

Do not turn “the requester did not include the repository path” into a user dependency. Search the workspace, inspect git remotes, and use the canonical `plato-corp/design` repository when reachable. Request help only when autonomous lookup fails, access is denied, or verified sources remain ambiguous.

A grounding receipt is completed evidence, not a to-do list. Do not write “확인 예정” or “미확인” merely because the diagnostic window has just started. Perform the lookup before sending the brief; when verification truly fails, name what was attempted and why it failed.

## Decide whether UI design is needed

Test interventions in order:

1. Better evidence or no change.
2. Existing behavior/default/permission correction.
3. Discoverability correction in an existing flow.
4. UX copy or feedback.
5. Recomposition of existing primitives/components.
6. New or materially changed UI.

Select the smallest intervention that can produce the success signal. If UI is justified, state the hypothesis and validation condition:

```text
Because <evidence and causal hypothesis>,
we will <coherent intervention>,
so that <primary user outcome>.
This holds if <observable validation>; it fails if <falsifier>.
```

## Decision Brief contract

Use this report when the cause is uncertain or multiple forms of intervention remain possible:

1. Verdict: design now, investigate first, or solve without new UI.
2. Grounding receipt.
3. Facts / assumptions / open decisions.
4. Primary outcome and success signal.
5. Recommended smallest intervention.
6. Risks, falsifier, and next verification.

Do not produce variants until there are at least two material decision axes worth comparing.

## Pressure traps

| Pressure | Correct response |
|---|---|
| “The PM already chose it” | Treat it as a hypothesis unless the user explicitly makes it a fixed constraint. |
| “Release closes in two hours” | Time-box evidence gathering and choose a reversible step; do not turn uncertainty into certainty. |
| “Six users complained” | Confirm the signal, then investigate the causal step and completion behavior. |
| “The current UI already does this” | Shipped behavior is evidence, not proof that it is usable or system-correct. |
| “Just make it more prominent” | Define the object, state, action, and success signal before choosing prominence. |
| “The repository path was not included” | Locate the known canonical repository yourself before asking the user to supply it. |
