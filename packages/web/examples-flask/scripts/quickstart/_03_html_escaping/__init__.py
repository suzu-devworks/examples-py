"""HTML Escaping.

All user-supplied values that appear in the output must be escaped to protect against injection attacks.

> *If a user managed to submit the name <script>alert("bad")</script>*

But in flask, the / in the URL is of course a path separator, so it will be Not Found.
Even if I changed it to %2f, it seems that flask decodes it before parsing it, so the result was the same.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_03_html_escaping run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/%E3%83%91%E3%82%A4%E3%82%BD%E3%83%B3
    # > HTTP/1.1 200 OK

    curl -v http://localhost:5000/%3Cscript%3Ealert%28%22bad%22%29%3C%2fscript%3E
    # > HTTP/1.1 404 NOT FOUND
    ```

"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/<name>")
def hello_by(name: str) -> str:
    return f"Hello, {escape(name)}!"
