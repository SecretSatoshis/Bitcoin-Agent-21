# BRK Series and Derived-Metric Reference

> **Purpose:** Maintained deployment reference for (1) common BRK raw series identifiers
> Agent 21 can request and (2) custom derived on-chain calculations used by Secret
> Satoshis. The live BRK catalog is authoritative for currently available series and
> indexes.

---

## 1) BRK Data Source

- **BRK API Base:** [https://bitview.space/api](https://bitview.space/api)
- **BRK Repo:** [https://github.com/bitcoinresearchkit/brk](https://github.com/bitcoinresearchkit/brk)
- **Upstream compact spec:** [https://bitview.space/api.json](https://bitview.space/api.json)
- **Upstream full spec:** [https://bitview.space/openapi.json](https://bitview.space/openapi.json)
- **LLM docs:** [https://bitview.space/llms.txt](https://bitview.space/llms.txt), [https://bitview.space/llms-full.txt](https://bitview.space/llms-full.txt)

### 1.1 How to Call the BRK API

**Core idea:** BRK data is queried by **series name** + **index**.

#### Discovery and metadata

- **Search series:** `GET /api/series/search?q={query}&limit={n}`
- **Series info:** `GET /api/series/{series}`
- **Available indexes + aliases:** `GET /api/series/indexes`

#### Fetch series data

- **Standard:** `GET /api/series/{series}/{index}?start={start}&end={end}&limit={limit}`
- **Raw values only:** `GET /api/series/{series}/{index}/data?start={start}&end={end}&limit={limit}`
- **Latest value only:** `GET /api/series/{series}/{index}/latest`
- **Bulk:** `GET /api/series/bulk?series={s1},{s2},{s3}&index={index}&start={start}&end={end}&limit={limit}`

#### UTXO realized-price distributions

URPD routes are part of the full BRK API but are not exposed by the configured ChatGPT Action. Do not attempt to call or invent them in this deployment.

### 1.1.1 ChatGPT Action Capabilities

Treat the configured Action as authoritative. The full BRK API contains more routes and
parameters than this GPT can call.

| Capability | Available here |
|---|---|
| Series search, metadata, standard, raw, latest, and bulk routes | Yes |
| JSON | Yes |
| `format=csv` | No; the Action schema is JSON-only |
| URPD routes | No; absent from the Action schema |

If a needed capability is unavailable, disclose the limitation. Do not manufacture a
substitute endpoint or imply that a full reference spec is wired into the runtime.

### 1.2 Query Rules

- **The configured Action is JSON-only.** Its OpenAPI schema does not expose `format`, so do not request CSV through the Action. Parse the JSON response that actually arrives.
- **Use JSON for Action data.** Use CSV parsing only for uploaded or user-provided CSV files.
- **Use the current BRK range model.** `start` is inclusive and `end` is exclusive. Both accept `YYYY-MM-DD`, absolute integers, negative integers counted from the end, and ISO timestamps.
- **Use negative `start` for trailing windows.** Example: `start=-30` for the last 30 values, `start=-365` for the last 365 values, `start=-1` for the latest row.
- **Use explicit dates for exact historical windows.** Example: `start=YYYY-03-01&end=YYYY-04-01` for a calendar month range. Substitute the actual year being analysed; do not copy a year from this document.
- **Use `/latest` when only the newest value is needed.** Do not fetch a full wrapped series when a single latest value is enough.
- **Use `/data` when wrapper metadata is unnecessary.** This is useful when only the raw vector is needed for analysis.
- **Do not rely on `limit` for recent windows.** `limit` is secondary and can behave unexpectedly without a proper range anchor. Prefer `start=-N` for trailing windows or explicit `start` + `end` for fixed historical ranges.
- **Some series return compound values.** For example, OHLC-style series can return nested arrays rather than single numeric values. Confirm the series type with `GET /api/series/{series}` if the value shape matters.
- **Indexes accept aliases.** BRK accepts aliases like `day` for `day1`, `week` for `week1`, `month` for `month1`, and `dateindex` as an alias for `day1`.
- **Discover before guessing.** If a requested series is not in `BRK_SERIES`, use search plus metadata checks before fetching.

### 1.3 Series Discovery Workflow

Use this workflow whenever the requested series is not already in `BRK_SERIES`:

1. **Check the allowlist first.** If the exact series name is already in `BRK_SERIES`, use it directly.
2. **Search with a short concept stem.** Use `GET /api/series/search?q={query}&limit={n}` with concise terms like `velocity`, `profit`, `loss`, `hash`, `difficulty`, `supply`, `fees`, `realized`, `active`, or `price`.
3. **Try alternate concept words if needed.** Search is useful, but it is not perfect typo recovery. Prefer meaningful concept terms over misspelled full names.
4. **Inspect the candidate before fetching.** Use `GET /api/series/{series}` to confirm the series exists, supports the needed index, and returns the expected value type.
5. **Then fetch the data.** After a candidate is confirmed, call the standard, raw, latest, or bulk endpoint as needed.
6. **Use API suggestions on failures.** If a direct fetch returns `series_not_found`, use the suggested names from the error or rerun search with a broader term.

### 1.4 Format and Query Examples

- Latest dated daily price row as JSON: `GET /api/series/bulk?index=day&series=date,price_close&start=-1`
- Latest daily price value without a separate observation timestamp: `GET /api/series/price_close/day/latest`
- Last 365 dated daily rows as JSON: `GET /api/series/bulk?index=day&series=date,price_close&start=-365`
- Exact single-month daily window: `GET /api/series/price_close/day?start=YYYY-03-01&end=YYYY-04-01`
- Bulk valuation inputs as JSON: `GET /api/series/bulk?index=day&series=date,market_cap,realized_cap,supply&start=-365`
- Series discovery flow:
  - `GET /api/series/search?q=velocity&limit=10`
  - `GET /api/series/velocity_usd`
  - `GET /api/series/velocity_usd/day?start=-365`

---

## 2) BRK Raw Series Allowlist

> Use these common series names directly when calling BRK. They have been checked against the current BRK catalog, but the live catalog and discovery workflow remain authoritative.
>
> **If a name here returns `series_not_found`, treat this list as stale, not the API.** BRK renames series between versions. Search the catalog for the current name (§1.3), use it, and flag the mismatch so the list can be corrected — do not fall back to prose.

```py
BRK_SERIES = [
    "date",
    "timestamp",
    "price_close",
    "market_cap",
    "difficulty",
    "difficulty_adjustment",
    "hash_rate",
    "realized_price",
    "realized_cap",
    "sth_realized_price",
    "sth_realized_cap",
    "lth_realized_price",
    "lth_realized_cap",
    "coindays_destroyed_sum_24h",
    "utxo_count",
    "supply",
    "supply_usd",
    "sth_supply",
    "lth_supply",
    "fees_sum_24h_usd",
    "fees_sum_24h",
    "subsidy_sum_24h_usd",
    "subsidy_sum_24h",
    "coinbase_sum_24h_usd",
    "coinbase_sum_24h",
    "fees_average_24h_usd",
    "fees_average_24h",
    "effective_fee_rate_median",
    "fee_dominance",
    "utxos_over_1y_old_supply",
    "tx_count_sum_24h",
    "velocity_btc",
    "velocity_usd",
    "transfer_volume_sum_24h_usd",
    "inflation_rate",
    "nvt",
    "puell_multiple",
    "liveliness",
    "realized_profit_sum_24h",
    "realized_loss_sum_24h",
    "net_realized_pnl_sum_24h",
    "supply_in_profit",
    "supply_in_loss",
    "sopr_24h",
    "active_supply",
    "active_supply_sats",
    "active_supply_usd",
    "hash_price_ths",
    "hash_price_phs",
    "addrs_over_1sat_addr_count",
    "addrs_over_10sats_addr_count",
    "addrs_over_100sats_addr_count",
    "addrs_over_1k_sats_addr_count",
    "addrs_over_10k_sats_addr_count",
    "addrs_over_100k_sats_addr_count",
    "addrs_over_1m_sats_addr_count",
    "addrs_over_10m_sats_addr_count",
    "addrs_over_1btc_addr_count",
    "addrs_over_10btc_addr_count",
    "addrs_over_100btc_addr_count",
    "addrs_over_1k_btc_addr_count",
    "addrs_over_10k_btc_addr_count",
    "addrs_over_100k_btc_addr_count",
    "sending_addrs_average_24h",
    "receiving_addrs_average_24h",
    "active_addrs_average_24h",
    "addrs_under_1btc_addr_count",
    "addrs_under_10btc_addr_count",
    "addrs_under_10k_sats_addr_count",
    "addrs_under_1k_sats_addr_count",
    "addrs_under_10sats_addr_count",
    "utxos_1h_to_1d_old_supply",
    "utxos_under_1m_old_supply",
    "utxos_under_3m_old_supply",
    "utxos_under_6m_old_supply",
    "utxos_under_1y_old_supply",
    "utxos_under_2y_old_supply",
    "utxos_under_3y_old_supply",
    "utxos_under_4y_old_supply",
    "utxos_under_5y_old_supply",
    "utxos_under_10y_old_supply",
]
```

---

## 3) Derived Calculations Used by Secret Satoshis

> These are custom calculations built from BRK raw series. They are not BRK endpoint names.
> They are maintained internal definitions, not canonical BRK or industry-standard metric
> specifications. Preserve the stated formula, inputs, units, history, and warmup contract;
> coordinate any methodology change with downstream report and chart implementations.

### 3.0 History, Alignment, and Warmup Contract

Before calculating any derived metric:

1. Retrieve `date` or `timestamp` alongside all JSON value vectors. Require the same
   `index`, `start`, and `end` metadata and the same vector length before joining. Preserve
   each series' `version` for provenance, but do not require versions to match: BRK versions
   individual series independently.
2. Use sorted, unique timestamps. State the frequency and timezone. Do not align vectors
   solely because they happen to contain the same number of rows.
3. Preserve missing values unless the named methodology explicitly defines a fill rule.
4. For a rolling `Nd` calculation, require the full elapsed window and the methodology's
   minimum observation coverage. Leave the warmup blank. A partial result may be shown
   only when explicitly requested and must be labeled partial.
5. For `cumsum`, `expanding_*`, and any calculation labeled `all-time`, retrieve the full
   required history through the as-of date. If the beginning of the history is unknown or
   truncated, do not publish the result as all-time.
6. Validate nonzero denominators and compatible units before division.

In particular, `RevAllTimeUSD`, every thermocap calculation, `adjusted_bdd_mean`,
`hodl_bank_calc`, and `reserve_risk_calc` require complete methodology history. A trailing
request such as `start=-365` is not sufficient for those metrics.

### 3.1 Valuation / Cost Basis

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `RevAllTimeUSD` | `cumsum(coinbase_sum_24h_usd)` | `coinbase_sum_24h_usd` |
| `mvrv_ratio` / `CapMVRVCur` | `market_cap / realized_cap` | `market_cap`, `realized_cap` |
| `realized_price` *(recomputed)* | `realized_cap / supply` | `realized_cap`, `supply` |
| `nupl` | `(market_cap - realized_cap) / market_cap` | `market_cap`, `realized_cap` |
| `thermocap_multiple` | `market_cap / RevAllTimeUSD` | `market_cap`, `coinbase_sum_24h_usd` |
| `thermocap_price` | `RevAllTimeUSD / supply` | `coinbase_sum_24h_usd`, `supply` |
| `thermocap_price_multiple_4` | `(4 * RevAllTimeUSD) / supply` | `coinbase_sum_24h_usd`, `supply` |
| `thermocap_price_multiple_8` | `(8 * RevAllTimeUSD) / supply` | `coinbase_sum_24h_usd`, `supply` |
| `thermocap_price_multiple_16` | `(16 * RevAllTimeUSD) / supply` | `coinbase_sum_24h_usd`, `supply` |
| `thermocap_price_multiple_32` | `(32 * RevAllTimeUSD) / supply` | `coinbase_sum_24h_usd`, `supply` |
| `realizedcap_multiple_2` | `(2 * realized_cap) / supply` | `realized_cap`, `supply` |
| `realizedcap_multiple_3` | `(3 * realized_cap) / supply` | `realized_cap`, `supply` |
| `realizedcap_multiple_5` | `(5 * realized_cap) / supply` | `realized_cap`, `supply` |
| `realizedcap_multiple_7` | `(7 * realized_cap) / supply` | `realized_cap`, `supply` |

### 3.2 NVT and Transaction Value Models

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `NVTAdj` | `market_cap / transfer_volume_sum_24h_usd` | `market_cap`, `transfer_volume_sum_24h_usd` |
| `NVTAdj90` | `market_cap / mean(transfer_volume_sum_24h_usd, 90d)` | `market_cap`, `transfer_volume_sum_24h_usd` |
| `nvt_price` | `(median(NVTAdj, ~2y) * transfer_volume_sum_24h_usd) / supply` | `market_cap`, `transfer_volume_sum_24h_usd`, `supply` |
| `nvt_price_adj` | `(median(NVTAdj90, 1y) * transfer_volume_sum_24h_usd) / supply` | `market_cap`, `transfer_volume_sum_24h_usd`, `supply` |
| `nvt_price_multiple` | `price_close / nvt_price` | `price_close`, `market_cap`, `transfer_volume_sum_24h_usd`, `supply` |
| `nvt_price_multiple_ma` | `mean(nvt_price_multiple, 14d)` after a complete 14-day warmup | `price_close`, `market_cap`, `transfer_volume_sum_24h_usd`, `supply` |

### 3.3 Supply, Activity, and Network State

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `supply_pct_1_year_plus` | `(utxos_over_1y_old_supply / supply) * 100` | `utxos_over_1y_old_supply`, `supply` |
| `SplyActPct1yr` | `100 - supply_pct_1_year_plus` | `utxos_over_1y_old_supply`, `supply` |
| `TxCnt` | `tx_count_sum_24h` | `tx_count_sum_24h` |
| `supply_issued_ratio` | `supply / 21000000` | `supply` |
| `supply_issued_pct` | `(supply / 21000000) * 100` | `supply` |
| `pct_fee_of_reward` | `(fees_sum_24h / coinbase_sum_24h) * 100` | `fees_sum_24h`, `coinbase_sum_24h` |
| `one_year_plus_supply` | `utxos_over_1y_old_supply` | `utxos_over_1y_old_supply` |
| `under_one_year_supply` | `supply - utxos_over_1y_old_supply` | `utxos_over_1y_old_supply`, `supply` |
| `supply_in_profit_pct` | `(supply_in_profit / supply) * 100` | `supply_in_profit`, `supply` |
| `supply_in_loss_pct` | `(supply_in_loss / supply) * 100` | `supply_in_loss`, `supply` |

**Units — check before doing arithmetic on a BRK series:**

- `utxos_over_1y_old_supply` is **absolute BTC**, not a percentage. Divide it by `supply`
  and multiply by 100 to obtain `supply_pct_1_year_plus`.
- UTXO age describes dormancy, not observed market liquidity. Use
  `one_year_plus_supply` and `under_one_year_supply`. If an analysis uses them as a
  liquidity heuristic, call it an **age-based liquidity proxy**, not a measured liquidity
  classification.
- Use `supply_issued_ratio` for a 0–1 result and `supply_issued_pct` for percentage points.
  Treat the former name `pct_supply_issued` as a deprecated ambiguous alias and do not
  introduce it into new output.
- **Sanity-check absolute supply figures against the 21,000,000 cap.** Check bounded
  supply-share percentages against 0–100. Do not apply that bound to returns, changes,
  drawdowns, or other percentages that can validly be negative or exceed 100.

### 3.4 Miner Revenue and Production Models

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `miner_revenue_1_year` | `sum(coinbase_sum_24h_usd, 365d)` after a complete 365-day warmup | `coinbase_sum_24h_usd` |
| `miner_revenue_4_year` | `sum(coinbase_sum_24h_usd, 1460d)` after a complete 1,460-day warmup | `coinbase_sum_24h_usd` |
| `ss_multiple_1` | `market_cap / miner_revenue_1_year` | `market_cap`, `coinbase_sum_24h_usd` |
| `ss_price_1` | `miner_revenue_1_year / supply` | `coinbase_sum_24h_usd`, `supply` |
| `ss_multiple_4` | `market_cap / miner_revenue_4_year` | `market_cap`, `coinbase_sum_24h_usd` |
| `ss_price_4` | `miner_revenue_4_year / supply` | `coinbase_sum_24h_usd`, `supply` |

### 3.5 Quantity Theory / Velocity Models

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `tx_volume_yearly` | `sum(transfer_volume_sum_24h_usd, 365d)` after a complete 365-day warmup | `transfer_volume_sum_24h_usd` |
| `qtm_price` | `tx_volume_yearly / (supply * velocity_btc)` | `transfer_volume_sum_24h_usd`, `supply`, `velocity_btc` |
| `qtm_multiple` | `price_close / qtm_price` | `price_close`, `transfer_volume_sum_24h_usd`, `supply`, `velocity_btc` |
| `qtm_price_multiple_2` | `qtm_price * 2` | `transfer_volume_sum_24h_usd`, `supply`, `velocity_btc` |
| `qtm_price_multiple_5` | `qtm_price * 5` | `transfer_volume_sum_24h_usd`, `supply`, `velocity_btc` |
| `qtm_price_multiple_10` | `qtm_price * 10` | `transfer_volume_sum_24h_usd`, `supply`, `velocity_btc` |

### 3.6 Reserve Risk Pipeline

| Derived Calculation | Minimal Formula | Required BRK Series |
|---|---|---|
| `adjusted_bdd` | `coindays_destroyed_sum_24h / supply` | `coindays_destroyed_sum_24h`, `supply` |
| `adjusted_bdd_mean` | `expanding_mean(adjusted_bdd)` | `coindays_destroyed_sum_24h`, `supply` |
| `adjusted_bdd_above_avg` | `adjusted_bdd > adjusted_bdd_mean` | `coindays_destroyed_sum_24h`, `supply` |
| `vocd` | `price_close * adjusted_bdd` | `price_close`, `coindays_destroyed_sum_24h`, `supply` |
| `mvocd` | `median(vocd, 30d)` after a complete 30-day warmup | `price_close`, `coindays_destroyed_sum_24h`, `supply` |
| `daily_hodl_value` | `max(price_close - mvocd, 0)` | `price_close`, `coindays_destroyed_sum_24h`, `supply` |
| `hodl_bank_calc` | `cumsum(daily_hodl_value)` | `price_close`, `coindays_destroyed_sum_24h`, `supply` |
| `reserve_risk_calc` | `price_close / hodl_bank_calc` | `price_close`, `coindays_destroyed_sum_24h`, `supply` |

---

## 4) Quick Glossary

| Series | Meaning |
|---|---|
| `price_close` | Closing BTC price in USD for the selected index. |
| `market_cap` | Bitcoin market capitalization in USD. |
| `realized_cap` | Realized capitalization in USD. |
| `realized_price` | Realized cap divided by circulating supply. |
| `hash_rate` | Estimated Bitcoin network hash rate. |
| `difficulty` | Bitcoin mining difficulty. |
| `difficulty_adjustment` | Current or recent difficulty retarget change. |
| `supply` | Circulating Bitcoin supply. |
| `fees_sum_24h_usd` | Total miner fees over the last 24 hours in USD. |
| `coinbase_sum_24h_usd` | Total miner revenue over the last 24 hours in USD. |
| `tx_count_sum_24h` | Total transaction count over the last 24 hours. |
| `transfer_volume_sum_24h_usd` | Total USD-denominated transfer volume over the last 24 hours. |
| `velocity_btc` | BTC turnover rate proxy. |
| `velocity_usd` | USD turnover rate proxy. |
| `nvt` | Network value to transaction ratio. |
| `puell_multiple` | Miner revenue relative to its long-term norm. |
| `liveliness` | Share of coin-days destroyed relative to accumulated coin-days. |
| `sopr_24h` | Spent Output Profit Ratio over the last 24 hours. |
| `supply_in_profit` | Supply currently in profit. |
| `supply_in_loss` | Supply currently in loss. |
| `hash_price_ths` | Miner revenue per terahash per second. |

---

## 5) Discovery Workflow

**The single discovery procedure is §1.3 above.** Follow it whenever a series name is
unrecognised, absent from `BRK_SERIES`, or returns `series_not_found`.

Two points that apply once §1.3 has been run:

1. If multiple names are plausible, choose the closest semantic match and state the
   interpretation in the final analysis.
2. Only after §1.3 has been exhausted — search returned nothing, and the API offered no
   suggestions — say that the exact BRK series was not found and answer from Secret
   Satoshis research or foundational Bitcoin knowledge. **A `series_not_found` on a name
   taken from `BRK_SERIES` is not an exhausted search**; that list can go stale between
   BRK versions, so search for the current name before falling back to prose.

---

## 6) Agent 21 Policy Notes

- Agent 21 is **series-native** across prompts, examples, and tool assumptions.
- Agent 21 should share naming with the current Secret Satoshis data stack so Report, Chart, and Agent all operate on the same vocabulary.
- This ChatGPT Action returns **JSON**. Do not assume routes or parameters from the full BRK API are callable here.
