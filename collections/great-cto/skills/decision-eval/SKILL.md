---
name: decision-eval
description: Spawns the decision-scorer agent after architect proposes 2+ variants in an ADR. Produces a weighted scoring table and recommended choice saved to docs/decisions/.
when_to_use: |
  Apply when:
  - architect has written an ADR with 2+ alternatives under ## Alternatives Considered or ## Options
  - architect is about to finalize a multi-variant decision and needs an objective tie-breaker
  - CTO explicitly requests scoring before gate:arch approval
  Do NOT apply when:
  - The change is a bug fix, docs-only, or style/formatting update
  - The ADR has only 1 option (no real alternatives)
  - User says "skip scoring" or "no scoring"
  - project_size is nano (overhead exceeds value)
  - A variant's argument cannot name mechanism, evidence, and consequence
    (unfalsifiable — skip the scorer; do not score it into a pick)
  - You would have to invent Option C or a missing alternative to have 2+
effort: medium
allowed-tools: Read, Glob, Bash, Agent
paths:
  - "docs/decisions/**"
  - "docs/architecture/**"
  - ".great_cto/PROJECT.md"
---

# Decision Eval — automated scoring for architectural alternatives

Invoke after architect proposes 2+ variants, before creating gate:arch.

## When to invoke

Invoke this skill when ALL of these are true:

1. An ADR (`docs/adr/ADR-*.md`) or ARCH doc (`docs/architecture/ARCH-*.md`)
   contains a section with 2 or more named alternatives (look for
   `## Alternatives Considered`, `## Options`, or bold-prefixed options like
   `**Option A:**`)
2. The architect has not yet created `gate:arch`
3. The user has not said "skip scoring", "no scoring", or "skip decision-eval"
4. `project_size` in PROJECT.md is NOT `nano`

Skip silently (do not even mention) if any condition fails. Skipping
means do not invent options to score. If someone asked for a
recommendation and the variants are missing or unfalsifiable, stop and
return the gap — do not wait hoping architect will fill it.

## How to invoke

Read the most recent ADR or ARCH doc to confirm 2+ variants exist, then spawn
the `decision-scorer` agent with the file path as context:

```bash
# Identify target document
TARGET=$(ls -t docs/adr/ADR-*.md 2>/dev/null | head -1)
[ -z "$TARGET" ] && TARGET=$(ls -t docs/architecture/ARCH-*.md 2>/dev/null | head -1)

# Confirm 2+ variants
VARIANT_COUNT=$(grep -cE "^\*\*[A-Za-z]|^### [A-Za-z]|^- \*\*[A-Za-z]" "$TARGET" 2>/dev/null || echo 0)
```

If `VARIANT_COUNT >= 2`, dispatch the agent:

```
Agent: decision-scorer
Context: <TARGET file path>
Task: Score the architectural variants in <TARGET> against .great_cto/PROJECT.md criteria.
      Save output to docs/decisions/.
```

## Output location

The decision-scorer agent saves results to:
```
docs/decisions/DECISION-<slug>-<YYYYMMDD>.md
```

After the agent completes, read the output file and surface the recommendation
to the architect:

```
Decision scoring complete:
  Recommended: <variant name> (<score>/5.00)
  Runner-up:   <variant name> (<score>/5.00)
  Full report: docs/decisions/DECISION-<slug>-<YYYYMMDD>.md

Architect: review the scoring rationale before accepting or overriding the recommendation.
```

## Skip conditions

Output nothing and proceed to the next step if:
- `project_size: nano` in PROJECT.md
- Fewer than 2 variants found in the ADR/ARCH doc
- User message contains "skip scoring" or "skip decision-eval" or "no scoring"
- The target document is a bug-fix or docs-only ADR (check title for "fix:", "docs:", "chore:")
- A named variant's argument lacks mechanism + evidence + consequence
  (you cannot say what would make it wrong). Unfalsifiable arguments
  cannot be scored into a pick and cannot block `gate:arch`.
- Scoring would require inventing a third option or filling a missing
  alternative. Do not mint a variant to admit the scorer.

If the CTO asked for a scored pick and you skipped because evidence is
missing, return that gap. Do not open `gate:arch` on an empty or
unfalsifiable choice set.

## Integration with architect workflow

This skill sits between Step 4 (Write ADR) and Step 5 (Create gate:arch) in
`agents/architect.md`. Architect invokes it by name:

```
Invoke skill: decision-eval
```

After scoring completes, architect may:
- Accept the recommendation → proceed to gate:arch with the recommended option
- Override the recommendation → document rationale in the ADR under a new
  `## Scoring Override` section before creating gate:arch

The score is a measurement. It frames the CTO's next words at
`gate:arch`. Do not treat a post-score "yes" as if it were the original
variant the architect wrote. If you need the original pick, ask for it
separately from the scoring table.

This skill does not invent a new decision category. It scores variants
already written in the ADR. A later agent runs the same skip rules even
if `docs/decisions/` is empty or last month's DECISION-*.md is gone —
the method is the conditions above, not the growing file.
