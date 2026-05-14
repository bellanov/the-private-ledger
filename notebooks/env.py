import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo

    from notebooks.domain.environment import registry

    return mo, registry


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


if __name__ == "__main__":
    app.run()
