---
name: typescript-best-practices
description: "TypeScript best practices. Use when reading or editing any .ts or .tsx file. Observe required inputs first; HOLD when they are missing rather than guessing."
paths: ["**/*.ts", "**/*.tsx"]
disable-model-invocation: true
---

# TypeScript best practices

## When to use

Reading or editing any .ts or .tsx file; apply TypeScript best practices.

**Do not use when:**
- Non-TypeScript files
- No code to read or edit
- User asked for a language migration plan, not TS practice

## Intake — before you proceed

You need all of the following. If any is missing, stop.

1. Named .ts/.tsx files or an edit task in TypeScript
2. Readable project TS config / patterns when advising project-wide norms

If any is missing, stop. Say what is missing and what you need. Do not invent inputs to keep moving.

## HOLD — stop and return this, not a polished guess

When you cannot proceed, return the gap.

| Condition | What is missing | What it needs | Return instead |
|---|---|---|---|
| No TS file in scope | A .ts/.tsx target | Path or paste | Holding. |
| Advice would fight stated project tsconfig | Alignment with project config | Read tsconfig or ask | Do not invent a rival house style. |
| Would add types that invent domain facts | Types grounded in code | Observe first | Holding speculative types. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Prefer existing project patterns
- Do not add utility types unasked
- Smallest typing fix
- Expansion needs evidence from the request or the observed system — not from a habit of completeness.

## Will not produce

- any to silence errors without a plan
- Drive-by refactors while typing
- Fake strictness that breaks builds

## Before you return

Run this check. If any item fails, fix or HOLD — do not hand over a guess.

- Advice cites observed files
- Edits typecheck or HOLD with the error
- No invented domain

## What this process changes

The recipe is not a neutral mirror. It changes the work:

- Strict typing pushes designs toward representable states and can reject valid runtime shapes
- Best-practice lists flatten project-specific tradeoffs

What still needs a human: Whether to adopt a stricter pattern than the repo currently uses.

## Method card — same family every run

A later agent runs this from this file alone.

1. Observe TS files/config -> apply practices from Domain recipe -> verify types.

## Domain recipe

The following is the domain behavior to keep. Alignment sections above constrain intake, pauses, cuts, and refusals; they do not replace this recipe.

Apply the **type-system-discipline** principle skill first.

| Rule | Summary |
|------|---------|
| Discriminated unions | Model variants with a `kind` literal discriminant so impossible states can't be represented. No optional-field bags. |
| Branded types | Brand primitives with `& { readonly __brand: "X" }` so they can't be mixed up. Validate once at the boundary. |
| Constructive modeling | Build the shape so the illegal value can't be constructed. `[T, ...T[]]` for non-empty, `[T, T][]` for even length, `start` plus `duration` for a range. Not a runtime guard, not a wish for refinement types. |
| Simplest total type | Keep `T[]` while every operation on it stays total. Strengthen to `NonEmpty<T>` only where the loose type forces `!`, a cast, or a "should never happen" throw. |
| `unknown` over `any` | External data is `unknown`. |
| Schemas before guards | Before hand-writing a property-by-property type guard, use the repository's runtime schema library and infer the type from the schema, such as `z.infer`. |
| No `as` casts | Every `as` is a runtime crash waiting. Cast only after validation. |
| Narrowing hierarchy | Discriminant switch > `in` operator > `typeof`/`instanceof` > user-defined type guard > `as`. |
| Type guards | Must verify the claim. A lying guard is worse than `as` because the bug hides behind a name that says it's safe. Name them `isX` or `hasX`. |
| Exhaustiveness | Inline `const _exhaustive: never = x;` in default arms so the compiler errors when a new variant is added. |
| `satisfies` over `as` | Validates the value without widening literal types. |
| Boundary validation | Parse where data crosses in, into a named domain type. `Record<string, unknown>` (however spelled) stops at that parse. Trust types inside. See the **boundary-discipline** principle skill. |
| Schema-derived types | Reach for `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof` before declaring a new interface. |
| Object args | Pass objects, not positional, so argument order is self-documenting. Skip on hot paths (per-frame render, tokenizers, parsers). |
| Real tests | Don't mock what you can run. Prefer the framework's real test primitives with leak/disposable checks, and verify UI in a running build. Mock only what you can't run locally. |
| Structured telemetry | Prefer structured logger diagnostics with enough context to debug from an id. No `console.log` in shipped code. |

Examples: `references/patterns.md`.
