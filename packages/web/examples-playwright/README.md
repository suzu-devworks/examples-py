# examples-playwright

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
  - [Setup](#setup)
  - [Run tests](#run-tests)
- [Examples](#examples)

## Overview

This project is an example of end-to-end testing using Playwright.

- [Fast and reliable end-to-end testing for modern web apps | Playwright Python](https://playwright.dev/python/)
- [microsoft/playwright-python: Python version of the Playwright testing and automation library.](https://github.com/microsoft/playwright-python)

## Get started

### Setup

Get the dependent packages:

```shell
uv sync
```

Install the required browsers:

```shell
playwright install
```

### Run tests

```shell
pytest .
```

## Examples

- [Getting Started](./tests/playwright_getting_started/README.md)
- [Testing a self-hosted server](./tests/self_hosted_server_tests/)
