"""Cookies - Accessing Request Data.

To access cookies you can use the cookies attribute.
To set cookies you can use the set_cookie method of response objects.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#cookies

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_07_accessing_request_data/_04_cookies run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/ -b "username=Flask"
    ```
"""

from flask import Flask, Response, make_response, render_template, request

app = Flask(__name__)


@app.route("/")
def index() -> Response:
    username = request.cookies.get("username")
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    resp = make_response(render_template("hello.html", name=username))
    resp.set_cookie("username", "the username", secure=True, httponly=True, samesite="Strict")
    return resp
