"""CLI for ML Baseline System"""

import sys
import typer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
    
from make_sample_data import make_sample_feature_table

app = typer.Typer()


@app.command("make_sample_data")
def make_sample_data(n_users: int = typer.Option(50, help="Number of users to generate.")):
    """write a small demo frearures table ro data/processed/"""
    path = make_sample_feature_table(n_users=n_users)
    typer.echo(f"Sample data saved to: {path}")



@app.command()
def train():
    pass


if __name__ == "__main__":
    app()
