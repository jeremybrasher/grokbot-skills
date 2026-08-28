# grokbot-skills

Collection of agent skills shaped for [Grok Bot](https://cursor.com): one folder per skill, `SKILL.md` with `name` and a when-to-use `description`.

Sourced from the public directory [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills). Each skill keeps its original license and a `SOURCE.md` with the upstream URL. This is a collection, not a claim of authorship.

House skills that already live in Grok Bot (Brasher Criterion, Dune Contract, site-copy anti-slop, Schwartz channel) are not overwritten here.

## Layout

- `skills/` — one listed skill per folder
- `collections/` — listed packs that are themselves skill libraries
- `MANIFEST.json` — harvest result: copied, skipped, failed
- `COMPAT.md` — notes on Claude-Code-only hooks

## Use in Grok Bot

Copy a skill folder into the Grok Bot workflows library, or install it one at a time. Do not dump the whole shelf into the live catalog.

## Skip list

Offensive / exploit skills from the source list are not copied.

## Admission

Nothing ships into `skills/` or `collections/` until it clears [SCORING.md](SCORING.md). Raw copies land in `incoming/` first.

## Admitted

Only skills that clear AXIØM alignment at 90, with no HOLD and no veto. Raw harvest stays off this repo.

- `skills/buyer-eval` — 92.8 (2026-08-28)

- `skills/brainstorming` — 90.0 (2026-08-28)

- `skills/humanizer-ru` — 92.8 (2026-08-28)

- `skills/systematic-debugging` — 93.6 (2026-08-28)

- `skills/task-observer` — 92.8 (2026-08-28)

- `skills/vibe-creating-skill` — 90.8 (2026-08-28)

- `skills/test-driven-development` — 91.3 (2026-08-28)

- `skills/avoid-ai-writing` — 94.6 (2026-08-28)

- `collections/great-cto` — 93.0 (2026-08-28)

- `collections/notfair` — 95.3 (2026-08-28)
