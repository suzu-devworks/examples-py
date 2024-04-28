# pipenv

> Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, pyenv and virtualenv.

It's a combination of pip and venv. conda?  
Can't you make a wheel package?

## Table of Contents <!-- omit in toc -->

- [pipenv](#pipenv)
  - [References](#references)
  - [Installation](#installation)
    - [Using pip on venv](#using-pip-on-venv)
  - [Project management](#project-management)
    - [Project setup and create virtualenv](#project-setup-and-create-virtualenv)
    - [Remove the virtualenv](#remove-the-virtualenv)
    - [Spawns a shell within the virtualenv](#spawns-a-shell-within-the-virtualenv)
    - [Spawns a command installed into the virtualenv](#spawns-a-command-installed-into-the-virtualenv)
    - [Restore packages](#restore-packages)
    - [Install packages](#install-packages)
    - [Update packages](#update-packages)
    - [Uninstall packages](#uninstall-packages)
    - [Uninstall all packages](#uninstall-all-packages)
    - [List packages](#list-packages)
    - [Build wheel package](#build-wheel-package)
  - [Tips](#tips)
    - [Custom Script Shortcuts](#custom-script-shortcuts)
    - [Where you placed the site-package modules?](#where-you-placed-the-site-package-modules)
    - [Read environment file](#read-environment-file)
  - [Provide Console Scripts](#provide-console-scripts)
    - [Create entry point](#create-entry-point)


## References

- https://pipenv.pypa.io/en/latest/
- https://github.com/pypa/pipenv


## Installation

### Using pip on venv

```shell
pip install pipenv
```

## Project management

### Project setup and create virtualenv

Generate a Pipfile with the following command:

```shell
pipenv --python {py-version}
```

Enable environment variables if you want a virtual environment in your project folder.

```shell
export PIPENV_VENV_IN_PROJECT=true
```

```console
$ pipenv --python 3.8

Creating a virtualenv for this project…
Pipfile: /home/xxxxxx/workspaces/databases/test-pipenv/Pipfile
...

✔ Successfully created virtual environment!
Virtualenv location: /home/xxxxxx/.local/share/virtualenvs/test-pipenv-f7l9kGAQ
Creating a Pipfile for this project…
```

If you specify a version that is not installed, it will work with `pyenv`.

```console
$ pipenv --python 3.6

Warning: Python 3.6 was not found on your system…
Would you like us to install CPython 3.6.12 with Pyenv? [Y/n]: y

Installing CPython 3.6.12 with /home/xxxxxx/.anyenv/envs/pyenv/bin/pyenv (this may take a few minutes)…
✔ Success!
Downloading Python-3.6.12.tar.xz...
-> https://www.python.org/ftp/python/3.6.12/Python-3.6.12.tar.xz
Installing Python-3.6.12...
Installed Python-3.6.12 to /home/xxxxxx/.anyenv/envs/pyenv/versions/3.6.12


Creating a virtualenv for this project…
Pipfile: /home/xxxxxx/workspaces/databases/test-pipenv/Pipfile
...

✔ Successfully created virtual environment!
Virtualenv location: /home/xxxxxx/.local/share/virtualenvs/test-pipenv-f7l9kGAQ
Creating a Pipfile for this project…

```

When the pipenv environment is built with the virtual environment enabled:

```
$ pipenv --python 3.11

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Creating a Pipfile for this project...
```

### Remove the virtualenv

```shell
pipenv --rm
```

```console
$ pipenv --rm
Removing virtualenv (/home/xxxxxx/.local/share/virtualenvs/test-pipenv-f7l9kGAQ)…
```

### Spawns a shell within the virtualenv

```shell
pipenv shell
```

```console
$ pipenv shell

Launching subshell in virtual environment…
 . /home/xxxxxx/.local/share/virtualenvs/test-pipenv-f7l9kGAQ/bin/activate

(test-pipenv) $ python --version

Python 3.6.12

(test-pipenv) $ exit

```

### Spawns a command installed into the virtualenv

```shell
pipenv run {command}
```

### Restore packages

from `Pipfile`

```shell
pipenv install
pipenv install --dev
```

from `Pipfile.lock`

```shell
pipenv sync
pipenv sync --dev
```

from `requirements.txt`

```shell
pipenv install -r ./requirements.txt
```

### Install packages

Adding a package makes an entry in the `Pipfile`.

```shell
pipenv install {packages...}
pipenv install --dev {packages...}
```

```console
(test-pipenv) $ pipenv install numpy

Installing numpy…
Adding numpy to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Building requirements...
Resolving dependencies...
✔ Success!
Updated Pipfile.lock (2cfc5e)!
Installing dependencies from Pipfile.lock (2cfc5e)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
```

### Update packages

Runs lock, then sync.

```shell
pipenv update {packages...}
pipenv update --outdated
pipenv update
```

### Uninstall packages

Un-installs a provided package and removes it from `Pipfile`.

```shell
pipenv uninstall {packages...}
```

### Uninstall all packages

Uninstalls all packages not specified in `Pipfile.lock`.

```shell
pipenv clean
```

### List packages

Tree display of dependencies:

```shell
pipenv graph
```

### Build wheel package

**`pipenv` does not provide package creation. You need to use another tool such as `setuptools`.**



## Tips

### Custom Script Shortcuts

**`Pipfile`**:

```ini
[scripts]
format = "black -l 119 ."
lint = "flake8 --show-source ."
start = "python main.py runserver"
test = "pytest"
```

```console
$ pipenv run start
```

### Where you placed the site-package modules?

```shell
pipenv --venv
```

### Read environment file

If you prepare a `.env` file in the project folder, it seems to be automatically loaded when pipenv shell or pipenv run.

Write `.env` file:

```ini
DEBUG=1
```

Try running it:

```console
$ pipenv run python
>>> import os
>>> os.environ['DEBUG']
'1'
```


## Provide Console Scripts

`pipenv` cannot create packages and therefore cannot convert packages to commands, but you can define Python commands using custom script shortcuts.

### Create entry point

Create `console/command.py` file:

```py
import sys


def main():
    print("Hello pipenv.")


if __name__ == "__main__":
    sys.exit(main())

```

 `Pipfile` will look like this:

```ini
[scripts]
start = "python src/examples_packaging_pipenv/console/command.py"
```

When you run it:

```console
$ pipenv run start

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Hello pipenv.
```

It's a warning but I don't care.
