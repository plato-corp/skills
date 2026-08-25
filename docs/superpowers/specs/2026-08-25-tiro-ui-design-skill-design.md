# Tiro UI Design Skill — Design Specification

Date: 2026-08-25  
Status: review required before implementation  
Target repository: `plato-corp/skills`

## 1. Goal

Create one thin, adaptive product-design partner for Tiro's in-product GUI. A teammate should be able to invoke it once and experience the same decision sequence Hazel uses: understand the reported problem, decide whether UI design is actually required, ground the work in current evidence and the Tiro design system, explore materially different directions when useful, synthesize feedback, and finish only work that clears an explicit quality bar.

The skill optimizes for:

- product GUI UI/UX, not brand or landing-page art direction;
- repeatable judgment, not only visual polish;
- current `plato-corp/design` evidence, not memorized token values;
- one invocation with adaptive depth and selective reference loading;
- isolated HTML comparison reports when alternatives would improve the decision;
- a per-screen quality gate where every critical criterion scores at least 9/10.

## 2. Non-goals

- Brand and landing-page work. That will be a separate future `/tiro:landing-design` skill.
- Running motion exploration by default. Motion is an optional sidecar used only when it improves state comprehension, continuity, or feedback.
- Automatically redesigning every problem presented as a design request.
- Treating Figma, historical exports, screenshots, or shipped UI as authoritative without verifying their status.
- Requiring one fixed report format for every request.

## 3. Public invocation and package changes

The skill's display name is **Tiro UI Design**. Its installed command will be:

```text
/tiro:ui-design
```

The repository already installs every skill under the `tiro:*` namespace. Naming the folder `tiro-ui-design` would produce the redundant `/tiro:tiro-ui-design`, so the folder and frontmatter name will be `ui-design`.

The implementation will also:

- add the skill to the README skill table;
- broaden the marketplace and plugin descriptions/keywords beyond the current LLM Wiki-only wording;
- bump the plugin and marketplace version from `0.1.0` to `0.2.0` as a new capability, keeping both manifests synchronized.

## 4. Referenced structures

The skill reuses proven structures without copying another creator's visual taste wholesale:

- **UI/UX Pro Max:** establish product category, audience, and system constraints before styling.
- **Anthropic frontend design guidance:** make visual choices intentional and reject generic AI-SaaS composition.
- **Emil Kowalski skills:** keep prototypes isolated from production, make alternatives genuinely different, and treat motion as purposeful craft rather than decoration.
- **gstack:** score multiple dimensions, define the 10/10 target, and state how a candidate reaches it.
- **Taste Skill:** run an explicit anti-slop pass over layout, typography, interaction, and motion.
- **better-ui:** inspect final-detail failures such as nested radii, optical icon alignment, outlines, press feedback, and transition properties.
- **Vercel product-design skill:** use one thin entry point, progressive reference loading, evidence-backed rules, and repeatable evaluations.
- **Design Lab-style exploration:** compare alternatives with the same fixture data, then synthesize feedback instead of selecting by visual novelty.

Motion-specific material remains optional because the default workload is product GUI UI/UX.

## 5. Architecture

```text
plugins/tiro/skills/ui-design/
├── SKILL.md
├── references/
│   ├── product-judgment.md
│   ├── interface-quality.md
│   ├── prototype-and-reports.md
│   ├── korean-ui.md
│   └── motion.md
└── assets/
    └── report-shell.html

evals/ui-design/
├── cases.md
└── rubric.md
```

`SKILL.md` is a router and shared contract, not a full design handbook. It contains the source-resolution rule, request classification, compact core workflow, permission boundaries, routing table, and completion gate. The agent reads only the references required for the current request.

Reference responsibilities:

- `product-judgment.md`: evidence, reference gate, design-needed gate, primary user goal, causal diagnosis, decision logic, source authority.
- `interface-quality.md`: hierarchy, density, component/state/responsive design, anti-slop checks, design-system use, accessibility, and the numerical quality gate.
- `prototype-and-reports.md`: when to create 2–3 variants, shared-fixture comparison, feedback synthesis, and the three report modes.
- `korean-ui.md`: Korean wrapping, tracking, line-height, localization expansion, and mixed-language safeguards.
- `motion.md`: optional purpose test, restrained motion, reduced-motion handling, and the requirement to use the live Tiro motion guidance instead of memorized timings.
- `report-shell.html`: a restrained semantic HTML shell shared by the report modes. Exact visual tokens are populated from the verified design-system source at run time rather than hardcoded as permanent truth.

## 6. Adaptive depth and token budget

The skill chooses the shallowest depth that can make the decision safely.

| Depth | Typical request | References loaded |
|---|---|---|
| Fast | token conformance, one component, a small polish request | interface quality; Korean UI only if applicable |
| Standard | a screen or flow with a fairly clear problem | product judgment + interface quality |
| Explore | materially different information architecture, density, or interaction models | product judgment + interface quality + prototype/reports |
| Finish | confirmed direction, implementation hardening, handoff | interface quality + relevant implementation guidance |
| Motion sidecar | transition or feedback is essential to comprehension | motion in addition to the active depth |

Targets:

- `SKILL.md` stays at or below roughly 700 words.
- Default work loads no more than two reference files.
- Exploration normally loads three references; motion is never preloaded.
- Design-system reading is path-specific: start from its agent index and open only the relevant tokens, components, foundations, or guidelines.

These are routing constraints, not reasons to omit evidence that materially changes the decision.

## 7. Source resolution and design-system grounding

Before making visual decisions, the skill records a short **grounding receipt**:

```text
Design source: <repository or local checkout>
Ref / commit: <verified ref and SHA, when available>
Governing files: <only the files used>
Runtime evidence: <target product files or rendered surface inspected>
Known conflicts: <none, or explicit conflict>
```

Resolution order:

1. Read the target workspace's `AGENTS.md` or equivalent governing instructions.
2. Locate the current Tiro design-system checkout or inspect `plato-corp/design`.
3. Start with that repository's `llms.txt` or agent index and load only relevant files.
4. If an audit or handoff explicitly designates a ref as current SoT, verify that remote ref and record its commit before using it.
5. For exact values, machine-readable token sources outrank prose and examples. For component behavior, active component specifications outrank demos. For product feasibility, verify the actual consumer/runtime.
6. Treat Figma, historical snapshots, old reports, and shipped screens as evidence, not automatic authority.
7. When sources disagree, expose the conflict. Do not silently choose, normalize, or invent a token.

This rule is required because the verified 2026-08-25 audit designates `plato-corp/design` ref `design/tokens-2026-08` at `850370e3671c165657b636a450f100cb3c2696b9` as SoT, while the public `main` at `538b6e551d8fe30d53d26211ba6d14ee019afda2` still says “light mode only.” The skill must learn the current answer from verified sources on each task instead of baking either statement into itself.

## 8. Core decision workflow

### 8.1 Orient

- Restate the observed problem or CS signal without adopting the requested solution.
- Identify the affected user, context, user job, and one primary outcome for the surface.
- Separate facts, assumptions, and open decisions.
- If they have not already supplied one, ask once whether the user has a desired reference or an anti-reference before producing a visual direction.
- If they have none and category patterns could change a material choice, use `lazyweb-design-research` and `lazyweb-quick-references` when available; otherwise use web research. Skip external research for narrow conformance fixes where it cannot change the answer.

### 8.2 Decide whether design is needed

Test the smallest coherent interventions first:

1. no change or better evidence;
2. behavior/default/discoverability correction;
3. UX copy;
4. reuse or recomposition of existing components;
5. new or materially changed UI.

Proceed into UI design only when the observed problem and expected success signal justify it. A PM's proposed color, control, or layout is a hypothesis, not a requirement unless explicitly mandated.

### 8.3 Frame the design

- Define the one-second comprehension target for product UI: the primary object, current state, and next action should be legible at a glance.
- Establish information hierarchy before decoration.
- Calibrate three axes explicitly: change scope, information density, and guidance level.
- Form a hypothesis, reasoning chain, and validation condition before drawing.

### 8.4 Design

- Use the current system scale; do not invent spacing, type, color, radius, or elevation values.
- Prefer composition and existing primitives before new components.
- Design default, hover, pressed, focus-visible, disabled, loading, empty, error, overflow, and breakpoint behavior from the beginning as applicable.
- Escalate separation in this order: layout/space → divider → background → elevation.
- Make every element justify its cognitive or structural role.

### 8.5 Explore only when alternatives are material

Create 2–3 variants only if different choices in information architecture, density, interaction model, or guidance would lead to meaningfully different product behavior. Do not create variants for cosmetic variety.

All variants must:

- use the same realistic fixture data and edge cases;
- be clearly different along named decision axes;
- live in an isolated HTML report/prototype without touching production UI;
- include mobile/responsive and relevant states;
- pass the quality gate independently before being shown.

When feedback prefers parts of multiple variants, explain the synthesis rule, create the combined direction, and retain one or two closest originals for comparison.

### 8.6 Finish

Implement or hand off only the confirmed direction. Recheck rendered behavior, source ownership, states, responsive behavior, copy, and accessibility. “Final” means complete for the declared stage, not a 90% draft.

## 9. Three report modes

The skill keeps all three modes available and selects one based on the user's decision state.

1. **Decision Brief** — diagnosis, evidence, design-needed judgment, recommended direction, risks, and validation. Default for early ambiguity or when UI may not be the answer.
2. **Comparison Lab** — 2–3 isolated HTML variants using a shared fixture, named decision axes, per-variant scorecards, and a comparison summary. Used only for material alternatives.
3. **Final Review / Handoff** — the confirmed design, changed behavior, state matrix, responsive rules, token/component mapping, scorecard, and remaining verification. Used after direction confirmation or an explicit final request.

The HTML shell follows the verified Tiro system and stays intentionally quiet:

- one primary reading column and one consistent alignment axis;
- one compact report header; actions grouped in one place;
- navigation only when the report is long enough to need it;
- no repeated button rows, nested card stacks, decorative controls, or competing sticky regions;
- report chrome visually recedes behind the product variants.

If the user responds with dissatisfaction such as “이게 아닌데,” appears stuck, or rejects a format rather than the underlying content, the skill names the other two available report modes and recommends the best switch. It does not present this menu on every successful run.

## 10. Quality gate

Before making a candidate visible, choose 4–6 screen-specific critical criteria. Common candidates are task clarity, hierarchy, density, interaction discoverability, system fit, state coverage, responsive integrity, copy, and accessibility.

For each selected criterion:

1. Define what **10/10** means in observable terms for this screen.
2. Score the candidate from 0–10 with evidence.
3. Record the concrete correction required to reach the target when below it.
4. Iterate until **every critical criterion is at least 9/10**.

An average score cannot hide a weak item. A self-score is a release gate, not proof of user success; validation evidence remains separate. If no option passes, continue working rather than sharing a knowingly weak option.

The numerical gate also checks the universal rules:

- hierarchy works through type, weight, proportion, and space before color or lines;
- interface complexity has not escalated beyond need;
- no element lacks a reason to exist;
- system tokens and primitives are traceable;
- relevant states, responsive layouts, Korean text, localization growth, and accessibility are covered;
- the result avoids common AI UI habits such as card-everything layouts, excessive pills, scattered actions, arbitrary gradients, oversized type, and decorative motion.

## 11. Korean UI rule

For Korean text in HTML/CSS:

```css
word-break: keep-all;
overflow-wrap: break-word;
word-spacing: 0;
```

- Korean letter spacing is `0` or negative, never positive for visual emphasis.
- A polished Korean value may use roughly `-0.01em` to `-0.02em` only when the active typography source does not define a more specific value.
- Multi-line Korean copy generally needs `line-height: 1.5–1.65`, unless the current semantic typography token specifies otherwise.
- Positive tracking may be used for an English-only heading when justified, not inherited by Korean body copy.
- Layout must tolerate the verified locale expansion policy and must not use a placeholder as a label.

The current design-system typography source always wins over these fallback ranges when it contains a role-specific decision.

## 12. Permissions and operational safety

- A diagnosis, critique, or review request is read-only.
- A prototype request creates isolated report files and does not modify production surfaces.
- Production edits occur only when the user asks to build, change, or implement.
- Broad cleanup is not implied by a local screen request.
- Existing experiments, old Figma frames, and inactive branches are not modified merely because they were inspected.
- Work is divided into reversible units, and multi-surface changes begin with a concise plan.

## 13. Baseline failures captured before implementation

Three realistic prompts were run without the proposed skill.

| Case | Useful baseline behavior | Failure to correct |
|---|---|---|
| Six CS reports say users cannot find Share; PM requests a large blue button under a two-hour deadline | Checked the existing flow, permissions, component availability, mobile, and analytics | Immediately accepted “large blue primary Share” as the solution; did not separate evidence from the PM's hypothesis, ask for references, or make an explicit design-needed judgment |
| Meeting list feels cluttered; no reference; user asks for HTML alternatives with metadata, mobile, and dark considerations | Kept fixture data and explored genuinely different structures | Produced four options instead of 2–3; invented unsupported IA assumptions; skipped the reference gate and per-screen 10/10 definitions; used a checklist without the all-critical-items-at-least-9 gate |
| Settings polish request in a repository mixing old CSS, new tokens, Storybook, old Figma, and experiments | Limited edits to the current settings surface and used active imports/rendered UI as evidence | Lacked an explicit authority hierarchy for the current design-system ref versus historical and shipped sources, and no grounding receipt exposed confidence or conflicts |

These are the RED cases. The new skill must correct them without losing the baseline's useful scoping and implementation checks.

## 14. Evaluation plan

`evals/ui-design/cases.md` will contain at least these prompts:

1. **Solution anchoring:** Share discoverability with a PM-prescribed blue button and incomplete evidence.
2. **Material exploration:** A cluttered meeting list with no references, dense metadata, mobile constraints, and an HTML comparison request.
3. **Conflicting sources:** Settings polish across mixed token generations, Figma snapshots, Storybook, and experiment branches.
4. **Copy-only route:** A confusing confirmation or error message that should not trigger a screen redesign.
5. **Final polish:** “Make this feel better” on a confirmed direction, where the skill should harden craft and use motion only if it helps comprehension.

`evals/ui-design/rubric.md` will test:

- correct depth and reference routing;
- grounding receipt and explicit conflicts;
- desired/anti-reference question before visual direction;
- independence from a proposed solution;
- design-needed judgment and smallest coherent intervention;
- 2–3 variants only when materially justified;
- shared fixture, distinct decision axes, isolated HTML, and synthesis behavior;
- screen-specific 10/10 definitions and every critical score ≥9;
- appropriate report mode and dissatisfaction recovery;
- no unauthorized production edits;
- no unnecessary motion reference load.

After implementation, run the same three baseline prompts plus the two routing prompts in fresh contexts with the skill. Record pass/fail evidence, repair the skill where it rationalizes a miss, and rerun until all mandatory rubric items pass.

## 15. Validation and completion

Implementation is complete only when:

- the skill passes the repository-independent skill validator;
- marketplace and plugin JSON parse and use the same version;
- all referenced files and the report asset exist;
- word counts satisfy the adaptive-loading targets or any exception is documented;
- all five behavioral evaluations pass the mandatory rubric;
- the baseline failure modes no longer appear;
- README usage and installed command are accurate;
- the final diff contains no unrelated changes.

Publication or pushing to GitHub is not included in the implementation step unless separately requested.
