# Mempool.space Reference for Agent 21

Use the Mempool.space Action for current Bitcoin mainnet operational state and exact
public blockchain objects. It complements BRK; it does not replace BRK's maintained
historical market and on-chain series.

## Appropriate uses

- current chain-tip height and hash
- recent block summaries or a block resolved by height or hash
- current mempool size and fee distribution
- current fee-rate estimates
- current difficulty-adjustment estimate
- recent hashrate, difficulty, or block-fee history exposed by the Action
- a user-requested public transaction ID and its confirmation status
- validation and high-level statistics for a user-requested public Bitcoin address

Use BRK instead when the question needs a maintained historical series, valuation model,
market data, cohort analysis, or on-chain aggregate that BRK exposes directly.

## Units and calculations

- One bitcoin equals 100,000,000 satoshis.
- Transaction and address values returned by this API are commonly denominated in
  satoshis. Convert to BTC only when useful and show the conversion.
- Fee-rate estimates are denominated in satoshis per virtual byte (`sat/vB`). They are
  estimates, not confirmation guarantees.
- `size` is serialized bytes, `weight` is weight units, and virtual size is derived from
  weight. Do not treat those fields as interchangeable.
- Unix timestamps are seconds unless an endpoint explicitly states otherwise. Convert
  them to an explicit timezone and preserve the original timestamp when precision
  matters.
- For an address summary, confirmed balance is
  `chain_stats.funded_txo_sum - chain_stats.spent_txo_sum`. Unconfirmed net flow is
  `mempool_stats.funded_txo_sum - mempool_stats.spent_txo_sum`. Keep those two values
  separate unless the requested calculation explicitly combines them.

## Interpretation rules

- Treat the response as mempool.space's current view of the public Bitcoin network.
  Unconfirmed transactions, fee estimates, the chain tip, and projected difficulty can
  change after retrieval.
- A transaction is not confirmed merely because it appears in the mempool. Report the
  `confirmed` status and, when confirmed, its block height and time.
- A difficulty adjustment returned before the end of the adjustment period is an
  estimate. Label it as such and state when it was retrieved.
- Hashrate is estimated from observed block production and difficulty; it is not a
  direct measurement of every miner.
- Explorer address totals describe outputs associated with an address. They do not prove
  the identity, ownership, control, purpose, or complete wallet balance of any person or
  organization. A wallet may use many addresses, and a reused or shared address can
  create misleading attribution.
- Do not infer an entity, label, or relationship that the Action did not return and the
  user did not independently establish.
- Cross-check surprising or decision-relevant results when another configured source
  measures the same concept, and explain material differences in scope or timestamp.

## Address and transaction privacy

A Bitcoin address or transaction ID is public but can still be privacy-sensitive. An
Action lookup sends the identifier to mempool.space.

- Use an address lookup only when the user supplies the address, explicitly asks for the
  lookup, or the address is essential to answer their direct request.
- Do not ask for private keys, seed phrases, wallet exports, signatures, or login data.
- Never transmit or repeat a private key or seed phrase. If one appears, warn the user
  that it is sensitive and do not use it in an Action.
- Explain that address-level observations are pseudonymous public-chain facts, not proof
  of personal identity.

## Retrieval discipline

Use the narrowest endpoint that answers the question. Prefer transaction status over the
full transaction object when only confirmation is needed. Avoid repeated requests, and
handle rate limits or oversized responses by stating the limitation rather than
inventing missing data.

Official API reference: [mempool.space REST API](https://mempool.space/docs/api/rest)
