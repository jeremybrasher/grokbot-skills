# What we did with pstack

**Date:** 2026-09-15 (America/Chicago)  
**Stopgate:** PRIME  
**Instrument:** AXIØM skill alignment (`SCORING.md` / `axi-m-skill-alignment`)  
**Source:** Cursor plugin `pstack` (read-only cache)  
**Work root:** `/workspace/grokbot-skills/incoming/pstack/`

## Intent

Jeremy asked PRIME to analyze the pstack skills through the AXIØM lens and upgrade them. The plugin files stay managed by Cursor install/uninstall. We scored what each recipe actually does when run, upgraded every skill that failed the gate, and held repo admission until Jeremy cleared the stopgate.

## What pstack is here

pstack is poteto’s Cursor plugin pack: operational skills (`poteto-mode`, `setup-pstack`, `swarm`, `arena`, `tdd`, `unslop`, …), a large principles set, and Benny automation skills (triage, reproduce-and-fix, setup-benny). Fifty `SKILL.md` files in total from that cache.

## Gate we used

Seven weighted dimensions to 100:

| Key | Weight | What it measures |
|---|---|---|
| OFI | 20 | Observe first — real intake before generation |
| HD | 18 | HOLD discipline — named pause conditions and what returns instead of a guess |
| DBC | 16 | Delete before create — cut, reuse, refuse unless expansion is evidenced |
| NRC | 15 | Noise refusal — named slop it will not produce; at least one output check |
| RWR | 13 | Recurrence without rot — self-contained; same family on a later run |
| MT | 10 | Method transmission — the user can carry the method, not only the artifact |
| OEA | 8 | Observer effect — what the recipe itself distorts; what still needs a human |

Rules that mattered:

- Unevidenced dimension → **HOLD** (no invented 0 or 5). Any HOLD blocks repo entry.
- OFI = 0 or HD = 0 → **veto**.
- Under 80 stays in the work pipeline. Repo admit only at **composite ≥ 90**, no HOLD, no veto.
- Upgrades may add observe-first intake, HOLD exits, delete-first defaults, a refuse list, and a when-to-use description.
- Upgrades must not write the AXIØM cycle or operator names into the customer-facing recipe, costume-map the structure, or change the skill’s domain purpose.

## Pass 1 — originals

Every leaf under `skills/*/SKILL.md` and `automations/benny/skills/*/SKILL.md` was scored into `scores.jsonl` and ranked in `SCOREBOARD.md`.

**Counts**

| Bucket | Count |
|---|---|
| Scored | 50 |
| With ≥1 HOLD | 14 |
| Vetoes | 0 |
| Composite under 80 | 36 |
| Composite 80–89 | 0 |
| Composite ≥90 | 0 |

**Strongest originals (still below the gate)**

| Skill | Composite |
|---|---|
| `tdd` | 73.0 |
| `triage-issue-reports` | 72.9 |
| `why` | 70.8 |
| `poteto-mode` | 69.7 |
| `reproduce-and-fix-issues` | 69.5 |

**Weakest originals (multiple HOLDs or thinnest evidence)**

- `bro` — short restatement; HOLDs on HD / DBC / OEA  
- `principle-experience-first` — values statement; HOLDs on OFI / HD / OEA  
- `principle-outcome-oriented-execution` — thin phase advice; HOLDs on OFI / HD / OEA  
- `typescript-best-practices` — checklist without intake or pause  
- `how` — walkthrough without named HOLD exits or observer-effect

**Dominant pack gaps**

Observer-effect (OEA) was missing or thin on most leaves. Formal observe-first intake and HOLD return tables were thin on many. Delete-before-create was already stronger where laziness, subtract, and unslop lived in the original text.

Nothing in the original pack cleared 90. Everything entered the upgrade pipeline.

## Pass 2 — upgrades

Each skill was rewritten into `upgraded/<slug>/SKILL.md` with:

1. Clear when-to-use / do-not-use  
2. Intake checklist before work  
3. HOLD table (condition → missing → needs → return instead)  
4. Cut-first defaults for that operation  
5. Explicit refuse list  
6. At least one output check before return  
7. A short observer-effect note (what the recipe distorts; what stays human)

Domain purpose stayed the same. AXIØM cycle language stayed out of the recipes.

Rescores landed in `scores-after.jsonl` and per-skill `SCORE.json` beside each upgraded file.

**After upgrade**

| Metric | Value |
|---|---|
| Skills | 50 |
| HOLDs | 0 |
| Vetoes | 0 |
| Floor composite | 90.0 |
| Ceiling composite | 95.4 (`unslop`) |
| Mean composite | ~90.9 |

Highest after harden: `unslop` (95.4), then `poteto-mode`, `tdd`, `why`, Benny `reproduce-and-fix-issues` and `triage-issue-reports` (93.8). A large band of principles lands at exactly 90.0 — enough evidence to clear the gate after scaffolding, still thinner domain meat than the operational core.

## Stopgate and Jeremy’s call

PRIME held the GitHub copy. Plugin cache was never edited. Artifacts stayed under `incoming/pstack/`.

Jeremy was offered:

1. Admit operational core first  
2. Admit all 50 upgraded  
3. Hold for spot-check  

**Decision:** admit all 50 upgraded pstack skills into `jeremybrasher/grokbot-skills`.

Admission shape (in progress / next): collection pack under `collections/pstack/` (same pattern as `notfair` / `great-cto`), with each upgraded leaf as `skills/<slug>/`, plus pack `SOURCE.md`, `LICENSE`, `SCORE.json`, and this record. Individual top-level `skills/` entries that already exist under other names (e.g. obra TDD) are not overwritten; pstack `tdd` lives inside the collection.

## Artifact map

| Path | What it is |
|---|---|
| `REPORT.md` | Counts, gaps, recommended admit list |
| `SCOREBOARD.md` | Ranked originals + after tables |
| `scores.jsonl` | Attempt 1 scores |
| `scores-after.jsonl` | Attempt 2 scores |
| `upgraded/<slug>/SKILL.md` | AXIØM-aligned recipe |
| `upgraded/<slug>/SCORE.json` | Per-skill before/after + composite |
| `WHAT-WE-DID.md` | This narrative |

## One-line summary

We read fifty pstack skills as recipes, found none ready for the AXIØM repo gate, upgraded every one until each cleared ≥90 with no HOLD and no veto, kept the plugin originals untouched, and Jeremy ordered the full upgraded pack into grokbot-skills.
