# pdm

> PDM, as described, is a modern Python package and dependency manager supporting the latest PEP standards. But it is more than a package manager.

> _PEP 582 has been rejected_
>
> _This is a rejected PEP. However, due to the fact that this feature is the reason for PDM's birth, PDM will retain the support. We recommend using virtual environments instead._

`pyproject.toml` is PEP 621 supported.

## Table of Contents <!-- omit in toc -->

- [pdm](#pdm)
  - [References](#references)
  - [Installation](#installation)
    - [Using pip on venv](#using-pip-on-venv)
    - [Update](#update)
  - [Configurations](#configurations)
  - [Project management](#project-management)
    - [Project setup](#project-setup)
    - [Create virtualenv](#create-virtualenv)
    - [Restore packages](#restore-packages)
    - [Install packages](#install-packages)
    - [Update packages](#update-packages)
    - [Uninstall packages](#uninstall-packages)
    - [List packages](#list-packages)
    - [Build wheel package](#build-wheel-package)
  - [Tips](#tips)
    - [Use a task runner like npm.](#use-a-task-runner-like-npm)
    - [Dynamic versioning.](#dynamic-versioning)
  - [Provide Console Scripts](#provide-console-scripts)
    - [Create entry point](#create-entry-point)


## References

- https://pdm.fming.dev/latest/
- https://github.com/pdm-project/pdm


## Installation

### Using pip on venv

Installation methods:

```shell
pip install pdm
```

### Update

Update the PDM version:

```shell
pdm self update
```

## Configurations

PDM supports generating completion scripts for Bash, Zsh, Fish or Powershell.

for bash:

```shell
pdm completion bash > pdm.bash-completion
sudo mv pdm.bash-completion /etc/bash_completion.d/
```

- https://pdm.fming.dev/latest/#shell-completion

## Project management

### Project setup

```shell
pdm init
```

You will need to answer a few questions, to help PDM to create a pyproject.toml file for you.

```console
pdm init

Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /workspaces/examples-py/.venv/bin/python (3.11)
1. /usr/local/bin/python3.11 (3.11)
2. /usr/bin/python3.9 (3.9)
Please select (0):
Using Python interpreter: /workspaces/examples-py/.venv/bin/python (3.11)

Is the project a library that is installable?
If yes, we will need to ask a few more questions to include the project name and build backend [y/n] (n): y
Project name (mypackage):
Project version (0.1.0):
Project description ():
Which build backend to use?
0. pdm-backend
1. setuptools
2. flit-core
3. hatchling
4. pdm-pep517
Please select (0):
License(SPDX name) (MIT):
Author name (A.suzuki):
Author email (suzu.devworks@gmail.com):
Python requires('*' to allow any) (>=3.11):
Changes are written to pyproject.toml.

```

### Create virtualenv

pdm automatically creates a virtual environment the first time you run `pdm install`.

```shell
pdm install
```

Virtual environments will be used if the project interpreter( stored in `.pdm-python`) is from a virtualenv.
If `.pdm-python` doesn't exist, select the interpreter with `pdm use`.

### Restore packages

There are some similar commands for installing packages pinned to lockfiles, but with some differences.

- `pdm sync` installs packages from lock files.
- `pdm update` updates the lock file and then syncs.
- `pdm install` checks the project files for changes, updates the lock file if necessary, and then syncs.

`pdm install` installs the current project in editable mode.

### Install packages

```shell
pdm add {packages...}
```

When adding a development-only dependency:

```shell
pdm add  --dev {packages...}
pdm add  --dev --group {group} {packages...}
```

Editable dependencies:

```shell
pdm add -e {location} --dev
```

### Update packages

```shell
pdm update
pdm update {packages...}
```

### Uninstall packages

```shell
pdm remove {packages...}
```

### List packages

```shell
pdm list
```

### Build wheel package

```shell
pdm build
```

## Tips

### Use a task runner like npm.

PDM also supports custom script shortcuts in the optional `[tool.pdm.scripts]` section of `pyproject.toml`.

**`pyproject.toml`**:

```toml
[tool.pdm.scripts]
clean = "pyclean ."
clean_all_dirs_ = {shell = "find . | grep -E \"(/__pycache__$|\\.pyc$|\\.pyo$|/build$|/dist$)\" | xargs rm -rf"}
lint = "flake8"
test = "pytest"
```

To called a task, simply run:

```shell
pdm run clean
```

### Dynamic versioning.

**`pyproject.toml`**:

```toml
dynamic = ["version"]
# version = "0.1.0"

[tool.pdm]
version = {source = "file", path = "src/examples_packaging_pdm/__version.py"}
```

**`__version.py`**:

```py
__version__ = "0.1.1"
```


## Provide Console Scripts

How to provide console scripts in the PDM package.

- [Console scripts - PEP 621 Metadata](https://pdm-project.org/latest/reference/pep621/#console-scripts)

### Create entry point

Create `console/command.py` file:

```py
def main() -> None:
    print("Hello pdm.")
```

`pyproject.toml` is like this:

```ini
[project.scripts]
examples-pdm-cli = "examples_packaging_pdm.console.command:main"
```

Install the package locally:

```shell
pdm install
```

When you run it:

```console
$ examples-pdm-cli

Hello pdm.
```
