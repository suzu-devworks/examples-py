"""URL Building.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#url-building

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._04_routing_url_building run --debug
    ```

    Request from client:
    ```shell
    python src/quickstart/_04_routing_url_building.py
    ```
    ```console
    /
    /login
    /login?next=/
    /user/John%20Doe
    ```
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "index"


@app.route("/login")
def login() -> str:
    return "login"


@app.route("/user/<username>")
def profile(username: str) -> str:
    return f"{username}'s profile"


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("index"))
        print(url_for("login"))
        print(url_for("login", next="/"))
        print(url_for("profile", username="John Doe"))
