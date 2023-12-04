import matplotlib.pyplot as plt
import numpy as np


def plot_hist(
    results_pivots: list, percent_25_75: float, average_percentage: float
) -> None:
    """
    Plot the histogram of the repartition of the count values of the list with the average value and the
    25-75 quantiles
    Args:
        results_pivots (list):
        percent_25_75 (float):
        average_percentage (float):

    Returns:
        Plot the result
    """
    plt.figure(figsize=(18, 10))
    plt.hist(np.array(results_pivots), alpha=0.5)

    # Plot the 25-75 region
    plt.axvline(25, c="green", linewidth=2, linestyle="--")
    plt.text(x=25, y=-150, s="25%", c="green")

    plt.axvline(75, c="green", linewidth=2, linestyle="--")
    plt.text(x=75, y=-150, s="75%", c="green")

    plt.text(x=45, y=500, s=f"{percent_25_75} %", c="green", fontsize=30)
    plt.axvspan(25, 75, facecolor="green", alpha=0.2)

    # Plot the average
    plt.axvline(average_percentage, c="red", linewidth=3)
    plt.text(x=average_percentage - 1, y=-200, s=f"{average_percentage} %", c="red")

    plt.xlabel("Percentage split (%)", labelpad=30)
    plt.ylabel("count of elements", labelpad=30)
    plt.show()
