from flask import Blueprint, render_template

bp = Blueprint(
    "admin",
    __name__,
    static_folder="static",
    static_url_path="/static/admin",
    template_folder="templates",
)


@bp.route("/")
def index() -> str:
    return render_template("admin/index.html")
