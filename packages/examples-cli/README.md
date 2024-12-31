# examples-cli

This is a project to learn the basic functions and usage of Python.

## Table of Contents <!-- omit in toc -->

- [examples-cli](#examples-cli)
  - [Getting Started](#getting-started)
  - [Standard library study](#standard-library-study)
  - [Other libraries study](#other-libraries-study)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## Getting Started  

Install dependency packages:

```shell
uv sync
```

Executes command defined in `project.scripts`:

```shell
examples-cli --version
```

## Standard library study

- [`logging`](./src/examples_cli/libraries/logging/)
  > Learn log output and settings with console app.
- [`argparse`](./src/examples_cli/libraries/argparse/)
  > Learn how to define and handle command-line arguments using a console app.

## Other libraries study

- [`pillow`](./src/examples_cli/libraries/pillow/)
  > Learn how to use Pillow in a console app to manipulate images and exif information.

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --package packages/examples-cli
uv add --project packages/examples-cli pyyaml pillow
uv add --project packages/examples-cli --dev types-PyYAML types-Pillow
uv add --project packages/examples-cli examples-lib
```
