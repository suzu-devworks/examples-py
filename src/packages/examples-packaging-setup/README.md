# examples-packaging-setup

## Overview 

This is a project to learn packaging using setuptools.

## Table of Contents <!-- omit in toc -->

- [examples-packaging-setup](#examples-packaging-setup)
  - [Overview](#overview)
  - [Getting started](#getting-started)
    - [When preparing a venv](#when-preparing-a-venv)
    - [Install package manager](#install-package-manager)
    - [Build](#build)
    - [Run](#run)
  - [How the project was initialized](#how-the-project-was-initialized)
    - [Create project directories](#create-project-directories)
    - [Write `setup.cfg`, `setup.py` files](#write-setupcfg-setuppy-files)
    - [Generate source directories](#generate-source-directories)
  - [Provide Console Scripts](#provide-console-scripts)
    - [Create entry point](#create-entry-point)


## Getting started

### When preparing a venv

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.setup
. .venv.setup/bin/activate
```

### Install package manager

Install dependencies after updating pip and setuptools wheel

```shell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
```

### Build

```shell
cd src/packages/examples-packaging-setup
```

Install dependency packages for this project:

```shell
pip install -e .[dev,doc]
```

Install this package locally:

```shell
pip install -e .
```

### Run

When you run it:

```console
$ examples-setup-cli

Hello setuptools.
```


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
mkdir -p src/examples_packaging_setup/
touch src/examples_packaging_setup/__init__.py
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


## Provide Console Scripts

How to provide console scripts in the setuptools package.

- [Entry Points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)

### Create entry point

Create `console/command.py` file:

```py
def main() -> None:
    print("Hello setuptools.")
```

`setup.cfg` is like this:

```ini
[options.entry_points]
console_scripts =
    examples-setup-cli = examples_packaging_setup.console.command:main
```

Install the package locally:

```shell
pip install -e .
```

When you run it:

```console
$ examples-setup-cli

Hello setuptools.
```
