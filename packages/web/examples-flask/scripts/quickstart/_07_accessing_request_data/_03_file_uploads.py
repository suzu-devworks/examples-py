"""File Uploads - Accessing Request Data.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#file-uploads

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_07_accessing_request_data/_03_file_uploads run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/upload -X POST -F the_file=@./README.md
    ```
"""

import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from werkzeug import Response
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/tmp"


@app.route("/upload", methods=["GET", "POST"])
def upload_file() -> Response | str:
    error = None
    if request.method == "POST":
        file = request.files["the_file"]
        # file.save("/var/www/uploads/uploaded_file.txt")
        # file.save(f"/var/www/uploads/{secure_filename(str(file.filename)}")
        if file.filename == "":
            error = "No selected file"
            # flash("No file part")
            # return redirect(request.url)

        else:
            file_name = secure_filename(file.filename) if file.filename is not None else ""
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
            return redirect(url_for("download_file", name=file_name))

    return render_template("upload.html", error=error)


@app.route("/download/<name>")
def download_file(name: str) -> Response:
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)
