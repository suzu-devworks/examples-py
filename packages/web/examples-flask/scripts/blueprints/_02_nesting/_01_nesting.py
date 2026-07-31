"""Nesting Blueprints.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#registering-blueprints

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_02_nesting/_01_nesting run
    ```

    Outputted to the server console:

    ```console
    Nesting Blueprints:
     /parent/child/create
    ```
"""

from flask import Blueprint, Flask, url_for


def create_app() -> Flask:
    app = Flask(__name__)

    parent = Blueprint("parent", __name__, url_prefix="/parent")
    child = Blueprint("child", __name__, url_prefix="/child")

    @child.route("/create")
    def create() -> str:
        return "create!"

    parent.register_blueprint(child)
    app.register_blueprint(parent)

    with app.test_request_context():
        print("Nesting Blueprints:\n", url_for("parent.child.create"))

    return app
