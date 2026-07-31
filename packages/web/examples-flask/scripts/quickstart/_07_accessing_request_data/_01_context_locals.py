"""Context Locals - Accessing Request Data.

References:
    - https://flask.palletsprojects.com/en/stable/quickstart/#context-locals

Examples:
    Starting the server:

    ```shell
    flask --app ./examples/quickstart/_07_accessing_request_data/_01_context_locals run
    ```

    Outputted to the server console:

    ```console
    OK
    ```
"""

from flask import Flask, request

app = Flask(__name__)


with app.test_request_context("/hello", method="POST"):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == "/hello"
    assert request.method == "POST"
    print("OK")
