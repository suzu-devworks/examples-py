"""Redirects and Errors.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#redirects-and-errors

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._08_redirects_and_errors run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/              # HTTP/1.1 302 FOUND
    curl -v http://localhost:5000/login         # HTTP/1.1 401 UNAUTHORIZED
    curl -v http://localhost:5000/not-found     # HTTP/1.1 404 NOT FOUND
    ```
"""

from flask import Flask, abort, redirect, render_template, url_for
from werkzeug import Response

app = Flask(__name__)


@app.route("/")
def index() -> Response:
    return redirect(url_for("login"))


@app.route("/login")
def login() -> Response:
    abort(401)


@app.errorhandler(404)
def page_not_found(error: Exception) -> tuple[str, int]:
    return render_template("error.html"), 404
