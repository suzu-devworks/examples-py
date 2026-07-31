"""Static Files - Blueprint Resources.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#static-files

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_03_resources/_02_static_files run
    ```

    Outputted to the server console:

    ```console
    Static Files:  /static/style.css
    Static Files(admin):  /static/admin/style.css
    ```
"""

from flask import Flask, url_for


def create_app() -> Flask:
    from .admin import admin

    app = Flask(__name__)
    app.register_blueprint(admin)

    with app.test_request_context():
        print("Static Files: ", url_for("static", filename="style.css"))
        print("Static Files(admin): ", url_for("admin.static", filename="style.css"))

    return app
