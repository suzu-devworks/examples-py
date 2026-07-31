"""Blueprint Error Handlers.

Blueprints support the errorhandler decorator just like the Flask application object.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#blueprint-error-handlers

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_05_error_handlers run
    ```

    Request from client:

    ```shell
    curl -v http://localhost:5000/
        # HTTP/1.1 404 NOT FOUND (app.handler)

    curl -v http://localhost:5000/api/not-found
        # HTTP/1.1 404 NOT FOUND (app.handler)

    curl -v http://localhost:5000/raise
        # HTTP/1.1 404 NOT FOUND (simple_page.handler)

    curl -v http://localhost:5000/abort
        # HTTP/1.1 404 NOT FOUND (simple_page.handler)

    curl -v http://localhost:5000/returns
        # HTTP/1.1 404 NOT FOUND (Return without handle)
    ```

"""

from typing import Any

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException


def create_app() -> Flask:
    from .simple_page import simple_page

    app = Flask(__name__)
    app.register_blueprint(simple_page)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex: HTTPException) -> Any:
        app.logger.debug("app handler was called.")
        if request.path.startswith("/api/"):
            return jsonify(error=str(ex)), ex.code
        else:
            return ex

    return app
