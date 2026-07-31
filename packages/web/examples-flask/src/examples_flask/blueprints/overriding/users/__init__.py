from flask import Blueprint, render_template

bp = Blueprint(
    "users",
    __name__,
    static_folder="static",
    static_url_path="/static/users",
    template_folder="templates",
)


@bp.route("/")
def index() -> str:
    return render_template("users/index.html")
