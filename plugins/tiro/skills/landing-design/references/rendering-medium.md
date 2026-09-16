# Rendering-medium selection

Read this reference before visual composition when an approved rendered source has not already fixed the technique. Use it for the decisive screens and evidence-bearing sections, not for every paragraph or ordinary control.

## Keep four decisions separate

| Decision | Question | Example |
|---|---|---|
| Content model | What relationship must remain inferable? | transformation, containment, sequence |
| Carrier | What bears the evidence? | product state, graphic, photo |
| Rendering medium | How should this screen represent and behave? | SVG, DOM + WebGL, video |
| Implementation library | What can realize the approved medium in this stack? | an existing motion primitive, Three.js, a shader helper |

One decision never supplies the next. A `graphic` is not automatically styled HTML. A Three.js scene still needs a content model, evidence, and a reason that depth improves comprehension. Library selection comes last.

## Run a medium scan per decisive screen

Start from what the viewer must infer at rest, then identify what would become clearer through time, depth, continuity, procedural behavior, or direct manipulation. Shortlist only plausible media; do not enumerate a catalog for ceremony.

A decisive screen is the first viewport, a primary or signature carrier scene, a meaning-bearing interaction or transition, or a section whose evidence representation remains materially unresolved. Ordinary copy, navigation, and repeated controls inherit the accessible page system and do not require a ceremonial medium comparison.

| Medium | Strong fit | Weak fit or rejection signal |
|---|---|---|
| Semantic DOM + CSS | Reading, forms, tables, controls, disclosures, ordinary product states, exact responsive flow | Chosen only because it is familiar or fast; many decorative divs imitate a scene or simulation |
| SVG | Crisp bounded diagrams, paths, topology, timelines, masks, limited vector motion | Dense continuous particles, rich spatial depth, photographic or material realism |
| Raster image or generated asset | Authentic moment, art-directed texture, fixed high-detail composition | State must react, transform, localize, or remain sharp across unpredictable crops |
| Video or image sequence | Authored time-based narrative whose playback need not respond to the visitor | Direct manipulation, live data, many responsive states, essential meaning available only after autoplay |
| Canvas 2D | Drawing, many 2D marks, lightweight particles, pixel processing, a bounded simulation | Semantic reading and controls; simple vector relationships better expressed as SVG |
| WebGL or custom shader | Procedural material, continuous deformation, large particle fields, spatially coherent transformation, GPU image treatment | A static hierarchy, ordinary scroll reveal, or decoration with no evidence-bearing state |
| Three.js or React Three Fiber | Camera, depth, lighting, real 3D objects, spatial continuity, or direct manipulation are part of the explanation | A flat path, chart, card stack, or effect that gains no meaning from a scene graph |
| Shader or motion helper | The medium is already justified and a focused helper reduces implementation risk; examples may include Paper Shaders, Rive, or Lottie when compatible and available | The tool's demo becomes the concept, or a new dependency is chosen before the scene's job |
| Hybrid | Accessible DOM copy and controls surround an SVG, Canvas, video, or WebGL carrier; usually the safest advanced composition | Layers duplicate meaning, pointer handling conflicts, or the fallback is treated as a separate inferior design |

Include at least one non-DOM candidate when any of these is material to the approved evidence:

- depth or occlusion communicates ownership, containment, or hierarchy;
- continuity across states is easier to understand as one transformation than as swapped panels;
- particles or many independent marks carry real source data or fragmentation;
- procedural texture, distortion, or light expresses a verified material or boundary;
- camera or direct manipulation makes a spatial relationship inspectable;
- a flat implementation would require many artificial DOM fragments or lose the relationship.

Do not add a non-DOM candidate when the screen's job is stable reading, comparison, form entry, policy inspection, document access, or an ordinary state change that semantic HTML or SVG explains directly.

## Selection contract

Complete this before choosing a library or composing the full page:

```text
Screen or section:
Content model / semantic invariant:
Primary carrier / verified evidence:
What must be clear in the first static frame:
What time, depth, continuity, procedure, or input could clarify:
Plausible candidates:
Selected medium:
Observable communication or perceptual gain:
Closest rejected alternative / why it loses:
Current-stack integration:
New dependency or capability / authorization boundary:
DOM ownership of copy, controls, semantics, and next action:
Static / reduced-motion / unsupported-device fallback:
Loading / failure state:
Responsive reassembly:
Performance risks and measurable checks:
Approval state:
```

The selected medium must have an observable gain such as clearer containment, an unbroken before-to-after transformation, inspectable depth, more legible data density, or credible material evidence. `More immersive`, `premium`, `dynamic`, and `delightful` are not sufficient without a visible consequence.

DOM/CSS wins only after this comparison, not before it. WebGL, Three.js, shaders, Canvas, and video win only when their gain exceeds their runtime, accessibility, maintenance, authoring, and responsive cost.

## Progressive-enhancement boundary

An advanced renderer owns a bounded carrier layer, never the whole reading and action path.

- Keep headings, body copy, navigation, CTA, forms, and essential state in semantic DOM.
- Reserve carrier geometry before assets or scripts load so failure does not shift the page.
- Make the first static frame meaningful. Do not require autoplay or completed motion to explain an orphan shape.
- Provide an equivalent static or user-controlled state for reduced motion and unsupported devices.
- Preserve the claim and next action when loading fails; a poster frame or SVG fallback must be part of the approved composition.
- Pause continuous rendering when offscreen or hidden. Scale quality from measured device pressure instead of removing meaning at a generic tablet breakpoint.
- Bound pixel density, texture and asset weight, draw calls, memory, and main-thread coordination according to the current project budget. Measure on representative mobile hardware or an agreed proxy.
- Keep pointer and keyboard behavior intentional. Decorative rendering cannot intercept the controls layered around it.
- A new package, hosted asset, model, or service follows the active authorization rules; feasibility is not installation permission.

If a meaningful fallback cannot be authored, or the page's primary copy and action wait on the renderer, reject the advanced medium.

## Compare the smallest decisive scene

When two media remain credible, render only the actual-size Hero plus its next transition, or the one section where the difference is material. Hold these constant:

- content model and semantic invariant;
- verified facts and copy;
- carrier and composition bounds;
- color and component language;
- desktop and mobile target frames;
- fallback meaning.

Compare comprehension at rest, the added explanatory gain, every user-stoppable state, mobile reassembly, fallback quality, and runtime cost. Do not build parallel full pages or let one candidate gain stronger copy, a larger stage, or a more dramatic color climate.

## One representative choice

For `fragmented audio → connected retained note`, the content model is transformation and the carrier is a graphic grounded by a real product result.

- DOM/CSS is plausible for the surrounding claim, controls, and final note, but a field made from many decorative elements may become brittle and fail to preserve continuous motion.
- SVG is plausible when the fragments and routes are finite, crisp, and primarily two-dimensional.
- A DOM + WebGL or shader carrier becomes plausible when many fragments must continuously converge through one visible boundary and retain spatial coherence. It wins only if that continuity is easier to understand than the SVG version and a static SVG or product-state fallback carries the same claim.
- The following policy table remains semantic DOM; sharing a renderer across both screens would add cost without adding meaning.

This is a selection example, not a default recipe for audio pages.

## Common mistakes

| Mistake | Correction |
|---|---|
| `Graphic` becomes styled divs without a decision | Run the medium scan after the content model and carrier are fixed |
| “The project uses React” selects HTML/CSS | Treat React as the integration boundary; compare the carrier's plausible media |
| A fashionable shader or 3D demo becomes the concept | State the semantic invariant and observable gain before choosing the tool |
| One renderer is applied page-wide for consistency | Choose per decisive screen; keep coherence in composition, type, color, and behavior |
| Advanced media replace real copy or product evidence | Keep evidence and actions in DOM; let the renderer clarify one relationship |
| Desktop effect disappears on tablet or mobile | Author a reassembly or equivalent static/user-controlled carrier at the pressure point |
| Poster, loading, and reduced-motion states are afterthoughts | Approve them with the main carrier before implementation |
| Performance is asserted from library reputation | Capture project-specific runtime evidence at the actual rendered size |

## Quick reference

| Signal | First comparison |
|---|---|
| Stable reading, form, table, disclosure | DOM/CSS; add SVG only for a real relationship |
| Bounded vector topology or path | SVG vs DOM + SVG |
| Authentic or fixed art-directed evidence | Raster vs video if time is essential |
| Many 2D marks or drawing | Canvas 2D vs SVG |
| Procedural field or continuous deformation | WebGL/custom shader vs SVG/Canvas fallback |
| Inspectable depth, camera, or 3D object | Three.js/R3F vs a simpler 2D representation |
| Advanced carrier with readable page chrome | Hybrid DOM + selected renderer |

The goal is not renderer variety. It is to remove the silent HTML/CSS default and make every decisive screen earn the medium that represents its evidence best.
