#!/usr/bin/env python

import asyncio
import contextlib
import json
import logging

from websockets.asyncio.server import ServerConnection, broadcast, serve

logging.basicConfig()

USERS: set[ServerConnection] = set()

VALUE = 0


def users_event() -> str:
    return json.dumps({"type": "users", "count": len(USERS)})


def value_event() -> str:
    return json.dumps({"type": "value", "value": VALUE})


async def counter(websocket: ServerConnection) -> None:
    global USERS, VALUE
    try:
        # Register user
        USERS.add(websocket)
        broadcast(USERS, users_event())
        # Send current state to user
        await websocket.send(value_event())
        # Manage state changes
        async for message in websocket:
            event = json.loads(message)
            if event["action"] == "minus":
                VALUE -= 1
                broadcast(USERS, value_event())
            elif event["action"] == "plus":
                VALUE += 1
                broadcast(USERS, value_event())
            else:
                logging.error("unsupported event: %s", event)
    finally:
        # Unregister user
        USERS.remove(websocket)
        broadcast(USERS, users_event())


async def main() -> None:
    async with serve(counter, "localhost", 6789) as server:
        for sock in server.sockets:
            print(f"Server started at {sock.getsockname()[0]}:{sock.getsockname()[1]}")
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
