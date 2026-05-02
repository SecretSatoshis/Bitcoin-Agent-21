# Agent 21 - ChatGPT Knowledge Index

> **Purpose:** This is the ChatGPT runtime map for Agent 21. It shows what this GPT already has access to and where each resource lives. Use the individual skill files for detailed workflows.

---

## 1. Secret Satoshis Resources

These are the main Secret Satoshis surfaces and public references connected to this GPT:

| Surface | What It Is | Link |
|---|---|---|
| Website | Main Secret Satoshis site | [secretsatoshis.com](https://www.secretsatoshis.com/) |
| Newsletter | Published research, guides, and market analysis | [Secret Satoshis on Substack](https://www.newsletter.secretsatoshis.com/) |
| GitHub | Open-source repos across the stack | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| X | Public commentary and updates | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |
| ChatGPT Agent | The deployed Agent 21 Custom GPT | [Agent 21 on ChatGPT](https://chatgpt.com/g/g-BZXtVdU6M-agent-21) |

---

## 2. Tool Surfaces

This GPT already has these tool surfaces:

| Surface | Access | What It Gives |
|---|---|---|
| Uploaded Knowledge | already uploaded inside this GPT | Secret Satoshis research, Agent 21 knowledge files, shared skills |
| bitview.space Action | configured Action | live and historical Bitcoin market and on-chain data |
| GitHub Action | configured Action | public repo contents, templates, CSVs, and code |
| Python | built-in tool | charting, transformations, calculations, and analysis after retrieval |

ChatGPT-specific runtime notes:

- BRK Action calls are JSON-first in this runtime.
- Large GitHub files may require `getRepoContent` followed by `getRepoBlob`.
- Python is for analysis after retrieval, not for data access.

---

## 3. Shared Skills

These files teach Agent 21 how to perform specific tasks. Consult the relevant one before doing the task.

| File | Role |
|---|---|
| `voice.md` | Response sizing, tone, source-voice normalization, final phrasing |
| `data_analysis.md` | Data parsing, transformations, charting patterns, visual conventions |
| `brk.md` | Reference file for the bitview.space Action — BRK semantics, naming, discovery, range logic, derived calculations |
| `report_generation.md` | Template-driven report generation from Report Library |

---

## 4. Secret Satoshis Repos

These are the main repos the GPT may need to inspect through GitHub:

| Repository | What It Is For | Link |
|---|---|---|
| `SecretSatoshis/Bitcoin-Agent-21` | Agent identity, prompts, knowledge files, skills, tool contracts | [Bitcoin-Agent-21](https://github.com/SecretSatoshis/Bitcoin-Agent-21) |
| `SecretSatoshis/Bitcoin-Report-Library` | Canonical report templates and curated report datasets | [Bitcoin-Report-Library](https://github.com/SecretSatoshis/Bitcoin-Report-Library) |
| `SecretSatoshis/Bitcoin-Chart-Library` | Chart logic, definitions, and visualization assets | [Bitcoin-Chart-Library](https://github.com/SecretSatoshis/Bitcoin-Chart-Library) |

---

## 5. Uploaded Secret Satoshis Knowledge Files

These files are already uploaded to this GPT:

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
