from flask import Blueprint, render_template

admin = Blueprint(
    "admin",
    __name__,
    static_folder="static",
    # I include an argument to the static_url_path parameter to ensure that
    # the Blueprint's static path doesn't conflict with the static path of the main app.
    static_url_path="/static/admin",
    template_folder="templates",
)


@admin.route("/")
def index() -> str:
    return render_template("admin/index.html")
