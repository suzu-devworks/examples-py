"""Class Based Views.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#class-based-views

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_08_json_response.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/
    ```
"""

from aiohttp import web

routes = web.RouteTableDef()


async def handler(request: web.Request) -> web.StreamResponse:
    data = {"some": "data"}
    return web.json_response(data)


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes([web.get("/", handler)])
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
