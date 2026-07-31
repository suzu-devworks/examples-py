#!/usr/bin/env python

import asyncio

from websockets.asyncio.client import connect


async def hello() -> None:
    uri = "ws://localhost:8765"
    async with connect(uri) as websocket:
        print(f"Connect to: {websocket.remote_address[0]}:{websocket.remote_address[1]}")

        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {str(greeting)}")


if __name__ == "__main__":
    asyncio.run(hello())
