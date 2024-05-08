"""Rendering Templates.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._06_rendering_templates run --debug
    ```

    Request from client:
    ```shell
    curl -v http://localhost:5000/hello/
    curl -v http://localhost:5000/hello/python
    ```
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name: str | None = None) -> str:
    return render_template("hello.html", name=name)
