#!/usr/bin/env python

import asyncio
import contextlib
import datetime
import random

from websockets.asyncio.server import ServerConnection, serve


async def show_time(websocket: ServerConnection) -> None:
    print(f"Connect from: {websocket.remote_address[0]}:{websocket.remote_address[1]}")
    while True:
        message = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
        await websocket.send(message)
        await asyncio.sleep(random.random() * 2 + 1)


async def main() -> None:
    async with serve(show_time, "localhost", 5678) as server:
        for sock in server.sockets:
            print(f"Server started at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
