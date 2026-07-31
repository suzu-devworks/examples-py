from flask import Blueprint, abort, current_app, render_template
from werkzeug.exceptions import HTTPException, NotFound

simple_page = Blueprint("simple_page", __name__, template_folder="templates")


@simple_page.route("/raise")
def raise_error() -> str:
    raise NotFound


@simple_page.route("/abort")
def do_abort() -> str:
    abort(404)


@simple_page.route("/returns")
def returns_not_found() -> tuple[str, int]:
    """It is returned directly without being processed by the handler."""
    return '"Not Found" was returned', 404


@simple_page.errorhandler(404)
def page_not_found(ex: HTTPException) -> str:
    current_app.logger.debug("simple_page handler was called.")
    return render_template("pages/404.html", error=ex)
