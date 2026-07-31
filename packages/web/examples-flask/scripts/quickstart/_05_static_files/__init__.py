"""Static Files.

Just create a folder called static in your package or next to your module
and it will be available at /static on the application.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#static-files

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_05_static_files run
    ```

    Outputted to the server console:

    ```console
    /static/style.css
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    ```
"""

from flask import Flask, url_for

app = Flask(__name__)

with app.test_request_context():
    print(url_for("static", filename="style.css"))


@app.route("/")
def index() -> str:
    return f"Static Files: {url_for('static', filename='style.css')}"
