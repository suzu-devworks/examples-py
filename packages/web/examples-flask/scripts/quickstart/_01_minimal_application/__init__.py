"""A Minimal Application.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_01_minimal_application run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"
