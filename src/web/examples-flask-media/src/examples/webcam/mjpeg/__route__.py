import os
import time
from typing import Generator

from flask import Blueprint, Response, current_app, render_template

from .video_camera import VideoCamera

bp = Blueprint("webcam_mjpeg", __name__, template_folder="templates")
bp.add_url_rule("/", endpoint="index")

# export MJPEG_SRC="/workspaces/examples-py/temp/input.mp4"
# export MJPEG_SRC="srt://0.0.0.0:5501?mode=listener"
source_url = os.getenv("MJPEG_SRC", default="udp://0.0.0.0:5501")
mimetype_multipart = "multipart/x-mixed-replace; boundary=frame"


def gen(camera: VideoCamera) -> Generator[bytes, None, None]:
    app = current_app
    while True:
        frame = camera.get_frame()
        if frame is None:
            app.logger.debug("frame is none")
        else:
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

        # This is also a cause of delay
        time.sleep((1 / 30) / 3)


@bp.route("/")
def index() -> str:
    return render_template("webcam/mjpeg/index.html")


@bp.route("/video_feed")
def video_feed() -> Response:
    camera = VideoCamera(source_url)
    return Response(gen(camera), mimetype=mimetype_multipart)
