# NotFair Plugin

[![License: MIT](https://img.shields.io/badge/license-MIT-16a34a)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?logo=discord&logoColor=white)](https://discord.gg/gVJCRczpps)

**Open-source SEO, GEO, and marketing skills for AI agents.**

The NotFair Plugin gives Claude Code, Codex, Hermes, and other compatible agents practical marketing workflows they can follow—not another generic prompt collection. Use it to audit a site, investigate a traffic drop, analyze GA4 and Search Console, find wasted ad spend across Google, Meta, X, and LinkedIn, build campaign plans, and make reviewable changes.

Every skill is built in the open as a readable `SKILL.md`, with supporting references, scripts, and evals where needed. Inspect it, adapt it, or contribute a better workflow.

## What your agent can do

| Area | Examples |
|---|---|
| **SEO** | Full-site and page audits, keyword research, content planning, technical SEO, schema, local SEO, international SEO, e-commerce SEO, and regression monitoring |
| **GEO / AEO** | Improve content for citation and visibility in ChatGPT, Perplexity, Gemini, Claude, and Google AI Overviews |
| **Paid media** | Plan, review, and optimize cross-channel campaigns with explicit budgets, measurement, and approval boundaries |
| **Google Ads** | Audit accounts, analyze search terms, manage keywords and budgets, write RSA copy, plan assets, and diagnose landing pages |
| **Meta Ads** | Review Facebook and Instagram performance, diagnose creative fatigue, assess audiences, and create evidence-based creative briefs |
| **X Ads** | Analyze campaigns and line items, review conversion performance, manage targeting and creative, and execute approved changes |
| **LinkedIn Ads** | Connect B2B media to lead quality, analyze campaign groups and campaigns, and manage targeting, creative, conversions, and leads |
| **Analytics** | Query live GA4 and Search Console data, compare complete periods, inspect URLs, manage sitemaps, and update supported measurement configuration |
| **Content** | Turn search demand into editorial plans, briefs, articles, landing pages, metadata, and structured data |

The NotFair Plugin currently ships **45 skills** across SEO, GEO, paid media, advertising platforms, analytics, and cross-model review.

## Quick start

### Claude Code

Install the NotFair plugin from its marketplace:

```text
/plugin marketplace add nowork-studio/notfair-plugin
/plugin install notfair@nowork-studio
```

Then ask for the workflow you need:

```text
/notfair:seo-analysis
/notfair:geo-optimizer
/notfair:google-ads-audit
/notfair:meta-ads-creative
/notfair:paid-ads-x
/notfair:google-analytics
/notfair:search-console
```

You can also use plain language:

> Audit my site and tell me why organic traffic fell.

> Find pages that could earn citations in AI answers.

> Review last month's ad spend and show me the safest opportunities to improve ROAS.

### Cursor

Install **NotFair** from Cursor's plugin marketplace. The plugin loads the
open-source marketing skills in this repository and registers one hosted
NotFair MCP connection. Complete the browser OAuth flow when Cursor prompts
you, then ask Cursor to audit an ad account, analyze GA4 or Search Console, or
run one of the SEO and GEO workflows listed below.

For local testing before the marketplace listing is available, clone this
repository into Cursor's local plugin directory:

```bash
git clone https://github.com/nowork-studio/notfair-plugin.git ~/.cursor/plugins/local/notfair
```

Restart Cursor after installing or updating the local plugin.

### Kiro Powers

Install the public repository as a custom power from Kiro's Powers panel, or
find **NotFair** in the Powers registry after its listing is approved. The root
[`plugin.json`](plugin.json) and [`mcp.json`](mcp.json) follow the Agent Plugins
1.0 specification.

### Gemini CLI

Install the extension directly from GitHub:

```bash
gemini extensions install https://github.com/nowork-studio/notfair-plugin
```

The extension loads the repository guidance and the universal NotFair MCP. Run
`/mcp auth NotFair` in Gemini CLI when authentication is requested.

### Codex, Hermes, and other agents

Install the universal NotFair plugin directly through Codex:

```bash
codex plugin marketplace add nowork-studio/notfair-plugin --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

Codex installs the skills, registers one NotFair MCP connection, and opens its OAuth flow. If you prefer a workspace-local checkout, clone the repository and open it as a workspace; [`AGENTS.md`](AGENTS.md) maps marketing requests to the right skill.

```bash
git clone https://github.com/nowork-studio/notfair-plugin.git
cd notfair-plugin
```

If the `nowork-studio` marketplace is already configured, refresh it instead:

```bash
codex plugin marketplace upgrade nowork-studio --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

For host-specific setup, give your agent [`INSTALL_FOR_AGENTS.md`](INSTALL_FOR_AGENTS.md), or paste:

```text
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/nowork-studio/notfair-plugin/main/INSTALL_FOR_AGENTS.md
```

## Why skills instead of one giant marketing agent?

Marketing work gets unreliable when every request goes through the same vague prompt. The NotFair Plugin splits the work into focused, testable procedures.

- **Specialized:** each skill has a defined job, required inputs, decision rules, and output format.
- **Evidence-led:** live-data workflows use Search Console, Google Analytics, Google Ads, Meta Ads, X Ads, or LinkedIn Ads instead of guessing from generic best practices.
- **Safe by design:** read-only review comes before mutation, paid-media changes stay explicit, and unsupported capabilities are never implied.
- **Host-agnostic:** the canonical skills are plain files, not logic trapped inside one agent runtime.
- **Forkable:** everything is MIT licensed, so teams can review and adapt the workflows to their own standards.

## Pack method

A later agent runs this collection from [`METHOD.md`](METHOD.md). That file
is the method. This README is the face. Files under `skills/` are pointers
to the domain recipe (`seo/`, `paid-ads/`, `google-ads/`, `meta-ads/`,
`analytics/`). They are not a second recipe. If a pointer is missing, run
from `METHOD.md` plus the domain folder.

**When to use.** An operator has a site, an ad account, or a connected
Search Console / GA4 / ads property, and wants a live audit, a search or
answer-engine content plan, or a reviewable change to a page, campaign,
schema, or measurement setting.

**When not to.** No listed property or account, used as a reason to write
a best-practice essay. A campaign, sitemap, schema, or measurement write
without the exact object and a named yes. ChatGPT / TikTok / Amazon Ads
treated as live inventory. A `ready_for_review` brief labeled published.
A second page, campaign, or schema minted onto a job a live object
already occupies. A `skills/` pointer run as the full method.

**Intake — before any audit write, brief, or mutation.** You need the
job, the object (site URL and/or the exact property or account returned
by `listProperties`, `listConnectedPlatforms`, or the equivalent
harmless list), and — for any write — the named approver and the exact
object the write will touch. Paid launch also needs conversion and
verification, economics, daily and monthly budget, destination, geo,
approved claims, and the spend approver. If any item is missing, stop
and return the gap. Ask once. Do not invent a property, pick an account
to look busy, or proceed hoping a later skill will catch it.

**Wait vs hold.** Wait is for an approval a human can give on an object
that already exists. Never auto-approve; never proceed on timeout. Hold
is for a missing object: no URL, empty or unauthorized property list,
unconfirmed `sc-domain:` vs URL-prefix, write without exact property +
object + approval, launch inputs missing, ChatGPT / TikTok / Amazon
without a verified connector or export, broken conversion signal, or a
job already occupied by a live page, campaign, or schema the operator
has not named to cut or reuse. Missing evidence is hold, not
wait-and-hope. Do not open an approval on an empty object.

**Stop and return the gap, not a guess.** Unauthorized or empty
`listProperties` / account list (reconnect, then stop — do not claim
live data). Sitemap submit or delete without exact property + sitemap
URL + approval. Cannibalization unresolved and a net-new page requested.
A live campaign or JSON-LD `@type` already occupying the job. Invented
AOV or last-audit findings. A wrapper invoked as if it contained the
recipe. A shared contract file missing — keep list-first,
unauthorized-stop, audit-before-mutate, cut-before-create anyway.

**Cut first. Name the occupant before any net-new object.** Before a
new page, campaign, or schema, list the live objects that already do
this job (GSC page × query or crawl; live campaigns / ad groups / line
items / shared negatives; JSON-LD already on the URL). Say which will
be retired, redirected, noindexed, paused, excluded, or edited in
place. If a live object occupies the job, refuse to mint a second one.
Refresh striking-distance and CTR-underperforming URLs; do not schedule
a twin. Pause or exclude the narrowest losing ad unit before creating
structure. Edit live schema in place; do not emit a second `@type` for
the same entity. Drop stale sitemap URLs before submitting a
replacement set. Do not mint a second GA4 key event for the same
conversion. Ads audit and `paid-ads-review` stay read-only and run
before operate. Launch stays pre-spend.

**Will not produce.** Live-data claims without a listed property.
Mutations without exact object and approval. A second page, campaign,
or schema on an occupied job. A calendar row on top of unresolved
cannibalization. A spend plan on a broken conversion. Invented ChatGPT /
TikTok / Amazon campaign IDs. Unlabeled blended CPA/ROAS. Sitemap
submit as an index guarantee. A pointer treated as the method.

**Same family every run** (the files can rot; these steps do not):

1. Intake. Any gap → stop and return it.
2. List properties / platforms / accounts. Unauthorized or empty → stop.
3. Inventory live occupants of the job. Occupied → cut or reuse, not create.
4. Audit before mutate. Complete periods. Conversion integrity first.
5. Route one job to one domain `SKILL.md`. `skills/` is a pointer.
6. State the named cuts. Net-new only when the job is vacant or the
   operator named the object to replace.
7. Show exact property, current state, proposed state, rollback. Wait.
   Read back.
8. Return a decision, the evidence, the named cuts, and one next action.

**Recurrence is the method, not the log.** Audit logs, business-context
files, GSC caches, drift snapshots, and `skills/` wrappers are
snapshots. If a log or wrapper is missing, empty, or rotated, that is a
first run or a missing pointer — not a clean bill of health, and not a
reason to invent history or a second recipe. Live GSC / GA4 / ads
replace static snapshots only when the list authorized them.

**Measurement changes the decision.** Showing pulse metrics, waste
dollars, a brief, or a cannibalization table frames the next "yes."
After you present the artifact, the operator's approval is a response
to that measurement, not the original ask. If you need the original
job, stop and ask for it separately from the thing you just showed.
Choosing a property form changes the dataset. Routing to one skill
frames the problem as that skill's job. Restating this method in the
README, `METHOD.md`, and the companions can drift — `METHOD.md` wins on
start, stop, hold, and routing.

Full hold table, cut-first inventory, companion binding, and what this
process itself distorts: [`METHOD.md`](METHOD.md).

## Skill catalog

### SEO and GEO

| Skill | What it does |
|---|---|
| [`seo-analysis`](seo/seo-analysis/) | Audits a full site with Search Console and crawl data, then prioritizes the highest-impact fixes. |
| [`seo-page`](seo/seo-page/) | Performs a deep audit of one URL for intent, content, structure, and on-page SEO. |
| [`content-writer`](seo/content-writer/) | Writes or improves search-led articles, landing pages, and service pages. |
| [`content-planner`](seo/content-planner/) | Turns Search Console opportunities into a prioritized, dated editorial calendar. |
| [`keyword-research`](seo/keyword-research/) | Builds a keyword universe, classifies intent, and organizes topic clusters. |
| [`meta-tags-optimizer`](seo/meta-tags-optimizer/) | Improves titles, meta descriptions, Open Graph tags, and SERP click-through potential. |
| [`schema-markup-generator`](seo/schema-markup-generator/) | Creates and validates JSON-LD structured data. |
| [`broken-link-checker`](seo/broken-link-checker/) | Finds broken internal and external links and reports site-health issues. |
| [`geo-optimizer`](seo/geo-optimizer/) | Audits and rewrites content for citation in AI search and answer engines. |
| [`local-seo`](seo/local-seo/) | Reviews Google Business Profile, local pages, NAP consistency, reviews, and local schema. |
| [`hreflang-international`](seo/hreflang-international/) | Diagnoses hreflang, canonical, language, and regional targeting problems. |
| [`sitemap-audit`](seo/sitemap-audit/) | Checks XML sitemap structure, freshness, coverage, and URL validity. |
| [`image-seo`](seo/image-seo/) | Reviews alt text, formats, compression, responsive images, CLS, and image discovery. |
| [`ecommerce-seo`](seo/ecommerce-seo/) | Audits product pages, category pages, variants, faceted navigation, and product schema. |
| [`programmatic-seo`](seo/programmatic-seo/) | Plans useful templated pages at scale with demand, uniqueness, and indexation guardrails. |
| [`competitor-pages`](seo/competitor-pages/) | Compares ranking pages and produces a practical SERP brief. |
| [`sxo`](seo/sxo/) | Connects search visibility and SERP CTR to the post-click conversion experience. |
| [`seo-drift`](seo/seo-drift/) | Creates a baseline and detects ranking, metadata, canonical, and indexation regressions. |
| [`backlink-audit`](seo/backlink-audit/) | Reviews referring domains, anchor text, link risk, and internal-link opportunities. |
| [`setup-cms`](seo/setup-cms/) | Connects WordPress, Strapi, Contentful, or Ghost. |

### Paid media

| Skill | What it does |
|---|---|
| [`paid-ads`](paid-ads/paid-ads/) | Routes broad paid-media questions to the right channel and workflow. |
| [`paid-ads-setup`](paid-ads/paid-ads-setup/) | Connects accounts and captures business, economics, tracking, and budget context. |
| [`paid-ads-launch`](paid-ads/paid-ads-launch/) | Produces a reviewable campaign or multi-channel experiment plan before spend begins. |
| [`paid-ads-review`](paid-ads/paid-ads-review/) | Creates comparable weekly or monthly scorecards and checks tracking health. |
| [`paid-ads-optimize`](paid-ads/paid-ads-optimize/) | Finds waste and pacing problems, then proposes narrow, reversible changes. |
| [`paid-ads-creative`](paid-ads/paid-ads-creative/) | Develops cross-channel concepts, claim ledgers, fatigue hypotheses, and test briefs. |
| [`paid-ads-x`](paid-ads/paid-ads-x/) | Audits and operates connected X Ads campaigns, line items, targeting, creative, audiences, and budgets. |
| [`paid-ads-linkedin`](paid-ads/paid-ads-linkedin/) | Audits and operates connected LinkedIn Ads around qualified pipeline outcomes. |
| [`paid-ads-tiktok`](paid-ads/paid-ads-tiktok/) | Creates TikTok campaign plans, creator briefs, and short-form experiments. |
| [`paid-ads-amazon`](paid-ads/paid-ads-amazon/) | Plans and reviews Amazon Ads with margin-aware ACoS guardrails. |
| [`paid-ads-chatgpt`](paid-ads/paid-ads-chatgpt/) | Designs bounded ChatGPT Ads experiments or reviews verified exports. |
| [`paid-ads-integrations`](paid-ads/paid-ads-integrations/) | Verifies connector, account, and tool access before promising a capability. |
| [`paid-ads-guide`](paid-ads/paid-ads-guide/) | Explains installation, supported platforms, limits, and troubleshooting. |

### Google Ads

| Skill | What it does |
|---|---|
| [`google-ads-audit`](google-ads/audit/) | Scores account health, validates tracking, and finds wasted spend. |
| [`google-ads`](google-ads/manage/) | Reviews performance and manages supported keywords, bids, budgets, negatives, and campaigns. |
| [`google-ads-copy`](google-ads/copy/) | Writes compliant RSA headlines and descriptions with test variants. |
| [`google-ads-assets`](google-ads/assets/) | Plans sitelinks, callouts, snippets, image assets, and Performance Max briefs. |
| [`google-ads-landing`](google-ads/landing/) | Diagnoses keyword-to-ad-to-page relevance and landing-page quality. |

### Meta Ads

| Skill | What it does |
|---|---|
| [`meta-ads-audit`](meta-ads/audit/) | Audits tracking, structure, creative health, audiences, spend efficiency, and scaling readiness. |
| [`meta-ads`](meta-ads/manage/) | Reviews Facebook and Instagram performance and executes supported campaign operations. |
| [`meta-ads-creative`](meta-ads/creative/) | Produces evidence-based concepts, copy angles, UGC briefs, and refresh experiments. |

### Analytics

| Skill | What it does |
|---|---|
| [`google-analytics`](analytics/google-analytics/) | Analyzes live GA4 acquisition, engagement, pages, events, and conversions and safely manages supported measurement configuration. |
| [`search-console`](analytics/search-console/) | Analyzes live Search Console queries and pages, inspects URLs, and manages approved sitemap submissions. |

### Cross-model review and maintenance

| Skill | What it does |
|---|---|
| [`gemini`](gemini/) | Uses Google Gemini for a second opinion, adversarial challenge, or open consultation. |
| [`upgrade`](notfair-upgrade-skill/) | Updates an installed NotFair plugin and summarizes what changed. |

## Live data and integrations

Some skills work entirely from a repository, URL, or supplied export. Live account analysis uses one OAuth-connected [universal NotFair MCP](https://notfair.co/api/mcp/notfair_ads). The plugin registers that connection automatically. During the staged Google-first rollout, enabled workspaces connect Google Ads in the same OAuth flow; every other platform becomes available after it is connected in the selected NotFair workspace.

| Data source | Used for | Connection |
|---|---|---|
| **Google Search Console** | Search performance, queries, pages, indexing, URL inspection, and sitemaps | Universal NotFair MCP via `search_console_` tools |
| **Google Analytics 4** | Acquisition, engagement, landing pages, events, conversions, realtime, and measurement configuration | Universal NotFair MCP via `google_analytics_` tools |
| **Google Ads** | Campaign performance, search terms, bids, budgets, keywords, and change history | Universal NotFair MCP via `google_ads_` tools |
| **Meta Ads** | Facebook and Instagram campaigns, ad sets, creatives, and insights | Universal NotFair MCP via `meta_ads_` tools |
| **X Ads** | Campaigns, line items, performance, targeting, promoted posts, audiences, and approved mutations | Universal NotFair MCP via `x_ads_` tools |
| **LinkedIn Ads** | Campaign groups, campaigns, creatives, analytics, targeting, conversions, and leads | Universal NotFair MCP via `linkedin_ads_` tools |
| **CMS platforms** | Content and SEO-field review in WordPress, Strapi, Contentful, or Ghost | Platform API or compatible MCP |
| **Google Gemini** | Cross-model review | Gemini API key |

Google Ads, Meta Ads, X Ads, and LinkedIn Ads use explicit, bounded mutation tools. Search Console and GA4 also expose narrow configuration writes with approval and read-back rules. TikTok, Amazon, and ChatGPT Ads remain planning or export-review workflows unless the current agent session exposes a verified connector.

## Privacy and support

- [Privacy Policy](https://notfair.co/privacy)
- [Support and community](https://discord.gg/gVJCRczpps)
- [Issue tracker](https://github.com/nowork-studio/notfair-plugin/issues)

Inside a skill, connectors use tool-agnostic placeholders such as `~~google-ads`, `~~meta-ads`, `~~x-ads`, `~~linkedin-ads`, `~~search-console`, `~~google-analytics`, and `~~cms`. The agent resolves each placeholder to a compatible tool available in the current session, so the workflow is not coupled to one MCP namespace.

## How the repository is organized

```text
notfair-plugin/
├── AGENTS.md                    # intent-to-skill resolver for AI agents
├── .claude-plugin/              # Claude Code plugin manifest
├── paid-ads/                    # cross-channel planning, review, optimization
├── google-ads/                  # audit, management, copy, assets, landing pages
├── meta-ads/                    # audit, management, creative
├── analytics/                   # Google Analytics and Search Console MCP workflows
├── seo/                         # SEO, GEO, content, and technical-search skills
├── gemini/                      # cross-model review
├── test/                        # unit and LLM-judge evals
└── notfair/                     # optional local goal-loop application
```

[`AGENTS.md`](AGENTS.md) is the universal entry point. It maps user intent to the canonical `SKILL.md` and documents the external dependency each workflow requires.

## Optional: run recurring marketing goals locally

This repository also includes a local application for turning a measurable marketing outcome into a recurring agent loop. It is a companion to the skill library, not a requirement for using the skills.

```bash
npx notfair@latest
```

The app runs on your machine with Codex or Claude Code, stores state locally, and can track a verified metric over time. See [`notfair/README.md`](notfair/README.md) for setup, architecture, and operating details.

## Contributing

Each skill lives in its own category folder:

```text
seo/your-skill-name/
├── SKILL.md          # required instructions and frontmatter
├── references/       # optional supporting knowledge
└── scripts/          # optional deterministic tooling
```

When adding or changing a skill:

1. Keep the workflow focused on one clear marketing job.
2. Use imperative, testable instructions in `SKILL.md`.
3. Add or update eval coverage.
4. Update [`AGENTS.md`](AGENTS.md), the plugin manifest, [`VERSION`](VERSION), and [`CHANGELOG.md`](CHANGELOG.md).

Open a pull request with one skill or one coherent improvement. For application contributions, see [`notfair/CONTRIBUTING.md`](notfair/CONTRIBUTING.md) and [`notfair/ARCHITECTURE.md`](notfair/ARCHITECTURE.md).

## Community

- Join the [NotFair Discord](https://discord.gg/gVJCRczpps)
- [Open an issue](https://github.com/nowork-studio/notfair-plugin/issues)
- Star the repository if these workflows make your agent more useful

## License

[MIT](LICENSE)
