"""HTTP Forms.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#http-forms

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_10_http_forms.py
    ```

    Access from your browser:

    - <http://127.0.0.1:8000/>
"""

from aiohttp import web


async def root(request: web.Request) -> web.StreamResponse:
    resp = web.Response(content_type="text/html")
    resp.text = """
        <html>
            <body>
                <form action="/login" method="post" accept-charset="utf-8"
                    enctype="application/x-www-form-urlencoded">

                    <label for="login">Login</label>
                    <input id="login" name="login" type="text" value="" autofocus/>
                    <label for="password">Password</label>
                    <input id="password" name="password" type="password" value=""/>

                    <input type="submit" value="login"/>
                </form>
            </body>
        </html>
        """
    return resp


async def do_login(request: web.Request) -> web.StreamResponse:
    data = await request.post()
    login = data["login"]
    _password = data["password"]

    print(f"User {str(login)} is logged in.")

    exc = web.HTTPFound(location="/")
    exc.set_cookie("AUTH", "secret", httponly=True, secure=True)
    raise exc


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.router.add_get("/", root)
    app.router.add_post("/login", do_login)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
