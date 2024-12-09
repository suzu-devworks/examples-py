# uv

An extremely fast Python package and project manager, written in Rust.

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

## Table of Contents <!-- omit in toc -->

- [uv](#uv)
  - [References](#references)
  - [Install uv](#install-uv)
    - [Standalone installer](#standalone-installer)
    - [Docker](#docker)
    - [Upgrade uv](#upgrade-uv)
  - [Configurations](#configurations)
    - [Whether to allow Python downloads](#whether-to-allow-python-downloads)
  - [Create projects](#create-projects)
    - [`init --app`(default)](#init---appdefault)
    - [`init --package`](#init---package)
    - [`init --no-package`](#init---no-package)
    - [`init --lib`](#init---lib)
    - [`init --script`](#init---script)
    - [Workspace](#workspace)

## References

- <https://docs.astral.sh/uv/>

## Install uv

### Standalone installer

To install you can run a curl command:

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Docker

There are two ways to use uv with Docker: copy the binaries from the official image or install it using the installer.

This repository uses the DevContainers Python image, so we install it using the postCreateCommand.

### Upgrade uv

```shell
uv self update
```

## Configurations

### Whether to allow Python downloads

## Create projects

### `init --app`(default)

Create a project for an application.

```console
examples-app
├── .python-version
├── README.md
├── hello.py
└── pyproject.toml
```

### `init --package`

Set up the project to be built as a Python package.

```console
examples-package/
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── examples_package
        └── __init__.py
```

### `init --no-package`

Do not set up the project to be built as a Python package.

```console
examples-no-package
├── .python-version
├── README.md
├── hello.py
└── pyproject.toml
```

### `init --lib`

Create a project for a library.

```console
examples-lib
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── examples_lib
        ├── __init__.py
        └── py.typed
```

### `init --script`

Create a script.

```python
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


def main() -> None:
    print("Hello from examples-script!")


if __name__ == "__main__":
    main()
```

### Workspace

Create root pyproject.toml:

```shell
uv init --author-from auto
rm hello.py
```

Append to pyproject.toml

```toml

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
build-backend = "hatchling.build"
requires = ["hatchling"]

[tool.hatch.build.targets.wheel]
packages = ["packages/*"]
```
