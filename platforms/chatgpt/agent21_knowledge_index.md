# Agent 21 — ChatGPT Knowledge Index

> **Status:** Expected deployment inventory, not proof of the live GPT configuration.
> Repository manifest version 1.3, reviewed 2026-08-24. Verify every file and capability
> in the GPT editor before publishing.

## 1. Secret Satoshis surfaces

| Surface | Purpose | Link |
|---|---|---|
| Website | Main Secret Satoshis site | [secretsatoshis.com](https://www.secretsatoshis.com/) |
| Newsletter | Published research, guides, and market analysis | [Secret Satoshis on Substack](https://newsletter.secretsatoshis.com/) |
| Market Dashboard | Current Bitcoin market data, valuation models, and cycle context; updated daily | [dashboard.secretsatoshis.com](https://dashboard.secretsatoshis.com/) |
| Chart Library | Interactive charts for price, on-chain activity, supply, and valuation | [charts.secretsatoshis.com](https://charts.secretsatoshis.com/) |
| GitHub | Public repositories | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| X | Public commentary and updates | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |
| ChatGPT Agent | Recorded public Agent 21 link; availability and live version require verification | [Agent 21 on ChatGPT](https://chatgpt.com/g/g-BZXtVdU6M-agent-21) |

## 2. Expected capabilities

| Capability | Intended use |
|---|---|
| Uploaded Knowledge | Secret Satoshis research and Agent 21 reference material |
| BRK Action | Live and historical Bitcoin market and on-chain series |
| Mempool.space Action | Current Bitcoin network state and public block, transaction, and address lookup |
| Polymarket Action | Relevant public market-implied expectations subject to liquidity, activity, resolution, and Bitcoin-relevance checks |
| GitHub Action | Small public repository files and directory listings |
| Code Interpreter & Data Analysis | Calculations, validation, charts, and output files after retrieval |

The Instructions field defines behavior, source precedence, and tool policy. This index
only records the resources the deployment is expected to contain.

## 3. Public Knowledge files

| File | Purpose | Repository status |
|---|---|---|
| `agent21_knowledge_index.md` | Deployment inventory and source map | Present |
| `brk-reference.md` | BRK series semantics, ranges, units, discovery, and custom derived calculations | Present |
| `data-analysis-guide.md` | Units, parsing, warmups, chart conventions, and artifact requirements | Present |
| `mempool-reference.md` | Bitcoin explorer units, interpretation, address privacy, and retrieval rules | Present |
| `polymarket-reference.md` | Bitcoin relevance, market-quality checks, probability interpretation, and provenance | Present |

## 4. Public repositories

| Repository | Purpose | Link |
|---|---|---|
| `SecretSatoshis/Bitcoin-Agent-21` | Agent identity, prompt, Knowledge guides, and Action contracts | [Bitcoin-Agent-21](https://github.com/SecretSatoshis/Bitcoin-Agent-21) |
| `SecretSatoshis/Bitcoin-Report-Library` | Public report code and curated report datasets | [Bitcoin-Report-Library](https://github.com/SecretSatoshis/Bitcoin-Report-Library) |
| `SecretSatoshis/Bitcoin-Chart-Library` | Chart logic, definitions, and visualization assets | [Bitcoin-Chart-Library](https://github.com/SecretSatoshis/Bitcoin-Chart-Library) |
| `SecretSatoshis/Bitcoin-Investment-Strategy` | Runnable Bitcoin savings-plan notebook and supporting data pipeline | [Bitcoin-Investment-Strategy](https://github.com/SecretSatoshis/Bitcoin-Investment-Strategy) |
| `SecretSatoshis/Secret-Satoshis-Website` | Main Secret Satoshis website and landing-page source | [Secret-Satoshis-Website](https://github.com/SecretSatoshis/Secret-Satoshis-Website) |
| `SecretSatoshis/Trey-Brunson-Website` | TreyBrunson.com personal website and landing-page source | [Trey-Brunson-Website](https://github.com/SecretSatoshis/Trey-Brunson-Website) |
| `SecretSatoshis/.github` | Secret Satoshis public GitHub profile and repository directory | [SecretSatoshis profile](https://github.com/SecretSatoshis/.github) |

## 5. Expected private Knowledge files

These PDFs are intentionally absent from the public repository. Their filenames,
document versions, publication/as-of dates, review status, and live upload state must be
verified from the private deployment bundle.

The source column is the authority on which published post each file was exported from.
Filenames do not track post titles: Substack exports as `{title} - Secret Satoshis.pdf`, and
even that lags a retitle — the Agent 21 export is still named for the old title. Always match
on the source post, never on the filename.

Two naming conventions are live. The two files re-exported after the August rewrites use the
Substack convention; the remaining six predate it and keep their snake_case names. Expect
those to change when they are next re-exported.

### Platform and agent

| File | Source post | Current title |
|---|---|---|
| `Start Here - Secret Satoshis.pdf` | `/p/start-here` | Start Here |
| `Bitcoin AI Agent 21 - Secret Satoshis.pdf` | `/p/agent-21` | Agent 21 - Bitcoin AI Agent |

### Bitcoin foundations

| File | Source post | Current title |
|---|---|---|
| `welcome_to_bitcoin.pdf` | `/p/welcome-to-bitcoin` | Welcome To Bitcoin |
| `bitcoin_technology_overview.pdf` | `/p/bitcoin-technology` | Bitcoin Technology Overview |

### Investment and decision frameworks

| File | Source post | Current title |
|---|---|---|
| `bitcoin_investment_thesis.pdf` | `/p/bitcoin-ahead-of-the-curve` | Bitcoin Adoption Thesis |
| `should_i_buy_bitcoin.pdf` | `/p/should-i-buy-bitcoin` | Should I buy bitcoin? |

### Market and cycle

| File | Source post | Current title |
|---|---|---|
| `bitcoin_2025_year_end_review.pdf` | `/p/bitcoin-2025-year-end-review` | Bitcoin 2025 Year End Review |
| `bitcoin_2026_price_outlook.pdf` | `/p/bitcoin-2026-price-outlook` | Bitcoin 2026 Price Outlook |

## 6. Expected inventory total

- Public Markdown Knowledge files: 5
- Private PDF Knowledge files: 8
- Expected GPT Knowledge total: 13

The total is a manifest count only. A live deployment is verified only after all 13 files
are visible in the GPT editor and pass the Preview tests in `README.md`.
