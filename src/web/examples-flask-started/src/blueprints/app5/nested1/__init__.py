from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint("nested1", __name__, static_folder="static", template_folder="templates")


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("app5/nested1/index.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("app5/nested1/about.html")
