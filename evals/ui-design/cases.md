# Tiro UI Design behavioral cases

Run each case in a fresh context. For the RED control, do not expose the skill. For GREEN, instruct the evaluator to read and follow `plugins/tiro/skills/ui-design/SKILL.md`. Do not provide the expected answer to the acting agent.

## Case 1 — Share discoverability under pressure

```text
IMPORTANT: This is a real product decision. Choose what you would do next and produce the actual response to the requester. Do not answer as a quiz.

Six CS tickets this week say users cannot find how to share a meeting note. The PM has already told the team: “Put a large blue Share button in the meeting-note header.” A release branch closes in two hours, and engineering says the change is only ten minutes if you approve that direction now. The current design-system repository path was not included in the request.

The product already has a Share action somewhere, but you have not yet verified its location, permission behavior, analytics, mobile treatment, or whether users who found it could complete the flow. No desired or disliked references were supplied.

Act as the design partner. What do you do and what do you send back now?
```

### RED observation captured before authoring

The no-skill control immediately chose a large blue primary `공유` button in the header. It did inspect the existing flow, permissions, design-system component, mobile, and event tracking, but it treated the PM's proposed solution as the direction rather than a hypothesis. It did not ask about desired/anti-references, state a design-needed judgment, or distinguish verified facts from assumptions.

## Case 2 — Material exploration for a cluttered meeting list

```text
Our meeting list feels cluttered. Each row may contain title, workspace, owner, participants, recording duration, created time, updated time, processing state, sharing state, and two quick actions. It must work on mobile and across the active color modes. I have no reference in mind. Show alternatives as an HTML report.
```

### RED observation captured before authoring

The control created four alternatives with useful structural variety, but invented unsupported information-architecture assumptions, skipped the reference gate, and used a general checklist instead of defining screen-specific 10/10 targets and requiring every critical score to reach 9.

## Case 3 — Conflicting design sources

```text
Polish the Settings UI. This repository contains old CSS, a new token package, Storybook, an old Figma export, and several experiment branches. Fix everything that looks inconsistent.
```

### RED observation captured before authoring

The control sensibly limited edits to the active Settings surface, but did not produce an authority hierarchy, verified design-system ref/commit, grounding receipt, or explicit conflict record.

## Case 4 — Copy-only route

```text
Users hesitate at a delete confirmation that only says “Are you sure?” Make this UX clearer. Do not change the underlying delete behavior.
```

## Case 5 — Confirmed-direction hardening

```text
The information architecture and layout are confirmed. Make this screen feel finished. It has default and loading examples, but no empty, error, keyboard-focus, narrow-width, or reduced-motion review yet.
```
