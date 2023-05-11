# pipenv

> Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, pyenv and virtualenv.

It's a combination of pip and venv. conda?

## References

- https://pipenv.pypa.io/en/latest/
- https://github.com/pypa/pipenv

## Installation

### Using pip on venv

```shell
pip install pipenv
```

## Usage

### Create new virtualenv

```shell
pipenv --python {py-version}
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

If you specify a version that is not installed, it will work with pyenv.

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

### Delete virtualenv

```shell
pipenv --rm
```

```console
$ pipenv --rm
Removing virtualenv (/home/xxxxxx/.local/share/virtualenvs/test-pipenv-f7l9kGAQ)…
```

### Switch virtualenv

```shell
pipenv shell
```

```console
$ pipenv shell

Launching subshell in virtual environment…
 . /home/akira/.local/share/virtualenvs/test-pipenv-f7l9kGAQ/bin/activate

(test-pipenv) $ python --version

Python 3.6.12

(test-pipenv) $ exit
$

```

### Add Packages

Adding a package makes an entry in the `Pipfile`.

```shell
pipenv install {package}
pipenv install --dev {package}
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

### Update Packages

```shell
$ pipenv update {package}
$ pipenv update --outdated
```

### Restore Packages

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

### Clean Packages

```shell
pipenv clean
```

### List Packages

Tree display of dependencies:

```shell
pipenv graph
```

## Tips

### Read environment file

If you prepare a `.env` file in the project folder, it seems to be automatically loaded when pipenv shell or pipenv run.

`.env`:

```ini
DEBUG=1
```

```console
$ pipenv run python
>>> import os
>>> os.environ['DEBUG']
'1'
```

### Task runner

`Pipfile`:

```ini
[scripts]
start = "python main.py runserver"
test = "python -m unittest discover -v"
format = "autopep8 -ivr ."
lint = "flake8 --show-source ."
```

```console
$ pipenv run start
```

### Where you placed the site-package modules?

```shell
pipenv --venv
```
