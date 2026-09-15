---
name: setup-pstack
description: "Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, \"configure pstack models\", \"pstack budget\", or changing pstack's model choices. Observe required inputs first; HOLD when they are missing rather than guessing."
---

# Setup pstack

## When to use

Configure which models pstack uses per role and reasoning budget. Use for /setup-pstack, configure pstack models, pstack budget, or changing pstack model choices.

**Do not use when:**
- User only wants current defaults without writing a rule
- They asked to change an unrelated Cursor setting
- No pstack skills will run here

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Intent to configure pstack models
2. A way to detect available model slugs, or the user pasted list
3. Whether an existing pstack-models.mdc should be updated vs created

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| No detectable models and no pasted list | Confirmed available slugs | Detection result or user paste | I need model slugs I can confirm. I will not invent them. |
| User has not chosen a budget | Budget label | AskQuestion with the four budget options | The budget question. No rule write yet. |
| Real slug not in detected set | An available slug or alias | Re-ask with detected options | Stop. Ask again. Do not write an unconfirmed slug. |
| User declines write | Authority to write the rule | Explicit accept | Leave existing rule untouched. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Overwrite the whole rule file idempotently; do not append duplicate roles
- Delete a role line only when the user wants the skill default back
- Do not invent extra roles
- Offer create-verification-skill once; do not push if declined
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- Unconfirmed real model slugs
- Budget labels outside the four options
- Silent fallback to a guessed family when detection failed
- Rewriting unrelated Cursor rules

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Every real slug written was detected or user-confirmed
- Budget line present
- User confirmed the role table before write, or HOLDed
- File written only after validation

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Showing a default table anchors choices toward those families
- AskQuestion option order nudges budget selection
- alwaysApply rule changes every future session

What still needs a human: Final budget taste, which roles stay on Auto/inherit-parent, and whether to generate a verification skill.

## Method card — same family every run

A later agent runs this from this file alone.

1. Detect models -> load current rule -> ask budget -> map -> confirm roles -> validate -> write -> confirm.
2. Any missing slug or declined write -> HOLD, not a guessed config.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Write `~/.cursor/rules/pstack-models.mdc`, an always-applied rule that sets pstack's model per role.

## Steps

### 1. Detect available models

Enumerate the model slugs you can pass to a `Task` subagent in this session. That is the dependable source. If Cursor also exposes a models API or CLI that lists the user's entitled models, prefer it for completeness. If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid even though they are not detected slugs.

### 2. Load current state

The default role-to-model mapping is the rule shape shown in step 5 below. If `~/.cursor/rules/pstack-models.mdc` already exists, read it and treat its `# budget` line and its role values as the current choices. Otherwise start from those defaults.

### 3. Budget, map, and confirm

**(a) Ask for a budget.** Prefer AskQuestion over free text. Offer these four options with these exact labels, and name the current budget when the rule records one.

- `unlimited — keep max`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

**(b) Apply it.** Build the working table from the skill defaults, and on a re-run keep any role you changed by family, list, or alias (`inherit-parent`, `auto`). `unlimited` leaves every effort as in that table. `large`, `medium`, and `small` set the effort token of every real slug, panel entries included, to `xhigh`, `high`, or `medium`. The effort token is the last token, or the one before a trailing `fast`, on the ladder `max` > `xhigh` > `high` > `medium` > `low`. If the result is not a detected slug, use the same family's detected slug with the highest effort at or below the target, else mark the role as needing a choice. `inherit-parent` and `auto` do not change. So `small` turns `claude-fable-5-1-thinking-max` into `claude-fable-5-1-thinking-medium`, and `grok-4.6-fast-xhigh` into `cursor-grok-4.6-medium-fast` when only that form is detected.

**(c) Show the roles and confirm.** Show every role with its model, marking any real slug not in the detected set as needing a choice. Ask whether to accept as-is or change specific roles, offering the detected models plus `inherit-parent` and `auto` (both mean: this role runs on the parent chat model, which is how Auto users stay on Auto) as the options. Prefer AskQuestion over free text. For panel roles (arena runners, architect runners, interrogate reviewers) the value is a list, and one subagent runs per entry, alias entries included, so the list length sets the count. `arena cross-judge pool` is also a list, but Arena selects one value from it whose model family differs from the parent's when possible. `swarm workers` is the default model for every worker unless a race or comparison assigns another model per arm.

### 4. Validate

Every real slug written must be in the detected set. `inherit-parent` and `auto` always pass. If a chosen real slug is not available, stop and ask again.

### 5. Write the rule

Write `~/.cursor/rules/pstack-models.mdc` with `alwaysApply: true`, a `# budget` line with the chosen label and its target effort, and one line per role, using the same labels poteto-mode uses. Overwrite the whole file so re-runs stay idempotent. Shape:

```
---
description: pstack per-role model choices (overrides skill defaults)
alwaysApply: true
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: unlimited (max)
feature, refactoring: grok-4.6-fast-xhigh
bug-fix: grok-4.6-fast-xhigh
perf-issue: grok-4.6-fast-xhigh
hillclimb: grok-4.6-fast-xhigh
judgment and prose: claude-fable-5-1-thinking-max
hardest tasks: claude-fable-5-1-thinking-max
how explorer: grok-4.6-fast-xhigh
how explainer: claude-fable-5-1-thinking-max
why investigators: grok-4.6-fast-xhigh
why synthesizer: claude-fable-5-1-thinking-max
reflect tooling: gpt-5.6-sol-max
reflect judgment, divergent, synthesizer: claude-fable-5-1-thinking-max
arena runners: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
arena cross-judge pool: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
swarm workers: grok-4.6-fast-xhigh
architect runners: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
interrogate reviewers: claude-fable-5-1-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
```

### 6. Confirm

Tell the user the rule was written and that it applies to new sessions. Re-running this skill updates it.

### 7. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, invoke `/create-verification-skill` (resolves wherever pstack is installed: workspace, user, or plugin). On no, move on without pushing.
