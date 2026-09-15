---
name: principle-foundational-thinking
description: "Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Foundational Thinking

## When to use

Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious.

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

**Structural decisions** protect option value. **Code-level decisions** protect simplicity.

**Data structures first.** Get the data shape right before writing logic. Define core types early, trace every access pattern, and choose structures that match the dominant paths.

At code level, DRY the structure, not every line. Types and data models should converge. Three similar statements still beat a premature abstraction. Prefer explicit over clever. Test behavior and edge cases, not line counts.

**Concurrency corollary.** Before sharing state between actors, ask "what happens if another actor modifies this concurrently?" If not "nothing", isolate.

**Scaffold first.** If something helps every later phase, do it first. Ask "does every subsequent phase benefit from this existing?" CI, linting, test infrastructure, and shared types are scaffold. Sequence for option value: setup before features, tests before fixes. Keep commits small and single-purpose.

Each increment should land a coherent abstraction or deepen one that exists. Do not spread a new capability across callers as special-case coordination.

Subtraction comes before scaffolding. Remove dead code first, then lay foundations.
