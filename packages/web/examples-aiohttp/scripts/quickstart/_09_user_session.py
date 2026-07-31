"""User Sessions.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#user-sessions

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_09_user_session.py --app-factory make_app
    ```

    Request from client:

    ```shell
    curl -v http://localhost:8000/
    curl -v http://localhost:8000/ -b "AIOHTTP_SESSION=..."
    ```
"""

import base64
import time

from aiohttp import web
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet


async def handler(request: web.Request) -> web.StreamResponse:
    session = await get_session(request)

    last_visit = session.get("last_visit")
    session["last_visit"] = time.time()
    text = f"Last visited: {last_visit}"

    return web.Response(text=text)


async def make_app() -> web.Application:
    app = web.Application()
    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes([web.get("/", handler)])
    return app


if __name__ == "__main__":
    web.run_app(make_app(), port=8000)
