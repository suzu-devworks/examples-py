# examples-lib

This is a project to learn the basic functions and usage of Python.

## Table of Contents <!-- omit in toc -->

- [examples-lib](#examples-lib)
  - [Language reference](#language-reference)
  - [Standard library study](#standard-library-study)
  - [Third party library study](#third-party-library-study)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

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
rye init libs/examples-lib
cd libs/examples-lib
rye add --dev pytest-cov pytest-asyncio 
rye add pytz natsort numpy
rye add --dev types-pytz
```
