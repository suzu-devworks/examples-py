# examples-packaging-pdm

## Table of Contents <!-- omit in toc -->

- [examples-packaging-pdm](#examples-packaging-pdm)
  - [Overview](#overview)
  - [Getting started](#getting-started)
  - [More Information](#more-information)
  - [How the project was initialized](#how-the-project-was-initialized)
    - [Create project directories](#create-project-directories)
    - [Setup project](#setup-project)
    - [Install dependency packages](#install-dependency-packages)


## Overview 

This project is an attempt to create packages using PDM.

## Getting started

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.pdm
. .venv.pdm/bin/activate
```

After updating pip, install the package manager:

```shell
python -m pip install --upgrade pip
pip install pdm
```

Move to the root of your project...

```shell
cd src/packages/examples-packaging-pdm
```

Install this project:

```shell
pdm install
```

When you run it:

```console
$ examples-pdm-cli

Hello pdm.
```


## More Information

- [docs/packages/pdm](/docs/packages/pdm.md)


## How the project was initialized

### Create project directories

Create and move project folder:

```shell
mkdir -p src/packages/examples-packaging-pdm
cd src/packages/examples-packaging-pdm
```

### Setup project

pdm can be initialized in a project using a command:

```shell
pdm init -n --dist
```

The final directory will look like this:

```
.
├── .gitignore
├── .pdm-python
├── README.md
├── pyproject.toml
├── src
│   └── examples_packaging_pdm
│       └── __init__.py
└── tests
    └── __init__.py
```

### Install dependency packages

Install development dependency packages for this project:

```shell
pdm add -d flake8 mypy black isort pytest-cov pyclean
```
