import os
from pathlib import Path

from flask import Blueprint, current_app, render_template, send_from_directory
from flask_cors import CORS
from werkzeug import Response

from .utils import get_video_mimetype

bp = Blueprint("webcam_hls", __name__, static_folder="static", template_folder="templates")
bp.add_url_rule("/", endpoint="index")

CORS(bp, resources={r"*": {"origins": ["*"], "methods": ["GET"]}})

video_dir = os.getenv("HLS_SRC_DIR", default=str(Path.cwd() / "temp"))


@bp.route("/")
def index() -> str:
    return render_template("webcam/hls/index.html")


@bp.route("/video/<string:file_name>")
def stream(file_name: str) -> Response:
    logger = current_app.logger
    mimetype = get_video_mimetype(Path(file_name).suffix)
    logger.info(f"request: {file_name}")
    logger.info(f"mimetype: {mimetype}")
    logger.info(f"video_dir: {video_dir}")

    response = send_from_directory(directory=video_dir, path=file_name, mimetype=mimetype)

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


# @bp.errorhandler(500)
# @bp.errorhandler(404)
# def _handle_api_error(ex: any) -> None:
#     logger = current_app.logger
#     logger.error(ex)
