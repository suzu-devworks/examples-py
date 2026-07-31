from flask import Blueprint, render_template

from .admin import bp as admin
from .guests import bp as guests
from .users import bp as users

bp = Blueprint(
    "overriding",
    __name__,
    static_folder="static",
    static_url_path="/static/overriding",
    template_folder="templates",
)

bp.register_blueprint(admin, url_prefix="/admin")
bp.register_blueprint(users, url_prefix="/users")
bp.register_blueprint(guests, url_prefix="/guest")


@bp.route("/")
def index() -> str:
    return render_template("overriding/index.html")
