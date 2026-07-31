"""Variable Resources - Resources and Routes.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#variable-resources

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_04_variable_resources.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/aiohttp
    curl -v http://localhost:8000/12345
    ```
"""

from aiohttp import web

routes = web.RouteTableDef()


@routes.get(r"/{num:\d+$}")
async def regex_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text=f"Call number is: [{request.match_info['num']}")


@routes.get("/{name}")
async def variable_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text=f"Hello, {request.match_info['name']}")


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes(routes)

    # Resource views
    for resource in app.router.resources():
        print(resource)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
