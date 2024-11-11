# Rye

Rye is a comprehensive project and package management solution for Python.

[![Rye](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/rye/main/artwork/badge.json)](https://rye.astral.sh)

## Table of Contents <!-- omit in toc -->

- [Rye](#rye)
  - [References](#references)
  - [Install](#install)
  - [Updating Rye](#updating-rye)
  - [Configurations](#configurations)
    - [Use uv](#use-uv)
    - [How the project was initialized](#how-the-project-was-initialized)
    - [Install dependency packages](#install-dependency-packages)
    - [Provide Console Scripts](#provide-console-scripts)
  - [Commands](#commands)
    - [`add` Add dependencies](#add-add-dependencies)
    - [`remove` Remove dependencies](#remove-remove-dependencies)
    - [`list` List dependencies](#list-list-dependencies)

## References

- <https://rye.astral.sh/>

## Install

To install you can run a curl command:

```shell
curl -sSf https://rye.astral.sh/get | bash
```

The install script that is piped to bash can be customized with some environment variables:

`RYE_INSTALL_OPTION="--yes"`:

Skip all prompts.

`RYE_TOOLCHAIN={path to python}`

Set it to point to the Python interpreter you want to use as the internal interpreter.

After installation, load the environment and enable rye.

```shell
source "$HOME/.rye/env"
```

It seems to be added to the shell profile during installation.

```console
$ tail -n 5 ~/.profile

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
. "$HOME/.rye/env"
```

## Updating Rye

```shell
rye self update
```

## Configurations

### Use uv

uv is a Python package manager also developed by Astral.

Rye 0.37.0 already has UV enabled.

```console
$ rye config --get behavior.use-uv

true
```

### How the project was initialized

Create project this command:

```shell
rye init apps/examples-packaging-rye
```

Move to the root of your project...

```shell
cd apps/examples-packaging-rye
```

The final directory will look like this:

```console
.
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── examples_packaging_rye
        └── __init__.py
```

Once that is done, you can use rye sync to get the first synchronization. After that, Rye will have created a virtualenv in `.venv` and written lockfiles into `requirements.lock` and `requirements-dev.lock`.

```shell
rye sync
```

### Install dependency packages

Install dependency packages for this project:

```shell
rye add -d ruff mypy pytest-cov pyclean
```

### Provide Console Scripts

How to provide console scripts in the PDM package.

- [project.scripts - Python Project (pyproject.toml)](https://rye.astral.sh/guide/pyproject/#projectscripts)

Create entry point:

```py
def main() -> None:
    print("Hello rye.")
```

`pyproject.toml`:

```toml
[project.scripts]
examples-rye-cli = "examples_packaging_rye.console.command:main"
```

Install the package locally:

```shell
rye sync
```

When you run it:

```console
$ examples-rye-cli

Hello rye.
```

## Commands

### `add` Add dependencies

```shell
rye add "flask>=2.0"
```

or

```shell
rye add --dev ruff
```

### `remove` Remove dependencies

```shell
rye remove flask
```

### `list` List dependencies

```shell
rye list
```
