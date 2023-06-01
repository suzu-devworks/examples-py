## examples-packaging-poetry

## Setup

create a virtualenv in advance:

```shell
python -m venv .venv.poetry
. .venv.poetry/bin/activate

python -m pip install --upgrade pip
pip install poetry
```

Here's how this project is setup:

```shell
cd src/examples-packaging-poetry

poetry install
```

## Initialize project

This project is initially generated with the following command:

```shell
mkdir -p src/amples-packaging-poetry
cd src/amples-packaging-poetry

#　doesn't matter if the folder exists
poetry new .
poetry add --group dev flake8 mypy black isort pytest-cov pyclean
poetry add --group dev taskipy
```
