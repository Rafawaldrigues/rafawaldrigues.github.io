---
name: "Rafael Guerra Waldrigues Portfolio"
description: "An evidence-first portfolio for mobile security, reverse engineering, and the full stack foundation beneath them."
colors:
  examination-cyan: "#58d4e0"
  annotation-orange: "#ff6a00"
  graphite-ground: "#142121"
  frost-ink: "#ededed"
  heading-frost: "#edf1f2"
  body-mist: "#9fb0b3"
  glass-line: "#5c747c"
  muted-cyan: "#72a7af"
  hairline: "rgba(175, 218, 224, 0.55)"
  panel-wash: "rgba(12, 30, 33, 0.22)"
typography:
  display:
    fontFamily: "Signika Negative, system-ui, sans-serif"
    fontSize: "clamp(36px, 5vw, 72px)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: "normal"
  headline:
    fontFamily: "Signika Negative, system-ui, sans-serif"
    fontSize: "clamp(34px, 4vw, 58px)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Signika Negative, system-ui, sans-serif"
    fontSize: "clamp(22px, 2.08vw, 32px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "0.04em"
  body:
    fontFamily: "Signika Negative, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  label:
    fontFamily: "Signika Negative, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: "0.09em"
rounded:
  technical: "3px"
  control: "5px"
  dot: "50%"
spacing:
  xs: "6px"
  sm: "12px"
  md: "18px"
  lg: "24px"
  xl: "34px"
  section-mobile: "78px"
  section-desktop: "116px"
components:
  header-action-primary:
    textColor: "{colors.examination-cyan}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "36px"
  header-action-secondary:
    textColor: "{colors.heading-frost}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "36px"
  primary-nav:
    textColor: "{colors.heading-frost}"
    padding: "0"
  text-link:
    textColor: "{colors.heading-frost}"
    padding: "0 0 6px"
  evidence-node:
    backgroundColor: "{colors.panel-wash}"
    rounded: "{rounded.technical}"
    padding: "0 13px"
    height: "46px"
  evidence-rail:
    textColor: "{colors.heading-frost}"
    padding: "36px 4%"
  project-study:
    textColor: "{colors.body-mist}"
    padding: "72px 6% 66px 0"
---

# Design System: Rafael Guerra Waldrigues Portfolio

## Overview

**Creative North Star: "Mesa de luz"**

The portfolio behaves like software examined on a museum-conservation light table: a cool graphite field supports one dominant frosted evidence slab, and thin rules make claims feel traceable rather than ornamental. The central “Lâmina central” is the signature expression of this surface, not a requirement that every future page copy its composition.

The character is direct, technical, honest, curious, and understated. Evidence appears before adjectives; cyan reveals structure and interaction, while orange marks the one path or status that deserves attention. Material grain, translucency, and exact registration create refinement without “muito fru-fru.”

**Key Characteristics:**

- Cool graphite ground with frosted, translucent evidence surfaces.
- Restrained cyan examination light and a single orange annotation voice.
- Fine rules, registration geometry, and compact technical labels.
- Clear field-of-study positioning with no inflated expertise claims.
- Dense evidence on wide screens that becomes an orderly vertical sequence on mobile.
- Motion behaves like examination: plates register into place, light follows the pointer, and evidence paths develop only when inspected.

## Colors

The palette is a cool, low-luminance laboratory field whose two accents carry distinct semantic jobs.

### Primary

- **Examination Cyan** (`examination-cyan`): Reveals links, active navigation, focus, progress, and the connective structure of an analysis.

### Secondary

- **Annotation Orange** (`annotation-orange`): Marks one selected finding, active trace, or in-progress status; its rarity supplies emphasis.

### Neutral

- **Graphite Ground** (`graphite-ground`): The page ground and the base under material grain.
- **Frost Ink** (`frost-ink`): Default high-contrast copy on graphite.
- **Heading Frost** (`heading-frost`): Primary headings and feature names.
- **Body Mist** (`body-mist`): Explanatory copy that should recede behind evidence and titles.
- **Glass Line** (`glass-line`): Structural rules and the edges of translucent plates.
- **Muted Cyan** (`muted-cyan`): Metadata and technical labels that need affinity with the primary accent without competing with it.
- **Hairline** (`hairline`): The brightest reusable cool divider.
- **Panel Wash** (`panel-wash`): A translucent fill for evidence nodes over the textured ground.

### Named Rules

**The Two-Ink Rule.** Cyan explains the examination system; orange identifies the exceptional active path. Do not use both as equal decoration.

**The Evidence Contrast Rule.** Headings stay frosted and bright, supporting copy stays misted, and metadata recedes further so scanning order remains visible without extra ornament.

## Typography

**Display Font:** Signika Negative (with system UI and sans-serif fallbacks)

**Body Font:** Signika Negative (with system UI and sans-serif fallbacks)
**Label/Mono Font:** Signika Negative; no separate monospace face is part of the shipped system.

**Character:** Signika Negative gives the portfolio a practical technical voice with enough softness to avoid terminal cosplay. The hierarchy relies on scale, spacing, and restrained tracking rather than a decorative font pairing.

### Hierarchy

- **Display** (400, `clamp(36px, 5vw, 72px)`, 0.95): Major project names and the most prominent evidence titles.
- **Headline** (400, `clamp(34px, 4vw, 58px)`, 0.98): Section openings and contact statements.
- **Title** (400, `clamp(22px, 2.08vw, 32px)`, 1.05): Feature labels such as the central analysis title.
- **Body** (400, 17px, 1.55): Project explanations and supporting narrative; keep reading measures near the observed 54ch maximum where possible.
- **Label** (400, 13px, 0.09em tracking): Dates, statuses, facts, and technical metadata; uppercase is reserved for compact metadata, not ordinary prose.

### Named Rules

**The One-Face Rule.** Stay within Signika Negative and create hierarchy through scale, weight, rhythm, and contrast; do not introduce a display face merely to make the portfolio feel more “designed.”

**The Honest Label Rule.** Uppercase tracking signals metadata or state, never a promotional eyebrow above every section.

## Layout

The first viewport is a bounded evidence field: the hero caps at 1536px and uses the approved 1536:1024 composition, with a slim absolute header above one central slab. Long-form sections use a content shell capped at 1280px with 64px side clearance on wide screens, 32px at the intermediate breakpoint, and 20px on mobile.

Desktop sections use deliberate asymmetric grids: headings and explanations split at roughly 1.25:0.9, featured project copy uses three columns, and paired studies share one ruled row. Section rhythm is spacious (116px vertically) and contracts to 78px on mobile. At 1100px, complex grids simplify; at 720px, navigation and secondary evidence plates yield to a single vertical reading order. The central slab remains visible, while the attack path becomes four stacked rows and decorative connectors are removed.

**The Slab-Then-Sequence Rule.** Preserve one dominant evidence surface in the first viewport, then let subsequent sections read as ruled records rather than a wall of independent cards.

## Elevation & Depth

Depth is material, not theatrical. The hero earns dimensionality from layered translucent raster plates, frost, grain, and cool edges. Content sections are flat and separated by tonal washes and 1px rules; conventional floating-card shadows are absent. The only live shadow treatments are the hero title’s subtle highlight (`0 1px 0 rgba(255,255,255,0.24)`) and the active evidence node’s restrained inset orange glow (`inset 0 0 16px rgba(255,106,0,0.05)`).

### Shadow Vocabulary

- **Frost Highlight** (`0 1px 0 rgba(255,255,255,0.24)`): A narrow top-lit edge on the hero name only.
- **Active Trace Inset** (`inset 0 0 16px rgba(255,106,0,0.05)`): A nearly imperceptible material response inside the selected evidence node.

### Named Rules

**The Tonal-Not-Floating Rule.** Establish depth with translucency, overlap, texture, and ruled separation; do not add generic drop shadows to section containers.

## Shapes

The form language is square and technical. Evidence nodes use gently clipped 3px corners, header controls use a restrained 5px radius, and most structural containers remain square. One-pixel cool borders, short registration ticks, and precise connector lines do most of the shaping. Full circles are reserved for tiny connector endpoints, not for badges or ornamental bubbles.

**The Technical Corner Rule.** Keep controls between square and 5px; larger friendly-card rounding would break the light-table material language.

## Components

### Header Actions

- **Shape:** Compact outlined controls with gently clipped corners (5px) and a 36px minimum height.
- **Primary:** Cyan text and cyan border on a transparent ground, with horizontal padding (18px).
- **Secondary:** Frosted text with a muted cool border.
- **Hover / Focus:** Hover adds a very light cyan wash; keyboard focus uses a 2px cyan outline offset by 4px. Color and border changes run for 160ms with standard ease.

### Navigation

- **Style:** A quiet horizontal text row with generous 38px gaps on wide screens.
- **State:** Hover and `aria-current` use Examination Cyan. The row is removed below 720px so the brand and GitHub action remain legible.

### Motion

- **Focal sequence:** On entry, the evidence sheets register into place, the copy resolves, and one scan crosses the central slab. The whole authored moment finishes within 1.4 seconds.
- **Continuity:** Fine-pointer movement shifts the layered plates by no more than 10px and moves the examination light without changing the reading order.
- **Evidence:** Diagram nodes expose in a short capped stagger; below-fold evidence rails and register bars develop only when their record enters the viewport.
- **Reduced motion:** Registration, scanning, path drawing, and pointer displacement are removed. Color, focus, and content hierarchy remain intact.

### Cards / Containers

- **Corner Style:** Project studies and content records remain square; only evidence nodes use the 3px technical corner.
- **Background:** Mostly transparent over Graphite Ground, with selective translucent washes for the about section, toolkit, nodes, and evidence rail.
- **Shadow Strategy:** Follow the Tonal-Not-Floating Rule.
- **Border:** One-pixel cool rules define rows, columns, and grouping.
- **Internal Padding:** Project studies use a spacious desktop inset and collapse to a 56px vertical rhythm on mobile.

### Evidence Nodes

- **Style:** Translucent graphite cells with a cool border, three short internal evidence bars, and a 3px radius.
- **Active State:** The border and leading evidence bar switch to orange, with the restrained inset trace glow.
- **Behavior:** Desktop nodes connect across four analysis stages; mobile keeps the nodes but removes crossing connectors to preserve legibility.

### Evidence Rail

- **Style:** A lightly washed horizontal process line with cyan endpoints and one orange active segment.
- **Responsive State:** It remains one sequence on mobile and becomes horizontally scrollable instead of wrapping into an ambiguous path.

### Text Links

- **Style:** Frosted inline text with a cyan bottom rule and 6px lower breathing room.
- **Hover / Focus:** Hover changes the text to cyan; keyboard focus inherits the global cyan outline.

## Do's and Don'ts

### Do:

- **Do** lead with a concrete artifact, trace, project fact, or source relationship before applying evaluative language.
- **Do** keep cyan structural and interactive, and reserve orange for one active finding, status, or path.
- **Do** use fine rules, tonal washes, and translucency to group dense technical information.
- **Do** preserve the explicit “field of study” positioning whenever mobile security and reverse engineering lead the page.
- **Do** linearize evidence on narrow screens and remove connectors that would cross or obscure content.
- **Do** use finite motion to reveal registration, inspection, or evidence; keep ordinary body copy immediately available.

### Don't:

- **Don't** turn the interface into a neon hacker terminal or a conventional split-hero portfolio.
- **Don't** describe learning-stage work as expert authority, commercial proof, or unverified proficiency.
- **Don't** add large radii, pill-heavy UI, glossy gradients, or generic floating-card shadows.
- **Don't** use orange as a second general-purpose brand color; it is a scarce annotation.
- **Don't** promote the hero’s exact plate coordinates or registration offsets into a universal layout recipe.
