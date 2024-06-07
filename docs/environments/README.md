# Environments

## Table of Contents <!-- omit in toc -->

- [Environments](#environments)
  - [Flake8](#flake8)
  - [black](#black)
  - [isort](#isort)
  - [mypy](#mypy)

## Flake8

> Your Tool For Style Guide Enforcement.

- https://flake8.pycqa.org/en/latest/

Flake8 supports storing its configuration in your project in one of `setup.cfg`, `tox.ini`, or `.flake8`.

```ini
[flake8]
ignore = E203, W503
max-line-length = 119
```

- ignore:
  - [Whitespace before ':' (E203)](https://www.flake8rules.com/rules/E203.html)<br/>
    This is an item that causes an error when there is a space before the `:` specified for an indented block, but ternary operators and array slices also cause errors, so they are excluded.
 
  - [Line break occurred before a binary operator (W503)](https://www.flake8rules.com/rules/W503.html)<br/>
  The line break rules for binary operators are defined as both a line break before the operator (W503) and a line break after the operator (W504), so exclude one of them according to the rules defined in the project.

- max-line-length:
  - PEP8 states that it has 79 characters. Flake8 defaults to this value.
  - The Black formatter seems to default to 88 characters.
  - VSCode's default seems to be 120 characters.
  - On Github, it seems that it is common to see projects that limit the length to 119 characters, taking into account the character width of code reviews.


## black

> The uncompromising code formatter.
>> “Any color you like.”

- https://black.readthedocs.io/en/stable/

By default Black looks for `pyproject.toml` containing a `[tool.black]` section starting from the common base directory of all files and directories passed on the command line.

```ini
[tool.black]
line-length = 119
```

If `--exclude` is not set, Black will automatically ignore files and directories in `.gitignore` file(s).


## isort

> isort your imports, so you don't have to.

- https://pycqa.github.io/isort/

isort searches for the closest supported configuration file in the order listed below.

1. `[settings]` in `.isort.cfg` [preferred format]
2. `[tool.isort]` in `pyproject.toml` [preferred format]
3. `[isort]` in `setup.cfg`
4. `[isort]` in `tox.ini`
5. `.editorconfig`

```ini
[tool.isort]
profile = "black"
src_paths = ["src", "tests"]
#
known_first_party = ["examples"]
```

- `known_first_party`<br>
  Force isort to recognize a module as being part of the current python project.


## mypy

> Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing

- https://www.mypy-lang.org/

Mypy supports reading configuration settings from a file with the following precedence order:

1. `./mypy.ini`
2. `./.mypy.ini`
3. `./pyproject.toml`
4. `./setup.cfg`
5. `$XDG_CONFIG_HOME/mypy/config`
6. `~/.config/mypy/config`
7. `~/.mypy.ini`

```ini
[mypy]
## Import discovery
files = []

## Platform configuration
python_version = 3.12

## Disallow dynamic typing
disallow_subclassing_any = true

## Untyped definitions and call
disallow_incomplete_defs = true
disallow_untyped_calls = true
disallow_untyped_decorators = true
disallow_untyped_defs = true

## None and Optional handling
no_implicit_optional = true
strict_optional = true

## Configuring warnings
#warn_unreachable = true
warn_redundant_casts = true
warn_return_any = true
warn_unused_configs = true
warn_unused_ignores = true

## Suppressing errors

## Miscellaneous strictness flags
#no_implicit_reexport = true
allow_redefinition = true
local_partial_types = true
strict = true
strict_equality = true

## Configuring error messages
pretty = true
show_error_context = true

[[mypy.overrides]]
ignore_missing_imports = true
module = []
```

- `strict = true`<br>
  Enable all optional error checking flags. You can see the list of flags enabled by strict mode in the full `mypy --help` output.
