## examples-packaging-poetry

## Setup

## Initialize project

```shell
# virtualenv
python -m venv .venv.poetry
. .venv.poetry/bin/activate
cd src

python -m pip install --upgrade pip
pip install poetry

#　doesn't matter if the folder exists
poetry new examples-packaging-poetry
cd examples-packaging-poetry

poetry add --group dev flake8 mypy black isort pytest-cov pyclean
poetry add --group dev taskipy

poetry install

```
