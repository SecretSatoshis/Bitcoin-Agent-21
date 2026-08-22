# Agent 21 Privacy Policy

Last updated: August 22, 2026

Agent 21 is a custom GPT that answers Bitcoin-related questions using uploaded reference
material and four read-only external Actions.

## Data Sent to External Services

When an Action is needed, ChatGPT may send only the parameters required for that request:

- **Bitcoin Research Kit (bitview.space):** a Bitcoin series name, index, range, and
  optional result limit.
- **Mempool.space (mempool.space):** the requested public network endpoint and, when the
  user requests a lookup, a public block hash, transaction ID, block height, or Bitcoin
  address. Bitcoin addresses and transaction IDs are public pseudonymous identifiers but
  may still be privacy-sensitive. Do not submit an address or transaction ID that you do
  not want sent to mempool.space.
- **Polymarket (gamma-api.polymarket.com):** public tag or market identifiers and narrow
  discovery filters such as a tag, status, liquidity, volume, order, or pagination
  cursor. The Action does not access a user's Polymarket account or activity.
- **GitHub (api.github.com):** a public repository owner, repository name, file or
  directory path, and optional branch, tag, or commit reference.

None of the Actions uses an Agent 21 account, API key, wallet, or user login. The Actions
do not write, modify, or delete external data. They cannot broadcast Bitcoin
transactions, accelerate transactions, place or cancel prediction-market orders, connect
wallets, or access private positions.

## Storage and Processing

This open-source project does not operate an intermediary Action server and does not
independently receive or store Action requests. Requests go from ChatGPT to the external
services named above. OpenAI, BRK's operator, and GitHub may process or retain request
data under their own terms and privacy policies. Mempool.space and Polymarket may do the
same for requests sent to their public APIs.

Uploaded files and conversations are handled by ChatGPT according to the user's ChatGPT
plan, workspace settings, and OpenAI policies.

## Scope

The public Action schemas expose read-only Bitcoin data, public blockchain lookups,
public prediction-market data, and public GitHub repository content. They do not request
private repository access, wallet credentials, private keys, seed phrases, account
positions, or personal account information.

If the Action configuration or data flows change, this policy must be updated before the
public GPT is republished.

## Contact

Questions can be submitted through the
[Bitcoin-Agent-21 GitHub repository](https://github.com/SecretSatoshis/Bitcoin-Agent-21/issues).
