import os

from flask import Blueprint, Response, current_app, render_template, request

from .utility import format_range_header, parse_range_header
from .video_chunks import get_chunk

bp = Blueprint("video_chunks", __name__, static_folder="static", template_folder="templates")
bp.add_url_rule("/", endpoint="index")


source_path = os.getenv("CHUNK_SRC", default="/workspaces/examples-py/temp/input.mp4")
chunk_size = int(os.getenv("CHUNK_SIZE", str(65535 * 2)))


@bp.route("/")
def index() -> str:
    return render_template("video/chunks/index.html")


@bp.after_request
def after_request(response: Response) -> Response:
    response.headers.add("Accept-Ranges", "bytes")
    return response


@bp.route("/video_feed")
def video_feed() -> Response:
    logger = current_app.logger

    range_header = request.headers.get("Range", None)
    logger.debug(f"chunks - Range: {range_header}")

    byte1, byte2 = parse_range_header(range_header)
    chunk, start, length, file_size = get_chunk(source_path, byte1, byte2, chunk_size)

    resp = Response(chunk, 206, mimetype="video/mp4", content_type="video/mp4", direct_passthrough=True)
    resp.headers.add("Content-Range", format_range_header(start, length, file_size))
    logger.debug(f"chunks - Content-Range: {format_range_header(start, length, file_size)}")

    return resp
