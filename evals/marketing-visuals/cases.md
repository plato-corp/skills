# Tiro Marketing Visuals behavioral cases

Run each case in a fresh context when independent model evaluation is available. For the RED control, do not expose the skill. For GREEN, instruct the evaluator to read and follow `plugins/tiro/skills/marketing-visuals/SKILL.md`. Do not provide the expected answer to the acting agent.

## Case 1 — Feature release with a supplied reference

```text
Tiro에 팀용 워크스페이스가 생겼다는 신규 기능 릴리즈를 알릴 블로그 썸네일이 필요해. 1초 안에 “Tiro에 팀용 워크스페이스가 생겼다”가 이해되어야 해.

Cursor Compile의 스트로크 기반 비주얼 문법을 참고하고 싶지만 그대로 베끼지는 말아줘. Tiro가 최초 속기사의 이름에서 온 브랜드라는 점도 1차원적인 깃펜·로마 이미지 없이 반영해줘. 한국어 타이틀은 Hahmlet, 제품 UI와 본문은 Pretendard야.

디자인 방향을 잡고 필요하면 비교 시안을 HTML로 보여줘.
```

### RED observation captured before authoring

The no-skill working session produced useful images and eventually found a distinctive material world, but the first comparison treated images as the main deliverable. The requester had to state that the actual text placement mattered more than a standalone image. The reference, typography calibration, and category emphasis were assembled across repeated turns instead of being converted into one compact working receipt and message hierarchy.

## Case 2 — Security announcement with no reference and a deadline

```text
오늘 안에 Tiro의 SOC 2 Type 2 인증 획득 소식을 블로그와 링크드인에 올려야 해. 참고하고 싶은 이미지는 딱히 없어. 보안 회사처럼 파랗고 차갑거나 자물쇠·방패가 크게 나오는 건 싫어. 빨리 완성 가능한 방향으로 알아서 만들어줘.
```

### RED observation captured before authoring

Before a dedicated skill existed, the announcement taxonomy and evidence-led security pattern appeared only after the requester manually listed security certification as a distinct content type. There was no reusable rule saying that certification name and verification evidence must lead, while generated background art must remain text-free and editable copy must be composed separately.

## Case 3 — Vague dissatisfaction after a first draft

```text
이 블로그 썸네일이 뭔가 AI가 만든 것처럼 애매하고 답답해. 정확히 뭐가 문제인지는 모르겠어. 다른 방향도 보고 싶긴 한데 시안을 잔뜩 늘리지는 말아줘. 알아서 다시 잡아봐.
```

Context available to the acting agent:
- an existing first-draft thumbnail;
- the eight user-selected Tiro mood references;
- `03 · 기기·소프트웨어 지원` and `05 · 투자 소식` were judged near-production quality.

### RED observation captured before authoring

The no-skill session generated broad visual variety and responded well to verbal feedback, but preference extraction remained implicit until the requester explicitly asked that the eight selected images become the moodboard. The six vocabulary images and the two near-production compositions were initially treated as equally useful references instead of a weighted hierarchy. A reusable rule for switching report format after dissatisfaction was also not yet attached to marketing work.

## Case 4 — Official nib versus literal-origin cliché

```text
Tiro가 음성, 회의, 개인 기록, 팀 기록처럼 서로 다른 환경에서 생긴 기록을 연결한다는 블로그 이미지를 만들어줘. Tiro 로고가 펜촉이라는 점을 살리고 싶고, 펜촉이 단독 오브제가 되어도 괜찮아. 다만 일반 깃펜이나 로마 시대 소품처럼 고대풍으로 보이는 건 싫어. 조용한 인테리어 사진만 예쁘게 놓인 이미지도 Tiro답지 않아.
```

### RED observation captured before authoring

The existing guidance correctly rejected quills, Roman props, and literal ancient decoration, but it did not distinguish those clichés from Tiro's official nib mark. In the working session, the agent over-applied the avoidance rule and proposed that a pen should not appear as a standalone object. The requester had to correct that the nib is the logo and may be the hero. The same session also showed that warm, quiet interior photography can pass the existing material rules while drifting into a pastoral Kinfolk look with no observable Tiro role.

## Case 5 — Multi-frame workspace article that needs diagrams

```text
팀 워크스페이스를 소개하는 한 편의 아티클에 이미지 네 장이 필요해. 순서는 Hero → 회사 자산과 정책 → 여러 워크스페이스 전환 → 팀 안의 개인 영역이야. Current 브랜드 룩으로 일관되게 만들되, 가짜 제품 UI나 의미 없는 카드·노드 다이어그램은 쓰지 말아줘.
```

### RED observation captured before authoring

The existing skill routed the story as a feature release and produced a coherent approved Photo Wash hero. It did not require a representation decision for each frame in a long-form series. The agent propagated the hero's photographic medium into the policy, transition, and personal-visibility frames, preserving mood while removing the relationships those frames had to explain. The requester had to point back to the legacy sequence and ask whether diagrams were necessary. The correction required a mixed series: one image-led hero followed by a result tree, a workspace branching diagram, and a nested visibility diagram.

## Case 6 — “AI 티를 빼달라”는 요청

```text
지금 만든 기능 릴리즈 이미지가 예쁘기는 한데 AI 티가 나. 그냥 덜 AI처럼 꾸미는 게 아니라, 이 이미지의 목적이 무엇인지와 여기서 AI 티가 난다는 게 정확히 무엇인지 먼저 정의하고 그 정의에 맞춰 다시 만들어줘.
```

### RED observation captured before authoring

The prior working session treated “AI-like” mainly as a list of familiar visual symptoms: equal cards, floating nodes, glows, random English labels, and generic SaaS composition. Those symptoms were useful but incomplete. They did not require the agent to define the artifact's intended viewer change or to prove that each major visual decision followed from that purpose and verified evidence. As a result, a candidate could avoid the listed clichés yet remain generic, atmospheric, or interchangeable with another brand. The requester had to restate that purpose definition, AI-smell definition, and execution against those definitions are the actual core workflow.
