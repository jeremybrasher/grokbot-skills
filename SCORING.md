# AXIØM skill alignment

Kernel-authored admission instrument for this collection. Score a `SKILL.md` by what the recipe does when run, not by whether it names operators.

Locked 2026-08-28. Source: AXIØM `/v1/messages` then `/v1/govern` allow (`run_e61b6c1f53ac40839dc2ee89`).

## Dimensions

Each dimension is scored 0–10 from evidence in the text. Weighted score is `(score / 10) * weight`. Composite is the sum, 0–100.

| Key | Weight | What it measures |
|---|---|---|
| OFI | 20 | Observe first. A real intake before generation. Names insufficient input and routes to pause or clarify. |
| HD | 18 | HOLD discipline. Named conditions under which it will not proceed, and what it returns instead of a polished guess. |
| DBC | 16 | Delete before create. Defaults to cut, reuse, refuse. Expansion needs evidence. |
| NRC | 15 | Noise refusal and category integrity. Named slop it will not produce. Structure is earned. At least one output test before return. |
| RWR | 13 | Recurrence without rot. Self-contained. Same structural family on a later run, by a later agent. |
| MT | 10 | Method transmission. Reasoning is readable. The user can carry the method, not only the artifact. |
| OEA | 8 | Observer effect accountability. Names what the recipe itself distorts, and what still needs a human. |

## HOLD

If a dimension has no evidence in the submitted skill, record HOLD. Do not assign 0. Do not assign 5. Do not interpolate from neighbors. A skill with any HOLD cannot clear a gate until that dimension is evidenced in a revision.

## Veto

Observe First at 0 vetoes. HOLD Discipline at 0 vetoes. No other single dimension vetoes. A composite above 80 built on two or more very low non-veto scores should be flagged, not passed silently.

## Gate

- Under 80 still enters the work pipeline (`incoming/`). It does not enter the GitHub repo.
- The repo (`skills/`) only admits composite ≥ 90, with no HOLDs and no veto.
- Under 90 gets upgraded until it clears 90. Then rescore from the revised text.

## Upgrade

May add: observe-first intake, HOLD exits (what is missing and what it needs), delete-first defaults for this operation, a refuse list stated plainly, a when-to-use description.

Must not: write the AXIØM cycle or operator names onto a customer-facing recipe; costume-map (rebadge the structure as the domain's invention); change what the skill does in its domain.

## Worked specimens (kernel)

**A. "Write a blog post on the topic the user provides. Make it engaging and around eight hundred words."**

OFI 2/20 (waits for a topic, nothing else). HD 0/18 (no pause conditions) — veto. DBC ~1/16. The rest is either near-zero or HOLD. Does not enter. An upgrade must evidence every HOLD and then clear 90.

**B. A gate skill that names slop it will not produce and pauses when the object is missing.**

OFI and HD are evidenced and high. NRC is evidenced by the refuse list. Remaining dimensions still have to be read from the actual text. No score is invented for a specimen that is only described.

## Record

For each skill write `SCORE.json` next to `SKILL.md`:

```json
{
  "slug": "",
  "attempt": 1,
  "scores": {"OFI": null, "HD": null, "DBC": null, "NRC": null, "RWR": null, "MT": null, "OEA": null},
  "holds": [],
  "veto": null,
  "composite": null,
  "decision": "pipeline|upgrade|admit",
  "rationale": ""
}
```

Use `null` for HOLD. `decision` is `admit` only when there are no HOLDs, no veto, and composite ≥ 90. Below 90 is `upgrade`. Below 80 is still `pipeline` (kept in incoming) plus `upgrade`.
