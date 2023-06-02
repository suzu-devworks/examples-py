# examples-packaging-poetry

Examples of projects managed with Poetry

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
pip install poetry

```

Here's how this project is setup:

```shell
cd src/examples-packaging-poetry

# install dependencies and self.
poetry install

```

## Create project

This project was generated with the command:

```shell
mkdir -p src/amples-packaging-poetry
cd src/amples-packaging-poetry

#　doesn't matter if the folder exists
poetry new .
poetry add --group dev flake8 mypy black isort pytest-cov pyclean
poetry add --group dev taskipy

```
