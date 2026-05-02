# Agent 21 on ChatGPT

Deployment assets for the ChatGPT Custom GPT version of Agent 21.

---

## Instructions

Paste `platforms/chatgpt/system_prompt.md` into the GPT's **Instructions** field.

This file is the ChatGPT-specific runtime prompt. It is a compressed version of the canonical prompt at `identity/system_prompt.md`, rewritten for the Custom GPT interface:
- uploaded **Knowledge** files
- configured **Actions**
- the built-in **Python** tool

## Knowledge Files

Upload the following files to the GPT's **Knowledge** section:

- `platforms/chatgpt/agent21_knowledge_index.md`
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

**Total: 17 files** (5 markdown + 12 PDFs). ChatGPT allows up to 20.

Use the ChatGPT-specific knowledge index above rather than the general repo-level index. It is written for the Custom GPT runtime where the knowledge files are already uploaded, the Actions are already configured, and the Python tool is built in.

## Actions

Configure two Actions under **Actions > Create new action**:

- **bitview.space (BRK API):** Paste `platforms/chatgpt/tools/brk_api/openapi_metrics.json` — no authentication
- **GitHub:** Paste `tools/github/openapi_spec.yaml` — no authentication

`platforms/chatgpt/tools/brk_api/openapi_metrics.json` is the ChatGPT Action spec for BRK's current **series** API. It is a vendored, upstream-aligned subset intended for GPT Actions, not the full BRK reference spec.

## Runtime Pair

The two primary ChatGPT runtime files are:

- `platforms/chatgpt/system_prompt.md` — behavior and tool policy for the Custom GPT
- `platforms/chatgpt/agent21_knowledge_index.md` — map of uploaded knowledge, configured Actions, and standard tool usage patterns

Keep those files aligned whenever ChatGPT deployment logic changes.

---

Canonical system prompt: [`identity/system_prompt.md`](../../identity/system_prompt.md)
