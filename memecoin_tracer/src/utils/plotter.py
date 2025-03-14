import matplotlib.pyplot as plt

def plot_trend(coin, hourly_counts):
    """Plot trend graph for coin mentions"""
    plt.plot(range(24), hourly_counts, label=coin)
    plt.xlabel("Hour of Day")
    plt.ylabel("Mention Count")
    plt.title(f"Trend Analysis for {coin}")
    plt.legend()
    plt.show()