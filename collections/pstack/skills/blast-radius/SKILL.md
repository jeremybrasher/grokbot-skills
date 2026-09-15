---
name: blast-radius
description: "Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing a small diff you don't trust. Observe required inputs first; HOLD when they are missing rather than guessing."
disable-model-invocation: true
---

# Blast radius

## When to use

Find what a change could break elsewhere before it ships; prove the safety fact by running real code.

**Do not use when:**
- No change named
- Cannot run or read the system
- User only wants a speculative essay with no proof

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. The change (diff, PR, or proposed edit)
2. A way to observe dependents
3. What safe-because would mean as a checkable claim

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| Change unnamed | Diff or description | PR, patch, or files | Need the change. Holding. |
| No way to observe dependents | Search/tests/runtime | Access or harness | Cannot claim blast radius blind. |
| Safety claim untestable here | An executable check | Test, script, or runtime probe | Do not write a safety essay without proof. |
| Would require production-only poke | Safe environment | Staging/local harness or HOLD | Will not poke production. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Prove one safety fact; do not boil the ocean
- Prefer existing tests/harnesses
- Delete speculative risk bullets with no path to evidence
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Unverified looks safe
- Endless dependent catalogs without a proof
- Expanding the change under review

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- At least one real execution or typed/search proof cited
- Unknowns listed as unknowns
- No production poke

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- The chosen probe defines what blast radius means
- Passing nearby tests can hide untested callers
- Writing risks as prose creates false completeness

What still needs a human: Residual untested callers and whether to ship anyway.

## Method card — same family every run

A later agent runs this from this file alone.

1. Name change -> find dependents -> pick one proof -> run it -> report radius + unknowns.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Find what a change breaks somewhere else, before it ships. Use for "blast radius of X", "what could this break", or reviewing a small diff you don't trust yet.

Companion to `how` and `why`. `how` tells you what the code does. `why` tells you why it's shaped that way. Blast radius tells you what it breaks somewhere else.

Listing the callers is not the job. The agent can grep those in a second. The job is the breakage grep won't show you.

## Don't trust your own writeup

A blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it's true. So don't hand back the writeup. Find the one or two facts the whole thing depends on and prove them by running code.

### How sure are you

For each fact the change's safety depends on, get it as far down this list as is cheap, and say where it stopped.

1. You said so. Worthless on its own.
2. You pointed at the line. A real `file:line`, or the library's own source.
3. You showed the bad case can't happen. You walked the failure step by step and it doesn't reach.
4. You ran it. A script or test that calls the real code and fails loud if you're wrong.
5. You reproduced it in the running app.

Any safety fact you can't get to step 4, say so. Don't write it up as settled. Step 4 is usually one small script that imports the same library the app ships and calls the exact function you're worried about.

## Steps

1. Read the change. The diff, the symbols it adds, changes, and deletes, and what it now does differently, including the part the diff doesn't spell out. Use `why` step 2 to pull the PR and commits.
2. Find the one fact it's safe because of. Most changes that look risky are safe because of a single fact, like "this call only drops already-dead cache entries and does nothing else". Find that fact. If it holds, most risky cases are cleared at once. Spend your time here, not on a long list of maybes.
3. Look where grep stops. Read the source of the library you call, and check its pinned version and any local patch. Work out when things run: microtasks, unmount and teardown, Solid versus React. Follow what a symbol search misses: the JSON an API returns, a DB column, a wire format, another language reading the same bytes, a feature flag, code three hops downstream.
4. Be honest about each risk. Give it a real chance of happening and a real cost if it does. Keep the risks you confirmed. List the ones you checked and cleared separately. Same rules as `why`. Cite a real `file:line`, a search that finds nothing is still an answer, and never make up a caller or an API.
5. Prove the one fact. Write a script or test that runs the real code, run it, and paste what happened. If you can't prove it cheaply, mark it unproven. Don't overstate.
6. For a big or wide change, run it as an `arena`. Ask several models the same question and merge the answers. Different models catch different real bugs.

## What to hand back

- **What it does.** What changed, including the part that isn't obvious.
- **The one fact it's safe because of.** State it, say which step you got it to, and show the proof. If you couldn't prove it, write unproven.
- **Risks.** Only the real ones. Each names how it breaks, the `file:line`, how likely and how bad, and how to check. Paste the proof for the ones that matter.
- **Cleared.** What you checked and why it's fine.
- **Before you merge.** The cheapest test or repro that catches the real bug, including the script you wrote.

Write it through `unslop`, cite real code, and strip anything private before it goes anywhere public.

**Reply:** the writeup above, with the one safety fact either proven or marked unproven.
