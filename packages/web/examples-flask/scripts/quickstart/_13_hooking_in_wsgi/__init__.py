"""Hooking in WSGI Middleware.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#hooking-in-wsgi-middleware

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_13_hooking_in_wsgi run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)  # type: ignore [method-assign]


@app.route("/")
def index() -> str:
    return "index"
