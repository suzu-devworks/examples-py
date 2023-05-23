# pip

> Pip is a package-management system written in Python and is used to install and manage software packages.[

## References

- https://pip.pypa.io/en/stable/
- https://github.com/pypa/pip

## Tips

### Write `requirements.txt`

```shell
pip freeze > requirements.txt
```

### Install the current project for development

Install a project in editable mode:

```shell
pip install -e .
```

> -e, --editable <path/url>

Uninstall is:

```shell
pip uninstall .
```

### build package

```shell
python -m build
```

```console
(PY3.9.1) % ls -1 dist
hellosetuptools-0.0.1.dev0-py3-none-any.whl
hellosetuptools-0.0.1.dev0.tar.gz
```
