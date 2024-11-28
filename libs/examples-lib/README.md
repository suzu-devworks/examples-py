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
- [functional programming](./tests/references/functionals/)
- [sorting](./tests/references/sorting/)
- [decorators](./tests/references/decorators/)
- [data models](./tests/references/data_models/)

## Standard library study

- [`datetime`](./tests/libraries/datetime/)
- [`NumPy`](./tests/libraries/numpy/)

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
