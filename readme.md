# Agent 21 — Bitcoin AI Agent

**Open-source ChatGPT agent for Bitcoin research and analysis, maintained by [Secret Satoshis](https://newsletter.secretsatoshis.com/).**

Agent 21 combines curated Bitcoin research with live market and on-chain series from the
[Bitcoin Research Kit (BRK)](https://github.com/bitcoinresearchkit/brk), current public
Bitcoin network state from [Mempool.space](https://mempool.space/), and selectively used
prediction-market context from [Polymarket](https://polymarket.com/). It is designed to
explain Bitcoin from first principles, distinguish evidence from interpretation, and
surface risks alongside opportunities.

## What Goes In and What Comes Out

Inputs can include:

- a user's Bitcoin question or requested analysis
- uploaded Secret Satoshis research
- live BRK series requested through a read-only Action
- current public Bitcoin network, block, transaction, fee, mining, or user-requested
  address data through a read-only Mempool.space Action
- relevant public prediction-market data through a read-only Polymarket Action
- small public repository files requested through a read-only GitHub Action
- user-provided files supported by ChatGPT

Outputs can include:

- Bitcoin explanations and research synthesis
- current or historical market and on-chain analysis
- current network-state and public blockchain lookup results
- carefully qualified Bitcoin-relevant market-implied expectations
- derived metrics, tables, and charts
- analysis files generated with Code Interpreter & Data Analysis

Agent 21 does not provide standalone analysis or recommendations for alt-coins, tokens,
NFTs, or DeFi.

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
| `PRIVACY.md` | Privacy disclosure for the public GPT and its external Actions |

The deployed GPT uses the smaller BRK Action schema, not the full development snapshot.
Keeping the Action surface narrow improves tool selection and stays within ChatGPT Action
response limits.

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

See [the ChatGPT deployment guide](platforms/chatgpt/README.md) for the exact setup and
Preview tests.

## Tool Contracts

- The full BRK snapshot and the GPT-specific subset are aligned to upstream BRK
  `v0.11.2`.
- All four Action schemas use OpenAPI 3.1, HTTPS, explicit unauthenticated security, unique
  operation IDs, and read-only GET operations.
- The ChatGPT-specific Mempool.space and Polymarket schemas keep path parameters inline
  and give every object response named properties for compatibility with the current GPT
  editor importer.
- The Mempool.space Action cannot broadcast or accelerate transactions and exposes no
  wallet operations. Public address lookup is limited to validation and summary
  statistics, with privacy and attribution safeguards.
- The Polymarket Action cannot trade or access accounts, wallets, orders, or positions.
  Its use is limited to materially Bitcoin-relevant markets that pass contextual
  liquidity, activity, spread, recency, and resolution-quality checks without a fixed
  dollar threshold.
- The GitHub Action is deliberately limited to the repository contents endpoint. It is
  appropriate for small public files and directories, not large blobs.
- Action schemas should be retested in the GPT editor whenever BRK, Mempool.space,
  Polymarket, GitHub, or ChatGPT Action requirements change.

## Main Surfaces

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
