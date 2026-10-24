# Stepped waveform — medium, 60 carriers, horizontal, slow flow

A self-contained brand graphic reference: the stepped-waveform geometry Tiro uses
as a product-proof backdrop, reduced to pure functions plus one ready carrier set.
No raster field, no product UI, no network.

This is a **current working reference**, not a universal default and not a
production-adopted setting. The `thin` and `thick` profiles are comparison
alternatives to `medium`.

## Files

| File | What it is |
|---|---|
| `stepped-wave-geometry.js` | Pure geometry (`geometry`, `section`, `at`, `clamp`, `profiles`). No DOM, no texture, no dependencies. Extracted verbatim from the local review renderer. |
| `carriers-nib-60.json` | 60 horizontal carrier rows sampled from the Tiro pen-nib graphic object. Human-readable numbers; the canonical data. |
| `carriers-nib-60.js` | Same data as a browser global (`window.TiroWaveCarriers`) so `index.html` opens straight from disk with no server. |
| `index.html` | Standalone preview: play/pause, theme toggle, profile switch. Reduced-motion static, stops when offscreen. No network requests. |
| `identity.test.cjs` | Smoke test + byte-for-byte identity check against the original source geometry. |
| `provenance.json` | Config values, source SHA-256s, and the policy exclusion list. |

## Run it

Preview — just open `index.html` in a browser (double-click; no server needed).

Test:

```sh
# standalone smoke test (no original source required)
node identity.test.cjs

# full identity check against the production geometry source
node identity.test.cjs /path/to/stepped-wave.js
```

## The idea

A "carrier row" is a flat array `[x0,y0, x1,y1, ...]` of paired upper/lower edge
vertices describing one horizontal section of an object. `geometry(rows, time,
horizontal, moving, sweep, profile)` turns the rows into a stepped field:

- one faint hairline baseline per carrier,
- four flat rectangular body weights whose thickness follows the object's local
  tonal mass, thresholded at three quantile cuts.

The five `widths` and three `cuts` per profile are the only style knobs. `medium`
is the reference here; `thin` and `thick` change only those numbers.

## Slow flow

With `sweep = null` and `moving = true`, the field drifts continuously:
`drift = (elapsedSeconds * 3) % 6`. That gentle, cell-quantised translation is the
"slow flow" — the signal travels through the material while carrier positions and
object length never breathe. Draw is throttled to ~32 ms. `prefers-reduced-motion`
freezes the field (`moving = false`, deterministic), and motion stops when the
document is hidden or on `pagehide`.

Precise config values are in `provenance.json`.

## Minimal integration

```js
const { geometry } = require('./stepped-wave-geometry.js');
const { rows } = require('./carriers-nib-60.json');

const g = geometry(rows, elapsedSeconds, /*horizontal*/ true, /*moving*/ true, null, 'medium');
// g.field   -> baseline path per carrier
// g.guides  -> hairline level-0 path (set stroke-width = g.widths[0])
// g.bodies  -> [4] flat-fill path strings, weights 1..4
// g.counts  -> bars emitted per weight
```

See `index.html` for a complete SVG binding with controls and accessibility
fallbacks.

## Scope and provenance

Derived from the Tiro onboarding backdrop. The geometry is extracted verbatim; the
60 carriers are generated from one abstract brand object (a pen nib — no text, no
faces, no UI, no PII) using the local review horizontal-sampling method. The large
raster field dataset, the full product simulation, product chrome, and any internal
references are deliberately excluded. Source hashes and the full exclusion list are
in `provenance.json`.

License: MIT (ThePlato Inc.), same as the repository `LICENSE`.
