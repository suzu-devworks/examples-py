#!/usr/bin/env python

import asyncio
import contextlib

from websockets.asyncio.server import ServerConnection, serve


async def hello(websocket: ServerConnection) -> None:
    name = await websocket.recv()
    print(f"<<< {str(name)}")

    greeting = f"Hello {str(name)}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main() -> None:
    async with serve(hello, "localhost", 8765) as server:
        for sock in server.sockets:
            print(f"Server started at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
