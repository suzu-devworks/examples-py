# example-py

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This is a project to learn the basic functions and usage of Python.


## Table of Contents <!-- omit in toc -->

- [example-py](#example-py)
  - [Getting Started](#getting-started)
  - [Standard Library study](#standard-library-study)
  - [Other Libraries study](#other-libraries-study)
  - [How the project was initialized](#how-the-project-was-initialized)


## Getting Started  

Install dependency packages and install myself locally as editable.

```shell
pdm install
```

Executes commands defined in `project.scripts`.

```shell
examples-cli --version
```


## Standard Library study

- [`datetime`](./tests/libraries/datetimes/)
  > Learn how to work with dates with datetime and timezone.
- [`logging`](./src/examples/libraries/logging/)
  > Learn log output and settings with console app.
- [`argparse`](./src/examples/libraries/argparse/)
  > Learn how to define and handle command-line arguments using a console app.


## Other Libraries study

- ['pillow'](./src/examples/libraries/pillow/)
  > Learn how to use Pillow in a console app to manipulate images and exif information.

<!-- spell-checker:words argparse -->


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init -n --dist -p src/examples-py
pdm add -e src/examples-py --dev --group src

cd src/examples-py
pdm add --dev flake8 mypy black isort pytest-cov pyclean
pdm add pyyaml pillow
pdm add --dev --group test pytz
pdm add --dev types-pytz types-PyYAML types-Pillow
```

<!-- spell-checker:words pyyaml -->
