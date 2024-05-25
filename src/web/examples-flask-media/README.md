# examples-flask-media

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## Table of Contents <!-- omit in toc -->

- [examples-flask-media](#examples-flask-media)
  - [Overview](#overview)
  - [References](#references)
  - [Getting started](#getting-started)
  - [Examples index](#examples-index)
  - [How the project was initialized](#how-the-project-was-initialized)
  - [Troubleshooting](#troubleshooting)
    - [ImportError: libGL.so.1: cannot open shared object file: No such file or directory](#importerror-libglso1-cannot-open-shared-object-file-no-such-file-or-directory)


## Overview 

This project is an example of web media and streaming using Flask.

## References


## Getting started

```shell
# select interpreter
pdm use

# install dependencies and self.
pdm install
```

Start flask server:

```shell
pdm run dev
```

## Examples index

- [Live streaming webcams](./src/examples/webcam/README.md)

## How the project was initialized

This project was initialized with the following command:

```shell
mkdir -p src/web/examples-flask-media
cd src/web/examples-flask-media

# create new pyproject.toml
pdm init -n
pdm add -d flake8 mypy black isort pytest-cov pyclean
pdm add flask
```


## Troubleshooting

### ImportError: libGL.so.1: cannot open shared object file: No such file or directory

```shell
apt install -y libgl1-mesa-dev
```
<!-- // spell-checker:words libgl1 -->
