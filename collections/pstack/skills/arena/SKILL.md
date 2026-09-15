---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Arena

## When to use

Spawn N parallel candidates at the same task, pick a base, graft winners from losers. Non-trivial artifact where one attempt locks the wrong shape.

**Do not use when:**
- Mechanical work with a settled shape
- Cannot state an artifact or rubric
- Budget cannot afford N candidates

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Artifact each candidate must produce
2. 3-6 gradeable rubric criteria for this task
3. Runner set and isolated output paths

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Artifact unnamed | What candidates produce | One sentence artifact | Holding fan-out. |
| Rubric under-specified | Gradeable criteria | Tighten rubric | Reframe. Do not spawn. |
| Wild divergence after run | Adequate Phase A prompt | Reframe and re-run | Do not average divergence. |
| Verify fails and no missed graft | A coherent base | Reframe or return to graft | Do not paper over. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Graft one or two things per loser, not most of it
- Prefer cleaner boundary / smaller API on ties
- No mechanical paste
- Skip second arena on settled design
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Holistic vibe pick without criterion scores
- Shipping unverified synthesis
- Shared writable candidate paths

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Every candidate read end-to-end before pick
- Synthesis note names base, grafts, rejections, verify
- Verification ran

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Rubric authoring steers all candidates toward the author's taste
- Cross-judge model family choice biases the base
- Grafting can create a chimera

What still needs a human: Whether the rubric is the right contract, and whether consensus shape is actually good.

## Method card — same family every run

A later agent runs this from this file alone.

1. Frame -> fan out -> cross-judge -> pick -> graft -> verify -> synthesis note.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Use `arena runners` from `~/.cursor/rules/pstack-models.mdc` when present. Otherwise default to one each on `claude-fable-5-1-thinking-max`, `gpt-5.6-sol-max`, `grok-4.6-fast-xhigh`, `claude-opus-5-thinking-xhigh`. Spawn more when the arena covers multiple design directions. Same model N times when the work is generation-bound rather than judgment-sensitive.
4. Assign output paths. Each candidate writes to its own location (a git worktree where possible, otherwise `/tmp/arena-<slug>/candidate-<n>/`), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Spawn all N subagents in one message with `run_in_background: true`, each with the task, the path to the shared grounding, its own output path, and instructions to produce both the artifact and a short rationale.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates complete, choose one model from the `arena cross-judge pool` in `~/.cursor/rules/pstack-models.mdc` when present. Otherwise use `claude-fable-5-1-thinking-max`, `gpt-5.6-sol-max`, `grok-4.6-fast-xhigh`, `claude-opus-5-thinking-xhigh`. Prefer a different model family from the parent's. Spawn one readonly judge subagent on that model. It sees the rubric and the candidates by path label, scores each criterion, and recommends a base with rationale. It runs in parallel with the parent's reading in Phase D, not with the candidates themselves. Don't spawn the judge while candidates are still writing.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.
