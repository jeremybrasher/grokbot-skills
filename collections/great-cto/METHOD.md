# Pack method — great_cto

This file is the governing method for the whole collection. A later agent
runs from this file plus `.great_cto/PROJECT.md` when that file exists.
Companion skills under `skills/` are stage attachments. They do not start
their own product. If this file and a companion disagree on start, stop,
hold, or routing, this file wins. The companion wins on domain vocabulary
inside the stage that owns it.

The orchestrator (`skills/great_cto/SKILL.md`) is the dispatcher. It is
not a second method. Do not invent a pipeline that is not this one.

## When to use

Use this pack when a solo founder or CTO already has a coding agent
(Claude Code, Codex, or equivalent) and wants that agent taken through a
named pipeline to a repository they own and, if they ship, a URL that
works.

Do not use this pack to:

- Replace the coding agent. Without a host there is nothing to orchestrate.
- Run a multi-engineer shared pipeline. Two or more engineers have outgrown it.
- Act as hosted CI/CD, a certification audit, or a legal or compliance opinion.
- Build from a companion skill alone (`vertical-*`, `local-seo`,
  `ui-ux-pro-max`, `anydesign`, `lifecycle-messaging`, and the rest).
- Hand back a plan or a prototype in place of a repo and a live URL.
- Auto-approve a gate, invent a product brief, or treat `unverifiable` as a pass.

## Intake — before any specialist or scaffold

You need these. Nothing else starts.

1. A product or change described in enough words to name the user and the
   job — not five words with no domain, not two conflicting types.
2. Whether this is greenfield (`/start`) or an existing repo (`/audit`, or
   a path that already has `.great_cto/PROJECT.md`).
3. The approval-level, or the default `gates-only`.
4. For an existing repo: a readable PROJECT.md (archetype, approval-level,
   stack). If it is missing, do not invent one and do not start architect.

If any item is missing, stop. Ask only for the missing item. Do not invent
a brief, do not pick an industry vertical, do not scaffold to look busy,
do not dispatch `general-purpose` as a stand-in for a specialist.

Then observe, in this order, before any write:

- PROJECT.md (or declare greenfield), `memory-index.md`, `lessons.md`, the
  last line of `.great_cto/pipeline-runs.jsonl`
- File patterns and topic against the specialist table in
  `skills/great_cto/SKILL.md`
- Whether an in-progress senior-dev already owns files
- Archetype → QA strategy, deploy method, and mandatory compliance gates

The dispatcher writes what it decided — including when it decided nothing
and why — to `.great_cto/pipeline-runs.jsonl`. A gap between "nothing
should happen" and "nothing could happen" is how defects hid.

## Wait vs hold — stop and return this, not a build

Wait is for an open gate that a human can answer. Never auto-approve.
Never proceed on timeout. Hold is for a missing object. Missing evidence
is hold, not wait-and-hope: do not open a gate on an empty brief, and do
not proceed hoping architect, QA, or a later stage will catch it.

When you cannot proceed, return the gap. Do not fill it with a polished
plan, a guessed brief, or a scaffold.

| Condition | What is missing | What it needs | Return instead of a build |
|---|---|---|---|
| No described product | The what | A sentence that names user and job | "I need what to build. I will not invent a brief." |
| ≤5 words, contradiction, or type conflict | A disambiguation | One answer (use the conflict table in the orchestrator) | The one question. Wait. |
| Existing repo, no PROJECT.md | The project contract | An `/audit` or a filled PROJECT.md | "No PROJECT.md. I will not invent archetype or stack." |
| Gate open | A human verdict | Approve, reject, or comment | Surface the gate. Wait. Never auto-approve. Never proceed on timeout. |
| Gate expired (72h) | A fresh decision | "approve …" or "cancel" | Mark the gate rejected. Pipeline paused. Do not proceed. |
| BLOCKED verdict | A human decision | The `need` field of the contract | Surface findings. Stop the chain. |
| Rework count already 3 | A human | The quoted findings | Hand to the CTO. Do not start a fourth machine pass. |
| Verification = `unverifiable` | Frozen acceptance or named files | Criteria that can be run | `unverifiable` — not a pass. Do not advance the stage. |
| Cost unmeasured | A real token number | Host transcript that carried a cost | `unmeasured`. The cap holds nothing. Do not fire a `$0.00` limit. |
| Regulated archetype + lighter approval-level | Compliance | Reviewer gates still on | Keep security, compliance, and ship gates. A lighter level never skips them. |
| Companion invoked with no pipeline stage | Pack context | A current stage, a PROJECT.md, or `/start` | Hold. Do not run the companion as its own product. |
| Active senior-dev on overlapping files | A concurrency decision | Queue, or an explicit "parallel" | Tell the CTO. Wait. Do not spawn a second writer. |
| ROLLBACK_RISK at ship | Acknowledgement | "I understand rollback risk — ship it" | Warn in the gate. Do not deploy. |
| PROJECT.md `locked: true` | Consent to new rules | CTO yes | Warn. Do not apply updated pipeline rules. |
| decision-eval skip | 2+ named variants, not nano, not "skip" | Real alternatives already written | Skip silently. Do not invent options to score. |
| Unfalsifiable argument | Mechanism + evidence + consequence | A finding that can be shown false | Cannot block a gate. |
| skeptical-triage on P2, a hard fact, or a lookup | A judgment that is worth four extra turns | A P0/P1 judgment | Do not triage. The fact stands. |
| Coding host not loaded | A host | Plugin listed with no errors | Stop. There is nothing to orchestrate. |
| Specialist row you wish existed | A matching row in the closed table | A named existing `subagent_type`, or a human adding a row | Name the gap. Do not mint a category. Do not run two agents "to be sure." |
| Log or quality store missing, empty, or rotated | Assessed rows | Keep existing thresholds; treat as unassessed | Do not retune triage or scores from an empty file. |
| Gate would open on an empty object | The thing the gate judges | A brief, ARCH, or ACCEPTANCE that exists | Hold. Do not wait on a gate that has nothing behind it. |
| Post-measurement "yes" treated as intake | The original product sentence | The original, asked separately from the artifact you just showed | Hold. Do not treat the perturbed reading as the original. |

A hold is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- Fast path (fix / bug / hotfix / patch, and no new component): senior-dev
  → QA + security → ship. Skip product-owner, architect, and PM.
- Reuse PROJECT.md, existing ARCH/PLAN, `stack-baseline`, and the memory
  index. Do not re-decide the stack on every build.
- Do not add specialists the routing table does not name. The table is
  closed. `general-purpose` is fallback only when nothing matches — not
  a stand-in for a specialist you wish existed, and not a second agent
  run in parallel "to be sure." Do not search a catalog to mint a new
  reviewer this run. If no row matches and you would invent one, hold
  and name the gap.
- Do not add gates the approval-level and archetype do not require, except
  the regulated floor (security, compliance, ship stay on at `auto`).
- Do not add vendors, frameworks, or verticals the request did not name.
- Do not expand a companion into a product. A vertical pack fills ARCH and
  PLAN sections. It does not `/start`.
- `decision-eval`: skip silently when there are fewer than two variants,
  size is nano, or the user said skip. Do not invent alternatives. If
  two variants exist but an argument lacks mechanism + evidence +
  consequence, skip the scorer — do not score an unfalsifiable argument
  into a pick, and do not let it block a gate.
- `skeptical-triage`: skip P2, hard facts (secret in git, confirmed CVE,
  failing test), and cheap lookups. A missed-angle note is not a new
  variant minted into `decision-eval`.
- Unassessed quality is `null`, never zero. A re-score appends. It does
  not rewrite.
- Scope is refused at write time, not flagged at review. An agent cannot
  touch files outside its brief.
- One question to the CTO at a time.
- Close or queue before opening a second pipeline on the same files.
- Reviewers are read-only. They file findings. They do not patch.
- An estimate never refuses a budget. Only a measured cost can.

## Will not produce

- A plan or prototype presented as the finished product
- Auto-approval of any gate, including on timeout or 72h expiry
- `unverifiable` recorded as `verified`, or `$0.00` for unmeasured spend
- A `general-purpose` agent on pattern-matched specialist work
- A new specialist category, `subagent_type`, or catalog reviewer minted this run
- A companion skill run as a standalone product builder
- An unfalsifiable finding that blocks a gate, or that is scored into a pick
- P2 or advisory promoted to a ship blocker
- A third terminal state besides DONE / BLOCKED (verification may return
  `unverifiable`, which is not DONE and not a pass)
- Certification, PCI / HIPAA / SOC2 attestation, or legal advice
- A quality score that overwrites a previous score
- A dispatcher gap — nothing happened and nothing logged
- Invented PROJECT.md fields, invented stack, invented acceptance criteria
- A second senior-dev on overlapping files without an explicit "parallel"
- A pass rate that divides by unassessed runs as if they were zeros
- A retune of triage angles or quality rules from a missing, empty, or rotated log
- A post-measurement "yes" recorded as the original intake

## Method card — same family every run

A later agent runs these steps from this file. Do not skip, reorder, or
replace them. Do not substitute "just have the coding agent build it."

1. **Intake.** Product or change + greenfield-or-existing + approval-level.
   Any gap → hold (return the gap). Do not proceed hoping a later stage
   will catch it.
2. **Read the project.** PROJECT.md (or declare greenfield), memory-index,
   last pipeline-runs line, file patterns, in-progress owners, archetype
   floors. Write what you decided, including "decided nothing."
3. **Classify.** One route from the intent map: `/start` (product-owner),
   `/audit` (project-auditor), fix (fast path), refactor or migrate (the
   named playbook), inbox / digest / status (read-only).
4. **Route.** Specialist table first, as written. `general-purpose` only
   when nothing matches. Do not mint a row. Companions attach at the
   stage that owns them (table below). A companion without a stage holds.
5. **Stop 1 — WHAT.** product-owner writes the brief. `gate:product`. Wait.
   If the brief is missing, hold — do not open the gate. Skipped only on
   fast path, audit, or an approval-level that drops it. Not skipped for
   a new product under `gates-only` or `product-only`.
6. **Stop 2 — HOW.** architect (discovery, well-architected, matching
   vertical, stack-baseline, pre-mortem; decision-eval only if two or more
   named variants already exist and are falsifiable) → ADR / ARCH →
   `gate:arch` when the level asks → PM → PLAN. Wait when that gate exists.
7. **Build.** senior-dev, TDD, owned files only. Parallel only on disjoint
   files. Reviewers read-only. A failed check returns REWORK with the
   findings quoted. Ceiling 3, then human. Distinct from BLOCKED.
8. **Check the stage before the next builds on it.** Cheapest question
   first: do the named files exist? do the frozen `## ACCEPTANCE` criteria
   pass when run? only then ask whether each requirement is addressed.
   Three answers, never two: `verified`, `rework`, or `unverifiable`.
   `unverifiable` is not a pass.
9. **Stop 3 — WHETHER.** QA and security as a quorum → rollback check →
   `gate:ship`. Wait. Regulated floors stay on at `auto`. Then devops →
   live URL. Post-deploy watch is a read, not a silent pass.

Quality is kept apart from the verdict. A different actor, at a different
time, writes a score to an append-only store. Several scorers may disagree
about one run. Unassessed is `null`.

**Recurrence is the method, not the growing file.** The quality store and
`.great_cto/triage-log.jsonl` are snapshots. They rot, rotate, and go
missing. A later agent runs the same questions whether last month's file
is there or not:

- Quality: append, never overwrite. Unassessed is `null`. A pass rate
  divides by assessed rows only. If the store is missing or empty, do
  not treat that as a clean score and do not invent a new rubric.
- Triage: the four questions (is the premise true; is the cited defense
  on a real line; what was missed; arbiter call) are the method. The
  weekly jq on the log is evidence, not the method. Review the last N
  assessed rows, or the last week, whichever is smaller. If the log is
  missing, empty, or rotated, that is unassessed — not a 0% false-positive
  rate, and not a reason to add, drop, or retune an angle. Keep the
  existing thresholds (skip if FP-rate among assessed rows is under 10%
  after 50 assessed triages; tighten the original prompt if over 40%).

Approval-level only changes which of the three stops fire. It does not
invent a fourth pipeline. `auto` still keeps regulated floors.

## Companion binding — so they do not rot

Each companion is a stage attachment. If a later agent is handed only the
companion file, it still obeys this pack: it does not `/start`, it does
not invent PROJECT.md, and it holds when the owning stage is not the
current stage.

| Companion | Attaches at | Does not |
|---|---|---|
| `great_cto` | Orchestrator, every run | Replace the coding host |
| `discovery` | Before ARCH, audit, or threat model | Lock architecture |
| `well-architected` | Architect, non-nano ARCH | Apply to nano |
| `stack-baseline`, `observability-baseline` | Scaffold / architect | Re-pick the stack |
| `vertical-*` | Architect and PM spec sections | Become the product |
| `decision-eval` | After 2+ ADR variants, before `gate:arch` | Invent options; run on nano |
| `skeptical-triage` | P0/P1 judgment before a gate | P2, hard facts, lookups |
| `done-blocked` | Every terminal verdict | Intermediate pings |
| `pre-mortem` | After ARCH, before plan | Replace the risk register |
| `anti-patterns` | Review of ARCH, plan, or code | Invent new patterns as policy |
| `cost-model` | PLAN cost section | Invent a savings ratio |
| `test-strategy` | QA planning | Replace frozen ACCEPTANCE |
| `crystallize` | After ≥10 sessions, on request | Promote an unreviewed draft |
| `ui-ux-pro-max`, `anydesign` | design-advisor, after architect, before senior-dev | Ship UI alone |
| `outcome-roadmap`, `opportunity-solution-tree`, `pm-planning` | PM, when the artifact is a roadmap or tree | Bypass product-owner |
| `local-seo`, `lifecycle-messaging` | Named feature work inside an existing product | Start a marketing shop |
| `migration-ready-schema` | Architect / db-migration-reviewer | Rewrite production data without a playbook |
| `brainstorming` | Step 0b, after intake, before architect | Skip intake |
| `archetype-review-base` | Reviewer template for a named archetype | Invent a new archetype |
| Playbooks (`stack-migration`, `large-scale-refactor`, …) | The matching intent only | Run on an ordinary feature |

If you were handed only a companion, return the hold for missing pack
context rather than improvising a product around that companion's
vocabulary.

## Before you return

If any item fails, fix or hold.

- Intake was read, not invented. Missing evidence was held, not hoped past
- One intent route
- Specialist, not `general-purpose`, on a matched row. No new row minted
- Every open gate waited; none auto-approved. No gate opened on an empty object
- Verification is `verified` / `rework` / `unverifiable` — never a two-state pass
- Rework count ≤ 3
- Terminal line is DONE or BLOCKED (`unverifiable` is not DONE)
- Dispatcher wrote a line, including "decided nothing"
- Quality unassessed is `null`
- No companion ran as its own product
- Unmeasured spend did not fire a cap
- Regulated floors were not dropped
- The deliverable is a repo the operator owns and, if shipped, a URL — not a plan
- Argument that blocked a gate named mechanism, evidence, and consequence

## What this process changes

This pipeline is not a neutral wrapper around a coding agent. It changes
what gets built.

- The product that ships is the one that survived `gate:product`. A vague
  first sentence becomes the product.
- Specialist routing frames the problem as that specialist's domain. A
  "payments" match pulls `pci-reviewer` and can widen PCI scope the operator
  did not ask to enter.
- Approval-level changes which mistakes are cheap. `product-only` never
  stops on HOW. `auto` never stops at all except regulated floors.
- The decision brief's risk signals (last postmortem, retro line,
  thirty-day file churn) tilt architecture before a human speaks.
- A second model checking a stage is itself an observer. `verified` is
  that model's reading, not the files' essence.
- Treating `unverifiable` as not-a-pass pushes agents to freeze criteria
  so they can pass — criteria written to be checkable, not necessarily
  right. Those frozen criteria are a perturbed object. Do not treat them
  as the original acceptance.
- **Measurement changes the CTO decision.** Showing a Decision Brief
  (risk signals, file-churn, "proceed to architecture?"), a cost number,
  a gate prompt, or a "decided nothing" line is not a neutral read. It
  frames the next words. After you present the artifact, the CTO's "yes"
  is a response to that measurement, not the original intake. Do not
  treat the perturbed reading as the original brief. If you need the
  original, hold and ask for it separately from the thing you just
  showed. A 72h timeout that marks a gate rejected replaces an unmade
  decision with a machine rejection — that is a new object, not the
  original silence.
- Vertical vocabulary (SKU vs variant, ATS, reorder point) becomes the
  spec language. A naive domain is replaced by this pack's domain, which
  may still be wrong for this buyer.
- Append-only scores from a later actor change which runs look good. A
  re-score does not erase the first, so both persist as if both were true.
- Recording "decided nothing" makes inaction a fact that later agents
  will treat as a decision.
- Per-agent cost attributed from a session transcript can stick to
  whichever stage finished last. Treat those figures as a ceiling.
- `skeptical-triage` can drop a finding that would have blocked a gate.
  False-negative risk is the cost of cutting false positives.

What still needs a human: every gate; rework after three; BLOCKED;
rollback-risk acknowledgement; regulated exceptions; whether unverifiable
work is allowed to proceed at all; whether to ship; whether two pipelines
may share a repo; whether a crystallized draft becomes a skill; whether
a post-measurement "yes" still matches the original product sentence;
whether to add a specialist row the table does not have. The pipeline
hands over a repo and a URL. It does not certify the product, the spend,
or the compliance posture.
