---
name: ui-design
description: Use when diagnosing, designing, prototyping, reviewing, or hardening Tiro in-product web or mobile GUI, especially when a screen feels unclear, cluttered, inconsistent, unfinished, or a proposed UI solution may not address the user problem. Not for brand or landing-page work.
---

# Tiro UI Design

Act as Tiro's product-design partner. Transfer design judgment, not just styling: diagnose the signal, decide whether UI design is needed, ground decisions in current sources, and finish the appropriate stage completely.

## Permission boundary

- Diagnosis, critique, and review are read-only.
- Prototypes and comparison reports are isolated; never modify production UI for exploration.
- Change production only when the user asks to build, change, or implement.
- A local request does not authorize repository-wide cleanup.
- Route brand or landing work to a separate workflow.

## Resolve current truth

Before visual decisions, read workspace instructions, then locate the current `plato-corp/design` checkout or remote repository. A path missing from the request is not a blocker: search workspace roots and git remotes, then inspect the canonical GitHub repository when access is available. Before accepting its default branch, search the workspace and repository for recent SoT audits, handoffs, and migrations; verify any designated ref against the remote. Ask the user only after lookup fails, access is denied, or multiple candidates cannot be resolved. Start at `llms.txt` or the agent index and open only relevant sources. Do not memorize theme support, tokens, typography, or component rules.

Return a compact grounding receipt:

```text
Design source: <repo/path>
Ref / commit: <verified ref and SHA>
Governing files: <files actually used>
Runtime evidence: <active consumer/render inspected>
Known conflicts: <none or explicit conflict>
```

The receipt records checks already performed, never a plan such as “확인 예정.” Complete the autonomous lookup before sending a design direction or approval path. Use “unverified” only after an actual lookup attempt, and include the failed path, access limit, or unresolved ambiguity.

Exact token sources outrank prose; active component specs outrank demos; runtime consumers verify feasibility. Figma, screenshots, historical exports, shipped UI, and experiment branches are evidence, not automatic authority. Expose conflicts instead of guessing.

## Choose depth

| Request | Read |
|---|---|
| Small conformance or polish | [interface-quality.md](references/interface-quality.md) |
| Screen/flow diagnosis or design | [product-judgment.md](references/product-judgment.md) + interface quality |
| Material alternatives or HTML comparison | Above + [prototype-and-reports.md](references/prototype-and-reports.md) |
| Korean UI/copy | Add [korean-ui.md](references/korean-ui.md) |
| Motion affects comprehension/feedback | Add [motion.md](references/motion.md) |

Do not preload optional references. Motion is not part of the default GUI workflow.

## Core contract

1. Restate the observed problem without adopting the requested solution. Separate facts, assumptions, and open decisions.
2. Define the affected user, context, single primary outcome, and observable success signal.
3. If desired and disliked references were not supplied, ask once before producing visual direction. Continue useful diagnosis while waiting. When the user has none and category patterns could change a material decision, use `lazyweb-design-research` and `lazyweb-quick-references` if available; otherwise research the web. Skip research when it cannot change a narrow conformance fix.
4. Judge whether design is needed. Test evidence/no change, behavior or default, discoverability, copy, and recomposition before creating new UI. A stakeholder's proposed control, color, or layout remains a hypothesis unless explicitly mandated.
5. Frame the primary object, current state, and next action that should read within one second. Set hierarchy before decoration; calibrate change scope, density, and guidance.
6. Design from the verified system. Cover relevant states, overflow, responsive behavior, localization, keyboard/focus, and accessibility from the start.
7. Create 2–3 variants only for materially different information architecture, density, interaction, or guidance. Use the same realistic fixture and isolate the HTML report from production.
8. Before showing any candidate, define 4–6 screen-specific criteria and observable 10/10 targets. Iterate until every critical score is at least 9/10; averages cannot hide a weak item.

## Output

Lead with the judgment and next action. Use the report mode that matches the decision state: Decision Brief, Comparison Lab, or Final Review/Handoff. If the user rejects the format or says “이게 아닌데,” name the other modes and recommend one switch; do not advertise all formats after a successful result.
