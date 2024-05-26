from typing import NoReturn

from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

bp = Blueprint("app1", __name__, template_folder="templates", url_prefix="/app1")


@bp.route("/", defaults={"page": "index"})
@bp.route("/<page>")
def show(page: str) -> str | NoReturn:
    try:
        return render_template(f"pages/{page}.html")
    except TemplateNotFound:
        abort(404, f"pages/{page}.html")
