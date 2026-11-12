import matplotlib.pyplot as plt


# same colors as my hw2 plot
COLORS = {"W": "#2e9bbd", "L": "#8d4a9c"}
LABELS = {"W": "Won", "L": "Lost"}


def plot_age_gap(matches):
    """Scatter plot of age gap vs. the player's age, like the hw2 plot."""
    player = matches["player"][0]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.axhline(0, color="gray", lw=1)
    for result, g in matches.groupby("result"):
        ax.scatter(g["age_player"], g["age_gap"], color=COLORS[result],
                   label=LABELS[result], s=12, alpha=0.6)
    ax.set_xlabel(f"{player}'s age at the match")
    ax.set_ylabel(f"Age difference ({player} - opponent)")
    ax.set_title(f"{player} and the age of the opponents")
    ax.legend()
    return fig
