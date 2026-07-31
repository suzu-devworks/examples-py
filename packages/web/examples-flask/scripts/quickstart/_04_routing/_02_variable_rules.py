"""Variable Rules - Routing.

You can add variable sections to a URL by marking sections with <variable_name>.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_04_routing/_02_variable_rules run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/user/suzuki
    curl -v http://localhost:5000/post/101
    curl -v http://localhost:5000/path/foo/bar/baz
    ```

"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/user/<username>")
def show_user_profile(username: str) -> str:
    # show the user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    # show the post with the given id, the id is an integer
    return f"Post {escape(post_id)}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath: str) -> str:
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"
