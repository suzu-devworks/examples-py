# examples-packaging-setup

## Overview 

This is a project to learn packaging using setuptools.

## Build

### When preparing a venv

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.setup
. .venv.setup/bin/activate
```

### Package installation

Install dependencies after updating pip and setuptools wheel

```shell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -e .[dev,doc]
```

### Build package

```shell
python -m build
```

## How the project was initialized


### Create project directories

This project was initialized with the following command:

```shell
mkdir -p src/packages/examples-packaging-setup
cd src/packages/examples-packaging-setup

mkdir -p src/examples_packaging_setup/
touch src/examples_packaging_setup/__init__.py
```

### Write project files

Create two files for project settings.
There are no commands.

Here we create it in setup.cfg instead of pyproject.toml.

- [setup.py](./setup.py)
- [setup.cfg](./setup.cfg)

The final directory will look like this:

```
.
├── README.md
├── setup.cfg
├── setup.py
└── src
    └── examples_packaging_setup
        └── __init__.py
```

### Settings package version

If you want to define the version somewhere readable from python

- [Manage package versions in one place](https://packaging.python.org/ja/latest/guides/single-sourcing-package-version/)

Define versions globally in top level `__init__.py` :

```py
__version__ = "0.1.0"
```

And `setup.cfg` is like this:

```ini
[metadata]
...
version = attr: examples_packaging_setup.__version__
...
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

And `setup.cfg` is like this:

```ini
[options.entry_points]
console_scripts =
    examples-setup-cli = examples_packaging_setup.console.command:main
```

install the package locally:

```shell
pip install -e .
```

```console
$ examples-setup-cli

Hello setuptools.
```

