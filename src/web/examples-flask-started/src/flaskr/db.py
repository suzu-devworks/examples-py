import datetime
import sqlite3
from typing import Any

import click
from flask import Flask, current_app, g


def get_db() -> sqlite3.Connection | Any:
    if "db" not in g:
        # spell-checker:words PARSE_DECLTYPES
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e: Any | None = None) -> None:
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()

    with current_app.open_resource("schema.sql", "r") as f:
        data = f.read()
        script = data.encode("utf-8") if isinstance(data, bytes) else str(data)
        # spell-checker:words executescript
        db.executescript(script)


@click.command("init-db")
def init_db_command() -> None:
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app: Flask) -> None:
    # spell-checker:words teardown_appcontext
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def convert_datetime(val: bytes) -> datetime.datetime:
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())


sqlite3.register_converter("timestamp", convert_datetime)
