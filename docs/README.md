# docs

## Development

### How the workspace was initialized

create `pyproject.toml` file and directory:

```shell
rye init .
```

Add lines `pyproject.toml`:

```toml
[tool.rye]
dev-dependencies = []
managed = true
virtual = true

[tool.rye.workspace]
members = ["apps/*", "libs/*"]
```

Add development tools:

```shell
rye add -d ruff mypy pyclean
```
