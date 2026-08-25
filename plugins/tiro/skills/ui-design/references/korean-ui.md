# Korean product UI

Read when Korean text, localization, or an HTML report contains Korean.

## CSS fallback

Use the current semantic typography token when it defines these values. Otherwise:

```css
.ko {
  word-break: keep-all;
  overflow-wrap: break-word;
  letter-spacing: 0;
  word-spacing: 0;
  line-height: 1.5;
}
```

- Korean tracking is `0` or negative. Never add positive tracking for emphasis.
- For a polished Korean setting, roughly `-0.01em` to `-0.02em` may be appropriate only when no role-specific token exists.
- Multi-line Korean copy generally needs `1.5–1.65` line-height when the active type token does not specify a value.
- English-only headings may use slight positive tracking when justified; do not inherit it into Korean text.
- `word-spacing: 0` remains the default.

## Layout and language

- Keep labels separate from placeholders.
- Allow verified KO/JA expansion; avoid fixed widths that assume English length.
- Do not concatenate sentence fragments across locales.
- Use current Tiro glossary and UX-writing guidance for nouns, action labels, formality, and English-across-locales exceptions.
- Check long titles, names, timestamps, badges, errors, and mixed Korean/Latin strings at narrow widths.
- Prefer semantic type roles over one-off size/weight/tracking combinations.

## Visual QA

- Inspect actual wrapping; do not infer Korean line breaks from English mocks.
- Reject isolated particles, awkward one-syllable last lines, and positive-tracking inheritance.
- Confirm bold Korean headings remain readable without using extra spacing to imitate English typography.
- Re-score hierarchy and density after real localized strings replace placeholders.
