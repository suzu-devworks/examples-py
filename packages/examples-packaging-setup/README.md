# examples-packaging-setup

## Overview 

This is a project to learn packaging using setuptools.

## Table of Contents <!-- omit in toc -->

- [examples-packaging-setup](#examples-packaging-setup)
  - [Overview](#overview)
  - [Getting started](#getting-started)
  - [More Information](#more-information)
  - [How the project was initialized](#how-the-project-was-initialized)
    - [Create project directories](#create-project-directories)
    - [Write `setup.cfg`, `setup.py` files](#write-setupcfg-setuppy-files)
    - [Generate source directories](#generate-source-directories)
    - [Install packages](#install-packages)


## Getting started

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.setup
. .venv.setup/bin/activate
```

Update pip and setuptools wheels:

```shell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
```

Move to the root of your project...

```shell
cd packages/examples-packaging-setup
```

Install this project:

```shell
pip install -e .
```

When you run it:

```console
$ examples-setup-cli

Hello setuptools.
```


## More Information

- [docs/packages/setuptools](/docs/packages/setuptools.md)


## How the project was initialized

### Create project directories

Create and move project folder:

```shell
mkdir -p src/packages/examples-packaging-setup
cd src/packages/examples-packaging-setup
```

### Write `setup.cfg`, `setup.py` files

Create two files for project settings.
There are no commands.

Create these files:

- [setup.py](./setup.py)
- [setup.cfg](./setup.cfg)
- [pyproject.toml](./pyproject.toml)

### Generate source directories

Generate the initial directory for the package with the following command:

```shell
mkdir -p examples_packaging_setup/
touch examples_packaging_setup/__init__.py
```

The final directory will look like this:

```
.
├── README.md
├── pyproject.toml
├── setup.cfg
├── setup.py
└── src
    └── examples_packaging_setup
        └── __init__.py
```

### Install packages

Install development dependency packages for this project:

```shell
pip install -e .[dev,doc]
```
