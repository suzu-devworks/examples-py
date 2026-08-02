
# examples-py

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fsuzu-devworks%2Fexamples-py%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)
[![CI](https://github.com/suzu-devworks/examples-py/actions/workflows/py-ci.yaml/badge.svg)](https://github.com/suzu-devworks/examples-py/actions/workflows/py-ci.yaml)
[![CodeQL](https://github.com/suzu-devworks/examples-py/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/suzu-devworks/examples-py/actions/workflows/github-code-scanning/codeql)

## What is the purpose of this repository?

This repository is just my personal playground for learning and experimenting with Python Programming.

The content here might actually be helpful to other developers facing similar issues.

However, please keep in mind that this code is based solely on my own perspective and probably has lots of inaccurate
or questionable parts!

## What topics are covered?

This includes a wide variety of projects.

- [Fundamentals](./packages/fundamentals/)\
  Basic features of the Python programming language and examples using the standard library.

- [Networking](./packages/networking/)\
  Programming examples related to network communication.

- [Web Development](./packages/web/)\
  Examples of web application implementation using various Python frameworks.

## What should I prepare before development?

This repository provides multiple development container environments. Please select the libraries,
services, and databases you wish to use.

- [Python (uv)](./.devcontainer/): It is used in standard Python development
- [Python (uv with OpenCV)](./.devcontainer/cv2/): Adding OpenCV library for image processing and computer vision tasks
- [Python (uv with Web)](./.devcontainer/web/): The NGINX reverse proxy is started. Configurations
  for SSL certificates are also already set up.
