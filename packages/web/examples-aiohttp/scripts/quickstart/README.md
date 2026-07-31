# Web Server Quickstart

## Get started

There is no package build, but please get the dependent pages.

```shell
uv sync
```

Using CLI:

```shell
python -m aiohttp.web -H localhost -P 8000 scripts.quickstart._01_simple:create_app
```

Using aiohttp-devtools

```shell
adev runserver --host localhost -p 8000 --app-factory create_app scripts/quickstart/_01_simple.py
```

## References

- [Web Server Quickstart - aiohttp](https://docs.aiohttp.org/en/stable/web_quickstart.html)
