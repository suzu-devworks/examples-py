"""Nesting Blueprints.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#registering-blueprints

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_02_nesting/_02_subdomain run
    ```

    Outputted to the server console:

    ```console
    Nesting Blueprints:
     http://child.parent.localhost/create
    ```
"""

from flask import Blueprint, Flask, url_for


def create_app() -> Flask:
    app = Flask(__name__)

    parent = Blueprint("parent", __name__, subdomain="parent")
    child = Blueprint("child", __name__, subdomain="child")

    @child.route("/create")
    def create() -> str:
        return "create!"

    parent.register_blueprint(child)
    app.register_blueprint(parent)

    with app.test_request_context():
        print("Nesting Blueprints:\n", url_for("parent.child.create", _external=True))

    return app
