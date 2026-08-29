# Agent 21: Bitcoin Intelligence

**Open-source ChatGPT agent for Bitcoin research and analysis, maintained by [Secret Satoshis](https://newsletter.secretsatoshis.com/).**

Agent 21 combines curated Bitcoin research with live market and on-chain series from the
[Bitcoin Research Kit (BRK)](https://github.com/bitcoinresearchkit/brk), current public
Bitcoin network state from [Mempool.space](https://mempool.space/), and prediction-market
context from [Polymarket](https://polymarket.com/).

Learn more in the [Agent 21 FAQ](https://newsletter.secretsatoshis.com/p/agent-21) on
Substack.

## Public Repository Layout

| Path | Purpose |
|---|---|
| `platforms/chatgpt/system_prompt.md` | Instructions pasted into the GPT editor |
| `platforms/chatgpt/agent21_knowledge_index.md` | Map of uploaded reference material and configured capabilities |
| `platforms/chatgpt/knowledge/` | Text-forward BRK, data-analysis, Mempool.space, and Polymarket reference files uploaded as Knowledge |
| `platforms/chatgpt/tools/brk_api/openapi_metrics.json` | JSON-only BRK OpenAPI subset used by the GPT Action |
| `platforms/chatgpt/tools/mempool_space/openapi.json` | Read-only Mempool.space OpenAPI subset used by the GPT Action |
| `platforms/chatgpt/tools/polymarket/openapi.json` | Read-only Polymarket OpenAPI subset used by the GPT Action |
| `tools/github/openapi_spec.yaml` | Read-only GitHub OpenAPI schema used by the GPT Action |
| `tools/brk_api/openapi_spec.json` | Full upstream BRK OpenAPI snapshot for development reference |
| `scripts/check_dependency_contract.py` | CI check that the public data-analysis library pins match the installed environment |
| `PRIVACY.md` | Privacy disclosure for the public GPT and its external Actions |

## How It Runs

Agent 21 runs as a custom GPT in ChatGPT:

1. The system prompt defines scope, behavior, tool order, and output checks.
2. Knowledge files provide curated source material and analysis methodology.
3. The BRK Action retrieves live Bitcoin market and on-chain series as JSON.
4. The Mempool.space Action retrieves current Bitcoin network state and exact public
   block, transaction, or user-requested address information.
5. The Polymarket Action retrieves a small set of relevant public tags and markets for
   carefully qualified market-expectations context.
6. The GitHub Action reads small public files or directory listings.
7. Code Interpreter & Data Analysis performs calculations, creates charts, and writes
   requested artifacts after data has been retrieved.

## Tool Contracts

- The full BRK snapshot and the GPT-specific subset are aligned to upstream BRK
  `v0.11.2`.
- The Mempool.space Action cannot broadcast or accelerate transactions and exposes no
  wallet operations. Public address lookup is limited to validation and summary
  statistics, with privacy and attribution safeguards.
- The Polymarket Action cannot trade or access accounts, wallets, orders, or positions.
  Its use is limited to materially Bitcoin-relevant markets that pass contextual
  liquidity, activity, spread, recency, and resolution-quality checks without a fixed
  dollar threshold.
- The GitHub Action is deliberately limited to the repository contents endpoint. It is
  appropriate for small public files and directories, not large blobs.

## Links and Resources

| Surface | Link |
|---|---|
| Agent 21 on ChatGPT | [chatgpt.com/g/g-BZXtVdU6M-agent-21](https://chatgpt.com/g/g-BZXtVdU6M-agent-21) |
| Secret Satoshis | [newsletter.secretsatoshis.com](https://newsletter.secretsatoshis.com/) |
| Secret Satoshis on X | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |
| Secret Satoshis GitHub | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| BRK | [github.com/bitcoinresearchkit/brk](https://github.com/bitcoinresearchkit/brk) |
| Mempool.space API | [mempool.space/docs/api/rest](https://mempool.space/docs/api/rest) |
| Polymarket API | [docs.polymarket.com](https://docs.polymarket.com/market-data/overview) |

## License

This repository is licensed under the [GNU General Public License v3.0](LICENSE).
