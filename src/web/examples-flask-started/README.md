# examples-flask-started

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## Table of Contents <!-- omit in toc -->

- [examples-flask-started](#examples-flask-started)
  - [Overview](#overview)
  - [References](#references)
  - [Getting started](#getting-started)
  - [Tried this](#tried-this)
  - [How the project was initialized](#how-the-project-was-initialized)


## Overview 

Flask web programming examples.


## References

- https://flask.palletsprojects.com/


## Getting started

```shell
cd src/examples-flask-started

# select interpreter
pdm use

# install dependencies and self.
pdm install
```

Create database:

```shell
flask --app flaskr init-db
```

## Tried this

<!-- // spell-checker:words Quickstart -->
- [Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- [Tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/)


## How the project was initialized

This project was initialized with the following command:

```shell
mkdir -p src/examples-flask-started
cd src/examples-flask-started

# create new pyproject.toml
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean
pdm add flask

```
