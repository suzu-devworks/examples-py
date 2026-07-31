from logging import DEBUG, basicConfig
from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    from .blueprints.video.segments import blueprint as bp_video_segments
    from .blueprints.webcam.hls import blueprint as bp_webcam_hls
    from .blueprints.webcam.mjpeg import blueprint as bp_webcam_mjpeg

    basicConfig(level=DEBUG)

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # add blueprints
    app.register_blueprint(bp_webcam_mjpeg, url_prefix="/webcam/mjpeg")
    app.register_blueprint(bp_webcam_hls, url_prefix="/webcam/hls")
    app.register_blueprint(bp_video_segments, url_prefix="/video/segments")

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
