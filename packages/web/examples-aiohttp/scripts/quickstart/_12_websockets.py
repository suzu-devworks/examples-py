"""WebSockets.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets
    - https://docs.aiohttp.org/en/stable/web_advanced.html#websocket-shutdown

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_12_websockets.py
    ```

    Access from your browser:

    - <http://127.0.0.1:8000/>
"""

import weakref

from aiohttp import WSCloseCode, WSMsgType, web

websockets = web.AppKey("websockets", weakref.WeakSet[web.WebSocketResponse])


async def root(request: web.Request) -> web.StreamResponse:
    resp = web.Response(content_type="text/html")
    resp.text = """
        <html>
            <body>
                <h1>WebSockets</h1>
                <div id="output"></div>

                <script>
                document.addEventListener("DOMContentLoaded", () => {
                    const ws = new WebSocket(`ws://${window.location.host}/ws`);
                    ws.onopen = () => {
                        ws.send("test");
                    };
                    ws.onmessage = (event) => {
                        console.log(event.data);
                        document.getElementById("output").textContent = event.data;
                    };
                });
                </script>
            </body>
        </html>
        """
    return resp


async def websocket_handler(request: web.Request) -> web.WebSocketResponse:
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    request.app[websockets].add(ws)

    print("websocket connection closed")
    try:
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == "close":
                    await ws.close()
                else:
                    await ws.send_str(msg.data + "/answer")
            elif msg.type == WSMsgType.ERROR:
                print(f"ws connection closed with exception {ws.exception()}")

    finally:
        request.app[websockets].discard(ws)

    return ws


async def on_shutdown(app: web.Application) -> None:
    for ws in app[websockets]:
        await ws.close(code=WSCloseCode.GOING_AWAY, message=b"Server shutdown")


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()

    app[websockets] = weakref.WeakSet()
    app.on_shutdown.append(on_shutdown)

    app.router.add_get("/", root)
    app.router.add_get("/ws", websocket_handler)  # registered as HTTP GET
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
