"""Debug Mode.

When you enable debug mode:

- The server will automatically reload if any code changes,
- The browser will display an interactive debugger if an error occurs during a request.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_02_debug_mode run --debug
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
    raise ValueError("An error occurred.")
