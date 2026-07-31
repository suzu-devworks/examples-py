"""Response Encoding.

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/encodings/_01_resource_encoding run --debug
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
    curl -v http://localhost:5000/string
    curl -v http://localhost:5000/string/encode
    curl -v http://localhost:5000/bytes
    curl -v http://localhost:5000/bytes/decode
    ```

"""

from typing import Any

from flask import Flask

app = Flask(__name__)


@app.route("/")
def default_resource() -> str:
    with app.open_resource("./resources/utf-8.txt") as f:
        data: str | bytes = f.read()
        script = data.decode("utf-8") if isinstance(data, bytes | bytearray) else str(data)
        app.logger.debug(script)

    return f"<code>{script}</code>"


@app.route("/string")
def string_resource() -> str:
    with app.open_resource("./resources/utf-8.txt", "r") as f:
        script: str = f.read()  # utf-8 encoded
        app.logger.debug(script)

    return f"<code>{script}</code>"


@app.route("/string/encoding")
def string_encoding_resource() -> str:
    with app.open_resource("./resources/utf-8.txt", "r", encoding="utf-8") as f:
        script: str = f.read()  # utf-8 encoded
        app.logger.debug(script)

    return f"<code>{script}</code>"


@app.route("/bytes")
def bytes_resource() -> str:
    with app.open_resource("./resources/utf-8.txt", "rb") as f:
        data: Any = f.read()
        script = bytes(data)
        app.logger.debug(script)

    return f"<code>{str(script)}</code>"


@app.route("/bytes/decode")
def bytes_decode_resource() -> str:
    with app.open_resource("./resources/utf-8.txt", "rb") as f:
        data: Any = f.read()
        script = bytes(data).decode("utf-8")  # utf-8 encoded
        app.logger.info(script)

    return f"<code>{script}</code>"
