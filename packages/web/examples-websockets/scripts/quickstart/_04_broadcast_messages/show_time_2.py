#!/usr/bin/env python

import asyncio
import contextlib
import datetime
import random

from websockets.asyncio.server import ServerConnection, broadcast, serve

CONNECTIONS: set[ServerConnection] = set()


async def register(websocket: ServerConnection) -> None:
    print(f"Connect from: {websocket.remote_address[0]}:{websocket.remote_address[1]}")
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)


async def show_time() -> None:
    while True:
        message = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
        broadcast(CONNECTIONS, message)
        await asyncio.sleep(random.random() * 2 + 1)


async def main() -> None:
    async with serve(register, "localhost", 5678) as server:
        for sock in server.sockets:
            print(f"Server started at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
        await show_time()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
