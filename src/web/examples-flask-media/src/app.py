from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    from examples.webcam.mjpeg import blueprint as webcam_mjpeg

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # add blueprints
    app.register_blueprint(webcam_mjpeg, url_prefix="/webcam/mjpeg")

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
