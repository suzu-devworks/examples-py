"""About Responses.


he return value from a view function is automatically converted into a response object for you.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#about-responses

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_09_about_responses run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/not-found
    # > HTTP/1.1 404 NOT FOUND

    curl -v http://localhost:5000/
    curl -v http://localhost:5000/generator
    curl -v http://localhost:5000/me
    curl -v http://localhost:5000/users
    ```
"""

from collections.abc import Generator
from typing import Any

from flask import Flask, make_response, render_template, url_for
from werkzeug import Response

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error: Exception) -> Response:
    """
    1. If a response object of the correct type is returned it’s directly returned from the view.
    """
    resp = make_response(render_template("error.html"), 404)
    resp.headers["X-Something"] = "A value"
    return resp


@app.route("/")
def use_str() -> str:
    """
    2. If it’s a string, a response object is created with that data and the default parameters.
    """
    return render_template("index.html")


@app.route("/generator")
def use_generator() -> Generator[str]:
    """
    3. If it’s an iterator or generator returning strings or bytes, it is treated as a streaming response.
    """

    def _generator() -> Generator[str]:
        yield "<ul>"
        for i in range(10):
            yield f"<li>Step{i + 1}</li>"
        yield "</ol>"

    return _generator()


"""
4. If it’s a dict or list, a response object is created using jsonify().
"""


class User:
    def __init__(self, username: str, theme: str, image: str) -> None:
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self) -> dict[str, Any]:
        return {
            "username": self.username,
            "theme": self.theme,
            "image": url_for("static", filename=self.image),
        }


def get_current_user() -> User:
    return get_all_users()[0]


def get_all_users() -> list[User]:
    return [
        User("Alice", "system", "system-image"),
        User("Bob", "light", "light-image"),
        User("Carol", "dark", "dark-image"),
    ]


@app.route("/me")
def me_api() -> dict[str, Any]:
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("static", filename=user.image),
    }


@app.route("/users")
def users_api() -> list[dict[str, Any]]:
    users = get_all_users()
    return [user.to_json() for user in users]


"""
5. If a tuple is returned the items in the tuple can provide extra information.
   Such tuples have to be in the form (response, status), (response, headers), or (response, status, headers).
   The status value will override the status code and headers can be a list or dictionary of additional header values.
"""


@app.route("/error")
def use_tuple() -> tuple[Response, int]:
    resp = make_response("Error", 500)
    return resp, 400  # overwrite http status code


"""
6. If none of that works, Flask will assume the return value
   is a valid WSGI application and convert that into a response object.
"""
