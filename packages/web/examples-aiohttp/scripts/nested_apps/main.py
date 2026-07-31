"""Run a Simple Web Server.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/nested_apps/main.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/
        # HTTP/1.1 302 Found to /admin/resource
    ```
"""

from aiohttp import web

from .admin import admin, admin_key  # type: ignore


async def index(request: web.Request) -> web.StreamResponse:
    admin = request.app[admin_key]
    url = admin.router["name"].url_for()
    raise web.HTTPFound(location=url)


def create_app(argv: list[str] | None = None) -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes([web.get("/", index)])

    app.add_subapp("/admin/", admin)
    app[admin_key] = admin

    # Resource views
    for resource in app.router.resources():
        print(resource)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
