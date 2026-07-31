# examples-http

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
- [CommandLine HTTP servers](#commandline-http-servers)

## Overview

This project is an example of web programming using Python.

## Get started

Get the dependent packages:

```shell
uv sync
```

- HTTPS servers:
  - `https_index_server.py` - Tiny HTTPS index server using `http.server`
  - `https_custom_handler_server.py` - Tiny HTTPS custom handler server using `http.server`

## CommandLine HTTP servers

For development purposes, you can start a simple server with `http.server`.

```shell
python -m http.server 9000
```
