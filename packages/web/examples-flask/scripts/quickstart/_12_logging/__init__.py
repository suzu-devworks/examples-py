"""Logging.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#logging

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_12_logging run --debug
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```

    outputted to the server console:

    ```console
    [2024-12-29 06:19:38,950] DEBUG in __init__: A value for debugging
    [2024-12-29 06:19:38,950] WARNING in __init__: A warning occurred (42 apples)
    [2024-12-29 06:19:38,950] ERROR in __init__: An error occurred
    ```
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    app.logger.debug("A value for debugging")
    app.logger.warning("A warning occurred (%d apples)", 42)
    app.logger.error("An error occurred")
    return "OK"
