"""Unique URLs / Redirection Behavior - Routing.

Try different behavior depending on whether the canonical URL
for your endpoint has a trailing slash or not.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#unique-urls-redirection-behavior

Examples:
    Starting the server:

        ```shell
        flask --app ./examples/quickstart/_04_routing/_03_unique_urls run
        ```

    When there is a trailing slash.
    Request from client to "/projects/":

    ```shell
    curl -v http://localhost:5000/projects/
    # > HTTP/1.1 200 OK

    curl -v http://localhost:5000/projects
    # > HTTP/1.1 308 PERMANENT REDIRECT
    ```

    When there is no trailing slash.
    Request from client to "/about":

    ```shell
    curl -v http://localhost:5000/about/
    # > HTTP/1.1 404 NOT FOUND

    curl -v http://localhost:5000/about
    # > HTTP/1.1 200 OK
    ```

"""

from flask import Flask

app = Flask(__name__)


@app.route("/projects/")
def projects() -> str:
    return "The project page"


@app.route("/about")
def about() -> str:
    return "The about page"
