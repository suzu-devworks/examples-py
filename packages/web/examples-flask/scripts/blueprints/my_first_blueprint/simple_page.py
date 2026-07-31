from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

simple_page = Blueprint("simple_page", __name__, template_folder="templates")


@simple_page.route("/", defaults={"page": "index"})
@simple_page.route("/<page>")
def show(page: str) -> str:
    try:
        return render_template(f"pages/{page}.html")
    except TemplateNotFound:
        abort(404)
