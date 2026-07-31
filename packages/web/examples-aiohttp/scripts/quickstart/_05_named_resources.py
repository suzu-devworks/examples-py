"""Reverse URL Constructing using Named Resources - Resources and Routes.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#reverse-url-constructing-using-named-resources

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_05_named_resources.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/validate
    ```
"""

from aiohttp import web
from yarl import URL

routes = web.RouteTableDef()


@routes.get("/root", name="root")
async def named_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Root handler processed.")


@routes.get("/validate")
async def name_validate_handler(request: web.Request) -> web.StreamResponse:
    # build a URL from a named resource.
    url = request.app.router["root"].url_for().with_query({"a": "b", "c": "d"})
    assert url == URL("/root?a=b&c=d")

    # pass in the parts of the route:
    url = request.app.router["user-info"].url_for(user="john_doe").with_query("a=b")
    assert url == URL("/john_doe/info?a=b")

    return web.Response(text="Root handler is valid.")


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes(routes)

    app.router.add_resource(r"/{user}/info", name="user-info")

    # Resource views
    for resource in app.router.resources():
        print(resource)

    for name, resource in app.router.named_resources().items():
        print(name, resource)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
