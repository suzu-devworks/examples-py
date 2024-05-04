"""Routing.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._03_routing run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/
    curl -v http://localhost:5000/hello

    curl -v http://localhost:5000/user/suzuki
    curl -v http://localhost:5000/post/101
    curl -v http://localhost:5000/path/foo/bar/baz

    curl -v http://localhost:5000/projects/         # HTTP/1.1 200 OK
    curl -v http://localhost:5000/projects          # HTTP/1.1 308 PERMANENT REDIRECT
    curl -v http://localhost:5000/about/            # HTTP/1.1 404 NOT FOUND
    curl -v http://localhost:5000/about             # HTTP/1.1 200 OK

    curl -v http://localhost:5000/login
    curl -v http://localhost:5000/login -X POST
    ```
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Index Page"


@app.route("/hello")
def hello() -> str:
    return "Hello, World"


"""
### Variable Rules
"""


@app.route("/user/<username>")
def show_user_profile(username: str) -> str:
    # show the user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath: str) -> str:
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


"""
Unique URLs/Redirection Behavior
"""


@app.route("/projects/")
def projects() -> str:
    """
    - /projects/  -> OK.
    - /projects   -> redirect /projects/ in browser.
    """
    return "The project page"


@app.route("/about")
def about() -> str:
    """
    - /about    -> OK.
    - /about/   -> 404 “Not Found” error.
    """
    return "The about page"


"""
### URL Building
"""


"""
### HTTP Methods
"""


@app.get("/login")
def login_get() -> str:
    return show_the_login_form()


@app.post("/login")
def login_post() -> str:
    return do_the_login()


def show_the_login_form() -> str:
    return "Show the login form."


def do_the_login() -> str:
    return "Accept login."
