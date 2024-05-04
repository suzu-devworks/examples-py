"""A Minimal Application.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._01_hello run --debug
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
