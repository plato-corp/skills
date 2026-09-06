# Tiro landing-design for Claude Code

`tiro:landing-design` is the public-page workflow for Tiro landing pages, pricing and ROI pages, promotional subpages, security explainers, and other persuasive or decision-supporting web surfaces. It is not the workflow for recurring in-product GUI tasks.

## Install from GitHub

Run these commands in Claude Code:

```text
/plugin marketplace add plato-corp/skills
/plugin install tiro@plato-skills
```

Restart Claude Code, or run `/reload-plugins` after an update. The skill is then available as:

```text
/tiro:landing-design
```

To fetch a newer release:

```text
/plugin marketplace update plato-skills
```

If the repository is private, authenticate Git first with an account that can read `plato-corp/skills`.

## Paste-ready autonomous prompt

Use this when you want Claude Code to inspect, plan, implement, and verify without stopping for routine design approvals:

```text
/tiro:landing-design

이 랜딩페이지 작업을 autonomous mode로 끝까지 진행해줘.

대상:
- 저장소/경로: <repository or local path>
- 현재 URL: <local or deployed URL>
- 페이지 job: <persuade | decide | read | route>
- 목표 행동: <the one visitor action that matters>

보존할 것:
- 검증된 사실, 링크, 가격, 접근 상태, 기존 필수 콘텐츠
- 현재 제품의 디자인 시스템과 공용 Header/Footer 계약

바꿔도 되는 것:
- 정보 구조, 카피 위계, 섹션 구성, 시각 방향, 반응형 재조립, 상호작용과 모션

완료 기준:
- 먼저 현재 페이지와 가장 가까운 공개 형제 페이지를 확인해 site family를 기록한다.
- visitor job과 page thesis를 고정하고, 모든 주장에 근거를 연결한다.
- 기존 페이지라면 섹션·카피·링크·상태 인벤토리를 만든 뒤 누락 없이 재구성한다.
- 한 개의 evidence-bearing carrier와 한 개의 명확한 visual direction을 선택한다.
- 데스크톱 1440px, 태블릿, 모바일 390px/360px에서 실제 렌더를 검사한다.
- 키보드, focus, reduced motion, overflow, console, test, lint, build를 확인한다.
- Blocker/Major 시각 결함을 수정하고 재캡처한 뒤에만 완료라고 보고한다.

중간 승인은 생략하되, 사실 충돌·권한 부족·되돌릴 수 없는 결정이 있으면 그 지점에서만 멈춰라. 마지막에는 변경 파일, 검증 결과, 남은 위험만 간결하게 보고해라.
```

## Focused invocations

Use one action when the whole workflow is unnecessary:

```text
/tiro:landing-design critique
현재 구현은 수정하지 말고 1440px와 390px 렌더를 기준으로 Blocker/Major만 진단해줘.
```

```text
/tiro:landing-design polish
승인된 메시지와 콘텐츠는 보존하고, 반복되는 섹션 실루엣과 약한 CTA 위계만 한 번의 correction pass로 고쳐줘.
```

```text
/tiro:landing-design release
실제 렌더, 반응형, 접근성, 동작, 테스트, 린트, 빌드를 확인하고 release verdict를 내려줘.
```

For an approved rendered page that must be moved into another repository, explicitly request `fidelity-port` and name the canonical source, destination, and allowed deltas.

## What good output looks like

Claude Code should leave a compact state record using:

```text
page / job / active action / locked / open / passed / evidence paths / explicit deltas
```

The final result is not complete merely because the code builds. The visitor must be able to identify what to read, what to believe, what to inspect next, and what action to take; the rendered desktop and mobile page must support that route.
