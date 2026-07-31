# examples-flask-media

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Setup](#setup)
  - [Run](#run)
- [Examples](#examples)

## Overview

This project is an example of web media and streaming using Flask.

### Setup

Get the dependent packages:

```shell
uv sync
```

### Run

Run the server:

```shell
flask --app examples_flask_media run
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Examples

- [Example of webcam streaming using MJPEG](./src/examples_flask_media/blueprints/webcam/mjpeg/README.md)
- [Example of segmented video streaming](./src/examples_flask_media/blueprints/video/chunks/README.md)
