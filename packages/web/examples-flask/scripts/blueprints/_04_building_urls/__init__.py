"""Building URLs.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#building-urls

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_04_building_urls run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask, redirect, url_for
from werkzeug import Response


def create_app() -> Flask:
    from .admin import admin

    app = Flask(__name__)
    app.register_blueprint(admin, url_prefix="/admin")

    # redirect to home.
    @app.route("/")
    def index() -> Response:
        return redirect(url_for("admin.index"))

    return app
