"""Redirects and Errors.

To redirect a user to another endpoint, use the redirect() function;
to abort a request early with an error code, use the abort() function:

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#redirects-and-errors

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_08_redirects_and_errors run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    # > HTTP/1.1 302 FOUND

    curl -v http://localhost:5000/login
    # > HTTP/1.1 401 UNAUTHORIZED

    curl -v http://localhost:5000/not-found
    # > HTTP/1.1 404 NOT FOUND
    ```
"""

from flask import Flask, abort, redirect, render_template, url_for
from markupsafe import escape
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
    return render_template("error.html", error=escape(error)), 404
