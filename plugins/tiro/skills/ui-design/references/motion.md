# Motion sidecar

Read only when motion affects state comprehension, continuity, spatial change, or feedback, or when the user explicitly asks for motion.

## Purpose gate

For each transition, state:

```text
Trigger: what changed
User question answered: where did it go / did it work / what is active
Animated properties: minimum needed
Reduced-motion equivalent: same meaning without the movement
```

If motion does not answer a user question, omit it. Do not use animation to compensate for unclear hierarchy or to make a static screen feel more “premium.”

## Implementation rules

- Read the current Tiro motion guideline and component source before choosing duration, easing, or properties; do not memorize numeric values in this skill.
- Prefer opacity and position for enter/exit or spatial continuity, and subtle press feedback for controls when the active system permits it.
- Avoid layout-janking properties, attention-seeking loops, decorative bounce/spring, blur, glow, particles, and parallax unless a current explicit product rule authorizes them.
- Preserve interruption and rapid-repeat behavior; an animation must not trap input or leave an impossible intermediate state.
- Honor `prefers-reduced-motion` or the platform equivalent and verify the non-motion state transition.
- Review loading, success, error, panel, overlay, and focus behavior together with motion rather than as separate decoration.

Motion is optional. A GUI task that passes without it should not load or apply this reference.
