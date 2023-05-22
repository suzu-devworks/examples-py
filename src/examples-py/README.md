# examples-py

## Setups

```shell
clone https://github.com/suzu-devworks/examples-py.git

cd examples-py
cd src/examples-py

pdm use
pdm install

```

## Create projects

```shell
# create virtual environment
python -m venv .venv
. .venv/bin/activate

# upgrade base packages.
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools

# add Package manager(PDM).
pip install pdm

mkdir -p src/examples-py
cd src/examples-py

# create new pyproject.toml (in setuptools)
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean

```
