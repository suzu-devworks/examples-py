# poetry

> Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## References

- https://python-poetry.org/
- https://github.com/python-poetry/poetry

## Installation

### Using pip on venv

I installed it with pip and it seems fine.

```shell
pip install poetry
```

### Update poetry

Poetry itself can be updated:

```shell
poetry self update
```

## Usage

### Project setup

```shell
mkdir {project}
cd {project}

poetry new .

or

poetry init
```

`init` is generates `pyproject.toml`.  
`new` also creates an initial directories and files.

### Build package

`poetry-core` is python wheels are supported.

```shell
poetry build
```

## virtualenv

By default, Poetry creates a virtual environment in `{cache-dir}/virtualenvs`.  
however, Poetry will detect and respect an existing virtual environment that has been externally activated.

### Switch virtualenv

Here's how to activate your virtual environment:

```shell
poerty shell
```

## Tips

### Use a task runner like npm.

The `taskipy` is complementary task runner for python.

- https://github.com/taskipy/taskipy

To install taskipy as a dev dependency, simply run:

```shell
poetry add --group dev taskipy
```

In your pyproject.toml file, add a new section called `[tool.taskipy.tasks]`:

**pyproject.toml**

```toml
[tool.taskipy.tasks]
clean = "pyclean ."
test = "pytest"
```

To called a task, simply run:

```shell
poetry run task cleanshellshell

or

task clean
```

### Create the virtualenv inside the project’s root directory.

```shell
poetry config virtualenvs.in-project true
```

set configuration to `~/.config/pypoetry/config.toml`:

```toml
[virtualenvs]
in-project = true
```
