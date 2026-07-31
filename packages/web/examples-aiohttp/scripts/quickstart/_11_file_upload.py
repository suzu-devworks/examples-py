"""File Uploads.

References:
    - https://docs.aiohttp.org/en/stable/web_quickstart.html#file-uploads

Examples:
    Starting the server:

    ```shell
    adev runserver scripts/quickstart/_11_file_upload.py
    ```

    Access from your browser:

    - <http://127.0.0.1:8000/>
"""

import os

from aiohttp import BodyPartReader, web


async def root(request: web.Request) -> web.StreamResponse:
    resp = web.Response(content_type="text/html")
    resp.text = """
        <html>
            <body>
                <form action="/store/mp3" method="post" accept-charset="utf-8"
                    enctype="multipart/form-data">
                    <label for="name">Name</label>
                    <input id="name" name="name" type="text" value=""/>
                    <br/>
                    <label for="mp3">Mp3</label>
                    <input id="mp3" name="mp3" type="file" value=""/>
                    <br/>
                    <input type="submit" value="submit"/>
                </form>
            </body>
        </html>
        """
    return resp


async def store_mp3_handler(request: web.Request) -> web.StreamResponse:
    # # WARNING: don't do that if you plan to receive large files!
    # data = await request.post()

    # mp3 = data["mp3"]

    # # .filename contains the name of the file in string format.
    # if isinstance(mp3, web.FileField):
    #     filename = mp3.filename

    #     # .file contains the actual file data that needs to be stored somewhere.
    #     mp3_file = mp3.file

    #     content = mp3_file.read()
    # else:
    #     return web.Response(text="Invalid file upload", status=400)

    # return web.Response(
    #     body=content,
    #     headers=MultiDict({"Content-Disposition": f'attachment; filename="{filename}"'}),
    # )

    reader = await request.multipart()

    # /!\ Don't forget to validate your inputs /!\

    # reader.next() will `yield` the fields of your form

    field = await reader.next()
    if not isinstance(field, BodyPartReader) or field.name != "name":
        return web.Response(text="Invalid form data", status=400)
    _name = await field.read(decode=True)

    field = await reader.next()
    if not isinstance(field, BodyPartReader) or field.name != "mp3" or field.filename is None:
        return web.Response(text="Invalid form data", status=400)
    filename = field.filename

    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    os.makedirs("/tmp/upload/", exist_ok=True)
    with open(os.path.join("/tmp/upload/", filename), "wb") as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    return web.Response(text=f"{filename} sized of {size} successfully stored")


def create_app() -> web.Application:
    """default app-factory for aiohttp."""
    app = web.Application()
    app.router.add_get("/", root)
    app.router.add_post("/store/mp3", store_mp3_handler)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
