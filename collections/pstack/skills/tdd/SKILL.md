---
name: tdd
description: "Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is unclear, expensive, integration-heavy, or not requested. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# TDD Bug Fix

## When to use

User explicitly asks for TDD / failing / regression test, OR the bug has an obvious cheap local test target.

**Do not use when:**
- Test path unclear, expensive, integration-heavy, or not requested
- Only manual/scripted verification is practical
- Feature work with no failing behavior named

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Named bug or intended-vs-actual behavior
2. A candidate cheap executable check path, or an explicit skip reason
3. Authority to edit tests and production code

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Bug unnamed | Intended and current behavior | One sentence each | I need the behavior delta. Holding. |
| No cheap test path and user insisted on TDD | A practical executable check | Narrower target or alternate verification | State why a failing test is impractical. Do not invent a bad test. |
| Failing-before not demonstrated | Red evidence | Fix the test/repro first | Do not edit production code yet. |
| Would weaken assertions to match wrong code | Correct expected behavior | Product confirmation of behavior change | Holding. Will not weaken the test. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Smallest focused regression test
- Prefer no new test over a bad test
- Smallest production change
- No broad fixture churn
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Tests that mostly assert mocks
- Changing tests to match a wrong implementation
- Silent skip of the regression step
- Expensive harness for a small fix when not requested

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Failing-before evidence named, or explicit impracticality + alternate check
- Passing-after evidence named
- Nearby validation mentioned when risk is broader

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- The first cheap test target can become the whole bug story
- Requiring red-green can delay a verified one-line fix
- Sibling coverage expansion can balloon the PR

What still needs a human: Whether the cheap local target is the right object, and whether to skip TDD for cost.

## Method card — same family every run

A later agent runs this from this file alone.

1. Understand bug -> choose narrow check -> red -> fix -> green -> nearby validation -> report evidence.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

When fixing a bug with a clear, cheap test path, make the broken behavior executable before changing production code. The goal is a focused regression test that fails before the fix and passes after it.

Do not force a test when it would be impractical. If the available test would require broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state, vague reproduction steps, or large unrelated fixture churn, skip adding a new test and use the closest useful verification instead.

## Workflow

1. **Understand the bug.** Identify the intended behavior, current behavior, affected path, and smallest observable reproduction.
2. **Choose the narrowest executable check.** Prefer the closest unit, component, integration, or regression test already used for that codepath. If no practical test path is obvious, do not create one from scratch just to satisfy the workflow.
3. **Write the failing test first.** Add the smallest focused test that would have caught the bug. The test should encode intended behavior, not mirror the current implementation.
4. **Run the new test before fixing.** Confirm it fails for the intended reason. If it passes or fails for an unrelated reason, correct the test or reproduction before editing the implementation.
5. **Fix the bug.** Make the smallest production change that satisfies the intended behavior while preserving nearby contracts.
6. **Rerun the regression test.** Confirm the test now passes.
7. **Run nearby validation.** Run relevant adjacent tests, type checks, lint, or scenario checks when the change has broader risk.

## If a Failing Test Is Impractical

Do not silently skip the regression step. Before fixing, explicitly explain why a failing test is impossible or not worth the cost, then choose the closest executable regression check available. Examples include a targeted script, manual reproduction command, browser automation, snapshot comparison, log assertion, or focused integration check.

Prefer no new test over a bad test. A bad test is one that mostly tests mocks, encodes current implementation details, depends on timing or unrelated global state, needs expensive infrastructure for a small fix, or would be deleted immediately after proving the fix.

## Guardrails

- Do not change tests merely to match a wrong implementation.
- Do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.
- Keep the regression test focused on the bug. Avoid broad fixture churn or unrelated coverage expansion.
- Do not add tests when the practical signal is weak. Use manual or scripted verification and say why.
- If the bug is flaky, make the test deterministic where possible and document the signal being locked down.
- If the bug exposes a broader class of failures, first land the focused regression path, then consider additional sibling coverage.

## Final Response

Report the evidence, not just the outcome:

- Name the failing-before test or executable check and the failure it produced.
- Name the passing-after test run and any nearby validation performed.
- If failing-before evidence could not be demonstrated, state why and describe the closest regression check used instead.
