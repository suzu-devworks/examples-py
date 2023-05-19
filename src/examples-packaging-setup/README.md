# examples-packaging-setup

## Setup

## Initialize project

Run the following command:

```shell
# virtualenv
python -m venv .venv.setup
. .venv.setup/bin/activate
cd src

python -m pip install --upgrade pip
pip install --upgrade setuptools wheel

mkdir examples-packaging-setup
cd examples-packaging-setup

```

Create each of these files:

- [setup.py ...](./setup.py)
- [setup.cfg ...](./setup.cfg)
