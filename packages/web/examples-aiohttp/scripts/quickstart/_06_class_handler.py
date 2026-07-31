"""Organizing Handlers in Classes - Resources and Routes.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#organizing-handlers-in-classes

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_06_class_handler.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/intro
    curl -v http://localhost:8000/greet/aiohttp
    ```
"""

from aiohttp import web


class Handler:
    def __init__(self) -> None:
        pass

    async def handle_intro(self, request: web.Request) -> web.StreamResponse:
        return web.Response(text="Hello, world")

    async def handle_greeting(self, request: web.Request) -> web.StreamResponse:
        name = request.match_info.get("name", "Anonymous")
        txt = f"Hello, {name}"
        return web.Response(text=txt)


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    handler = Handler()

    app = web.Application()
    app.add_routes(
        [
            web.get("/intro", handler.handle_intro),
            web.get("/greet/{name}", handler.handle_greeting),
        ]
    )

    # Resource views
    for resource in app.router.resources():
        print(resource)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
