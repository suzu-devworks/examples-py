"""Handler.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#handler

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_03_handler_use_decorator.py
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/
    curl -v -X POST http://localhost:8000/post
    curl -v -X PUT http://localhost:8000/put
    curl -v -X PATCH http://localhost:8000/path

    curl -v -X HEAD http://localhost:8000/
        # HTTP/1.1 405 Method Not Allowed
    ```
"""

from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/", allow_head=False)
async def get_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Get handler processed.")


@routes.post("/post")
async def post_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Post handler processed.")


@routes.put("/put")
async def put_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Put handler processed.")


async def all_handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="All handler processed.")


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.add_routes(routes)
    app.add_routes([web.route("*", "/path", all_handler)])
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
