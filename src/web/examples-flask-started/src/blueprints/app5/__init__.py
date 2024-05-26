from flask import Blueprint

from .nested1 import bp as nested1

bp = Blueprint("app5", __name__, static_folder="static", template_folder="templates")
bp.register_blueprint(nested1, url_prefix="/nested1")
