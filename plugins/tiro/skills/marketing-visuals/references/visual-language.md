# Visual language

Use whenever visual direction, image generation, typography, or final craft is in scope.

## Weighted moodboard

The selected eight images have two authority levels.

### Fidelity bar — read first

- `assets/moodboard/07-compatibility-reference.png`: large left-aligned Korean message, calm negative space, one connected right-side object family, quiet compatibility chips, restrained mark.
- `assets/moodboard/08-milestone-reference.png`: headline positioned against a rising tactile event, confident company tone without financial hype, bottom evidence/sample label.

These two are near-production references. Use them to judge type placement, whitespace, image-to-copy balance, and emphasis. Do not impose their left/right layout on every story.

### Supporting vocabulary

| Asset | Useful for |
|---|---|
| `01-shared-surface.png` | team presence, collaboration, shared surface |
| `02-context-rooms.png` | personal/team/company boundaries and context |
| `03-after-meeting.png` | traces of conversation and aftermath |
| `04-compressed-time.png` | live moments becoming reusable context |
| `05-modular-nota.png` | notation, speed, Tiro's origin without literal history |
| `06-living-archive.png` | organizational memory and relationships |

Load only the images relevant to the current category and decision.

## Current taste signals

- Treat anti-AI quality as purpose–evidence causality, not a handcrafted look. Surface traits cannot rescue an interchangeable composition.
- Judge image and typography together; a standalone background is not a candidate.
- Prefer one clear visual event and one dominant message field over evenly distributed decoration.
- Use warm stone, Tironian brown, cotton paper, vellum, linen, wood, thread, seams, layers, and quiet daylight.
- Lines must encode record, context, compression, transition, or connection—not ornamental movement.
- Favor soft continuity and poised dimensionality over fragmented collage and split-screen composition.
- Invoke Tiro's origin through rapid capture, base stroke plus modifier, compression, context, and living record.
- Keep brand authority quiet. Avoid performative futurism and exaggerated luxury styling.

## Nib → Trace → Connection

Continue to avoid literal-origin props. Tiro's official nib in `assets/tiro-mark.svg` is a core brand asset, not a generic historical-writing prop.

- The official Tiro nib may stand alone as the hero object when it serves the one-second message. It does not need a hand, a full pen body, or a historical scene to justify its presence.
- A trace beginning at the nib may express a real transition among speech, capture, record, structure, and sharing. Name the represented transition before drawing the line; if no message or evidence changes along it, remove it as decoration.
- Use this grammar when capture, continuity between environments, or connected records is central to the story. Do not force it into announcements whose proof should lead directly.
- Keep the official signature geometry intact. A separate nib-derived graphic may become photographic, sculptural, dimensional, cropped, or materially rendered when its source geometry remains recognizable and it is not presented as a replacement logo.
- Distinguish the official nib from generic quills, nostalgic fountain-pen still life, Roman props, manuscript cosplay, and arbitrary ancient glyphs. Those remain origin clichés.
- A photo-led candidate does not pass through warm mood alone. Quiet interiors, linen, wood, paper, plants, and daylight require an observable Tiro role through the official nib, a semantic trace, record evidence, or a verified product cue. Otherwise classify the result as Kinfolk drift and revise it.

## Palette

Resolve the current design source first. For this report scaffold and current marketing experiments, the working fallback is:

```css
--tiro-background: #FAFAF9;
--tiro-foreground: #3A2018;
```

These are not proof of current token conformance. Extend only with verified warm brown and stone roles. Do not introduce cool gray/blue styling or gradients.

## Typography roles

Requester-confirmed marketing working direction, 2026-08-26:

- Korean display: Hahmlet.
- English display: Reckless when the verified licensed source is available.
- Japanese display: Kozuka Gothic Pr6N R through the verified Adobe Fonts source.
- Product UI, utility labels, and body: Pretendard.

Packaged Hahmlet and Pretendard files support the report shell. They do not grant access to other licensed fonts.

### Known source conflict

At verified `plato-corp/design` ref `design/tokens-2026-08`, commit `71754875143ab598ba2b5fba31e74bf7fa729ab2`, current prose guidance assigns Averia Serif Libre to English marketing and Pretendard JP to Korean/Japanese headlines. `tokens/typography.yaml` still contains Hahmlet under `brandKr` but marks that role unused/deprecated. `tokens/colors.yaml` also carries Light/Dark semantic structures while `llms.txt` describes light-only usage.

For isolated marketing prototypes, use the requester-confirmed working direction and include this conflict in the source receipt. Before a final public asset, require either an updated SoT or an explicit project-level override. Do not describe an overridden prototype as fully design-system compliant. For exact color values, prefer machine-readable semantic tokens over prose and record any divergence from the scaffold fallback.

Korean defaults:

```css
word-break: keep-all;
overflow-wrap: break-word;
word-spacing: 0;
```

- Korean tracking is `0` or negative. Never add positive tracking for emphasis.
- Positive tracking is allowed for an English-only utility label when it does not inherit into Korean text.
- Korean body line-height usually needs `1.5–1.65` unless the verified role specifies another value.

## 1200×675 title baseline

Starting calibration for Korean display:

```text
Family: Hahmlet
Weight: 510
Size: 72px equivalent
Line-height: 1.08–1.10
Letter-spacing: -0.07em
Vertical correction: 0
```

This baseline belongs to the tested title/canvas class, not every sentence. Recheck line count, mixed Latin/Korean width, punctuation, visual center, and image collision.

Every change records:

```text
Role/title: <identifier>
Previous: <size / line-height / tracking / position>
New: <size / line-height / tracking / position>
Reason: <observable optical problem corrected>
```

## Image generation contract

- Generate background art without text, letters, numbers, logos, certification seals, metrics, or watermarks.
- Reserve usable negative space based on the approved composition, not an arbitrary left/right default.
- Name intended crop and channel, dominant object, material, lighting, palette, and avoid list.
- Inspect outputs for unintended letterforms, cliché symbols, false brand marks, distorted devices, and decorative noise.
- Save selected project-bound assets inside the skill consumer's workspace; do not leave them only in a tool cache.

## Avoid

- generic SaaS 3D blobs, glowing spheres, glassmorphism, arbitrary gradients;
- cold blue cybersecurity, giant lock/shield badges;
- neon waveform, microphone, or podcast clichés;
- rocket, chart, coins, confetti, or victory poses for investment news;
- generic quills, nostalgic fountain-pen still life, Roman busts, parchment cosplay, or literal ancient glyph decoration; apply the official Tiro nib according to `Nib → Trace → Connection` instead of banning it;
- excessive pills, nested cards, repeated buttons, decorative squiggles;
- fake metrics, badges, screenshots, seals, partner marks, and claims.
