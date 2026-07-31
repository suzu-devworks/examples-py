# Example - home

Let's try running the first example from the official website.

## References

- [Example - FastAPI framework](https://fastapi.tiangolo.com/#example)

## Getting started

```shell
uv run fastapi dev ./scripts/home/main.py 
```

```console
   FastAPI   Starting development server 🚀
      ...
    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs
      ...
      INFO   Application startup complete.
```

Access  from your browser:

- <http://127.0.0.1:8000/items/5?q=somequery>

The response JSON will look like this:

```json
{"item_id":5,"q":"somequery"}
```
<!-- spell-checker:words somequery -->

Interactive API docs:

- <http://127.0.0.1:8000/docs>
