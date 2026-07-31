from aiohttp import web


async def handler(request: web.Request) -> web.StreamResponse:
    return web.Response(text="Hello, world")


admin = web.Application()
admin_key = web.AppKey("admin_key", web.Application)
admin.add_routes([web.get("/resource", handler, name="name")])
