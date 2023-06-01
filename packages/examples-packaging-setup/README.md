# examples-packaging-setup

## Setup

create a virtualenv in advance:

```shell
python -m venv .venv.setup
. .venv.setup/bin/activate

python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
```

Here's how this project is setup:

```shell
cd packages/examples-packaging-setup

pip install -e .[dev,doc]
```

## Create project

This project is initially generated with the following command:

```shell
mkdir -p packages/examples-packaging-setup
cd packages/examples-packaging-setup
```

Create each of these files:

- [setup.py ...](./setup.py)
- [setup.cfg ...](./setup.cfg)
