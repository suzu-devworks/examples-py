# examples-packaging-pipenv

## Overview 

This is a project to learn packaging using pipenv.


## Table of Contents <!-- omit in toc -->

- [examples-packaging-pipenv](#examples-packaging-pipenv)
  - [Overview](#overview)
  - [Getting started](#getting-started)
  - [More Information](#more-information)
  - [How the project was initialized](#how-the-project-was-initialized)
    - [Create project directories](#create-project-directories)
    - [Generate `Pipfile` file](#generate-pipfile-file)
    - [Generate source directories](#generate-source-directories)
    - [Install packages](#install-packages)


## Getting started

If you don't want to pollute the environment, have a separate venv:

```shell
python -m venv .venv.pipenv
. .venv.pipenv/bin/activate
```

After updating pip, install the package manager:

```shell
python -m pip install --upgrade pip
pip install pipenv
```

Move to the root of your project...

```shell
cd packages/examples-packaging-pipenv
```

When you run it:

```console
$ pipenv run start

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Hello pipenv.
```

It's a warning but I don't care.


## More Information

- [docs/packages/pipenv](/docs/packages/pipenv.md)


## How the project was initialized

### Create project directories

Create and move project folder:

```shell
mkdir -p packages/examples-packaging-pipenv
cd packages/examples-packaging-pipenv
```

### Generate `Pipfile` file

Generate a `Pipfile` with the following command:

```shell
# You need pyenv if you want other python versions.
# A virtual environment is not created because it was executed in venv.
pipenv --python 3.11
export PIPENV_VENV_IN_PROJECT=true
```

### Generate source directories

Generate the initial directory for the package with the following command:

```shell
mkdir -p src/examples_packaging_setup/
touch src/examples_packaging_setup/__init__.py
```

The final directory will look like this:

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── src
    └── examples_packaging_pipenv
        └── __init__.py
```

### Install packages

Install dependency packages for this project:

```shell
pipenv install --dev flake8 mypy black isort pytest-cov
```
