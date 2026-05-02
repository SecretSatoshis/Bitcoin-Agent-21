# Data Analysis Guide — Agent 21

> **Purpose:** Standard patterns for data analysis, charting, and visualization. Consult this guide when creating charts or performing data analysis. Follow these patterns for consistent, publication-quality output across any data source.

---

## 1. Data Workflow

Every data analysis task follows the same sequence.

1. **Identify data** — Consult `agent21_knowledge_index.md` to determine what data is needed and where it lives (BRK API, uploaded knowledge, curated data sets, user-provided data, etc.).
2. **Fetch data** — Retrieve via the appropriate Action or source. Get all required data before processing.
3. **Process data** — Parse into a pandas DataFrame. Compute any derived metrics or transformations.
4. **Visualize** — Build the chart using matplotlib following the style standards below.
5. **Analyze** — Provide written interpretation alongside the chart to help the user understand what they're seeing. Lead with the key insight, provide context on what the data shows, and explain why it matters. This analysis is part of the response text, not on the chart itself.

**Critical:** Data retrieval (steps 1–2) and data processing (steps 3–5) are separate steps. Retrieve all data first, then process and visualize.

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
- **Price data defaults to log scale** — Bitcoin price and any price-denominated metric should use log scale (`ax.set_yscale("log")`). This shows proportional moves consistently across all time ranges. Only use linear scale if the user specifically requests it or the time range is very short (< 90 days).

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
    plt.xticks(rotation=45, ha="right")
```

### Legend & Branding

```python
def finalize_chart(ax, data_source=""):
    # Legend at bottom, horizontal
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12),
              ncol=3, frameon=False, fontsize=10)
    # Data source attribution
    if data_source:
        ax.annotate(data_source, xy=(1, -0.18), xycoords="axes fraction",
                    ha="right", fontsize=8, color="#666")
    # Watermark
    ax.text(0.5, 0.5, "SecretSatoshis.com", transform=ax.transAxes,
            fontsize=36, color="gray", alpha=0.15,
            ha="center", va="center")
    plt.tight_layout()
```

---

## 3. Standard Chart Types

### 3.1 Time Series Line Chart

Single or multi-metric line chart over time.

```python
import pandas as pd
import matplotlib.pyplot as plt

def time_series_chart(df, metrics, title, ylabel, log_scale=False, data_source=""):
    """
    Standard time series line chart.

    Args:
        df: DataFrame with DatetimeIndex
        metrics: list of dicts [{"col": "column_name", "label": "Display Name", "color": "#hex"}]
        title: Chart title
        ylabel: Y-axis label
        log_scale: Default True for price data. Use log for values spanning orders of magnitude.
        data_source: Attribution string (e.g., "Data: BRK API")
    """
    fig, ax = setup_chart(title, ylabel)

    for i, m in enumerate(metrics):
        color = m.get("color", CHART_COLORS[i % len(CHART_COLORS)])
        ax.plot(df.index, df[m["col"]], label=m["label"], color=color, linewidth=1.5)

    if log_scale:
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

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2,
               loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=False)

    format_dates(ax1)
    finalize_chart(ax1, data_source=data_source)
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

BRK series endpoints can be consumed as either CSV or JSON depending on the runtime, payload shape, and transport constraints. Use the parser that matches the retrieved format rather than assuming one format is universal.

```python
import pandas as pd
from io import StringIO

def parse_csv_response(csv_text, time_col="timestamp", time_unit="s"):
    """
    Parse a CSV response from BRK API into a DataFrame with DatetimeIndex.
    Use this when the retrieved series payload is CSV text.
    """
    df = pd.read_csv(StringIO(csv_text))

    if time_col in df.columns:
        df[time_col] = pd.to_datetime(df[time_col], unit=time_unit, errors="coerce")
        df.set_index(time_col, inplace=True)

    # Convert numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def parse_time_series(data, time_col="timestamp", time_unit="s"):
    """
    Parse JSON/dict data into a DataFrame with DatetimeIndex.
    Use this for JSON series responses, user-provided data, or other dict/list payloads.
    """
    df = pd.DataFrame(data)

    if time_col in df.columns:
        df[time_col] = pd.to_datetime(df[time_col], unit=time_unit, errors="coerce")
        df.set_index(time_col, inplace=True)

    # Convert numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
```

### 4.2 Common Transformations

#### Moving Averages & Smoothing

```python
def compute_moving_average(df, col, window, label=None):
    """Simple moving average (SMA)."""
    label = label or f"{window}_day_ma_{col}"
    df[label] = df[col].rolling(window=window).mean()
    return df

def compute_ema(df, col, span, label=None):
    """Exponential moving average (EMA) — more weight on recent values."""
    label = label or f"{span}_day_ema_{col}"
    df[label] = df[col].ewm(span=span, adjust=False).mean()
    return df

def compute_rolling_median(df, col, window, label=None):
    """Rolling median — resistant to outliers."""
    label = label or f"{window}_day_median_{col}"
    df[label] = df[col].rolling(window=window).median()
    return df
```

#### Ratios & Relationships

```python
def compute_ratio(df, numerator, denominator, label):
    """Ratio between two columns."""
    df[label] = df[numerator] / df[denominator]
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
def compute_pct_change(df, col, periods=1, label=None):
    """Period-over-period percent change."""
    label = label or f"{col}_pct_change_{periods}d"
    df[label] = df[col].pct_change(periods=periods) * 100
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

def compute_rolling_sum(df, col, window, label=None):
    """Rolling sum over a window (e.g., 365-day total revenue)."""
    label = label or f"{window}_day_sum_{col}"
    df[label] = df[col].rolling(window=window).sum()
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

def compute_rolling_std(df, col, window, label=None):
    """Rolling standard deviation."""
    label = label or f"{window}_day_std_{col}"
    df[label] = df[col].rolling(window=window).std()
    return df

def compute_annualized_volatility(df, col, window, label=None):
    """Annualized volatility from daily returns."""
    label = label or f"{window}_day_vol_{col}"
    daily_returns = df[col].pct_change()
    df[label] = daily_returns.rolling(window=window).std() * np.sqrt(365)
    return df

def compute_z_score(df, col, window, label=None):
    """Z-score — how many std devs from the rolling mean."""
    label = label or f"{col}_zscore_{window}d"
    rolling_mean = df[col].rolling(window=window).mean()
    rolling_std = df[col].rolling(window=window).std()
    df[label] = (df[col] - rolling_mean) / rolling_std
    return df

def compute_percentile_rank(df, col, window, label=None):
    """Rolling percentile rank (0–100) within a window."""
    label = label or f"{col}_pctrank_{window}d"
    df[label] = df[col].rolling(window=window).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1] * 100, raw=False
    )
    return df
```

#### Correlation & Comparison

```python
def compute_rolling_correlation(df, col_a, col_b, window, label=None):
    """Rolling correlation between two series."""
    label = label or f"corr_{col_a}_{col_b}_{window}d"
    df[label] = df[col_a].rolling(window=window).corr(df[col_b])
    return df

def compute_normalized(df, col, label=None):
    """Normalize to 0–1 range (min-max scaling) for cross-metric comparison."""
    label = label or f"{col}_normalized"
    col_min = df[col].min()
    col_max = df[col].max()
    df[label] = (df[col] - col_min) / (col_max - col_min)
    return df

def compute_indexed(df, col, base_date=None, label=None):
    """Index to 100 at a base date (or first value) for relative comparison."""
    label = label or f"{col}_indexed"
    if base_date:
        base_val = df.loc[base_date, col]
    else:
        base_val = df[col].dropna().iloc[0]
    df[label] = (df[col] / base_val) * 100
    return df
```

#### Period Returns & Performance

```python
def compute_ytd_return(df, col):
    """Year-to-date return as %."""
    first_of_year = df[df.index >= f"{df.index[-1].year}-01-01"][col].iloc[0]
    return (df[col].iloc[-1] / first_of_year - 1) * 100

def compute_period_returns(df, col):
    """Compute standard return periods from the most recent value."""
    current = df[col].iloc[-1]
    returns = {}
    for label, days in [("7d", 7), ("30d", 30), ("90d", 90), ("365d", 365)]:
        if len(df) > days:
            past = df[col].iloc[-(days + 1)]
            returns[label] = (current / past - 1) * 100
    returns["YTD"] = compute_ytd_return(df, col)
    return returns
```

### 4.3 Standard Data Cleanup

```python
def clean_data(df):
    """Standard cleanup for time series data."""
    # Drop rows where all metric columns are NaN
    df.dropna(how="all", inplace=True)

    # Sort by date
    df.sort_index(inplace=True)

    # Forward-fill small gaps (weekends, missing days)
    df.ffill(limit=3, inplace=True)

    return df
```
