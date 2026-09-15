---
name: principle-encode-lessons-in-structure
description: "Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Encode Lessons in Structure

## When to use

Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text.

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

Encode recurring fixes in mechanisms (tools, code, metadata, automation) instead of textual instructions. Every error, human correction, and unexpected outcome is a learning signal. Capture it, route it, and close the loop.

**Why:** Textual instructions are easy to miss. They require the reader to notice, remember, and comply. Structural mechanisms (lint rules, metadata flags, runtime checks, automation scripts) enforce the rule without cooperation.

**Pattern:**
When you catch yourself writing the same instruction a second time:
1. Ask: can this be a lint rule, a metadata flag, a runtime check, or a script?
2. If yes, encode it. Delete the instruction
3. If no (requires judgment), make the instruction more prominent and add an example of the failure mode

**Pick the strongest mechanism.** When more than one mechanism would work, choose the strongest the situation allows (an unrepresentable state that cannot compile, then a lint or banned API that fails CI, then a canonical helper, then a runtime check), because agents copy whatever the surrounding code already does and a weaker guard becomes the next template.

**Corollary:** If the fix is structural, only use the structural fix. The instruction is the symptom.

**Feedback loop:**
- **Capture every correction.** When the human intervenes or tests fail, decide if it's a one-off or a pattern.
- **Route to the right layer.** One-off -> brain note. Recurring fix -> skill or lint rule. Systemic issue -> principle.
- **Close the loop.** Don't just record. Apply now or create a concrete todo.

**Anti-patterns:**
- Acknowledging without recording ("I'll keep that in mind" does not persist)
- Recording without routing (a brain note about a lint rule that should exist is wasted unless the lint rule gets implemented)
- Fixing without generalizing (fixing one instance while leaving the recurring pattern intact)
