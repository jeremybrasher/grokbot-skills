---
name: figure-it-out
description: "Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions via show-me-your-work. Use for /figure-it-out, 'figure it out', a large migration, or when no narrower playbook applies. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Figure it out

## When to use

No narrower playbook fits: large migration, ambitious multi-part change, or work reviewed after stepping away.

**Do not use when:**
- A bundled playbook already fits
- Standing multi-day program rather than one bespoke run
- Cannot state any done predicate

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Task that failed narrower playbook match
2. Falsifiable done predicate
3. Whether the human will review after stepping away

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Narrower playbook fits | True figure-it-out need | Route to that playbook | Wrong skill. Holding. |
| Done predicate missing | Falsifiable done | Write the predicate | Do not start the long run. |
| Multi-hour run, no checkpoint presented | Framing checkpoint | Present framing/tradeoffs | HOLD commit to the long run until checkpoint. |
| INCONCLUSIVE treated as pass | Honest verdict | Fix gate or keep open | Inconclusive is not a pass. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Atomic landable units; riskiest unknown first
- Verify harness before features
- Revert units that do not advance the predicate
- Do not over-fan
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Batching all checks at the end
- Self-report verification
- Hiding negatives
- Silent workarounds for a broken gate

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Playbook designed before code
- Decision trail path named
- Predicate checked on real product

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Bias toward more rigor can over-gate reversible work
- Hypothesis loop can local-optima a bad predicate
- Committed trails create narrative gravity in review

What still needs a human: Rigor level tradeoffs and whether open items block trust.

## Method card — same family every run

A later agent runs this from this file alone.

1. Frame -> design workflow -> hypothesis loop per unit -> audit trail -> verify against predicate.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

When the task matches no playbook, design one. The deliverable before any code is the workflow itself: a sequence of phases that scales rigor to the task, runs the scientific method, and leaves a decision trail a human can audit after stepping away. Bias toward more rigor. The cost of building the wrong thing dwarfs the cost of being careful.

## Start

Open a todolist whose first item is to read the Principles section of the **poteto-mode** skill. Then add the phases below as todos.

## Phase A: Frame

Ground first, then commit. Don't start the run until you can state:

- The definition of done as a falsifiable predicate (the **prove-it-works** principle skill).
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The rigor level, biased high. One-way doors and high blast radius get more. Reversible low-stakes steps get less. Rigor is gates and artifacts, not "try harder".

Present the framing and tradeoffs before committing to a long run. Reversible work proceeds (the **never-block-on-the-human** principle skill), but a multi-hour run earns one checkpoint.

## Phase B: Design the workflow

Decompose into atomic, independently-landable units. Sequence riskiest-unknown-first. Scaffold and verification come before features (the **foundational-thinking** principle skill).

- Build the verification harness before the work, with the baseline captured from the pre-change state, so the check reads as "old value vs new value".
- For one-way-door design decisions, run the **architect** skill (it runs **arena**). Skip it for mechanical work whose shape is already concrete. A second arena over a settled design is over-engineering (the **laziness-protocol** principle skill).
- Decide what fans out. Parallelize only across seams, and give each worker its own worktree or branch (the **separate-before-serializing-shared-state** principle skill). Don't over-fan.
- Write the designed phase list down. That list is what the human reviews.

Then execute the design. Add its steps to the todolist as concrete items, after the Phase C entry and before Phase D. Run each under the Phase C loop discipline, and weave the Phase D log through them, a row as each step lands, rather than saving the whole trail for the end.

## Phase C: Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert it if it didn't.
Apply the **sequence-verifiable-units** principle skill, verifying each unit before starting the next instead of batching checks at the end.

- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Pair delegated work with a judge and audit the delegates' artifacts yourself before trusting them. If a worker games the gate, reset and harden the contract. If the gate itself is wrong, fix the gate in its own change rather than routing around it.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Don't hide a negative.

## Phase D: Keep the audit trail

Log the run via the **show-me-your-work** skill, one canonical TSV with a row per decision and per unit, evidence as links. figure-it-out's work is usually ambitious enough to commit the trail so the reviewer can read it in the PR. Commit it when confidence has to be shown. Prefer evidence produced by committed scripts. The trail plus the diff is what lets the human come back and trust the work.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Encode any recurring correction as a gate, a lint rule, a check, or a script (the **encode-lessons-in-structure** principle skill).

**Reply:** the playbook you designed, the rigor level and why, the decision-trail path, what's verified against the predicate, and what's still open.
