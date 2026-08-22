# Agent 21 Data Analysis Reference

> **Purpose:** Methodology, units, and visual conventions for Agent 21 analysis. The
> code excerpts in this guide are self-contained for use as an uploaded ChatGPT knowledge file.

---

## 1. Data Workflow

Every data analysis task follows the same sequence.

1. **Identify data** — Consult `agent21_knowledge_index.md` to determine what data is needed and where it lives (BRK API, uploaded knowledge, curated data sets, user-provided data, etc.).
2. **Fetch data** — Retrieve current BRK data through the configured Action and repository content through the GitHub Action. Get all required data before processing.
3. **Process data** — Parse into a pandas DataFrame. Compute any derived metrics or transformations.
4. **Visualize** — Build the chart using matplotlib following the style standards below.
5. **Analyze** — Provide written interpretation alongside the chart to help the user understand what they're seeing. Lead with the key insight, provide context on what the data shows, and explain why it matters. This analysis is part of the response text, not on the chart itself.

**Critical:** Data retrieval (steps 1–2) and data processing (steps 3–5) are separate steps. Retrieve all data first, then process and visualize.

### 1.1 Units Convention

This applies to every Report Library CSV under
`https://secretsatoshis.github.io/Bitcoin-Report-Library/csv/` and to anything derived
from them. Getting it wrong produces a 100× error that still looks like a plausible
number, so check before computing.

- **Any column whose name carries a percent marker — `(%)`, `% Change`, `_pct` — is in
  percentage points.** `3.32` means 3.32%, never 332% and never 0.0332. This covers
  `Return (%)`, `Report Date Return (%)`, `ROI (%)`, `7 Day Change (%)`, `drawdown_pct`,
  and the `_7_change` / `_90_change` / `_MTD_change` / `_YTD_change` / `_YOY_change`
  families in `master_metrics_data.csv.gz`. **Do not multiply these by 100 again.**
- **`monthly_heatmap_data.csv` is also in percentage points** (`3.32` = 3.32%). Its
  columns are month names, so they carry no marker—this is the one file where the scale
  has to be known rather than read from the column name. **Do not multiply it by 100.**
- **Values are numeric, not pre-formatted.** No `$`, `,` or `%` characters to strip.
- **Missing data is empty (NaN)** — never `0`, never `inf`. A model warmup window is
  blank rather than zero-filled; treat a blank as "no value", not as zero.
- **Raw BRK series carry their own units** and are not normalised — see the units notes
  in `brk-reference.md` before doing arithmetic on one. In particular,
  supply-cohort series are
  absolute BTC, not shares.

**Sanity-check before publishing:** confirm the source filename and inspect representative
values before scaling. For example, a heatmap value near `10.0` means about 10%, as does a
master-metrics change value near `10.0`. Also check supply figures against the 21,000,000
cap and percentage values against plausible ranges. A result far outside those bounds is
probably a unit error, not a finding.

---

## 2. Secret Satoshis Visual Style

These standards are derived from the Secret Satoshis Bitcoin Chart Library. Follow them for all charts.

### Color Palette

```python
# Standard color rotation for chart lines
CHART_COLORS = [
    "#7149C6",  # Purple
    "#0079FF",  # Blue
    "#FF0060",  # Pink/Red
    "#22A699",  # Teal
    "#8c564b",  # Brown
    "#e377c2",  # Light pink
    "#7f7f7f",  # Gray
    "#bcbd22",  # Olive
    "#17becf",  # Cyan
]

# Bitcoin's signature color — always use for Bitcoin price
BITCOIN_ORANGE = "#FF9900"
```

**Rules:**
- Bitcoin price always gets `BITCOIN_ORANGE` (`#FF9900`)
- Other metrics rotate through `CHART_COLORS` in order
- Background is always white
- Grid lines are light gray, y-axis only
- **Price data uses log scale unless an explicit exception applies** — Bitcoin price and any price-denominated metric should use `y_scale="log"`. This shows proportional moves consistently across all time ranges. Use `y_scale="linear"` only if the user specifically requests it or the time range is very short (< 90 days). Generic chart helpers require the caller to choose the scale explicitly rather than guessing from column names.

### Typography & Layout

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Standard figure setup
def setup_chart(title, ylabel, figsize=(14, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title, fontsize=16, fontweight="bold", pad=15, loc="center")
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel("")
    ax.grid(axis="y", alpha=0.3)
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return fig, ax
```

### Axis Formatting

```python
# USD formatting for price axes
def format_usd(ax, decimals=0):
    if decimals == 0:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    else:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"${x:,.{decimals}f}"))

# BTC formatting
def format_btc(ax):
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"{x:,.0f} BTC"))

# Percentage formatting
def format_pct(ax):
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"{x:.1f}%"))

# Number formatting (generic)
def format_number(ax):
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))

# Date axis
import matplotlib.dates as mdates
def format_dates(ax):
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.tick_params(axis="x", labelrotation=45)
    for label in ax.get_xticklabels():
        label.set_horizontalalignment("right")
```

### Legend & Branding

```python
def finalize_chart(ax, data_source="", legend_handles=None, legend_labels=None):
    # Legend at bottom, horizontal. Callers with multiple axes can pass a
    # combined handle/label set so the secondary-axis entries are preserved.
    if legend_handles is None:
        legend_handles, legend_labels = ax.get_legend_handles_labels()
    if legend_handles:
        ax.legend(legend_handles, legend_labels,
                  loc="upper center", bbox_to_anchor=(0.5, -0.12),
                  ncol=3, frameon=False, fontsize=10)
    # Data source attribution
    if data_source:
        ax.annotate(data_source, xy=(1, -0.18), xycoords="axes fraction",
                    ha="right", fontsize=8, color="#666")
    # Watermark
    ax.text(0.5, 0.5, "SecretSatoshis.com", transform=ax.transAxes,
            fontsize=36, color="gray", alpha=0.15,
            ha="center", va="center")
    ax.figure.tight_layout()
```

### Artifact Output Contract

Interactive display is not a saved deliverable. Before producing a chart, establish:

- explicit output path and filename extension
- format and DPI (`180` minimum for ordinary publication output unless the destination
  defines another requirement)
- whether overwriting an existing file is authorized
- source/as-of metadata to retain with the artifact or adjacent manifest
- whether the figure must be closed after saving (default yes for batch work)

Use the self-contained helper below. It refuses implicit overwrites, requires an extension,
saves figure-scoped output, and closes the figure by default.

```python
from pathlib import Path
from typing import Mapping

def save_chart(
    fig,
    output_path,
    *,
    dpi=180,
    overwrite=False,
    close=True,
    metadata: Mapping[str, str] | None = None,
):
    """Save a chart deterministically and optionally release its figure."""
    import matplotlib.pyplot as plt

    path = Path(output_path).expanduser().resolve()
    if not path.suffix:
        raise ValueError("output_path must include a file extension")
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite existing chart: {path}")
    if dpi < 72:
        raise ValueError("dpi must be at least 72")

    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=dpi, bbox_inches="tight", metadata=dict(metadata or {}))
    if close:
        plt.close(fig)
    return path
```

---

## 3. Standard Chart Types

### 3.1 Time Series Line Chart

Single or multi-metric line chart over time.

```python
import pandas as pd
import matplotlib.pyplot as plt

def time_series_chart(df, metrics, title, ylabel, y_scale, data_source=""):
    """
    Standard time series line chart.

    Args:
        df: DataFrame with DatetimeIndex
        metrics: list of dicts [{"col": "column_name", "label": "Display Name", "color": "#hex"}]
        title: Chart title
        ylabel: Y-axis label
        y_scale: Required; either "log" or "linear". Use "log" for Bitcoin
            price and other price-denominated values unless an explicit
            exception applies.
        data_source: Attribution string (e.g., "Data: BRK API")
    """
    if y_scale not in {"linear", "log"}:
        raise ValueError('y_scale must be either "linear" or "log"')

    if y_scale == "log":
        non_positive = [
            m["col"]
            for m in metrics
            if (df[m["col"]].dropna() <= 0).any()
        ]
        if non_positive:
            raise ValueError(
                f"log scale requires positive values; check columns: {non_positive}"
            )

    fig, ax = setup_chart(title, ylabel)

    for i, m in enumerate(metrics):
        color = m.get("color", CHART_COLORS[i % len(CHART_COLORS)])
        ax.plot(df.index, df[m["col"]], label=m["label"], color=color, linewidth=1.5)

    if y_scale == "log":
        ax.set_yscale("log")

    format_dates(ax)
    finalize_chart(ax, data_source=data_source)
    plt.show()
```

### 3.2 Price with Indicator Bands

Primary metric with computed band lines (multiples, moving averages, thresholds).

```python
def price_band_chart(df, primary_col, primary_label, bands, title, ylabel="Price (USD)", data_source=""):
    """
    Primary metric with indicator bands.

    Args:
        df: DataFrame with DatetimeIndex
        primary_col: Column name for the primary metric
        primary_label: Display label for primary metric
        bands: list of dicts [{"col": "col_name", "label": "Label", "color": "#hex", "style": "--"}]
        title: Chart title
    """
    fig, ax = setup_chart(title, ylabel)

    # Primary line — on top
    ax.plot(df.index, df[primary_col], label=primary_label, color=BITCOIN_ORANGE, linewidth=2, zorder=10)

    # Band lines
    for i, b in enumerate(bands):
        color = b.get("color", CHART_COLORS[i % len(CHART_COLORS)])
        style = b.get("style", "-")
        ax.plot(df.index, df[b["col"]], label=b["label"], color=color,
                linewidth=1.2, linestyle=style, alpha=0.8)

    ax.set_yscale("log")
    format_usd(ax)
    format_dates(ax)
    finalize_chart(ax, data_source=data_source)
    plt.show()
```

### 3.3 Dual-Axis Chart

Two metrics with different scales sharing a time axis.

```python
def dual_axis_chart(df, left_metric, right_metric, title, data_source=""):
    """
    Dual y-axis chart.

    Args:
        left_metric: dict {"col": "col_name", "label": "Label", "ylabel": "Y Label", "color": "#hex"}
        right_metric: dict {"col": "col_name", "label": "Label", "ylabel": "Y Label", "color": "#hex"}
    """
    fig, ax1 = setup_chart(title, left_metric["ylabel"])

    # Left axis
    color1 = left_metric.get("color", BITCOIN_ORANGE)
    ax1.plot(df.index, df[left_metric["col"]], label=left_metric["label"],
             color=color1, linewidth=1.5)

    # Right axis
    ax2 = ax1.twinx()
    color2 = right_metric.get("color", CHART_COLORS[0])
    ax2.plot(df.index, df[right_metric["col"]], label=right_metric["label"],
             color=color2, linewidth=1.5)
    ax2.set_ylabel(right_metric["ylabel"], fontsize=12)
    ax2.spines["top"].set_visible(False)

    # Combined legend. Pass it to finalize_chart so it is not replaced by a
    # second legend containing only the left-axis metric.
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    format_dates(ax1)
    finalize_chart(
        ax1,
        data_source=data_source,
        legend_handles=lines1 + lines2,
        legend_labels=labels1 + labels2,
    )
    plt.show()
```

### 3.4 Area / Stacked Area Chart

For composition, distribution breakdowns, or cumulative metrics.

```python
def stacked_area_chart(df, metrics, title, ylabel, data_source=""):
    """
    Stacked area chart for composition/distribution data.

    Args:
        metrics: list of dicts [{"col": "col_name", "label": "Label"}]
    """
    fig, ax = setup_chart(title, ylabel)

    cols = [m["col"] for m in metrics]
    labels = [m["label"] for m in metrics]
    colors = [m.get("color", CHART_COLORS[i % len(CHART_COLORS)]) for i, m in enumerate(metrics)]

    ax.stackplot(df.index, *[df[c] for c in cols], labels=labels, colors=colors, alpha=0.7)

    format_dates(ax)
    finalize_chart(ax, data_source=data_source)
    plt.show()
```

### 3.5 Horizontal Bar Chart

For point-in-time comparisons across categories.

```python
def horizontal_bar_chart(data, title, xlabel, data_source=""):
    """
    Horizontal bar chart for category comparisons.

    Args:
        data: list of dicts [{"label": "Category", "value": 1000}]
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]
    colors = [CHART_COLORS[i % len(CHART_COLORS)] for i in range(len(data))]

    ax.barh(labels, values, color=colors)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_title(title, fontsize=16, fontweight="bold", pad=15)
    ax.grid(axis="x", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.patch.set_facecolor("white")

    finalize_chart(ax, data_source=data_source)
    plt.show()
```

---

## 4. Data Processing Patterns

### 4.1 Parsing Time Series Data

The configured BRK Action returns JSON. Use the JSON parser for Action responses and use the CSV parser only for user-provided or uploaded CSV text.

```python
import pandas as pd
from io import StringIO

def _parse_datetime_values(values, time_col, time_unit):
    """Parse either numeric epoch values or date/ISO strings."""
    raw_time = pd.Series(values, copy=False)
    numeric_time = pd.to_numeric(raw_time, errors="coerce")
    non_null = raw_time.notna()
    non_null_count = non_null.sum()
    numeric_count = numeric_time[non_null].notna().sum()

    if 0 < numeric_count < non_null_count:
        raise ValueError(
            f"{time_col} mixes numeric epochs with date-like strings"
        )

    if non_null_count and numeric_count == non_null_count:
        parsed_time = pd.to_datetime(
            numeric_time, unit=time_unit, errors="coerce", utc=True
        )
    else:
        parsed_time = pd.to_datetime(raw_time, errors="coerce", utc=True)

    if len(parsed_time) and parsed_time.isna().any():
        raise ValueError(f"{time_col} contains missing or unparseable timestamps")

    return parsed_time


def parse_csv_response(csv_text, time_col="timestamp", time_unit="s"):
    """
    Parse uploaded or user-provided CSV text into a DataFrame with DatetimeIndex.
    """
    df = pd.read_csv(StringIO(csv_text))

    if time_col not in df.columns:
        raise ValueError(f"CSV payload must include a {time_col!r} column")

    df[time_col] = _parse_datetime_values(df[time_col], time_col, time_unit).array
    df.set_index(time_col, inplace=True)
    df.sort_index(inplace=True)
    if not df.index.is_unique:
        raise ValueError("time-series timestamps must be unique")

    # Convert numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def parse_time_series(
    data,
    time_col="timestamp",
    time_unit="s",
    timestamps=None,
    value_col="value",
):
    """
    Parse JSON data into a DataFrame with DatetimeIndex.

    BRK's wrapped SeriesData and raw /data responses contain values but no
    per-row timestamps. For those shapes, pass the matching BRK `timestamp`
    series (either its wrapper or raw data array) through `timestamps`.

    Record-oriented inputs that already contain `time_col` do not need a
    separate timestamp vector.
    """

    def unwrap_values(payload):
        if isinstance(payload, dict) and "data" in payload:
            return payload["data"]
        return payload

    def validate_parallel_metadata(value_payload, timestamp_payload):
        if not isinstance(value_payload, dict) or not isinstance(timestamp_payload, dict):
            return
        keys = ("index", "start", "end")
        mismatches = {
            key: (value_payload.get(key), timestamp_payload.get(key))
            for key in keys
            if key in value_payload
            and key in timestamp_payload
            and value_payload.get(key) != timestamp_payload.get(key)
        }
        if mismatches:
            raise ValueError(
                f"BRK timestamp/value metadata does not align: {mismatches}"
            )

    values = unwrap_values(data)

    # A BRK wrapper is metadata plus a raw value vector. A raw vector has the
    # same timestamp requirement. Refuse to invent an index when it is absent.
    is_brk_wrapper = isinstance(data, dict) and "data" in data
    is_raw_vector = isinstance(values, list) and (
        not values or not isinstance(values[0], dict)
    )

    if is_brk_wrapper or is_raw_vector:
        if timestamps is None:
            raise ValueError(
                "BRK value vectors do not contain per-row timestamps; pass the "
                "matching timestamp series or supply timestamped records."
            )

        validate_parallel_metadata(data, timestamps)
        timestamp_values = unwrap_values(timestamps)
        if not isinstance(timestamp_values, list):
            raise TypeError("timestamps must be a list or a BRK SeriesData wrapper")
        if len(timestamp_values) != len(values):
            raise ValueError(
                "timestamp and value vectors must contain the same number of rows"
            )

        df = pd.DataFrame({time_col: timestamp_values, value_col: values})
    else:
        df = pd.DataFrame(data)

    if time_col not in df.columns:
        raise ValueError(f"record-oriented input must include a {time_col!r} column")

    df[time_col] = _parse_datetime_values(df[time_col], time_col, time_unit).array
    df.set_index(time_col, inplace=True)
    df.sort_index(inplace=True)
    if not df.index.is_unique:
        raise ValueError("time-series timestamps must be unique")

    # Convert scalar columns to numeric. Preserve compound BRK values such as
    # OHLC arrays for explicit expansion by the caller.
    for col in df.columns:
        contains_compound_values = df[col].dropna().map(
            lambda value: isinstance(value, (list, tuple, dict))
        ).any()
        if not contains_compound_values:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
```

### 4.2 Common Transformations

Every helper whose argument or generated label says `day` uses a calendar-time window and
requires a unique `DatetimeIndex`. If a methodology intentionally uses a fixed number of
observations instead, call pandas' observation-count operation explicitly and label the
result in observations rather than days.

For daily production metrics, the default warmup requires `window_days` observations and
leaves earlier rows blank. The reusable helper script additionally supports an explicit
`min_coverage` threshold. Set `allow_partial=True` only when the user or methodology asks
for a partial window, and include `partial` in the displayed label or disclosure.

#### Moving Averages & Smoothing

```python
def _calendar_series(df, col):
    """Return a time-ordered series suitable for calendar-window operations."""
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("day-based calculations require a DatetimeIndex")
    if not df.index.is_unique:
        raise ValueError("day-based calculations require a unique DatetimeIndex")
    return df[col].sort_index()


def _calendar_window(series, window_days, min_observations=None):
    if not isinstance(window_days, int) or window_days < 1:
        raise ValueError("window_days must be a positive integer")
    if min_observations is None:
        # Daily production metrics stay blank until the complete window exists.
        min_observations = window_days
    if not isinstance(min_observations, int) or min_observations < 1:
        raise ValueError("min_observations must be a positive integer")
    return series.rolling(f"{window_days}D", min_periods=min_observations)


def compute_moving_average(
    df, col, window_days, label=None, min_observations=None
):
    """Simple moving average over an actual calendar-day window."""
    label = label or f"{window_days}_day_ma_{col}"
    series = _calendar_series(df, col)
    df[label] = _calendar_window(
        series, window_days, min_observations
    ).mean()
    return df


def compute_ema(df, col, halflife_days, label=None):
    """Calendar-time EMA using a decay half-life measured in days."""
    if not isinstance(halflife_days, (int, float)) or halflife_days <= 0:
        raise ValueError("halflife_days must be positive")
    label = label or f"{halflife_days}_day_ema_{col}"
    series = _calendar_series(df, col)
    df[label] = series.ewm(
        halflife=f"{halflife_days}D", times=series.index, adjust=True
    ).mean()
    return df


def compute_rolling_median(
    df, col, window_days, label=None, min_observations=None
):
    """Median over an actual calendar-day window."""
    label = label or f"{window_days}_day_median_{col}"
    series = _calendar_series(df, col)
    df[label] = _calendar_window(
        series, window_days, min_observations
    ).median()
    return df
```

#### Ratios & Relationships

```python
def compute_ratio(df, numerator, denominator, label, on_zero="raise"):
    """Ratio between two columns, with an explicit zero-denominator policy."""
    zero_mask = df[denominator].eq(0)
    if zero_mask.any() and on_zero == "raise":
        raise ZeroDivisionError(f"{denominator} contains zero values")
    if on_zero not in {"raise", "nan"}:
        raise ValueError('on_zero must be "raise" or "nan"')
    df[label] = df[numerator] / df[denominator].mask(zero_mask)
    return df

def compute_difference(df, col_a, col_b, label):
    """Difference between two columns."""
    df[label] = df[col_a] - df[col_b]
    return df

def compute_multiple(df, col, factor, label):
    """Multiply a column by a constant (e.g., realized price × 3)."""
    df[label] = df[col] * factor
    return df
```

#### Change & Momentum

```python
def compute_pct_change(df, col, days=1, label=None):
    """Percent change from the observation at the exact calendar-day offset."""
    if not isinstance(days, int) or days < 1:
        raise ValueError("days must be a positive integer")
    label = label or f"{col}_pct_change_{days}d"
    series = _calendar_series(df, col)
    prior = series.shift(freq=f"{days}D")
    df[label] = (series / prior - 1) * 100
    return df

def compute_log_returns(df, col, label=None):
    """Log returns — better for compounding and statistical analysis."""
    import numpy as np
    label = label or f"{col}_log_return"
    df[label] = np.log(df[col] / df[col].shift(1))
    return df

def compute_drawdown(df, col, label=None):
    """Drawdown from running all-time high (as negative %)."""
    label = label or f"{col}_drawdown"
    running_max = df[col].cummax()
    df[label] = (df[col] - running_max) / running_max * 100
    return df

def compute_distance_from_high(df, col, label=None):
    """Current value as % of all-time high."""
    label = label or f"{col}_pct_of_ath"
    df[label] = df[col] / df[col].cummax() * 100
    return df
```

#### Aggregation & Accumulation

```python
def compute_cumulative(df, col, label=None):
    """Running cumulative sum."""
    label = label or f"{col}_cumulative"
    df[label] = df[col].cumsum()
    return df

def compute_rolling_sum(
    df, col, window_days, label=None, min_observations=None
):
    """Sum over an actual calendar-day window (e.g., 365-day revenue)."""
    label = label or f"{window_days}_day_sum_{col}"
    series = _calendar_series(df, col)
    df[label] = _calendar_window(
        series, window_days, min_observations
    ).sum()
    return df

def compute_expanding_mean(df, col, label=None):
    """Expanding mean — all-time average up to each point."""
    label = label or f"{col}_expanding_mean"
    df[label] = df[col].expanding().mean()
    return df
```

#### Volatility & Dispersion

```python
import numpy as np

def compute_rolling_std(
    df, col, window_days, label=None, min_observations=None
):
    """Standard deviation over an actual calendar-day window."""
    label = label or f"{window_days}_day_std_{col}"
    series = _calendar_series(df, col)
    df[label] = _calendar_window(
        series, window_days, min_observations
    ).std()
    return df


def compute_annualized_volatility(
    df, col, window_days, label=None, min_observations=None
):
    """Annualized volatility from a strictly daily series."""
    label = label or f"{window_days}_day_vol_{col}"
    series = _calendar_series(df, col).dropna()
    day_gaps = series.index.to_series().diff().dropna()
    if not day_gaps.eq(pd.Timedelta(days=1)).all():
        raise ValueError(
            "annualized daily volatility requires one observation per calendar day; "
            "resample explicitly before calling"
        )
    daily_returns = series.pct_change(fill_method=None)
    df[label] = _calendar_window(
        daily_returns, window_days, min_observations
    ).std() * np.sqrt(365)
    return df


def compute_z_score(df, col, window_days, label=None, min_observations=None):
    """Z-score against an actual calendar-day window."""
    label = label or f"{col}_zscore_{window_days}d"
    series = _calendar_series(df, col)
    window = _calendar_window(series, window_days, min_observations)
    rolling_mean = window.mean()
    rolling_std = window.std()
    df[label] = (df[col] - rolling_mean) / rolling_std
    return df


def compute_percentile_rank(
    df, col, window_days, label=None, min_observations=None
):
    """Percentile rank (0–100) within an actual calendar-day window."""
    label = label or f"{col}_pctrank_{window_days}d"
    series = _calendar_series(df, col)
    df[label] = _calendar_window(
        series, window_days, min_observations
    ).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1] * 100, raw=False
    )
    return df
```

#### Correlation & Comparison

```python
def compute_rolling_correlation(
    df, col_a, col_b, window_days, label=None, min_observations=None
):
    """Correlation over an actual calendar-day window."""
    label = label or f"corr_{col_a}_{col_b}_{window_days}d"
    series_a = _calendar_series(df, col_a)
    series_b = _calendar_series(df, col_b)
    df[label] = _calendar_window(
        series_a, window_days, min_observations
    ).corr(series_b)
    return df

def compute_normalized(df, col, label=None):
    """Normalize to 0–1 range (min-max scaling) for cross-metric comparison."""
    label = label or f"{col}_normalized"
    values = df[col].dropna()
    if values.empty:
        raise ValueError(f"{col} contains no values to normalize")
    col_min = values.min()
    col_max = values.max()
    if col_min == col_max:
        raise ValueError(f"{col} is constant and has no normalization range")
    df[label] = (df[col] - col_min) / (col_max - col_min)
    return df

def compute_indexed(df, col, base_date=None, label=None):
    """Index to 100 at a base date (or first value) for relative comparison."""
    label = label or f"{col}_indexed"
    values = df[col].dropna()
    if values.empty:
        raise ValueError(f"{col} contains no values to index")
    if base_date is not None:
        target = pd.Timestamp(base_date)
        if isinstance(df.index, pd.DatetimeIndex):
            if df.index.tz is not None and target.tzinfo is None:
                target = target.tz_localize(df.index.tz)
            elif df.index.tz is None and target.tzinfo is not None:
                target = target.tz_convert("UTC").tz_localize(None)
        matches = df.loc[df.index == target, col].dropna()
        if len(matches) != 1:
            raise ValueError("base_date must identify exactly one non-missing observation")
        base_val = matches.iloc[0]
    else:
        base_val = values.iloc[0]
    if base_val == 0:
        raise ZeroDivisionError("indexed series requires a nonzero base value")
    df[label] = (df[col] / base_val) * 100
    return df
```

#### Period Returns & Performance

```python
def compute_ytd_return(df, col, max_start_lag="3D"):
    """Year-to-date return as %, or None when the year-start value is unavailable."""
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("period returns require a DatetimeIndex")

    series = df[col].dropna().sort_index()
    if series.empty:
        return None

    current_time = series.index[-1]
    year_start = pd.Timestamp(
        year=current_time.year, month=1, day=1, tz=current_time.tz
    )
    year_values = series.loc[series.index >= year_start]
    if year_values.empty:
        return None

    first_time = year_values.index[0]
    if first_time - year_start > pd.Timedelta(max_start_lag):
        return None

    first_value = year_values.iloc[0]
    current_value = series.iloc[-1]
    if first_value == 0:
        return None
    return (current_value / first_value - 1) * 100


def compute_period_returns(df, col, max_staleness="3D"):
    """Compute calendar-period returns from the most recent valid value."""
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("period returns require a DatetimeIndex")

    series = df[col].dropna().sort_index()
    if series.empty:
        return {}

    current_time = series.index[-1]
    current_value = series.iloc[-1]
    tolerance = pd.Timedelta(max_staleness)
    returns = {}

    for label, days in [("7d", 7), ("30d", 30), ("90d", 90), ("365d", 365)]:
        target_time = current_time - pd.Timedelta(days=days)
        eligible = series.loc[series.index <= target_time]
        if eligible.empty:
            continue

        past_time = eligible.index[-1]
        if target_time - past_time > tolerance:
            continue

        past_value = eligible.iloc[-1]
        if past_value != 0:
            returns[label] = (current_value / past_value - 1) * 100

    ytd_return = compute_ytd_return(df, col, max_start_lag=max_staleness)
    if ytd_return is not None:
        returns["YTD"] = ytd_return
    return returns
```

### 4.3 Standard Data Cleanup

```python
def clean_data(df, fill_columns=None, fill_limit=None):
    """
    Sort time-series data without silently replacing missing observations.

    Forward filling is opt-in and must name the columns whose methodology
    permits carrying a prior value forward.
    """
    cleaned = df.copy().sort_index()

    if fill_columns:
        if fill_limit is None or fill_limit < 1:
            raise ValueError("fill_limit must be a positive integer when filling")

        missing_columns = [col for col in fill_columns if col not in cleaned.columns]
        if missing_columns:
            raise KeyError(f"unknown fill columns: {missing_columns}")

        cleaned.loc[:, fill_columns] = cleaned[fill_columns].ffill(limit=fill_limit)

    return cleaned
```
