"""
Rich Text Template with Style Configuration
============================================
A structured template for building styled terminal output using the `rich` library.
"""

import logging

from rich import box
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
from rich.style import Style
from rich.table import Table
from rich.theme import Theme

# ─────────────────────────────────────────────
# STYLE CONFIGURATION
# ─────────────────────────────────────────────

STYLES = {
    # Semantic styles
    "app.title": Style(color="bright_cyan", bold=True),
    "app.subtitle": Style(color="cyan", italic=True),
    "app.header": Style(color="bright_white", bold=True, underline=True),
    # Status styles
    "status.success": Style(color="bright_green", bold=True),
    "status.warning": Style(color="bright_yellow", bold=True),
    "status.error": Style(color="bright_red", bold=True),
    "status.info": Style(color="bright_blue", bold=True),
    "status.muted": Style(color="grey50", italic=True),
    # Data styles
    "data.key": Style(color="bright_magenta"),
    "data.value": Style(color="white"),
    "data.highlight": Style(color="bright_yellow", bold=True),
    "data.code": Style(color="green", bgcolor="grey7"),
    # Border / panel styles
    "panel.default": Style(color="bright_cyan"),
    "panel.warning": Style(color="bright_yellow"),
    "panel.error": Style(color="bright_red"),
    # Text styles
    "text.bold": Style(bold=True),
    "text.italic": Style(italic=True),
    "text.dim": Style(dim=True),
    "text.strike": Style(strike=True),
    "text.link": Style(color="bright_blue", underline=True),
}

THEME = Theme({k: str(v) for k, v in STYLES.items()})


# ─────────────────────────────────────────────
# CONSOLE SETUP
# ─────────────────────────────────────────────

console = Console(
    theme=THEME,
    highlight=True,  # Automatic syntax highlighting
    markup=True,  # Enable Rich markup tags
    emoji=True,  # Enable emoji rendering
    record=False,  # Set True to capture output
    width=100,  # Fixed width (or omit for auto)
)


# ─────────────────────────────────────────────
# LOGGING SETUP (Rich handler)
# ─────────────────────────────────────────────

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(
            console=console,
            rich_tracebacks=True,
            markup=True,
            show_path=True,
        )
    ],
)
log = logging.getLogger("app")


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────


def print_title(title: str, subtitle: str = "") -> None:
    """Render a prominent application title block."""
    console.print()
    console.print(f"[app.title]  {title}  [/app.title]", justify="center")
    if subtitle:
        console.print(f"[app.subtitle]{subtitle}[/app.subtitle]", justify="center")
    console.print(Rule(style="bright_cyan"))


def print_section(label: str) -> None:
    """Render a section divider with a label."""
    console.print(Rule(f"[app.header]{label}[/app.header]", style="grey50"))


def print_status(message: str, level: str = "info") -> None:
    """
    Print a status line with a prefix icon.
    level: 'success' | 'warning' | 'error' | 'info' | 'muted'
    """
    icons = {
        "success": ":white_check_mark:",
        "warning": ":warning:",
        "error": ":cross_mark:",
        "info": ":information:",
        "muted": ":speech_balloon:",
    }
    icon = icons.get(level, ":information:")
    console.print(f"{icon}  [status.{level}]{message}[/status.{level}]")


def print_key_value(data: dict, title: str = "") -> None:
    """Render a dictionary as an aligned key-value table."""
    table = Table(
        show_header=bool(title),
        header_style="app.header",
        box=box.SIMPLE_HEAVY,
        border_style="grey30",
        expand=False,
    )
    if title:
        table.title = f"[app.header]{title}[/app.header]"
    table.add_column("Key", style="data.key", no_wrap=True)
    table.add_column("Value", style="data.value", no_wrap=False)

    for key, value in data.items():
        table.add_row(str(key), str(value))

    console.print(table)


def print_panel(
    content: str,
    title: str = "",
    level: str = "default",
    expand: bool = False,
) -> None:
    """Render content inside a styled panel box."""
    border_style = f"panel.{level}"
    console.print(
        Panel(
            content,
            title=f"[app.header]{title}[/app.header]" if title else "",
            border_style=border_style,
            expand=expand,
            padding=(1, 2),
        )
    )


def print_code(snippet: str, language: str = "python") -> None:
    """Render a syntax-highlighted code block."""
    from rich.syntax import Syntax

    syntax = Syntax(snippet, language, theme="monokai", line_numbers=True)
    console.print(syntax)


def run_with_progress(tasks: list[dict]) -> None:
    """
    Run a list of tasks with a progress bar.

    tasks: list of {"name": str, "steps": int, "fn": callable}
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
        transient=True,
    ) as progress:
        for task_cfg in tasks:
            task_id = progress.add_task(
                f"[status.info]{task_cfg['name']}[/status.info]",
                total=task_cfg["steps"],
            )
            task_cfg["fn"](progress, task_id)


# ─────────────────────────────────────────────
# DEMO / ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    print_title("My Rich App", subtitle="Terminal UI with styled output")

    print_section("Status Messages")
    print_status("Operation completed successfully.", level="success")
    print_status("Disk usage above 80%.", level="warning")
    print_status("Connection refused on port 5432.", level="error")
    print_status("Listening on http://localhost:8000", level="info")
    print_status("Debug mode is active.", level="muted")

    print_section("Key / Value Data")
    print_key_value(
        {
            "Environment": "production",
            "Version": "3.2.1",
            "Database": "postgres://localhost:5432/mydb",
            "Workers": "4",
            "Debug": "False",
        },
        title="Configuration",
    )

    print_section("Panels")
    print_panel("Everything is running smoothly.", title="System OK", level="default")
    print_panel("Certificate expires in 7 days.", title="Warning", level="warning")
    print_panel("Failed to reach upstream API.", title="Error", level="error")

    print_section("Code Snippet")
    print_code(
        'def greet(name: str) -> str:\n    return f"Hello, {name}!"\n\nprint(greet("Rich"))',
        language="python",
    )

    print_section("Logging")
    log.debug("This is a [bold]debug[/bold] message.")
    log.info("Application started.")
    log.warning("Something looks off.")
    log.error("An error occurred.")

    print_section("Progress")

    import time

    def fake_task(progress, task_id):
        for _ in range(10):
            time.sleep(0.05)
            progress.advance(task_id)

    run_with_progress(
        [
            {"name": "Loading config", "steps": 10, "fn": fake_task},
            {"name": "Connecting to DB", "steps": 10, "fn": fake_task},
            {"name": "Syncing data", "steps": 10, "fn": fake_task},
        ]
    )

    print_status("All tasks complete!", level="success")
    console.print()


if __name__ == "__main__":
    main()
