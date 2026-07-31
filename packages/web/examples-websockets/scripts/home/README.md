# echo - websockets

## Table of Contents <!-- omit in toc -->

- [Homepage](#homepage)
  - [Echo server](#echo-server)

## Homepage

Let's try the first example on the official website's homepage.

- [websockets documentation :link:](https://websockets.readthedocs.io/en/stable/)

### Echo server

There are asyncio and threading versions, but I think it's enough to just remember asyncio.

Start server:

```shell
uv run examples/home/echo/server.py 
```

Start client:

```shell
uv run examples/home/echo/client.py 
```

Also, websockets provides an interactive client:

```shell
uv run -m websockets ws://localhost:8765/
```
