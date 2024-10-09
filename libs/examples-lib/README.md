# examples-lib

This is a project to learn the basic functions and usage of Python.

## Table of Contents <!-- omit in toc -->

- [examples-lib](#examples-lib)
  - [Language reference](#language-reference)
  - [Standard library study](#standard-library-study)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## Language reference

- [sequences](./tests/references/sequences/)
  > Learn about basic sequence type operations.
- [functional programming](./tests/references/functionals/)
  > Learn about functional programming.
- [sorting](./tests/references/sorting/)
  > Learn about different sorts.
- [decorators](./tests/references/decorators/)
  > Learn how to define and use decorators.
- [data models](./tests/references/data_models/)
  > Learn data models using special methods in Python.

## Standard library study

- [`datetime`](./tests/libraries/datetime/)
  > Learn how to work with dates with datetime and timezone.
- [`NumPy`](./tests/libraries/numpy/)
  > NumPy provides support for typed multidimensional arrays for efficient numerical computation and a large library of high-level mathematical functions to manipulate them.

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
