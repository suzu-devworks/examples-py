#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = ["websockets>=15.0"]
# ///

"""Echo server using the asyncio API."""

import asyncio
import contextlib

from websockets.asyncio.server import ServerConnection, serve


async def echo(websocket: ServerConnection) -> None:
    async for message in websocket:
        print(f"<< {str(message)}")
        await websocket.send(message)


async def main() -> None:
    async with serve(echo, "localhost", 8765) as server:
        for sock in server.sockets:
            print(f"Server started at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
        await server.serve_forever()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
