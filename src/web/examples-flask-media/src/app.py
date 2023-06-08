from typing import Any, Mapping

from flask import Flask


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/")
    def hello() -> str:
        return "Hello, World!"

    return app
