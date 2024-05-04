"""Static Files.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#static-files

Examples:
    Request from client:
    ```shell
    python src/quickstart/_05_static_files.py
    ```
    ```console
    /static/style.css
    ```
"""

from flask import Flask, url_for

app = Flask(__name__)


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("static", filename="style.css"))
