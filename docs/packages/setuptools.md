# setuptools

> Setuptools is a collection of enhancements to the Python distutils that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages.

## Table of Contents <!-- omit in toc -->

- [setuptools](#setuptools)
  - [References](#references)
  - [Installation](#installation)
  - [Setuptools configurations](#setuptools-configurations)
    - [Configure `pyproject.toml` project](#configure-pyprojecttoml-project)
    - [Configure `setup.cfg` project](#configure-setupcfg-project)
  - [Project management](#project-management)
    - [Dependency management](#dependency-management)
    - [Development mode.](#development-mode)
    - [Build wheel package](#build-wheel-package)
  - [`setup.py` command](#setuppy-command)
    - [Usage](#usage)
    - [Clean](#clean)
  - [Tips](#tips)
    - [Settings package version](#settings-package-version)
  - [Provide Console Scripts](#provide-console-scripts)
    - [Create entry point](#create-entry-point)


## References

- https://setuptools.pypa.io/en/latest/setuptools.html
- https://docs.python.org/ja/3/distutils/setupscript.html
- https://packaging.python.org/ja/latest/guides/distributing-packages-using-setuptools/
- https://github.com/pypa/setuptools


## Installation

Ensure pip, setuptools, and wheel are up to date.

```shell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel build
```

## Setuptools configurations

After a little research, the current setuptools configuration seems to fall into three categories.

1. legacy pattern of setup.cfg + setup.py ([pillow](https://github.com/python-pillow/Pillow)?)
2. pyproject.toml + setup.cfg(main) compatibility pattern ([django](https://github.com/django/django)?)
3. Future-oriented patterns in pyproject.toml ([flask](https://github.com/pallets/flask)?)

### Configure `pyproject.toml` project

It seems that 61.0.0 supports management with pyproject.toml.

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

### Configure `setup.cfg` project

**`setup.py`**:

Serves two primary functions:

1. your project are configured
2. the command line interface for running various commands that relate to packaging tasks.

> When a PEP 517 build is invoked, setuptools will emulate a dummy setup.py file.  
> However, editable installs are not supported, so you'll eventually need a setup.py.

**`setup.cfg`**:

Ini file containing option defaults for the setup.py command.

**`README.md`**:

All projects should contain a readme file.

**`MANIFEST.in`**:

needed when you need to package additional files that are not automatically included in a source distribution.

**`LICENSE.txt`**:

Every package should include a license file detailing the terms of distribution.

## Project management

### Dependency management

Dependencies will be installed together when you list them in `install_requires`:

```toml
[options]
install_requires =
    requests>=2.30.0
    importlib-metadata; python_version<"3.8"
```

Allows you to declare dependencies that are not installed by default:

```toml
[options.extras_require]
dev =
    flake8>=6.0.0
    mypy>=1.3.0
    black>=23.3.0
    isort>=5.12.0
    pytest-cov>=4.0.0
    pyclean>=2.7.0
doc =
    sphinx
```

Specify the key when installing:

```shell
pip install -e .[dev,doc]
```

### Development mode.

```shell
pip install -e .
```

### Build wheel package

```shell
python -m build
```
If you get the error `No module named` build:

```shell
pip install build
```


## `setup.py` command

### Usage

```shell
python setup.py --help-commands
python setup.py --help clean
```

### Clean

```shell
python setup.py clean --all
```


## Tips

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
