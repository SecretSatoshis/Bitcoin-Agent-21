# Agent 21 - Claude Knowledge Index

> **Purpose:** This is the Claude runtime map for Agent 21. It shows what this Claude project already has access to and where each resource lives. Use the individual skill files for detailed workflows.

---

## 1. Secret Satoshis Resources

These are the main Secret Satoshis surfaces and public references connected to this Claude project:

| Surface | What It Is | Link |
|---|---|---|
| Website | Main Secret Satoshis site | [secretsatoshis.com](https://www.secretsatoshis.com/) |
| Newsletter | Published research, guides, and market analysis | [Secret Satoshis on Substack](https://newsletter.secretsatoshis.com/) |
| GitHub | Open-source repos across the stack | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| X | Public commentary and updates | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |

---

## 2. Tool Surfaces

This Claude project already has these tool surfaces:

| Surface | Access | What It Gives |
|---|---|---|
| Uploaded Knowledge | already uploaded inside this Claude project | Secret Satoshis research, Agent 21 knowledge files, shared skills |
| GitHub Connector | configured connector | public repo contents, templates, CSVs, and code |
| Analysis Tool | built-in tool | live Bitcoin data retrieval, charting, transformations, calculations, and analysis |

Claude-specific runtime notes:

- Use the analysis tool with Python `requests` for bitview.space (BRK API) when live or historical Bitcoin data is needed.
- Claude can use the analysis tool for data access and analysis in the same workflow.
- Prefer CSV for BRK retrieval in Claude when working with time series or analysis-sized data, unless JSON is more appropriate for a small metadata or latest-value response.
- Use the GitHub connector for repo contents only when the current request needs repository files, curated datasets, templates, or code.

---

## 3. Shared Skills

These files teach Agent 21 how to perform specific tasks. Consult the relevant one before doing the task.

| File | Role |
|---|---|
| `voice.md` | Response sizing, tone, source-voice normalization, final phrasing |
| `data_analysis.md` | Data parsing, transformations, charting patterns, visual conventions |
| `brk.md` | Reference file for bitview.space (BRK API) usage — BRK semantics, naming, discovery, range logic, derived calculations |

Keep this file focused on what exists. Let those files define the detailed workflows.

---

## 4. Secret Satoshis Repos

These are the main repos the Claude project may need to inspect through GitHub:

| Repository | What It Is For | Link |
|---|---|---|
| `SecretSatoshis/Bitcoin-Agent-21` | Agent identity, prompts, knowledge files, skills, tool contracts | [Bitcoin-Agent-21](https://github.com/SecretSatoshis/Bitcoin-Agent-21) |
| `SecretSatoshis/Bitcoin-Report-Library` | Public report code and curated report datasets | [Bitcoin-Report-Library](https://github.com/SecretSatoshis/Bitcoin-Report-Library) |
| `SecretSatoshis/Bitcoin-Chart-Library` | Chart logic, definitions, and visualization assets | [Bitcoin-Chart-Library](https://github.com/SecretSatoshis/Bitcoin-Chart-Library) |

---

## 5. Uploaded Secret Satoshis Knowledge Files

These files are already uploaded to this Claude project:

### Platform and Agent

- `start_here_secret_satoshis_faq.pdf`
- `bitcoin_ai_agent_21.pdf`

### Bitcoin Foundations

- `welcome_to_bitcoin.pdf`
- `bitcoin_technology_overview.pdf`

### Investment and Decision Frameworks

- `bitcoin_investment_thesis.pdf`
- `should_i_buy_bitcoin.pdf`

### On-Chain Analysis

- `bitcoin_onchain_fundamentals.pdf`
- `bitcoin_onchain_network_health.pdf`
- `bitcoin_onchain_price_analysis.pdf`

### Market and Cycle

- `bitcoin_market_price_analysis.pdf`
- `bitcoin_2025_year_end_review.pdf`
- `bitcoin_2026_price_outlook.pdf`

---
