# Online formats — capability map

Generic guidance for producing Tiro online marketing assets with this skill. It describes what this skill can produce directly, what needs a real implementation surface, and how static, editable, and runtime outputs differ. It carries no campaign, channel-history, or internal source data; confirm the actual destination, dimensions, and format through intake.

## Static vs editable vs runtime

These are different kinds of output and must not be conflated:

- **Raster static** — PNG / JPG. A flat exported image at fixed pixels. Good for most image placements. The size is whatever you export; it is not an inherent spec of any channel.
- **Editable vector / markup** — SVG or HTML/CSS. Editable, scalable, and composable. An SVG or an HTML *graphic* is still a graphic asset, not a shipped channel surface.
- **Actual implementation surface** — a real email HTML build, or a real product/in-app popup implementation. This is **not** the same as an editable graphic. It involves the destination's own layout, delivery, and runtime constraints, and is a separate implementation scope. Do not treat "make the graphic" and "implement the email/popup" as one deliverable unless both were requested.

A single source graphic can be adapted across several placements, but adapting a graphic is not the same as building the channel surface that hosts it.

## What this skill can produce directly

- Static raster images (PNG / JPG) at a confirmed size.
- Editable vector (SVG) and HTML/CSS graphic compositions, rendered locally.
- A static **cover frame or keyframe** for a motion piece, exported as an image.

## What needs more than a graphic

- **Full motion video (MP4).** A finished video requires the runtime or project source, the fonts, any audio, and current verified source material. Without those, produce a static cover or keyframe instead and state that the full render is out of scope until the source and assets are available. Do not assume a resolution, aspect ratio, fps, or duration — confirm them.
- **Real email HTML** and **real in-app / product popups.** These are implementation surfaces with their own layout and delivery rules. The skill can produce the graphic or editable layer they host; building the surface itself is a separate, explicitly scoped task.

## Dimensions and specs are confirmed, not assumed

- Export dimensions come from intake. If only the destination is known, propose dimensions as clearly labeled assumptions and confirm before the final export.
- A size that appears in a brief or request is a *requested* size, not a verified published spec. A size this skill previously generated is its own output, not a precedent.
- Any platform-standard dimensions you suggest for short vertical video or similar formats are **suggestions**, offered as such, not platform-verified facts. Mark them as proposals and confirm.

## Paired versions

By default, the same message is delivered in both a product-present and a brand-only version in the same chosen format (see the skill's paired-version section). The brand-only version is recomposed as its own purposeful graphic, not the product version with the screenshot removed. If there is no verified latest-production capture, deliver the brand-only version and report the product-present one as blocked pending a real capture; never use a placeholder or an old prototype as the final product version.
