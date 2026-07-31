"""Blueprint Resource Folder - Blueprint Resources.

References:
    - https://flask.palletsprojects.com/en/stable/blueprints/#blueprint-resource-folder

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/blueprints/_03_resources/_01_resource_folder run
    ```

    Outputted to the server console:

    ```console
    Blueprint Resource Folder:
      /workspaces/examples-py-web/packages/examples-flask/./examples/blueprints/my_first_blueprint
    style.css is:
      b'/*  @/my_first_blueprint/static/style.css */\n'
    ```
"""

from flask import Flask


def create_app() -> Flask:
    from my_first_blueprint.simple_page import simple_page

    app = Flask(__name__)

    print("Blueprint Resource Folder:\n", simple_page.root_path)

    with simple_page.open_resource("static/style.css") as f:
        code = f.read()
        print("style.css is:\n", code)

    return app
