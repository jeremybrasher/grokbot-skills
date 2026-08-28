---
name: vibe-creating-prompt
description: Judges whether a user's input suits the Vibe Creating style of video-prompt writing, and when it does, distills single-scene prompts, multi-shot descriptions, emotional imagery, or mixed input into prompts that are easier for a video model to generate from — while preserving any user-specified dialogue, voiceover, music, sound effects, and other hard constraints. Use when a user wants to turn an idea, story, feeling, or rough/over-specified prompt into a strong text-to-video prompt (Seedance, Sora, Kling, Veo, Runway, etc.), or asks to "rewrite", "improve", "clean up", or "vibe-ify" a video prompt. Observe the input first; do not invent a scene to have something to rewrite. Do NOT use for long narrative films that need precise word-for-word dialogue sync, industrial shot lists meant to be executed verbatim, functional/UI demos and step-by-step tutorials, or a request to render/generate the video itself.
license: MIT
---

# Vibe Creating Prompt Skill

## Overview

Vibe Creating distills what the user *actually wants to express* so a later video model can lock onto the visual center, the emotional direction, and the continuity of the experience. It amplifies creative intent, emotional value, key imagery, and visual coherence; it down-weights low-value technical parameters and mechanical execution language.

This skill is a *judgment-first* rewriter. It does not blindly shorten or "vibe-ify" everything. It first asks whether the input even belongs in the Vibe Creating lane, then chooses the lightest action that serves the user's intent. It writes a prompt. It does not render a clip.

## When to use

Use when the user wants a *text-to-video prompt rewritten or judged*: an idea, a story beat, a feeling, a rough prompt, or an over-specified shot script they want turned into something a video model can generate from. Triggers include "rewrite", "improve", "clean up", "vibe-ify", "make this a video prompt", or handing you a scene and asking for Seedance / Sora / Kling / Veo / Runway language.

**Do not use this to:**

- Render, generate, upscale, or edit the video itself
- Write a feature-length screenplay or a season bible
- Execute an industrial shot list verbatim (keep it; do not restyle it)
- Sync long-form dialogue word-for-word to picture
- Produce a UI demo, product-tour, or step-by-step tutorial script
- Invent a scene because the user said "make something cinematic" with no object
- Score, brand, or market the prompt; this skill only judges and (when fit) rewrites

## Intake — before any rewrite

You need three things. Nothing else starts. Do not pick a rewrite mode, do not delete a parameter, do not invent a visual anchor.

1. **A video-prompt object.** The user's idea, scene, feeling, rough prompt, or over-specified prompt — the text itself. "Make something cinematic" or a model name with no scene is not an object.
2. **Enough of that object to observe.** You can read a subject or a feeling or a shot script. A link you cannot open, or "see my other chat", is not enough.
3. **A rewrite-or-judge task.** They want the prompt judged, cleaned, rewritten, or vibe-ified. A request to *generate the clip*, to storyboard a feature, or to produce a tutorial, is a different task.

If any of those is missing, stop. Say what is missing and what you need. Do not invent a scene so you have something to rewrite.

Then, and only then, assign Scenario (S), Expression (E), and Information (I), and pick an action.

## HOLD — stop and return this, not a rewritten prompt

When you cannot proceed, return the gap. Do not fill it with a polished prompt.

| Condition | What is missing | What it needs | Return instead of a rewrite |
|---|---|---|---|
| No video-prompt object | A scene, idea, feeling, or prompt to judge | The text of the object | "I need the scene, idea, or prompt itself. I will not invent one." |
| Object unreadable | Text you can observe | Paste, file, or a link you can actually read | "I cannot see the prompt. I will not guess it." |
| Task is render / generate the video | A rewrite-or-judge request | The prompt job, or a different skill | "This skill only writes the prompt. I will not render the clip." |
| Abstract only — a mood word with no subject, object, or scene | A visual anchor | One thing that can be seen (person / object / named concept / VFX subject) | 1–3 questions. No draft unless they already named a visible thing. |
| Subject present, no action or state | One beat | One action, state, or still | Ask for the beat. Do not invent motion. |
| Fragments with no main relationship and no style direction | A through-line | Who/what relates, or one style word they choose | Ask. Do not stitch a plot. |
| Ultra-short subject+event, no style / viewing-mode / key moment, and you would have to invent one to rewrite | A direction | One of: use-case, visual style, or the moment that matters | Ask 1–3. A first pass is allowed only if the direction is already mostly clear — then ask only the critical gaps. |
| Multi-shot input with jumps you cannot see a reason for | The reason the cuts exist | The experience line, or permission to keep the jumps as written | Ask. Do not invent connective tissue. Do not flatten. |
| Long-form piece that only stands with word-level dialogue sync | A VC-fit goal | Split visual segments out, or keep as-is | Keep as-is. Explain the workflow mismatch. No VC rewrite of the dialogue. |
| Industrial shot list meant to be executed verbatim | A creative-translation goal | An explicit ask to restyle, or keep as-is | Keep as-is. Explain this is a shot-list workflow. |
| UI demo, tutorial, or step-by-step instruction | A creative-expression goal | A different task, or keep as-is | Keep as-is. VC is not recommended. |
| User asked you to invent relationships, twists, scenes, or an emotional change | Evidence in the input | A beat they wrote, or a yes that they want that addition | Refuse the invention. Rewrite only what is there, or HOLD. |
| Two visual anchors tied, and the action would be a rewrite that must pick one | A named center | They name the thing that most deserves to be seen | Ask which center. Do not silently pick. |
| User explicit keep-constraint on dialogue / VO / music / SFX / structure / parameters | Nothing — the constraint is present | Obey it | Do not HOLD. Keep the constraint. A VC version is extra, or offered only after they agree. |

A HOLD is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more.

- **Pass-through is the default** when the input already has a clear subject, structure, time relationship, core imagery, and a clear emotional goal, and the text is already strongly generation-ready. Do not rewrite to look busy.
- **Delete undeclared technical decoration** (focal lengths, camera-position jargon, speed multipliers, exact dolly distances, shot numbers the user did not ask to keep, DOF / aperture / exposure / shutter, equipment notes, pure editing instructions). Translate intent; do not replace deleted numbers with new numbers.
- **Do not add** a character, relationship, plot twist, scene, location, emotional change, style pack (cinematic, analog grain, golden hour, anamorphic), or model-preset name the input did not contain.
- **Do not expand.** Output is not meaningfully longer than input. Do not balloon an ultra-short input into long prose.
- **Do not flatten** a multi-shot experience into one paragraph, and do not number output unless they asked to keep numbers or a list.
- **Do not restyle S3.** Low-fit goals (UI, tutorial, exact dialogue-sync long-form, industrial shot list) stay as-is.
- **Sound the user wrote stays verbatim.** You may reorder picture around it. You may not reword, replace, or delete it.
- **One action, one mode.** Do not stack a rewrite on top of an optional VC version unless they asked for both.
- Extra atmosphere words, extra shots, or a "stronger" emotion need evidence in the input — not a habit of making prompts cinematic.

## Will not produce

Do not return any of the following:

- A scene you invented because the object was missing
- New character relationships, plot twists, scene details, or emotional changes
- A rewritten prompt for a long-form piece that only stands with word-level dialogue sync
- A "vibe" restyle of an industrial shot list or a UI / tutorial script, unless they explicitly asked
- Dialogue, VO, music, SFX, or lyrics the user wrote, altered or "improved"
- Shot numbers, list format, or a delivery structure they did not ask to keep — and also: do not *strip* numbers they *did* ask to keep
- Internal labels (`S1`, `E2`, "Mode 5") in the user-visible output
- A rendered clip, a storyboard of stills, or a claim that the video will match
- A seventh action label, a new rewrite mode, or an output shape other than Judgment / Action / Result / Notes
- A synonym dump of mood words in place of a visual center
- Intensity upgrades the input did not earn (quiet → melancholic, sad → tragic, product demo → hero film)

## Method card — same family every run

A later agent runs this from this file alone. There is no companion file to load. Do not stall. Do not invent a different rewriter, a style-pack, or a model-preset mapper. Do not skip, reorder, or replace these steps.

1. **Intake.** Video-prompt object + readable text + a rewrite-or-judge task. Any gap → HOLD.
2. **Assign Scenario (S).** Score the *goal*, not the formatting. Use the scoring rules in this file. One of S1 / S2 / S3.
3. **Assign Expression (E).** Score the *form of the text*. Use the scoring rules in this file. One of E1 / E2 / E3.
4. **Information check (I).** Can you name a visual anchor and an action or state? If a must-have is missing, the action is **ask first** (or a first pass plus 1–3 gaps when the direction is already mostly clear). I runs in parallel with S and E; missing info wins over a high S.
5. **HOLD scan.** If a row in the HOLD table matches, return that row's result. Do not rewrite around it.
6. **Pick one action** from the routing matrix, then apply the four hard routing rules. The six legal actions are defined below. Do not mint a seventh.
7. **Pick one rewrite mode** only if the action is light cleanup, direct rewrite, or optional VC version. Use the mode rules in this file. One mode per run.
8. **Execute the action** by its definition. Conflict order: (1) user-explicit content and hard constraints, (2) creative optimization that does not break them, (3) VC readability. Camera policy and sound policy in this file apply here.
9. **Output** in the fixed four-part shape: **Judgment / Action / Result / Notes (if any).** Never expose S/E/mode labels.
10. **Pre-return check.** Run the checklist in this file. Fail → fix or HOLD. Then return.

### How to assign S (goal, not formatting)

Read what they want the clip *for*. Ignore whether they used shot numbers.

- **S1 — VC-native.** The goal is to express a scene through story, emotion, memory, atmosphere, imagery, or experience flow, and they are not asking for verbatim industrial execution. VC clearly helps.
- **S2 — partial.** Brand, product, or character showcase, or a stylized ad. VC may help; it is optional. Do not push.
- **S3 — low fit.** UI demo, tutorial, step-by-step instruction, a long-form piece that only stands with word-level dialogue sync, or an industrial shot list meant to be executed verbatim.

If a must-keep constraint forces a low-fit workflow (exact long-form dialogue sync, execute-this-shot-list), assign S3 even when the visuals are atmospheric. Mixed goals take the lowest-fit band that covers a must-keep constraint.

### How to assign E (form of the text)

- **E1 — close to VC.** The text already reads as a vivid scene or story. Execution jargon is absent or incidental (one stray "close-up" is still E1).
- **E2 — mixed.** Creative content and execution language are interleaved (shot numbers next to emotional beats; "dolly-in" next to a memory).
- **E3 — precision control.** Shot numbers, focal lengths, movement parameters, or timecodes dominate. If half or more of the clauses are control tokens (mm, f-stop, timecode, shot #, dolly distance, A/B cam), it is E3. If control tokens appear but scene language still leads, it is E2.

Precision-control writing is not a low-fit scenario. An E3 script can still be S1.

### How to check I (density)

A strong VC prompt uses four layers. Fill whichever is missing first — do not mechanically demand all four:

1. **Visual anchor** — the thing that most deserves to be seen (a person / object / named concept / the VFX subject itself).
2. **Action or state** — what's happening (one action, state, or beat — just one).
3. **Local tonality** — how this moment *feels* (one mood word or adjective already in the input, or a close paraphrase that does not upgrade intensity).
4. **Video theme** — where the clip is used + its visual style, *if the input or the user named them*. Do not invent a use-case or a style pack.

Ask first when: there is no visual anchor; only an abstract feeling with no subject/object/scene; a subject but no action or state; fragments with no main relationship or style direction; an ultra-short input that has a subject and event but no clear style / viewing-mode / key moment and you would have to invent one; or multi-shot content with jumps you cannot see a reason for.

Ask for the minimum needed to land the chosen action, usually in one round, 1–3 questions.

### The six actions — exact meaning

Use one label, verbatim, in the Action line:

- **pass-through** — Result is the user's text unchanged. Use when the input is already strongly generation-ready (clear subject, structure, time relationship, core imagery, emotional goal). Notes omitted unless a keep-constraint was observed.
- **light cleanup** — Delete only undeclared technical decoration and repetition. Keep every beat, name, sound line, and order. Length stays within about 10% of the input. No new imagery. No new emotion.
- **direct rewrite** — One rewrite mode. One usable prompt, or 2–5 segments if the input already had them. No new characters, relationships, twists, scenes, or emotional changes. Not meaningfully longer than the input. A single segment is usually ~30–120 words; loosen this to preserve structure, dialogue, or multi-segment progression.
- **ask first** — Result is 1–3 questions for the missing layer(s). No rewrite, unless the direction is already mostly clear — then a first pass plus only the critical 1–3 gaps.
- **keep as-is** — Result is the original. Judgment names the mismatch (long-form dialogue sync / industrial shot list / UI-tutorial / other S3). No stylize. No optional VC unless they asked.
- **optional VC version** — Primary result is the original (or a light cleanup of it). A second, labeled VC version is attached. The user chooses. Do not present the VC version as the only result. Use for S2, or when they asked to see a VC take without replacing the original.

### Routing matrix (default action per S × E cell)

| | **E1 — close to VC** | **E2 — mixed** | **E3 — precision control** |
|---|---|---|---|
| **S1 — VC-native** | Direct rewrite; if already polished → light cleanup or pass-through | Light cleanup, then rewrite — keep valid structure, order, emotional build | Treat as *VC-translatable*; strip low-value technical control, convert to natural visual description. Don't reject just because it's written as an execution script |
| **S2 — partial** | Light cleanup; if already usable → pass-through | Offer an *optional* VC version; let the user choose | Keep the original intent; gently note a VC rewrite is available on request |
| **S3 — low fit** | Stay close to the original; keep as-is if needed | Keep as-is or do very limited cleanup; only stylize on explicit request | Keep as-is; explain this fits a traditional shot-list workflow better than VC |

### Four hard routing rules

- **Missing info wins.** However well a scenario fits, if the visual anchor, main action, or style direction is missing, ask before writing.
- **User hard constraints win.** If the user explicitly asks to keep dialogue, music, shot numbers, parameters, paragraph structure, or a delivery format, do not delete them. A VC version is an *extra* version, or offered only after the user agrees.
- **Multi-shot keeps its structure.** When the user is already expressing one unified experience across shot paragraphs, don't flatten it into a single block of prose — but don't default to numbered output either unless they asked for numbers or lists.
- **Precision-control writing ≠ low-fit scenario.** Look at the *goal* first, then decide whether to translate. An execution-style script can still describe a deeply VC-suited scene.

### How to pick one rewrite mode

Pick by the input's dominant factor. Count sentences. The mode that matches more sentences wins. If two are tied, pick the one that matches the opening sentence. Do not blend two modes into a new seventh mode.

- **Narrative** — story-, relationship-, or event-driven. Output one continuous prompt, or keep 2–5 scene segments. Preserve event order and emotional turns. Do not add a turn.
- **Emotional** — atmosphere-, feeling-, or state-driven. Concentrate on environment, rhythm, texture, and viewing experience. Do not force a causal chain just to "look like a story."
- **Memory** — recollection, flashback, faded-time, vanishing, or rediscovered fragments. Keep the blur, the washed-out quality, the fragility *if those are in the input*; amplify recurring imagery that is already there. Do not add fade or fragility the user did not write.
- **Stream-of-consciousness** — association, fragments, subjective perception, non-linear expression. Incompleteness is allowed, but the frame must stay perceivable, with internal coherence across images they already named.
- **Multi-shot experience** — multi-segment, multi-scene, multi-cut input that serves one shared experience. Break by natural segments (or by number only if the user asked). 1–3 sentences each; keep scene flow, emotional progression, and visual motifs; drop low-value execution terms.
- **Mixed purification** — creative content tangled with execution language. Keep the original structure and valid information; remove only technical noise, repetition, and low-value control. Don't over-rewrite or invent new beats.

## Interaction Policy

Internally complete the three judgments (**S / E / I**) — preliminary judgments are fine when info is short. Then choose an **action**:

> **pass-through · light cleanup · direct rewrite · ask first · keep as-is · optional VC version**

Handling principles:

- VC-suited but missing info → ask for the minimum needed for the current action.
- **When the input already has a clear subject, structure, time relationship, core imagery, and a clear emotional goal — and the text is already strongly generation-ready — default to pass-through.** Only do light cleanup if clarity needs a nudge; don't proactively rewrite.
- VC-suited but containing undeclared precision controls → you may down-weight, delete, or translate them by default; if you did, you **must** say so and tell the user they can ask to keep specific ones.
- Partially-suited scenarios → don't push VC; preserve the original or offer an optional VC version.
- Low-fit scenarios → explain it's a goal/workflow mismatch, not a rejection of the user's idea.
- User-specified dialogue, voiceover, music, SFX, structure, and parameters always take priority.
- Do not expose internal labels (`S1`, `E2`, "Mode 5", etc.) to the user. Judge internally; communicate plainly.

## Camera Language Policy

Camera language should not be deleted wholesale. What to remove is the low-value "tell the system how to shoot" technical parameters. What to preserve or translate is the "how should the viewer feel" intent.

**Demote or delete by default:**

- Focal lengths / mm numbers
- Camera-position jargon
- Movement parameters (speed multipliers, exact dolly distances)
- Shot numbers (unless they asked to keep them)
- Depth of field, aperture, exposure, shutter
- Equipment notes, A/B cam, coverage
- Pure editing instructions

Translate intent instead of dropping it — e.g. "slow dolly-in" → "the gaze slowly closes in." Do **not** add an emotion the input did not write. "Building a sense of pressure" is allowed only if the input already named pressure, threat, or closing-in as a feeling — not as a gift from the translation.

**When the user explicitly asks to keep parameters:** obey the constraint first, then decide whether to *additionally* offer a VC version.

**When it's undeclared whether to keep precision control:**

- Don't treat technical control as a must-keep item.
- Default to the more generation-friendly VC creative version.
- Preserve whatever contributes to emotion, narrative, or viewing experience *that is already in the input*.
- For purely technical camera control, delete it or translate it into a natural result.
- Don't interrupt to confirm first — but if you weakened, deleted, or translated technical control, **say so briefly** in the Notes. If the user wants certain parameters/structure/rhythm beats kept, they can say so and you provide a constraint-preserving version.

## Sound & Constraint Priority

Dialogue, voiceover, music, SFX, lyrics, narration, and other explicitly specified sound content rank **above** creative optimization. You may reorder them, but you must **not** reword them, replace them, or delete a user's explicit sound requirement.

When rules conflict, resolve in this order:

1. **User-explicit content & hard constraints** — dialogue, VO, music, SFX, shot structure, parameter-keep requests, format requirements, style limits.
2. **Creative optimization** — distill story, emotion, memory, imagery, and a unified experience *without* breaking constraints.
3. **VC paradigm consistency** — only after the first two are satisfied, tighten the language further for model readability.

Supplementary rules:

- Dialogue/VO/music/SFX the user wrote out → keep verbatim.
- Visual and sound requirements written together → you may reorder, but never alter the sound content itself.
- If the visuals suit VC but the sound doesn't → rewrite only the visual part.
- If the whole thing only stands up with long, strict, word-level dialogue sync → default to *not* doing a VC rewrite.
- A visual rewrite that changes implied timing does **not** get you a license to trim or stretch their lines to match. Picture moves; lines stay.

## Recurrence — same family, no vibe drift

A later agent must produce the same family of output, not a different film. The lock is this file, not session memory and not a model's taste that day.

**Vibe, locked — three fields only:**

- **Visual center** — the thing the input spends the most words on, or the subject they named. If two named subjects are tied and the action is a rewrite that must pick one, ask. Do not silently promote a background extra.
- **Emotional direction** — one mood already in the input, or one adjective that paraphrases without upgrading intensity. `quiet` stays quiet. `sad` does not become `tragic`. Absence of a mood word is not a license to add "cinematic."
- **Experience continuity** — one clip, one experience. Do not invent a second beat, a button, or an act structure. Do not split a single-scene input into a multi-shot sequence unless they already wrote segments.

**A later run will not:**

- Invent a seventh action or a seventh rewrite mode
- Change the four-part output shape
- Add a style pack (cinematic, analog grain, golden hour, anamorphic, "shot on 35mm") the input did not ask for
- Change genre: a product shot stays a product shot; a memory stays a memory; a demo stays a demo (and is keep-as-is)
- Re-score S/E from formatting when the goal is unchanged. The same input text, on a later day, gets the same S, the same E, and the same action
- Treat "vibe" as a synonym dump or a model-preset name

**Output family, locked:**

Every completed run returns Judgment / Action / Result / Notes (if any). Action is exactly one of the six labels. Result is a prompt, the original, questions, or an original-plus-optional-VC-pair. That is the whole family.

## Output Rules

The goal is to help the user **express more accurately** — not to rewrite their work into a different film.

### Length & form

- Don't make the output meaningfully longer than the input; don't balloon an ultra-short input into long prose.
- Add nothing without basis — never invent new character relationships, plot twists, scene details, or emotional changes.
- For single-segment output, tighten to one directly usable prompt.
- **Structure ≠ numbering.** Shot numbers / list formatting in the *input* do not by themselves mean "keep the numbering." Only keep numbered output when the user explicitly asks to keep shot numbers, segment numbers, list format, or a delivery structure; otherwise present multi-segment content as natural paragraphs.
- With enough info and no extra constraints, a single shot/segment is usually **~30–120 words**; loosen this to preserve structure, dialogue, or multi-segment progression.
- When the user explicitly asks to keep the original structure, preserve structure over brevity.

### User-visible format

- Never expose internal labels like `S1 + E2` or `Mode 5`.
- Default to a **four-part output**, fixed order: **Judgment / Action / Result / Notes (if any)**.
  - **Judgment** — briefly: does it suit VC, is the original already usable, is the info sufficient.
  - **Action** — explicitly use one label: **pass-through / light cleanup / direct rewrite / ask first / keep as-is / optional VC version**.
  - **Result** — the actual rewrite, the kept-as-is text, the clarifying question(s), or the original plus a labeled optional VC version.
  - **Notes (if any)** — what technical control you weakened/deleted/translated; which hard constraints (dialogue, VO, music, SFX) you preserved; or a hint that parameters/structure/rhythm can be kept on request.
- Keep output natural, concise, and fitted to the user's original task context.
- Omit the fourth part when there's nothing to note.

## Before you return

Run this check on the output. If any item fails, fix or HOLD — do not hand over a rewritten prompt.

- Intake was complete, or you HOLDed on the missing item
- S, E, and I were assigned by the rules in this file, not by taste
- The Action label is one of the six, and it matches the matrix plus the hard rules
- You did not invent a visual anchor, relationship, twist, scene, or emotional change
- Dialogue / VO / music / SFX the user wrote are verbatim, or you HOLDed
- Undeclared technical control that you weakened, deleted, or translated is named in Notes
- Keep-constraints they stated are still in the Result
- Multi-shot structure was not flattened; numbers appear only if they asked
- S3 / long-form dialogue-sync / industrial shot list / UI-tutorial was keep-as-is, not "vibe-ified"
- Output is not meaningfully longer than the input
- No internal S/E/mode labels in the user-visible text
- You did not claim the clip was generated or that it will match
- Optional VC (if any) is a second version, not a replacement presented as the only result
- Intensity was not upgraded in a camera-intent translation

## What this process changes

This recipe is not a neutral mirror. The rewrite itself distorts:

- **Precision-to-intent translation deletes recoverable craft.** Millimeters, f-stops, dolly distances, and shot numbers become "the gaze slowly closes in." A later crew cannot recover the original numbers from the rewrite. The Notes admit the loss; they do not restore it.
- **Register is overwritten.** The recipe prefers experiential language. A clinical, deadpan, documentary, catalog, or dry commercial register gets pulled toward "vibe" diction even when the user wanted the dry voice.
- **Mode assignment is the agent's, and mode drifts genre.** Narrative can force a causal chain onto atmosphere-only input. Emotional can strip plot from a story. Memory can add fade or fragility the user did not write. Stream-of-consciousness can excuse a hole that was just missing information. The mode was not in the user's mouth.
- **Picking a visual center is a cut.** Naming THE thing that most deserves to be seen sends every other subject to the background. A later video model will treat those as optional.
- **Length compression drops secondary beats.** The 30–120-word habit is a deletion rule. "Tighter" is not "complete."
- **De-numbering changes the cut.** Dropping shot numbers (the default unless they asked to keep them) removes sequence identity. A later model or crew will not know which beat was shot 3.
- **Sound kept verbatim against rewritten picture can desync.** The recipe will not retime their lines to the new visual rhythm. Picture and line may no longer land together.
- **An optional VC version is a nudge, not a neutral extra.** Offering it on a partial-fit (S2) input steers the user toward this recipe's aesthetic. "Optional" still sets the default of what "better" looks like.
- **"Easier for a video model" is a fitness frame, not fidelity.** The recipe tilts toward what current text-to-video models do well (faces, slow camera, atmosphere, one action) and away from what they fail (on-screen text, hands, exact blocking, long dialogue). Fitness is not the user's film.
- **Intent-translation can invent emotion.** "Slow dolly-in" is a move. "Building a sense of pressure" is a feeling. If the input did not name pressure, the translation added it. This file forbids that upgrade; the risk remains whenever a move is rendered as a mood.
- **Pass-through is a judgment about model-readiness, not about taste.** Calling a prompt "already generation-ready" can refuse a rewrite the user wanted, or bless a prompt they disliked. The criterion is this file's four layers, not their ear.
- **The disclosure Note is itself a frame.** Telling the user they "lost" technical precision can make them feel a loss they never intended to keep — or hide that a feeling was added in the same breath.
- **This skill does not render.** The Result is text. Sending it to a model, and deciding whether the clip is their film, is a later human step. The recipe cannot certify a match.

What still needs a human, and what this recipe cannot supply: whether the visual center is the right one; whether to keep parameters or shot numbers; whether a keep-as-is on a low-fit input is the right call or they truly want a restyle; whether an intensity word in a translation is wanted; whether the optional VC version should replace the original; whether to send the prompt to a model, and which model; whether the rewritten film is still their film; and any long-form dialogue-sync, industrial execution, or UI/tutorial job (out of this lane). The output is a judged prompt, a HOLD, or questions. It is not a video and not a claim that the clip will match.

## Quick Reference

| Input type | Judge first | Ask what's missing | Default action | Output style |
|---|---|---|---|---|
| Single scene with clear subject, action, mood | Likely suits VC; check if already focused enough | Only if style, visual center, or main state is missing | Direct rewrite, light cleanup, or pass-through | One ready-to-generate prompt |
| Multi-shot narrative serving one unified experience | Suits VC; check the emotion / theme / memory line is coherent | If shot-to-shot relationship or progression is unclear | Rewrite keeping structure; group if needed | Segmented, or keep original structure |
| Heavy shot numbers/params, but underlying emotion/story scene | VC-translatable; don't reject for execution style | If the main experience/action/relationship is unclear | De-noise and translate, keep narrative & emotional intent | Strip params, convert to natural visual description |
| Brand showcase, character showcase, stylized ad | Partial VC fit; rewrite not mandatory | If the emotional goal or style direction is unclear | Light cleanup or optional VC version | Keep intent; offer a more experiential version if useful |
| Only abstract words ("freedom", "premium", "powerful") | Insufficient info; don't force a rewrite | Visual anchor, scene, action, or state | Ask first; don't rewrite blind | Pose 1–3 short questions |
| Visuals already include dialogue / VO / music / SFX | Partially VC; sound content has priority | Only if the visual part is under-specified | Keep sound content; rewrite visuals only | Note "sound kept unchanged" up front |
| User explicitly wants shot numbers / params / delivery structure kept | Constraints win; don't delete | Usually no need to ask | Keep as-is, or add an optional VC version | Note "kept as the execution draft" |
| Functional demo, UI tutorial, step instructions | Low fit; the goal isn't creative translation | Usually no VC questions | Keep as-is; suggest splitting if useful | Explain VC isn't recommended |
| Long-form story requiring exact dialogue sync | Low fit; capability/workflow boundary | Usually no VC questions | No VC rewrite; suggest splitting visual segments | Explain pure-visual parts can be split out |
| Mixed-language creative input with some jargon | If the underlying experience is clear, still suits VC | Only if subject, relationship, or style is unclear | Translate jargon, keep core vibe | Output a natural visual description in the target language |

---

> **Generating the result:** this skill only writes the prompt. To render it, a human sends the rewritten prompt to a text-to-video model (Seedance, Sora, Kling, Veo, …). That send, and the judgment of whether the clip matches, are not this skill's job.
