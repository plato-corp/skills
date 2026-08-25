# Share discoverability evaluation — 2026-08-25

Case: `cases.md` → Case 1
Method: fresh-context acting agents; read-only; evaluators could read the skill and routed references but not the rubric, specification, git history, or prior results.

## RED control

Without the skill, the acting agent immediately selected a large blue primary Share button in the meeting-note header. It inspected useful implementation concerns, but accepted the PM's prescribed control as the design direction, skipped the desired/anti-reference question, and did not state a design-needed judgment.

## GREEN iterations

### Iteration 1 — partial pass

The agent rejected the large blue button, treated six CS tickets as a signal rather than a cause, defined completion-oriented success, and proposed a time-boxed evidence pass.

New failure, verbatim:

> 디자인 시스템 저장소 경로와 현재 기준 ref, 기존 공유 컴포넌트·사용 위치를 바로 전달해 주세요.

The path missing from the request became a user dependency even though the canonical repository was known. The skill was updated to require workspace/git-remote/canonical-repository lookup before asking.

### Iteration 2 — partial pass

The agent stopped asking the user for the path, but deferred grounding instead of performing it.

New failure, verbatim:

> Design source: canonical plato-corp/design checkout/remote 확인 예정
> Ref / commit: 미확인 — 시각 방향 승인 전에 기록

The skill was updated so a grounding receipt records completed checks, not future work; unverified status now requires a named failed attempt or access limit.

### Iteration 3 — partial pass

The agent inspected active UI behavior and recorded concrete runtime evidence, but accepted the default branch as current:

> Ref / commit: main · 538b6e551d8fe30d53d26211ba6d14ee019afda2

This contradicted the newer 2026-08-25 audit that designates another ref as SoT. The skill was updated to search recent audits, handoffs, and migrations before accepting a default branch and to verify the named remote ref.

### Iteration 4 — pass

The agent rejected solution anchoring, selected an investigate-first Decision Brief, continued useful work while asking about references, defined completion metrics, and found the current designated source:

```text
Design source: plato-corp/design 원격 저장소
Ref / commit: design/tokens-2026-08 / 850370e3671c165657b636a450f100cb3c2696b9
Governing files: 2026-08-25 GitHub↔Figma 전수 감사
Runtime evidence: 워크스페이스에서 활성 tiro-client/tiro-app 체크아웃을 찾지 못했고, GitHub 콘텐츠 접근은 repo scope 부족으로 제한됨
Known conflicts: Figma가 GitHub 정본과 불일치하므로 현재 시각 기준으로 사용할 수 없음
```

It did not invent runtime evidence. It named the failed lookup/access boundary and therefore kept conditional recommendations conditional.

## Mandatory rubric result

| Item | Result | Evidence |
|---|---|---|
| Reject immediate large-blue-button approval | Pass | Opened with explicit non-approval |
| Treat CS as signal, not cause | Pass | Separated friction evidence from discoverability/permission/completion cause |
| Smallest evidence pass | Pass | Desktop/mobile, roles, full share flow, events |
| Resolve current design source | Pass | Verified designated ref and exact commit; exposed Figma conflict |
| Ask desired/anti-reference without blocking | Pass | Asked once and continued diagnosis |
| Completion-oriented success signal | Pass | Open/view and success/open conversion, errors, CS recurrence |
| Correct report mode | Pass | Decision Brief; no premature variants or production mutation |
| Motion remains unloaded | Pass | Motion was not part of the response |

Outcome: **PASS for Case 1 after three narrowly-scoped refactors.** Cases 2–5 remain pending and this skill is not yet deployment-complete.
