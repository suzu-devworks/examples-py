"""Accessing Request Data.

References:
    - https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data

Examples:
    Starting the server:
    ```shell
    flask --app src.quickstart._07_accessing_request_data run --debug
    ```

    Request from client:
    ```shell
    python src/quickstart/_07_accessing_request_data.py

    curl -v http://localhost:5000/login -X GET
    curl -v http://localhost:5000/login -X POST --data-urlencode "username={your name}" -d "password={password}"
    curl -v http://localhost:5000/upload -X POST -F the_file=@./README.md
    curl -v http://localhost:5000/ -b "username={your name}"
    ```
"""

from flask import Flask, Response, make_response, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

"""ref
### Context Locals
"""

if __name__ == "__main__":
    with app.test_request_context("/hello", method="POST"):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == "/hello"
        assert request.method == "POST"
        print("OK")

"""
### The Request Object
"""


@app.route("/login", methods=["POST", "GET"])
def login() -> str:
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template("login.html", error=error)


def valid_login(username: str, password: str) -> bool:
    return True


def log_the_user_in(username: str) -> str:
    return f"{username} is login."


"""
### File Uploads
"""


@app.route("/upload", methods=["GET", "POST"])
def upload_file() -> str:
    if request.method == "POST":
        file = request.files["the_file"]
        file_name = secure_filename(str(file.filename))
        print(f"save file to: uploads/{file_name}")
        # file.save(f"uploads/{file_name}")
    return f"OK: {file_name}, ({file.content_type})"


"""
### Cookies
"""


@app.route("/")
def index() -> Response:
    username = request.cookies.get("username")
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    resp = make_response(render_template("hello.html", name=username))
    resp.set_cookie("username", "the username")
    return resp
