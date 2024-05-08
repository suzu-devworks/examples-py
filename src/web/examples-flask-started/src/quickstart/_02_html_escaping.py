"""HTML Escaping.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#html-escaping

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._02_html_escaping run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/%E3%83%91%E3%82%A4%E3%82%BD%E3%83%B3
    ```
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/<name>")
def hello_by(name: str) -> str:
    return f"Hello, {escape(name)}!"
