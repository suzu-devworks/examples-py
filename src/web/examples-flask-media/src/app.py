from logging import DEBUG, basicConfig
from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    from examples.video.chunks import blueprint as video_chunks
    from examples.webcam.hls import blueprint as webcam_hls
    from examples.webcam.mjpeg import blueprint as webcam_mjpeg

    basicConfig(level=DEBUG)

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # add blueprints
    app.register_blueprint(webcam_mjpeg, url_prefix="/webcam/mjpeg")
    app.register_blueprint(webcam_hls, url_prefix="/webcam/hls")
    app.register_blueprint(video_chunks, url_prefix="/video/chunks")

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
