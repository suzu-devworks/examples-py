# setuptools

> Setuptools is a collection of enhancements to the Python distutils that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages.

## Table of Contents <!-- omit in toc -->

- [setuptools](#setuptools)
  - [References](#references)
  - [Installation](#installation)
  - [Configuration `pyproject.toml` project](#configuration-pyprojecttoml-project)
  - [Configuration `setup.cfg` project](#configuration-setupcfg-project)
    - [Initial files](#initial-files)
    - [Dependency management](#dependency-management)
  - [Usage](#usage)
    - [Development mode.](#development-mode)
    - [Build package](#build-package)


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

## Configuration `pyproject.toml` project

It seems that 61.0.0 supports management with pyproject.toml.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

## Configuration `setup.cfg` project

### Initial files

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

## Usage

### Development mode.

```shell
pip install -e .
```

### Build package

```shell
python -m build
```
If you get the error `No module named` build:

```shell
pip install build
```

<!-- ## Tips -->
