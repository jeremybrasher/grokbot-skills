---
name: how
description: "Use for \\\"how does X work\\\", code walkthroughs before changing something, and placement / ownership / layering questions (\\\"where should this live\\\", \\\"which package owns this\\\", \\\"is this the right layer\\\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# How

## When to use

How does X work, code walkthroughs before changing something, placement/ownership/layering questions.

**Do not use when:**
- Why/rationale/history questions (use why)
- No readable code or system
- User wants a redesign as the first deliverable

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Named subject (symbol, feature, path, or behavior)
2. Readable code or runtime to observe
3. Question mode: mechanism vs placement

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Subject missing | Named X | Symbol, file, or behavior | I need the subject. Holding. |
| Cannot read the code/system | Observable artifact | Access or paste | Cannot walk through what I cannot see. |
| Question is why/history | Wrong skill | Route to why | Holding how; this needs why. |
| Would invent a layer map | Evidence from the tree | Actual packages/modules | Do not invent ownership. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Explain the path that matters; do not dump the whole module
- Prefer one clear call chain
- No drive-by refactors while explaining
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Speculative architecture presented as current fact
- Unrequested redesign
- Walkthroughs from memory of similar apps

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Claims cite files/symbols observed this run
- Placement advice names existing owners
- Separated mechanism vs recommendation if both appear

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Walkthrough order creates a false main path
- Ownership answers can freeze a layering debate
- Explorer/explainer split can disagree on the same code

What still needs a human: Whether the explained path is the one they care about.

## Method card — same family every run

A later agent runs this from this file alone.

1. Intake -> observe code -> walk the chain -> answer placement if asked -> cite paths.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): spawn parallel explorers first, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Spawn all explorers in a single message:

- `subagent_type`: `generalPurpose`
- `model`: your configured how-explorer model (default `grok-4.6-fast-xhigh`)
- `readonly`: `true`

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Spawn one Task subagent that explores and explains in one pass:

- `subagent_type`: `generalPurpose`
- `model`: your configured how-explainer model (default `claude-fable-5-1-thinking-max`)
- `readonly`: `true`

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once all explorers have returned, spawn one Task subagent to synthesize their findings into one explanation:

- `subagent_type`: `generalPurpose`
- `model`: your configured how-explainer model (default `claude-fable-5-1-thinking-max`)
- `readonly`: `true`

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
