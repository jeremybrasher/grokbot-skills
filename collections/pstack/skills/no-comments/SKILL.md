---
name: no-comments
description: "Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# No comments

## When to use

Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints.

**Do not use when:**
- The description trigger is not met
- Required inputs are unavailable and cannot be obtained
- A narrower skill better fits

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. A named object of work matching this skill
2. Inputs the domain recipe needs to start
3. Authority for any writes the recipe performs

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Object missing | Named object of work | One sentence from the user | I need the object. Holding. |
| Required input missing | That input | Obtain or ask | Name the gap. Do not guess. |
| Write authority missing | Explicit go-ahead | Ask | Read-only response or HOLD. |
| Trigger mismatch | Correct skill | Route away | Wrong skill. Holding. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Prefer reuse and deletion over new surface area
- Do not expand scope past the request
- Skip optional flourishes
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Polished guesses when inputs are missing
- Drive-by refactors
- Fabricated citations or evidence

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Intake complete or HOLD
- Domain recipe steps followed
- Outputs match what the recipe promises

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- The recipe default sequence changes which facts get attention first
- Structured outputs can create false completeness
- Automation defaults nudge later agents to repeat the same shape

What still needs a human: Whether to proceed past residual unknowns and any irreversible action.

## Method card — same family every run

A later agent runs this from this file alone.

1. Intake -> follow Domain recipe -> output check -> return result or HOLD.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Spawn Comment Sicko. Act on accepted findings.

Defer to Comment Sicko's fresh perspective.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Steps

1. Spawn `Task` with `subagent_type: "Comment Sicko"`. Pass the scope. Do not restate its rules.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, run `/how` or `/why` on their symbol. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. Reject a second, report it open, and fail `/no-comments`.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, run `/architect` once for the accepted set and surrounding code. Stop at the sketch. Architect shapes. Step 4 implements.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The **principle-fix-root-causes** and **principle-redesign-from-first-principles** skills guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise delete, report the constraint open, and sketch out-of-scope work.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.
