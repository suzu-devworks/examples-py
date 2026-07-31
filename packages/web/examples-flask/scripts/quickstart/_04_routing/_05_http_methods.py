"""HTTP Methods - Routing.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#http-methods

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_04_routing/_05_http_methods run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/login
    curl -v http://localhost:5000/login -X POST
    ```

    If GET is present, Flask will automatically add support for the HEAD and OPTIONS methods.

    ```shell
    curl -v http://localhost:5000/login -I
    # > HTTP/1.1 200 OK

    curl -v http://localhost:5000/login -X OPTIONS
    # > HTTP/1.1 200 OK
    ```
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """This is useful when each part uses common data."""
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()


@app.get("/login2")
def login_get() -> str:
    return show_the_login_form()


@app.post("/login2")
def login_post() -> str:
    return do_the_login()


def show_the_login_form() -> str:
    return "Show the login form."


def do_the_login() -> str:
    return "Accept login."
