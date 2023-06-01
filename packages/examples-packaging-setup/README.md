# examples-packaging-setup

Examples of projects managed with setuptools.

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
pip install --upgrade setuptools wheel

```

Here's how this project is setup:

```shell
cd packages/examples-packaging-setup

# install dependencies and self.
pip install -e .[dev,doc]

```

## Create project

This project was generated with the command:


```shell
mkdir -p packages/examples-packaging-setup
cd packages/examples-packaging-setup
```

Create each of these files:

- [&#x2710; `setup.py` ...](./setup.py)
- [&#x2710; `setup.cfg` ...](./setup.cfg)
