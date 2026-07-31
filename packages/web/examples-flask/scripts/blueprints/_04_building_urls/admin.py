from flask import Blueprint, url_for

admin = Blueprint("admin", __name__)


@admin.route("/")
def index() -> str:
    return f"""<ul>
            <li>This is (admin): {url_for("admin.index")}</li>
            <li>This is (dot): {url_for(".index")}</li>
        </ul>
        """
