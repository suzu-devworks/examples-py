# examples-lib

This is a project to learn the basic functions and usage of Python.

## Table of Contents <!-- omit in toc -->

- [Getting Started](#getting-started)
- [Language reference](#language-reference)
- [Standard library study](#standard-library-study)
- [Third party library study](#third-party-library-study)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Getting Started  

Install dependency packages:

```shell
uv sync
```

Run test:

```shell
uv run --directory packages/examples-lib pytest 
```

## Language reference

- [sequences](./tests/references/sequences/)
  > *Learn about basic sequence type operations in Python.*
- [functional programming](./tests/references/functionals/)
  > *Learn about functional programming in Python.*
- [sorting](./tests/references/sorting/)
  > *Learn how to sort a list in Python.*
- [decorators](./tests/references/decorators/)
  > *Learn the definition and usage of decorators in Python.*
- [data models](./tests/references/data_models/)
  > *Learn how to define data models using special methods in Python.*

## Standard library study

- [`datetime`](./tests/libraries/datetime/)
  > The datetime module supplies classes for manipulating dates and times.

## Third party library study

- [`NumPy`](./tests/libraries/numpy/)
  >　NumPy is a library that adds support for large multidimensional arrays and matrices, and a large collection of advanced mathematical functions for manipulating these arrays.

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-lib
uv add --project packages/examples-lib --dev pytest pytest-cov pytest-asyncio 
uv add --project packages/examples-lib pytz natsort numpy
uv add --project packages/examples-lib --dev types-pytz
```
