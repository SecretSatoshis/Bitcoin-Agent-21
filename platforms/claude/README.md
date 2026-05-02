# Agent 21 on Claude

Files and instructions for deploying Agent 21 as a Claude custom project.

---

## Project Instructions

Paste the contents of `system_prompt.md` (from this folder) into the project's **Project Instructions** field. This is adapted from the canonical prompt at `identity/system_prompt.md` for the Claude project environment.

## Knowledge Files

Upload the following to the project's **Knowledge** section:

- `platforms/claude/agent21_knowledge_index.md`
- `resources/skills/brk.md`
- `resources/skills/report_generation.md`
- `resources/skills/voice.md`
- `resources/skills/data_analysis.md`
- 12 Secret Satoshis PDFs (located in `resources/secret_satoshis/`):
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

**Total: 17 files** (5 markdown + 12 PDFs). Knowledge files persist across sessions in Claude projects.

Use the Claude-specific knowledge index above rather than the general repo-level index. It is written for the Claude project environment where the knowledge files are already uploaded, the GitHub connector is available, and the analysis tool is built in.

## GitHub Connector

1. Go to project settings > Connectors
2. Enable the GitHub integration
3. Connect the following repositories:
   - `SecretSatoshis/Bitcoin-Report-Library`
   - `SecretSatoshis/Bitcoin-Chart-Library`
4. Sync repository contents so files are accessible within the project

## Live Data Access

No connector setup is needed for bitview.space. Claude's built-in analysis tool can call the bitview.space API directly via Python `requests`. The system prompt and knowledge index instruct Agent 21 to use the analysis tool lazily when the current request actually needs live Bitcoin data.

Agent 21 should use BRK's current **series** API, not the legacy metrics routes. The vendored BRK docs/specs in this repo are aligned to the v0.2+ series model and should be refreshed from current upstream BRK docs when BRK changes.

---

Canonical system prompt: [`identity/system_prompt.md`](../../identity/system_prompt.md)
