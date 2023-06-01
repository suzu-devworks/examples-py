# examples-py

Python programming examples.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Setup

Clone the repository:

```shell
clone https://github.com/suzu-devworks/examples-py.git

cd examples-py

```

Create a virtualenv in advance:

```shell
python -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
pip install pdm

```

Here's how this project is setup:

```shell
cd src/examples-py

# select interpreter
pdm use

# install dependencies and self.
pdm install

```

## Create project

This project was generated with the command:

```shell
mkdir -p src/examples-py
cd src/examples-py

# create new pyproject.toml (in setuptools)
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean
pdm add -dG test pytz pyyaml natsort

pdm add pillow

```
