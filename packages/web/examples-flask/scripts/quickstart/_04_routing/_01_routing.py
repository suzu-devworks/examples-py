"""Routing.

Use the route() decorator to bind a function to a URL.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#routing

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_04_routing/_01_routing run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    curl -v http://localhost:5000/hello
    ```

"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Index Page"


@app.route("/hello")
def hello() -> str:
    return "Hello, World"
