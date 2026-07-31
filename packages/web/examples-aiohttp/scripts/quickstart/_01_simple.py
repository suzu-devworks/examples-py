"""Run a Simple Web Server.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_01_simple.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/
    ```
"""

from aiohttp import web


async def hello(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Hello, world")


def create_app(argv: list[str] | None = None) -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes([web.get("/", hello)])
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
