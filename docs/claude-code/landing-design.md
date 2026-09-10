# Tiro landing-design for Claude Code

`tiro:landing-design` builds and redesigns product and campaign landing pages with a compact, self-contained studio workflow. It is not the workflow for recurring in-product GUI tasks.

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

Before the release branch is merged, test that exact GitHub branch with:

```text
/plugin marketplace add plato-corp/skills@codex/tiro-landing-design
/plugin install tiro@plato-skills
```

To fetch a newer release:

```text
/plugin marketplace update plato-skills
```

If the repository is private, authenticate Git first with an account that can read `plato-corp/skills`.

## Start a landing project

```text
/tiro:landing-design

대상: <저장소/경로와 현재 URL>
방문자와 제품: <대상 사용자와 검증된 제품 사실>
목표 행동: <방문자가 마지막에 할 행동>
보존할 것: <기존에 승인된 내용>
변경 범위: <기획·카피·디자인·구현 중 맡길 범위>

건당 억 단위 프로젝트를 책임지는 디자인 스튜디오 대표 기준으로 진행해줘.
이번 프로젝트의 핵심 요구와 6개 영역 × 10개 평가 항목을 먼저 만들고,
대제목만 이어 읽는 검사와 실제 화면·동작 검수 후 완성본을 보여줘.
```

The skill contains the required workflow in one file. It generates `LANDING-DESIGN.md` and `LANDING-REVIEW.md` in the project rather than loading a fixed 60-item rubric or a tree of reference instructions.

Before claiming a complete new landing, inspect the actual heading sequence without body text, section handoffs, two distinct scroll behaviors, desktop/tablet/mobile layouts, intermediate widths, and actual interactions. Every project-specific item must score at least 4.5/5 with relevant evidence. Scores are internal review judgments, not user research or proof of design quality.

## Focused changes

```text
/tiro:landing-design
레이아웃은 유지하고 제목만 고쳐줘. 실제 대제목을 순서대로 붙여 읽고,
본문 없이 제품의 기능과 이점을 이해할 수 있도록 다듬어줘.
세 기기의 줄바꿈도 확인해줘.
```

Focused corrections retain unaffected decisions and validate relevant criteria and responsive regressions. They do not trigger a new full-page rubric or a requirement to add two scroll effects. Exact ports of an approved source should preserve the source and are outside this creative redesign workflow.
