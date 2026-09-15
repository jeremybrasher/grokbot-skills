---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Swarm

## When to use

Fan out N parallel workers for coverage, races, gauntlets, or exploration. /swarm, swarm this.

**Do not use when:**
- A single sequential investigation suffices
- No done predicate can be stated
- Workers would write the same shared path without separation

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Done predicate and return artifact shape
2. Shape: partition, race, or mix — and N
3. Worker model choice (rule or default)

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| No done predicate | Falsifiable done | One sentence predicate | Frame incomplete. Holding fan-out. |
| N unset and not derivable | Worker count | User N or shape-derived N | Ask N. Do not spawn. |
| Shared writable output for writers | Per-worker output paths | Separate paths/worktrees | Holding. Separate before serializing shared state. |
| All workers blocked/drop out | At least one result | Retry, reshape, or abort | Report BLOCKED. Do not invent consolidated success. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Do not paste raw worker dumps
- Compact table + one-line issues only
- Proceed with N-1 on dropout; do not respawn endlessly
- Do not expand scope mid-swarm without reframing
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Fan-out without a done predicate
- Fake PASS when workers were BLOCKED
- Averaging contradictory race results without a declared rule

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Phases completed or HOLD before fan-out
- Selection rule applied if race
- Gaps/dropouts explicit

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Partition boundaries invent seams that may not match the problem
- First-pass race rules favor speed over quality
- Aggregation discards dissenting detail

What still needs a human: Whether N and shape are worth the cost, and final call on conflicting findings.

## Method card — same family every run

A later agent runs this from this file alone.

1. Frame -> fan out -> aggregate -> one report. HOLD if frame incomplete.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Fan out N parallel cloud workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the cloud concurrency limit.
4. Pick the worker model from `swarm workers` in `~/.cursor/rules/pstack-models.mdc` when present. Otherwise use `grok-4.6-fast-xhigh`. For a model race, name each arm's model up front.
5. Give each worker its own writable output when it writes.

## Phase B: Fan out

Spawn all N workers in one message with `subagent_type: generalPurpose`, `environment: "cloud"`, `run_in_background: true`, and the configured model. Use `environment: "local"` only when the worker needs access to something on the user's computer.

When a worker must start from a non-default pushed branch, pass `cloud_base_branch`.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
