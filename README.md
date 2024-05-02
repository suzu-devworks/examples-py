# examples-py

Workspace for studying Python programming.

## What is this

This repository is the author's personal playground to learn Python and experiment with its features.
This might be helpful for developers having the same problem.

However, please note that the code described here is based on my personal opinion and may contain many inaccuracies.


## Projects

- [examples-py](./src/examples-py/README.md)
- packages
  - [examples-packaging-setup](./src/packages/examples-packaging-setup/README.md)
  - [examples-packaging-pipenv](./src/packages/examples-packaging-pipenv/README.md)
  - [examples-packaging-poetry](./src/packages/examples-packaging-poetry/README.md)
  - [examples-packaging-pdm](./src//packages//examples-packaging-pdm/README.md)


## More Information

- [Documentation](./docs/README.md)


## Build all projects

```shell
git clone https://github.com/suzu-devworks/examples-py.git
cd examples-py

python -m venv .venv
. .venv/bin/activate

pip install --upgrade pip
pip install pdm

pdm run build
```

<!-- // spell-checker:words setuptools -->
<!-- // spell-checker:words pipenv -->
