# examples-flask

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
  - [Setup](#setup)
  - [Run flaskr](#run-flaskr)
  - [Run examples\_flask](#run-examples_flask)
- [Examples](#examples)
  - [User’s Guide](#users-guide)
  - [Others](#others)
  - [examples\_flask apps](#examples_flask-apps)

## Overview

This project is an examples of Python web application using Flask.

- [Flask’s documentation](https://flask.palletsprojects.com/)

## Get started

### Setup

Get the dependent packages:

```shell
uv sync
```

### Run flaskr

Create a database:

```shell
flask --app flaskr init-db
```

Run the server:

```shell
flask --app flaskr run 
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

### Run examples_flask

Run the server:

```shell
flask --app examples_flask run 
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Examples

### User’s Guide

- [Quickstart](./examples/quickstart/README.md)
- [Tutorial - flaskr](./src/flaskr/README.md)
- [Modular Applications with Blueprints](./examples/blueprints/README.md)

### Others

- [Encodings](./examples/encodings/README.md)

### examples_flask apps

- [Overriding Blueprint Resources](./src/examples_flask/blueprints/overriding/)
