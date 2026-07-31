from collections.abc import Mapping
from typing import Any

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .blueprints.overriding import bp as bp_overriding

    app.register_blueprint(bp_overriding, url_prefix="/overriding")

    app.logger.debug(f"Registering Blueprints:\n{app.url_map}")

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
