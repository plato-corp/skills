# Decision workflow

Use for standard and exploratory announcement work, especially when the message, reference, evidence, or source authority is unclear.

## 1. Frame the actual communication problem

Do not start with an image style. Record:

```text
Event: <what actually happened>
Audience: <who needs to care>
Channel: <blog / LinkedIn / other>
Purpose: When <audience> encounters this on <channel>, they should <recognize / understand / believe / do> <one thing> within <time>.
One-second message: <the sentence that makes the purpose legible>
Required evidence: <product cue / certification / support target / verified fact>
Non-goal: <what this image is not trying to communicate>
Verified facts: <facts with a source>
Assumptions: <not yet verified>
Open decisions: <choices that change the design>
Deadline: <if relevant>
```

The purpose is the intended viewer change, not the asset type (`thumbnail`), mood (`warm`), style (`editorial`), or production action (`make an image`). Choose one primary verb and one object. The one-second message is its release criterion. If the headline and dominant scene do not make that change legible, restructure before polishing.

## 2. Define AI-smell for this artifact

“AI-like” does not mean that an AI tool was used, and “less AI-like” is not a preset aesthetic. It is an observable failure of design causality: major visual choices appear because they are familiar, decorative, or statistically plausible rather than because this purpose and evidence require them.

Diagnose the complete image-plus-type frame with five tests:

1. **Purpose causality:** Can the dominant composition, hierarchy, and medium be explained from the purpose statement?
2. **Element role:** Does every salient element have one message, evidence, structural, or brand role?
3. **Evidence traceability:** Is the dominant proof traceable to a verified feature, certification, supported target, voice behavior, person, place, or milestone?
4. **Brand-swap test:** If only the logo and headline were replaced, would the frame still work unchanged for another SaaS or lifestyle brand?
5. **Rendered hierarchy:** At one second and thumbnail size, does the intended viewer change read before styling, atmosphere, or layout cleverness?

Equal cards, floating nodes, random English labels, glows, generic SaaS UI, pastoral atmosphere, and decorative traces are common clues, not the definition. Removing them does not pass the gate when the purpose–evidence disconnect remains. Likewise, asymmetry, texture, imperfection, zine styling, and handcrafted effects do not make a generic decision purposeful.

When a test fails, revise the message, evidence, representation, or hierarchy that caused the failure. Do not merely roughen, simplify, or restyle the same generic composition.

## 3. Resolve current sources

Read workspace instructions, then find the current Tiro design repository or canonical `plato-corp/design` remote. Search recent audits, handoffs, and migrations before accepting a default branch. Start at the repository's agent index or `llms.txt`; load only relevant brand, color, type, and asset sources.

Authority order:

1. verified designated SoT ref;
2. machine-readable brand and token sources for exact values;
3. active brand/type guidance for behavior and roles;
4. explicitly confirmed task direction, as a named prototype or project override when it conflicts with 1–3;
5. current consumers for feasibility;
6. Figma, historical exports, shipped thumbnails, and moodboards as evidence.

Expose conflicts. Do not merge mismatched sources silently. A task-level override may move a prototype forward, but final public work requires an updated SoT or explicit project-level authorization and must not claim false conformance.

## 4. Reference gate

Ask once when the request contains neither a desired reference nor a disliked reference:

> 시각적으로 참고하고 싶은 이미지·브랜드·링크와, 피하고 싶은 느낌이 있나요?

Continue useful message and source diagnosis while waiting. The question is answered when the user supplies a reference, an anti-reference, or says none exists; do not repeat it.

Reference routes:

- **Supplied reference:** identify transferable principles such as composition, stroke logic, material, crop, type scale, density, or evidence placement. Do not reproduce recognizable art.
- **No reference:** inspect the weighted Tiro board in `assets/moodboard/`. Read references 07–08 first for craft, then the relevant 01–06 images for vocabulary.
- **Material category gap remains:** use `lazyweb-design-research` and `lazyweb-quick-references` when available; otherwise research the web. Prefer primary sources and verify volatile platform specifications at task time.

Skip external research for narrow copy, crop, or optical corrections where it cannot change the answer.

## 5. Verify claims before visual emphasis

Separate factual evidence from layout copy. Do not invent:

- certification scope, audit date, seal wording, or compliance claims;
- supported devices, platforms, integrations, or release status;
- accuracy, latency, language coverage, or other voice metrics;
- investment amount, investor, valuation, date, or growth claim;
- partner logos, customer names, or quotes.

If the required fact is not verified, keep the direction conceptual and label sample copy as hypothetical. A polished layout cannot turn an assumption into evidence.

## 6. Decide whether new image-making is needed

Try the smallest coherent intervention:

1. clarify the message or factual proof;
2. correct title hierarchy, crop, or spacing;
3. reuse a selected Tiro asset with a new evidence block;
4. recombine an existing visual family;
5. generate a new background or materially new composition.

New imagery is justified when existing assets cannot express the announcement's primary evidence or when the image/type relationship requires a different visual event.

## 7. End the framing stage with a decision

Return:

```text
Primary message: <one sentence>
Purpose: <audience / channel / intended change / time>
Category: <one of six>
Evidence anatomy: <what must lead and support>
Reference route: <supplied / Tiro board / researched>
Design-needed judgment: <reuse / recompose / generate>
Candidate count: <one, or 2–3 with named material axes>
AI-smell risks: <failed or fragile tests from the five-test definition>
Claims still requiring verification: <none or list>
```
