# Getting Started - Playwright for Python

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Installation](#installation)
- [Writing tests](#writing-tests)
- [Generating tests](#generating-tests)
  - [Running Codegen](#running-codegen)
  - [Recording a test](#recording-a-test)
  - [Generating locators](#generating-locators)
- [Running and debugging tests](#running-and-debugging-tests)
  - [Debugging tests](#debugging-tests)
- [Trace viewer](#trace-viewer)
- [Setting up CI](#setting-up-ci)
- [Pytest Plugin Reference](#pytest-plugin-reference)

## Overview

Try Getting Started on the official website.

- [Installation | Playwright Python](https://playwright.dev/python/docs/intro)

## Installation

Install the Pytest plugin:

```shell
pip install pytest-playwright
```

Install the required browsers:

```shell
playwright install
```

Browser and OS dependencies are installed with one command:

```shell
playwright install --with-deps chromium
```

See all supported browsers:

```shell
playwright install --help
```

## Writing tests

- [See...](./_02_writing_tests/)

## Generating tests

### Running Codegen

```shell
playwright codegen demo.playwright.dev/todomvc
```
<!-- spell-checker: words codegen todomvc -->

For Mac, you need [XQuartz](https://www.xquartz.org/)

### Recording a test

1. Change the target in the Playwright inspector to `Pytest`
2. Actions like click or fill by simply interacting with the page
3. Assertions by clicking on one of the icons in the toolbar and then clicking on an element on the page to assert against
4. When you have finished interacting with the page, press the 'record' button to stop
5. Use the 'copy' button to copy the generated code to your editor
6. Use the clear button to clear the code to start recording again
7. Once finished, close the Playwright inspector window or stop the terminal command

### Generating locators

1. Press the 'Record' button to stop the recording
2. Click on the 'Pick Locator' button and then hover over elements in the browser window
  to see the locator highlighted underneath each element
3. Click on an element will display the element's locator in the Locator window
4. Use the copy button to copy the locator and paste it into your code

## Running and debugging tests

### Debugging tests

```shell
PWDEBUG=1 pytest -s test_example.py
```
<!-- spell-checker: words PWDEBUG -->

## Trace viewer

Recording a trace:

```shell
pytest --tracing on
```

This will record the trace and place it into the file named `trace.zip` in your test-results directory.

Opening the trace:

```shell
playwright show-trace trace.zip
```

## Setting up CI

- [See playwright.yml](../../../../.github/workflows/playwright.yml)

## Pytest Plugin Reference

- [See...](./_07_pytest_plugin_reference/)
