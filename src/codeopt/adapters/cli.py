"""Local CLI adapter; commands arrive in Phase 1."""

import typer

app = typer.Typer(
    help="Verify and benchmark Python optimization candidates.",
    invoke_without_command=True,
)


@app.callback()
def main() -> None:
    """Local command-line entry point for the future optimization pipeline."""
