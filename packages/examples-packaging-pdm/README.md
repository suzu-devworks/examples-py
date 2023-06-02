# examples-packaging-pdm

Examples of projects managed with PDM.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

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
pip install pdm

```

Here's how this project is setup:

```shell
cd packages/examples-packaging-pdm

# select interpreter
pdm use

# install dependencies and self.
pdm install

```

## Create project

This project was generated with the command:

```shell
mkdir -p packages/examples-packaging-pdm
cd packages/examples-packaging-pdm

# create new pyproject.toml
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean

```
