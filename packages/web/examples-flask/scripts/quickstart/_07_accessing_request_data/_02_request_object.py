"""The Request Object - Accessing Request Data.

The request object used by default in Flask.
Remembers the matched endpoint and view arguments.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_07_accessing_request_data/_02_request_object run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/login
    curl -v http://localhost:5000/login -X POST --data-urlencode "username={your name}" -d "password={password}"
    ```
"""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login() -> str:
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template("login.html", error=error)


def valid_login(username: str, password: str) -> bool:
    return len(username) > 4 and len(password) > 6


def log_the_user_in(username: str) -> str:
    return f"{escape(username)} is login."
