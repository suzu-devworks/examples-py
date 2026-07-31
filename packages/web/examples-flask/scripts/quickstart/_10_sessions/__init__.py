"""Sessions.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#sessions

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_10_sessions run
    ```

    When you are not logged in from client:

    ```shell
    curl -v http://localhost:5000/
    # > HTTP/1.1 401 UNAUTHORIZED
    ```

    Show login form:

    ```shell
    curl -v http://localhost:5000/login
    # > HTTP/1.1 200 OK
    ```

    Log in with your username and password:

    ```shell
    curl -v http://localhost:5000/login -X POST --data "username={your name}" -d "password={password}"
    # > HTTP/1.1 302 FOUND
    ```

    Resend using the session key. This is done automatically by the browser.

    ```shell
    curl -v http://localhost:5000/ -b "session={Cookie value included in login response};"
    # > HTTP/1.1 200 OK
    ```

    Log out:

    ```shell
    curl -v http://localhost:5000/logout -b "session={Cookie value included in login response};"
    # > HTTP/1.1 302 FOUND
    ```

    Session rejected after logout:

    ```shell
    curl -v http://localhost:5000/ -b "session={Cookie value included in login response};"
    # > HTTP/1.1 401 UNAUTHORIZED
    ```
"""  # noqa E501

import secrets

from flask import Flask, redirect, request, session, url_for
from werkzeug import Response

app = Flask(__name__)


def create_fake_secret_key() -> bytes:
    return secrets.token_hex().encode()


# Set the secret key to some random bytes. Keep this really secret!
# How to generate good secret keys:
# > python -c 'import secrets; print(secrets.token_hex())'
# app.secret_key = b"******"
app.secret_key = create_fake_secret_key()


@app.route("/")
def index() -> str | tuple[str, int]:
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in", 401


@app.route("/login", methods=["GET", "POST"])
def login() -> Response | str:
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@app.route("/logout")
def logout() -> Response:
    # remove the username from the session if it's there
    # Not removed?
    session.pop("username", None)
    return redirect(url_for("index"))
