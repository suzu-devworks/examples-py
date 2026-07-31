# Tutorial - User Guide

I'll try some of the code from the official website tutorial.

## Table of Contents <!-- omit in toc -->

- [References](#references)
- [Examples](#examples)
  - [Security](#security)
  - [CORS (Cross-Origin Resource Sharing)](#cors-cross-origin-resource-sharing)
  - [Bigger Applications - Multiple Files](#bigger-applications---multiple-files)

## References

- [Tutorial - User Guide - FastAPI](https://fastapi.tiangolo.com/tutorial/)

## Examples

### Security

Learn how to implement simple authentication using oauth2's password flow.

Starting the server:

```shell
uv run fastapi dev ./scripts/tutorials/security/main.py
```

Interactive API docs:

- <http://127.0.0.1:8000/docs>

Let's press the Authorize button.

### CORS (Cross-Origin Resource Sharing)

You can configure it in your FastAPI application using the CORSMiddleware.

First, set the secret:

```shell
export SECRET_KEY=$(openssl rand -hex 32)
```

Starting the server:

```shell
uv run fastapi dev ./scripts/tutorials/cors/main.py
```

CORS request from client:

```shell
curl -v http://localhost:8000/ -H "Origin:https://localhost.tiangolo.com"
```

```console
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET / HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.88.1
> Accept: */*
> Origin:https://localhost.tiangolo.com
> 
< HTTP/1.1 200 OK
< date: Thu, 30 Jan 2025 12:57:22 GMT
< server: uvicorn
< content-length: 25
< content-type: application/json
< access-control-allow-credentials: true
< access-control-allow-origin: https://localhost.tiangolo.com
< vary: Origin
< 
* Connection #0 to host localhost left intact
```

If the `access-control-allow-origin` header is present in the response, the request is successful (allowed).

### Bigger Applications - Multiple Files

In a real application, you would need to implement quite a few APIs, so creating them in a single file would be impractical.

This is the equivalent of Flask's Blueprints.

For examples:

```shell
uv run fastapi dev ./scripts/tutorials/app/main.py
```

Interactive API docs:

- <http://127.0.0.1:8000/docs>
