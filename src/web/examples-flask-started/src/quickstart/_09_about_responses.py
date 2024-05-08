"""About Responses.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._09_about_responses run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/not-found     # HTTP/1.1 404 NOT FOUND
    curl -v http://localhost:5000/me
    curl -v http://localhost:5000/users
    ```
"""

from typing import Any

from flask import Flask, make_response, render_template, url_for
from werkzeug import Response

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error: Exception) -> Response:
    resp = make_response(render_template("error.html"), 404)
    resp.headers["X-Something"] = "A value"
    return resp


"""
APIs with JSON
"""


class User(object):
    def __init__(self, username: str, theme: str, image: str):
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
