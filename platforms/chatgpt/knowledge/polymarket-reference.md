# Polymarket Reference for Agent 21

Use the Polymarket Action only as a source of public market-implied expectations that
materially inform Bitcoin analysis. It is a contextual sentiment and expectations
source—not a source of observed Bitcoin network facts, objective probabilities, or
investment instructions.

## Relevant subject matter

A market may be useful when its outcome has a clear transmission path to Bitcoin. That
can include:

- Bitcoin adoption, price milestones, protocol events, mining, or regulation
- crypto policy, enforcement, stablecoins, exchanges, or market structure when the
  Bitcoin connection is material
- interest rates, inflation, central-bank policy, fiscal policy, liquidity, recession,
  or other macroeconomic conditions that affect risk appetite or Bitcoin valuation
- elections, legislation, appointments, court decisions, or geopolitical events when a
  plausible policy, liquidity, regulatory, or market channel to Bitcoin can be explained

Do not use an unrelated political, sports, entertainment, or alt-coin market merely
because it is active. Do not turn contextual crypto markets into standalone alt-coin
recommendations. State the Bitcoin connection instead of leaving it implicit.

## Candidate selection

Start with a narrow topical tag slug. Resolve it to an exact tag ID, then request a small
tagged market set. If the slug does not resolve, do not invent an ID. Before relying on a
candidate, inspect its exact market record and its included event summary.

Use judgment rather than a fixed dollar threshold. Market scale varies by topic and time
horizon, so evaluate liquidity and quality relative to other genuinely relevant
candidates. Prefer markets that are:

- active, open, and accepting orders when a current expectation is needed
- recently updated and consistent with the requested time horizon
- meaningfully liquid and actively traded relative to comparable relevant markets
- supported by cumulative and recent volume rather than a stale historical total alone
- quoted with a usable bid/ask spread and internally coherent last price
- governed by specific, understandable resolution criteria and a credible resolution
  source

Reject or clearly qualify markets that are thin, stale, inactive, closed, ambiguously
worded, far outside the relevant horizon, easily manipulated, or materially inconsistent
across price fields. If visible data suggests concentration or other market-quality risk,
disclose it. Absence of such data is not proof that the risk is absent.

Liquidity and volume filters in the Action are optional tools. Do not encode or apply one
universal minimum. First identify the relevant candidate set, compare its scale and
trading quality, and then use a defensible adaptive filter if one helps reduce noise.

## Reading probabilities correctly

- `outcomes` and `outcomePrices` may arrive as JSON-encoded strings. Parse both arrays
  and align values by array position; never assume the first price is `Yes` without
  checking the outcome labels.
- Treat an outcome price as an approximate market-implied probability only after checking
  the aligned label, current status, spread, liquidity, and update time.
- Bid, ask, last trade, and displayed outcome price can differ. Use the field that matches
  the claim and disclose a meaningful spread or disagreement.
- A displayed price of `0.62` is market pricing near 62%, not proof of a 62% real-world
  probability and not a model-calibrated forecast.
- Prices may reflect fees, market frictions, participant composition, speculation,
  information gaps, and manipulation risk. Do not add false precision.
- Closed or resolved markets may support historical analysis but must not be presented as
  current expectations.

## Resolution and provenance checks

Before citing a market-implied expectation, verify and report as appropriate:

1. the exact market question and outcome used
2. active, closed, and accepting-orders status
3. end date and last update time
4. the resolution criteria and resolution source
5. liquidity, cumulative volume, recent volume when available, and bid/ask spread
6. the retrieval time and the specific price field used

If the wording or resolution rule does not actually settle the proposition being
discussed, do not use the market as evidence for that proposition.

## Integration with other sources

- Use BRK for current and historical Bitcoin market or on-chain measurements.
- Use Mempool.space for current operational network state and public block, transaction,
  or address lookups.
- Use Polymarket only for a relevant market-implied expectation, clearly separated from
  observed facts and Agent 21's interpretation.
- Compare prediction-market information with primary facts or configured Bitcoin data
  when the conclusion matters. A Polymarket price does not validate the underlying claim.

The Action is read-only. Never offer to trade, place or cancel an order, connect a wallet,
inspect a user's positions, or request keys, signatures, or authentication data.

Official API reference: [Polymarket public market data](https://docs.polymarket.com/market-data/overview)
