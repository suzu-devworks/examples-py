from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint("app4", __name__)


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("app4/index.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("app4/about.html")
