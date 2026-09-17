---
name: brand-design
description: Orchestrate professional brand and visual design work for logos, VI systems, company brochures, catalogs, key visuals, posters, product/effect images, campaign assets, art direction, AI-image workflows, design review, and print handoff. Use as the default entry point when a design brief spans multiple visual disciplines or when the user is unsure which specialist workflow to use.
---

# Brand Design

Treat this as the team entry point and router.

## Load

Read `../../rules/brief-intake.md`, `../../rules/visual-quality.md`, `../../rules/asset-rights.md`, and `../../rules/delivery.md` as needed. Load only relevant specialist skills.

## Procedure

1. Inspect the supplied brief, files, images, references, brand assets, source copy, output medium, dimensions, and vendor constraints.
2. Extract the smallest useful design brief. Ask only for missing information that can materially change the direction or correctness; otherwise proceed with explicit assumptions.
3. Route the work:
   - logo / mark / lockup -> `logo-design`
   - VI / guidelines -> `brand-identity`
   - brochure / catalog / booklet -> `brochure-design`
   - KV / poster / effect image -> `visual-concept`
   - moodboard / visual thesis -> `art-direction`
   - generation prompt -> `image-prompt`
   - critique -> `visual-review`
   - prepress -> `print-production`
4. For open-ended exploration, develop 2-3 genuinely different directions. Vary idea, composition, type language, image language, material, and emotional register; do not present color swaps as separate concepts.
5. Explain each direction in commercial terms: what it communicates, who it suits, what makes it recognizable, and where it may fail.
6. If the user has already selected a direction, do not restart exploration. Develop the chosen direction into a coherent system.
7. Produce the highest artifact level the current toolchain actually supports: direction, specification, generated draft, editable source, or vendor-ready output. State the level honestly.
8. Run a separate `visual-review` pass before final handoff when the work is substantial.

## Deliverables

Adapt to the task, but normally include: brief summary, creative direction, visual system, production/application notes, created artifacts or file plan, review findings, and unresolved decisions.

## Failure conditions

Do not fabricate business facts or assets. Do not claim a prompt is an image, a mockup is a finished identity, or a PDF is print-ready without the relevant checks.
