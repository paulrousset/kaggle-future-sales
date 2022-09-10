import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def plot_quantiles(df: pd.DataFrame, var: float, title: str, width: int = 12, height: int = 4,
                   label_size: float = 8.5) -> None:
    """Plotting quantiles for a given variable."""
    quantiles = df[var].quantile([0.01, 0.05, 0.1, 0.25, 0.5, .75, .9, .95, 0.99])

    sns.set_context('paper')
    sns.set_color_codes('muted')
    f, ax = plt.subplots(figsize=(width, height))
    sns.barplot(x=quantiles.values, y=quantiles.index.astype(str),  color='b', edgecolor='w')
    sns.despine(bottom=True)
    ax.bar_label(ax.containers[0], size=label_size, fmt='%1.0f')
    if title:
        plt.title(title)
    plt.show()


def plot_histograms(volume: pd.DataFrame, sales: pd.DataFrame, title1: str, title2: str, share_axis: bool = True,
                    width: int = 15, height: int = 6) -> None:
    """Plotting two histograms (volumes & sales)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width, height))
    if not share_axis:
        fig.subplots_adjust(hspace=.6)
    # Volume Dimension
    volume.plot.bar(ax=ax1)
    ax1.set_title(title1)
    ax1.legend().set_visible(False)
    ax1.set(xlabel=None)
    # Sales Dimension
    if share_axis:
        sales.plot.bar(ax=ax2, sharex=ax1)
    else:
        sales.plot.bar(ax=ax2)
    ax2.set_title(title2)
    ax2.legend().set_visible(False)
    ax2.set(xlabel=None)


def get_quantiles_from_values(df: pd.DataFrame, variable: float, values: [], unit: str) -> None:
    """Print quantiles corresponding to given values."""
    for value in values:
        quantile = stats.percentileofscore(df[variable], value).round(1)
        print("{}% of cases have {} under {}".format(quantile, unit, value))

