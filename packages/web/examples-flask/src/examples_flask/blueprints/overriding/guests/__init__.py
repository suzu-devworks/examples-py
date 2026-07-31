from flask import Blueprint, render_template

bp = Blueprint(
    "guests",
    __name__,
    static_folder="static",
    static_url_path="/static/guests",
    template_folder="templates",
)


@bp.route("/")
def index() -> str:
    return render_template("guests/index.html")
