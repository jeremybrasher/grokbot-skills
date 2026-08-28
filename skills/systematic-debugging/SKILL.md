---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. Observe the failure first. Do not use it to implement an already-approved design, to add a feature with no failing behavior, or to guess a root cause from a one-line complaint.
---

# Systematic Debugging

## Overview

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to use

Use for a technical failure you can name: test failures, production bugs, unexpected behavior, performance problems, build failures, integration issues.

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

**Do not use this to:**
- Implement an already-approved design (that is implementation, not debugging)
- Add a feature that has no failing behavior
- Rewrite architecture on the first failure
- Produce a postmortem, a status update, or a blame assignment

## Intake — before Phase 1

You need three things. Nothing else starts. Do not form a hypothesis, do not add instrumentation, do not propose a fix.

1. **A named failure.** An error message, a failing test, a broken behavior, a measured regression. "Something's wrong" or "the app is weird" is not enough.
2. **A system you can observe.** Repo, logs, stack, environment, or a reproduction the partner can run. A screenshot of a symptom with no access is not enough.
3. **A way to gather evidence.** Either a consistent reproduction, or a next measurement you can take. If you can neither reproduce nor measure, you cannot investigate.

If any of those is missing, stop. Say what is missing and what you need. Do not invent a root cause. Do not propose a "likely" fix to keep moving.

Then, and only then, enter Phase 1.

## HOLD — stop and return this, not a fix

When you cannot proceed, return the gap. Do not fill it with a polished patch.

| Condition | What is missing | What it needs | Return instead of a fix |
|---|---|---|---|
| No named failure | The object of investigation | Error, failing test, broken behavior, or measured regression | "I need the failure itself — an error, a test, or the broken behavior. I will not invent one." |
| No observable system | Access to code, logs, stack, or environment | A path, a log, a repo, or a reproduction the partner can run | "I cannot observe the system, so I cannot investigate. Holding." |
| Neither reproducible nor measurable | A next fact | Steps that trigger it, or one measurement to take | "Not reproducible and I have no next measurement. I will not guess." |
| Phase 1 not done | A stated root cause with evidence | Completed investigation: error read, reproduced or measured, recent changes checked | The investigation so far. No patch. |
| Hypothesis is vague | A single testable claim | "I think X is the root cause because Y" | Write the claim or HOLD. Do not change code. |
| Fix would ship without a failing reproduction | A test or script that fails the same way | Simplest reproduction that fails first | The reproduction. No production change. |
| 3+ fixes already failed | A decision on the pattern, not another patch | Human discussion: keep this architecture or change it | The three failures, the coupling they revealed, the question. Do not attempt fix #4. |
| Human said "stop guessing" / "is that not happening?" / "we're stuck?" | A return to evidence | Phase 1 restarted with what you assumed named | Stop. Name the assumption. Return to Phase 1. |
| Production, data-loss, or security blast radius | Human authority to touch that surface | Explicit yes from the partner | The risk and the question. No change. |
| Companion file missing (`root-cause-tracing.md`, a TDD skill, a verification skill) | Nothing — those files are optional | The methods already in this file | Do not stall. Use the quick versions below. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Do not add a component, wrapper, retry, timeout, or feature flag to work around a failure you have not named.
- Do not keep code from a failed hypothesis. Revert it before the next test.
- Do not bundle refactor with the fix. "While I'm here" is a new request.
- Do not add a second layer of instrumentation after the failing boundary is already visible.
- Prefer revert of the recent change that introduced the failure over a new branch of logic.
- Prefer delete the bad path over adding a guard that leaves the bad path alive.
- The smallest change is allowed only after a root cause is named. Smallest-change is not a license to patch a symptom.
- Extra files, extra tests beyond the one reproduction, or extra logging in the shipped fix need a reason from the failure — not from a habit of completeness.
- If a companion technique file is missing, do not create it. Use the method card in this file.

## Will not produce

Do not return any of the following:

- A patch before Phase 1 is complete
- A "probably X" guess dressed as a root cause
- A symptom workaround (retry, catch-and-ignore, sleep, default value) presented as the fix
- Multiple unrelated changes in one attempt
- A failing-test skip, a deleted assertion, or "I'll verify manually"
- Code kept from a failed hypothesis
- An architecture rewrite on the first or second failure
- A claim of "no root cause" before the investigation in this file is finished
- A fourth fix attempt after three failures, without the architecture question
- A stall because a companion file or another skill is missing
- A root cause invented because the failure is not reproducible

## Method card — same family every run

A later agent runs this from this file alone. `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, and any TDD or verification skill are optional extras. If they are missing, do not stall and do not invent a different method — use the card below. Do not skip, reorder, or replace these phases.

1. **Intake.** Named failure + observable system + a way to gather evidence. Any gap → HOLD.
2. **Phase 1 — root cause.** Read the error completely. Reproduce or take the next measurement. Check recent changes. If the system has component boundaries, instrument each boundary once, then read where it breaks. If the error is deep in a call stack, trace backward to the original bad value (quick version in Phase 1). Stop when you can say what fails and why. No patch in this phase.
3. **Phase 2 — pattern.** Find a working example of the same kind. Read the reference completely if you are implementing a pattern. List every difference. Name the dependencies and assumptions.
4. **Phase 3 — one hypothesis.** Write one claim: "I think X is the root cause because Y." Change one variable to test it. If it fails, revert and write a new claim. Do not stack changes.
5. **Phase 4 — fix.** Write the simplest failing reproduction first. Then one change at the named root. Verify the reproduction now passes and neighbors still pass. If the change fails and you have tried fewer than three: return to Phase 1. If three have failed: HOLD for architecture, do not attempt a fourth.
6. **Return.** Root cause stated, reproduction that failed then passed, single change, or a HOLD. Nothing else.

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Don't skip past errors or warnings
   - They often contain the exact solution
   - Read stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Can you trigger it reliably?
   - What are the exact steps?
   - Does it happen every time?
   - If not reproducible → gather more data, don't guess

3. **Check Recent Changes**
   - What changed that could cause this?
   - Git diff, recent commits
   - New dependencies, config changes
   - Environmental differences

4. **Gather Evidence in Multi-Component Systems**

   **WHEN system has multiple components (CI → build → signing, API → service → database):**

   **BEFORE proposing fixes, add diagnostic instrumentation:**
   ```
   For EACH component boundary:
     - Log what data enters component
     - Log what data exits component
     - Verify environment/config propagation
     - Check state at each layer

   Run once to gather evidence showing WHERE it breaks
   THEN analyze evidence to identify failing component
   THEN investigate that specific component
   ```

   **Example (multi-layer system):**
   ```bash
   # Layer 1: Workflow
   echo "=== Secrets available in workflow: ==="
   echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

   # Layer 2: Build script
   echo "=== Env vars in build script: ==="
   env | grep IDENTITY || echo "IDENTITY not in environment"

   # Layer 3: Signing script
   echo "=== Keychain state: ==="
   security list-keychains
   security find-identity -v

   # Layer 4: Actual signing
   codesign --sign "$IDENTITY" --verbose=4 "$APP"
   ```

   **This reveals:** Which layer fails (secrets → workflow ✓, workflow → build ✗)

5. **Trace Data Flow**

   **WHEN error is deep in call stack:**

   If `root-cause-tracing.md` is in this directory, use it. If it is missing, use this quick version — do not stall.

   **Quick version:**
   - Where does bad value originate?
   - What called this with bad value?
   - Keep tracing up until you find the source
   - Fix at source, not at symptom

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. **Find Working Examples**
   - Locate similar working code in same codebase
   - What works that's similar to what's broken?

2. **Compare Against References**
   - If implementing pattern, read reference implementation COMPLETELY
   - Don't skim - read every line
   - Understand the pattern fully before applying

3. **Identify Differences**
   - What's different between working and broken?
   - List every difference, however small
   - Don't assume "that can't matter"

4. **Understand Dependencies**
   - What other components does this need?
   - What settings, config, environment?
   - What assumptions does it make?

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. **Form Single Hypothesis**
   - State clearly: "I think X is the root cause because Y"
   - Write it down
   - Be specific, not vague

2. **Test Minimally**
   - Make the SMALLEST possible change to test hypothesis
   - One variable at a time
   - Don't fix multiple things at once

3. **Verify Before Continuing**
   - Did it work? Yes → Phase 4
   - Didn't work? Form NEW hypothesis
   - DON'T add more fixes on top

4. **When You Don't Know**
   - Say "I don't understand X"
   - Don't pretend to know
   - Ask for help
   - Research more

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. **Create Failing Test Case**
   - Simplest possible reproduction
   - Automated test if possible
   - One-off test script if no framework
   - MUST have before fixing
   - If a test-driven-development skill is present you may use it for the reproduction. If it is missing, write the simplest failing reproduction here. Do not stall.

2. **Implement Single Fix**
   - Address the root cause identified
   - ONE change at a time
   - No "while I'm here" improvements
   - No bundled refactoring

3. **Verify Fix**
   - Test passes now?
   - No other tests broken?
   - Issue actually resolved?
   - If a verification skill is present you may use it. If it is missing, run the reproduction and the neighboring tests yourself. Do not stall.

4. **If Fix Doesn't Work**
   - STOP
   - Count: How many fixes have you tried?
   - If < 3: Return to Phase 1, re-analyze with new information
   - **If ≥ 3: STOP and question the architecture (step 5 below)**
   - DON'T attempt Fix #4 without architectural discussion

5. **If 3+ Fixes Failed: Question Architecture**

   **Pattern indicating architectural problem:**
   - Each fix reveals new shared state/coupling/problem in different place
   - Fixes require "massive refactoring" to implement
   - Each fix creates new symptoms elsewhere

   **STOP and question fundamentals:**
   - Is this pattern fundamentally sound?
   - Are we "sticking with it through sheer inertia"?
   - Should we refactor architecture vs. continue fixing symptoms?

   **Discuss with your human partner before attempting more fixes**

   This is NOT a failed hypothesis - this is a wrong architecture.

## Red Flags - STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
- "Here are the main problems: [lists fixes without investigation]"
- Proposing solutions before tracing data flow
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals new problem in different place**

**ALL of these mean: STOP. Return to Phase 1.**

**If 3+ fixes failed:** Question the architecture (see Phase 4.5)

## your human partner's Signals You're Doing It Wrong

**Watch for these redirections:**
- "Is that not happening?" - You assumed without verifying
- "Will it show us...?" - You should have added evidence gathering
- "Stop guessing" - You're proposing fixes without understanding
- "Ultra-think this" - Question fundamentals, not just symptoms
- "We're stuck?" (frustrated) - Your approach isn't working

**When you see these:** STOP. Return to Phase 1.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question pattern, don't fix again. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare | Identify differences |
| **3. Hypothesis** | Form theory, test minimally | Confirmed or new hypothesis |
| **4. Implementation** | Create test, fix, verify | Bug resolved, tests pass |

## When Process Reveals "No Root Cause"

If systematic investigation reveals issue is truly environmental, timing-dependent, or external:

1. You've completed the process
2. Document what you investigated
3. Implement appropriate handling (retry, timeout, error message)
4. Add monitoring/logging for future investigation

**But:** 95% of "no root cause" cases are incomplete investigation.

## Before you return

Run this check on the output. If any item fails, fix or HOLD — do not hand over a patch.

- Intake was complete, or you HOLDed on the missing item
- Phase 1 named a root cause with evidence, or you HOLDed
- You did not propose a fix before that root cause
- A single hypothesis was tested; failed-hypothesis code was reverted
- A failing reproduction existed before the production change
- The change is one change, at the source, not a symptom workaround
- Neighboring tests still pass, or you said which ones you could not run
- You did not attempt a fourth fix after three failures
- You did not stall because a companion file was missing
- Production / data-loss / security surfaces still need a human yes if you touched them

## What this process changes

The recipe is not a neutral mirror. Running it changes the work:

- **The first failing test can become the whole object.** Phase 4 requires a reproduction before the fix. That test then defines "done." A production failure that is wider than the first test you wrote will be treated as fixed when that test goes green. The recipe narrows the bug to whatever you happened to encode first.
- **The architecture gate can delay a simple fix.** After three failed attempts the recipe forbids a fourth and asks whether the pattern is sound. The third failure may have been a bad hypothesis, not a bad architecture. The gate will hold a one-line fix hostage to an architecture conversation the partner did not ask for.
- **Smallest-change can hide a bad root.** Phase 3 says change one variable. A tiny patch that makes the reproduction pass can confirm a local symptom while the real source sits one layer up. "It went green" is not "we found the source." The recipe rewards the smallest change that silences the current test.
- **Instrumentation is not free observation.** Boundary logs, extra env dumps, and stack prints change timing, payload shape, and which path runs. The failure you then "see" may be the instrumented system, not the original one. Investigator fixation follows the first layer that looks wrong.
- **Working-example comparison makes "match the working one" the goal.** Phase 2 will pull the broken path toward the nearest similar code, including its accidents. Differences you listed become the fix list even when the working example is itself wrong for this case.
- **Completing Phase 1 before any patch delays an already-named one-line root.** When the error, the line, and the recent commit already name the cause, the ceremony still forbids the patch until the rest of the checklist is ticked. That is the recipe spending time the failure does not need.
- **Companion files, if used, pull the work onto their objects** (a tracing writeup, a TDD loop, a verification ritual). This file is enough. Using them changes what gets discussed.

What still needs a human, and cannot be supplied by this recipe: whether the first failing test is the right object; whether three failed fixes are architecture or three bad hypotheses; whether to ship the smallest confirmed change or keep looking; whether "no root cause" is truly environmental; any production, data-loss, or security change; and whether to refactor the pattern instead of fixing it. The output is an investigation plus one change, or a HOLD. It is not a decision to ship.

## Supporting Techniques

These techniques are part of systematic debugging and available in this directory. They are optional. If a file is missing, use the method card and the quick versions above.

- **`root-cause-tracing.md`** - Trace bugs backward through call stack to find original trigger
- **`defense-in-depth.md`** - Add validation at multiple layers after finding root cause
- **`condition-based-waiting.md`** - Replace arbitrary timeouts with condition polling
