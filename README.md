# Codex Brand & Visual Design Skills

A Codex-native skill suite for brand identity and commercial visual design work: logos, VI systems, company brochures, key visuals, campaign imagery, art direction, AI image prompting, design review, and print-production handoff.

The default team entry point is `$brand-design`. Designers should not need to learn every specialist skill.

## Quick start

```text
$brand-design
Help me create a visual direction for this company brochure.
First inspect the brief, audience, existing brand assets, content, format, and production constraints.
Give me three genuinely different directions, recommend what each direction is best for, then develop the selected direction into a page system and handoff spec.
```

## Skill map

```text
brand-design        orchestrator / default entry point
logo-design         logo concepts, lockups, reduction, vector-ready handoff
brand-identity      color, typography, imagery, grid, icon and application system
brochure-design     company brochure, catalog, booklet and editorial layout system
visual-concept      KV, campaign visual, poster, product/effect-image direction
art-direction       moodboard, visual thesis, reference language and shoot/render direction
image-prompt        production-ready prompts for image generation/editing workflows
visual-review       evidence-based critique and correction priorities
print-production    prepress, bleed, color, resolution and printer handoff checks
```

## Design principles

- Start from business purpose, audience, medium, brand character, and production constraints before choosing aesthetics.
- Prefer distinct creative directions over shallow style variations.
- Separate concept, generated imagery, editable source, and print-ready output. Never claim an artifact exists if it was not actually created.
- Use references to understand visual grammar, not to trace or reproduce protected logos, artwork, or distinctive trade dress.
- Judge commercial design by clarity, recognition, hierarchy, consistency, usefulness, and production fitness, not by novelty alone.
- Treat AI-generated imagery as source material that still requires selection, retouching, typography, composition, and human art direction.

## Repository structure

```text
AGENTS.md
.agents/
  rules/              shared design rules
  skills/             Codex Agent Skills
scripts/              lightweight validation
 docs/                 team usage and baseline notes
```

## Status

`v0.1.0-dev` — first usable team baseline. It intentionally focuses on repeatable workflow and quality gates before adding large reference libraries or company-specific brand assets.
