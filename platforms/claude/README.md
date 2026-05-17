# Agent 21 on Claude

Files and instructions for deploying Agent 21 as a Claude custom project.

---

## Instructions

Paste `platforms/claude/system_prompt.md` into the project's **Project Instructions** field.

This file is the Claude-specific runtime prompt.
- uploaded **Knowledge** files
- configured **GitHub connector**
- built-in **Analysis Tool**

## Knowledge Files

Upload the following to the project's **Knowledge** section:

- `platforms/claude/agent21_knowledge_index.md`
- `resources/skills/brk.md`
- `resources/skills/voice.md`
- `resources/skills/data_analysis.md`
- 12 Secret Satoshis PDFs from the private deployment bundle:
  - `start_here_secret_satoshis_faq.pdf`
  - `bitcoin_ai_agent_21.pdf`
  - `welcome_to_bitcoin.pdf`
  - `bitcoin_technology_overview.pdf`
  - `bitcoin_investment_thesis.pdf`
  - `should_i_buy_bitcoin.pdf`
  - `bitcoin_onchain_fundamentals.pdf`
  - `bitcoin_onchain_network_health.pdf`
  - `bitcoin_onchain_price_analysis.pdf`
  - `bitcoin_market_price_analysis.pdf`
  - `bitcoin_2025_year_end_review.pdf`
  - `bitcoin_2026_price_outlook.pdf`

**Total: 16 files** (4 markdown + 12 PDFs). Knowledge files persist across sessions in Claude projects.

Use the Claude-specific knowledge index above rather than the general repo-level index. It is written for the Claude project environment where the knowledge files are already uploaded, the GitHub connector is available, and the analysis tool is built in.

## GitHub Connector

1. Go to project settings > Connectors
2. Enable the GitHub integration
3. Connect the following repositories:
   - `SecretSatoshis/Bitcoin-Agent-21`
   - `SecretSatoshis/Bitcoin-Report-Library`
   - `SecretSatoshis/Bitcoin-Chart-Library`
4. Sync repository contents so files are accessible within the project

## Live Data Access

No connector setup is needed for bitview.space. Claude's built-in analysis tool can call the bitview.space API directly via Python `requests`. The system prompt and knowledge index instruct Agent 21 to use the analysis tool lazily when the current request actually needs live Bitcoin data.

Agent 21 should use BRK's current **series** API, not the legacy metrics routes. The vendored BRK docs/specs in this repo are aligned to the v0.2+ series model and should be refreshed from current upstream BRK docs when BRK changes.

---

## Runtime Pair

The two primary Claude runtime files are:

- `platforms/claude/system_prompt.md` — behavior and tool policy for the Claude project
- `platforms/claude/agent21_knowledge_index.md` — map of uploaded knowledge, GitHub connector, and standard tool usage patterns

Keep those files aligned whenever Claude deployment logic changes.

---
