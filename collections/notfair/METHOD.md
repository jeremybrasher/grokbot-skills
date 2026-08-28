# Pack method — notfair

This file is the governing method for the whole collection. A later agent
runs from this file. Companion skills under `seo/`, `paid-ads/`,
`google-ads/`, `meta-ads/`, `analytics/`, and the copies under `skills/`
are job attachments. They do not start their own marketing shop.

If this file and a companion disagree on start, stop, hold, or routing,
this file wins. The companion wins on domain vocabulary inside the job
that owns it.

A file under `skills/` is a pointer, not a second recipe. It exists so a
host can register the skill. It says "read the domain `SKILL.md`" and
stops there. If that pointer is missing, rotated, or out of date, run
from this file plus the domain folder. Do not invent a second workflow
to fill the gap.

Shared files that some companions name (`operating-contract.md`,
`preamble.md`, `measurement-framework.md`, `analysis-principles.md`) are
evidence attachments. If they are missing, the steps below still run:
list first, stop when unauthorized, audit before any write, name what to
cut or reuse before any net-new object.

## When to use

Use this pack when an operator already has a site, an ad account, or a
connected Search Console / GA4 / ads property, and wants an agent to
audit live performance, plan or refresh content for search or answer
engines, or make a reviewable change to a page, campaign, schema, or
measurement setting.

Do not use this pack to:

- Rank or spend from a generic best-practice essay when live GSC, GA4,
  or ads access was never listed.
- Publish a campaign, sitemap, schema block, or measurement change
  without the exact property or account, the exact URL or object, and
  named approval.
- Assume ChatGPT Ads, TikTok Ads, or Amazon Ads inventory, account
  access, or mutation tools exist in this session.
- Treat a `ready_for_review` brief as a live campaign, or a sitemap
  submission as an indexing guarantee.
- Mint a second page, campaign, or schema object when a live one
  already occupies the same job.
- Run a `skills/` pointer as if it contained the full method.

## Intake — before any audit write, brief, or mutation

You need these. Nothing else starts.

1. The job, in one line: site audit, page audit, content refresh or
   plan, schema change, paid review, paid launch, paid mutation,
   analytics read, or measurement-config change.
2. The object: a site URL, and/or the exact Search Console property,
   GA4 property, or ads account. The exact form must come from a
   harmless list (`listProperties`, `listConnectedPlatforms`, or the
   equivalent account/property list) — not from a guessed
   `sc-domain:` string, a `G-` measurement ID, or a remembered
   account name.
3. For any write (ads mutation, sitemap submit or delete, GA4 key-event
   or custom-dimension change, schema publish, CMS edit): the named
   human who can approve, and the exact object the write will touch.
4. For a paid launch: primary conversion and how it is verified, target
   CPA/ROAS or customer economics, daily and monthly budget, destination
   URL, geography, approved offer and claims, and the spend approver.

If any item is missing, stop. Ask only for the missing item. Return the
gap. Do not invent a property, do not pick an account to look busy, do
not proceed hoping a later skill will catch it, and do not wait as if
the object will appear.

Then observe, in this order, before any write:

- Harmless list of properties, platforms, or accounts actually
  connected in this session.
- Whether the connector is missing or unauthorized. If it is, give the
  reconnect path and stop before claiming live data.
- Live occupants of the job: GSC page × query rows, the site's existing
  URLs, live campaigns / ad groups / line items, and JSON-LD already on
  the page.
- The last audit log, `business-context.json`, or `seo-drift` baseline
  if one exists. If the file is missing, empty, or rotated, this is a
  first run — not a reason to invent previous issues or skip intake.

## Wait vs hold — stop and return this, not a polished guess

Wait is for an approval a human can give on an object that already
exists: "submit this sitemap URL on this property", "pause this
campaign", "archive this GA4 dimension". Never auto-approve. Never
proceed on timeout.

Hold is for a missing object. Missing property, missing URL, missing
approval, missing connector, or a job already occupied by a live object
the operator has not named to cut or reuse — that is hold, not
wait-and-hope. Do not open an approval on an empty object. Do not
proceed hoping the audit, the launch brief, or a later skill will fill
it.

When you cannot proceed, return the gap. Do not fill it with a generic
SEO report, a guessed campaign, or invented schema.

| Condition | What is missing | What it needs | Return instead of a guess |
|---|---|---|---|
| No site URL and none in the repo | The object | A URL the operator names | "I need the site URL. I will not invent a domain." |
| `listProperties` / account list empty or unauthorized | Access | Reconnect the connector; a listed property | Reconnect path. Stop. Do not claim live GSC, GA4, or ads data. |
| Property form unconfirmed (`sc-domain:` vs URL-prefix; `properties/123` vs `G-`) | The exact property | The listed form, confirmed | The listed candidates. Hold. Do not pick one to look busy. |
| Write requested; no exact property + object + approval | The write target and a yes | Named property, named URL or entity, named approval | "No approval on a named object. I will not mutate." |
| Sitemap submit or delete without exact property + sitemap URL + approval | Those three | Show them, then wait | Hold. Submission is not an index guarantee even after a yes. |
| Paid launch missing conversion, budget, destination, geo, claims, or approver | A launch input | The missing field | Name the gap. Do not build a spend plan around a guess. |
| ChatGPT / TikTok / Amazon Ads treated as live | A verified connector or export | Official evidence of inventory | Plan or export-review only. Do not mint a campaign ID. |
| Conversion signal broken, and a spend change is requested | A trustworthy conversion | Fix tracking, then re-read | Stop. Pulse metrics and ROAS are meaningless. Do not optimize. |
| Same query, two or more live pages ranking, and a net-new page is requested | A canonical winner | Operator picks the page to keep | Hold. Do not schedule a third page. |
| Live campaign, ad group, or line item already occupies the objective / audience / query set | A cut-or-reuse decision | Name the live unit to pause, exclude, or reuse | Hold. Do not mint a second campaign for the same job. |
| Live JSON-LD `@type` already occupies the page job | A reuse decision | Update that object in place, or name it for retirement | Hold. Do not emit a second block of the same type for the same entity. |
| `business-context.json` stale or missing and unit economics are required | Economics | AOV, margin, or an explicit "unknown" | Ask. Do not invent AOV or margin. |
| Audit log, drift baseline, or GSC cache missing, empty, or rotated | Prior evidence | Run as a first read; keep the method | Do not invent last month's issues. Do not skip intake. |
| Wrapper under `skills/` invoked as the full recipe | The domain file or this method | Read the domain `SKILL.md`, or this file | Hold if neither is reachable. Do not improvise from the pointer. |
| Shared preamble or operating-contract file missing | An attachment | This file's steps | Keep list-first, unauthorized-stop, audit-before-mutate, cut-before-create. |
| Approval opened on an object that was never listed | The listed object | A property or account from the harmless list | Hold. Do not wait on a gate that has nothing behind it. |

A hold is a return value, not a delay before you guess.

## Defaults: cut first

This operation defaults to less, not more. Before any net-new page,
campaign, or schema, name the live objects that already occupy the job
and say which will be cut, merged, redirected, paused, noindexed, or
reused. If a live object occupies the job, refuse to mint a second one.

**Pages and content**

- Pull GSC page × query (or a live crawl if GSC is not connected) and
  list URLs that already rank for, or target, the requested job.
- Cannibalization (same query, multiple pages with material impressions):
  pick one winner. Retire, redirect, or noindex the losers. Do not
  schedule a new URL until the winner is named.
- Striking-distance or CTR-underperformer: refresh the live page or its
  title and description. That is not a new URL.
- Unanswered intent (no live page occupies the job): a net-new page is
  allowed only after the inventory says the job is vacant.
- Programmatic sets: do not generate empty or thin combinations. Noindex
  or skip them. Do not stand up a second template for a live URL pattern.
- SERP brief (`competitor-pages`) binds to the existing target URL when
  one exists. A brief is not permission to mint a parallel article.

**Campaigns and ads**

- List live campaigns, ad groups, line items, shared negative lists, and
  assets that already occupy the objective, audience, or query set.
- Prefer this order: exclude an irrelevant query, placement, or audience;
  pause the narrowest losing unit; adjust budget or bid in a measured
  step; only then consider a new structure.
- Reuse shared negative lists and existing sitelinks, callouts, and
  snippets. Do not duplicate a list or asset that already covers the job.
- `google-ads-audit` / `meta-ads-audit` / `paid-ads-review` run before
  any mutation skill. Launch is a pre-spend brief (`ready_for_review`),
  not a live campaign. Never resume a campaign without a separate yes.
- A small budget split across several new channels is usually an
  underpowered experiment: say so. Do not mint four campaigns to look
  complete.

**Schema and measurement**

- Crawl existing JSON-LD on the URL. If a live `@type` already occupies
  the job (Product on a product page, FAQPage on an FAQ, Organization on
  the brand, Article on the post), edit that object in place. Do not
  emit a second `<script type="application/ld+json">` of the same type
  for the same entity.
- Retire schema that no longer matches visible content (HowTo on a page
  that is no longer a how-to; Product with a price the page does not
  show) before adding a replacement type.
- Sitemaps: drop stale, redirected, 404, and noindex URLs from the live
  sitemap before submitting a replacement set that occupies the same
  paths. `deleteSitemap` and `submitSitemap` need the exact property,
  the exact sitemap URL, and approval. Deleting a submitted sitemap does
  not deindex its URLs.
- GA4: do not mint a second key event for the same conversion. Archiving
  a custom dimension is irreversible and the parameter name cannot be
  reused — require approval that names the property and the dimension.
- Drift: if a baseline exists, compare against it. Do not create a
  parallel baseline as a substitute for the method.

**Reuse of pack state**

- Reuse a fresh `business-context.json`, GSC cache, or audit log. Do not
  rewrite them as if this were the first run.
- One skill owns one job. Do not run a second skill "to be sure" on the
  same object in the same turn.
- One question to the operator at a time.

## Will not produce

- Live GSC, GA4, or ads claims when `listProperties` / the account list
  was empty or unauthorized
- A mutation without the exact property or account, the exact URL or
  entity, and named approval
- A second page, campaign, or schema object while a live one occupies
  the job
- A content calendar entry that adds a URL on top of an unresolved
  cannibalization
- A spend plan built on a broken conversion signal
- ChatGPT / TikTok / Amazon campaign IDs, delivery, or settings invented
  without a verified connector or export
- A blended CPA or ROAS presented as a single truth without a labeled
  definition
- Sitemap submission described as an indexing guarantee
- A `ready_for_review` brief labeled `published`
- A `skills/` pointer treated as the full method, or a second recipe
  written to replace a missing pointer
- Invented AOV, margin, property IDs, or last-audit findings
- Averaged-already-aggregated CTR or position treated as a new metric
- A dashboard dump in place of a decision and a named next action

## Method card — same family every run

A later agent runs these steps from this file. Do not skip, reorder, or
replace them. Do not substitute "just write the page" or "just launch
the campaign." The 45 companions attach at a step; they do not replace
the sequence.

1. **Intake.** Job + object (URL and/or listed property or account) +
   approval-if-write. Any gap → hold (return the gap). Do not proceed
   hoping a later skill will catch it.
2. **List.** Harmless `listProperties` / `listConnectedPlatforms` /
   account list. Unauthorized or empty → stop. Confirm the exact listed
   form before any read that will be treated as live.
3. **Inventory the occupants.** Name the live pages, campaigns, and
   schema objects that already do this job. If one occupies it, the next
   step is cut or reuse, not create.
4. **Audit before mutate.** Read-only evidence from live GSC, GA4, or
   ads when connected: complete equivalent periods, labeled provisional
   rows, conversion integrity first. Ads audits (`google-ads-audit`,
   `meta-ads-audit`, `paid-ads-review`) run before the matching operate
   skill. Paid launch stays pre-spend.
5. **Route one job.** One companion owns the turn (table below). Domain
   folder `SKILL.md` is the recipe. `skills/` is a pointer. Missing
   pointer does not mint a parallel method.
6. **Cut or reuse, then maybe create.** State what will be retired,
   redirected, noindexed, paused, excluded, or edited in place. A
   net-new page, campaign, or schema is allowed only when the inventory
   shows the job vacant, or the operator has named the live object to
   replace.
7. **Approve, then write.** Show exact property, current state, proposed
   state, blast radius, and rollback. Wait. Never wrap a write in a
   bulk script. Read back from before/after evidence or a fresh list.
8. **Return the artifact.** A decision, the evidence, the named cut or
   reuse, and one next action — an audit, a calendar, a `ready_for_review`
   brief, or a change record. Not a dashboard transcription. Not a
   published campaign that was only briefed.

**Recurrence is the method, not the growing file.** Audit logs,
`business-context.json`, GSC caches, `seo-drift` snapshots, and the
`skills/` wrappers are snapshots. They rot, rotate, and go missing. A
later agent runs the same questions whether last month's file or a
wrapper is there or not:

- Missing log or baseline: first run. Do not invent prior issues. Do
  not treat absence as a clean bill of health.
- Fresh log: compare, then keep or update. Do not overwrite a previous
  audit as if it never happened.
- Missing wrapper: this file plus the domain `SKILL.md`. The pointer is
  not the recipe.
- Missing shared contract file: the steps in this file still bind.

Live GSC, GA4, and ads reads replace static snapshots when the
connector is authorized. When it is not, hold — do not fall back to a
remembered industry average presented as this property's data.

## Companion binding — so wrappers do not rot

Each companion is a job attachment. If a later agent is handed only a
`skills/` pointer, it still obeys this pack: it reads the domain file,
it does not mint a second object onto an occupied job, and it holds
when the property, URL, or approval is missing.

| Companion | Attaches at | Does not |
|---|---|---|
| `seo-analysis`, `seo-page` | Site or URL audit after intake and list | Mutate; invent a property |
| `content-planner` | Calendar after GSC inventory | Schedule a URL on top of cannibalization |
| `content-writer`, `geo-optimizer` | Refresh or vacant-job draft after inventory | Mint a second page for an occupied query |
| `competitor-pages` | SERP brief on an existing target URL | Replace inventory; authorize a parallel article |
| `keyword-research` | Universe and clusters | A publish calendar; a new URL |
| `meta-tags-optimizer` | Title / description refresh on a live URL | A new page |
| `schema-markup-generator` | In-place JSON-LD after crawl of live schema | A second `@type` for the same entity job |
| `programmatic-seo` | Template spec; noindex or skip thin rows | A doorway farm; a second template on a live pattern |
| `sitemap-audit`, `search-console` | Sitemap inventory; submit/delete only after exact property + URL + approval | Indexing guarantees |
| `seo-drift` | Baseline or compare | A parallel baseline used as the method |
| `broken-link-checker`, `image-seo`, `hreflang-international`, `local-seo`, `ecommerce-seo`, `backlink-audit`, `sxo` | Named technical or local job on listed URLs | A new site section without inventory |
| `setup-cms` | Connect a CMS the operator named | Invent CMS credentials |
| `google-analytics` | Listed GA4 property | A `G-` ID as the property; a second key event for the same conversion |
| `paid-ads` | Router after intake | A duplicate of a platform skill |
| `paid-ads-setup`, `paid-ads-integrations` | Connection and capability map | Promising a tool the session does not expose |
| `paid-ads-review` | Read-only scorecard | Mutations |
| `paid-ads-launch` | Pre-spend brief | A live campaign; resume without a separate yes |
| `paid-ads-optimize` | Waste and pacing after review | A new campaign before pause / exclude / reuse |
| `paid-ads-creative` | Concepts and claim ledger | Unpublished copy treated as live |
| `google-ads-audit`, `meta-ads-audit` | Read-only account health; run before operate | Writes |
| `google-ads`, `meta-ads`, `paid-ads-x`, `paid-ads-linkedin` | Approved, bounded mutations after audit | Writes without audit, exact object, and approval |
| `google-ads-copy`, `google-ads-assets`, `google-ads-landing` | Copy, assets, or landing diagnosis on existing entities | A second campaign for the same query set |
| `paid-ads-tiktok`, `paid-ads-amazon`, `paid-ads-chatgpt` | Plan or verified-export review | Assumed inventory or minted campaign IDs |
| `paid-ads-guide` | Product and boundary questions | Performance claims |
| `gemini` | Second-model review | A substitute for live GSC / GA4 / ads |
| `upgrade` | Plugin update notes | A change to this method |

If you were handed only a pointer under `skills/`, read the domain
`SKILL.md` it names. If that file is also missing, return the hold for
missing pack context rather than improvising a marketing workflow from
the pointer's frontmatter.

## Before you return

If any item fails, fix or hold.

- Intake was listed, not invented. Missing property, URL, or approval
  was held, not hoped past
- Harmless list ran before any live claim
- Unauthorized access stopped before a live-data sentence
- Live occupants of the job were named; cut or reuse before any net-new
  page, campaign, or schema
- No second object minted onto an occupied job
- Audit ran before mutate. Launch stayed `ready_for_review` until the
  platform confirmed the object
- One companion owned the job. The `skills/` file was treated as a
  pointer
- Writes named property, current state, proposed state, and rollback,
  then waited
- Sitemap submit was not called an index guarantee
- Return is a decision, evidence, named cuts, and one next action

## What this process changes

This pack is not a neutral wrapper around a marketing agent. It changes
what gets claimed and what gets built.

- Connecting live GSC, GA4, or ads changes what can be said. A sentence
  that would have been a best-practice guess becomes a property-level
  claim. If the list was empty, that claim is a fabrication.
- Choosing `sc-domain:example.com` rather than `https://example.com/`
  changes the dataset. The confirmed property is a perturbed object.
  Do not treat it as "the site."
- Showing pulse metrics, waste dollars, a `ready_for_review` brief, or
  a cannibalization table is not a neutral read. It frames the next
  "yes." After you present the artifact, the operator's approval is a
  response to that measurement, not the original ask. If you need the
  original job, hold and ask for it separately from the thing you just
  showed.
- Routing to a specialized skill frames the problem as that skill's
  job. An "organic traffic" ask pulled into `geo-optimizer` becomes a
  citation rewrite; the same ask pulled into `paid-ads-optimize` becomes
  a spend cut. The frame is a distortion. Name it when you route.
- Cut-first makes retirement visible. A page, campaign, or schema that
  would have sat beside a new twin is removed or reused. That changes
  the live graph the next agent will see.
- Restating this method in the README, this file, and forty-five
  companions can itself drift. When they disagree, this file wins on
  start, stop, hold, and routing. Do not average the three.
- A second model (`gemini`) checking a brief is itself an observer.
  Its agreement is that model's reading, not the property's essence.
- Saving an audit to a host account or a local log creates a new
  object later runs will treat as history. A missing log is not a
  clean score.

What still needs a human: confirming the listed property or account;
every write approval; irreversible GA4 archive; whether to retire a
URL that still ranks; spend; policy and claims; whether a broken
conversion may keep spending; whether a vacant-job page should be
created at all; whether a post-measurement "yes" still matches the
original ask. The pack hands back an audit, a brief, a calendar, or a
read-back change. It does not certify rankings, incremental
conversions, or indexation.
