# example-py

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This is a project to learn the basic functions and usage of Python.

## Table of Contents <!-- omit in toc -->

- [example-py](#example-py)
  - [Standard Library study](#standard-library-study)
  - [How the project was initialized](#how-the-project-was-initialized)


## Standard Library study

- [`datetime`](./tests/standards/datetimes/)  
Learn how to work with dates with datetime and timezone.


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init -n --dist -p src/examples-py
pdm add -e src/examples-py --dev --group src

cd src/examples-py
pdm add -d flake8 mypy black isort pytest-cov pyclean
```
