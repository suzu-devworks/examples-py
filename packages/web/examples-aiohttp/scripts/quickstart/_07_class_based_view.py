"""Class Based Views - Resources and Routes.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#class-based-views

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_06_class_based_view
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/path/to/aiohttp
    curl -v -X POST http://localhost:8000/path/to/aiohttp
    ```
"""

from aiohttp import web


class MyView(web.View):
    async def get(self) -> web.StreamResponse:
        return await self.get_resp(self.request)

    async def post(self) -> web.StreamResponse:
        return await self.post_resp(self.request)

    async def get_resp(self, request: web.Request) -> web.StreamResponse:
        name = request.match_info.get("name", "Anonymous")
        txt = f"Get: {name}"
        return web.Response(text=txt)

    async def post_resp(self, request: web.Request) -> web.StreamResponse:
        name = request.match_info.get("name", "Anonymous")
        txt = f"Post: {name}"
        return web.Response(text=txt)


def create_app() -> web.Application:
    """default app-factory for aiohttp."""

    app = web.Application()
    app.add_routes([web.view("/path/to/{name}", MyView)])
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
