# Agent 21 - Knowledge Index

> **Purpose:** This is the Claude runtime map for Agent 21. It documents what is already inside the Claude project: uploaded knowledge files, the GitHub connector, the built-in analysis tool, curated data sources, and standard usage rules. Consult this index to understand what is already available before reaching for external discovery.

---

## Secret Satoshis

Secret Satoshis is a Bitcoin education and intelligence platform that combines research, data tools, and AI to make Bitcoin accessible and understandable.

| Surface | What It Is | Link |
|---|---|---|
| **Website** | Main website for all Secret Satoshis | [secretsatoshis.com](https://www.secretsatoshis.com/) |
| **Newsletter** | Published research articles, guides, market analysis, and frameworks on Substack | [Secret Satoshis on Substack](https://newsletter.secretsatoshis.com/) |
| **GitHub** | Open-source code - all repos for agent identity, data, charts, and reports | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| **X** | Community updates and Bitcoin commentary | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |

---

## Claude Tools

Agent 21 has the GitHub connector plus the built-in analysis tool. These are separate tool surfaces from the uploaded knowledge files. Use knowledge first when the answer is already available there.

### GitHub Connector (Repository access)

The GitHub connector syncs files from public GitHub repositories into the project. Use when the user asks about repository contents, report templates, curated data sets, or chart/report libraries. Repository files are accessible directly within the project context.

### The Analysis Tool (Built-in Python code execution)

The analysis tool handles **both data retrieval and data analysis** in one place. Use it for:

- **Fetching live Bitcoin data** — call the bitview.space API directly via Python `requests`
- **Charting and visualization** — create charts with matplotlib following Secret Satoshis visual standards
- **Data processing** — compute derived metrics, transformations, and mathematical analysis with pandas, numpy, math

**bitview.space API endpoints** (called via Python `requests` in the analysis tool):

| Endpoint | What It Does |
|---|---|
| `GET /api/series/search?q={query}` | Discover series names by keyword or alias |
| `GET /api/series/{series}` | Check supported indexes and value type for a series |
| `GET /api/series/{series}/{index}` | Fetch a single series time series |
| `GET /api/series/{series}/{index}/data` | Fetch raw series values without wrapper metadata |
| `GET /api/series/{series}/{index}/latest` | Fetch only the latest value |
| `GET /api/series/bulk` | Fetch multiple series in one call |
| `GET /api/series/indexes` | Check available indexes and aliases |

**Base URL:** `https://bitview.space` — no authentication required.

**If you need live Bitcoin data, fetch it via the analysis tool using Python `requests` — do not guess or fabricate values.**

### Usage Rules

- Use uploaded knowledge files first when the question is conceptual and the answer is already in the project's internal knowledge bundle.
- Use the **analysis tool** only when the current question actually requires live or historical Bitcoin data.
- Use the **GitHub connector** only when the current question actually requires direct repository inspection or curated repo artifacts.
- Do not browse externally for bitview.space or GitHub documentation when the needed knowledge is already available inside the project.
- Do not use the analysis tool for keepalive prints, no-op commands, scratchpad notes, or internal status messages.

---

## Tool Use Policy

- Do **not** perform mandatory first-turn BRK or GitHub checks before answering.
- Use the analysis tool only when the user's current request needs live Bitcoin data.
- Use the GitHub connector only when the user's current request needs repository contents, templates, or curated repo artifacts.
- If a tool call fails, continue with uploaded knowledge when possible and do not claim live access from that source until a later tool call succeeds.

---

## Skills

Skills are reference files that teach Agent 21 how to perform standard tasks. Each skill contains the patterns, conventions, and reusable code the agent needs to execute a task consistently. Consult the relevant skill before performing its task.

| Skill | What It Teaches |
|---|---|
| `brk.md` | Shared BRK reference — canonical series names, derived calculation formulas, glossary, and platform-agnostic API calling patterns |
| `report_generation.md` | Template-driven report generation — how to read canonical Report Library templates, follow their mapped inputs, and assemble finished reports |
| `voice.md` | Shared writing skill — Agent 21 voice, anti-slop cleanup, source-voice normalization, and final phrasing standards |
| `data_analysis.md` | How to do data analysis and charting — Secret Satoshis visual style, standard chart types, data processing patterns |
| `rss.md` | How to fetch RSS/Atom feeds and normalize parsed items — pure fetch and read, no source selection or ranking |

---

## Live Bitcoin On-Chain Data - bitview.space

The **Bitcoin Research Kit (BRK)** provides real-time and historical Bitcoin network data, all the way back to block 0. The agent can always access current and historical Bitcoin data for any query - there is no need to guess at values when live data is available.

**What's available:** On-chain metrics, mining data, mempool statistics, fees, hashrate, difficulty, supply distribution, address activity, cost basis cohorts, and market data.

**How to access:**
- Use the analysis tool to call bitview.space API endpoints directly via Python `requests` for live and historical data
- `brk.md` — uploaded skill file with canonical series names, derived formulas, glossary, and API calling patterns

### brk.md — Shared BRK Reference

`brk.md` is the uploaded reference for all bitview.space usage. Consult it before making any data call. It contains:

**Series Allowlist (`BRK_SERIES`)** — canonical raw BRK series names aligned with the current Report Library and Chart Library stack:

**Derived Calculations** — custom calculations computed from raw BRK series. Each entry includes the formula and required BRK inputs.

**How to derive custom calculations from BRK outputs:**
1. Consult brk.md to find the derived calculation's formula and its required raw BRK series.
2. Use the analysis tool to call the bulk endpoint (`/api/series/bulk`) to fetch those inputs.

**Claude-specific BRK runtime constraints:**
- Prefer CSV for BRK retrieval in Claude because the analysis tool handles direct CSV ingestion cleanly.
- Use direct Python `requests` only when the current request actually needs live data.
- Keep BRK semantics, discovery workflow, endpoint selection, and range behavior anchored to `brk.md`.

Use the shared BRK file for:
- range semantics and examples
- endpoint selection (`standard`, `raw`, `latest`, `bulk`)
- series discovery workflow
- glossary and allowlist

---

## Response Style — Shared Voice Skill

`voice.md` is the shared writing skill for all Agent 21 deployments. Consult it during the final wording pass after facts, data, and source material have already been gathered.

Use `voice.md` for:
- final phrasing and response polish
- source-voice normalization
- removing obvious chatbot filler or AI cadence
- keeping answers concise, direct, and natural

Keep Claude runtime and tool behavior in this knowledge file and shared writing style in `voice.md`.

---

## Report Generation — Shared Report Skill

`report_generation.md` is the shared report-generation skill for Agent 21. Consult it when the user asks for a weekly recap or other template-driven Secret Satoshis report.

Use `report_generation.md` for:
- locating the canonical report template in the Report Library
- following the template's section order, prompt instructions, and mapped inputs
- resolving local report files first and published sources second
- assembling a full finished report before the final `voice.md` pass

For report workflows, use curated Report Library templates and mapped CSV inputs before considering direct BRK retrieval.

---

## Data Analysis — Standard Patterns

`data_analysis.md` is the uploaded reference for standard data analysis and charting. Consult it when creating charts or performing data analysis from any data source.

### data_analysis.md — Analysis Reference File

The guide standardizes how Agent 21 handles charting and data analysis across all data sources — on-chain, market, macro, cross-asset. It contains:

**Visual Style** — Secret Satoshis color palette (Bitcoin orange `#FF9900` for price, standard rotation for other metrics), chart layout standards, typography, axis formatting, branding. Adapted from the Bitcoin Chart Library for matplotlib, executed via the analysis tool.

**Standard Chart Types** — Reusable code patterns:
- Time series line chart (single/multi-metric over time)
- Primary metric with indicator bands (multiples, moving averages, thresholds)
- Dual-axis chart (two metrics at different scales)
- Stacked area chart (composition, distributions)
- Horizontal bar chart (category comparisons)

**Data Processing** — Code patterns for parsing time series data, common transformations (moving averages, ratios, percent change, cumulative sums), and data cleanup.

---

## Curated Data Sets - Secret Satoshis Github Repositories

Secret Satoshis maintains curated data repositories with pre-built data sets, charts, and reports that follow internal standards.

| Repository | What It Contains | Link |
|---|---|---|
| **Bitcoin Report Library** | Report generation templates and curated data sets | [SecretSatoshis/Bitcoin-Report-Library](https://github.com/SecretSatoshis/Bitcoin-Report-Library) |
| **Bitcoin Chart Library** | Chart generation utilities, chart templates, and visualization data | [SecretSatoshis/Bitcoin-Chart-Library](https://github.com/SecretSatoshis/Bitcoin-Chart-Library) |

**How to access repo files:** Use the GitHub connector to browse synced repository contents when repo files, report templates, chart assets, report assets, or curated data sets are relevant to the user's question.

**Data hierarchy inside Claude:** Check uploaded knowledge first for conceptual answers. Check curated repo data next when a published artifact or template may already exist. If the needed data does not already exist in a curated form, get it fresh through the analysis tool.

---

## Knowledge Files - Secret Satoshis Content

The following Secret Satoshis articles and frameworks are uploaded as project knowledge files in this Claude project. These are supplemental knowledge - they provide research context, analytical frameworks, and educational content that the agent can draw on to enhance responses.

*All files below are already uploaded to this project.*

### Core

| File | Coverage |
|---|---|
| `agent21_knowledge_index.md` | This file - knowledge map of all available resources in the project |

### Platform & Agent

| File | Coverage |
|---|---|
| `start_here_secret_satoshis_faq.pdf` | Secret Satoshis platform overview, onboarding, ecosystem structure, subscriber guide |
| `bitcoin_ai_agent_21.pdf` | Agent 21 overview, capabilities, how it fits into Secret Satoshis |

### Bitcoin Foundations

| File | Coverage |
|---|---|
| `welcome_to_bitcoin.pdf` | Introduction to Bitcoin - plain-English foundations and why it matters |
| `bitcoin_technology_overview.pdf` | How Bitcoin works - money-as-technology framing, protocol fundamentals |

### Investment & Decision Frameworks

| File | Coverage |
|---|---|
| `bitcoin_investment_thesis.pdf` | Long-term Bitcoin thesis - adoption logic, macro and technology framing |
| `should_i_buy_bitcoin.pdf` | Practical decision framing - allocation mindset, risk framing, accumulation approach |

### On-Chain Analysis

| File | Coverage |
|---|---|
| `bitcoin_onchain_fundamentals.pdf` | Core on-chain fundamentals - what matters and why, baseline metric families |
| `bitcoin_onchain_network_health.pdf` | Network health - activity, security, participation, sustainability signals |
| `bitcoin_onchain_price_analysis.pdf` | On-chain indicators tied to valuation, cycle positioning, and price context |

### Market & Cycle

| File | Coverage |
|---|---|
| `bitcoin_market_price_analysis.pdf` | Price-based market frameworks and historical cycle context |
| `bitcoin_2025_year_end_review.pdf` | 2025 year in review - what happened and how it mapped to expectations |
| `bitcoin_2026_price_outlook.pdf` | 2026 outlook - scenario frameworks and forward-looking analysis |

### File Relationships

The knowledge files are interconnected:

- The **foundations** files build from introductory concepts to technical depth - Welcome to Bitcoin covers the essentials, Technology Overview goes deeper into protocol and monetary properties.
- The **investment** files bridge from thesis to action - Investment Thesis frames the long-term case, Should I Buy Bitcoin provides practical decision frameworks.
- The **on-chain** files start with fundamentals and branch into specific analytical lenses - Fundamentals covers the baseline, Network Health focuses on adoption and security, Price Analysis focuses on valuation signals.
- The **market** files cover price behavior and periodic assessments - Market Price Analysis provides cycle frameworks, the Year End Review and Price Outlook are periodic snapshots.
- On-chain and market analysis are complementary lenses on the same underlying questions - on-chain approaches from network data, market approaches from price data.

---

## External Resources

Trusted external references the agent can cite or direct users to.

### Secret Satoshis

| Resource | URL |
|---|---|
| Secret Satoshis (Main Site) | https://www.secretsatoshis.com/ |
| Secret Satoshis GitHub | https://github.com/SecretSatoshis |

### BRK (Bitcoin Research Kit)

| Resource | URL |
|---|---|
| BRK GitHub Repo | https://github.com/bitcoinresearchkit/brk |
| BRK API Endpoint | https://bitview.space/api |

---

If the needed knowledge is not in an uploaded file or curated data set, answer from foundational Bitcoin knowledge.

The agent always has access to live data by calling the bitview.space API via the analysis tool, and can discover curated data sets via the GitHub connector.
