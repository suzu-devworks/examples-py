"""Redirect.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#redirect

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_13_redirect.py
    ```

    Access from your browser:

    - <http://127.0.0.1:8000/>
"""

import os
from typing import Any, NoReturn

import aiohttp_jinja2
import jinja2
from aiohttp import web
from multidict import MultiDictProxy


@aiohttp_jinja2.template("index.html")
async def index(request: web.Request) -> web.StreamResponse | dict[str, str]:
    if request.cookies.get("AUTH") is None:
        location = request.app.router["login"].url_for()
        raise web.HTTPFound(location=location)
    return {"username": "admin"}


@aiohttp_jinja2.template("login.html")
async def login(request: web.Request) -> web.StreamResponse | dict[str, str]:
    if request.method == "POST":
        form = await request.post()
        error = validate_login(form)
        if error:
            return {"error": error}
        else:
            # login form is valid

            location = request.app.router["index"].url_for()
            exc = web.HTTPFound(location=location)
            exc.set_cookie("AUTH", "secret", httponly=True, secure=True)
            raise exc

    return {}


def validate_login(form: MultiDictProxy[str | Any]) -> str:
    if form["username"] != "admin" or form["password"] != "admin":
        return "Invalid username or password"
    return ""


async def logout(request: web.Request) -> NoReturn:
    exc = web.HTTPFound(location="/login")
    exc.del_cookie("AUTH")
    raise exc


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(f"{os.path.dirname(__file__)}/templates"),
    )

    app.router.add_get("/", index, name="index")
    app.router.add_get("/login", login, name="login")
    app.router.add_post("/login", login, name="login")
    app.router.add_get("/logout", logout)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
