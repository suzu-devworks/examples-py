# examples-packaging-pipenv

## Setup

create a virtualenv in advance:

```shell
python -m venv .venv.pipenv
. .venv.pipenv/bin/activate

python -m pip install --upgrade pip
pip install pipenv
```

Here's how this project is setup:

```shell
cd src/examples-packaging-pipenv

pipenv install --dev
```

## Inisialize project

This project is initially generated with the following command:

```shell
cd examples-packaging-pipenv

# You need pyenv if you want other python versions.
# A virtual environment is not created because it was executed in venv.
pipenv --python 3.11

pipenv install --dev flake8 mypy black isort pytest-cov
```
