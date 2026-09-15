---
name: principle-boundary-discipline
description: "Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Boundary Discipline

## When to use

Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions.

**Do not use when:**
- The trigger in the description is not met
- A narrower operational skill already covers the same decision
- You would only be citing the name without changing a choice

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. A concrete situation (change, bug, design fork, or review object) that might invoke this principle
2. Enough context to tell whether the trigger actually fires
3. The decision or action this principle would change

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Trigger unclear | Evidence the trigger fires | A fact from the work that matches the description | Name the gap. Do not cite the principle as decoration. |
| No situation object | A change, bug, fork, or review target | One sentence naming the object | I need the object of work before applying this principle. |
| Would only rename the same plan | A choice the principle actually changes | A different next action, or silence | Holding. Citing without changing a choice is noise. |
| Conflicts with a hard user constraint | Alignment with stated constraints | User confirmation or a different principle | State the conflict. Do not override the user constraint. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Do not expand scope to fully apply the principle
- Prefer the smallest structural change the principle demands
- If the principle says delete, delete before adding
- Do not write an essay about the principle; show the changed choice
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- A decorative citation with no changed decision
- A rewrite of the whole system when a local application suffices
- Invented project facts to make the principle fit

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Trigger was evidenced or you HOLDed
- The principle changed a named choice, or you HOLDed
- No decorative citation
- Domain purpose of the surrounding task is unchanged

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Naming a principle early anchors the agent on that frame and can hide better-fitting principles
- Stop-rules can freeze useful exploration when the census or premise is incomplete
- Delete-first readings can discard still-needed scaffolding if the dead-weight call is wrong

What still needs a human: Whether the trigger truly fired, whether the structural fix is worth the blast radius, and whether to override for a product reason.

## Method card — same family every run

A later agent runs this from this file alone.

1. Intake: situation + trigger evidence + decision to change. Gap -> HOLD.
2. State the trigger match in one sentence.
3. Apply the pattern in the Domain recipe below.
4. Return the changed choice (or HOLD), not a principle lecture.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Place validation, type narrowing, and error handling at system boundaries. Trust internal code unconditionally. Business logic lives in pure functions. The shell is thin and mechanical.

**Why:** Scattered validation is noisy, redundant, and gives a false sense of safety. Keep logic out of framework wiring so it can be tested without the framework.

**The pattern:**
- **At boundaries** (CLI args, config files, external APIs, network protocols): validate, return errors, handle defensively.
- **Inside the system:** typed data, error propagation, no re-validation. Trust the types.
- **Across the boundary.** Expose domain concepts, not the boundary's private representation. Keep general-purpose mechanism inside and special-purpose policy at the edge.

**Applications:**

Validation and error handling:
- Validate config at parse time (the boundary), not inside business logic
- Parse raw data into domain types at the boundary
- Do not re-export transport, storage, framework, or wire types through the public surface
- No redundant nil checks deep in call chains if the boundary already validated

Code organization:
- Business logic in pure functions with no framework dependencies
- Parse functions: pure transforms from raw bytes to typed state
- Prompt construction: structured state in, string out
- Scoring and assessment: pure transforms from state to results

**The tests:**
- "Is this data crossing a system boundary right now?" If not, validation is redundant.
- "Can this be a pure function that the shell just calls?" If yes, extract it.
