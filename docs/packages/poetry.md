# poetry

> Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Table of Contents <!-- omit in toc -->

- [poetry](#poetry)
  - [References](#references)
  - [Installation](#installation)
    - [Using pip on venv](#using-pip-on-venv)
    - [Update poetry](#update-poetry)
  - [Package management](#package-management)
    - [Project setup](#project-setup)
    - [Create virtualenv](#create-virtualenv)
    - [Remove the virtualenv](#remove-the-virtualenv)
    - [Spawns a shell within the virtualenv](#spawns-a-shell-within-the-virtualenv)
    - [Spawns a command installed into the virtualenv](#spawns-a-command-installed-into-the-virtualenv)
    - [Restore packages](#restore-packages)
    - [Add package](#add-package)
    - [List packages](#list-packages)
    - [Update package](#update-package)
    - [Update outdated packages](#update-outdated-packages)
    - [Remove package](#remove-package)
    - [Build wheel package](#build-wheel-package)
  - [Tips](#tips)
    - [Use a task runner like npm.](#use-a-task-runner-like-npm)
  - [Provide Console Scripts](#provide-console-scripts)
    - [Create entry point](#create-entry-point)

## References

- https://python-poetry.org/
- https://github.com/python-poetry/poetry


## Installation

### Using pip on venv

I installed it with pip and it seems fine.

```shell
pip install poetry
```

### Update poetry

Poetry itself can be updated:

```shell
poetry self update
```


## Package management

### Project setup

```shell
mkdir {project}
cd {project}

poetry new .

or

poetry init
```

`init` is generates `pyproject.toml`.  
`new` also creates an initial directories and files.

### Create virtualenv

Create a virtual environment when installing dependencies

```shell
poetry install
```

By default, Poetry creates a virtual environment in `{cache-dir}/virtualenvs`.

If you want a virtual environment in your project folder, enable the following settings in `poetry.toml`:

```shell
poetry config virtualenvs.in-project true --local
```

however, Poetry will detect and respect an existing virtual environment that has been externally activated.

### Remove the virtualenv

```shell
poetry env remove {virtualenv}
```

### Spawns a shell within the virtualenv

```shell
poetry shell
```

### Spawns a command installed into the virtualenv

```shell
poetry run {command}
```

### Restore packages

Wherever you have `pyproject.toml` do the following

```shell
poetry install
```

Current projects are installed in editable mode by default.

### Add package

How to add dependencies:

```shell
poetry add {packages...}
```

### List packages

```shell
poetry show
```

### Update package

```shell
poetry update {packages...}
```

Same as deleting `poetry.lock` and running install.

### Update outdated packages

show outdated list:

```shell
poetry show --outdated
```

Update all dependency packages:

```shell
poetry update
```

`poetry.lock` should be updated.


### Remove package

```shell
poetry remove {packages...}
```

### Build wheel package

`poetry-core` is python wheels are supported.

```shell
poetry build
```

## Tips

### Use a task runner like npm.

The `taskipy` is complementary task runner for python.

- https://github.com/taskipy/taskipy

To install taskipy as a dev dependency, simply run:

```shell
poetry add --group dev taskipy
```

In your pyproject.toml file, add a new section called `[tool.taskipy.tasks]`:

**`pyproject.toml`**:

```toml
[tool.taskipy.tasks]
clean = "pyclean ."
test = "pytest"
```

To called a task, simply run:

```shell
poetry run task clean

or

task clean
```


## Provide Console Scripts

How to provide console scripts in the poetry package.


### Create entry point

Create `console/command.py` file:

```py
def main() -> None:
    print("Hello poetry.")
```

`pyproject.toml` is like this:

```ini
[tool.poetry.scripts]
examples-poetry-cli = 'examples_packaging_poetry.console.command:main'
```

Install the package locally:

```shell
poetry install
```

When you run it:

```console
$ examples-poetry-cli

Hello poetry.
```
