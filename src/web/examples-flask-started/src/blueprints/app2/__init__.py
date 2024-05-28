from typing import NoReturn

from flask import Blueprint, render_template

bp = Blueprint("app2", __name__, static_folder="static", template_folder="templates", url_prefix="/app2")


@bp.route("/")
def index() -> str | NoReturn:
    return render_template("index-app2.html")


@bp.route("/about")
def about() -> str | NoReturn:
    return render_template("about-app2.html")


@bp.route("/hello")
def hello() -> str | NoReturn:
    return render_template("app2/hello.html")
