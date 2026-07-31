"""Templates - Blueprint Resources.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#templates

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_03_resources/_03_templates run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask


def create_app() -> Flask:
    from .admin import admin

    app = Flask(__name__)
    app.register_blueprint(admin)

    return app
