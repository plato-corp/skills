/* Tiro stepped-waveform geometry — pure functions, no DOM, no raster.
 *
 * Extracted verbatim (geometry authority only) from the local review renderer.
 * Source: stepped-wave.js  sha256 c3931500251c72857fb51d05000c97591787fe91099d12890b735a29dafec529
 * The production file also carries an embedded paper-ink PNG texture and the
 * SVG DOM render path; neither is reproduced here. This file is the geometry
 * only, so a stepped waveform can be computed from material carrier rows with
 * zero dependencies.
 *
 * A "carrier row" is a flat array [x0,y0, x1,y1, ... ] of paired upper/lower
 * edge vertices describing one object section. references/.../carriers-*.json
 * ships a ready set of 60 horizontal rows.
 *
 * profiles: the five flat bar weights and three tonal cut quantiles for each
 * line thickness. "medium" is the working reference for this skill.
 */
(function (root) {
  const profiles = {
    thin:   { widths: [.045, .105, .19, .30, .44], cuts: [.40, .70, .90] },
    medium: { widths: [.05, .1425, .265, .41, .59], cuts: [.325, .60, .825] },
    thick:  { widths: [.055, .18, .34, .52, .74], cuts: [.25, .50, .75] }
  };

  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

  function section(row, horizontal) {
    const n = row.length / 4, edge = horizontal ? 1 : 0, samples = [];
    for (let j = 0; j < n; j++) {
      const a = j * 2, b = row.length - 2 - a;
      samples.push({
        along: row[a + 1 - edge],
        center: (row[a + edge] + row[b + edge]) / 2,
        half: Math.abs(row[a + edge] - row[b + edge]) / 2
      });
    }
    return samples;
  }

  function at(points, position) {
    if (position < points[0].along || position > points.at(-1).along)
      return { half: 0, center: points[0].center };
    let lo = 0, hi = points.length - 1;
    while (hi - lo > 1) { const mid = (lo + hi) >> 1; if (points[mid].along < position) lo = mid; else hi = mid; }
    const a = points[lo], b = points[hi], f = clamp((position - a.along) / Math.max(.00001, b.along - a.along), 0, 1);
    return { half: a.half + (b.half - a.half) * f, center: a.center + (b.center - a.center) * f };
  }

  /* rows:        array of carrier rows (flat paired-vertex arrays)
   * time:        seconds; only the fractional cell drift matters for flow
   * horizontal:  true for 60-horizontal reference
   * moving:      false freezes the field (reduced motion / static preview)
   * sweep:       null => continuous flow; a finite 0..1 => one-shot transition
   * profile:     "thin" | "medium" | "thick"
   * Returns { field, guides, bodies:[5 path strings], widths, counts }.
   */
  function geometry(rows, time, horizontal, moving = true, sweep = null, profile = "thin") {
    const selected = profiles[profile] || profiles.thin;
    const pitch = (horizontal ? 356 : 366) / Math.max(1, rows.length - 1), sections = rows.map(r => section(r, horizontal));
    const bodies = [[], [], [], []], guides = [], counts = [0, 0, 0, 0], widths = selected.widths.map(v => v * pitch);
    const cell = 6, clock = moving ? time : 0, oneShot = Number.isFinite(sweep), progress = oneShot ? clamp(sweep, 0, 1) : 0;
    const sweeping = moving && oneShot && progress > 0 && progress < 1;
    // One cell of travel ends on the same grid, so settling cannot snap back.
    const drift = oneShot ? (sweeping ? cell * progress * progress * (3 - 2 * progress) : 0) : (clock * 3) % cell;
    const field = sections.map(points => { const c = points[0].center; return horizontal ? `M0 ${c.toFixed(2)}H390` : `M${c.toFixed(2)} 0V380`; });
    const candidates = [];
    sections.forEach((points, index) => {
      const supported = points.filter(p => p.half > pitch * .025); if (supported.length < 2) return;
      const start = supported[0].along, end = supported.at(-1).along, center = points[0].center;
      guides.push(horizontal ? `M${start.toFixed(2)} ${center.toFixed(2)}H${end.toFixed(2)}` : `M${center.toFixed(2)} ${start.toFixed(2)}V${end.toFixed(2)}`);
      for (let j = Math.floor((start - drift) / cell); j <= Math.ceil((end - drift) / cell); j++) {
        const lo = Math.max(start, j * cell + drift), hi = Math.min(end, (j + 1) * cell + drift); if (hi - lo < .02) continue;
        const along = (lo + hi) / 2, material = at(points, along), tone = clamp(material.half / (pitch * .41), 0, 1); if (tone < .075) continue;
        candidates.push({ lo, hi, along, material, tone, index });
      }
    });
    // Quantiles use visible cells, not vertex counts: short/long carriers and
    // flat book-page highlights must not silently lose the upper weight.
    const tones = candidates.map(c => c.tone).sort((a, b) => a - b);
    const cuts = selected.cuts.map(q => tones[Math.floor((tones.length - 1) * q)] || 1);
    for (const { lo, hi, along, material, tone, index } of candidates) {
      const local = clamp((progress - .08 * index / Math.max(1, rows.length - 1)) / .92, 0, 1);
      const distance = oneShot ? along - (-80 + 560 * local) : ((along - clock * 38 - index * 1.6 + 210) % 420 + 420) % 420 - 210;
      const envelope = Math.max(0, 1 - Math.abs(distance) / 64);
      const signal = oneShot ? (sweeping ? .06 * envelope * Math.sin(distance * Math.PI / 22) * Math.sin(Math.PI * progress) : 0) : 0;
      const level = cuts.filter(c => tone + signal >= c - .000001).length;
      const w = widths[level + 1], length = hi - lo, c = material.center;
      bodies[level].push(horizontal
        ? `M${lo.toFixed(2)} ${(c - w / 2).toFixed(2)}h${length.toFixed(2)}v${w.toFixed(2)}h${(-length).toFixed(2)}Z`
        : `M${(c - w / 2).toFixed(2)} ${lo.toFixed(2)}h${w.toFixed(2)}v${length.toFixed(2)}h${(-w).toFixed(2)}Z`);
      counts[level]++;
    }
    return { field, guides: guides.join(''), bodies: bodies.map(v => v.join('')), widths, counts };
  }

  const api = { geometry, profiles };
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.SteppedWaveGeometry = api;
})(typeof window === 'object' ? window : globalThis);
