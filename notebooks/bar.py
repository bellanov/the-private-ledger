import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np

    from notebooks.domain.environment import registry

    return mo, np, plt, registry


@app.cell
def _(registry):
    # Define Global Variables
    # Variables are parsed automatically from pre-defined .env files
    ENV = registry.get_service(".env").get_config()
    return (ENV,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Environment Values

    _Environment Values_ can be accessed via the `ENV` dictionary.
    """)
    return


@app.cell
def _(ENV):
    ENV
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grouped bar chart with labels
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#grouped-bar-chart-with-labels
    """)
    return


@app.cell
def _(np, plt):
    # data from https://allisonhorst.github.io/palmerpenguins/
    species = ("Adelie", "Chinstrap", "Gentoo")
    penguin_means = {
        "Bill Depth": (18.35, 18.43, 14.98),
        "Bill Length": (38.79, 48.83, 47.50),
        "Flipper Length": (189.95, 195.82, 217.19),
    }

    x = np.arange(len(species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout="constrained")

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Length (mm)")
    ax.set_title("Penguin attributes by species")
    ax.set_xticks(x + width, species)
    ax.legend(loc="upper left", ncols=3)
    ax.set_ylim(0, 250)

    plt.show()
    return


if __name__ == "__main__":
    app.run()
