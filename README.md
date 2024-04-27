# examples-py

Workspace for studying Python programming.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)


## What is this

This repository is the author's personal playground to learn Python and experiment with its features.
This might be helpful for developers having the same problem.

However, please note that the code described here is based on my personal opinion and may contain many inaccuracies.


## More Information

- [Documentation](./docs/README.md)


## Build all projects

Clone project:

```shell
git clone https://github.com/suzu-devworks/examples-py.git
cd examples-py
```

> If you use DevContainers, switch to containers now.

Install the package manager:

```shell
pip install --user pdm
```

Create a new virtual environment:

```shell
python -m venv .venv
. .venv/bin/activate

pip install --upgrade pip
```

Build the top-level project:

```shell
pdm run build
```
