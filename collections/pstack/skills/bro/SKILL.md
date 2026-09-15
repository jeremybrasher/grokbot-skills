---
name: bro
description: "Restate the last message in plain human language, with no jargon. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# bro

## When to use

Restate the last message in plain human language, with no jargon.

**Do not use when:**
- No prior message to restate
- User asked for analysis or advice, not a restatement
- Source is already plain and restating would add noise

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. The last message (or explicitly named message) to restate
2. Confirmation that plain restatement is wanted

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| No message to restate | Source text | Point at the message | Nothing to restate. Holding. |
| Would invent meaning not present | Faithful paraphrase | Stay inside the source | Holding rather than embellish. |
| User wanted analysis | Wrong skill | Route to the right skill | bro only restates. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- One plain restatement
- No added advice
- No jargon substitutions that change meaning
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Advice smuggled into a restatement
- Jargon glossaries unless needed for the restatement itself
- Fabricated context

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Output is plain language
- Meaning preserved
- No new claims

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Simplification can drop nuance the speaker relied on
- Choosing which clause to foreground changes emphasis

What still needs a human: Whether the restatement captured the intended emphasis.

## Method card — same family every run

A later agent runs this from this file alone.

1. Intake source -> restate plainly -> return only the restatement or HOLD.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Restate your last message. Stop using jargon and speak coherently. State it more simply and concisely, like one human talking to another.
