import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help="adds an item")
def add(task : str, category : str):
    typer.echo(f"adding {task}, {category}")

@app.command(short_help="delete an item")
def delete(position : int):
    tyepr.echo(f"deleting {position}")

@app.command(short_help="update an item")
def update(position : int, task : str = None, category : str = None):
    typer.echo(f"updating {position}")


if __name__ == "__main__":
    app()
