# examples-packaging-pdm

## Setup

create a virtualenv in advance:

```shell
python -m venv .venv.pdm
. .venv.pdm/bin/activate

python -m pip install --upgrade pip
pip install
```

Here's how this project is setup:

```shell
cd src/examples-packaging-pdm

pdm install
```

## Initialize project

This project is initially generated with the following command:

```shell
mkdir -p src/amples-packaging-pdm
cd src/amples-packaging-pdm

# create new pyproject.toml
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean
```
