/* Identity + smoke test for the extracted stepped-wave geometry.
 *
 *   node identity.test.cjs [path-to-original-stepped-wave.js]
 *
 * With no argument it runs the standalone smoke test only (no network, no DOM):
 * it asserts the extracted geometry produces a stable, non-empty medium
 * 60-horizontal field and that reduced-motion (moving=false) is deterministic.
 *
 * Given the original local-review stepped-wave.js it additionally asserts the
 * extracted geometry matches the source byte-for-byte across flow, static, and
 * one-shot sweep for the medium profile plus the thin/thick alternatives.
 */
const assert = require('assert');
const ext = require('./stepped-wave-geometry.js');
const { rows, meta } = require('./carriers-nib-60.json');

function fingerprint(g) {
  return JSON.stringify([g.bodies, g.guides, g.field, g.counts, g.widths]);
}

// --- standalone smoke test (always runs) ---
assert.strictEqual(rows.length, 60, 'expected 60 carriers');
assert.strictEqual(meta.count, 60);
const base = ext.geometry(rows, 0, true, true, null, 'medium');
const total = base.counts.reduce((a, b) => a + b, 0);
assert.ok(total > 200, 'medium field should produce a dense bar set, got ' + total);
assert.strictEqual(base.bodies.length, 4, 'four fill weights expected');
assert.strictEqual(base.field.length, 60, 'one baseline per carrier');
// reduced motion is frozen and reproducible
assert.strictEqual(
  fingerprint(ext.geometry(rows, 5, true, false, null, 'medium')),
  fingerprint(ext.geometry(rows, 99, true, false, null, 'medium')),
  'static output must not depend on time'
);
// flow actually moves the field
assert.notStrictEqual(
  fingerprint(ext.geometry(rows, 0, true, true, null, 'medium')),
  fingerprint(ext.geometry(rows, 1, true, true, null, 'medium')),
  'flow output must advance with time'
);
console.log('smoke OK: medium 60-horizontal bars =', base.counts, 'total', total);

// --- identity test against the original (optional) ---
const originalPath = process.argv[2];
if (!originalPath) {
  console.log('identity: skipped (pass path to original stepped-wave.js to enable)');
  process.exit(0);
}
const orig = require(originalPath);
let checks = 0;
function cmp(label, a, b) { assert.strictEqual(fingerprint(a), fingerprint(b), label); checks++; }
for (const t of [0, 0.37, 1.9, 6.2, 33.333])
  cmp('flow medium t=' + t, orig.geometry(rows, t, true, true, null, 'medium'), ext.geometry(rows, t, true, true, null, 'medium'));
cmp('static medium', orig.geometry(rows, 5, true, false, null, 'medium'), ext.geometry(rows, 5, true, false, null, 'medium'));
for (const p of [0, 0.25, 0.5, 0.75, 1])
  cmp('sweep p=' + p, orig.geometry(rows, 0.5, true, true, p, 'medium'), ext.geometry(rows, 0.5, true, true, p, 'medium'));
cmp('flow thin', orig.geometry(rows, 2, true, true, null, 'thin'), ext.geometry(rows, 2, true, true, null, 'thin'));
cmp('flow thick', orig.geometry(rows, 2, true, true, null, 'thick'), ext.geometry(rows, 2, true, true, null, 'thick'));
console.log('identity OK:', checks, 'comparisons matched original source');
