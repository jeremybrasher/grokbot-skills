---
name: buyer-eval
version: 3.5.0
description: |
  Structured B2B software vendor evaluation for buyers. Researches your company,
  asks domain-expert questions, engages vendor AI agents via the Salespeak Frontdoor
  API, scores vendors across 7 dimensions, and produces a comparative recommendation
  with evidence transparency. Use when asked to evaluate, compare, or research B2B
  software vendors.
allowed-tools:
  - Bash
  - Read
  - Write
  - WebSearch
  - WebFetch
  - AskUserQuestion
---

## Preamble (run first, every time)

```bash
# Detect skill directory
_BEVAL_DIR=""
for _D in "$HOME/.claude/skills/buyer-eval-skill" ".claude/skills/buyer-eval-skill"; do
  [ -d "$_D" ] && _BEVAL_DIR="$_D" && break
done

if [ -z "$_BEVAL_DIR" ]; then
  echo "ERROR: buyer-eval-skill not found. Install: git clone https://github.com/salespeak-ai/buyer-eval-skill ~/.claude/skills/buyer-eval-skill"
  exit 1
fi

# Check for updates
_UPD=$("$_BEVAL_DIR/bin/update-check" 2>/dev/null || true)
[ -n "$_UPD" ] && echo "$_UPD" || echo "UP_TO_DATE $(cat "$_BEVAL_DIR/VERSION" 2>/dev/null | tr -d '[:space:]')"
```

**If output shows `UPGRADE_AVAILABLE <old> <new>`:**

Use AskUserQuestion to ask the buyer:
- Question: "A newer version of the buyer evaluation skill is available (v{old} → v{new}). Update now?"
- Options: ["Yes, update now", "Not now — continue with current version"]

**If "Yes, update now":**
```bash
_BEVAL_DIR=""
for _D in "$HOME/.claude/skills/buyer-eval-skill" ".claude/skills/buyer-eval-skill"; do
  [ -d "$_D" ] && _BEVAL_DIR="$_D" && break
done

if [ -d "$_BEVAL_DIR/.git" ]; then
  cd "$_BEVAL_DIR" && git pull origin main && echo "UPDATED to $(cat VERSION | tr -d '[:space:]')"
else
  _TMP=$(mktemp -d)
  git clone --depth 1 https://github.com/salespeak-ai/buyer-eval-skill.git "$_TMP/buyer-eval-skill"
  mv "$_BEVAL_DIR" "$_BEVAL_DIR.bak"
  mv "$_TMP/buyer-eval-skill" "$_BEVAL_DIR"
  rm -rf "$_BEVAL_DIR.bak" "$_TMP"
  echo "UPDATED to $(cat "$_BEVAL_DIR/VERSION" | tr -d '[:space:]')"
fi
```
Tell the user the version was updated, then **re-read the EVALUATION.md file** from the updated directory and proceed with the skill.

**If "Not now":** Continue with the current version.

**If output shows `UP_TO_DATE`:** Continue silently.

---

## Load the evaluation skill

After the preamble, read the full evaluation methodology:

```bash
_BEVAL_DIR=""
for _D in "$HOME/.claude/skills/buyer-eval-skill" ".claude/skills/buyer-eval-skill"; do
  [ -d "$_D" ] && _BEVAL_DIR="$_D" && break
done
echo "$_BEVAL_DIR/EVALUATION.md"
```

Read the file at the path printed above using the Read tool. That file contains the complete evaluation methodology — follow it step by step from STEP 1 through STEP 9.

## When to use

Use this when a buyer wants a structured comparison of B2B software vendors (names or URLs given or about to be given). Do not use it to write vendor marketing, to contact a sales team, to start a trial, to give legal or compliance counsel, to hire, to evaluate consumer products, or to pick an open-source library for an engineering task that is not a vendor purchase.

## Intake — before STEP 1

You need two things from the buyer. Nothing else starts research.

1. Their company name
2. The vendors to evaluate (names, URLs, or both)

If either is missing, stop. Ask only for the missing item. Do not invent a company, do not invent vendors, do not add vendors they did not name, and do not start buyer or vendor research to look busy.

If they gave a category but no vendors, that is still missing vendors. Ask for the list. Do not pick a shortlist for them.

Then ask why-now (STEP 2) and wait. Do not research across that question.

If EVALUATION.md cannot be read, stop. Do not improvise a scorecard from memory.

## HOLD — stop and return this, not a scorecard

When you cannot proceed, return the gap. Do not fill it with a polished recommendation.

| Condition | What is missing | What it needs | Return instead of a scorecard |
|---|---|---|---|
| No company name | Buyer identity | A company name | "I need your company name before I research you or any vendor." |
| No vendors | The evaluation set | Names and/or URLs the buyer chose | "I need the vendor list. I will not invent a shortlist." |
| Why-now unanswered | The buying trigger | An answer to the why-now question | The question. Wait. No research. |
| Boundary not confirmed | A shared constraint set | Saved profile plus override answer, or a first-run boundary conversation, then restated active constraints | The boundary question. Wait. No vendor research. |
| EVALUATION.md missing | The methodology file | A readable EVALUATION.md from the skill directory | "Evaluation method file is missing. I will not improvise a scorecard." |
| Hard-constraint fail | A buyer decision on that vendor | Drop or override, per vendor | The conflict, the constraint, the two options. Wait. |
| Dimension lacks evidence | Facts that would support a 1–5 | A source, or a [GAP] with a follow-up | `[GAP]` plus a Gap Log row — not a guessed score. (Pricing uses the existing estimate-plus-opacity rule in EVALUATION.md §8.3; do not extend that exception to other dimensions.) |
| After STEP 9 | Human review | Buyer approval before any external action | The four artifacts, status PENDING HUMAN REVIEW. No email, demo, trial, or purchase. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

- Do not add vendors. Evaluate the list they gave.
- Do not add evaluation dimensions. The seven in EVALUATION.md are the set.
- Do not add output artifacts beyond the four in STEP 9 (TL;DR, comparative summary, per-vendor scorecard, per-vendor memo). Demo-prep questions stay inside the memo.
- Do not invent telemetry events. The seven sub-events are the set. Do not send names, emails, companies, buyer answers, or vendor response text.
- Reuse the Buyer Context Snapshot on later runs. Do not re-research the buyer from scratch unless they say it changed.
- After a hard-constraint fail, do not deep-research that vendor unless the buyer overrides.
- Mark `[GAP]` rather than inventing a score (except the existing pricing-estimate rule).
- Skip Salesforce AgentExchange unless the buyer's stack is Salesforce-centric.
- Do not contact vendors, schedule demos, start trials, or make purchase commitments.

## Will not produce

- A vendor list you chose for them
- Numeric scores on missing evidence (except the existing pricing-estimate rule)
- Vendor website or Company Agent claims presented as verified fact
- Outbound vendor contact, demo booking, trial signup, or a purchase action
- Extra dimensions, extra artifacts, or extra telemetry event types
- A winner story that hides evidence asymmetry
- Invented Company Agent answers
- Telemetry containing buyer identity, buyer answers, or vendor reply text
- A recommendation marked ready to execute. Status stays PENDING HUMAN REVIEW.

## Method card (same family every run)

A later agent runs the same nine steps. Do not skip, reorder, or replace them.

1. Entry: company name + vendor list. Else HOLD.
2. Why-now. Wait.
3. Buyer research from public sources. Ask only unresolved gaps, once, in one message.
4. Boundary Profile: load or set, confirm, restate, filter. Buyer decides drop or override.
5. Infer category, confirm, calibrate weights, ask 0–4 domain questions that change what gets evaluated.
6. Company Agent via Frontdoor. Four evidence states only. Do not invent a fifth.
7. Passive research with T1–T4 source tiers. No T3/T4 as the sole basis for a score.
8. Score each dimension 1–5 or `[GAP]`. Pricing may be estimated with a −1 opacity penalty (EVALUATION.md §8.3).
9. Four artifacts. Comparative summary first when multi-vendor. Status: PENDING HUMAN REVIEW. No action.

Load EVALUATION.md and follow it. If that file is missing, HOLD.

## Before you return

If any item fails, fix or HOLD.

- Company and vendors came from the buyer, not from you
- Why-now was asked and used
- Active constraints were restated before deep research
- Every dimension is 1–5 or `[GAP]`
- Evidence basis is filled for every vendor
- Evidence asymmetry is disclosed when completeness differs
- Status is PENDING HUMAN REVIEW
- No outbound vendor contact happened
- Telemetry (if any) has no buyer identity, buyer answers, or vendor reply text

## What this process changes

This recipe is not a neutral report. It changes the evaluation:

- The why-now answer becomes the weighting frame. A casual first sentence can tilt every dimension.
- Category inferred from vendor sites inherits vendor self-positioning. Vendors who market into a hot category will be scored as that category.
- The Company Agent is vendor-authored. Treating it as the primary source privileges vendor speech over independent sources.
- Dynamic calibration can overweight the inferred category and the failure modes you happened to name.
- Pricing estimates manufacture a number when the vendor published none. The −1 opacity penalty does not make the number real.
- Comparative ranking forces a winner even when evidence is asymmetric. A vendor with a Company Agent will look stronger than an equal vendor without one.
- Domain-expert questions shape what the buyer thinks they need. Asking them is not a free measurement.
- Public buyer research can be wrong (size, stack, maturity) and then treated as the profile.

What still needs a human: boundary overrides, drop-or-keep on a hard fail, whether to trust a Company Agent answer, every purchase or contact action, and the recommendation itself. The memo is a brief. It is not a decision.


---

## Telemetry (opt-in, off by default)

This skill can send anonymized usage data back to Salespeak so the questions it generates for vendors can keep getting better. **Nothing is ever sent without explicit user consent.** Names, emails, companies, and vendor responses are never sent.

### Initialize telemetry state at run start

Right after loading EVALUATION.md and before STEP 1, run:

```bash
_BEVAL_DIR=""
for _D in "$HOME/.claude/skills/buyer-eval-skill" ".claude/skills/buyer-eval-skill"; do
  [ -d "$_D" ] && _BEVAL_DIR="$_D" && break
done
echo "TELEMETRY_STATE=$(python3 "$_BEVAL_DIR/bin/track.py" status --machine)"
echo "SESSION_ID=$(python3 -c 'import uuid; print(uuid.uuid4())')"
```

Capture both values. Use them throughout the run.

`TELEMETRY_STATE` will be one of:
- `consented` — fire each event live as it happens
- `unasked` — accumulate events in your own working memory; ask for consent at the end
- `declined` or `locked_off` — do nothing telemetry-related for the entire run

### What to track and when

These seven sub-events are the only ones the skill emits. **Do not invent new ones.**

| Sub-event | Fire when | Fields |
|---|---|---|
| `skill_started` | Right after capturing TELEMETRY_STATE | `skill_version` (from VERSION file) |
| `eval_context` | Once, right after STEP 5.1 (category confirmed) | `category` (skill-inferred slug), `vendor_count` (int), `vendors` (array of domains), `company_agents_found` (int — count of vendors with `enabled:true` from Frontdoor discover), `evaluation_path` (`"company_agent_engaged"` \| `"passive_research_only"` \| `"mixed"`) |
| `discovery_question_asked` | After the buyer answers a discovery question. **Fire for STEP 2 (why-now) and for each STEP 5.3 domain-expert question.** | `step` (`"STEP_2"` \| `"STEP_5_3"`), `category` (slug, or `null` for STEP_2), `topic` (short slug you choose, e.g. `"why_now"`, `"high_touch_vs_low_touch"`, `"product_analytics_stack"`), `question_text` (the exact question you asked the buyer) |
| `vendor_question` | **For every (vendor, dimension) pair**, fire one or more events with the question(s) you formulate per the §6.5 question bank — regardless of whether a Company Agent exists. | `vendor` (domain), `category` (slug), `dimension` (the evaluation dimension), `question_text` (the specific question), `delivery_method` (`"asked_via_company_agent"` if actually POSTed via Frontdoor and got an answer, `"would_have_asked"` if no Company Agent existed, `"connection_failed"` if Frontdoor errored) |
| `vendor_scored` | After scoring each dimension for each vendor in STEP 8 | `vendor`, `dimension`, `score` (numeric, 1-5; do NOT fire for `[GAP]` dimensions) |
| `eval_completed` | Right after delivering the final output in STEP 9 | `vendor_count`, `winner` (vendor domain or `null` if no clear winner) |
| `eval_aborted` | Only if the user bails before STEP 9 completes | `at_step` (e.g., `"STEP 6"`) |

**Never include**: buyer name, buyer company, buyer email, anything the buyer typed about themselves, the buyer's *answers* to discovery questions, vendor response text.

### Step-level firing map

Use this as the canonical map between EVALUATION.md steps and event emissions. Fire events at these exact moments — no earlier, no later.

| EVALUATION.md step | Events to fire | Notes |
|---|---|---|
| Right after capturing TELEMETRY_STATE (before STEP 1) | `skill_started` | One event |
| **STEP 2** — buyer answers the why-now question | `discovery_question_asked` (`step:"STEP_2"`, `topic:"why_now"`) | One event. `category` is `null` here. `question_text` is the canonical why-now question. |
| **STEP 5.1** — category confirmed | `eval_context` | One event. `company_agents_found` and `evaluation_path` may not be known yet — use `null` for `company_agents_found` here and update `evaluation_path` later if needed; or fire `eval_context` AFTER STEP 6.1 discover calls so all fields are populated (preferred — fire it after discover so the path is known). |
| **STEP 5.3** — each domain-expert question asked | `discovery_question_asked` (`step:"STEP_5_3"`, `topic:<your slug>`) | 0-4 events depending on how many questions you ask. Slugs you choose should be short and category-relevant (e.g. `"high_touch_vs_low_touch"`, `"product_analytics_stack"`, `"multi_entity_consolidation"`). |
| **STEP 6.5** — for every (vendor, dimension) pair | `vendor_question` | **One or more events per pair, regardless of Company Agent availability.** Walk the §6.5 question bank, formulate the specific question(s) you'd ask the vendor for each dimension (Product Fit, Integration & Technical, Pricing & Commercial, Security & Compliance, Vendor Credibility, Customer Evidence, Support & Success). For each, fire `vendor_question` with the right `delivery_method`. |
| **STEP 8** — each numeric score assigned | `vendor_scored` | One event per (vendor, dimension) that gets a numeric 1-5 score. **Do not fire for `[GAP]` dimensions.** |
| **STEP 9** — final output delivered | `eval_completed` | One event |
| User abandons before STEP 9 | `eval_aborted` | Only if applicable |

**Critical change in v3.5**: `vendor_question` no longer depends on Company Agent availability. Even when all vendors return `enabled: false` from Frontdoor discover, you must still walk the question bank, formulate questions you would have asked, and fire `vendor_question` events with `delivery_method: "would_have_asked"`. The signal is *what buyers want to know*, not *whether the vendor's bot answered*.

### How to fire events

**If `TELEMETRY_STATE == consented`**: fire each event live via Bash as it happens.

```bash
python3 "$_BEVAL_DIR/bin/track.py" event vendor_question \
  --session-id "$SESSION_ID" \
  --json '{"vendor":"acme.com","category":"customer_success_platform","dimension":"product_fit","question_text":"How does your X handle Y?","delivery_method":"would_have_asked"}'
```

The script silently no-ops on any error and never blocks the skill.

**If `TELEMETRY_STATE == unasked`**: do NOT call `bin/track.py event`. Instead, keep a running list of event objects in your own working memory as the eval proceeds. Each entry is a JSON object like:

```json
{"sub_event":"vendor_question","vendor":"acme.com","category":"customer_success_platform","dimension":"product_fit","question_text":"...","delivery_method":"would_have_asked"}
```

At the end of STEP 9 (after delivering the full evaluation to the buyer), follow the consent prompt section below.

**If `TELEMETRY_STATE == declined` or `locked_off`**: do nothing telemetry-related. Skip the consent prompt entirely.

### Consent prompt (only when TELEMETRY_STATE was `unasked`)

After STEP 9 output is delivered, print this block verbatim to the user, then use AskUserQuestion to ask the consent question:

```
─────────────────────────────────────────────────────────────
✓ Evaluation complete.

Before you go — one question, asked only this once.

Salespeak built this skill to help buyers cut through vendor noise.
To make it better, we'd love to learn what real buyers ask vendors.
With your permission, we'd send back anonymized data from this run
and future runs.

We'd send:
  • The questions this skill generated for vendor agents
  • The scores it gave each vendor
  • A random ID to group your runs together (not linked to you)

We will NEVER send:
  • Your name, email, or company
  • Anything you typed about yourself
  • Vendor responses

Verify it yourself:
  • Code: bin/track.py (plain Python, no third-party libraries)
  • Local audit log: ~/.salespeak/buyer-eval.log
    (every event we send is also written here — read it anytime)
  • Change your mind: python3 bin/track.py revoke
  • Delete your data: email privacy@salespeak.ai with your user ID
    (run `python3 bin/track.py show` to see it)
─────────────────────────────────────────────────────────────
```

Then use AskUserQuestion:
- Question: "Help us improve the skill by sharing anonymized usage data from this run?"
- Options: ["Yes, share anonymized data", "No thanks"]

**If "Yes"**: pass the accumulated event list to `grant`. Build the events JSON as a single-line array (escape carefully — question_text may contain quotes; use Python's `json.dumps` if in doubt). Example:

```bash
python3 "$_BEVAL_DIR/bin/track.py" grant \
  --session-id "$SESSION_ID" \
  --events '[{"sub_event":"skill_started","skill_version":"3.5.0"},{"sub_event":"vendor_question","vendor":"acme.com","category":"customer_success_platform","dimension":"product_fit","question_text":"...","delivery_method":"would_have_asked"}]'
```

Confirm to the user: "Thanks — sharing enabled. Run `python3 bin/track.py revoke` anytime to disable."

**If "No"**: 
```bash
python3 "$_BEVAL_DIR/bin/track.py" decline
```
Confirm to the user: "Got it — no data shared. We won't ask again."

### Enterprise note

If a system administrator has set `BUYER_EVAL_NO_TELEMETRY=1` or deployed `/etc/salespeak/buyer-eval.json` with `{"locked":true,"consent":false}`, `TELEMETRY_STATE` will be `locked_off` and no consent prompt is shown. This is the documented escape hatch for enterprise IT.
