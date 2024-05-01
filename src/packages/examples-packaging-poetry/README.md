## examples-packaging-poetry

## Overview 

This is a project to learn packaging using poetry.

## Table of Contents <!-- omit in toc -->

- [examples-packaging-poetry](#examples-packaging-poetry)
- [Overview](#overview)
- [Getting started](#getting-started)
- [More Information](#more-information)
- [How the project was initialized](#how-the-project-was-initialized)
  - [Create project directories](#create-project-directories)
  - [Setup project](#setup-project)
  - [Install dependency packages](#install-dependency-packages)


## Getting started

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.poetry
. .venv.poetry/bin/activate
```

After updating pip, install the package manager:

```shell
python -m pip install --upgrade pip
pip install poetry
```

Move to the root of your project...

```shell
cd src/packages/examples-packaging-poetry
```

Install this project:

```shell
poetry install
```

When you run it:

```console
$ examples-poetry-cli

Hello poetry.
```

## More Information

- [docs/packages/poetry](/docs/packages/poetry.md)


## How the project was initialized

### Create project directories

Create and move project folder:

```shell
mkdir -p src/packages/examples-packaging-poetry
cd src/packages/examples-packaging-poetry
```

### Setup project

Initialized in a project using a command:

```shell
#　doesn't matter if the folder exists
poetry new .
```

The final directory will look like this:

```
.
├── README.md
├── examples_packaging_poetry
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py
```

### Install dependency packages

Install development dependency packages for this project:

```shell
poetry add --group dev flake8 mypy black isort pytest-cov pyclean
poetry add --group dev taskipy
```

<!-- // spell-checker:words taskipy -->
